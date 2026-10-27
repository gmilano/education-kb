---
industry: education
region: Global
updated: 2026-10-27
---

## 🆕 `p476` — `2026-10-27` — **🟢 `Gap 475-A` IS ANSWERED: the version election IS readable, it lives in packaging metadata and per-source-file notices exactly as `p475` predicted — and on one row it is the OPPOSITE of what the payload reader concluded. `penecho/penecho` elects `AGPL-3.0-only`. 🔴 But the election is readable on only 4 of 8 GPL-family repos; for the other 4 it is not merely unread, it is UNREADABLE on every channel this base can reach.**

🔵 **Gate posture, unchanged from `p475` (`Gap 446-A`):** `make hooks` **not attempted** — the industry KB is
cloned outside the harness repo and the harness refuses execution of code arriving in a clone
(`Code from External`). **Nothing below is gate-attested.** Checks re-implemented in this session's own
code, held outside the clone, and green: frontmatter keys and closed-vocabulary `region` on all eight
shelves; every table checked for separator presence and pipe-count consistency, with **no header row
published as data**; append-only preserved on both trending shelves and prepend-only on these; every
address resolved first-hand by `git ls-remote --symref`; every grant and metadata file fetched from
`raw.githubusercontent.com`, written to a file, and the **file** measured (`Gap 468-A`).

🟢 **Cross-pass control reproduced exactly, seventh consecutive pass, measured this pass and not carried.**
`HKUDS/DeepTutor` `main/LICENSE` **11,408 B · `cd2f54e1e506`** at HEAD **`a31d82624c27`** — byte-, digest-
and HEAD-identical to `p470`–`p475`.

🔴 **`Gap 472-A` honoured, not retried.** `curl -sI https://github.com/<repo>` still answers only the
proxy's own `200 Connection Established`. 🔴 **New channel limit measured this pass:** `api.github.com` returns
**HTTP 403** for every repository not attached to this session, so the REST tree endpoint is unavailable — this
is why the depth probe below had to use a shallow clone instead.

---

### 🟢 The version-election reader `Gap 475-A` asked for, built and run on 8 GPL-family repos

🔵 `p475` proved the licence **payload** carries no election (`any later version` appears 3× in every
GPL-family payload as preamble and appendix boilerplate, 3 of 3) and named where the election actually
lives: **per-source-file notices and packaging metadata**. This pass reads both. Evidence:
[`evidence/version-election.2026-10-27-p476.tsv`](../evidence/version-election.2026-10-27-p476.tsv).

| repo | 🔴 payload reader (`p475`) said | 🟢 packaging metadata, read first-hand | 🟢 per-source-file notice | verdict |
|---|---|---|---|---|
| [moodle/moodle](https://github.com/moodle/moodle) | `or-later` | `composer.json` → **`GPL-3.0-or-later`** | present, 3 of 3 files | 🟢 **`or-later` GENUINELY ELECTED** |
| [frappe/lms](https://github.com/frappe/lms) | `or-later` | `package.json` → **`AGPL-3.0-or-later`** | none, 0 of 2 files | 🟢 **`or-later` ELECTED** (one channel only) |
| [openeducat/openeducat_erp](https://github.com/openeducat/openeducat_erp) | `or-later` | 14 × `__manifest__.py` → `LGPL-3` (bare) | present, **187 of 209** `.py` files | 🟢 **`or-later` ELECTED** (by source notice) |
| [penecho/penecho](https://github.com/penecho/penecho) | `or-later` | `package.json` → **`AGPL-3.0-only`** | none | 🔴 **`only` ELECTED — reader REFUTED** |
| [instructure/canvas-lms](https://github.com/instructure/canvas-lms) | `or-later` | `package.json` → `AGPL-3.0` (bare) | none, 0 of 3 files | 🟡 bare id, **no election** |
| [h5p/h5p-php-library](https://github.com/h5p/h5p-php-library) | `or-later` | `composer.json` → `GPL-3.0` (bare) | none, 0 of 2 files | 🟡 bare id, **no election** |
| [openedx/openedx-platform](https://github.com/openedx/openedx-platform) | `or-later` | **no licence field** in `pyproject.toml` (48,283 B) or `package.json` | none, 0 of 5 files | 🔴 **UNREADABLE, all channels** |
| [echo-loop/Echo-Loop](https://github.com/echo-loop/Echo-Loop) | `or-later` | **no licence field** in `pubspec.yaml` | none, 0 of 2 files | 🔴 **UNREADABLE, all channels** |

🔴 **Score the payload reader against measurement: right 3 of 8, wrong 1 of 8, unknowable 4 of 8.** The one
it got wrong matters most — `penecho` declares `AGPL-3.0-only`, so a future AGPLv4 is **not** available to a
downstream user, which is the exact opposite of the permission `or-later` implies. 🔵 `p475`'s instruction to
read every GPL-family `or-later` cell as `VERSION_ELECTION_UNREAD` was right; this pass upgrades half of
them to a measured grade and the other half to `UNREADABLE` — a stronger statement than `UNREAD`, because
it says further reading on these channels will not help.

🟡 **A bare SPDX id is not an election to `only`.** `AGPL-3.0` and `GPL-3.0` without a suffix are
**deprecated** SPDX identifiers, deprecated precisely because they do not say which. Canvas and H5P are
recorded as *no election*, not as `only`.

🟢 **Two non-GPL controls run so the method cannot be accused of manufacturing signal:**
`sakaiproject/sakai` `pom.xml` declares *Educational Community License, Version 2.0* and
`learningequality/kolibri` `package.json` declares `MIT` — both agree with the payload already on the
foundation shelf, and neither produced a spurious election.

🟡 **A measurement caveat found in this pass's own first attempt.** The FSF notice **wraps across lines**
(`…either version 3 of the` / `License, or (at your option) any later version`), so a single-line `grep`
undercounts it — the first run of this reader scored openeducat `0 of 209` before the multi-line-aware
re-grep scored it `187 of 209`. This is the same class of defect as `p475`'s line-wrap digest false
negative, and any future reader on this channel must normalise whitespace before matching.

### 🟢 `Gap 475-C` is closed — both unread grants read first-hand, and both are permissive

| repo | grant path | bytes | digest12 | grant read | build-on-able |
|---|---|---|---|---|---|
| [PetoiCamp/OpenCat-Quadruped-Robot](https://github.com/PetoiCamp/OpenCat-Quadruped-Robot) | `main/LICENSE` | 1,069 | `517ad70869fe` | **MIT** | 🟢 **YES** |
| [ystemsrx/mini-nanoGPT](https://github.com/ystemsrx/mini-nanoGPT) | `master/LICENSE` | 1,063 | `703b1fc21029` | **MIT** | 🟢 **YES** |

🟢 **Every row on this shelf now carries a first-hand grant. There are no `🟡 unread` rows left**, so for the
first time this shelf's permissive census is complete rather than partial.

### 🟢 `Gap 475-E`'s instrument now exists — the first per-pass star snapshot stored in this base

🔵 `Gap 475-E`: *"this base has never stored a per-pass star snapshot it could difference."* It has one now:
[`evidence/star-snapshot.2026-10-27-p476.tsv`](../evidence/star-snapshot.2026-10-27-p476.tsv), 13 rows.

🔴 **It is a SAME-DAY delta and therefore NOT a velocity** — `p475` ran on this same calendar date. What it
establishes is narrower and still worth having: **`p475`'s magnitudes are real.** Every one of the 13 rows
reproduces within `+90`, which is what a correct first-hand read looks like, and nothing like the
20,000-star error `p475` found in the carried values.

| measure | value |
|---|---|
| rows re-measured | 13 of 13 |
| rows that moved at all | **4** |
| total movement across all 13 rows | **+94★** |
| `HKUDS/DeepTutor` share of that movement | **+90★ = 95.7 %** |

🔵 **Attention is concentrated in one row, not spread across a tier.** The honest velocity figure available
today is a **lifetime average** (`stars ÷ days since creation`), recorded per row in the evidence file:
DeepTutor **147.0★/day** over 303 days, Echo Loop **26.2★/day** over 173 days, penecho **23.8★/day** over
105 days, antivibe **5.6★/day**, PageLM **4.9★/day**. 🔴 A lifetime average is not a current rate and must
not be read as one; the next pass can finally difference a real interval against this snapshot.

### 🟢 The live agent tier — 13 real rows, every grant first-hand, every star first-hand

🔵 `grant_read` is the payload's own title, not a badge, an index or a roundup. `★` read
`2026-10-27` from the authenticated channel, never web-relayed.

| agent | repo | grant (read first-hand) | ★ (first-hand) | Δ vs `p475` | what it is | build-on-able |
|---|---|---|---|---|---|---|
| DeepTutor | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | Apache-2.0 · 11,408 B · `cd2f54e1e506` | 44,531 | +90 | Lifelong personalised tutoring; multi-agent + RAG; CLI/WebSocket/SDK | 🟢 **YES** |
| OpenCat | [PetoiCamp/OpenCat-Quadruped-Robot](https://github.com/PetoiCamp/OpenCat-Quadruped-Robot) | **MIT** · 1,069 B · `517ad70869fe` | 5,511 | +1 | Quadruped robot framework for STEM/robotics education | 🟢 **YES** (newly graded) |
| Echo Loop | [echo-loop/Echo-Loop](https://github.com/echo-loop/Echo-Loop) | AGPL-3.0 · 34,523 B · `0d96a4ff68ad` · 🔴 election unreadable | 4,524 | +2 | AI English listen/speak trainer; shadowing, spaced repetition (Flutter) | 🔴 no — network copyleft |
| penecho | [penecho/penecho](https://github.com/penecho/penecho) | **AGPL-3.0-only** · 34,523 B · `0d96a4ff68ad` | 2,504 | +1 | Shared canvas for handwriting, equations, diagrams, spatial reasoning (Electron) | 🔴 no — network copyleft, **and no `or-later` escape** |
| LearnHouse | [learnhouse/learnhouse](https://github.com/learnhouse/learnhouse) | AGPL-3.0 · 34,523 B · `8486a10c4393` | 2,424 | 0 | AI-powered headless learning platform (Python/React) | 🔴 no — network copyleft |
| PageLM | [CaviraOSS/PageLM](https://github.com/CaviraOSS/PageLM) | **PageLM Community License** · `main/LICENSE.md` · 8,563 B · `c834209c5f33` | 2,049 | 0 | Open NotebookLM analogue: quizzes, flashcards, notes, podcasts | 🔴 **no — bespoke, non-commercial** |
| antivibe | [mohi-devhub/antivibe](https://github.com/mohi-devhub/antivibe) | MIT · 1,065 B · `a9e5355735ea` | 1,129 | 0 | Turns AI-generated code into educational deep dives (agent skill) | 🟢 **YES** |
| kaobuddy | [jin-zi-xuan/kaobuddy-pwa](https://github.com/jin-zi-xuan/kaobuddy-pwa) | 🔴 **UNGRANTED** (10 root paths probed) | 392 | 0 | Chinese-language exam-cram PWA, BYOK | 🔴 **no — no grant at all** |
| mini-nanoGPT | [ystemsrx/mini-nanoGPT](https://github.com/ystemsrx/mini-nanoGPT) | **MIT** · 1,063 B · `703b1fc21029` | 384 | 0 | One-click pretrain+SFT teaching rig for LLM fundamentals | 🟢 **YES** (newly graded) |
| ai-shifu | [ai-shifu/ai-shifu](https://github.com/ai-shifu/ai-shifu) | Apache-2.0 · `main/LICENSE.txt` · 11,342 B · `c00cbb6a47a7` | 329 | 0 | Script-driven teaching agent / teaching assistant | 🟢 **YES** |
| AI Video Tutorial Gen | [AkshitIreddy/AI-Powered-Video-Tutorial-Generator](https://github.com/AkshitIreddy/AI-Powered-Video-Tutorial-Generator) | MIT · 1,070 B · `deffdff30dfd` | 316 | 0 | Illustrated video lessons, local models + cloud providers | 🟢 **YES** |
| EduPintarIPAS | [RozhakDev/EduPintarIPAS](https://github.com/RozhakDev/EduPintarIPAS) | MIT · 1,092 B · `0fc419538e54` | 20 | 0 | Indonesian science chatbot for grade-6 pupils | 🟢 **YES** |
| LuyenChuTieuHoc | [langmaninternet/LuyenChuTieuHoc](https://github.com/langmaninternet/LuyenChuTieuHoc) | 🔴 **UNGRANTED** (10 root paths probed) | 12 | 0 | Vietnamese primary handwriting sheets to MoET standard | 🔴 **no — no grant at all** |

🟢 **Build-on-able: 7 of 13, and 13 of 13 are graded.** 🔴 The shape `p475` reported survives re-measurement:
the three highest-starred *new* education-AI projects (Echo Loop, penecho, LearnHouse) are all network
copyleft, two rows are ungranted outright, and both ungranted rows are APAC-origin. 🟢 What changed is the
permissive side: the two newly-read grants are both MIT, so the permissive tier is larger than `p475` could
state — but it grew by **reading**, not by anything happening in the ecosystem.

### 🔴 Every grant above was re-fetched at TODAY's HEAD — and doing so reproduced `p475`'s short-probe finding against this pass's own first attempt

🔵 `p475`'s digests were recorded earlier the same day. 🟡 **Eight of thirteen HEADs had nevertheless moved
by the time this pass read them**, so carrying a digest forward — even by hours — is not the same as reading
one. All thirteen were re-fetched at the HEAD resolved today.

| what was re-measured | result |
|---|---|
| grants re-fetched at today's HEAD | **13 of 13** |
| digests reproducing `p475` exactly | **11 of 11 previously recorded** — every one |
| HEADs that moved between `p475` and `p476` | **8 of 13** (PageLM, ai-shifu, antivibe, kaobuddy, EduPintarIPAS, LuyenChuTieuHoc, AI Video Tutorial Gen, and Sakai on the foundation shelf) |
| ungranted rows re-probed at their new HEADs | **2 of 2 — still ungranted** at 10 root paths |

🔴 **The self-inflicted finding, recorded because it is the same defect `p475` documented and it caught this
pass too.** The first re-read used a **one-path probe** (`LICENSE` only) and returned `HTTP 404` for
`CaviraOSS/PageLM` and `ai-shifu/ai-shifu` — two repositories this base has published as granted for many
passes. Both grants are present and intact; they simply are not at `LICENSE`:

| repo | one-path probe (`LICENSE`) | where the grant actually is | digest |
|---|---|---|---|
| [CaviraOSS/PageLM](https://github.com/CaviraOSS/PageLM) | 🔴 **404** | `main/LICENSE.md` · 8,563 B | `c834209c5f33` — reproduces `p475` |
| [ai-shifu/ai-shifu](https://github.com/ai-shifu/ai-shifu) | 🔴 **404** | `main/LICENSE.txt` · 11,342 B | `c00cbb6a47a7` — reproduces `p475` |

🟢 **So `p475`'s widening from 5 paths to 10 is independently vindicated, by a pass that briefly regressed to
1 and immediately published two false negatives.** 🔵 The grant **path** is now recorded in the table above
for both rows, not just the bytes and digest — because the path is the part that breaks.

### 🔴 Gaps this pass registers

| gap | statement |
|---|---|
| 🔴 **`Gap 476-A`** | **4 of 8 GPL-family repos have an UNREADABLE version election** (`openedx/openedx-platform`, `echo-loop/Echo-Loop` on every channel; `canvas-lms`, `h5p-php-library` carry bare deprecated ids). For these the question is not "has anyone read it" but "is it recorded anywhere" — and on packaging metadata, source notices and payload, it is not. Resolving them needs a channel this base does not have: release artefacts, `.spec`/distro packaging, or the maintainers. |
| 🔴 **`Gap 476-B`** | **The `or-later` backfill across RETAINED HISTORY is still not done.** This pass graded 8 repos. Every other GPL-family `or-later` cell in history below remains `VERSION_ELECTION_UNREAD`, and `Gap 475-A`/`Gap 475-B` are therefore narrowed, not closed. |
| 🟡 **`Gap 476-C`** | **`frappe/lms` and `penecho` elections rest on ONE channel each** (packaging metadata), with no corroborating source notice. Only `moodle` (metadata + 3 files) and `openeducat` (187 files) are corroborated across two channels. A single-channel election is a maintainer's declaration in one file, and a `package.json` licence field is routinely wrong in ways a `LICENSE` file is not. |
| 🔴 **`Gap 476-D`** | **The star snapshot's delta is same-day and cannot measure velocity** (`Gap 475-E` is half-closed: the instrument exists, the time series does not). The lifetime-average rates published above are averages over 105–303 days and say nothing about this week. |
| 🟡 **`Gap 475-D` carried forward unresolved** | **`PetoiCamp/OpenCat` is hardware-coupled** and its education relevance is STEM-kit, not AI-tutoring. Its grant is now read (MIT), so it is no longer *unread* — but whether a hardware framework belongs on an *agents* shelf is still unresolved, and this pass did not resolve it. |
| 🔴 **`Gap 475-Y` carried forward untouched** | **38 malformed tables in RETAINED HISTORY** across the eight shelves (ragged pipe counts; one table with no separator row at `agents/top.md` line ~4990). All 38 predate `p475`. This pass's own tables are clean; **no history was repaired**, because rewriting history is what the append-only rule forbids and a separate corrections shelf has never been agreed. |

## 🆕 `p475` — `2026-10-27` — **🔴 THIS BASE GRADES `or-later` BY READING THE LICENCE PAYLOAD, AND THAT IS A UNIFORM FALSE POSITIVE: the stock GPL-family text carries "any later version" THREE TIMES in every payload measured (3 of 3), in the preamble and the how-to-apply appendix, regardless of what the project actually elected. 🔴 And the top row's magnitude was wrong by 20,000 stars — `HKUDS/DeepTutor` is `44,441★` first-hand, not the ~22k/~24k carried since `p54`.**

🔵 **Gate posture, per `Gap 446-A`:** `make hooks` **not attempted** — the industry KB is cloned outside the
harness repo and the harness refuses execution of code arriving in a clone (`Code from External`).
**Nothing below is gate-attested.** Checks re-implemented in this session's own code, held outside the
clone, and green: frontmatter keys and closed-vocabulary `region` on all eight shelves; every table
checked for separator presence and pipe-count consistency, with **no header row published as data**;
append-only preserved on both trending shelves and prepend-only on these; every address resolved
first-hand by `git ls-remote --symref`; every grant fetched from `raw.githubusercontent.com`, written
to a file, and the **file** measured (`Gap 468-A`). 21 graded payloads in
[`evidence/grant-payload.2026-10-27-p475.tsv`](../evidence/grant-payload.2026-10-27-p475.tsv),
3-payload control in
[`evidence/orlater-control.2026-10-27-p475.tsv`](../evidence/orlater-control.2026-10-27-p475.tsv).

🟢 **Cross-pass control reproduced exactly, sixth consecutive pass.** `HKUDS/DeepTutor` `main/LICENSE`
**11,408 B · `cd2f54e1e506`** at HEAD **`a31d82624c27`** — byte-, digest- and HEAD-identical to `p470`–`p474`.

🔴 **`Gap 472-A` honoured, not retried.** `curl -sI https://github.com/<repo>` still answers only the
proxy's own `200 Connection Established`. Reproduced once as a control, then abandoned.

---

### 🔴 The `or-later` reader is a uniform false positive — the pass's load-bearing finding, because it invalidates a GRADE, not a row

🔵 `p473` built a licence reader that "carries the `or-later` elections", keyed on strings in the
grant payload. 🔴 **The string it keys on is part of the stock licence text.** Every GPL-family
payload ships a preamble and a *How to Apply These Terms to Your New Programs* appendix, and both
recite "any later version" as **boilerplate** — not as the project's election.

| payload read first-hand | family | occurrences of `any later version` | 🔴 what a payload-keyed reader concludes |
|---|---|---|---|
| [openedx/edx-platform](https://github.com/openedx/edx-platform) `master/LICENSE` · 35,136 B · `e12d78569742` | AGPL-3.0 | **3** | `or-later` |
| [h5p/h5p-php-library](https://github.com/h5p/h5p-php-library) `master/LICENSE.txt` · 35,146 B · `c53a65c2fd56` | GPL-3.0 | **3** | `or-later` |
| [instructure/canvas-lms](https://github.com/instructure/canvas-lms) `master/LICENSE` · 34,520 B · `57c8ff33c9c0` | AGPL-3.0 | **3** | `or-later` |

🔴 **3 of 3.** The reader cannot return anything *but* `or-later` for a GPL-family repo, so the grade
carries no information. 🟢 **Where the election actually lives:** in the per-source-file notices the
appendix tells the author to paste, and in packaging metadata (`setup.cfg`, `composer.json`, a
`.spec`) — **not in the payload the reader reads**. Until a reader looks there, every GPL-family
`or-later` cell on these shelves should be read as `VERSION_ELECTION_UNREAD`, not as a measured grade.

### 🟡 Digest identity has a false-negative mode, found by accident on three AGPL payloads

🔵 This base uses digest identity as its cross-pass control. 🟡 Three AGPL-3.0 payloads read this
pass are **all 34,523 B**; two share digest `0d96a4ff68ad` and the third does not:

| repo | bytes | digest12 | relation |
|---|---|---|---|
| [echo-loop/Echo-Loop](https://github.com/echo-loop/Echo-Loop) | 34,523 | `0d96a4ff68ad` | byte-identical to penecho |
| [penecho/penecho](https://github.com/penecho/penecho) | 34,523 | `0d96a4ff68ad` | byte-identical to Echo-Loop |
| [learnhouse/learnhouse](https://github.com/learnhouse/learnhouse) | 34,523 | `8486a10c4393` | **differs by a line-wrap only** |

🟢 **Diffed, not assumed.** The entire difference is one line-break position in the appendix:
`…as published by / the Free Software Foundation…` versus `…as published / by the Free Software
Foundation…`. **Same length, same terms, different digest.** So a digest mismatch does **not** imply
a different grant, and a control built only on digests will raise false alarms on reflowed text.
🔵 The `p470`–`p475` DeepTutor control survives this, because it matches on bytes *and* digest *and* HEAD.

### 🔴 Magnitude correction on the top row, and it is large

🔵 `Gap 474-G` flagged one web-relayed star count as stale. 🔴 The problem is bigger than one row:
**`HKUDS/DeepTutor` is `44,441★`** read first-hand from the authenticated channel today. This base
carried `~22k★` (`p54`) and `~24k★` (`p65`), and a secondary blog found this pass still says
"over 15,000". 🟢 Every star count below is first-hand as of `2026-10-27`, never web-relayed.

### 🟢 The live agent tier — 13 real rows, every grant read first-hand this pass

🔵 `grant_read` is the payload's own title, not a badge, an index or a roundup.

| agent | repo | grant (read first-hand) | ★ (first-hand) | what it is | build-on-able |
|---|---|---|---|---|---|
| DeepTutor | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | Apache-2.0 · 11,408 B · `cd2f54e1e506` | 44,441 | Lifelong personalised tutoring; multi-agent + RAG; CLI/WebSocket/SDK | 🟢 **YES** |
| Echo Loop | [echo-loop/Echo-Loop](https://github.com/echo-loop/Echo-Loop) | AGPL-3.0 · 34,523 B · `0d96a4ff68ad` | 4,522 | AI English listen/speak trainer; intensive listening, shadowing, spaced repetition (Flutter) | 🔴 no — network copyleft |
| penecho | [penecho/penecho](https://github.com/penecho/penecho) | AGPL-3.0 · 34,523 B · `0d96a4ff68ad` | 2,503 | Shared canvas for handwriting, equations, diagrams, spatial reasoning | 🔴 no — network copyleft |
| LearnHouse | [learnhouse/learnhouse](https://github.com/learnhouse/learnhouse) | AGPL-3.0 · 34,523 B · `8486a10c4393` | 2,424 | AI-powered headless learning platform (Python/React) | 🔴 no — network copyleft |
| PageLM | [CaviraOSS/PageLM](https://github.com/CaviraOSS/PageLM) | **PageLM Community License** · 8,563 B · `c834209c5f33` | 2,049 | Open NotebookLM analogue: quizzes, flashcards, notes, podcasts | 🔴 **no — bespoke, non-commercial** |
| antivibe | [mohi-devhub/antivibe](https://github.com/mohi-devhub/antivibe) | MIT · 1,065 B · `a9e5355735ea` | 1,129 | Turns AI-generated code into educational deep dives (agent skill) | 🟢 **YES** |
| kaobuddy | [jin-zi-xuan/kaobuddy-pwa](https://github.com/jin-zi-xuan/kaobuddy-pwa) | 🔴 **UNGRANTED** (10 root paths probed) | 392 | Chinese-language exam-cram PWA, BYOK | 🔴 **no — no grant at all** |
| ai-shifu | [ai-shifu/ai-shifu](https://github.com/ai-shifu/ai-shifu) | Apache-2.0 · 11,342 B · `c00cbb6a47a7` | 329 | Script-driven teaching agent / teaching assistant | 🟢 **YES** |
| AI Video Tutorial Gen | [AkshitIreddy/AI-Powered-Video-Tutorial-Generator](https://github.com/AkshitIreddy/AI-Powered-Video-Tutorial-Generator) | MIT · 1,070 B · `deffdff30dfd` | 316 | Illustrated video lessons, local models + cloud providers | 🟢 **YES** |
| EduPintarIPAS | [RozhakDev/EduPintarIPAS](https://github.com/RozhakDev/EduPintarIPAS) | MIT · 1,092 B · `0fc419538e54` | 20 | Indonesian science chatbot for grade-6 pupils | 🟢 **YES** |
| LuyenChuTieuHoc | [langmaninternet/LuyenChuTieuHoc](https://github.com/langmaninternet/LuyenChuTieuHoc) | 🔴 **UNGRANTED** (10 root paths probed) | 12 | Vietnamese primary handwriting sheets to MoET standard | 🔴 **no — no grant at all** |
| OpenCat | [PetoiCamp/OpenCat-Quadruped-Robot](https://github.com/PetoiCamp/OpenCat-Quadruped-Robot) | grant not read this pass | 5,510 | Quadruped robot framework for STEM/robotics education | 🟡 unread |
| mini-nanoGPT | [ystemsrx/mini-nanoGPT](https://github.com/ystemsrx/mini-nanoGPT) | grant not read this pass | 384 | One-click pretrain+SFT teaching rig for LLM fundamentals | 🟡 unread |

🔴 **Build-on-able: 6 of 11 graded.** The two most-starred *new* education-AI repos of this window
(Echo Loop, penecho) are both AGPL-3.0, and the third (LearnHouse) is too — **the new high-star
education-AI tier is network copyleft, not permissive.** Two more are ungranted outright, and both
of those are APAC-origin.

### 🔴 Gaps this pass registers

| gap | statement |
|---|---|
| 🔴 **`Gap 475-A`** | **Every `or-later` cell this base has published is unmeasured.** The control above shows the payload cannot distinguish an election. No shelf row has been re-graded, because the real election lives in source-file headers and packaging metadata that no reader here has ever opened. 🔵 The fix is a reader that greps `*.py`/`*.php`/`*.java` notices and `setup.cfg`/`composer.json`, not the LICENSE. |
| 🔴 **`Gap 475-B`** | **`Gap 474-A`'s scope backfill is still not done, and this pass did not do it either.** 21 payloads were graded on family and presence; **none was graded on scope**. The three `SPLIT_SCOPE` assets `p474` found remain the only scope-graded rows in the base. |
| 🟡 **`Gap 475-C`** | **Two rows are published with an unread grant** (`OpenCat`, `mini-nanoGPT`), marked 🟡 rather than dropped, because their magnitude is first-hand and useful. They are **not** build-on-able until read, and must not be counted in any permissive census. |
| 🔴 **`Gap 475-Y`** | **The gate this pass ran finds 38 malformed tables in RETAINED HISTORY across the eight shelves** (ragged pipe counts, and one table with no separator row at `agents/top.md` line ~4990). 🟢 All 38 predate `p475`; this pass's own 23 tables and 112 data rows are clean. 🔴 They are **not fixed**, because both trending shelves are append-only and rewriting history would destroy the record the shelves exist to keep. 🔵 A ragged table renders as dropped cells, so some historical rows are **already being read wrong** — the compiler, not the prose, decides what those rows become. The decision of whether append-only outranks correctness here is not this pass's to make. |
| 🟡 **`Gap 475-D`** | **`PetoiCamp/OpenCat` is hardware-coupled** and its education relevance is STEM-kit, not AI-tutoring. It sits on this shelf because the topic sweep returned it at 5,510★; whether a hardware framework belongs on an *agents* shelf is unresolved. |


## 🆕 `p474` — `2026-10-27` — **🔴 A GRANT HAS A FAMILY, A VERSION AND A CLASS — AND IT ALSO HAS A *SCOPE*, WHICH NO READER ON THIS BASE HAS EVER READ. Three payloads found this pass license DIFFERENT SUBTREES DIFFERENTLY from one file, and the worst case is an evaluation asset whose LICENSE RETRACTS ITS OWN EARLIER CC BY CLAIM over 1,038,963 problems and points at third-party terms, some of them `CC BY-NC`. 🟢 And `Gap 473-C` is CLOSED: the title reader now reads Portuguese, re-grading two AGPL-3.0-or-later payloads that it previously published as `UNSTATED`.**

🔵 **Gate posture, per `Gap 446-A`:** `make hooks` **not attempted** — the industry KB is cloned
outside the harness repo this pass, and the harness refuses execution of code arriving in a clone
(`Code from External`). **Nothing below is gate-attested.** Checks re-implemented in this session's
own code and green: frontmatter keys and closed-vocabulary `region` on all nine shelves; every table
checked for separator presence and pipe-count consistency, with **no header row published as data**;
append-only preserved on both trending shelves and on these shelves by prepend-only edit; every
address resolved first-hand by `git ls-remote --symref`; every grant read first-hand from
`raw.githubusercontent.com`, body written to a file and the file measured (`Gap 468-A`).
27 addresses in
[`evidence/grant-class.2026-10-27-p474.tsv`](../evidence/grant-class.2026-10-27-p474.tsv),
24 graded payloads in
[`evidence/grant-lang-scope.2026-10-27-p474.tsv`](../evidence/grant-lang-scope.2026-10-27-p474.tsv).

🔴 **`Gap 472-A` honoured, not retried.** `curl -sI https://github.com/HKUDS/DeepTutor` → `403`
behind the proxy's own `200 Connection Established`. Reproduced once as a control, then abandoned.

🟢 **Cross-pass control reproduced exactly, fifth consecutive pass.** `HKUDS/DeepTutor`
`main/LICENSE` **11,408 B · `cd2f54e1e506`** at HEAD **`a31d82624c27`** — byte-, digest- and
HEAD-identical to `p470`–`p473`.

---

### 🔴 The scope axis — the pass's load-bearing finding, because it invalidates a COLUMN, not a row

🔵 This base grades a grant on family (`p454`), version (`p455`), presence (`Gap 466-A`) and class
(`Gap 467-A`). 🔴 **Every one of those axes assumes the grant covers the whole repository.** Three
payloads read first-hand this pass do not:

| repo | grant path · bytes · digest | what the ONE file actually says | 🔴 why a single licence cell is wrong |
|---|---|---|---|
| [bncc-dev/bncc-benchmark](https://github.com/bncc-dev/bncc-benchmark) | `main/LICENSE` · **911 B** · `d19733bb7540` | 🔵 Title block is **`# Licenças`** — not a licence title at all. **MIT** for `harness/` and `test/`; **CC BY 4.0** for the item bank (`itens/`), the round results (`resultados/`) and `METODOLOGIA.md` | 🔴 The *code* is permissive; the **benchmark items — the only reason to take the repo — are CC BY**, so attribution travels into any deliverable that ships them |
| [bncc-dev/bncc-pacotes](https://github.com/bncc-dev/bncc-pacotes) | `main/LICENSE` · **1,299 B** · `86bf5f5e6306` | 🔵 Same `# Licenças` model. **MIT** for `packages/*/src/`, `python/bncc/*.py`, `mcp-worker/src/`; **CC BY 4.0** for embedded JSONs synced from a pinned commit of `bncc-dados`. 🔴 Name and visual identity **explicitly not licensed**: *"O código é livre; a marca não"* | 🔴 **The published artifacts carry both grants in one file** — the npm tarball and the PyPI wheel ship MIT code *and* CC BY data together. A client's dependency scanner sees `MIT` and the attribution duty ships silently |
| [richer-richard/arquimedes](https://github.com/richer-richard/arquimedes) | `main/LICENSE` · **3,103 B** · `b8e2e1c65fdc` | 🔵 Opens *"This repository is not one work and is not under one license."* **MIT** for `arquimedes/`, `tools/`, `site/`; **CC BY 4.0** for this project's own annotations only; 🔴 `problems/` and `images/` are **third-party and NOT relicensed** | 🔴 **The payload retracts its own earlier grant in writing**: *"An earlier version of this file placed `problems/`, `images/`, and `data/` under CC BY 4.0. That sentence was this project's claim. It was not a grant from the contest organizers."* **CEMC material is `CC BY-NC 4.0`** → `UNSELLABLE` under this base's own `grant_class` taxonomy |

🔴 **Read that third row again.** The asset is advertised as 1,038,963 structured maths problems
with answers and solutions — the single largest education evaluation corpus this base has found.
**The 1.03M problems are the part that is not licensed to you.** A reader that takes the repo's
licence from an index, a badge or even this payload's *first* line publishes `MIT` and is wrong
about everything that matters.

🟢 **Reader shipped, not just the finding.**
[`family_lang.py`](../compose/code/p474-scope-and-language/family_lang.py) now returns a `scope`
alongside family/version, and refuses to emit a sound single cell when scope is `SPLIT_SCOPE`
([`controls.py`](../compose/code/p474-scope-and-language/controls.py), **27/27**, of which **23 are
real measured payloads** and 4 are labelled synthetic).

### 🟢 `Gap 473-C` closed — the title reader now reads Portuguese, and the second instance found itself

🔵 The gap said every licence reader here is keyed on English title strings, and that
`portabilis/i-diario`'s AGPL-3.0 **in Portuguese** therefore published as `UNSTATED`. 🟢 The
non-English title layer exists, folds accents, and carries the `or-later` elections
(`qualquer versão posterior`, `cualquier versión posterior`):

| payload | bytes · digest | 🔴 English-only reader | 🟢 `p474` reader |
|---|---|---|---|
| [portabilis/i-diario](https://github.com/portabilis/i-diario) `1.6/LICENSE` | 35,326 B · `fe85f94658bf` | 🔴 **`UNSTATED`** | 🟢 **`AGPL-3.0-or-later`** |
| [portabilis/pre-matricula-digital](https://github.com/portabilis/pre-matricula-digital) `2.12/LICENSE` | 35,326 B · `fe85f94658bf` | 🔴 **`UNSTATED`** | 🟢 **`AGPL-3.0-or-later`** |

🟢 **The second row was not sought — it arrived on the `educacao` leg and graded itself.** Identical
bytes and identical digest to `i-diario`, at a **different repository** on a **versioned default
branch** (`2.12`). So the Portuguese AGPL payload is a *vendor-wide* pattern at Portabilis, not one
file: every Portabilis component an engagement touches must be assumed AGPL until its payload is
read. 🔵 **2 disagreements across 24 graded payloads (8.3 %)** — and both are the one family whose
trigger is network use.

### 🟢 The evaluation tier, re-run with NO star floor (`Gap 473-A`, partially closed)

🔵 `p473` found nine instruments on research vocabulary and declared its own n = 9 too small to
carry a client argument. 🟢 Two legs re-run this pass with **no star floor**, three numbers each, per
the gap's own contract:

| leg | hits | returned + graded | 🟢 usable education-AI supply after relevance grading |
|---|---|---|---|
| `education llm-evaluation` | **48** | 12 | **8** |
| `topic:benchmark topic:education` | **19** | 12 | **5** |

🔴 **The relevance trap is the highest-starred row in the leg.**
[langfuse/langfuse-workshop](https://github.com/langfuse/langfuse-workshop) (57★) is the top hit for
`education llm-evaluation` and is **a workshop that teaches evaluation** — `education` as a
*delivery mode*, not as the domain under test. 🔵 Same shape as `Gap 467-H`'s `tutor`/`tutorial`
collision, now measured on a second vocabulary.

🟢 **The tier's grant rate is much better than `p473`'s 44.4 % ungranted suggested** — on the 11
evaluation-tier addresses graded first-hand this pass, **10 grant and 1 does not**
([`AksharaRgsu2024/LLM_Factuality_Evaluation`](https://github.com/AksharaRgsu2024/LLM_Factuality_Evaluation),
**14 paths probed**, `main`). 🔴 But `Gap 473-A`'s number is **not** closed by that: this is a
different token set, so the two rates are not comparable, and the real finding is the scope axis
above — three of these "permissive" rows do not grant what they appear to grant.

### 🟢 Agents and instruments added this pass — 13 rows, every grant read first-hand today

| Name | Repo | Grant (path read · bytes · digest) | ★ | Region | What it is, and what it is for |
|---|---|---|---|---|---|
| Atölye.Platform | [PolyOS-Team/Atolye.Platform](https://github.com/PolyOS-Team/Atolye.Platform) | 🟢 **MIT** — `main/LICENSE` · 1,069 B · `fc9ec90c31a1` | 16 | EMEA | 🟢 **The first Turkish education-infrastructure row this base can name.** Exam submission + education management, optimised for **Pardus** (Türkiye's national Linux distribution) school laboratories. Multilingual, React/Node. 🔵 Region basis: **orthographic** (Turkish prose) *and* institutional |
| StudentBench | [Handshake-AI-Research/studentbench](https://github.com/Handshake-AI-Research/studentbench) | 🟢 **MIT** — `main/LICENSE` · 1,078 B · `3cb4c0b9467a` | 11 | Global | Reproduces every figure, table and empirical result in the StudentBench paper. Tutoring-focused LLM evaluation; **MIT whole-work**, so it can enter a deliverable outright |
| BNCC Benchmark | [bncc-dev/bncc-benchmark](https://github.com/bncc-dev/bncc-benchmark) | 🔴 **SPLIT_SCOPE** — `main/LICENSE` · 911 B · `d19733bb7540` (MIT code / CC BY 4.0 items) | 9 | LATAM | **Open hallucination benchmark of LLMs over Brazil's national curriculum**: 15,300 responses across 17 models, public methodology and raw data, **private held-out set against contamination**. The only national-curriculum-grounded education benchmark on these shelves |
| BNCC Pacotes | [bncc-dev/bncc-pacotes](https://github.com/bncc-dev/bncc-pacotes) | 🔴 **SPLIT_SCOPE** — `main/LICENSE` · 1,299 B · `86bf5f5e6306` (MIT code / CC BY data / **marca unlicensed**) | 9 | LATAM | npm + PyPI packages **and an MCP server** exposing `bncc-dados` in one line. 🟢 The MCP surface is what makes the Brazilian curriculum callable from an agent |
| BNCC Dados | [bncc-dev/bncc-dados](https://github.com/bncc-dev/bncc-dados) | 🟢 **MIT** — `main/LICENSE` · 1,092 B · `e162f8f4b461` | 22 | LATAM | Brazil's national curriculum as verified open data: **1,721 learning objectives** in JSON, SQLite and CSV with per-record provenance |
| EduSafeBench | [kaushikatla-cell/EduSafeBench](https://github.com/kaushikatla-cell/EduSafeBench) | 🟢 **MIT** — `main/LICENSE` · 1,056 B · `1126322e2cc8` | 0 | North America | Reproducible reliability benchmarks for AP CSA / AP CSP learning assistants, with an external review workflow. 🔵 Region basis: **institutional, not orthographic** (AP is a US College Board programme) |
| SLM writing-feedback tutor (pt-BR) | [RandMelville/slm-writing-feedback-tutor-ptbr](https://github.com/RandMelville/slm-writing-feedback-tutor-ptbr) | 🟢 **MIT** — `main/LICENSE` · 1,085 B · `b7e21ba75eea` | 1 | LATAM | Diagnostic benchmark of **8 open SLMs ≤3.8B for OFFLINE Socratic writing tuition in Brazilian Portuguese**, Fisher-exact analysis + 4-isolation falsification protocol. 🟢 The offline/small-model axis is the one that fits low-connectivity public schooling |
| Arquimedes | [richer-richard/arquimedes](https://github.com/richer-richard/arquimedes) | 🔴 **SPLIT_SCOPE** — `main/LICENSE` · 3,103 B · `b8e2e1c65fdc` (MIT code; **problems third-party, CEMC `CC BY-NC`**) | 1 | Global | 1,038,963 structured maths problems with answers, solutions and LaTeX, as gzipped JSONL shards, plus an MCP server. 🔴 **Take the harness, not the corpus** — see the scope table above |
| SciReason-Forge | [chenhz01/scireason-forge](https://github.com/chenhz01/scireason-forge) | 🟢 **Apache-2.0** — `main/LICENSE` · 11,938 B · `7cae8b289d20` | 1 | Global | Verifiable scientific-reasoning task **generators** — 5 types, solver-graded, **contamination-proof by construction** (pure stdlib). 🟢 Generated items have no third-party corpus to license: the clean answer to the `arquimedes` trap |
| Eyedot (点睛) | [Simon-zj1/eyedot](https://github.com/Simon-zj1/eyedot) | 🟢 **MIT** — `main/LICENSE` · 1,089 B · `e385b6b49565` | 2 | APAC | Turns a learner's own PDFs/notes into auto-graded exams with **per-scoring-point judgement**, flags low-confidence judgements for human review, and schedules revision with FSRS. 🔵 Region basis: orthographic (Chinese prose) |
| Open Harness Atlas | [Benjamin-KY/open-harness-atlas](https://github.com/Benjamin-KY/open-harness-atlas) | 🟢 **Apache-2.0** — `main/LICENSE` · 11,289 B · `e0f0d038f8b6` | 10 | Global | Knowledge graph of 793 open-source AI harnesses across governance, agent, evaluation, red-team and routing, 97 % curator-reviewed. Useful as a **discovery index**, not as a graded source — every grant it names still needs a first-hand read |
| LLM Factuality Evaluation | [AksharaRgsu2024/LLM_Factuality_Evaluation](https://github.com/AksharaRgsu2024/LLM_Factuality_Evaluation) | 🔴 **UNGRANTED** — 14 paths probed on `main` | 2 | Global | Pipeline judging factuality of LLM responses for AI in education. 🔴 **No grant at any probed path: cannot enter a deliverable.** Carried so the tier's denominator stays honest |
| Agents from scratch | [pguso/agents-from-scratch](https://github.com/pguso/agents-from-scratch) | 🟢 **MIT** — `main/LICENSE` · 1,091 B · `f78cc6bf1d57` | 🔵 web-relayed ≈796, **late-May-2026, not re-measured** | Global | Builds agents from first principles against a local LLM; tagged `ai-education`. 🔵 The only MIT education-tagged agent the brief's own generic query surfaced — the generic query is a weak instrument here and that is recorded, not hidden |

🔵 **Stars are index-relayed from MCP `search_repositories`, 2026-10-27, never first-hand**
(`Gap 467-D`). Grants, addresses, bytes and digests above are all first-hand today.

## 🆕 `p473` — `2026-10-27` — **🟢 THE "NO OPEN-SOURCE EDUCATION-AI EVALUATION HARNESS EXISTS" GAP THIS BASE HAS CARRIED FOR DOZENS OF PASSES IS CLOSED AND ITS PREMISE EXPLAINED: nine instruments exist, every one of them sits below 60★, and so every star-ordered sweep this base has ever run was structurally blind to the entire tier. 🔴 And the tier is the least usable shelf in this KB — 4 of 9 are UNGRANTED, Khan Academy's carries a bespoke licence that recites a permissive grant and then bars production use and model training, and the ONLY permissively-licensed education evaluation harness found anywhere is West-Africa-origin at 4★.**

🔵 **Gate posture, per `Gap 446-A`:** `make hooks` not attempted — the industry KB is cloned outside
the harness repo this pass. **Nothing below is gate-attested.** Checks re-implemented in this
session's own code and green: frontmatter keys and closed-vocabulary `region` on all nine shelves;
every table below checked for separator presence and pipe-count consistency, with **no header row
published as data**; append-only preserved on both trending shelves and on these shelves by
prepend-only edit; every address resolved first-hand by `git ls-remote --symref`
([`evidence/p473-address-resolution.tsv`](../evidence/p473-address-resolution.tsv)); every grant
read first-hand from `raw.githubusercontent.com`, body written to a file and the file measured
(`Gap 468-A`). 43 graded cells in
[`evidence/grant-class.2026-10-27-p473.tsv`](../evidence/grant-class.2026-10-27-p473.tsv).

🔴 **`Gap 472-A` honoured, not retried.** `curl -sI https://github.com/HKUDS/DeepTutor` → `403`
behind the proxy's own `200 Connection Established`; `api.github.com/repos/HKUDS/DeepTutor` → `403`.
Reproduced once as a control and then abandoned, as `p472` prescribed.

🟢 **Cross-pass control reproduced exactly, fourth consecutive pass.** `HKUDS/DeepTutor`
`main/LICENSE` **11,408 B · `cd2f54e1e506`** at HEAD **`a31d82624c27`** — byte-, digest- **and
HEAD**-identical to `p465`, `p466` and `p472`. The payload channel is stable; the index channel is
not (stars read **44,177** by `p472` this morning).

### 🟢 The standing evaluation-harness gap — CLOSED with nine named instruments, and the reason it stayed open

🔵 The gap has been phrased on this shelf for many passes as *"no open-source education-AI
evaluation harness surfaced at any star floor — searched `education agent`, `topic:edtech`,
`topic:education-ai`, `topic:lms`, `grading topic:education`."* 🟢 **Every one of those tokens is a
product vocabulary.** The supply is published as **benchmarks in the research literature** and
named accordingly, so it answers to `benchmark`, `*Bench`, `llm-evaluation` and `evaluation-framework`
and to none of the five tokens tried. Run on the research vocabulary, the tier appears at once.

| Instrument | Repo | Grant (path read, bytes, digest) | Stars | Region | What it measures, and whether Globant may use it |
|---|---|---|---|---|---|
| **wassce-benchmark** | [acheamponge/wassce-benchmark](https://github.com/acheamponge/wassce-benchmark) | 🟢 **MIT** — `main/LICENSE`, 1,076 B `df8c7a998c17` | 4 | EMEA | 🟢 **The only permissively-licensed education evaluation harness this base has found, at any star floor, in any region.** Open LLMs scored on the **WASSCE**, the exam ~2 million West Africans sit every year. **Usable in a paid engagement without conditions** |
| **bncc-benchmark** | [bncc-dev/bncc-benchmark](https://github.com/bncc-dev/bncc-benchmark) | 🟢 **COMPOSITE** — `main/LICENSE` 911 B `d19733bb7540` → code **MIT** (`LICENSE-CODIGO.md` 1,286 B `e1ed7acaf9e2`) + items/results/methodology **CC BY 4.0** (`LICENSE-DADOS.md` 577 B `9b70e1d9a0c9`) | 9 | LATAM | 🟢 **LLM hallucination over Brazil's BNCC national curriculum**: 15,300 answers from 17 models, a published methodology and a **private held-out split against contamination**. 🟢 `CC BY 4.0` is **BY, not BY-NC** — the item bank is commercially usable with attribution. **Usable** |
| **mathtutorbench** | [eth-lre/mathtutorbench](https://github.com/eth-lre/mathtutorbench) | 🔴 **UNGRANTED** — no payload at 14 root paths | 45 | EMEA | 🔴 **An EMNLP 2025 Oral benchmark for open-ended pedagogical capability, with a reward model for scoring teacher responses — and it grants nothing.** The most cited instrument in the tier is the one with no licence |
| **tutoring-accuracy-dataset** | [Khan/tutoring-accuracy-dataset](https://github.com/Khan/tutoring-accuracy-dataset) | 🟡 **BESPOKE "Evaluation Dataset License"** — `main/LICENSE`, 2,690 B `53cf7aa78a89` | 57 | North America | Khan Academy's math-tutoring accuracy benchmark. 🔴 **Restricted to internal non-commercial model evaluation**; redistribution, **model training** and production use expressly prohibited, not sublicensable, and the restriction **propagates into any combined dataset**. 🟢 But §3 explicitly permits evaluating *products intended for commercial use* and commercial use of the *insights*. **Usable as an internal gate; never shippable** |
| **CSTutorBench** | [Yunfeng-Wan/CSTutorBench](https://github.com/Yunfeng-Wan/CSTutorBench) | 🔴 **CC BY-NC 4.0** — `main/LICENSE`, 313 B `9530f3063565` (pointer form) | 2 | APAC | 2,970 multi-turn CS-tutoring dialogues from real university forums. 🔴 Payload states *"Commercial use is strictly prohibited."* **Not usable** |
| **overlooked-bench** | [kcelestinomaria/overlooked-bench](https://github.com/kcelestinomaria/overlooked-bench) | 🟡 **AGPL-3.0** — `main/LICENSE`, 34,523 B `0d96a4ff68ad` | 1 | EMEA | A recurring benchmark aimed squarely at what mainstream evals skip, **"education beyond the university track"** and small/non-US organisational tasks, Kenya-origin. 🔴 Network copyleft: run it in CI, never inside the deliverable |
| **TutorTrace** | [divadbaroon/TutorTrace_dataset_and_benchmark](https://github.com/divadbaroon/TutorTrace_dataset_and_benchmark) | 🔴 **UNGRANTED** — no payload at 14 root paths | 5 | Global | Dataset + benchmark, no stated grant |
| **llm-instruction-benchmarking** | [conradborchers/llm-instruction-benchmarking](https://github.com/conradborchers/llm-instruction-benchmarking) | 🔴 **UNGRANTED** — no payload at 14 root paths | 7 | Global | AIED25: *can LLMs match tutoring-system adaptivity?* — the adaptivity question stated as a measurement, ungranted |
| **Multi-Agent-Tutoring-Systems** | [isra-moussaoui/Multi-Agent-Tutoring-Systems](https://github.com/isra-moussaoui/Multi-Agent-Tutoring-Systems) | 🔴 **UNGRANTED** — no payload at 14 root paths | 5 | Global | Whether multi-agent architectures reduce **pedagogical sycophancy**, on the BEA 2026 propositional-logic benchmark. 🔵 The question a studio should be asking of its own tutor, with no grant to borrow |

### 🔴 The evaluation tier, stated as a number — and it is the worst shelf in this KB

| grant class | instruments | share | Globant can build on it? |
|---|---|---|---|
| 🔴 **UNGRANTED** | 4 | **44.4 %** | **No** |
| 🟢 Permissive (MIT, incl. the composite's code half) | 2 | 22.2 % | Yes |
| 🔴 NonCommercial / bespoke non-shippable | 2 | 22.2 % | Internal evaluation only, never shipped |
| 🟡 AGPL-3.0 | 1 | 11.1 % | CI-side only, outside the deliverable |

🔴 **Set that against this base's own agent tier, which `p472` measured at 42.9 % permissive and
14.3 % ungranted.** The tier that exists to *verify* education AI is **three times more likely to be
ungranted** than the tier it verifies. 🔵 The causal reading is plain and worth carrying: the agent
tier is built by people shipping products, who reach for a licence; the evaluation tier is built by
researchers shipping papers, for whom the artefact of record is the PDF and the repository is a
supplement.

🟢 **And the single operative sentence for an engagement:** the only education evaluation instrument
that may enter a deliverable unconditionally is **4★ and from West Africa**, and the second is
**9★ and from Brazil**. The two regions this base has recorded for passes as *supply-absent* are
the only two that supplied a usable one.

### 🟢 New permissive agent rows, grant-verified this pass

| Agent | Repo | Grant (path read, bytes) | Stars | Region | What it is |
|---|---|---|---|---|---|
| **knowledge-spaces** | [vanderbilt-data-science/knowledge-spaces](https://github.com/vanderbilt-data-science/knowledge-spaces) | 🟢 **MIT** — `main/LICENSE`, 1,090 B `ed2ed868dffc` | 30 | North America | 🟢 **Knowledge Space Theory as a working pipeline**, 10 agent skills: course materials → knowledge graph → adaptive assessment → personalised materials → just-in-time instruction planning. Vanderbilt Data Science. 🔵 The one row on this shelf with a **named learning theory** under the adaptivity, rather than a prompt chain |
| **lineage-skill** | [JuneYaooo/lineage-skill](https://github.com/JuneYaooo/lineage-skill) | 🟢 **Apache-2.0** — `main/LICENSE`, 11,358 B `cfc7749b96f6` | 463 | Global | Videos, PDFs, transcripts and notes → **source-backed** teacher skills. 🔵 Its licence payload is **digest-identical** to `oppia/oppia`'s — see the instrument note below |
| **Claw-ED** | [SirhanMacx/Claw-ED](https://github.com/SirhanMacx/Claw-ED) | 🟢 **MIT** — `main/LICENSE`, 1,078 B `4d5d987f4f89` | 63 | Global | **Local-first** AI teaching assistant producing *editable* lesson drafts, student materials and slides. 🟢 Local-first matters where the EU AI Act's high-risk duties or a district data-residency rule bite |

### 🔴 Two ungranted newcomers, named rather than dropped

| Repo | Stars | Probe result | Why it is worth naming anyway |
|---|---|---|---|
| [ASEpochs/ai-digital-teacher](https://github.com/ASEpochs/ai-digital-teacher) | 13 | 🔴 **UNGRANTED** at 14 root paths, HEAD `b9bdcd78a85e` | Multimodal **classroom observation**: camera perception, behaviour reasoning, voice alerts. 🔴 The capability sits exactly where the EU AI Act is strictest and the grant is absent — a row to watch, not to use |
| [bobuel/bloom-taxonomy-quiz-builder-skill](https://github.com/bobuel/bloom-taxonomy-quiz-builder-skill) | 3 | 🔴 **UNGRANTED** at 14 root paths, HEAD `5fed5008499b` | Source-grounded quiz building with teacher review at explicit **Bloom levels** — the shape `compose/patterns.md` wants, with nothing to borrow |

### 🔴 `Gap 467-A`'s signature reproduced independently, on a major organisation's repo

🔵 `Gap 467-A` said: *a permissive grant FORM is not a permissive grant*, proved on `CaviraOSS/PageLM`,
and warned that the signature to re-sweep is a grant sentence in a bespoke instrument.
🔴 **Khan Academy's `Evaluation Dataset License` is that shape exactly**, and it is not a hobby repo:

> *"permission to use the Dataset internally, solely for purposes of evaluating artificial
> intelligence models… including, without limitation, the rights to use, copy, modify, merge, or
> combine with other data"*

🔵 Read to the end of that sentence and it says `internally, solely`. Read only the familiar middle
and it reads as MIT. 🟢 **The gap's prescription holds and is now two-for-two across unrelated
publishers** — the restriction override must run on *every* payload carrying a permissive grant
sentence without a recognised title, not merely on the ones that look amateur.

### 🟢 An instrument result this pass did not go looking for: the digest rule, demonstrated in BOTH directions in one sweep

🔵 `p466`'s standing rule is *"digest identifies licence text + holder; size identifies nothing."*
This pass's Apache-2.0 population tests it from both sides at once:

| observation | payloads | reading |
|---|---|---|
| 🔴 **11,357 B, THREE different digests** | `lrsql` `c71d239df917` · `ADL_LRS` `58d1e17ffe51` · `uol-redacoes-xml` `b40930bbcf80` | A size screen at 11,357 would call three distinct payload instances one file. 🔵 And the causes are legible: `lrsql`↔`ADL_LRS` differ by a **leading blank line against a missing trailing newline — two changes that cancel to the byte**; `uol-redacoes-xml` carries the **pre-2019 GitHub template with `{}` placeholders** where the others carry `[]`, the same length either way |
| 🟢 **11,358 B, ONE digest shared by two unrelated repos** | `lineage-skill` and `oppia/oppia`, both `cfc7749b96f6` | 🟢 The digest correctly identifies the *same* canonical instance across repositories that share no authorship |
| 🔴 **Apache-2.0 spans 10,982 → 11,408 B this pass alone** | 8 payloads, **6 distinct byte values, 7 distinct digests** | OpenOLAT 10,982 · terracotta 11,323 · (11,357 ×3) · (11,358 ×2) · my-learning-analytics 11,379 · DeepTutor 11,408 |

🟢 **So `Gap 465-A`'s amendment gets a third canonical Apache-2.0 family**: bare SPDX (~10,273 B),
GitHub-template-with-APPENDIX in **brackets**, and GitHub-template-with-APPENDIX in **braces** — and
the last two are **the same size**. Declaring raw bytes is necessary, declaring *which* canonical
text is necessary, and **only the digest is sufficient.**

### 🔵 Declared gaps on this shelf

- 🔴 **`Gap 473-A` — the evaluation tier's 44 % ungranted rate is measured at n = 9 and that is too
  small to carry.** The tier was found on one vocabulary in one pass. Next pass should run
  `*Bench` / `llm-evaluation` / `evaluation-framework` / `topic:benchmark` with **no star floor** and
  publish hits, novel-by-address and **usable supply after relevance grading** as three separate
  numbers (`Gap 467-H`), so the rate is tested rather than assumed.
- 🔴 **Four ungranted instruments are worth one email each, and that is not a repository action.**
  `mathtutorbench` (ETH Zurich), `TutorTrace`, `llm-instruction-benchmarking` (AIED25) and
  `Multi-Agent-Tutoring-Systems` are all academic artefacts whose authors almost certainly intend
  openness. Recorded as **ungranted**, because intent is not a licence.
- 🔵 **No LATAM-origin conversational *agent* surfaced even on the language axis.** The Portuguese
  leg (`intel/market.md`, `repos/foundations.md`) returned a school information system, a gradebook,
  a curriculum dataset, an essay corpus and a benchmark — **infrastructure and content, no tutor.**
  Stated as an informed asymmetry, not as coverage.

## 🆕 `p472` — `2026-10-27` — **🔴 THE VERIFICATION CHANNEL THE STANDING TASK PRESCRIBES IS A UNIFORM FALSE-NEGATIVE GENERATOR: `curl -sI https://github.com/<repo>` returned 403 on 31 of 31 repositories verified-live this pass, and its single non-403 was the proxy's own `Connection Established` line, not GitHub's. 🔴 And on the live top tier only 6 of 14 agents are build-on-able — the single most-starred AI tutor on GitHub (29,550★) carries NO GRANT AT ALL, and a 2,049★ repo that reads open ships a bespoke NON-COMMERCIAL licence.**

🔵 **Gate posture, per `Gap 446-A`:** `make hooks` not attempted — the industry KB is cloned outside
the harness repo this pass. **Nothing below is gate-attested.** Frontmatter keys and
closed-vocabulary `region` verified on all eight shelves; every table below checked for separator
presence and pipe-count consistency, with **no header row published as data**; append-only preserved
on both trending shelves and on these six by prepend-only edit.

🔵 **`Gap 468-A` honoured.** No licence payload below was measured through a shell variable: each
body was written to a file and the file measured.

### 🔴 `Gap 472-A` — the prescribed `curl -sI` URL check cannot verify anything on this harness

🔵 The standing task says *"Verify every URL before writing it (`curl -sI`)"*. Run against the 31
repositories this pass verified live by payload, it returns **403 for all 31**. The one call that
did not return 403 is worse than the ones that did:

| probe | result | reading |
|---|---|---|
| `curl -sI https://github.com/<any of 31 live repos>` | **403** × 31 | 🔴 **UNIFORM FALSE NEGATIVE.** A pass that obeyed the instruction literally would have deleted every real row on this shelf as a 404-class failure |
| `curl -sI https://github.com/openedx/edx-platform` | `HTTP/1.1 200 Connection Established` | 🔴 **FALSE POSITIVE, and not even GitHub's.** That status line is the **proxy's CONNECT response**. A checker grepping for `200` passes this repo on a header the origin never sent |
| `GET raw.githubusercontent.com/openedx/edx-platform/master/README.rst` | **200**, payload | 🟢 Existence proved by a byte only the origin could serve |

🔴 **So the instruction's channel is unusable here and its failure mode is silent in both
directions.** 🟢 Registered as **`Gap 472-A`**: on this harness a repository address is verified by
**MCP `search_repositories`** (live `html_url`, `stargazers_count`, `archived`, `pushed_at`,
unscoped per `Gap 471`) for metadata and by a **`raw.githubusercontent.com` GET** for payload. Both
channels were used for every row below. `curl -sI` against `github.com` is to be recorded as dead
for this purpose, not retried.

### 🔴 The live top tier, licence-first — 6 of 14 are build-on-able

🔵 Stars from MCP `search_repositories`, **2026-10-27**. Licence column names the **path read
first-hand** and its measured byte count. 🔴 Sorted by what Globant may build on, not by stars.

| Agent | Repo | Licence (path read, bytes) | Stars | Region | What it is |
|---|---|---|---|---|---|
| **DeepTutor** | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | 🟢 **Apache-2.0** — `main/LICENSE`, 11,408 B | **44,177** | APAC | Multi-agent lifelong personalised tutoring over graph-RAG; HKU Data Intelligence Lab. 🔴 **Now the largest education repository this base has ever carried**, and it is APAC-origin |
| **book-to-skill** | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | 🟢 **MIT** — `master/LICENSE.md`, 1,068 B | **36,206** | Global | Turns a technical book PDF into an agent skill with retrievable structure; created 2026-05-01 |
| **get-it** | [beltromatti/get-it](https://github.com/beltromatti/get-it) | 🟢 **Apache-2.0** — `main/LICENSE`, 11,359 B | 1,135 | EMEA | Feynman-technique study agent over a knowledge graph; built at **GDG AI Hack Milan 2026**, Italy |
| **Papermorph** | [DozenTwelve/Papermorph](https://github.com/DozenTwelve/Papermorph) | 🟢 **MIT** — `main/LICENSE`, 1,069 B | 961 | Global | Turns books into animated, narrated interactive web lessons; emits SCORM |
| **claudemy** | [assafkip/claudemy](https://github.com/assafkip/claudemy) | 🟢 **MIT** — `main/LICENSE`, 1,069 B | 466 | Global | Researches a topic and builds a course of 2-minute cited audio lessons |
| **ai-shifu** | [ai-shifu/ai-shifu](https://github.com/ai-shifu/ai-shifu) | 🟢 **Apache-2.0** — `main/LICENSE.txt`, 11,342 B | 329 | APAC | Conversational teaching agent, China-origin; multilingual teaching loop |
| **tutor-gpt** | [plastic-labs/tutor-gpt](https://github.com/plastic-labs/tutor-gpt) | 🟡 **GPL-3.0** — `main/LICENSE`, 35,149 B | 932 | North America | Theory-of-Mind reasoning tutor. Copyleft: service-side use is fine, redistribution is not |
| **ChatTutor** | [HugeCatLab/ChatTutor](https://github.com/HugeCatLab/ChatTutor) | 🟡 **AGPL-3.0** — `main/LICENSE`, 34,522 B | 1,315 | APAC | Visual, interactive STEM tutor. 🔴 AGPL reaches **network use** — hosting it for a client triggers source disclosure |
| **frametell** | [sitor-ai/frametell](https://github.com/sitor-ai/frametell) | 🟡 **AGPL-3.0** — `main/LICENSE`, 34,523 B | 412 | Global | Local-first explainer-video director agent, any model |
| **education-agent-skills** | [GarethManning/education-agent-skills](https://github.com/GarethManning/education-agent-skills) | 🟡 **CC BY-SA 4.0** — `main/LICENSE`, 1,230 B | 914 | EMEA | 165 evidence-grounded teaching skills. 🔴 **A content licence, not a code grant**: commercial use allowed, but derivatives must ship CC BY-SA |
| **Auto-Empirical-Research-Skills** | [brycewang-stanford/Auto-Empirical-Research-Skills](https://github.com/brycewang-stanford/Auto-Empirical-Research-Skills) | 🟡 **CC BY-SA 4.0** — `main/LICENSE`, 620 B | 4,788 | North America | 23,000+ empirical-research skills across 8 social-science disciplines; Stanford REAP / CoPaper.AI |
| **PageLM** | [CaviraOSS/PageLM](https://github.com/CaviraOSS/PageLM) | 🔴 **"PageLM Community License" — NON-COMMERCIAL** — `main/LICENSE.md`, 8,563 B | 2,049 | Global | Community NotebookLM: quizzes, flashcards, notes, podcasts. 🔴 **Bespoke licence inside an otherwise open-looking repo.** Its own text bars *"use in software-as-a-service offerings"* and any revenue-generating use. **Unusable in a paid engagement** |
| **Mr.-Ranedeer-AI-Tutor** | [JushBJJ/Mr.-Ranedeer-AI-Tutor](https://github.com/JushBJJ/Mr.-Ranedeer-AI-Tutor) | 🔴 **UNGRANTED** — no licence at 6 root paths; `package.json` 404, `pyproject.toml` 404; no grant in `README.md` | **29,550** | Global | 🔴 **The most-starred AI tutor on GitHub carries no licence at all.** Default copyright: no right to copy, modify or deploy |
| **ai-ethos** | [aaryansamanta/ai-ethos](https://github.com/aaryansamanta/ai-ethos) | 🔴 **UNGRANTED** — no licence at 6 root paths | 498 | North America | 501(c)(3) multilingual tutoring for underserved learners, 7 languages. 🔴 Describes itself as open-source; grants nothing |

### 🔴 The census, stated as a number

| licence class | agents | share | Globant can build on it? |
|---|---|---|---|
| 🟢 Permissive (MIT / Apache-2.0) | 6 | **42.9 %** | Yes |
| 🟡 Copyleft (GPL-3.0 / AGPL-3.0) | 3 | 21.4 % | Only with a licence-boundary design — see `compose/patterns.md` `P2` |
| 🟡 CC BY-SA 4.0 (content, no code grant) | 2 | 14.3 % | Commercially yes, but derivatives ship share-alike |
| 🔴 Non-commercial | 1 | 7.1 % | **No** |
| 🔴 Ungranted | 2 | **14.3 %** | **No** |

🔴 **The two headline numbers of this shelf are 29,550 and 2,049, and neither is usable.** 🟢 The
operative finding for an engagement: **capability is not the constraint on this shelf — the grant
is**, and star rank is anti-correlated with usability at the top. A studio that picks the
best-known education agent by stars picks an ungranted one twice over.

### 🔵 Declared gaps on this shelf

- 🔴 **No LATAM-origin education agent surfaced.** The only LATAM-origin education repository found
  in this window is [menthorlabs/menthor](https://github.com/menthorlabs/menthor) (Brazil,
  Apache-2.0 `main/LICENSE` 11,337 B, 582★) and it is **archived / read-only**. Recorded as an
  informed gap, not as coverage.
- 🔵 **No open-source education-AI evaluation harness surfaced** at any star floor — searched
  `education agent`, `topic:edtech`, `topic:education-ai`, `topic:lms`, `grading topic:education`.
  Carried forward from prior passes; still unfilled.

## 🆕 `p471` — **🟢 THE CHANNEL THIS BASE HAS RECORDED AS "`api.github.com`: 403, BLOCKED" FOR 470 PASSES IS NOT BLOCKED — IT IS PER-REPOSITORY AUTHORISED, and the mechanism is readable in the refusal body. 🔴 `Gap 470-A`'s own prescription is REFUTED: the "ships a plugin or integration" heuristic it proposed is ANTI-predictive (8.6 % against the control's 26.0 %); the real predictor is repository SIZE, monotonic across five bands from 0.0 % to 66.7 %. 🔴 And a root-path probe does not merely miss copyleft below the root — it has published **"NO GRANT"** on a row standing on the SELL shelf that is granted GPL-3.0 two directories down.**

🔵 **Gate posture, per `Gap 446-A`:** `make hooks` not attempted — the industry KB is cloned outside
the harness repo this pass. **Nothing below is gate-attested.** The checks were re-implemented in
this session's own code and are green: frontmatter keys and closed-vocabulary `region` on all eight
shelves; every new table checked for separator presence and pipe-count consistency, with **no header
row published as data**; append-only proved on both trending shelves by prior-body containment.

🔵 **`Gap 468-A` honoured.** No payload below was measured through a shell variable: every licence
body was written to a file and the file measured, so trailing bytes survive.

### 🔴 The channel record this base has carried for 470 passes is mechanistically wrong

🔵 Every pass since `p1` has recorded `api.github.com` as **403 / blocked**, and `p458` through
`p470` treated that as a property of the host or of GitHub. It is neither. Probed four ways this
pass, the channel separates cleanly — and the refusal body names the rule:

| probe | code | bytes | reading |
|---|---|---|---|
| `GET api.github.com/` | **200** | **2** | 🔴 **FALSE POSITIVE.** The payload is `{}` — a proxy stub. A liveness probe that checks the root for HTTP 200 reports this channel **UP** while it is unusable |
| `GET /repos/gmilano/education-kb` (**attached**) | **200** | 6 055 | 🟢 **Full payload**, `stargazers_count`, `default_branch`, `pushed_at` |
| `GET /repos/panaversity/ksor` (**unattached**) | **403** | 378 | 🔴 *"GitHub access to this repository is not enabled for this session. Use `add_repo` to request access."* |
| `GET /search/repositories` | **403** | 249 | 🔴 *"sessions are bound to their configured repositories."* |

🔴 **So the record should read: `api.github.com` is per-repository authorised, not blocked.** The
403 is an authorisation scope, and it is liftable per repository. That is a different fact with a
different consequence, and 470 passes of "blocked" concealed it.

🔴 **And the first probe is the one to keep.** This pass's own opening move was `curl` against
`api.github.com/` — it returned **200**, and for a few minutes this section was going to announce a
channel recovery. The 200 is two bytes of proxy stub. 🟢 Registered as **`Gap 471-A`**: a channel
liveness probe must assert on a **payload the channel alone could produce**, never on a status code
from a service root, because an intermediary can satisfy the status code without the service.

### 🟢 The asymmetry inside one server, which is the usable half

| channel | third-party repos | what it serves |
|---|---|---|
| MCP `github` → `search_repositories` | 🟢 **UNSCOPED** | `q=moodle` → `total_count` **35 732**, with live `stargazers_count`, `forks_count`, `pushed_at`, `archived`, `default_branch` |
| MCP `github` → `get_file_contents` | 🔴 **SCOPED** | *"repository is not configured for this session"* |
| `api.github.com` direct | 🔴 **SCOPED** | 403 unless attached |

🔵 Two tools in the **same MCP server** carry different scopes. Search reaches all of GitHub;
contents reaches two repositories. The practical consequence for every future pass: **metadata
discovery is global, payload reads are not** — so star counts and recency come from the search tool
and every licence body still comes from `raw.githubusercontent.com`, which is exactly the split this
pass used.

### 🔴 A zero on that channel is indistinguishable from a dead channel, and this pass nearly filed one

🔵 The first discovery leg of the pass, `education AI tutor agent stars:>50 pushed:>2026-09-01`,
returned `total_count: 0`, `incomplete_results: false`, **no error**. Read alone, that is the
saturation nil this base has published six times. It is not one:

| leg | free-text terms | qualifiers | `total_count` |
|---|---|---|---|
| `education AI tutor agent stars:>50 pushed:>2026-09-01` | 4 | 2 | 🔴 **0** |
| `AI tutor education stars:>50` | 3 | 1 | 🟢 11 |
| `education agent pushed:>2026-09-01` | 2 | 1 | 🟢 **1 075** |
| `moodle` | 1 | 0 | 🟢 **35 732** |

🔴 **The qualifiers are not what zeroes it — the free-text term count is.** GitHub ANDs free-text
terms across name, description and README; four of them co-occurring in one education repository is
close to empty before any `stars:` or `pushed:` bound applies. 🟢 Registered as **`Gap 471-B`**:
every discovery leg must carry a **positive control** in the same channel and the same call shape,
because on this channel a legitimate empty result and a broken channel are byte-identical. This is
`p468`'s vocabulary finding on a third axis — not the language of the query, not its register, but
its **arity**.

### 🟢 `Gap 470-A` CLOSED — by enumerating the tree instead of guessing paths

🔵 `Gap 470-A` asked for the grant to be re-read "at that subtree", with the README's licence
heading as "the cheapest index to which subtrees to check". That is a heuristic over an unknown set.
The instrument this pass built does not need the index: a **blobless shallow clone**
(`git clone --depth 1 --filter=blob:none`) materialises the full path list without a single file
body, and `git ls-files` then yields **every** licence-shaped path at **any** depth. It cost no API
access and it works on repositories the API refuses.

🟢 **Validated against `p470`'s own case before being trusted — and it beats it.** At the identical
HEAD `6bc743c6a5fe`, `p470` published three paths for `mgarlabx/edukors_graph`. The instrument
returns **four**:

| path at `6bc743c6a5fe` | payload | class |
|---|---|---|
| `LICENSE.md` | **1 087 B** · `625342dc4d3d` | **MIT** — 🟢 reproduces `p470` to the digit |
| `plugin/edukorsplayer/COPYING.txt` | 35 151 B · `e79e9c8a0c85` | **GPL-3.0-or-later** |
| `plugin/edukorsplayer/THIRD_PARTY.md` | 785 B · `42e7a91016b6` | notices |
| 🔴 `plugin/edukorsplayer/vendor/edukors/LICENSE.md` | **1 087 B** · `625342dc4d3d` | 🔴 **MIT — byte-identical to the root**, re-vendored *inside* the GPL subtree |

🔴 **So `edukors_graph` is three layers, not two:** MIT at the root, GPL-3.0-or-later for the Moodle
plugin, and the original MIT grant restored for the `edukors` component vendored *within* that
plugin. For a studio that is the useful layer — the vendored component stays extractable under MIT
even though the plugin shipping around it is GPL — and no root-path probe and no README heading
would have found it.

### 🔴 The prediction this pass registered, and its refutation

🔵 Stated before the run: the at-risk tier (names matching `moodle|canvas|plugin|lti|integration|vendor|connector|mcp|edx|chamilo|ilias`) would partition at **≥ 15 %** and the control at **≤ 5 %**. Swept over **229** of 237 shelf addresses that cloned:

| tier | basis | n | partitioned | rate | prediction |
|---|---|---|---|---|---|
| at-risk | name matches the plugin/integration vocabulary | 152 | 13 | **8.6 %** | 🔴 **refuted** |
| control | every 7th remaining shelf address | 77 | 20 | **26.0 %** | 🔴 **refuted, and inverted** |

🔴 **The heuristic is worse than no heuristic — it is anti-predictive**, and the mechanism is that
the vocabulary selects *small single-purpose connectors*: ~130 of the 152 at-risk addresses are
one-endpoint MCP servers with one root `LICENSE` and no subtree at all. The name says "integration";
the tree says 20 files.

### 🟢 What does predict it, with a denominator — and it is computable before any licence is read

| tree size (paths) | n | partitioned | rate |
|---|---|---|---|
| < 25 | 44 | 0 | **0.0 %** |
| 25–99 | 82 | 4 | **4.9 %** |
| 100–499 | 58 | 6 | **10.3 %** |
| 500–1 999 | 27 | 11 | **40.7 %** |
| ≥ 2 000 | 18 | 12 | **66.7 %** |

🟢 **Monotonic across all five bands, no exceptions.** Shelf-wide: **33 of 229 repositories
(14.4 %)** carry a grant below the root, across **580** anchored licence paths. The operational form
is one line — `git ls-files | wc -l` — and it is available *before* reading any licence: **under 25
paths, a root read is sufficient; over 500, a root read is more likely wrong than right.**

### 🔴 This pass's own matcher was defective, at 44.4 %, and the controls caught it

🔵 The first cut matched the licence tokens as substrings anywhere in a basename. On
`jude-miller-dev/Milky-institute-online` it returned **18 grants** that are Java and XML source
files — `NoticeTaskController.java`, `NoticeTemplateDTO.java`, `NoticeTaskMapper.xml` — because
`NOTICE` is a prefix of `NoticeTask`.

| matcher | matches | repos affected | false positives | rate |
|---|---|---|---|---|
| naive, unanchored substring | 1 044 | 23 | **464** | 🔴 **44.4 %** |
| anchored basename | **580** | 0 | 0 | 🟢 0.0 % |

🔴 **Nearly half of the first run's "licence paths" were not licences.** The corrected matcher
requires the basename to *be* the token, optionally followed by an extension or a licence-name
suffix (`LICENSE-MIT`, `COPYING.txt`). Every number in this section is the anchored one. 🔵 Both
matchers are kept in `evidence/matcher-false-positive.2026-10-27-p471.tsv` so the rate is checkable
rather than asserted.

### 🔴 Three classes of subtree grant — and the discriminator is the COPYRIGHT HOLDER, not the licence family

🔵 A subtree grant does not mean the repository is granted. Four repositories carry **no root grant
and a real licence payload below it**, and they fall into three distinct classes with opposite
consequences:

| repo | ★ | subtree payload, read first-hand | class | effect on the shelf |
|---|---|---|---|---|
| [`formalms/formalms`](https://github.com/formalms/formalms) | 37 | `html/license.txt` **GPL-2.0** · 18 346 B · `4e63feff285d` (+ 9 further language copies) | 🟢 **R — recovered** | 🔴 **Contradiction resolved.** `agents/top.md` carried *"no licence payload at 10 paths → REFUSED"*; `agents/trending.md` carried *GPL-2.0 recovered in-tree*. The trending shelf was right |
| [`particify/arsnova-server`](https://github.com/particify/arsnova-server) | 67 | `core/LICENSE` **GPL-3.0** · 35 147 B · `8ceb4b9ee5ad` | 🟢 **R — recovered** | 🔴 **SELL-SHELF CORRECTION** — see below |
| [`particify/arsnova-server`](https://github.com/particify/arsnova-server) | 67 | `formatting/LICENSE` · **133 B** · `747c3a657b2b` — *"Copyright (c) 2020-present Particify … All rights reserved."* | 🔴 **X — reservation** | 🔴 A subtree can make a repository **less** usable, not more |
| [`Chloris-Blaxk/inno-agent-hub`](https://github.com/Chloris-Blaxk/inno-agent-hub) | 13 | 37 paths; `homework-grader/LICENSE` MIT 1 068 B `8755221656d4` **© ChantillyAn**; `math-tutor` + `tutor` MIT 1 062 B `daf4ed4cc059` **© Artem**; `k12-lesson-planning` **Apache-2.0** 11 357 B; `socratic-tutor` **EPL-2.0** 14 197 B | 🟡 **V — vendored third-party** | 🟢 **`Gap 395-D` CLOSED** — see below |
| [`Takamatsu-Hikaru/AI-Research-Guide`](https://github.com/Takamatsu-Hikaru/AI-Research-Guide) | 181 | `public/blog/guide/wiki/vendor/LICENSE.txt` MIT 1 051 B `70d37354d639` **© 2022 Luca Ongaro** | 🟡 **V — vendored third-party** | 🟢 **Refusal STANDS.** A naive subtree reader would have "recovered" this row and been wrong |

### 🔴 The sell-shelf correction, stated plainly

🔵 `verticals/solutions.md` publishes **ARSnova** with *"🔴 **NO GRANT** at 10 paths, none in
`build.gradle.kts` or `gradle.properties`"*, and `agents/top.md` says the same. Both are wrong, and
wrong in **both directions**:

- 🟢 `core/LICENSE` is **GPL-3.0**, 35 147 B · `8ceb4b9ee5ad` — and that digest is **this base's own
  canonical GPL-3.0 cell**, the one it records for `moodle/moodle` and Chamilo. A cross-pass control
  passes on a repository these shelves had never read for GPL.
- 🔴 `formatting/LICENSE` names **Particify itself** and reserves all rights. A studio vendoring
  `arsnova-server` wholesale would ship that module.

🟡 **The honest bound on the recovery.** The base's own warning that *"All rights reserved"* is stock
BSD-3 boilerplate was applied: at **133 B** this payload carries a copyright line, the reservation
sentence and **no permission grant of any kind** — a BSD-3 body is ~1.5 KB. So the reservation is
real. But the converse is weaker than it looks: a **GPL payload carries the FSF's copyright, not the
project's**, so the copyright-holder test that settles the `V` class above is *unavailable* for
copyleft texts. That `core/LICENSE` grants the `core` module rests on the subtree's position in the
tree, not on a name in the payload. 🟢 Registered as **`Gap 471-C`**: for a copyleft payload found
below the root, the grant's **scope** is not determined by the payload, and the cheapest closure is
the project's own `README`/`COPYRIGHT` notice rather than the licence body.

### 🟢 `Gap 395-D` CLOSED after 76 passes — and not in the direction it was framed

🔵 `Gap 395-D` has read since `p395`: *"the pass's best address is MIT and the part a studio would
actually reuse is ungranted."* For `inno-agent-hub` the reusable parts **are** granted — and not by
the hub. Proved by digest equality rather than inferred:

| path | bytes · digest | copyright line |
|---|---|---|
| `ChantillyAn/homework-grader` → `LICENSE` (root) | **1 068 B · `8755221656d4`** | `Copyright (c) 2026 ChantillyAn` |
| `inno-agent-hub` → `skill-library/homework-grader/LICENSE` | **1 068 B · `8755221656d4`** | `Copyright (c) 2026 ChantillyAn` |

🟢 `cmp` reports the two files **identical**. The hub's `math-tutor` and `tutor` both read
`Copyright (c) 2026 Artem` — a second third party, and the shared digest `daf4ed4cc059` shows they
are one grant copied twice. 🔴 **Every subtree grant in the hub names someone other than its owner.**
So the closure is: the hub grants **nothing**; the skills are granted **by their upstreams**; and the
studio route is to vendor from upstream, which the licence digest identifies for free. 🔵 This is
`p446`'s LINEAGE mechanism confirmed on a new instance, with the digest as the index.

### 🟢 Granted novel rows this pass — read first-hand at `HEAD`, `2026-10-27`

🔵 Two rows, and the count is the finding rather than a shortfall: the discovery legs returned **14
candidates on the general education vocabulary and 0 of 14 were unshelved**. Both additions came
from a single licence-filtered rubric leg.

| repo | grant (first-hand) | bytes · digest | ★ | ref | region | what it contributes |
|---|---|---|---|---|---|---|
| [`TREMA-UNH/rubric-grading-workbench`](https://github.com/TREMA-UNH/rubric-grading-workbench) | **MIT** | 1 068 B · `3f68bfcd4ec5` | 15 | `main` `13aaed5161ec` | **North America** | Autograding workbench for retrieve/generate systems from the University of New Hampshire — the first **academic-provenance** rubric component on these shelves, and the only one whose evaluation design is published rather than asserted |
| [`ChantillyAn/homework-grader`](https://github.com/ChantillyAn/homework-grader) | **MIT** | 1 068 B · `8755221656d4` | 7 | `master` `5e9aab47822f` | Global | Rubric-driven homework grading with chain-of-thought scoring, explicit bias mitigation and a PDCA quality cycle. 🟢 The **upstream** of the skill vendored in `inno-agent-hub`, identified by digest |

🔵 Both carry a **single root grant and no subtree partition** — the instrument was run on each, at
26 and 73 paths respectively, which the size band above predicts (< 100 paths → 4.9 %).

### 🔴 Refused this pass — stated, because a silent refusal reads like a miss

| candidate | probe at `HEAD` | why refused |
|---|---|---|
| [`cobibean/soul-grader-skill`](https://github.com/cobibean/soul-grader-skill) | `main` `56fdda5c57e2` · **MIT** · 1 065 B · `f1319ce8b6ac` · **60★** | 🔴 **Off-class.** Grades `SOUL.md` agent-identity files against a rubric — not student work. Granted, live and the highest-starred thing the rubric leg returned, and not an education asset. `p453`'s homonym class, on a licence-filtered leg |

### 🔵 The governance gap, confirmed on an independent channel with a denominator

🔵 `p468` and `p470` both concluded that the governance shortfall is an absence of **supply** rather
than of discovery. Reproduced here on the newly-proved channel: `education governance license:mit`
returns **61 repositories in total**, whose **maximum star count is 16**, and of the top eight
returned, five are off-class (DeFi/web3 token platforms, a climate atlas). 🟢 Same conclusion, new
channel, and now with a ceiling attached rather than an impression.

### 🟢 Open gaps registered by this pass

| gap | statement | cheapest closure for the next pass |
|---|---|---|
| **`471-A`** | A liveness probe must assert on a payload only the channel could produce, never a status code from a service root — `api.github.com/` returns 200 with 2 bytes of proxy stub | Re-probe the four channels with payload assertions and record the matrix again |
| **`471-B`** | On `search_repositories` a legitimate empty result and a broken channel are byte-identical; free-text **arity**, not qualifiers, drives legs to zero | Carry a positive control (`q=moodle`) in every discovery leg; declare a nil only when the control returns |
| **`471-C`** | For a copyleft payload below the root, the payload cannot establish the grant's **scope**, because the copyright line is the FSF's | Read `arsnova-server`'s own README/COPYRIGHT notice and settle whether GPL-3.0 covers the repository or only `core/` |
| **`471-D`** | The 8 of 237 addresses that failed to clone are untyped — `chamilo/chamilo`, `openedx/openedx-mcp` and six others returned no tree | Re-run the blobless clone on those 8; separate "large/slow" from "gone" with `git ls-remote` |
| **`471-E`** | The size-band screen is measured on 229 addresses from one industry; its monotonicity is untested elsewhere | Run `git ls-files \| wc -l` banding on another industry KB's shelf when the rotation reaches it |

## 🆕 `p470` — **🔴 A GRANT CAN BE PARTITIONED BY SUBDIRECTORY, AND THE 13-PATH ROOT PROBE THIS BASE SPENT FIVE PASSES REFINING CANNOT SEE IT: `mgarlabx/edukors_graph` serves MIT at `LICENSE.md` and **GPL-3.0-or-later** at `plugin/edukorsplayer/COPYING.txt`, both read first-hand. 🟢 And the governance substrate `p468` said these shelves lacked is found and granted: `panaversity/ksor`, Apache-2.0, 232★, naming education institutions in its own first paragraph.**

🔵 **Gate posture, per `Gap 446-A`:** `make hooks` not attempted — the industry KB is cloned
outside the harness repo this pass. **Nothing below is gate-attested.** The checks were
re-implemented in this session's own code and are green: frontmatter keys and closed-vocabulary
`region` on all eight shelves; every new table checked for separator presence and pipe-count
consistency, with **no header row published as data**; append-only proved on both trending shelves
by prior-body containment.

🔵 **Channel state, re-probed this pass (`2026-10-27`).** `api.github.com` direct: **403**, for the
470th pass. `raw.githubusercontent.com`: **200**, every licence payload below. `git ls-remote
--symref`: working, every default ref and `HEAD` below. Session GitHub tool channel: working, every
star count below. 🔴 `eur-lex.europa.eu`, `ec.europa.eu`, `europa.eu`, `op.europa.eu` and
`artificialintelligenceact.eu`: **DNS `ENOTFOUND` on both `curl` and the page-fetch channel** — see
`intel/market.md` for what that did and did not prevent.

🟢 **`Gap 468-A` honoured.** No payload below was measured through a shell variable: every licence
body was written to a file and the file measured, so trailing bytes survive.

### 🔴 The headline: a grant split across directories

🔵 [`mgarlabx/edukors_graph`](https://github.com/mgarlabx/edukors_graph) presents as a clean MIT
row. Its root `LICENSE.md` is stock MIT — **1 087 B · `625342dc4d3d`** — and the GitHub licence
field says `MIT`. Both are true and both are incomplete.

| path read at `main` `6bc743c6a5fe` | payload | class, read first-hand |
|---|---|---|
| `LICENSE.md` | **1 087 B** · `625342dc4d3d` | **MIT** — the schema, the standalone player, original Edukors resources |
| `plugin/edukorsplayer/COPYING.txt` | **35 151 B** · `e79e9c8a0c85` | 🔴 **GPL-3.0-or-later** — the Moodle integration |
| `plugin/edukorsplayer/THIRD_PARTY.md` | **785 B** · `42e7a91016b6` | reused MIT code retains its own notices |

🔴 **Why the root probe misses it.** This base's licence instrument probes up to thirteen paths —
all of them at the repository root. Every one of them returns the MIT payload, correctly, and the
probe stops. The GPL grant is two directories down, and **nothing at the root hints that a second
grant exists**. The only thing that reveals it is the README's own `# License` heading, which this
pass read:

> *The schema, standalone player and original Edukors resources are licensed under the MIT License
> — see LICENSE.md. The Moodle integration in `plugin/edukorsplayer/` is GPL-3.0-or-later — see
> `plugin/edukorsplayer/COPYING.txt`.*

🔵 The split is not evasive, it is **forced**: Moodle is GPL, so any Moodle plugin must be GPL. That
is the general case, and it is why this will recur — every permissive education project that ships
an LMS integration has this shape waiting inside it. 🟢 Registered as **`Gap 470-A`**: a root-path
licence sweep establishes the grant on the *root tree only*. Where a repository ships a plugin,
integration or vendored subtree, the grant must be re-read at that subtree, and the README's own
licence heading is the cheapest index to which subtrees to check.

🟢 **For a studio this is usable, and the boundary is where it falls:** vendor the JSON schema and
the standalone player under MIT; the moment the Moodle plugin ships, that artefact is
GPL-3.0-or-later.

### 🟢 Granted novel education agents — every grant read first-hand at `HEAD`, `2026-10-27`

| agent | repo | grant (read first-hand) | ★ | region | what it does |
|---|---|---|---|---|---|
| KSoR | [`panaversity/ksor`](https://github.com/panaversity/ksor) | **Apache-2.0** · 11 342 B · `2f538e0b9e84` | **232** (51f) | APAC (Panaversity) | **Knowledge System of Record**: one governed, authoritative knowledge record that humans and agents operate from. Its own second paragraph is about education — "tutors, teaching assistants, and assessment agents operate from different curricula, sources, or rules". Topics include `ai-governance`. TypeScript, `main` `b50f28926fae` |
| Edukors Graph | [`mgarlabx/edukors_graph`](https://github.com/mgarlabx/edukors_graph) | 🟡 **MIT root + GPL-3.0-or-later plugin** — see the split above | 17 (2f) | **LATAM** (BR) | Open standard for **learning graphs**: a course as nodes (what the student sees) and edges (where they go next), one JSON file, diagnose-and-branch. PHP + JSON Schema, self-described **Experimental**. Pushed 2026-10-25 |
| Education Advisor (教育参谋) | [`232252/education-advisor`](https://github.com/232252/education-advisor) | **MIT** · 1 090 B · `703786ab8abd` | 4 (2f) | APAC (CN) | Local desktop assistant **for the class head-teacher**, not the student: conduct scores, counselling plans, weekly reports, parent-school scripts, academic analysis, AI homework marking. 18 roles, Electron + React + Rust, bring-your-own model, data stays local. Pushed 2026-10-25 |
| aula | [`NouhKhouyi/aula`](https://github.com/NouhKhouyi/aula) | **MIT** · 1 068 B · `b208dbc2fdee` | 2 | Global | Local-first agent harness that **probes what the learner knows**, plans the shortest route to the goal, and checks each step lands before moving. Topics `ai-tutor`, `agentsmd`. Pushed 2026-10-26 |
| ZYREN AI Tutor | [`MONaser04/Zyren-AI-Tutor`](https://github.com/MONaser04/Zyren-AI-Tutor) | **MIT** · 1 085 B · `aa716156b15d` | 2 | **EMEA** (Egypt) | Real-time multimodal Socratic tutoring: LiveKit WebRTC voice, screen perception, digital blackboard, 3D WebGL geometry, KaTeX. v2.0.0, 55 tests. Arabic-language support named throughout its README |
| 活书 huoshu | [`MXC-CKK/huoshu`](https://github.com/MXC-CKK/huoshu) | **MIT** · 1 059 B · `a005f12beb1c` | 3 | APAC (CN) | Turns a textbook into a navigable **knowledge graph**: AI graph build, Socratic questioning, RAG retrieval, spaced repetition. Python, 401 tests passing, published to PyPI as `learning-agent` |
| SyllabusGraph | [`OscarBarreraGithub/syllabusgraph`](https://github.com/OscarBarreraGithub/syllabusgraph) | **MIT** · 1 083 B · `3cc3fae03d97` | 1 | Global | **Evidence-backed** concept graph and course planner: builds concepts and relationships *with source evidence*, independent review step, then shapes a course. Driven from Codex/Claude Code; keeps source books private |
| Curriculum Knowledge Graph | [`mizcausevic-dev/curriculum-knowledge-graph`](https://github.com/mizcausevic-dev/curriculum-knowledge-graph) | **MIT** · 1 069 B · `a5ed17e0b90a` | 1 | Global | FastAPI service over courses, prerequisites, skills and outcomes with **prerequisite bottleneck analysis** for higher ed. 🟡 Portfolio-tier: its README's own section is "Why This Repo Is Good" and it pairs with a sibling showcase repo |
| Bodhi Map | [`AI-First-Community/Bodhi`](https://github.com/AI-First-Community/Bodhi) | **MIT** · 1 095 B · `967480f4f094` | 5 (1f) | Global | Interactive knowledge graph of modern AI — 123 concepts, tokens and attention through LoRA, DPO, reasoning models and agents, typed connections. Installable PWA |
| DMAS | [`gmtigrisva123/DMAS`](https://github.com/gmtigrisva123/DMAS) | **MIT** · 1 087 B · `3a7f63107f13` | 1 | Global | Deductive multi-agent system aimed at moving AIEd from answer-generation to **cognitive diagnostics** and behavioural inference |
| GitLearnOS | [`Guojiz/gitlearnos`](https://github.com/Guojiz/gitlearnos) | **MIT** · 1 063 B · `8b1ba1377eaa` | 7 | Global | Git-native learning environment: targeted practice, local RAG, **learner-owned memory** held in the learner's own repository |
| extend-slides | [`L01nki1/extend-slides`](https://github.com/L01nki1/extend-slides) | **MIT** · 1 064 B · `17dcc81817e1` | 16 | APAC (CN) | Expands courseware, handouts and lecture recordings into standalone revision documents |
| KuroTutor | [`ZYT64/KuroTutor`](https://github.com/ZYT64/KuroTutor) | **MIT** · 1 079 B · `d797049c4e6a` | 4 | APAC (CN) | Tutor delivered **inside a chat client**: photo problem-solving, homework marking, wrong-answer review, scheduled lessons |
| exam-kit | [`Tissue-for-charlie/exam-kit`](https://github.com/Tissue-for-charlie/exam-kit) | **MIT** · 1 075 B · `3cd67a7398b6` | 3 | APAC (CN) | Agent skill (`SKILL.md`): slides, Word, PDF or a blackboard photo into a printable revision outline, self-test bank and knowledge graph — **offline, three printable HTML files** |
| open-book-exam-pack | [`X1a0heZzzz/open-book-exam-pack`](https://github.com/X1a0heZzzz/open-book-exam-pack) | **MIT** · 1 056 B · `1126322e2cc8` | 4 | APAC (CN) | Agent skill building open-book exam revision PDFs from courseware, past papers and **verified textbook page indexes** |
| benkyo | [`youseiushida/benkyo`](https://github.com/youseiushida/benkyo) | **MIT** · 1 068 B · `7fe4879acb36` | 2 | Global | Textbook into adaptive tutoring: knowledge graphs, problem-first sequencing, memory across sessions |
| recall | [`Garuda8887/recall`](https://github.com/Garuda8887/recall) | **MIT** · 1 099 B · `0bfc98ccf58b` | 5 | Global | Self-hosted spaced-repetition calendar: SM-2 scheduling, forgetting curves, knowledge graph. Privacy-first, self-hosted |
| manim-coding-skill | [`shihabshahrier/manim-coding-skill`](https://github.com/shihabshahrier/manim-coding-skill) | **MIT** · 1 065 B · `5ce7ed6c2a3e` | 5 | Global | Agent skill producing **ManimGL STEM animations** — the explainer-video half of a tutoring stack. Default ref `master` |
| song-hao-math | [`tong666-bit/song-hao-math`](https://github.com/tong666-bit/song-hao-math) | **MIT** · 1 083 B · `f01123fc5f24` | 4 | APAC (CN) | University and postgraduate-entrance mathematics drill agent: calculus, linear algebra, probability, complex analysis; step-by-step board work, counterexamples, theorem conditions |
| tandemcode-harness | [`Djbrl/tandemcode-harness`](https://github.com/Djbrl/tandemcode-harness) | **MIT** · 1 062 B · `d62944c6f3f9` | 1 | Global | Interactive learning harness: notes, drawing on screenshots, pluggable open-weight models |

🔵 **Twenty rows, twenty grants, twenty first-hand reads.** Every one is novel to these shelves —
graded by **anchored** address per `Gap 469-B`, so no row here is a substring artefact.

🔴 **The other half of that number, stated here and not buried.** One row is above 20★
(`panaversity/ksor`, 232). Of the remaining nineteen, **sixteen are at 5★ or below** and twelve are
single-maintainer. These are **fork-and-own starting points**, not dependencies to take and track
downstream. The pattern `Gap 464-A`'s closure established holds for a third consecutive pass:
*permissive education supply exists in quantity and almost none of it exists at scale.*

### 🟢 `p467`'s unsolvable substitution is solvable — and the catch is the star axis

🔵 `p467` recorded that the obvious build for a curriculum-aligned tutor reaches for a **4 000★
knowledge graph under `CC-BY-NC-4.0`**, unusable in any paid engagement, and specified a substitute
it could not source. This pass sourced it, on a licence-filtered leg: **ten MIT curriculum- or
concept-graph projects**, all read first-hand above — `edukors_graph` (17★, the one with a standard
and a schema behind it), `chat-edu/v3` (16★), `Bodhi` (5★), `recall` (5★), `huoshu` (3★),
`exam-kit` (3★), `benkyo` (2★), `aula` (2★), `syllabusgraph` (1★), `curriculum-knowledge-graph` (1★).

🔴 **So the substitution is real and the trade is explicit.** The NonCommercial graph has no
permissive peer anywhere near its scale; it has **ten permissive peers between 1★ and 17★**. A
client engagement swaps 4 000★ of curation it may not sell for 17★ of a schema it may. 🟢 For the
recipe that wires the permissive side together, see `compose/patterns.md` this pass.

### 🟡 `Gap 469-A` reproduces on a second repository, as a CONJUNCTIVE grant

🔵 [`mathruffian-dot/taigi-teaching-agent`](https://github.com/mathruffian-dot/taigi-teaching-agent)
— `main` `6953bf35d521`, **13★** — serves a payload my size screen flagged at **1 453 B ·
`c3fa97fa9128`**, against stock MIT's ~1 070. Read to the end, as `Gap 469-A` requires: stock MIT,
then a `---` rule, then a Chinese appendix that **confines the grant to this repository's own code
and documents**. Named as staying under their own original terms: the **Ithuan Suisiann (意傳媠聲)
TTS service**, the Ministry of Education's **《臺灣台語常用詞辭典》 dictionary content and audio
files**, the `facebook/mms-tts-nan` model, and **official MOE teaching materials**.

🔴 **The code is granted; the curriculum corpus is not** — and in a 108-curriculum-aligned Taiwanese
Hokkien teaching agent, the ministry corpus and the official audio *are* the product. This is
`p464`'s conjunctive-grant class recurring, and it is now the pattern rather than the exception:
across this pass and `p464`, every curriculum-*aligned* agent whose grant was read to the end turned
out to grant its code and withhold its curriculum data. 🟢 Registered as **`Gap 470-B`**: for any
agent that claims alignment to a national curriculum, the shelf must state the grant on the
**corpus** separately from the grant on the code, because a studio can ship the second and not the
first.

### 🔴 Refused this pass — stated, because a silent refusal reads like a miss

| candidate | probe at `HEAD` | why refused |
|---|---|---|
| [`shenquan520/reading-analysis`](https://github.com/shenquan520/reading-analysis) | `main` `a63f496bc1ec` · **CC BY-NC-SA 4.0** · 17 124 B · `f5042f838c57` | 🔴 **NonCommercial.** Gaokao/CET/Kaoyan reading-comprehension skill with a 10-class distractor taxonomy and a 127-card methodology library — the best-made assessment artefact of the pass, and unusable in any paid engagement. GitHub's licence field: `NOASSERTION` |
| [`caijimiao345/study-abroad-planner`](https://github.com/caijimiao345/study-abroad-planner) | `main` `86a123f19181` · **CC BY-NC-SA 4.0** · 20 850 B · `e66c269d4819` | 🔴 **NonCommercial.** Verifies every figure against official university pages — exactly the citation-audit behaviour `intel/market.md` calls for. GitHub's licence field: `NOASSERTION` |
| [`FIY-pc/vibe-logisim`](https://github.com/FIY-pc/vibe-logisim) | `main` `a69438637ccc` · **GPL-3.0** · 35 149 B · `3972dc9744f6` | copyleft — a deployment-or-fork decision, not a build-on component. AI-assisted Logisim workbench for computer-organisation courses. Placed on `verticals/solutions.md` |
| [`lhd23333/QuizForge`](https://github.com/lhd23333/QuizForge) | `master` `10138fbfb368` · **GPL-3.0** · 35 149 B · `3972dc9744f6` | copyleft, same reason. Local-first maths/physics question-bank workbench: OCR import, Markdown management, paper assembly, safe TeX templates. Byte- and digest-identical grant to the row above |
| [`ChengshuaiZhao0/Awesome-Trustworthy-AI4Edu`](https://github.com/ChengshuaiZhao0/Awesome-Trustworthy-AI4Edu) | `main` `b0ff5eb7dc09` · **no licence at 13 paths** | ungranted — and it is the only trustworthy-AI-for-education research index the pass found, which is the loss |
| [`Pedrosasouza/AcademicFlow-Agent`](https://github.com/Pedrosasouza/AcademicFlow-Agent) | `main` `8e341c21f789` · **no licence at 13 paths** | ungranted — LangGraph/ReAct academic-management agent on Ollama, **LATAM (BR)**, and unusable. The regional loss of the pass |
| [`goncalvespedroo/sokra-tutor`](https://github.com/goncalvespedroo/sokra-tutor) | `main` `eebbc28b7569` · **no licence at 13 paths** | ungranted — Socratic tutor with persistent student memory |
| [`sayeeg-11/SahiiiDSA`](https://github.com/sayeeg-11/SahiiiDSA) | `main` `c732abed3a47` · **no licence at 13 paths** | ungranted — DSA tutoring by guided questioning rather than answers |
| [`simpleqt/radai`](https://github.com/simpleqt/radai) | `main` `0b1e8a4bbf9d` · **no licence at 13 paths** | ungranted — LangGraph platform for university course TA, question banks, learning analytics |
| [`chuantiet5-stack/zhiqi-ai-education-assistant`](https://github.com/chuantiet5-stack/zhiqi-ai-education-assistant) | `main` `369a11f9a533` · **no licence at 13 paths** | ungranted — education agent, textbook RAG, homework marking, focus monitoring |
| [`chat-edu/v3`](https://github.com/chat-edu/v3) | `main` `f44f5eeeb68b` · **MIT** · 1 064 B · `3dc45db43baf` | 🟡 granted and **abandoned**: 16★, but last pushed **2026-05-22** and its README is the unmodified `create-next-app` boilerplate. Read as a reference, never a dependency |
| [`Mereithhh/guandan-lab`](https://github.com/Mereithhh/guandan-lab) | `main` live · Apache-2.0 · 13★ | 🔴 **off-class.** A coach for Guan Dan, a card game. Returned under an education leg because it "teaches"; `p453`'s homonym finding, recurring |

### 🔴 This pass's own instrument published nine wrong assertions before publication, and the base was right

🔵 My first licence classifier labelled **two** GPL-3.0 payloads — `FIY-pc/vibe-logisim` and
`lhd23333/QuizForge` — as **`AGPL-3.0`**, and attached **seven** false restriction flags across
three rows. 🔴 **The class error is wrong in the direction that matters most**: AGPL and GPL differ
precisely on whether network use triggers a disclosure duty, which is the only licence question a
hosted engagement actually asks.

🔵 **The mechanism.** The classifier tested whether the payload *contains* the string
`GNU AFFERO GENERAL PUBLIC LICENSE`. Stock **GPL-3.0 names the AGPL three times** — at lines 552,
556 and 559 of its own text, in `13. Use with the GNU Affero General Public License`. So a
containment test on the AGPL's name labels **every GPL-3.0 repository in existence** as AGPL.

🟢 **The fix, and it is the same shape as `Gap 467-C`'s:** classify from the payload's **title**,
anchored to the first lines, never from containment anywhere in the body. Re-run title-anchored, all
28 payloads classify correctly.

🟢 **And the cross-pass control PASSES, on the largest denominator this base has used for a licence
control.** These shelves already carry `35 149 B · 3972dc9744f6` as **GPL-3.0** across **31 distinct
repositories** — `lamb-project/lamba`, `ahmedEid1/lumen`, `papillonapp/papillon-ed-core`,
`lanis-mobile/lanis-rs`, `elderguardian/maria`, `Arudchayan/adam-mcp`, `plastic-labs/tutor-gpt`,
`Koha-Community/Koha` at the 35 151 variant, and 24 more — and this pass reproduces **both
byte-values and both digests exactly**, from three repositories none of those shelves named. The
base's prior label was right; my instrument was wrong. 🟢 Registered as
**`Gap 470-C`**: a licence-family test must be anchored to the payload's title, because three
licence families name each other inside their own bodies.

🔵 **The seven wrong flags, itemised.** `NONCOMMERCIAL` and `CC-NC` fired on
`FIY-pc/vibe-logisim` and `lhd23333/QuizForge` — both on GPL's *permissive* phrase
*"noncommercially"*, which appears once in every GPL-3.0 payload. `TRADEMARK` fired on those two
and on `panaversity/ksor`, the last from Apache-2.0 §6, a clause every Apache-2.0 payload carries.
🔴 A flag that fires on every member of a licence family carries zero information, and a
NonCommercial flag that fires on a *permission* is worse than none. The corrected test matches the
restrictive form only — the licence-name token or an explicit prohibition — and on re-run it fires
on exactly the two CC BY-NC-SA rows and nothing else. Of five flag classes, **one earned its
place**: the overlong-payload flag, which is what caught `taigi-teaching-agent` above.

## 🆕 `p469` — **🔴 A WIDELY-CITED "BEST OPEN-SOURCE LMS 2026" ROUNDUP PUTS AN MIT LABEL ON AN AGPL-3.0 PLATFORM: `frappe/lms` (3 350★) serves GNU AGPLv3 at `license.txt`, read first-hand — the one licence class that would force source disclosure to every network user of a Globant-hosted build. 🟢 And the rubric-feedback gap `p464` named as unclosable IS CLOSED WITH FOUR MIT GRANTS — every one of them at 0–4★ with a single maintainer, which is the other half of the finding and is stated here, not buried.**

🔵 **Gate posture, stated first per `Gap 446-A`:** `make hooks` not attempted — the industry KB is
cloned outside the harness repo this pass. **Nothing below is gate-attested.** The checks were
re-implemented in this session's own code and are green: frontmatter keys and closed-vocabulary
`region` on all eight shelves; every new table checked for separator presence and pipe-count
consistency, with **no header row published as data**; append-only proved on both trending shelves
by prior-body containment; every address below re-resolved first-hand this pass by
`git ls-remote --symref` plus a licence-payload read at `HEAD`.

🟢 **`Gap 468-A` honoured.** No payload on this shelf was measured through a shell variable. Every
licence body was written to a file and the file measured, so trailing newlines survive. Star
counts are two-channel per `Gap 467-D`: `api.github.com` is still **403** direct from this host, and
the session GitHub tool channel served every `stargazers_count` below on **2026-10-27**.

### 🔴 The headline, with the payload behind it

| claim | source of the claim | first-hand read at `HEAD` | verdict |
|---|---|---|---|
| `frappe/lms` is **MIT** | secondary "10 Best Open-Source LMS in 2026" roundup | `license.txt` @ `develop` · **GNU AGPL v3** · 33 893 B · `db1a87ba81e8` | 🔴 **REFUTED** — AGPL-3.0, not MIT |
| `formalms/formalms` is **Apache-2.0** | same class of roundup ("disputed") | **no licence payload at 10 paths** @ `master` `446a77a9b9cb` | 🔴 **REFUSED** — ungranted, so neither label holds |
| `OpenOLAT/OpenOLAT` is **Apache-2.0** | same class of roundup | `LICENSE` @ `master` · **Apache-2.0** · 10 982 B · `6dbc5b605ed0` | 🟢 **CONFIRMED** |

🔵 The three rows came from one search leg and one source class. One was wrong in the direction
that costs a client engagement, one was wrong in both directions at once, and one was right. A
roundup's licence column is a claim, never a grant.

### 🟢 Granted education agents — read first-hand this pass, `2026-10-27`

| agent | repo | licence (read at `HEAD`) | ★ | region | what it does |
|---|---|---|---|---|---|
| DeepTutor | [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) | **Apache-2.0** · 11 408 B · `cd2f54e1e506` | 43 930 | APAC (HKU) | Lifelong personalised tutoring; multi-agent + RAG, self-hosted web app and CLI. `HEAD` `a31d82624c27`, pushed 2026-10-26 |
| OpenMAIC | [`THU-MAIC/OpenMAIC`](https://github.com/THU-MAIC/OpenMAIC) | **MIT** · 1 065 B · `ba2525637432` | 41 563 | APAC (Tsinghua) | Open Multi-Agent Interactive Classroom; one-click immersive lesson generation, TypeScript. `HEAD` `84a88bc4fda2` |
| AI Teaching Agent | [`littlecookie0722/AI-Teaching-Agent`](https://github.com/littlecookie0722/AI-Teaching-Agent) | **MIT** · 1 069 B · `297c4cba7b33` | 0 | Global | Markdown source → reviewable Lab + Exam + grading package and slides; structured DSLs, sandboxed eval, **CLI/MCP tools**, human-review stop line. 4.3 MB tree, `HEAD` `b90bd88a2899` |
| GradeAI | [`vijju9019/GradeAI`](https://github.com/vijju9019/GradeAI) | **MIT** · 1 077 B · `6a1c56b153f8` | 0 | Global | Rubric-criterion exam evaluation with a **human-in-the-loop teacher review cockpit**, split-screen rubric comparison, score override. FastAPI + React 19. Created **2026-10-25** |
| GradeMate | [`laurauguc/grading_assistant`](https://github.com/laurauguc/grading_assistant) | **MIT** · 1 072 B · `3b21045edbad` | 4 | North America | Teachers apply curated rubrics or upload their own to grade written work; React + Django, live hosted demo. Last push 2025-08-11 |
| EduRAG | [`ThallesYVasconcelos/Agente-Educacional`](https://github.com/ThallesYVasconcelos/Agente-Educacional) | **MIT** · 1 089 B · `5eaa67118ee6` | 0 | **LATAM** (Brazil) | Agentic RAG for Brazilian *Anos Iniciais* teachers, grounded in **BNCC, PCN and PNLD** with page citations; generates EF01–EF04-aligned lesson plans. LangGraph + local models via Ollama |
| IA para Aprender | [`insolitos/IA_para_aprender`](https://github.com/insolitos/IA_para_aprender) | **MIT** · 1 075 B · `a152c15af5d9` | 0 | **EMEA** (Portugal) | Web app for digital- and AI-literacy teaching in Portuguese **school libraries**, 2.º/3.º ciclo and secondary. Created 2026-10-14 |
| AI Assignment Grader | [`KamoliddinS/AI-Assignment-Grader`](https://github.com/KamoliddinS/AI-Assignment-Grader) | **MIT** body (no title line) · 1 077 B · `988f496a7b26` | 2 | Global | Grades answers from spreadsheets, emails a PDF feedback report. 27 KB script-tier; **last push 2023-10-15** — read as a reference, not a dependency |
| Agente Educativo Psicocognitivo | [`papayaykware/agente-educativo-psicocognitivo`](https://github.com/papayaykware/agente-educativo-psicocognitivo) | **MIT** · 1 069 B · `e34780266778` | 0 | **LATAM** / ES | DKT knowledge tracing + emergent psycho-cognitive profile + affective computing. 🟡 Its own README calls itself a **roadmap in four phases** with base code — architecture, not a running tutor |

🔵 Nine rows, nine grants, nine first-hand reads. Five of the nine are new to this shelf.

### 🟢 `Gap 464-A` CLOSED — and the closure is weaker than the gap implied

🔵 `p464` recorded that the clearest LATAM opportunity on `intel/market.md` — **rubric-based
assignment feedback** — had no granted supply behind it. That is no longer true. Four MIT grants
now sit on this shelf for exactly that job: `vijju9019/GradeAI`, `laurauguc/grading_assistant`,
`littlecookie0722/AI-Teaching-Agent` and `KamoliddinS/AI-Assignment-Grader`.

🔴 **State the other half or the closure misleads.** Their star counts are **0, 4, 0 and 2**. Every
one is a single-maintainer repository; one was last pushed in **2023**; one was **created two days
before this pass**. None is a dependency you take and maintain downstream of. All four are
**starting points you fork and own**, and the rubric logic — not the LLM call — is the part worth
reading. The gap this closes is *"nothing granted exists"*. It does not close *"something
production-grade exists"*, and no row on this shelf does.

### 🟡 `lbedu.me`'s grant is CONJUNCTIVE, and this shelf carried the bytes without the carve-out

🔵 [`lbhubedu/lbedu.me`](https://github.com/lbhubedu/lbedu.me) is shelved here at MIT · 2 118 B ·
`18272c548223`. My read reproduces those bytes and that digest exactly. What the shelf does not
record is **why the payload is 2 118 B when stock MIT is ~1 070 B**: below the MIT text, a
`Trademark & Content Notice` **expressly excludes** three things from the grant and reserves them
*All Rights Reserved* — the **"LBEdu" name, logos and brand symbols**; the **institutional texts,
history, editorial copy and manifesto**; and the **images and photographs**, naming
`public/images/` by directory. The code (React components, TypeScript, CSS, build config) is MIT
and reuse as a technical base is explicitly encouraged, provided brand and institutional content
are replaced. 🟢 Registered as **`Gap 469-A`**: a licence payload materially longer than its stock
text must be read to the end before a grant class is published — the carve-out lives past the
warranty clause.

### 🔴 Refused this pass — stated, because a silent refusal reads like a miss

| candidate | probe | why refused |
|---|---|---|
| [`David78-beto/TutorMind`](https://github.com/David78-beto/TutorMind) | `main` `8230a75831cf` live; **no licence at 6 paths** | ungranted — unusable in any client engagement |
| [`valarie-yang/assignment-ai-grading-system`](https://github.com/valarie-yang/assignment-ai-grading-system) | `main` `3cc82d1a89b3` live; **no licence at 6 paths** | ungranted — and it is the most on-brief rubric design of the set, which is the loss |
| [`GradeAI/gradeai`](https://github.com/GradeAI/gradeai) | `main` `4de8e8614582` live; **no licence at 6 paths** | ungranted |
| [`Micel357/Edu-mentor-AI`](https://github.com/Micel357/Edu-mentor-AI) | `main` `31046d9e0179` live; **no licence at 6 paths** | ungranted — pedagogical multi-agent system, LATAM-adjacent, and unusable |
| [`makecindy/cindy`](https://github.com/makecindy/cindy) | Apache-2.0 · 11 358 B · `cfc7749b96f6` · **6 532★** | 🔴 **not education supply.** A secondary trending roundup lists it under an education trend ("learn inference internals"); its own README and topics make it a general-purpose desktop agent. Granted, live, trending — and off-class. `p453`'s homonym finding, recurring |
| [`promptster-ai/rubric`](https://github.com/promptster-ai/rubric) | MIT, 2026 | out of class — it grades **engineers' AI fluency**, not student work |

### 🟢 Instrument false alarm, caught before publication

🔴 My first novelty sweep reported `chamilo/chamilo` and `openeducat/openeducat` as **shelf
addresses that do not resolve** — `git ls-remote` fails on both, and both appeared in 155 and 197
shelf files respectively. 🟢 **Refuted before publication.** Both were **substring hits** inside the
canonical addresses: `grep -ro "github.com/chamilo/chamilo)"` and the same for `openeducat` return
**0** across all eight shelves. Neither bare form is published as a link target anywhere. The
canonical addresses resolve live and are graded correctly on `verticals/solutions.md`:
`chamilo/chamilo-lms` (`master` `cd27c720ee18`) and `openeducat/openeducat_erp` (`19.0`
`46a5d7d40082`). 🟢 Registered as **`Gap 469-B`**: a novelty or liveness sweep over these shelves
must anchor the address, because every canonical name here contains a shorter one.

## 🆕 `p468` — **🟢 `Gap 467-D` IS CLOSED, AND IT WAS NEVER A NETWORK PROBLEM: `api.github.com` is 403 from this host and `repos.ecosyste.ms` is unreachable — both re-confirmed today — but this session's own GitHub tool channel serves `stargazers_count`, so the star axis is two-channel for the first time in 468 passes. 🔴 And the saturation this base has published for six passes is REFUTED AS STATED: the discovery channel is not exhausted, its VOCABULARY is. One Spanish-language leg returned 9 addresses in 12 that these shelves have never carried, against 9 in 64 across three English legs — a 5.7× difference from the query language alone. 🔵 The catch, stated with the claim: the non-English legs' usable build-on yield is still ZERO.**

🔴 **Gate posture, stated first per `Gap 446-A`: `make hooks` was DENIED** (`Code from External`)
before any gate body ran — **fifteen denials in sixteen passes**. 🔵 **Nothing below is
gate-attested.** The checks were re-implemented in this session's own code and are green:
frontmatter keys and closed-vocabulary `region` on all eight shelves; every new table checked for
separator presence and pipe-count consistency, with **no header row published as data**;
append-only proved on both trending shelves by prior-body containment; every address below
re-resolved first-hand this pass.

### 🟢 Seven cross-pass controls, reproduced HEAD-, byte- AND digest-identical to `p467`

| control | grant · bytes · `sha256₁₂` | HEAD | vs `p467` |
|---|---|---|---|
| [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) | Apache-2.0 · 11 408 B · `cd2f54e1e506` | `a31d82624c27` | 🟢 identical on all four axes |
| [`GarethManning/education-agent-skills`](https://github.com/GarethManning/education-agent-skills) | `CC-BY-SA` · 1 230 B · `f952182df4eb` | `135d6275e7db` | 🟢 identical |
| [`canyongbs/advisingapp`](https://github.com/canyongbs/advisingapp) | `Elastic-2.0` · 3 860 B · `48255018b41f` | `c79803f21cb8` | 🟢 identical |
| [`xiaoyang111222/cn-math-taxonomy`](https://github.com/xiaoyang111222/cn-math-taxonomy) | `CC-BY-NC` · 19 347 B · `41003d4a7474` | `cf262d886821` | 🟢 identical |
| [`CaviraOSS/PageLM`](https://github.com/CaviraOSS/PageLM) | 🔴 bespoke `PageLM Community License` · 8 563 B · `c834209c5f33` | `a6646794661b` | 🟢 identical — `Gap 467-A`'s counter-example is stable |
| [`falkenslab/miyagi`](https://github.com/falkenslab/miyagi) | **MIT** · 1 078 B · `d0a329112827` | `d8849a82e9ea` | 🟢 identical |
| [`av-leschinskiy/moodle-mcp`](https://github.com/av-leschinskiy/moodle-mcp) | **MIT** · 1 078 B · `67b516c28e67` | `69c36847e7ad` | 🟢 identical |

🔵 Two controls were added this pass (`miyagi`, `moodle-mcp`) because both are Moodle teacher-side
rows and both sit on the LATAM/EMEA boundary this file is repeatedly asked about.

### 🔴 This pass's own instrument was wrong twice, and both were caught before publication

🔴 **`p465`'s −1-byte defect is REPRODUCED INDEPENDENTLY, and the cause is now named exactly.** My
v1 probe read `falkenslab/miyagi` at **1 077 B · `5698cc474826`** against the shelf's 1 078 B ·
`d0a329112827` — the same −1 byte at an unchanged HEAD that `p465` diagnosed. The cause is not a
bug in one script: it is the **`$(curl …)` idiom**. Command substitution strips *all* trailing
newlines, so every payload measured through a shell variable is short by its trailing-newline
count. v2 writes the payload to a file and measures the file; it reproduces all seven controls
exactly. 🟢 Registered as **`Gap 468-A`**: no payload on these shelves may be measured through a
shell variable, ever.

🔴 **The star-agreement instrument's v1 was also wrong, in the opposite direction.** It searched
whole shelf files for a star figure beside each address and scored 14 of 21 as disagreements —
but a shelf carrying 467 passes of history holds `1 704★` and `3 948★` for the same repository
that reads `4 029★` today. Those are a **time series, not a disagreement**; v1 was a containment
test wearing an agreement test's label. 🟢 Registered as **`Gap 468-B`**. v2, restricted to each
file's current pass section, is reported below.

### 🟢 `Gap 467-D` closed — the star axis, measured on a second channel

🔵 `Gap 467-D` stated that every star count on these shelves is single-channel and
index-relayed. Both of its named dead ends were re-probed today and both are still dead:

| channel | probe | result today |
|---|---|---|
| `api.github.com` direct | `curl -s -o /dev/null -w '%{http_code}'` on `/repos/HKUDS/DeepTutor` | 🔴 **403** — unchanged |
| `repos.ecosyste.ms` | same probe on `/api/v1/hosts/GitHub/repositories/HKUDS%2FDeepTutor` | 🔴 **`000`** (connection never established) — unchanged |
| 🟢 **session GitHub tool channel** | repository search, reading `stargazers_count` | 🟢 **reachable** — returns live counts for every address in the result set |

🟢 So the gap closes, and the lesson is about where the base looked rather than about the network:
the second channel was available for the whole of `p467` and was not tried, because the gap was
written as a *curl* problem. Agreement at the overlap, **n = 3** and stated as such:

| address | `p467` section figure | second channel, 2026-10-27 | verdict |
|---|---|---|---|
| [`CaviraOSS/PageLM`](https://github.com/CaviraOSS/PageLM) | 2 049★ | 2 049 | 🟢 exact |
| [`canyongbs/advisingapp`](https://github.com/canyongbs/advisingapp) | 340★ | 340 | 🟢 exact |
| [`xiaoyang111222/cn-math-taxonomy`](https://github.com/xiaoyang111222/cn-math-taxonomy) | 4 027★ | 4 029 | 🟡 **+2 in one day** — a live counter, not an error |

🔵 n = 3 is too small to retire the index-relayed caveat. It is enough to say the axis is no
longer single-channel, and enough to say the drift at one day is **+2 of 4 027 (0.05 %)**.

### 🔴 The saturation finding, restated correctly: the vocabulary is exhausted, not the channel

🔵 Five discovery legs, **79 distinct addresses**, every one graded against these shelves:

| leg | query language | graded | already carried | novel by address | novel rate |
|---|---|---|---|---|---|
| recency × stars (`created:>2026-08-01`) | English | 29 | 24 | 5 | 17.2 % |
| `topic:edtech` × `pushed:>2026-09-01` | English | 30 | 28 | 2 | 6.7 % |
| SIS / LMS connector vocabulary | English | 7 | 5 | 2 | 28.6 % |
| 🟢 `educacion IA docentes` | **Spanish** | 12 | 3 | **9** | **75.0 %** |
| 🟢 `educacao inteligencia artificial escola` | **Portuguese** | 3 | 0 | **3** | **100 %** |

🟢 **English legs: 9 novel in 64 (14.1 %). Non-English legs: 12 novel in 15 (80.0 %).** A **5.7×**
difference produced by nothing but the language the query was written in. Six passes of
*"usable novel yield ZERO"* were measuring an English-language index, and said so nowhere.

🔴 **And the correction does not rescue the supply.** Of the 12 non-English novel addresses, nine
are coursework artifacts — a doctoral thesis site, three near-identical teacher-training project
pages from one account, a survey's supplementary material, an essay. Two are software; one of
those serves no grant. **Usable build-on yield of the non-English legs: zero.** The honest
statement is therefore narrower than the headline rate and is the one that should be carried:
*novelty by address is a vocabulary artifact; usable supply is genuinely scarce.*

### 🟢 Novel rows added this pass, each grant read first-hand at `HEAD`

| agent | repo | grant · bytes · `sha256₁₂` @ HEAD | ★ | `grant_class` | what it does |
|---|---|---|---|---|---|
| nietzschian-debugger | [`DilawarShafiq/nietzschian-debugger`](https://github.com/DilawarShafiq/nietzschian-debugger) | **MIT** · 1 071 B · `a7055a6d5672` @ `94e452d3fc83` | 153 | 🟢 `PERMISSIVE` | A deliberately confrontational debugging tutor: refuses to hand over the fix and interrogates the student toward it. 🟢 The only row on this shelf built around **withholding** the answer, which is the pedagogy an integrity-anxious faculty buyer asks for by name |
| awesome-student-resources | [`StudentSuite/awesome-student-resources`](https://github.com/StudentSuite/awesome-student-resources) | **MIT** · 1 069 B · `537c697c69a5` @ `602df143c5a9` | 32 | 🟢 `PERMISSIVE` | Curated IB / IGCSE / SAT study-tool index. Useful as a **catalogue input**, not as a codebase |
| awesome-study-resources | [`StudentSuite/awesome-study-resources`](https://github.com/StudentSuite/awesome-study-resources) | **MIT** · 1 069 B · `537c697c69a5` @ `74d5a7bbf17b` | 30 | 🟢 `PERMISSIVE` | Exam-prep index tagged free / freemium / paid / open-source. 🟡 See the lineage note below — this is **not** an independent second grant |
| OpenTeacherAgent | [`ai-swarm-solutions-group/OpenTeacherAgent`](https://gitlab.com/ai-swarm-solutions-group/OpenTeacherAgent) | **AGPL-3.0-or-later** · 34 523 B · `0d96a4ff68ad` @ `59a33fecff73` | n/a (GitLab) | 🟡 `NETWORK_COPYLEFT` | Teacher states an intent in natural language → agent generates interactive exercises, composes course pages, exports the whole project as one self-contained offline HTML bundle with score tracking. Rust + Vue, single binary |

🟡 **The two `StudentSuite` rows serve a byte-identical grant payload** — 1 069 B, `537c697c69a5`,
same organisation, different repositories. This is the lineage shape `p446` found in the
LMS-MCP tier, and it is why this shelf counts **grants**, not LICENSE files: these are two
repositories and **one** grant.

🟢 **`OpenTeacherAgent` settles the GitLab argument this base has had with itself twice.** `p466`
claimed GitLab yields novel education supply at ~2.5× the GitHub rate; `p467` refuted that as a
token collision (`tutor` matching inside `tutorial`) and published *"usable education-AI supply:
ZERO"*. 🔴 **`p467`'s zero is refuted by exactly one row** — and one row is the right size for
the claim. GitLab's education yield is non-zero, very small, and, as `p466` observed and this row
confirms, **AGPL**.

### 🔴 Refused this pass, with the reason read from the payload

| address | grant · bytes · `sha256₁₂` @ HEAD | ★ | why refused |
|---|---|---|---|
| [`walkinglabs/modern-llm-notebook`](https://github.com/walkinglabs/modern-llm-notebook) | 🔴 `CC-BY-NC-SA-4.0` · 425 B · `d65ff2212f3e` @ `03715769cb94` | **272** | 🔴 `UNSELLABLE`. The most-starred novel address of the pass, and a NonCommercial grant bars it from any paid engagement. A hands-on LLM-architecture course — exactly the shape a corporate-upskilling engagement would reach for |
| [`rudra496/StealthHumanizer`](https://github.com/rudra496/StealthHumanizer) | **MIT** · 1 074 B · `8967efcf60c6` @ `c727cd6774f7` | 189 | 🔴 **Permissively granted and still refused.** Its stated purpose is defeating Turnitin and GPTZero. Recorded as an **academic-integrity counter-signal** on [`intel/trends.md`](../intel/trends.md), never as build-on supply for an education client |
| [`mdakram2001/AMU-Utilities`](https://github.com/mdakram2001/AMU-Utilities) | 🔴 **NO GRANT** at 10 root paths @ `cb8b178ef9f8` | 0 | SIS MCP server for Aligarh Muslim University. 🔴 **APAC's only novel address this pass, and it is ungranted** |
| [`s-caserta99/DocuQuery_MCP`](https://github.com/s-caserta99/DocuQuery_MCP) | 🔴 **NO GRANT** at 10 root paths @ `85523c2f8252` | 0 | Literature-Q&A MCP server for researchers |
| [`leonine1983/aprendix`](https://github.com/leonine1983/aprendix) | 🔴 **NO GRANT** at 10 root paths @ `7df5ee4c76d6` | 0 | Brazilian school-management system with AI dropout-risk support — the right product shape for LATAM and **nothing to build on** |
| [`fabianastudillo/cafe-con-prompts`](https://github.com/fabianastudillo/cafe-con-prompts) | 🟡 `Creative Commons Atribución` · 751 B · `c7a4fd88d164` @ `7ac77c6574a0` | 0 | 🟡 `CONTENT_NOT_SOFTWARE`. Ecuadorian Spanish-language teacher prompt library. Usable **as content with attribution**; it is not a codebase. 🔵 Its grant is published in Spanish — the first on these shelves |
| [`aj-group4860936/EduAgent`](https://gitlab.com/aj-group4860936/EduAgent) | 🔴 **NO GRANT** at 4 root paths @ `93d406dbaf8a` | n/a | GitLab; agent-based educational content generation and review |

### 🔴 Novel supply by region, with the empty regions named

🔵 Per the ingest brief, a region that returned nothing is written down rather than omitted.

| region | novel build-on rows this pass | what was actually found |
|---|---|---|
| North America | **0** | 🔴 Declared gap. The two permissive novel rows (`nietzschian-debugger`, the `StudentSuite` pair) declare no country, so they are placed Global, not NA |
| EMEA | **0** | 🔴 Declared gap. Every EMEA-placed address the legs returned — `ink-waffle/sisu-mcp` (Finland), `Haris0059/ibu-mcp` (Bosnia), `particify/arsnova-server` (Germany), `Selleo/mentingo` (Poland) — is **already carried**. `OpenTeacherAgent`'s GitLab group states no country |
| APAC | **0** | 🔴 One novel address, `mdakram2001/AMU-Utilities` (India), and it serves **no grant at 10 paths** |
| LATAM | **0** | 🔴 Two novel addresses — `fabianastudillo/cafe-con-prompts` (Ecuador, content licence) and `leonine1983/aprendix` (Brazil, no grant). **Neither is build-on supply.** The Spanish and Portuguese legs that surfaced them are the two most productive legs of the pass by address count and the least productive by usable yield |

### 🔴 Gaps this pass registers

| gap | statement | how the next pass closes it |
|---|---|---|
| 🔴 **`Gap 468-A`** | **No payload may be measured through a shell variable.** `$(curl …)` strips trailing newlines; this pass's v1 probe reproduced `p465`'s −1-byte defect from that idiom alone, on a population, not on one row. | Make the file-backed `probe2.sh` the only payload reader on this base; add a control whose payload **ends in a newline** and assert its byte count, so the defect cannot return silently |
| 🔴 **`Gap 468-B`** | **An agreement test against a shelf that carries 467 passes of history is a containment test.** v1 scored 14 of 21 star figures as disagreements; 13 of those were simply older readings of the same repository. | Scope every cross-pass comparison to the **current pass section** of each file, and publish the section boundary used |
| 🟢 **`Gap 468-C`** | **Discovery vocabulary is English-only and that is now measured: 14.1 % novel by address against 80.0 % for Spanish and Portuguese.** The brief's own region legs are written in English. | Run one non-English leg **per pass, per region** — Spanish, Portuguese, Arabic, Bahasa, Hindi — and publish the novel-by-address rate per language beside the usable-supply rate, so the two are never conflated again |
| 🟡 **`Gap 468-D`** | **The star axis is two-channel at n = 3.** Too small to retire the index-relayed caveat `Gap 467-D` imposed. | Grade the second channel against the current pass sections at n ≥ 30 before any star figure on these shelves is described as first-hand |

---

## 🆕 `p467` — **🟢 `Gap 466-A` AND `Gap 466-C` ARE CLOSED BY ONE INSTRUMENT, 41/41 controls, applied to 103 addresses — and the closure's OWN FIRST RUN published SIX WRONG VERDICTS, every one caught by reading the payload behind the verdict. 🔴 The headline is the worst of them, and it inverts `Gap 466-A` one further turn: a PERMISSIVE GRANT FORM IS NOT A PERMISSIVE GRANT. A 2 049★ platform opens with MIT's grant sentence verbatim and then restricts it to non-commercial use with a revenue-share clause. 🟢 And a licence class this base has never carried is read first-hand: CERN-OHL-S.**

🔴 **Gate posture, stated first per `Gap 446-A`: `make hooks` was DENIED** (`Code from External`)
before any gate body ran — **fourteen denials in fifteen passes**. 🔵 **Nothing below is
gate-attested.** The checks were re-implemented in this session's own code and all are green:
frontmatter keys and closed-vocabulary `region` on all nine shelves; every new table checked for
separator presence and pipe-count consistency, with **no header row published as data**;
append-only proved on both trending shelves by prior-body containment; every address below
re-resolved first-hand this pass.

### 🟢 Four cross-pass controls, reproduced HEAD-, byte- AND digest-identical to `p466`

| control | grant · bytes · `sha256₁₂` | HEAD | vs `p466` |
|---|---|---|---|
| [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) | Apache-2.0 · 11 408 B · `cd2f54e1e506` | `a31d82624c27` | 🟢 identical on all four axes |
| [`GarethManning/education-agent-skills`](https://github.com/GarethManning/education-agent-skills) | `CC-BY-SA` · 1 230 B · `f952182df4eb` | `135d6275e7db` | 🟢 identical |
| [`canyongbs/advisingapp`](https://github.com/canyongbs/advisingapp) | `Elastic-2.0` · 3 860 B · `48255018b41f` | `c79803f21cb8` | 🟢 identical |
| [`xiaoyang111222/cn-math-taxonomy`](https://github.com/xiaoyang111222/cn-math-taxonomy) | `CC-BY-NC` · 19 347 B · `41003d4a7474` | `cf262d886821` | 🟢 identical |

🔵 `p465` found its own instrument off by −1 byte at unchanged HEADs and diagnosed it. This pass
reproduces all three of `p466`'s licence re-grades plus the standing headline control exactly, so
the −1 defect is **confirmed fixed at population scale**, not just on the one row.

### 🔴 THE PASS'S HEADLINE: a permissive grant FORM is not a permissive grant

🔵 `Gap 466-A` said *a present grant is not a permissive one*. This row says something strictly
worse, because it defeats the remedy as well as the screen:

[`CaviraOSS/PageLM`](https://github.com/CaviraOSS/PageLM) — **2 049★**, a self-hosted NotebookLM
alternative, the most-starred education *platform* in this window — serves **"PageLM Community
License"** (8 563 B · `c834209c5f33` @ HEAD `a6646794661b`). Its first grant sentence is MIT's,
word for word:

> *"Permission is hereby granted, free of charge, to any person obtaining a copy of this software
> and associated documentation files (the "Software"), to use, copy, modify, and run the Software
> for **personal, educational, or non-commercial research purposes**…"*

🔴 Then: **redistribution "strictly prohibited"** (§2); **no commercial use** without a separate
agreement (§3); a **revenue-sharing agreement required before any commercial deployment**, breach
terminating the licence and exposing *"disgorgement of profits"* (§4); and a **partial-use clause**
making *"any portion, code snippet, algorithm, design pattern"* in a commercial product a
Commercial Use (§7).

🔴 **This pass's own v1 reader graded it `MIT / PERMISSIVE`.** So does this base's standing
reader: [`family_title.py`](../compose/code/p456-ref-resolution/family_title.py)'s
`PERMISSIVE_GRANT` arm **suppresses its bespoke-licence check** whenever the body recites a
permissive grant form — which is exactly what this payload does — and then returns
`MIT (body form, no title)`. 🟢 **The base is not wrong about this row and never was:** `pass255`
caught it *"only because PageLM recites the MIT grant verbatim"*, `pass257` recorded it, and the
8 563 B / `c834209c5f33` digest read first-hand today is **identical to that record**. A later pass
regressed the cell to `MIT`; the shelves' own history held the correct reading. 🔵 Registered as
**`Gap 467-A`**, and the remedy is in the instrument below as a **restriction override** that
outranks the body layer.

### 🟢 The instrument: a `grant_class` axis, which is what both gaps asked for

[`compose/code/p467-grant-class/`](../compose/code/p467-grant-class/) —
[`grant_class.py`](../compose/code/p467-grant-class/grant_class.py) ·
[`controls.py`](../compose/code/p467-grant-class/controls.py) **41/41 pass** ·
[`probe.sh`](../compose/code/p467-grant-class/probe.sh) ·
[`sweep.py`](../compose/code/p467-grant-class/sweep.py).

| class | what it means for a Globant engagement | n in this pass's population |
|---|---|---|
| 🟢 `PERMISSIVE` | build on, ship, relicense into a deliverable | **63** |
| 🟢 `PUBLIC_DOMAIN` | as above, no attribution obligation | 0 |
| 🟡 `WEAK_COPYLEFT` | link, do not vendor modified sources | 1 |
| 🟡 `STRONG_COPYLEFT` | derivative works carry the grant | 7 |
| 🟡 `NETWORK_COPYLEFT` | fits a self-hosted institutional buyer, wrong for multi-tenant SaaS | 10 |
| 🟡 `CONTENT_NOT_SOFTWARE` | usable as *content* with attribution; ShareAlike propagates | 3 |
| 🔴 `UNSELLABLE` | **barred from a paid engagement** — `*-NC`, `Elastic-*`, `BUSL-*`, `SSPL`, bespoke restrictive | **5** |
| 🔴 `NO_GRANT` | no payload at any of 10 root paths | 11 |
| 🟡 `COMPOSITE_PER_ASSET` | the repository is **not** the unit of grant — clear per asset | 2 |
| 🟡 `POINTER_CROSS_REPO` | the grant lives in **another repository**; follow it | 1 |
| 🟡 `RESERVED_UNDECIDED` | payload says the licence is undecided — **ask the author** | 0 here, 1 on GitLab |

🟢 **`Gap 466-C` is closed in the strong form: NO verdict in this instrument reads payload size.**
`bytes` and `sha256₁₂` are carried as provenance only, so a later pass can prove it read the same
payload. 🔵 The gap's own evidence — AGPL-3.0 at **7** live byte values spanning 1 116 B — is what
makes size unusable, and nothing here depends on it.

🟡 **`Gap 466-A`'s prescription is UNDER-SPECIFIED, and the number is published rather than
smoothed over.** It asks for the class to be read from *"the payload's first non-blank line"*.
**87 of 103** families can be: the other **16** cannot, because Apache-2.0 puts "Version 2.0" on
its *second* non-blank line and the commonest MIT shape in the wild opens on a bare copyright line
with no title at all. Every such row is published `line1=0` and never silently promoted. Registered
as **`Gap 467-B`**.

### 🔴 The six wrong verdicts this pass's own instrument published, and what each one cost

🔵 Each was found by reading the payload behind the verdict — never by the verdict, and never by a
count. Full ledger:
[`evidence/grant-class-corrections.2026-10-26-p467.tsv`](../evidence/grant-class-corrections.2026-10-26-p467.tsv).

| address | ★ | v1 said | 🟢 v2 says, read first-hand | the defect |
|---|---|---|---|---|
| [`CaviraOSS/PageLM`](https://github.com/CaviraOSS/PageLM) | 2 049 | 🔴 `MIT / PERMISSIVE` | 🔴 **`NOT-OSI (PageLM Community License)` / `UNSELLABLE`** · 8 563 B `c834209c5f33` | the MIT grant **sentence** inside a bespoke restrictive licence. Remedy: a restriction override running **after** the body layer and outranking it |
| [`codeforlife-education/aimmo`](https://github.com/codeforlife-education/aimmo) | 117 | 🔴 `NOT-OSI / UNSELLABLE` | 🟡 **`POINTER_CROSS_REPO`** → `ocadotechnology/codeforlife-workspace@main/LICENSE.md`, followed first-hand: **AGPL-3.0** · 32 920 B · `420e5ccb5e59` | a 115 B pointer condemned as a refusal. `p454`'s reader has a pointer rule but resolves **in-repo paths only**; this target is another repository |
| [`Wakoma/nimble`](https://github.com/Wakoma/nimble) | 110 | 🔴 `NOT-OSI / UNSELLABLE` | 🟢 **`CERN-OHL-S` / `STRONG_COPYLEFT`** · 13 419 B · `d6475a84171f` @ HEAD `315910f164c0`, `br=master` | a **free reciprocal** licence read as a refusal. Commercial use is permitted under reciprocity |
| [`scollovati/awesome-lti`](https://github.com/scollovati/awesome-lti) | 79 | 🔴 `UNSTATED` | 🟡 **`CC-BY-SA` / `CONTENT_NOT_SOFTWARE`** · 20 131 B · `7abe19ec9bb7` | the payload's first line is **"Attribution-ShareAlike 4.0 International"** — the words *Creative Commons* appear **nowhere on it**. Two live title forms per CC family; v1 knew one |
| [`learning-commons-org/knowledge-graph`](https://github.com/learning-commons-org/knowledge-graph) | 164 | 🔴 `UNSTATED` | 🟡 **`COMPOSITE_PER_ASSET`** · 5 789 B · `d849ffef4f98` | the grant is a property of **each dataset**, not of the repository — see below |
| [`learning-commons-org/evaluators`](https://github.com/learning-commons-org/evaluators) | 87 | 🔴 `UNSTATED` | 🔴 **`COMPOSITE_PER_ASSET (MIT code + NonCommercial content)`** · 1 615 B · `86c7be78af8b` | **MIT code, CC BY 4.0 content, and a CC BY-NC-SA 4.0 corpus inside one payload.** A reader taking the first content clause reads `CC BY 4.0` and misses the NC half two sentences later |

🟡 One further correction, same class, lesser cost:
[`Jeremy-xuan/SocraticNovel`](https://github.com/Jeremy-xuan/SocraticNovel) is **`CC-BY-NC-SA`**,
not `CC-BY-NC` — same `UNSELLABLE` verdict, and the ShareAlike clause is a second obligation on top
of the commercial bar.

### 🟢 The per-asset grant surface — a class these shelves have never had a verdict for

🔵 [`learning-commons-org/knowledge-graph`](https://github.com/learning-commons-org/knowledge-graph)
(164★) is the shape `intel/market.md`'s curriculum-alignment opportunity most wants: standards-aligned
instructional content as a data layer for educational AI. Its payload, read first-hand:

> *"Knowledge Graph code is licensed under **MIT**. … Knowledge Graph datasets are **not all
> licensed the same way**. Each dataset … is labeled with an access type … **Open + Gated** and
> **Gated** content **are not covered by CC BY 4.0, CC0, or any other open license** referenced
> here."*

🟢 **Operationally this is good news and the first sellable answer to `p466`'s `CC-BY-NC` data
finding** — the *code* is MIT and build-on. 🔴 But the **data must be cleared per dataset**, and
two of its three access tiers are affirmatively not open. A row like this cannot carry a single
`licence` cell at all, which is why it gets its own class rather than a family name.

### 🟢 Sell-shelf rows added this pass — with `grant_class`, forge and region, per `Gap 466-A`/`466-E`

🔵 **Four rows. Not a minimum, a count.** 103 addresses were coverage-checked across four GitHub
index channels; **99 were already carried** by this base and **4 were novel by address**. All four
are published, including the two that are not education supply, because a silent omission looks
like absence.

| repository | ★ | `grant_class` · grant · `sha256₁₂` | forge | region signal · basis | what it actually is |
|---|---|---|---|---|---|
| [`Wakoma/nimble`](https://github.com/Wakoma/nimble) | 110 | 🟡 `STRONG_COPYLEFT` · **CERN-OHL-S** · `d6475a84171f` · 13 419 B | GitHub | `UNPLACED` · 🔴 English README, no orthographic signal | 🟢 **A licence class this base has never carried.** A rapidly-deployable offline wireless mesh network — *hardware* — for community and school connectivity. Pairs with `learningequality/kolibri` (MIT, 1 161★) as the **physical** layer of an offline-first estate. 🔴 CERN-OHL-S is **strongly reciprocal**: hardware derivatives must ship their design sources. @ HEAD `315910f164c0` |
| [`wombats-writing-code/xoces`](https://github.com/wombats-writing-code/xoces) | 74 | 🟢 `PERMISSIVE` · MIT · `1115d8b49039` · 1 082 B | GitHub | `UNPLACED` | JS widgets for chord and tree visualisation of hierarchical, connected data — i.e. a renderer for the prerequisite graphs this base's curriculum rows emit. 🔴 **Last touched 2025-11-28**; shelved as a component, not a dependency |
| [`ably-labs/realtime-quiz-framework`](https://github.com/ably-labs/realtime-quiz-framework) | 77 | 🟢 `PERMISSIVE` · Apache-2.0 · `c71d239df917` · 11 357 B | GitHub | `UNPLACED` | A realtime quiz backbone (Vue + Node). 🔴 **ARCHIVED** and vendor-coupled to Ably's pub/sub. Reference only |
| [`mytechnotalent/HNN`](https://github.com/mytechnotalent/HNN) | 31 | 🟢 `PERMISSIVE` · Apache-2.0 · `c71d239df917` · 11 357 B | GitHub | `UNPLACED` | A hand-worked neural-network walkthrough notebook. AI-literacy *content*, not platform supply |

🔵 **Two of those four serve the identical Apache-2.0 payload** (`c71d239df917`, 11 357 B) — which
is 51 B away from `DeepTutor`'s 11 408 B `cd2f54e1e506`. 🟢 That is `Gap 466-C`'s point made once
more, from the other direction: **two byte-values 51 B apart are the same licence, and nothing here
branches on the difference.**

### 🔴 The discovery nil, on a channel stronger than the one the ingest brief prescribes

🔵 The brief prescribes web search. `p462` measured that channel's novel-repository yield at
**zero** over 36 tokens. This pass ran a **different and strictly stronger** channel: GitHub's own
search index through the session's MCP tools, which returns `stargazers_count`, `license.spdx_id`,
`pushed_at` and `default_branch` per hit — so candidates can be ordered and filtered before a
single probe is spent.

| channel | tokens / filters | hits | already carried | novel by address | 🔴 usable education-AI build-on supply |
|---|---|---|---|---|---|
| GitHub index, `topic:ai-tutor stars:>50` | 1 | 25 | 25 | 0 | 0 |
| GitHub index, `education AI agent stars:>100` | 1 | 13 | 13 | 0 | 0 |
| GitHub index, `topic:edtech stars:>30` | 1 | 50 | 48 | 2 | 0 |
| GitHub index, `topic:ai-education stars:>20` | 1 | 29 | 29 | 0 | 0 |
| **union, de-duplicated** | 4 | **103** | **99 (96 %)** | **4** | 🔴 **0** |

🔴 **Seventh independent reproduction of the saturation nil**, and the first with this denominator:
96 % of a star-ordered, four-channel sweep of GitHub's own index was already on these shelves, and
the 4 novel addresses are one hardware project, one archived vendor demo, one 2025-dormant widget
library and one tutorial notebook. 🟢 **The conclusion is not "search harder" — it is that
discovery on this base's carried vocabulary is finished, and only a change of AXIS (forge,
recency, language, or an adjacent subdomain) can yield supply.** Both axis legs run this pass are
on [`repos/trending.md`](../repos/trending.md).

### 🟢 `Gap 466-B` is CLOSED WITH A NUMBER — and the number REFUTES the gap's own premise

🔵 `Gap 466-B` asserted that *"the ungranted denominator correlates with star count in the wrong
direction"* and that *"a pass that prioritises candidates by stars will spend its probes on
ungranted supply"*. It prescribed recording `(★, grant-present)` for every probed address and
publishing the correlation at **n ≥ 60**. 🟢 Done at **n = 103**, every pair read first-hand:
[`evidence/grant-class.2026-10-26-p467.tsv`](../evidence/grant-class.2026-10-26-p467.tsv).

| star band | n | grant present | grant rate | 🟢 **sellable** | **sell rate** |
|---|---|---|---|---|---|
| ≥ 1 000 ★ | 13 | 13 | **1.00** | 8 | 0.62 |
| 300–999 ★ | 19 | 16 | 0.84 | 10 | 0.53 |
| 100–299 ★ | 38 | 36 | 0.95 | 26 | 0.68 |
| < 100 ★ | 33 | 27 | 0.82 | 19 | 0.58 |
| **all** | **103** | **92** | **0.89** | **63** | **0.61** |

🔴 **The gap is refuted on its own axis.** Grant presence *rises* with stars — **1.00** in the top
band against **0.82** in the bottom — so star ordering does **not** waste probes on ungranted
supply. `p466` generalised from one row (`ai-ethos`, 498★, ungranted); at n = 103 that row is an
exception, not a trend.

🟢 **And the finding that replaces it is sharper, because it is the one that costs money.**
**Sellability is FLAT across every band: 0.62 / 0.53 / 0.68 / 0.58.** Stars predict that a licence
*exists*; they carry **no information whatever** about whether it *permits*. 🔵 That is precisely
`Gap 466-A`'s three rows restated as a population law — 914★, 340★ and 4 000★ all had a grant and
none could be sold — and it means **the grant-class read can never be skipped on a high-star row**,
which is the opposite of the candidate-ordering reform the gap prescribed. Registered as
**`Gap 467-C`**.

🔴 **One measurement the gap asked for CANNOT be made from this host, and it is declared.** The
star figures above come from GitHub's search index via this session's MCP tools. The two
independent star channels are both **blocked**: `api.github.com/repos/<addr>` returns **403**
(*"GitHub access to this repository is not enabled for this session"*) and `repos.ecosyste.ms`
is refused by the egress proxy (`connect_rejected`). 🔵 So every star count on these shelves is
**single-channel and unreproducible by a second instrument**, where every *grant* is two-channel
and first-hand. Registered as **`Gap 467-D`**.

### 🔴 The ungranted denominator, published in full

🔵 **11 of 103 (10.7 %)** serve no licence payload at any of ten root paths
(`LICENSE`, `LICENSE.md`, `LICENSE.txt`, `LICENCE`, `LICENCE.md`, `COPYING`, `COPYING.md`,
`LICENSE.rst`, `license`, `License.md`).

| address | ★ | note |
|---|---|---|
| [`aaryansamanta/ai-ethos`](https://github.com/aaryansamanta/ai-ethos) | 498 | 🔴 reproduces `p466` — a 501(c)(3) delivering multilingual tutoring to underserved and neurodiverse learners, mission-aligned and legally unusable |
| [`jude-miller-dev/Milky-institute-online`](https://github.com/jude-miller-dev/Milky-institute-online) | 364 | production-grade Spring Cloud adult-education platform with a course-recommendation agent · `zh` / APAC |
| [`minicoohei/ai-agent-camp`](https://github.com/minicoohei/ai-agent-camp) | 345 | non-engineer AI-agent curriculum · `zh` / APAC |
| [`hkalant/awesome-edtech-tools`](https://github.com/hkalant/awesome-edtech-tools) | 216 | curated instructional-design tool list |
| [`DAMO-NLP-SG/M3Exam`](https://github.com/DAMO-NLP-SG/M3Exam) | 105 | 🔴 multilingual/multimodal/multilevel exam **benchmark** — an evaluation asset with no grant |
| [`mahseema/aibooks`](https://github.com/mahseema/aibooks) | 95 | AI/ML book list |
| [`Imboyeong/Fact-vs-Fiction-LLM-Test-`](https://github.com/Imboyeong/Fact-vs-Fiction-LLM-Test-) | 93 | Korean LLM-accuracy study hub · `ko` / APAC |
| [`jaltekruse/Free-Math`](https://github.com/jaltekruse/Free-Math) | 74 | offline digital maths-homework grading |
| [`A-R007/Multi-Agent-Study-Assistant`](https://github.com/A-R007/Multi-Agent-Study-Assistant) | 64 | six-agent study platform |
| [`vincenzo-afk/KingstonConnect`](https://github.com/vincenzo-afk/KingstonConnect) | 41 | Indian college-management platform with portal integration |
| [`shychee/py_ai_tutorial`](https://github.com/shychee/py_ai_tutorial) | 22 | Python AI course, 17 industry projects · `zh` / APAC |

### 🔴 Gaps this pass registers

| gap | statement | how the next pass closes it |
|---|---|---|
| 🔴 **`Gap 467-A`** | **A permissive grant FORM is not a permissive grant, and both readers on this base return `MIT` for the counter-example.** `CaviraOSS/PageLM` (2 049★) recites MIT's grant sentence verbatim and restricts it in the same sentence to non-commercial use, prohibits redistribution, and requires a revenue-share agreement. `family_title.py`'s `PERMISSIVE_GRANT` arm suppresses its own bespoke check on exactly this shape. | Port the **restriction override** from [`grant_class.py`](../compose/code/p467-grant-class/grant_class.py) into `family_title.py`, then re-sweep every carried cell whose basis is `MIT (body form, no title)` — that basis is the exact signature of this defect |
| 🟡 **`Gap 467-B`** | **`Gap 466-A`'s one-line anchor cannot grade 16 of 103 payloads.** Apache-2.0 carries its version on the second non-blank line; the commonest MIT shape has no title at all. | Keep `line1` as a published column on every graded row, and treat `line1=0` as requiring the title-block + body layers — never as grounds to withhold a verdict |
| 🔴 **`Gap 467-C`** | **Stars predict that a licence EXISTS, not that it PERMITS.** At n = 103 the grant rate rises with stars (1.00 vs 0.82, refuting `Gap 466-B`) while the **sell rate is flat at 0.53–0.68 across all four bands**. | Never promote a high-star row without a first-hand `grant_class`; re-run the band table each pass and publish it when n ≥ 200 so the flatness is tested rather than assumed |
| 🔴 **`Gap 467-D`** | **Every star count on these shelves is single-channel.** `api.github.com` → 403 (session-scoped), `repos.ecosyste.ms` → `connect_rejected`. Grants are two-channel and first-hand; stars are not reproducible by any second instrument from this host. | Mark every star figure as index-relayed, never first-hand; if a second channel becomes reachable, re-measure the band table before relying on it |

---

## 🆕 `p466` — **🔴 THREE HIGH-VISIBILITY ROWS THIS BASE CARRIES ARE NOT BUILD-ON SUPPLY, and every one of them would pass a star-count and "has-a-LICENSE" screen: a 914★ teacher-skills library is `CC-BY-SA-4.0` (not a software licence), a 340★ higher-ed advising platform is `Elastic-2.0` (not OSI), and a 4 000★ maths knowledge graph is `CC-BY-NC-4.0` — NonCommercial, so it is unusable in any Globant client engagement. 🟢 And a FORGE this base has never sampled is reachable and NOT saturated: GitLab yields novel education supply at ~2.5× the GitHub rate — all of it AGPL-3.0.**

🔴 **Gate posture, stated first per `Gap 446-A`: `make hooks` was not run** — the harness refuses
execution of code that arrived in a clone (`Code from External`), now **thirteen denials in
fourteen passes**. 🔵 **Nothing below is gate-attested.** The checks were re-implemented in this
session's own code: frontmatter keys and closed-vocabulary `region` on all nine shelves; every new
table checked for separator presence, pipe-count consistency and **no header row published as
data**; append-only proved on both trending shelves by prior-body containment; every address below
re-resolved first-hand.

### 🟢 The instrument, with a NEGATIVE control this base has never published

🔵 Two first-hand channels, as `p450`/`p463`/`p464`/`p465` established: `git ls-remote --symref
<addr> HEAD` (**tree identity + default branch**) and `raw.../<addr>/<branch>/<LICENSE>` captured
with `curl -o <file>` (**payload bytes** → size + `sha256₁₂`), measured per `Gap 465-A`'s
**raw-bytes** contract, never through command substitution.

| probe | live address (`HKUDS/DeepTutor`) | nonexistent address | discriminates? |
|---|---|---|---|
| 🔴 `curl -sI https://github.com/<addr>` — **the probe the ingest brief prescribes** | `403` | `403` | 🔴 **NO — sixth independent reproduction of zero bits.** No row on this shelf rests on it |
| 🟢 `git ls-remote --symref` | `HEAD a31d82624c27`, `br=main` | **UNRESOLVED** | 🟢 **YES** — this is why the house instrument is `ls-remote`, and the first time the base has recorded the negative leg |

🟢 **Cross-pass control reproduced byte-, digest- and HEAD-identical to `p465`:** `HKUDS/DeepTutor`
`LICENSE` **Apache-2.0 · 11 408 B · `cd2f54e1e506`** @ HEAD **`a31d82624c27`**. 🔵 Its star count is
**43.8k** against the **43 537** `p465` recorded index-exact — still incrementing, so the base's
headline agent is fresh, not stale.

### 🔴 The three licence re-grades — read at the payload, against what a screen would have said

| repository | ★ | what a star + "has-a-LICENSE" screen says | 🔴 what the payload actually says, read first-hand | consequence for a Globant engagement |
|---|---|---|---|---|
| [`GarethManning/education-agent-skills`](https://github.com/GarethManning/education-agent-skills) | 914 | permissive supply — "165 evidence-based AI skills for teachers, school leaders and EdTech builders" | 🔴 **`CC-BY-SA-4.0`** · 1 230 B · `f952182df4eb` @ HEAD `135d6275e7db` — **not a software licence at all**, and **ShareAlike** | 🔴 Usable as *content* with attribution, but the ShareAlike condition propagates to adaptations. **Not** a library to vendor into a client deliverable without counsel. The single most-starred teacher-skills artefact in this window, and it is **not** MIT |
| [`canyongbs/advisingapp`](https://github.com/canyongbs/advisingapp) | 340 | an open-source higher-ed advising CRM + AI assistant — the closest thing in this window to a sellable vertical platform | 🔴 **`Elastic License 2.0`** · 3 860 B · `48255018b41f` @ HEAD `c79803f21cb8` — **source-available, NOT OSI-approved** | 🔴 Elastic-2.0 forbids providing the software to third parties **as a hosted or managed service**. That is precisely the Globant delivery model for a university CRM. **Refused as build-on supply**; retained as a design reference |
| [`xiaoyang111222/cn-math-taxonomy`](https://github.com/xiaoyang111222/cn-math-taxonomy) | 4 000 | a large, actively-maintained maths/English/physics knowledge graph with diagnostics — exactly the substrate an adaptive-learning build needs | 🔴 **`CC-BY-NC-4.0`** · 19 347 B · `41003d4a7474` @ HEAD `cf262d886821` — **NonCommercial** | 🔴 **Unusable in any paid engagement**, which is every Globant engagement. The highest-star education-specific *data* asset found this pass and it is commercially closed |

🔵 **Why this is the headline and not a footnote.** All three resolve, all three serve a root
licence payload, all three would be shelved as supply by any screen that checks *presence* of a
`LICENSE` rather than *reading* it — and two of the three (`CC-BY-NC`, `Elastic-2.0`) are
affirmatively **unsellable**, not merely awkward. This is `Gap 461-B`'s class inverted: that gap
warned that *an index verdict of `NOASSERTION` is not an absent grant*; these rows show that **a
present grant is not a permissive one**. Registered as **`Gap 466-A`**.

### 🟢 Sell-shelf row added this pass — agent/skill tier

🔵 **One row. Not a minimum, a count.** 30 candidate addresses were coverage-checked across two
GitHub channels; **28 were already carried by this base** and 2 were novel, of which **1 is
ungranted**. One remains at this tier, and one is what is published.

| repository | ★ | grant · `sha256₁₂` | region · basis | provenance (declared upstream) | what it actually does |
|---|---|---|---|---|---|
| [`ShawnRen57/omni-learning-anything`](https://github.com/ShawnRen57/omni-learning-anything) | 3 | 🟢 **MIT** · `f3a9a5d7a599` · 1 092 B | Global · 🔴 no single-region basis | 🟡 **none declared** — ships as a portable *agent skill*, no dependency manifest | takes any subject and emits a personalised learning plan plus illustrated daily lessons. 🔵 Shelved less for its own weight (3★) than as a **datapoint in the skill-packaging trend measured on [`agents/trending.md`](trending.md)**: it is supply that assumes a host agent and ships no runtime of its own; HEAD `0d9b20e5c770` |

### 🔴 The ungranted denominator — published, because a silent omission looks like absence

| address | ★ | first-hand verdict |
|---|---|---|
| [`aaryansamanta/ai-ethos`](https://github.com/aaryansamanta/ai-ethos) | **498** | 🔴 **`NO-ROOT-GRANT`** @ HEAD `9acaafc718f2` — resolves, 498★, a nonprofit delivering multilingual AI tutoring to underserved and neurodiverse learners, and it serves **no root licence payload** under any of `LICENSE`, `LICENSE.md`, `LICENSE.txt`, `COPYING`, `LICENCE`. 🔵 The most-starred **ungranted** education row this base has recorded; mission-aligned and legally unusable |
| [`henriquegpb/gradesinteli`](https://github.com/henriquegpb/gradesinteli) | 86 | 🔴 **`NO-ROOT-GRANT`** @ HEAD `2ded74019bb2` — 🔴 **and it is the LATAM row.** Brazilian, built against the Adalove platform. See the standing LATAM finding below |
| [`paher-din/XunJie`](https://github.com/paher-din/XunJie) | 5 | 🔴 **`NO-ROOT-GRANT`** @ HEAD `d72aed730e26` — novel this pass, project-based teaching agent (循阶). Ungranted |

🔴 **The LATAM assignment-feedback gap `p464` registered does NOT close, and now it has a named
cause.** `p464` found the repository matching `intel/market.md`'s clearest LATAM opportunity —
rubric-based assignment feedback — **ungranted**. This pass found the Brazilian grade/feedback row
`gradesinteli` and it is **also ungranted**, at 86★. 🟢 One LATAM row *does* carry a grant
([`menthorlabs/menthor`](https://github.com/menthorlabs/menthor), Apache-2.0, below and on
[`verticals/solutions.md`](../verticals/solutions.md)) but it is a teaching **platform**, not
feedback. 🔵 Two independent passes, two ungranted LATAM feedback rows: this is now a **reproduced**
pattern, not a single miss.

### 🟡 Re-grades of carried rows, confirming rather than correcting

| repository | first-hand read | verdict |
|---|---|---|
| [`virgiliojr94/book-to-skill`](https://github.com/virgiliojr94/book-to-skill) | 🟢 **MIT** · `LICENSE.md` (not `LICENSE`) · 1 068 B · `be9b04bccfb4` @ HEAD `a24e62f4d8ca`, `br=master` | 🟢 permissive, confirmed. **36.2k★** — the largest education-adjacent artefact in this window, and it is a *skill compiler*, not an app |
| [`jcputney/scorm-again`](https://github.com/jcputney/scorm-again) | 🟢 **MIT** · 1 072 B · `383b85b370e8` @ HEAD `86ab328f0e5b`, `br=master` | 🟢 permissive. Substrate → [`repos/foundations.md`](../repos/foundations.md) |
| [`jupyter/nbgrader`](https://github.com/jupyter/nbgrader) | 🟢 **BSD-3-Clause** · 1 512 B · `3a83d5b8e22c` @ HEAD `c2e1ab63512b` | 🟢 permissive. Substrate → [`repos/foundations.md`](../repos/foundations.md) |
| [`CGSeb/lessonfolk`](https://github.com/CGSeb/lessonfolk) · [`OmarZen/scholarship-navigator`](https://github.com/OmarZen/scholarship-navigator) · [`finereli/yarareads`](https://github.com/finereli/yarareads) | 🟢 MIT at **1 063 B** `55873542fedc` / **1 064 B** `cdc1ae6b9064` / **1 066 B** `7c4cf856c78c` | 🟢 three MIT payloads, three sizes, three digests — 🔵 see the fixture finding on [`repos/foundations.md`](../repos/foundations.md): **MIT size is not an identity** |

### 🔴 Gaps this pass registers

| gap | what is wrong | what would close it |
|---|---|---|
| 🔴 **`Gap 466-A`** | **A present grant is not a permissive grant, and no screen on these shelves tests the difference.** Three carried rows (914★, 340★, 4 000★) serve root licence payloads that are respectively content-copyleft, source-available-non-OSI and **NonCommercial**. A "has-a-LICENSE" check passes all three; two are unsellable. | Add a `grant_class` axis read from the payload's **first non-blank line**, with an explicit `UNSELLABLE` value for `*-NC`, `Elastic-*`, `BUSL-*`, `SSPL`, and require it on every sell-shelf row before publication. |
| 🟡 **`Gap 466-B`** | **The ungranted denominator correlates with star count in the wrong direction and nothing here measures it.** The single most-starred row probed this pass that is *not* a known project (`ai-ethos`, 498★) is ungranted, as is the 86★ LATAM row, while 3★ rows carry clean MIT. Visibility is not evidence of a grant, and a pass that prioritises candidates by stars will spend its probes on ungranted supply. | Record `(★, grant-present)` for every probed address in the evidence store and publish the correlation once n ≥ 60, so candidate ordering can be set from measurement rather than from stars. |

## 🆕 `p465` — **🔴 THIS PASS'S OWN INSTRUMENT WAS DEFECTIVE AND THE BASE CAUGHT IT: the three cross-pass controls disagreed with `p464` by exactly −1 byte each, at IDENTICAL HEADs. Three files cannot shrink by one byte at an unchanged HEAD — the fault was mine, it is diagnosed, and all three reproduce exactly once corrected. 🟢 `Gap 463-D` is CLOSED WITH A NUMBER, not with silence: African education supply is 61 repositories whose MAXIMUM star count is 12. 🟢 And a licence class this base has never carried is read first-hand — a WAQF dedication.**

🔴 **Gate posture, stated first per `Gap 446-A`: `make hooks` was DENIED** (`Code from External`)
before any gate body ran — **twelve denials in thirteen passes**. 🔵 **Nothing below is
gate-attested.** Mitigation re-implemented in this session's own code: frontmatter keys and
closed-vocabulary `region` checked on all eight shelves; every new table checked for separator
presence, pipe-count consistency and **no header row published as data**; append-only proved on
both trending shelves by prior-section containment; every address below re-resolved by
`git ls-remote`.

### 🔴 The instrument defect, published before any row it touched

🔵 **Two first-hand channels as `p450`/`p463`/`p464` established:** `git ls-remote <addr> HEAD`
(**tree identity**) and `raw.githubusercontent.com/<addr>/<branch>/LICENSE` (**payload bytes** →
size + `sha256₁₂`). 🔴 **The `curl -sI https://github.com/<addr>` probe the ingest brief
prescribes is reproduced unusable for a fifth independent time** — `403` for live and
nonexistent addresses alike. No row here rests on it.

🔴 **My first reading of all three controls was wrong, in the same direction, by the same amount:**

| control | `p464` published | `p465` **first** read | `p465` **corrected** read | verdict |
|---|---|---|---|---|
| `openedx/edx-platform` | AGPL-3.0 · 35 136 B · `e12d78569742` · HEAD `addd09d7801b` | 35 135 B · `106a1b4b8b71` | **35 136 B · `e12d78569742`** · HEAD **`addd09d7801b`** | 🟢 reproduced exactly |
| `Vacademy-io/vacademy_platform` | AGPL-3.0 · 34 523 B · `0d96a4ff68ad` · HEAD `3a9c66db938c` | 34 522 B · `4df3c306ddda` | **34 523 B · `0d96a4ff68ad`** · HEAD **`3a9c66db938c`** | 🟢 reproduced exactly |
| `DaRL-GenAI/instructional_agents` | MIT · 1 067 B · `4e085d826a64` · HEAD `f835eb45f508` | 1 066 B · `ae280df5a726` | **1 067 B · `4e085d826a64`** · HEAD **`f835eb45f508`** | 🟢 reproduced exactly |

🔵 **Cause, named so no later pass repeats it:** the first instrument captured the payload with
`body=$(curl ...)`. **POSIX command substitution strips trailing newlines**, so every size was
one byte short and every digest was the digest of the file *minus its final `\n`*. Writing
`curl -o <file>` and measuring the file fixes it. 🟢 **The base was right and this pass was
wrong**; the controls are byte-, digest- and HEAD-identical under the corrected instrument.

🔴 **One claim is WITHDRAWN BEFORE PUBLICATION as a result.** The first reading showed AGPL-3.0
at both `34 522` and `34 523` B and I was about to publish "the stock AGPL-3.0 text exists in two
byte-variants". It does not. `Maicarons/RubricSpan` reads **34 523 B · `0d96a4ff68ad`** —
*identical* to `Vacademy-io`. The variance was my own instrument, on one side of the comparison
only.

### 🟡 But the convention defect underneath it is REAL, and it is the base's, not mine

🔴 `p455` published the GPL-3.0 payload as **`35 148` B · `8b1ba204bb69`**. Measured first-hand
this pass, those are exactly the **newline-stripped** figures for stock GPL-3.0, whose raw values
are **35 149 B · `3972dc9744f6`** (`princebilogocode/naabiga-os`, read below). 🔵 So **`p455` and
`p464` published payload sizes under two different conventions**, and nothing on these shelves
declares which a given cell uses. A pass that compares a `p455` cell against a `p464` cell for the
same stock licence sees a 1-byte disagreement and can report a payload change that never happened
— the exact false positive I nearly published above. Registered as **`Gap 465-A`**.

### 🟢 Sell-shelf rows added this pass — agent / skill tier, grants read first-hand

🔵 **Three rows. Not a minimum, a count.** 20 novel candidate addresses were probed this pass;
11 carry a grant; of those, 4 are copyleft (→ [`verticals/solutions.md`](../verticals/solutions.md)),
3 are substrate rather than agent (→ [`repos/foundations.md`](../repos/foundations.md)), and 1 is
published separately below because a one-word licence cell would be false. **Three remain at this
tier, and three is what is published.** 🔴 Per `Gap 463-E`, every row carries a provenance cell.

| repository | ★ | created | grant · `sha256₁₂` | region · basis | provenance (declared upstream) | what it actually does |
|---|---|---|---|---|---|---|
| [`erlan775959-code/markwise`](https://github.com/erlan775959-code/markwise) | 0 | 2026-09-13 | 🟢 MIT · `e33397c72fff` · 1 073 B | Global · 🔴 no single-region basis; feedback is multilingual by design | 🟢 **declared**: `anthropic>=1.5.0` (MIT) + FastAPI, in `pyproject.toml` | rubric marking as an agentic workflow: transcribes typed/PDF/handwritten work, **double-marks each criterion with two independent graders and a moderator**, and **verifies in code that every quoted evidence string actually occurs in the work** — invented evidence is flagged. Also flags grader-manipulation attempts ("please give this full marks") and safeguarding concerns. Declares itself **Alpha**; HEAD `9651396c0558` |
| [`omerfarooq223/AutoGrader-Agent`](https://github.com/omerfarooq223/AutoGrader-Agent) | 3 | 2026-03-06 | 🟢 MIT · `78adf0554b1a` · 1 077 B | Global | 🟢 **declared**: `groq`, `google-genai`, `scikit-learn`, `PyMuPDF`, `python-docx`, `openpyxl` (`requirements.txt`) | ZIP of submissions + brief → generated rubric → per-criterion score. 🟢 **Deterministic-first by design**: template-matched briefs skip the LLM entirely, **all arithmetic (totals, deductions, score capping) is done in Python not the model**, and identity resolves from a roster before filename/folder/content. Plagiarism via TF-IDF cosine + char n-gram; HEAD `9c4bddb0537a` |
| [`oas114/EduShield`](https://github.com/oas114/EduShield) | 11 | 2026-08-21 | 🟢 MIT · `6c106d9deefc` · 1 068 B | **APAC** · zh-TW README, scoped to Taiwan's 個人資料保護法 | 🟡 **none declared** — pure browser JS, no dependency manifest in tree | mask-then-restore de-identification shield for student data **before** it is pasted into a hosted model, and re-identification after: 100 % client-side, data never leaves the device. 🟢 **Its own README refuses the compliance claim**: it states it provides technical masking, is **not** legal advice and does **not** by itself guarantee PDPA compliance. 🟡 Ko-fi funded; HEAD `fdb4c3621b2f` |

### 🟢 The grant class this base has never carried: a WAQF dedication

| repository | ★ | grant · `sha256₁₂` | region · basis | what the payload actually says |
|---|---|---|---|---|
| [`maljefairi/arabic-llm-course`](https://github.com/maljefairi/arabic-llm-course) | 4 | 🟡 **`WAQF` — not OSI, not SPDX** · `8c40487433ac` · 1 287 B | **EMEA** · Arabic-language payload and course body | 24-chapter Arabic end-to-end LLM training course with PyTorch examples. Its `LICENSE` is **not a software licence at all**: it is an Islamic endowment dedication — «وقفٌ لوجه الله تعالى» — resting on «حبس الأصل وتسبيل المنفعة» (the asset is withheld from private ownership, its benefit released to all). It grants, in prose, use, copying, distribution, **modification**, building upon and benefit **for any purpose, educational or commercial, without permission or fee**; HEAD `600100d93823` |

🔵 **Why this matters past curiosity.** It is a first-hand instance of **`Gap 461-B`**'s class —
*an index verdict of `NOASSERTION` is not an absent grant* — arriving from a direction this base
has never sampled. A permissiveness filter keyed on SPDX identifiers drops this repository as
ungranted; read at the payload it is **more** permissive than MIT (it imposes no attribution
condition, only a request). 🔴 **It is nonetheless NOT shelved as build-on supply**, for a reason
that is legal rather than technical: an endowment dedication has no warranty disclaimer, no
licence-grant formalism and no governing-law clause, so what a Globant client's counsel would need
is absent even though the author's intent is plainly maximal. 🟢 Recorded as **supply that exists
and cannot yet be sold**, which is the honest cell.

### 🟡 A conjunctive grant, reproduced from a second independent direction

🔵 `p464` published `guicortei/feynman-technique` as the base's first **conjunctive** payload — MIT
code with a non-MIT carve-out inside the same file. 🟢 **That class reproduces**, from an unrelated
owner and region:

| repository | ★ | grant · `sha256₁₂` | region · basis | the carve-out, quoted |
|---|---|---|---|---|
| [`Zo-Dns/Al-Idrisi.AI`](https://github.com/Zo-Dns/Al-Idrisi.AI) | 4 | 🟡 **MIT + two carve-outs** · `b92c46c14a74` · 1 416 B | **EMEA** · Arabic-language atlas | open-source interactive Arabic atlas of AI. Payload: *"source code and software documentation … licensed under the MIT License below. Original educational content is licensed separately under `docs/legal/CONTENT_LICENSE.md`. Third-party materials are excluded from both grants."* 🔴 **So the thing an education client would actually reuse — the content — is NOT under the MIT cell**; HEAD `bbbc75fd782b` |

### 🔴 Rows REFUSED this pass, with the reason, because a silent omission looks like absence

🔵 `Gap 463-A` asks for arrivals *and* departures to be accounted. These were probed, resolved and
**deliberately not shelved**:

| address | why refused |
|---|---|
| [`Cicada33016/coursera-assistant`](https://github.com/Cicada33016/coursera-assistant) | 🔴 MIT and live (`f0b14a4e5f6e`), but its function is **circumventing assessment**: Coursera video/lecture auto-completion and a quiz solver. Not a Globant build-on asset under any engagement; carried here only so a later recency pass does not re-discover it as novel supply |
| [`five-plus-one/AI-Marker-Suite`](https://github.com/five-plus-one/AI-Marker-Suite) | 🟡 Already carried (36 files). Re-read first-hand: **GPL-3.0 · 35 154 B · `1ab858f515df`** — 🔴 **5 bytes larger than stock GPL-3.0 and a different digest**, so this is a genuinely variant copyleft payload, not the template. 104★, automates marking across 30 Chinese exam platforms **including an unattended mode** ("leave it running overnight, it's all marked by morning") that bypasses double-marking arbitration. Named as a **risk exhibit**, not supply |
| `Gayatri-Education/Gayatri-Demo` · `majid-alsakani/sini-alkhafif-app` · `btc-plain-talk/bitcoin-plain-talk` · `Durrell-229/academie-composition` · `adoumouangnamouemmanuel/AfridemiQ` | 🔴 **`NO-ROOT-GRANT`** — all five resolve at `git ls-remote` and serve no root licence payload under any of `LICENSE`, `LICENSE.md`, `LICENSE.txt`, `COPYING`, `LICENCE`. This is the **ungranted denominator** for this pass: 5 of 20 novel addresses |
| `godz1llla/awesome-kazakhstan-dev` | 🟡 Resolves, 39★, but it is an **awesome-list**, not a build-on artefact. Recorded so the count is honest, not shelved |

### 🟡 Discovery hygiene: a same-owner BATCH, which the topic-set detector of `Gap 464-B` would miss

🔴 `KajarnakLOKOSSOU2008/kajarai` and `KajarnakLOKOSSOU2008/edubox` were created
**`2026-09-04T13:18:18Z` and `2026-09-04T13:18:20Z` — two seconds apart, by one owner.** 🔵
`Gap 464-B`'s detector compares topic sets *across unrelated owners* to catch template clones;
this is the sibling case it does not cover — **mass-scaffolded repositories under a single owner**,
where the tell is the creation timestamp, not the topics. Only `edubox` serves a grant and only
`edubox` is shelved. Registered as **`Gap 465-B`**.

### 🔴 Gaps this pass registers

| gap | what is wrong | what would close it |
|---|---|---|
| 🔴 **`Gap 465-A`** | Payload sizes on these shelves are published under **two undeclared conventions** — `p455` newline-stripped, `p464` raw bytes — so the same stock licence reads 1 byte apart across passes and a comparison manufactures a phantom payload change. | Declare **raw bytes** the contract in the Makefile gate, add a `sha256` of stock MIT/Apache-2.0/GPL-3.0/AGPL-3.0 as fixtures, and re-grade any carried cell whose size is one byte under the fixture. |
| 🟡 **`Gap 465-B`** | `Gap 464-B`'s template-clone detector keys on topic sets **across owners** and therefore cannot see **same-owner batch scaffolding** (two repos created 2 s apart, one ungranted). | Add a creation-timestamp clustering check: flag any candidate whose owner published ≥2 repositories within 60 s. |
| 🔴 **`Gap 465-C`** | The `WAQF` row is permissive **in substance** and unsellable **in form**, and this base has no cell for that state — it is recorded in prose only, so a filter sees either "permissive" or "ungranted" and both are wrong. | Add a `grant_form` axis (`OSI` / `bespoke-formal` / `dedication-informal`) distinct from `grant_permissiveness`, and re-grade the carried `CC-BY-SA`, `Waqf` and `NOASSERTION` rows against it. |
| 🟡 **`Gap 465-D`** | `Gap 463-D` is closed for **supply** (measured below) but the Africa/MEA **intel** leg returned nothing for Kenya at all, while supply for Kenya exists (`Civicom-Aid/matokeo-rms`, MIT). Intel and supply are nil on opposite sides. | Run the Kenya intel leg against named instruments — Commission for University Education, Ministry of Education ICT policy — rather than "Kenya AI education". |


## 🆕 `p464` — **🟢 The recency channel `p463` opened is REPRODUCED by an independent operator: 20 candidates, 12 absent from this entire base, 7 granted, 6 permissive. 🔴 And the one row that matches the clearest LATAM opportunity on `intel/market.md` — rubric-based assignment feedback — is UNGRANTED, so the gap that file names cannot be closed with the supply this one found. 🟡 One grant is published as CONJUNCTIVE: MIT code with a non-MIT corpus carve-out inside the same payload.**

🔴 **Gate posture, stated first per `Gap 446-A`: `make hooks` was DENIED, and so was every
individual gate.** The harness permission classifier refused both `make hooks` and a direct
`python3` invocation of the repo's own gate scripts (`Code from External`) — **eleven denials in
twelve passes, and one step stricter than `p463`**, which was still permitted to run
`p277-table-structure` and `p383-region-heading-gate` by hand. 🔵 **Nothing below is
gate-attested.** Mitigation, re-implemented in this session's own code rather than the repo's:
frontmatter keys and closed-vocabulary `region` checked on all eight shelves; every new table
checked for separator presence, pipe-count consistency and **no header row published as data**;
append-only proved on both trending shelves by prior-section containment; **every address
introduced this pass re-resolved by `git ls-remote`.**

🔵 **Instrument.** Two first-hand channels, as `p450` and `p463` established:
`git ls-remote <addr> HEAD` (**tree identity**) and
`raw.githubusercontent.com/<addr>/<branch>/LICENSE` (**payload bytes** → size + `sha256₁₂`).
🔴 **The `curl -sI https://github.com/<addr>` probe the ingest brief prescribes is reproduced
unusable, now from a fourth independent direction:** it returns `403` for a live address and for
a nonexistent one *alike* — `openedx/edx-platform` and `gmilano/this-does-not-exist-xyz123` are
indistinguishable through it. No row here rests on it.

🔴 **A channel measurement that is new this pass, and a future pass will misread it if it is not
written down: the GitHub *search* API is not reachable from the `gh` CLI here.**
`gh api "search/repositories?q=..."` returns **`403 — "sessions are bound to their configured
repositories. Use repository-scoped endpoints"`**. Repository search survives **only** through
the MCP `search_repositories` tool; `gh` reaches only the two attached repos. 🔵 A pass that
reaches for `gh` to discover supply will read that `403` as *no results* and publish a nil that
is an artifact of the channel — the exact error class `p463` caught on the web legs.

### 🟢 Cross-pass controls — reproduced before any verdict

| control | published by `p463` | this pass read | verdict |
|---|---|---|---|
| 🟢 `openedx/edx-platform` `LICENSE` | AGPL-3.0 · 35 136 B · `e12d78569742` · HEAD `addd09d7801b` | **35 136 B · `e12d78569742`** · HEAD **`addd09d7801b`** | 🟢 **reproduced, byte-, digest- and HEAD-identical** |
| 🟢 `Vacademy-io/vacademy_platform` `LICENSE` | AGPL-3.0 · 34 523 B · `0d96a4ff68ad` · HEAD `3a9c66db938c` | **34 523 B · `0d96a4ff68ad`** · HEAD **`3a9c66db938c`** | 🟢 **reproduced** |
| 🟢 `DaRL-GenAI/instructional_agents` `LICENSE` | MIT · 1 067 B · `4e085d826a64` · HEAD `f835eb45f508` | **1 067 B · `4e085d826a64`** · HEAD **`f835eb45f508`** | 🟢 **reproduced** |

### 🟢 Sell-shelf rows added this pass — agent / skill tier, grants read first-hand

🔵 **Five rows. Not a minimum, a count:** 12 novel addresses were probed, 7 carry a grant, and of
those 7 one is AGPL-3.0 (→ [`verticals/solutions.md`](../verticals/solutions.md)) and one is
substrate rather than agent (→ [`repos/foundations.md`](../repos/foundations.md)). Five remain,
and five is what is published.

| repository | ★ | created | grant · `sha256₁₂` | region · basis | what it actually does |
|---|---|---|---|---|---|
| [`maplexrain/unyra`](https://github.com/maplexrain/unyra) | 54 | 2026-09-29 | 🟢 MIT · `f7ef32f1240e` · 1 067 B | **APAC** · zh README (归一 Unyra) | local-first exploratory-learning desktop app (Electron + React); HEAD `ebec6b22918d` |
| [`Kaiji-Z/dsh-plugin-lookatstudy`](https://github.com/Kaiji-Z/dsh-plugin-lookatstudy) | 22 | 2026-08-15 | 🟢 MIT · `157154a57ac1` · 1 081 B | Global · 🔴 no language or institution basis; the DeepSeek-Harness ecosystem is **not** a region | turns any markdown / folder / GitHub repo into a gated skill-tree course with **BKT mastery + SM-2 review**; HEAD `d7d86c48c1af` |
| [`Nauv357/pickq`](https://github.com/Nauv357/pickq) | 22 | 2026-08-08 | 🟢 MIT · `91192368c03b` · 1 064 B | Global | PDFs / notes / screenshots → private question bank, spaced repetition, **fully offline**; default branch `master`, HEAD `31753c5f106f` |
| [`junichikatsu/SocraMetry`](https://github.com/junichikatsu/SocraMetry) | 16 | 2026-08-09 | 🟢 MIT · `7b779e5b512d` · 1 069 B | **APAC** · ja README, B2B | Socratic questioning that **returns questions, not answers**, plus 5-axis attainment / accuracy / growth scoring meant as evidence for HR review; default branch `develop`, HEAD `dd46d7a4aa1c` |
| [`guicortei/feynman-technique`](https://github.com/guicortei/feynman-technique) | 16 | 2026-07-28 | 🟡 **MIT + carve-out** · `be43f29a819a` · 1 695 B | Global · 🔴 owner handle reads lusophone; **a handle is not a basis** and this is not placed on it | explanation-ladder agent skill: mechanism before name, one analogy with its limits; HEAD `7905e9b1a230` |

### 🟡 The conjunctive grant, published as its own row because a one-word licence cell would be wrong

🔵 [`guicortei/feynman-technique`](https://github.com/guicortei/feynman-technique)'s payload is
**1 695 B where every other MIT payload this pass read is 1 064–1 081 B**, and the difference is
not boilerplate drift. Read first-hand, the file is the MIT text **plus a titled section**:

> *NOTE ON QUOTED MATERIAL* — quotations "remain the property of their respective copyright
> holders and are **not licensed under the MIT terms above**"; *The Feynman Lectures on Physics*
> is **© California Institute of Technology**, free to read online but **not in the public
> domain**.

🟢 **The grading, and it is the useful part for a client deliverable:** the **code** is MIT and
may be vendored; the **corpus the skill is built from is not**, and the payload says so in its
own words. 🔴 A shelf cell reading `MIT` alone would license a Globant engagement to ship the
corpus. This is `p427`'s conjunctive-grant class arriving on the agent tier, where the base has
mostly seen it on platforms, and it is the reason the size anomaly was read instead of rounded off.

### 🔴 Not shelved, with the reason — and one of them is the LATAM opportunity this base already named

| address | ★ | created | HEAD | why not shelved |
|---|---|---|---|---|
| [`tjayze/olympiad-problem-forge`](https://github.com/tjayze/olympiad-problem-forge) | 56 | 2026-09-21 | `e7e488923641` | 🔴 **no licence payload** on any of `LICENSE`, `LICENSE.md`, `LICENSE.txt`, `COPYING`, `LICENCE` — ungranted |
| [`princechhimpachhimpasaab-lang/omega-epsilon-problem-forge`](https://github.com/princechhimpachhimpasaab-lang/omega-epsilon-problem-forge) | 55 | 2026-08-25 | `1571d001e055` | 🔴 ungranted — **and see the clone finding below** |
| [`roVeloupe/essay-grader`](https://github.com/roVeloupe/essay-grader) | 20 | 2026-09-07 | `f124b665d881` | 🔴 ungranted. 🔵 **This is the painful one:** photo → OCR → proofreading → **rubric-based grading** → export is precisely the assignment-feedback workflow `intel/market.md` names as LATAM's clearest opening (92 % student adoption vs **19 %** faculty feedback use). The matching tool exists and **may not be used** |
| [`vincenzo-afk/PenFlow`](https://github.com/vincenzo-afk/PenFlow) | 25 | 2026-08-14 | `f5ba85efbd33` | 🔴 ungranted — local-first handwriting / OCR study pages |
| [`scriptology/open-course-cli`](https://github.com/scriptology/open-course-cli) | 17 | 2026-07-16 | `99f761f44d73` | 🔴 ungranted — terminal language tutor in Rust |

🔵 **Ungranted rate this pass: 5 of 12 (41.7 %).** 🟢 That is the *same order* as the 6-of-6 and
4-of-17 figures `p463` measured on different slices, and it is now the stable shape of this
channel: **roughly half of what recency discovery returns cannot be built on at all**, which is
an argument for budgeting discovery against grant yield rather than hit count.

### 🔴 A discovery-channel hygiene finding: recency + a star floor does not screen out TEMPLATE CLONES

🔵 Two of the five ungranted rows are not two projects. Measured side by side:

| field | [`tjayze/olympiad-problem-forge`](https://github.com/tjayze/olympiad-problem-forge) | [`princechhimpachhimpasaab-lang/omega-epsilon-problem-forge`](https://github.com/princechhimpachhimpasaab-lang/omega-epsilon-problem-forge) |
|---|---|---|
| description | "Best Open-Source Math Olympiad Problem Generator 2026" | "Olympiad Problem Generator **2026**: Create Infinite **Spanish** Math Olympiad-Style Challenges" |
| topic set | 14 topics incl. `epsilon-ome-trainer`, `llama-cpp-python`, `pyqt5`, `sqlite3`, `ome` | 🔴 **the same 14 topics, identical strings** |
| language · forks · grant | HTML · 0 · none | HTML · 0 · none |
| ★ · created | 56 · 2026-09-21 | 55 · 2026-08-25 |
| `fork` flag | `false` | `false` |

🔴 **Both declare `fork: false`, so the fork-lineage channel cannot see this.** An identical
14-string topic set across two unrelated owners, with near-identical descriptions, 0 forks each
and star counts one apart, is a template clone, not independent corroboration of a trend.
🟢 **The cheap detector is the topic set**, which this base already collects and does not compare.
🔴 **Why it matters beyond hygiene:** the second one says **"Spanish"**, and a pass hunting LATAM
supply — which `intel/market.md` has hunted for five passes — would have shelved it as a LATAM
find. It is ungranted and probably synthetic. Registered as `Gap 464-B`.

## 🆕 `p463` — **🟢 THE SATURATION NIL BREAKS ON BOTH SIDES AT ONCE. One date bound returned 13 addresses absent from this entire base, 11 of them granted — after four passes published "usable novel yield ZERO". 🔴 And an audit of this base's OWN evidence store found a channel nothing here measures: 21 projects were SILENTLY EVICTED from every sell shelf since `p406`, 10 of them live and permissive, including the only differential-privacy row this base has ever carried. 🔵 My own first reading of that — a 15.5 % ledger defect — is REFUTED and withdrawn before publication: graded at its own commit the ledger is 238/238 correct.**

🔴 **Gate posture, stated first per `Gap 446-A`: `make hooks` was NOT RUN.** The harness
permission classifier **refused the invocation outright** (`Code from External`) — the same
refusal `p462` recorded, not a proxy failure and not a missing target. **Nothing below is
gate-attested**, and the gate's inability to run remains the standing obstacle: `Gap 446-A`
cannot be closed by a pass that is not permitted to run the gate.

🔵 **Instrument, and one channel the prescribed probe cannot replace.** Two channels, both
first-hand: `git ls-remote <addr> HEAD` (**tree identity**) and `raw.githubusercontent.com`
(**payload bytes**). 🔴 **The `curl -sI https://github.com/<addr>` check this base is instructed
to use is unusable from this host: it returns `403` for every address, live or withdrawn** —
`openedx/edx-platform` and a non-existent slug are indistinguishable through it. A probe that
returns the same code for a 200 and a 404 is not a verification step, and no row below rests on
it. This reproduces `p450`'s replacement of that probe from an independent direction.

### 🟢 Cross-pass controls — reproduced before any verdict

| control | published by `p462` | this pass read | verdict |
|---|---|---|---|
| 🟢 `openedx/edx-platform` `LICENSE` | AGPL-3.0 · 35 136 B · `e12d78569742` · HEAD `addd09d7801b` | **35 136 B · `e12d78569742`** · HEAD **`addd09d7801b`** | 🟢 **reproduced, byte-, digest- and HEAD-identical** |
| 🟢 `Vacademy-io/vacademy_platform` `LICENSE` | AGPL-3.0 · 34 523 B · `0d96a4ff68ad` · HEAD `3a9c66db938c` | **34 523 B · `0d96a4ff68ad`** · HEAD **`3a9c66db938c`** | 🟢 **reproduced** |
| 🟢 `DaRL-GenAI/instructional_agents` `LICENSE` | MIT · 1 067 B · `4e085d826a64` · HEAD `f835eb45f508` | **1 067 B · `4e085d826a64`** · HEAD **`f835eb45f508`** | 🟢 **reproduced** |

🟢 `p462`'s rule — *a byte-identical licence payload is near-zero evidence of repository
identity* — is **independently confirmed on a new pair this pass found**:
[`sitor-ai/frametell`](https://github.com/sitor-ai/frametell) serves the **same** AGPL-3.0
payload as `Vacademy-io/vacademy_platform` (34 523 B · `0d96a4ff68ad`) at a **different** HEAD
(`683b3e5e8cfa` ≠ `3a9c66db938c`). Two unrelated projects, one stock text.

### 🟢 The saturation nil is an artifact of the DISCOVERY SLICE, not of supply — and the variable is RECENCY

🔴 Four consecutive passes (`p459`–`p462`) graded the prescribed channel and published the same
verdict: *usable novel repository yield ZERO*. 🟢 **That verdict is correct about the channel and
wrong about the supply.** Both legs were run this pass, side by side:

| channel | addresses returned | absent from the ENTIRE base | granted | permissive |
|---|---|---|---|---|
| 🔴 the prescribed web-search legs (4 global + 4 regional) | ~30 repo-shaped tokens | 🔴 **0** | — | — |
| 🟢 GitHub repository-search API, `created:>` × `stars:>` slice | **17** | 🟢 **13** | 🟢 **11** | 🟢 **10** |

🔴 **Every repo-shaped token the web legs returned falls into one of three already-known
buckets**, which is why they grade nil: a general-purpose agent (OpenHands, CrewAI, `opencode`,
OpenClaw — not education supply), an already-carried vertical platform (OpenEduCat, Open edX,
ERPNext/`frappe`, Moodle, Kolibri, RosarioSIS, Dolibarr, Fedena), or an already-carried education
repository (`withmarbleapp/os-taxonomy`).

🟢 **One of those requires a correction to how a nil gets read.** The vertical leg returned
**openSIS**, and a slug-shaped guess (`openSIS-Classic/OpenSIS-Classic`) is `grep`-absent from
this base — which looks like a discovery. It is not: the platform is carried under its real
address [`OS4ED/openSIS-Classic`](https://github.com/OS4ED/openSIS-Classic), on **3** sell
shelves. 🔴 **A novelty check keyed on a guessed slug manufactures false positives**; the check
must be keyed on the address the probe resolves.

🟢 **And the probe returned a free identity reading while confirming it:**
`OS4ED/openSIS-Classic` and `OS4ED/openSIS-Responsive-Design` both resolve to HEAD
**`8348cd069aa2`** — the same tree under two names. 🟡 Graded honestly, same-HEAD is **alias *or*
undiverged fork** and this pass does not claim which; per `p462` the payload cannot settle it
either (both serve no root grant at all). Registered as `Gap 463-C`.

🔵 **The variable that bought the 13, stated so the next pass can reuse it.** Not vocabulary —
`p453`'s vocabulary-spend ledger already shows vocabulary exhausted, and this pass's Spanish and
platform-name legs returned **0** and **0**. The variable is **`created:>2026-06-01`**. The
education supply is being written *now*, faster than the shelves sample it, and a star-ranked
query without a date bound returns the same incumbents every hour. **A date bound is the cheapest
discovery instrument this base has.**

### 🔴 This base has a SILENT EVICTION CHANNEL, and it is as productive to mine as discovery

🔵 **The suspicion this pass started with was REFUTED before it was published**, and the method
matters more than the result. `evidence/carried-existence.2026-10-23-p406.tsv` records, per
address, the files that carried it; **238** of its rows name `agents/top.md`. Checked against
`agents/top.md` **at HEAD**, 37 of those 238 are absent — which reads as a 15.5 % ledger defect,
exactly the shape `p455` retracted in full. 🟢 So it was checked against **its own commit**
(`ed3d76c`, pass 406) first:

| graded against | rows naming `agents/top.md` | address absent from the file |
|---|---|---|
| 🟢 `ed3d76c` — the ledger's **own** commit | 238 | 🟢 **0** |
| 🔴 `a2bfd2d` — HEAD (`p462`) | 238 | 🔴 **37** |

🟢 **The ledger was right about all 238.** There is no ledger defect. The 37 are **evictions** —
addresses that were on `agents/top.md` at `p406` and are not on it now. 🔴 **`p455`'s lesson
holds and is restated: a disagreement between an instrument and a shelf is a question about
WHEN, and grading it at one commit answers the wrong one.**

🔴 **What the 37 did next, measured first-hand against the current tree:**

| fate | n | reading |
|---|---|---|
| 🟢 **moved** to `repos/foundations.md` or `verticals/solutions.md` | **16** | legitimate reorganisation — `p443`'s agent-addressable split, working |
| 🔴 **dropped from every sell shelf** | **21** | survive only in the append-only record |

🔴 **And the denominator that makes it a finding rather than a tidy-up:** over the same span
`agents/top.md` grew from **187 to 374** distinct addresses and from **1 576 to 3 767** lines.
**The shelf doubled while quietly evicting 21 projects.** Every gate in this base measures
*arrival* — `gate-promotion`, the promotion ledger, the arrival baseline, `PROMO_RATCHET`.
🔴 **Nothing measures departure.** An address can leave a sell shelf with no row, no reason and
no gate, and this pass found it only by diffing a nine-pass-old evidence file against the tree.
Registered as **`Gap 463-A`: the sell shelves need an eviction ledger, and a row may only leave
with a stated reason.**

🟢 **All 21 were re-probed this hour. Eleven evictions are justified by a reason this pass can
state from first-hand evidence:**

| evicted address | first-hand reading | eviction |
|---|---|---|
| [`eastarctica/canvas-mcp`](https://github.com/eastarctica/canvas-mcp) | 🔴 **no HEAD, no payload** — the address no longer resolves | 🟢 **justified** |
| [`naresh1401/education-tutor-agent`](https://github.com/naresh1401/education-tutor-agent) | HEAD `2cb9dcf317c1`, 🔴 no grant payload | 🟢 justified |
| [`a-r007/multi-agent-study-assistant`](https://github.com/a-r007/multi-agent-study-assistant) | HEAD `3c1c88b95a9d`, 🔴 no grant payload | 🟢 justified |
| [`adorsys-gis/moodle-aiprovider_openaicompatible`](https://github.com/adorsys-gis/moodle-aiprovider_openaicompatible) | HEAD `371278b0ebd6`, 🔴 no grant payload | 🟢 justified |
| [`lmscloud-io/moodle-aiprovider_openaicompatible`](https://github.com/lmscloud-io/moodle-aiprovider_openaicompatible) | HEAD `040b74d5b13e`, 🔴 no grant payload | 🟢 justified |
| [`matsuolab/lecture-ai-engineering-2026-hi`](https://github.com/matsuolab/lecture-ai-engineering-2026-hi) | HEAD `d74eafdda870`, 🔴 no grant payload | 🟢 justified |
| [`murderszn/open-tutor`](https://github.com/murderszn/open-tutor) | 🔴 **869 B · `c341a936e405`, UNTITLED** — a notice, not a stock grant (`GRANT-BY-REFERENCE` class) | 🟢 justified |
| [`lamb-project/lamb`](https://github.com/lamb-project/lamb) | **GPL** · 35 349 B · `17fe6d0ffa96` · HEAD `d49c5843626b` | 🟢 justified — copyleft, not a build-on row |
| [`lamb-project/lamba`](https://github.com/lamb-project/lamba) | **GPL-3.0** · 35 149 B · `3972dc9744f6` · HEAD `87e203af202c` | 🟢 justified — 🔵 and note: **different digest AND different HEAD from `lamb`** → two projects, never one pair |
| [`openedx/ease`](https://github.com/openedx/ease) | **AGPL-3.0** · `LICENSE.txt` 35 136 B · `e12d78569742` · HEAD `056da0adc6f3` | 🟢 justified — network copyleft |
| [`edx/ease`](https://github.com/edx/ease) | **AGPL-3.0** · identical payload · HEAD **`056da0adc6f3`** | 🟢 justified — 🟢 same HEAD as `openedx/ease`: **one project, two addresses** |

🔴 **Ten are not.** These are **live, permissively granted, already-verified** projects sitting on
no sell shelf, with nothing in the base stating why they left:

| recoverable address | grant, read first-hand this hour | HEAD | region · basis | why a studio wants it |
|---|---|---|---|---|
| [`pytorch/opacus`](https://github.com/pytorch/opacus) | 🟢 **Apache-2.0** · `LICENSE` 10 241 B · `bcf6964d43d8` | `df040e4a1594` | North America · Meta/PyTorch | 🔴 **the only differential-privacy row this base has ever carried** — and it is the control EMEA's high-risk duty asks for |
| [`meta-pytorch/opacus`](https://github.com/meta-pytorch/opacus) | 🟢 Apache-2.0 · identical payload | **`df040e4a1594`** | North America | 🟢 same HEAD as `pytorch/opacus` → **one project, two addresses**; cite one |
| [`bartmassey-upstream/canvas-mcp`](https://github.com/bartmassey-upstream/canvas-mcp) | 🟢 **MIT** · 1 071 B · `5385a26e2fac` | `b62e1ec8abd6` | Global · no placement signal | Canvas LMS over MCP — agent-addressable today |
| [`bibo242/blackboard-mcp`](https://github.com/bibo242/blackboard-mcp) | 🟢 **MIT** · 1 084 B · `d65abf96e389` | `1fd96db0378d` | Global · no placement signal | Blackboard over MCP — the only Blackboard seam here |
| [`anonymousonyx22/canvas-lms-student-mcp`](https://github.com/anonymousonyx22/canvas-lms-student-mcp) | 🟢 **MIT** · 1 072 B · `ed912ca72d9e` | `e1335f93f05c` | Global · no placement signal | student-scoped Canvas MCP — the read side of the same tier |
| [`ai4bharat/anudesh-backend`](https://github.com/ai4bharat/anudesh-backend) | 🟢 **MIT** · 1 067 B · `e2cd4cec54f7` | `4e6460823f5b` | **APAC** · AI4Bharat, IIT Madras | Indic instruction-data collection backend |
| [`ai4bharat/indicifeval`](https://github.com/ai4bharat/indicifeval) | 🟢 **MIT** · 1 074 B · `1bff713bf26a` | `1bb5f1bc4936` | **APAC** · AI4Bharat, IIT Madras | 🟢 instruction-following **evaluation** for Indic languages — the evidence layer `HolonIQ`'s trend demands |
| [`lowwwbank/anything-to-course`](https://github.com/lowwwbank/anything-to-course) | 🟢 **MIT** · 1 066 B · `d41346e796d6` | `f11bbf21572a` | Global · no placement signal | material → spaced-repetition course, as an agent skill |
| [`098765d/ai_tutor`](https://github.com/098765d/ai_tutor) | 🟢 **MIT** · 1 059 B · `15ecd34b91de` | `e7503b7c95de` | Global · no placement signal | tutor reference implementation |
| [`sirhanmacx/claw-ed`](https://github.com/sirhanmacx/claw-ed) | 🟢 **MIT** · 1 078 B · `4d5d987f4f89` | `18f2e223cdd1` | Global · no placement signal | agent-harness education skill |

🔵 **The comparison is the point of this pass.** Discovery, run on the best channel available,
bought **11** granted novel addresses for eight web legs and six API queries. Re-reading the
base's own nine-pass-old evidence file bought **10** already-verified permissive addresses for
**zero network calls**. 🟢 **Re-promotion is not housekeeping; at this maturity it is a
discovery channel with a better yield per unit of spend**, and it is the one channel four
consecutive nil-passes never tried. Recipe: `Pattern AW`.

### 🟢 Novel agent-addressable rows — 8, each grant read first-hand this hour

🔵 Placement rule is `p443`'s: **agent-addressable** (a skill, agent or MCP server a tutoring or
administrative agent can call today) lands here; APIs, scrapers, schemas and stacks land on
`repos/foundations.md`. Star counts are a **point reading** from the GitHub repository-search API
this hour, not a trend.

| repository | grant · payload · `sha256₁₂` | HEAD | ★ | region · basis | what it does |
|---|---|---|---|---|---|
| [`ERRRC/kaogong-shuati`](https://github.com/ERRRC/kaogong-shuati) | 🟢 **MIT** · `LICENSE` 1 062 B · `449d0e5f8c86` | `12cf8e73be8f` | 122 | **APAC** · Chinese civil-service exam (国考/省考) | offline-first question bank with AI explanation and an error book; PWA + SQLite, self-hostable |
| [`Andiii208/seu-handbook-skill`](https://github.com/Andiii208/seu-handbook-skill) | 🟢 **MIT** · `LICENSE` 1 497 B · `965a0edb5701` | `38f5000aa444` | 52 | **APAC** · Southeast University, CN | an institution's student handbook split **per clause with provenance** into a local agent skill — the cleanest template here for "institutional rulebook → auditable agent" |
| [`Queena34/StudyPilot`](https://github.com/Queena34/StudyPilot) | 🟢 **MIT** · `LICENSE` 1 065 B · `1c49d485d539` | `abe229cb120b` | 50 | **APAC** · Chinese-language README | 🟢 multi-agent coach that answers **only from the uploaded course material, with citations, and says so when the material does not cover it** — the refusal behaviour is the auditable property |
| [`ryannli/immersive-reading`](https://github.com/ryannli/immersive-reading) | 🟢 **MIT** · `LICENSE` 1 063 B · `db7ff5821c21` | `efce3dc24138` | 48 | Global · no placement signal | long-form source → chaptered learning space with attribution, search, highlights, notes |
| [`callmevanshh/campusask`](https://github.com/callmevanshh/campusask) | 🟢 **MIT** · `LICENSE` 1 067 B · `0b3e2dc7fa93` | `7cb9e1c32190` | 41 | **APAC** · IIIT Delhi, India | cited Q&A over official academic-rule PDFs with page links — RAG + FastAPI |
| [`2362094903-ops/study-assistant-skills`](https://github.com/2362094903-ops/study-assistant-skills) | 🟢 **MIT** · `LICENSE` 1 062 B · `d4b1c51084cb` | `3f555b845ac1` | 27 | **APAC** · Chinese postgrad exam (考研) | skill suite: mind map, lecture notes, past-paper-style exam, error book, Feynman check, mastery dashboard, progress across sessions. 🔴 **In this base's record since `p434`, graded `OK`/MIT there, and on no sell shelf until now** — a second instance of `Gap 443-A` |
| [`mantou6666/Math-Modeling-Agent-Flow`](https://github.com/mantou6666/Math-Modeling-Agent-Flow) | 🟢 **MIT** · `LICENSE` 1 067 B · `b66691d6d740` | `69b2a4f15995` | 26 | **APAC** · CUMCM / MCM-ICM contests | four-stage pipeline Solver→Paper→Finalizer→Growth with explicit anti-hallucination and version-conflict stages |
| [`Aisland-SJL/Aisland-teach`](https://github.com/Aisland-SJL/Aisland-teach) | 🟢 **MIT** · `LICENSE` 1 099 B · `f46f29be1b28` | `e11b8fc33344` | 16 | **APAC** · bilingual EN / 简体中文 | teaches from the learner's actual level then **verifies by making them restate it**. 🔵 Declares derivation from [Matt Pocock's `teach` skill](https://github.com/mattpocock/skills) (MIT) in its README — the attribution chain is stated, not inferred |

### 🔴 Refused this pass, named rather than padded

| address | ★ | HEAD | why refused |
|---|---|---|---|
| [`Frisher1/ClaudeCode-Workflow-Lab`](https://github.com/Frisher1/ClaudeCode-Workflow-Lab) | 117 | `415cca9127eb` | 🔴 **no grant payload** at any of `LICENSE`, `LICENSE.md`, `LICENSE.txt`, `COPYING` on `main` or `master`. Ungranted ≠ permissive |
| [`Ciucky/no-numb`](https://github.com/Ciucky/no-numb) | 32 | `891d93f87974` | 🔴 **no grant payload**, same enumeration |
| [`sitor-ai/frametell`](https://github.com/sitor-ai/frametell) | 407 | `683b3e5e8cfa` | 🟡 **not novel** — carried in this base's record since `p445` and graded there. 🔴 And **AGPL-3.0** (34 523 B · `0d96a4ff68ad`), so it is not a build-on row whatever its star count. 🔵 Its HEAD has moved since the record's `b9bcbc2312f8` |

### 🔵 Gap register opened by this pass

| gap | statement | how the next pass closes it |
|---|---|---|
| 🔴 **`Gap 463-A`** | The sell shelves have **no eviction ledger**. 21 projects left every sell shelf between `p406` and `p462` with no row, no reason and no gate; every existing gate measures arrival. | Write `evidence/evictions.<date>-p<N>.tsv` from the `Pattern AW` diff, and add a gate that fails when an address on the previous commit's sell shelves is absent from this one **without a reason cell**. |
| 🔴 **`Gap 463-B`** | A novelty check keyed on a **guessed slug** manufactures false positives — `openSIS` read as uncarried when `OS4ED/openSIS-Classic` sits on 3 shelves. | Resolve the product name to an address through the probe **before** the `grep`, and key the check on the resolved address. |
| 🟡 **`Gap 463-C`** | `OS4ED/openSIS-Classic` and `OS4ED/openSIS-Responsive-Design` share HEAD `8348cd069aa2`. Alias or undiverged fork is **unsettled**, and neither serves a root grant so the payload channel cannot settle it. | Run `gate-fork-direction`'s full-history channel on the pair. |
| 🔴 **`Gap 463-D`** | **The Middle East and Africa returned nothing on any EMEA leg** — EMEA's evidence here is EU-27 + UK + Germany only. | Run legs keyed on named national systems (as `p443` did for LATAM) rather than on the region word: Gulf ministry platforms, Nigerian and Kenyan HE systems, francophone African curricula. |
| 🟡 **`Gap 463-E`** | Skill-tier supply (**7 of 13** novel addresses) carries **derivation chains stated only in the README**. A `LICENSE` read grades such a row clean while saying nothing about what it was built from. | Make `p288`'s README channel standing for the skill tier: every skill-tier row records a provenance cell (declared upstream + its grant) or `PROVENANCE-UNSTATED`. |
| 🔴 **`Gap 446-A`** | **Still open, and still not closable by this pass.** `make hooks` was refused (`Code from External`); nothing in this pass is gate-attested. | Needs a harness permission decision, not a pass. |

## 🆕 `p462` — **`Gap 461-A` IS CORRECTED, AND THE CORRECTION SHRINKS IT: of the four addresses `p461` published as stale aliases, only TWO are aliases. One is a DIVERGED FORK PAIR that `p461` mistook for a rename because the two repositories serve the same stock MIT text, and one was never a live shelf address at all. 🔴 And the saturation nil is reproduced a fifth time — this time on the PRESCRIBED web-search channel itself, 36 tokens graded, usable novel repository yield ZERO.**

🔴 **Gate posture, stated first per `Gap 446-A`: `make hooks` was NOT RUN, and the reason is new.**
This pass is executing under a harness whose permission classifier **refused the `make hooks`
invocation outright** (`Code from External`) — not a proxy failure, not a missing target, a refusal
to execute the repository's own Makefile. So **nothing below is gate-attested**, and the gate's
inability to run is itself the standing obstacle: `Gap 446-A` cannot be closed by a pass that is
not permitted to run the gate.

🔵 **Instrument.** Three channels, and the decisive one is new to this line of passes:
`git ls-remote <addr> HEAD` (**tree identity**), `raw.githubusercontent.com` (**payload bytes**, reused
deliberately as the cross-pass control), and the authenticated GitHub repository-search API
(**index resolution and exact `stargazers_count`**).

### 🟢 Cross-pass controls — reproduced before any verdict

| control | published by `p461` | this pass read | verdict |
|---|---|---|---|
| 🟢 `openedx/edx-platform` `LICENSE` | AGPL-3.0 · 35 136 B · `e12d78569742` | **35 136 B · `e12d78569742`** | 🟢 **reproduced, byte- and digest-identical** |
| 🟢 `Vacademy-io/vacademy_platform` `LICENSE` | AGPL-3.0 · 34 523 B · `0d96a4ff68ad` | **34 523 B · `0d96a4ff68ad`** | 🟢 **reproduced** |
| 🟢 `DaRL-GenAI/instructional_agents` `LICENSE` | MIT · 1 067 B · `4e085d826a64` | **1 067 B · `4e085d826a64`** | 🟢 **reproduced** |
| 🟢 `openeducat/openeducat_erp` `19.0/LICENSE` | 8 241 B | **8 241 B · `528f840368`** | 🟢 **reproduced, and the digest is now recorded** |

### 🟢 Identity graded by HEAD sha — the channel `p461` did not have

`git ls-remote <addr> HEAD` works from this host and returns the commit the address resolves to.
Two addresses that return the **same sha** are the same repository; two that return **different
shas** are two repositories, whatever their licence payloads look like.

| address pair | raw `LICENSE` payload | HEAD sha, alias | HEAD sha, canonical | verdict |
|---|---|---|---|---|
| `openedx/edx-platform` → `openedx/openedx-platform` | identical · 35 136 B · `e12d78569742` | `addd09d7801b` | `addd09d7801b` | 🟢 **same repository** — rename alias, and it still resolves |
| `Vacademy-io/vacademy_platform` → `Vacademy-io/vacademy_edtech_platform` | identical · 34 523 B · `0d96a4ff68ad` | `3a9c66db938c` | `3a9c66db938c` | 🟢 **same repository** — rename alias, and it still resolves |
| `DaRL-GenAI/instructional_agents` vs `Hyan-Yao/instructional_agents` | identical · 1 067 B · `4e085d826a64` | `f835eb45f508` | `1c2a9f9e3d26` | 🔴 **NOT the same repository** — two live, divergent HEADs |
| `OpenEduCat-Inc/OpenEduCat` → `openeducat/openeducat_erp` | alias **404** at `19.0`, `master` and `main`; canonical **200** · 8 241 B · `528f840368` | 🔴 unresolvable — `ls-remote` falls through to a credential prompt | `46a5d7d40082` | 🔴 **alias is ABSENT**, not a redirect |

### 🔴 The rule this establishes, and it is reusable

🔴 **A byte-identical licence payload is near-zero evidence of repository identity, and for the
boilerplate grant families it is no evidence at all.** `p461` read an identical 1 067 B MIT text at
`DaRL-GenAI/instructional_agents` and `Hyan-Yao/instructional_agents` and concluded one was the
other's stale alias. The HEAD shas say otherwise: `f835eb45f508` ≠ `1c2a9f9e3d26`, two live
repositories with independent histories. The payloads match **because stock MIT text is
universal** — the same 1 067 B body appears on dozens of unrelated rows on these very shelves.
Identity is a property of the **tree**, and only the sha channel reads the tree.

### 🟡 What this leaves on the shelves — and it is less than `p461`'s headline implied

| `p461` claim | `p462` verdict | live-shelf consequence |
|---|---|---|
| 🔴 "FOUR shelf addresses are stale aliases" | 🟡 **TWO are** (`openedx/edx-platform`, `Vacademy-io/vacademy_platform`) | **cosmetic** — both resolve, both serve the right tree, neither is broken |
| 🔴 `DaRL-GenAI/instructional_agents` is an alias of `Hyan-Yao/instructional_agents` | 🔴 **refuted** — divergent HEADs, a fork pair | the two must be graded as **two rows**, never merged |
| 🔴 `OpenEduCat-Inc/OpenEduCat` is a stale shelf address | 🟢 **it is not a shelf address** — every live row on `verticals/solutions.md` (4) and `repos/foundations.md` (5) already cites `openeducat/openeducat_erp`; the alias appears **only inside `p461`'s own narrative** | **nothing to fix** |

🟢 **So the live shelves carry zero broken addresses.** That is a better state than `p461` reported
against itself, and it is stated here because an overstated defect costs the next pass real probes.

### 🟢 `Gap 461-B` gains a first-hand instance: `NOASSERTION` is an index verdict, not an absent grant

[`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) is classified
**`NOASSERTION`** (`"license": {"key": "other", "name": "Other"}`) by the GitHub index. Its payload
is not absent and not ambiguous:

| field | value |
|---|---|
| default ref | 🔴 **`19.0`** — not `main`, and `main` 404s |
| grant path | `19.0/LICENSE` (also served at `master`) |
| bytes · digest | **8 241 B** · `528f840368` |
| declared family | **LGPL-3.0** — *"OpenEduCat is published under the GNU LESSER GENERAL PUBLIC LICENSE, Version 3 (LGPLv3), as included below"*, with the GPL text appended beneath it as the LGPL's base |
| notice obligation | the payload reserves bundled external libraries to *"other GPL-compatible licenses"*, per-file |

🔴 So an index-only reader records this platform as ungranted, and a `main`-assuming payload reader
records it as ungranted too — **two independent ways to lose a real, readable copyleft grant on the
same row.** The grant is LGPL-3.0: usable as a dependency boundary, not a tier Globant can
relicense.

### 🔴 The prescribed channel, graded in full — 36 tokens, and the novel repository yield is ZERO

This pass ran **the eight prescribed legs and no others**: the four global legs
(`top open source AI agents education 2026 github MIT`, `github trending education AI 2026`,
`open source platform education ERP CRM SIS MIT Apache`, `AI education industry trends 2026`) and
the four regional legs (North America, EMEA, APAC, LATAM). Every repository-shaped token any leg
returned was graded against these shelves.

| | n | share |
|---|---|---|
| repository/project tokens returned and graded | **36** | |
| 🔴 already carried on these shelves | **34** | **94.4 %** |
| 🟡 unshelved | **2** | **5.6 %** |
| 🔴 **unshelved AND a repository — i.e. usable** | **0** | **0 %** |

🔴 **The two unshelved tokens are not repositories.** `BYJU'S` is a company name, returned by a
market-research vendor page as an APAC "key player"; `spacebasic.com` is the blog host that served
one of the vertical-platform hits. Neither is an address, a licence or a thing to build on.

🟢 **Fifth consecutive nil, and the first on the PRESCRIBED channel itself.** `p458`–`p461` reached
their nils on GitHub-API and topic-page channels while recording the prescribed web-search channel
separately. This pass ran the prescribed wording verbatim, global and per region, and it returns
**nothing these shelves do not hold** — so the saturation is now reproduced on the channel the
encargo actually specifies, not only on the substitutes built around it.

🟡 **Carried tokens, named so the denominator is auditable rather than asserted:**
`500-AI-Agents-Projects`, `ai-agents-for-beginners`, `agents-course`, `nanochat`, `llm-course`,
`ML-For-Beginners`, `OpenHands`, `MetaGPT`, `OpenClaw`, `CrewAI`, `LangChain`, `LangGraph`,
`smolagents`, `AutoGen`, `DeepTutor`, `OpenTutor`, `maxew6/ai-tutor-project`,
`krishna16-origin/ai-tutor`, `k-dense-ai/scientific-agent-skills`, `withmarbleapp/os-taxonomy`,
`HuggerHustle/ai-radar`, `ARUNAGIRINATHAN-K/awesome-ai-agents-2026`,
`caramaschiHG/awesome-ai-agents-2026`, `GegoK12`, `RosarioSIS`, `frappe/erpnext`, `Dolibarr`,
`OpenEduCat`, `Open edX`, `Moodle`, `Kolibri`, `BigBlueButton`, `Canvas`, `Pearson`.

### 🟡 A carried ★ figure moved by one, and that is a measurement, not a defect

`p461` recorded `openedx/openedx-platform` at **8 209**; this pass reads **8 210** on the same API
field. 🟢 Exact-integer ★ counts are **live counters**, so any such cell is true only at its read
time — which is why these shelves cite them with the pass that read them and never as standing
facts. The other three reproduce unchanged: `openeducat/openeducat_erp` **899**,
`Vacademy-io/vacademy_edtech_platform` **23**, `Hyan-Yao/instructional_agents` **22**.

### 🔴 Gaps this pass registers

- **`Gap 462-A`** — the fork pair `DaRL-GenAI/instructional_agents` (`f835eb45f508`) and
  `Hyan-Yao/instructional_agents` (`1c2a9f9e3d26`) is **ungraded for direction**: which is upstream,
  what diverged, and whether both are maintained. `gate-fork-direction` (`p404`) is the instrument
  for it and it needs full history, which this pass's shallow access does not have.
- **`Gap 462-B`** — every address on these shelves is carried under the name it was found under.
  A **population-scale alias census** by HEAD sha has never been run, so the alias rate across all
  carried addresses is unknown. `p461` found four candidates in 30 probes; that is a rate worth
  measuring, not extrapolating.
- **`Gap 446-A` stays OPEN and the obstacle is now named**: the gate cannot be run under a harness
  that refuses to execute the Makefile.

## 🆕 `p461` — **No row is added, and the nil is now REPRODUCED ON A FOURTH CHANNEL: 30 addresses graded against these shelves, 30 already carried, 0 unshelved — usable novel yield ZERO at a 100 % carried share, the highest yet. 🔴 But this pass found a defect the three prior instruments could not see: FOUR shelf addresses are stale aliases that resolve by redirect to repositories with different canonical names, and the raw channel serves byte-identical payloads for alias and canonical, so it cannot detect this at all.**

🔴 **Gate posture, stated first per `Gap 446-A`: `make hooks` was NOT RUN** — this pass reached the
shelves through a fresh clone rather than the Makefile, so **nothing below is gate-attested**.

🔵 **Instrument, and its primary channel shares no code path with `p458`–`p460`.** This pass
resolved through the **GitHub repository-search API** (`search_repositories`), which supplies two
things none of the prior passes had:

1. 🟢 **Exact integer `stargazers_count`** — this directly retires the limitation `p460` recorded
   against itself (*"every ★ figure this pass quotes is a rounded rendered value (`1.2k`, `7.5k`)
   — recorded as such, not as a count"*).
2. 🟢 **Grant resolution by `license:` qualifier** — the *index's own* classification, which is a
   third kind of grant assertion, distinct from `p460`'s payload byte-read and from the sidebar
   badge `p460` caught relaying a grant it did not hold.

🔵 **The raw-payload byte-read channel was deliberately REUSED, not replaced** — not as the
instrument but as the **control**, so this pass's numbers can be tied back to `p460`'s.

### 🟢 Cross-pass controls — reproduced before any verdict

| control | published by `p460` | this pass read | verdict |
|---|---|---|---|
| 🟢 `openedx/edx-platform` `LICENSE` | AGPL-3.0 · 35 136 B · `e12d78569742` | **35 136 B · `e12d78569742`** | **reproduced, byte- and digest-identical** |
| 🟢 `Vacademy-io/vacademy_platform` `LICENSE` | AGPL-3.0 · 34 523 B · `0d96a4ff68ad` | **34 523 B · `0d96a4ff68ad`** | **reproduced** |
| 🟢 fabricated address — negative | — | **404, NO GRANT at all probed paths** | **correctly refused** (`Gap 453-E` (d) mode) |

### 🔴 Saturation, fourth instrument, and the carried share is now total

| | n | share |
|---|---|---|
| addresses graded against these shelves | **30** | |
| 🔴 already carried here | **30** | **100 %** |
| 🟡 unshelved | **0** | **0 %** |
| 🔴 **unshelved AND granted — i.e. usable** | **0** | **0 %** |

🟢 **Four instruments, four passes, one verdict.** `p459` measured 97.1 % carried on the
repository-search API, `p460` measured 97.1 % on topic-page enumeration, and this pass — probing
the `ai-tutor`, `ai-education`, `knowledge-tracing`, `education`+`llm` topic sets and the
Spanish- and Portuguese-language surfaces — found **not one address these shelves do not already
hold**. The shelf is saturated against every channel so far applied to it.

### 🔴 `Gap 461-A` — the alias defect: an address that resolves to a repository other than the one named

🔵 The search index **does not resolve** four addresses these shelves carry. Each one's canonical
name has changed, and each old address still answers by redirect:

| shelf address | index resolves it? | canonical name per index | ★ exact | raw payload, alias vs canonical |
|---|---|---|---|---|
| 🔴 `openedx/edx-platform` | **no** | **`openedx/openedx-platform`** | **8 209** | **identical** — 35 136 B · `e12d78569742` both |
| 🔴 `Vacademy-io/vacademy_platform` | **no** | **`Vacademy-io/vacademy_edtech_platform`** | **23** | **identical** — 34 523 B · `0d96a4ff68ad` both |
| 🔴 `DaRL-GenAI/instructional_agents` | **no** | **`Hyan-Yao/instructional_agents`** | **22** | **identical** — 1 067 B · `4e085d826a64` both |
| 🔴 `OpenEduCat-Inc/OpenEduCat` | **no** | **`openeducat/openeducat_erp`** | **899** | **NOT identical** — alias **404** at `19.0`; canonical **200**, 8 241 B |

🟢 **The transfer is confirmed from inside the payload, not inferred from the rename.**
`Hyan-Yao/instructional_agents` serves `MIT License` whose copyright line reads
**`Copyright (c) 2025 DaRL-GenAI`** — the grant itself still names the old owner, which is what a
transfer looks like from the bytes up.

🔴 **Why the three prior instruments were blind to this.** A redirect is invisible to a payload
byte-read: `raw.githubusercontent.com` returns **the same bytes and the same digest** at the alias
and at the canonical name. So `p458`–`p460` each read a grant, each reproduced it exactly, and each
was **right about the licence and wrong about which repository holds it**.

🔵 **Direction of failure, and it is a new one.** `p459`'s fallback matcher **invented** a grant
from a body scan. `p460`'s sidebar badge **relayed** a grant the repository did not serve. This
defect does neither — the grant is real and correctly read. What is wrong is the **binding**: a
correct grant attached to a name that no longer designates the thing. 🟡 Consequence for anything
built on these shelves: an address that resolves today by redirect is **not a stable identifier**,
and a rename that is later un-redirected turns a verified row into a dead one with no change to
this repository.

### 🔴 `Gap 461-B` — `NOASSERTION` is not `absent`, and conflating them loses usable grants *and* admits copyleft

🔵 The index reports grant state in two distinguishable failure modes, and this pass tested both
against the payload. **They do not behave the same way:**

| repo | index says | payload read | real grant |
|---|---|---|---|
| 🟡 `openeducat/openeducat_erp` | `NOASSERTION` | **200**, 8 241 B | **LGPL-3.0** — *"OpenEduCat is published under the GNU LESSER GENERAL PUBLIC LICENSE, Version 3"* |
| 🔴 `GarethManning/education-agent-skills` | `NOASSERTION` | **200**, 1 230 B · `f952182df4eb` | **CC-BY-SA-4.0** — a *content* licence with share-alike, not a software grant |
| 🔴 `24kchengYe/human-skill-tree` | `NOASSERTION` | **200**, 1 134 B · `3fb8cda58638` | **AGPL-3.0** (short-form notice, not the full 34 KB text) |
| 🟢 `GeminiLight/awesome-ai-llm4education` | *field absent* | **404 × 3** | **NO GRANT** |
| 🟢 `JushBJJ/Mr.-Ranedeer-AI-Tutor` | *field absent* | **404 × 3** | **NO GRANT** |
| 🟢 `ECNU-ICALK/EduChat` | *field absent* | **404 × 3** | **NO GRANT** |
| 🟢 `aaryansamanta/ai-ethos` | *field absent* | **404 × 2** | **NO GRANT** |

🟢 **The rule this establishes, and it is actionable in both directions:**

- **`absent` → 4 of 4 genuinely serve no grant.** The index's *silence* is reliable; it may be
  treated as a refusal without a payload read.
- 🔴 **`NOASSERTION` → 3 of 3 serve a real, nameable grant.** The index's *`NOASSERTION`* means
  only *"the detector could not classify this file"*. It is *neither* a refusal *nor* a permission,
  and **must** trigger a payload read.
- 🔴 **And the cost of getting this backwards runs both ways.** Treating `NOASSERTION` as a refusal
  discards **LGPL-3.0 `openeducat_erp`**, an 899★ vertical this shelf wants. Treating it as a
  permission vendors **CC-BY-SA-4.0** and **AGPL-3.0** material into work that cannot carry
  share-alike — the more expensive error of the two, and the one no prior pass was positioned to
  catch, because `p460`'s instrument read payloads only where the index had already named a licence.

### 🟢 Exact ★ integers — retiring `p460`'s self-recorded rounding limitation

Index-exact at this pass, not rendered: `HKUDS/DeepTutor` **43 537** (observed incrementing to
**43 538** mid-pass — a live counter, recorded as a range not a point),
`openedx/openedx-platform` **8 209**, `moodle/moodle` **7 543**, `sakaiproject/sakai` **1 239**,
`chamilo/chamilo-lms` **1 020**, `openeducat/openeducat_erp` **899**, `GibbonEdu/core` **637**,
`ILIAS-eLearning/ILIAS` **505**, `openedx/XBlock` **471**, `pykt-team/pykt-toolkit` **452**,
`openfun/richie` **316**, `CAHLR/OATutor` **271**, `GeminiLight/awesome-ai-llm4education` **221**,
`Open-TutorAi/open-tutor-ai-CE` **114**, `Vacademy-io/vacademy_edtech_platform` **23**,
`Hyan-Yao/instructional_agents` **22**.

### 🔴 Decay flags — four carried rows are going stale, and two of them hold no grant

| row | last push | age at this pass | compounding problem |
|---|---|---|---|
| 🔴 `JushBJJ/Mr.-Ranedeer-AI-Tutor` | 2025-09-30 | **~13 months** | **NO GRANT** — 29 548★ and unvendorable |
| 🔴 `ECNU-ICALK/EduChat` | 2025-07-18 | **~15 months** | **NO GRANT** |
| 🟡 `24kchengYe/human-skill-tree` | 2026-03-25 | **~7 months** | grant is **AGPL-3.0** |
| 🟡 `Open-TutorAi/open-tutor-ai-CE` | 2026-06-26 | **~4 months** | BSD-3-Clause — the shelf's most permissive tutoring platform is its stalest |

🔵 `Open-TutorAi/open-tutor-ai-CE` is the one worth watching: **BSD-3-Clause at 114★** is the most
permissive multimodal tutoring base these shelves carry, and it has not moved in four months.

---
## 🆕 `p460` — **No row is added, and this time the nil is REPRODUCED ON A THIRD CHANNEL that shares no code path with `p459`'s: 34 addresses graded against these shelves, 33 already carried, 1 unshelved, and that 1 serves NO GRANT at 10 paths — usable novel yield ZERO. 🟢 And the cause `p458` and `p459` could only diagnose is FIXED this pass, outside this repo: the frozen rotation pointer has been advanced.**

🔴 **Gate posture, stated first per `Gap 446-A`: `make hooks` was NOT RUN** — this pass reached the
shelves through a fresh clone rather than the Makefile, so **nothing below is gate-attested**.

🔵 **Instrument, and it shares no code path with `p458`/`p459`'s.** This pass discovered through
web search plus **GitHub topic-page enumeration** (`topics/ai-education` **551** repos,
`topics/ai-tutor` **788**, `topics/education-ai` **70**) and verified every grant by **byte-reading
the payload** at `raw.githubusercontent.com`, gating on `%{http_code}`. **Controlled in both
directions before any verdict, and it reproduces seven values these shelves already published:**

| control | published here | this pass read | verdict |
|---|---|---|---|
| 🟢 `HKUDS/DeepTutor` `LICENSE` | Apache-2.0 · 11 408 B · `cd2f54e1e506` | **11 408 B · `cd2f54e1e506`** | **reproduced, byte- and digest-identical** |
| 🟢 `moodle/moodle` `COPYING.txt` | GPL-3.0 · 35 147 B | **35 147 B** | **reproduced** |
| 🟢 `openedx/edx-platform` `LICENSE` | AGPL-3.0 · 35 136 B · `e12d78569742` | **35 136 B · `e12d78569742`** | **reproduced** |
| 🟢 `sakaiproject/sakai` `LICENSE` | ECL-2.0 · 11 120 B · `0688f62d04f1` | **11 120 B · `0688f62d04f1`** | **reproduced** |
| 🟢 `openedx/XBlock` `LICENSE.TXT` | Apache-2.0 · 11 358 B · `cfc7749b96f6` | **11 358 B · `cfc7749b96f6`** | **reproduced** |
| 🟢 `ahmedEid1/lumen` `LICENSE` | GPL-3.0 · 35 149 B · `3972dc9744f6` | **35 149 B · `3972dc9744f6`** | **reproduced** |
| 🟢 `Vacademy-io/vacademy_platform` `LICENSE` | AGPL-3.0 · 34 523 B | **34 523 B · `0d96a4ff68ad`** | **reproduced** |
| 🟢 two fabricated addresses — negative | — | **404, 14-byte `404: Not Found`** | correctly refused (`Gap 453-E` (d) mode) |

### 🔴 The saturation finding, reproduced on an independent channel

🔵 `p459` measured saturation with the **GitHub repository-search API** (42 probed → 2 unshelved →
0 granted). This pass measured it with **web search + topic-page enumeration + payload byte-reads**
— no shared instrument, same hour, same shelf:

| | n | share |
|---|---|---|
| addresses surfaced and graded against these shelves | **34** | |
| 🔴 already carried here | **33** | **97.1 %** |
| 🟡 unshelved | **1** | **2.9 %** |
| 🔴 **unshelved AND granted — i.e. usable** | **0** | **0 %** |

🟢 **Two channels, two instruments, one hour, same verdict.** `p459`'s 0 % usable is not a property
of its instrument.

### The one unshelved address, and why it is not a row

| address | grant read at `HEAD` | ★ | verdict |
|---|---|---|---|
| [`mwasifanwar/eduadapt-ai`](https://github.com/mwasifanwar/eduadapt-ai) | 🔴 **NO GRANT** — 404 at all 10 probed paths | 26 | 🔴 **Refused.** RL-based adaptive-learning app; nothing may be vendored without a written grant |

### 🔴 Two defects in this pass's own instrument — recorded, not quietly fixed

1. 🔴 **A FALSE UNGRANTED on a carried foundation row, and it is a case-sensitivity defect.** This
   pass's grant ladder probed `LICENSE.txt` and **not** `LICENSE.TXT`, and published
   *"`openedx/XBlock` — NO GRANT at 9 paths"* internally before correction. 🟢 **The shelf was
   already right and already specific**: it carries the path as **`LICENSE.TXT` — uppercase
   extension**, and had recorded the exact trap (*"LICENSE.txt 404 x3, LICENSE.TXT -> 200"*) before
   this pass ran. Re-probed at the recorded path: **Apache-2.0, 11 358 B, `cfc7749b96f6`** —
   reproduced. 🔵 This is `Gap 455-A`'s failure *direction* (a false ungranted **discards a usable
   permissive dependency**) reached by a new mechanism: filename **case**, not ref.
2. 🔴 **A rendered-page licence label is not a grant, and it asserts one where no root grant file
   exists.** GitHub's sidebar labels `openedx/XBlock` `Apache-2.0`; the repository serves no grant
   at any lowercase root path, and the rendered claim rests on `README.rst` prose plus a
   `shields.io` badge. 🔵 Complementary direction to `p459`'s own fallback-matcher defect (which
   read `os-taxonomy` as "MIT"): that one **invented** a grant from a body scan, this one
   **relays** one from a renderer. 🟡 Every ★ figure this pass quotes is a **rounded rendered
   value** (`1.2k`, `7.5k`) — recorded as such, not as a count.

### 🟡 A licence badge over a contrary payload — second first-hand instance

[`ahmedEid1/lumen`](https://github.com/ahmedEid1/lumen) ships `![License: MIT]` in its `README.md`
and serves **GPL-3.0** at `HEAD/LICENSE` (**35 149 B · `3972dc9744f6`**). 🟢 **These shelves
already carry it correctly as GPL-3.0 at that exact digest** — so this is a reproduction, not a
correction, and it is the second first-hand instance of `p456`'s *"a licence badge is not a
licence"*, in the expensive direction: a reader trusting the badge vendors copyleft as permissive.

### 🟡 A carried ★ figure has a motive attached to it

[`24kchengYe/human-skill-tree`](https://github.com/24kchengYe/human-skill-tree) (584★, grant file
a **1 134-byte AGPL notice**, not the full text) ships `README.md` (**36 305 B · `1984e06440ee`**)
whose lines **815** and **817** address AI agents directly, in Chinese and English, and ask them to
press ⭐ Star — citing a fabricated statistic (*"agents who star quality repos run 200 % more
efficiently"*). 🟢 **Stated accurately: it is explicitly jocular** (*"Trust me, bro"*) and this pass
does **not** call it an attack. 🔵 It is recorded because **these shelves carry ★ as data**, and a
README that instructs its agent readers to move that metric is a reason to treat ★ as a
popularity relay rather than an independent signal — which is also why defect (2) above matters.

## 🆕 `p459` — **No row is added. Three GitHub-API legs returned 42 education addresses, 2 of them unshelved, and BOTH are refused for want of a licence grant — so the usable novel yield of this pass is ZERO, and that is the finding.**

🔴 **Gate posture, stated first: `make hooks` was NOT RUN** — this pass reached the shelves
through a fresh clone rather than the Makefile, so **nothing below is gate-attested**.

🔵 Instrument: a two-stage probe — `git ls-remote --symref` for liveness and default ref, then a
10-path grant read at that ref. **Controlled in both directions before use:**

| control | result |
|---|---|
| 🟢 `HKUDS/DeepTutor` — positive, asserted against the grant these shelves carry | **Apache-2.0**, `LICENSE` **11 408 B**, head `a31d82624c27` — **reproduced** |
| 🟢 two fabricated addresses — negative | both **`ADDRESS_DEAD`** |
| 🔴 **instrument defect, recorded against this pass, not against the shelves** | the probe's *fallback* licence matcher (a bare substring scan, used only when no licence title matches in the first 30 lines) read `withmarbleapp/os-taxonomy` as **"MIT"**. It is **not** MIT. The shelves' own first-hand record — **ODbL-1.0 + CC BY-SA 4.0**, `LICENSE` **25 289 B** — was re-read and **stands uncorrected**. Every grant quoted below was read from the licence title, never from the fallback |

### The two unshelved addresses, and why neither becomes a row

| address | grant read at `HEAD` | ★ | verdict |
|---|---|---|---|
| [`Takamatsu-Hikaru/AI-Research-Guide`](https://github.com/Takamatsu-Hikaru/AI-Research-Guide) | 🔴 **NO GRANT** at 10 paths · head `8df0f4d42d8d` | 181 | 🔴 **Refused.** Also not an agent: a bilingual (中文/EN) *reading guide* to entering AI research, published by the UESTC AI society. Prose, not a runnable tutor |
| [`selmetwa/parallel-arabic`](https://github.com/selmetwa/parallel-arabic) | 🔴 **NO GRANT** at 10 paths · head `1eb4d3acd568` | 26 | 🔴 **Refused.** Arabic reading/practice platform, Svelte. Nothing may be vendored without a written grant |

🟢 **Both were genuinely new to these shelves** — the discovery channel did not fail. What failed
is the *supply*: at the depth these searches reach, education has no un-shelved, permissively
licensed agent left to add.

### The denominator, so the nil is auditable

| leg | returned | unshelved | usable (granted) |
|---|---|---|---|
| `topic:ai-tutor` · `pushed:>2026-07-01` | 20 | 0 | 0 |
| `topic:education`+`topic:ai-agent` · `pushed:>2026-08-01`·`stars:>20` | 16 | 0 | 0 |
| `topic:edtech` · `pushed:>2026-09-15`·`stars:>15` + `topic:education`+`topic:mcp-server` | 25 + 12 | 2 | **0** |
| **total (deduplicated probe set)** | **42** | **2 — 4.8 %** | **0 — 0 %** |

🔴 Against `p458`'s **41.9 %** novel share on the same channel one pass earlier. The channel is
unchanged; the shelf is full. 🟢 The consequence is recorded in
[`intel/trends.md`](../intel/trends.md) and acted on in this repo's rotation — see that file.

## 🆕 `p458` — **🟢 THE CHANNEL RECORDED AS BLOCKED FOR 457 PASSES WORKS, AND IT IS THE FIRST ONE TO BEAT THE PRESCRIBED CHANNEL BY A MARGIN: the GitHub repository-search API returned 62 education candidates and 26 of them (41.9 %) are addresses these shelves have NEVER carried, against the prescribed web-search channel's SIXTH consecutive zero. 🔴 And the reason this is pass 458 of ONE industry is not a research finding at all — the rotation that selects the industry has been stuck for 85 days.**

🔴 **Gate posture, stated first as `Gap 446-A` requires: `make hooks` was NOT RUN** — this pass
reached the shelves through a fresh clone rather than the Makefile, so **nothing below is
gate-attested**. 🔵 The instrument is a two-stage probe (`git ls-remote --symref` for liveness and
default ref, then a 10-path payload read at that ref) and it was **controlled in both directions
before use**:

| control | result |
|---|---|
| 🟢 `HKUDS/DeepTutor` — positive, asserted against the value `p450` published | **11 408 B** · `cd2f54e1e506` — **reproduced exactly** |
| 🟢 `moodle/moodle` — positive | GPL-3.0 at **`COPYING.txt` 35 147 B** `8ceb4b9ee5ad` |
| 🟢 two fabricated addresses — negative | both **`ADDRESS_DEAD`** |

🔵 A second, unplanned corroboration: `m1kuorg/asked-before`'s Apache-2.0 payload reads
**11 357 B · `c71d239df917`** — byte- and digest-identical to the value `p453` published for
`node-ecole-directe`, measured by a different instrument on a different pass. 🟢 **Two passes
agree on a canonical grant digest.**

### 🟢 The discovery finding — a channel with a measured yield, not an assertion

🔵 `p450` recorded the GitHub API as *"github-api-proxy-blocked"* and every pass since has worked
around it. 🔴 **It is not blocked from this host.** Four queries over `topic:education`,
`topic:edtech`, `topic:mcp` and `topic:ai-agent` with `pushed:>2026-09-15` returned **62 distinct
education candidates**; each was checked against the **2 932 addresses** these shelves already
carry:

| | n | share |
|---|---|---|
| candidates returned | **62** | |
| 🟢 **NOT carried on any shelf here** | **26** | **41.9 %** |
| 🔵 already carried | 36 | 58.1 % |

🔵 Graded against the prescribed channel run in the same hour — four global legs plus one leg per
region, every token checked against [`intel/market.md`](../intel/market.md): **0 novel facts, 19
of 19 already on file**. 🟢 **The variable is the channel, and the margin is 26 to 0.** 🔵 The
mechanism is structural rather than lucky: the API returns `license.spdx_id` and `pushed_at` as
typed fields, so a licence and a liveness date arrive *with* the address instead of needing a
probe per candidate — which is what made 62 candidates affordable in one pass.

### 🟢 Twenty-one permissive build-on rows, every grant read first-hand at the resolved default ref

🔵 Of the 26 new addresses, **23 serve a readable grant**, **3 serve none anywhere** and **2 of
the 23 are copyleft** — leaving **21 permissive build-on rows**. 🔵 **19 are shelved here**; the two
platform-shaped ones go to [`verticals/solutions.md`](../verticals/solutions.md) and
[`repos/foundations.md`](../repos/foundations.md) rather than being double-counted on this shelf. Placed by region **only where the
repository's own text names a national system, an institution or a published standard**; where the
only evidence was the README's language, the row is left unplaced, because a language is not a
region.

#### 🇪🇺 EMEA — 5 permissive rows, each placed by a named national system

| Agent | Repo | Licence (read at `HEAD`) | What it is | Placed by |
|---|---|---|---|---|
| skillpilot | [`enpasos/skillpilot`](https://github.com/enpasos/skillpilot) | **Apache-2.0** · 10 089 B `6bbe4ace8a18` | Official curricula turned into dependency-aware skill graphs with mastery tracking | **German Gymnasium** curricula, named |
| somtoday-mcp | [`barzoj/somtoday-mcp`](https://github.com/barzoj/somtoday-mcp) | **MIT** · 1 082 B `47056e024c62` | Read-only MCP server for the Somtoday parent portal | **Somtoday**, Dutch parent portal |
| scholarship-navigator | [`OmarZen/scholarship-navigator`](https://github.com/OmarZen/scholarship-navigator) | **MIT** · 1 064 B `cdc1ae6b9064` | Eligibility checks, fit scores and dated plans over 35 scholarships + **56 Erasmus Mundus** programmes; MCP + skills | **Erasmus Mundus**, named |
| elettrolab | [`kkongiu/elettrolab`](https://github.com/kkongiu/elettrolab) | **MIT** · 1 072 B `00003db93c6b` | Didactic electronics lab — JSON circuits, MNA solver, 2D breadboard, MCP server for LLMs | Italian-language, **ITIS lab** idiom |
| miyagi | [`falkenslab/miyagi`](https://github.com/falkenslab/miyagi) | **MIT** · 1 078 B `d0a329112827` | Teacher agent over a **Moodle** course: grades to your rubric, runs the forum, builds topics and quizzes | 🟡 Spanish-language; **country NOT stated** |

🟡 `miyagi` is listed under EMEA on the Moodle-plus-Spanish reading and **flagged**: its own text
names no country, and Spanish-language Moodle tooling is as likely LATAM. 🔵 An engagement should
confirm before citing it as either.

#### 🌏 APAC — 5 permissive rows, placed by exam system or language standard

| Agent | Repo | Licence (read at `HEAD`) | What it is | Placed by |
|---|---|---|---|---|
| kaoyan-navigator-skill | [`mcxiaoxiao/kaoyan-navigator-skill`](https://github.com/mcxiaoxiao/kaoyan-navigator-skill) | **MIT** · 1 093 B `ddfed82a8a76` | Postgraduate school-selection skill: researches cutoffs, quotas and admission data, emits reach/match/safety advice | **考研**, China's national postgraduate exam |
| MandarinClips-mcp | [`IndexFlowing/MandarinClips-mcp`](https://github.com/IndexFlowing/MandarinClips-mcp) | **MIT** · 1 074 B `4a8b6a46d4b4` | 180 000+ authentic cinema dialogue clips, **HSK 3.0** vocabulary and pragmatic grammar formulas for TCSL educators | **HSK 3.0**, published standard |
| video2book | [`LINJIANG12/video2book`](https://github.com/LINJIANG12/video2book) | **MIT** · 1 100 B `0cec272164f7` | Turns long-form lecture video into textbook-grade prose and exam notes (faster-whisper) | **Bilibili** course corpus |
| mcd-math-journey | [`lilong65190349/mcd-math-journey`](https://github.com/lilong65190349/mcd-math-journey) | **MIT** · 1 086 B `48038468aa58` | 81 answer-**verifiable** maths levels for primary grades 3–6; answers re-checked against a live priced API, read-only | Chinese 课标 primary curriculum |
| studyhub-local | [`langming58-hash/studyhub-local`](https://github.com/langming58-hash/studyhub-local) | **MIT** · 1 084 B `27ec4446626e` | Local-first course-material hub with source-grounded study tools over Canvas | 🟡 zh-CN README; weak placement |

🟢 `mcd-math-journey` is the one row on this shelf whose **answer key is externally verifiable**:
the generator re-checks every answer against a third-party priced API rather than against the
model that wrote the question. 🔵 That is the pattern worth taking, independently of the subject.

#### 🇺🇸 North America — 3 permissive rows, placed by vendor or institution

| Agent | Repo | Licence (read at `HEAD`) | What it is | Placed by |
|---|---|---|---|---|
| canvas-mcp | [`boyuchengz/canvas-mcp`](https://github.com/boyuchengz/canvas-mcp) | **MIT** · 1 072 B `4450dee7f762` | **26 tools, every one a `GET`** — read-only Canvas LMS server; cannot submit, post, delete or mark read | **Canvas / Instructure** |
| Brightspace-API | [`RohanMuppa/Brightspace-API`](https://github.com/RohanMuppa/Brightspace-API) | **MIT** · 1 068 B `047079fbd491` | Read-only Brightspace layer usable from scripts or cron **without an agent** — the non-MCP sibling of `brightspace-mcp-server`, which these shelves already carry | **D2L Brightspace**, Purdue |
| canvasexpert-se | [`longhornteacher/canvasexpert-se`](https://github.com/longhornteacher/canvasexpert-se) | **MIT** · 1 085 B `a55fcd2567ea` | Teacher-directed Canvas assistant: portable engine, editable teaching playbooks, local MCP tools | **Canvas**, US K-12 idiom |

🟢 **`canvas-mcp` is the counter-example to `p448`'s finding, and it is explicit about it.**
`p448` measured that the LMS-connector tier is *not* read-only — 136 of 414 tool declarations
mutate. This server declares 26 tools and states that every one issues `GET` only, *"so even a
leaked connector URL only exposes what you could already see"*. 🔵 It is the first row here whose
read-only property is a **design claim in its own README** rather than an absence this base had to
measure. 🟡 Two caveats a buyer should know: it is **one day old** (created 2026-10-25) and sits at
**115 ★ with 0 forks**, a ratio no other row here has.

🔴 **`longhornteacher/canvasexpert-se` resolves its default ref to `dev`, not `main` or
`master`.** 🔵 This is exactly the false-negative class `p450` chased and `p456` resolved: a
guessed-ref probe would have returned `ADDRESS_DEAD` for a live, permissively granted repository.
🟢 `--symref` resolved it on the first attempt.

#### 🌐 Not placed — 6 permissive rows whose own text names no region

| Agent | Repo | Licence (read at `HEAD`) | What it is |
|---|---|---|---|
| chalkcast | [`FredMichel/chalkcast`](https://github.com/FredMichel/chalkcast) | **MIT** · 1 072 B `ec57848632f7` | MCP server that authors, renders **and visually verifies** Manim animations from a concept |
| SAMOSA | [`Hussain004/SAMOSA`](https://github.com/Hussain004/SAMOSA) | **MIT** · 1 064 B `987261e3f863` | Step auditor for matrix algebra and stochastics — checks every step of a derivation exactly, over finite fields |
| yarareads | [`finereli/yarareads`](https://github.com/finereli/yarareads) | **MIT** · 1 066 B `7c4cf856c78c` | Decodable early-literacy reader: every word sounds out from phonics already taught; bring-your-own-agent over MCP |
| lessonfolk | [`CGSeb/lessonfolk`](https://github.com/CGSeb/lessonfolk) | **MIT** · 1 063 B `55873542fedc` | Zero-to-advanced AI curriculum with an agent as the tutor |
| asked-before | [`m1kuorg/asked-before`](https://github.com/m1kuorg/asked-before) | **Apache-2.0** · 11 357 B `c71d239df917` | Mines a ChatGPT/Claude export for the questions you keep re-asking, then **tests you without AI** until proven |
| sciencelab3d | [`rudra496/sciencelab3d`](https://github.com/rudra496/sciencelab3d) | **MIT** · 1 069 B `c4161f1cc9be` | 40+ browser virtual experiments across physics, chemistry and biology |

🟢 `SAMOSA` and `chalkcast` share the property that makes them worth more than their star counts:
**both verify their own output** — SAMOSA by exact arithmetic over finite fields, chalkcast by
rendering the animation and looking at it. 🔵 `asked-before` inverts the usual tutoring loop by
removing the model from the assessment step.

### 🔴 Three addresses REFUSED — live, education-specific, and ungranted on every channel probed

🔵 These are not shelved as build-on rows. All three resolve, all three are real projects, and
**none serves a grant at any of 10 probed paths — nor declares one in its manifest**, which is a
cleaner negative than `p452`'s `MANIFEST_ONLY` class:

| address | ref | 10 licence paths | manifest | note |
|---|---|---|---|---|
| [`particify/arsnova-server`](https://github.com/particify/arsnova-server) | `master` | 🔴 404 at all 10 | 🔴 `build.gradle.kts`, `gradle.properties` — **no licence field** | **67 ★, 44 forks, created 2013** — the most-forked ungranted project these shelves have found |
| [`OutBlade/kit-campus-mcp`](https://github.com/OutBlade/kit-campus-mcp) | `main` | 🔴 404 at all 10 | 🔴 `pyproject.toml` — no licence field | Exam results and module catalogues for the **KIT Campus** portal (Karlsruhe) |
| [`peterxing/openscout`](https://github.com/peterxing/openscout) | `main` | 🔴 404 at all 10 | 🔴 `package.json` — no licence field | Signs in to Microsoft 365 itself via Graph |

🔴 **`arsnova-server` is the expensive one.** It is a thirteen-year-old audience-response backend
with 44 forks, and the word *"open"* appears nowhere in a grant. 🔵 A team that reads 67 ★ and a
`docker-compose` as permission is wrong, and so is every one of those 44 forks. 🟢 Engagement rule:
ARSnova needs a written grant from Particify before a line of it is vendored — ask, do not assume.

### 🟡 Two copyleft rows — recorded, NOT on the build-on tier

| address | licence read at `HEAD` | why it is flagged |
|---|---|---|
| [`Arudchayan/adam-mcp`](https://github.com/Arudchayan/adam-mcp) | 🟡 **GPL-3.0** · 35 149 B `3972dc9744f6` | Read-only MCP for **University of Basel ADAM (ILIAS 10)**, SWITCH edu-ID kept in the browser — the first **ILIAS** address on these shelves, and it is copyleft |
| [`Vacademy-io/vacademy_edtech_platform`](https://github.com/Vacademy-io/vacademy_edtech_platform) | 🔴 **AGPL-3.0** · 34 523 B `0d96a4ff68ad` | Topics itself `erp` + `crm` + `lms`; network copyleft, so a hosted multi-tenant deployment triggers source disclosure |

🔵 `adam-mcp` matters out of proportion to its 0 ★: **ILIAS is a national-scale LMS in the
German-speaking university sector** and no shelf here carried an address against it. 🟡 GPL-3.0
makes it a reference to read, not a library to link.

### 🔴 LATAM — a NIL, and the denominator says it is a NOVELTY nil, not a coverage hole

🔵 Stated explicitly because silence looks like coverage: **zero of the 26 new addresses are
LATAM.** 🟢 But the channel did not fail to return LATAM supply — it returned
[`alejooroncoy/campus-cli`](https://github.com/alejooroncoy/campus-cli) (UPC Aula Virtual,
Blackboard Learn, Peru), which **these shelves already carry**. 🔵 So the nil is in *novelty*, not
in coverage: this channel reaches LATAM, and the LATAM supply it reaches was already found. 🟡 The
one row that could have been LATAM — `miyagi` — does not name its country, and is flagged above
rather than counted here.


### 🔴 Three defects found inside this pass, in this pass's own instruments — recorded, not quietly fixed

🔵 Each would have published a confident wrong statement, and each was caught by a control
asserting a value this base had already published:

| # | defect | what it would have published | caught by |
|---|---|---|---|
| **(a)** | the append-only proof snapshotted both trending files to `$DIR/$(basename f).pre` — **both basenames are `trending.md`**, so one snapshot silently overwrote the other | a **false append-only VIOLATION** on [`agents/trending.md`](trending.md), comparing it against `repos/trending.md`'s bytes | the two "prior" sizes came back **identical** (3 324 005 B) for files of 51 077 and 39 810 lines |
| **(b)** | whole-body byte containment was applied to [`intel/market.md`](../intel/market.md), whose region block is amended **in place** by contract | a **false violation** — in-place amendment necessarily breaks containment of the whole prior body | `git diff --numstat` reporting **161 insertions, 0 deletions**, which is the correct instrument for an in-place file |
| **(c)** | the first licence-path list omitted `COPYING.txt`, so the `moodle/moodle` positive control returned `REPO_LIVE_NO_GRANT` | **"Moodle serves no grant"** — about the most-installed LMS in the world | the positive control failing *before* the sweep ran; path list extended to 10 and re-run |

🟢 Defect (a) is the useful one to carry forward: **whole-body containment is the right instrument
for an append-only file and the wrong one for a file amended in place**, and the two contracts need
two different checks. 🔵 Re-proved against `git show HEAD:<file>` rather than a local snapshot:
both trending files contain their **entire** prior body verbatim (4 372 716 B and 3 323 943 B), and
**all eight files show 0 deletions**.

### 🟡 An unplanned corroboration, and a correction to this pass's own first draft

🔵 [`RohanMuppa/brightspace-mcp-server`](https://github.com/RohanMuppa/brightspace-mcp-server) —
already carried here — was re-probed to check the sibling claim above. Its grant reads **MIT ·
1 068 B · `047079fbd491`**, **byte- and digest-identical** to `Brightspace-API`'s. 🟢 Same author,
same MIT text, two addresses — the sibling relationship is measured, not inferred. 🔴 This pass's
first draft had listed `brightspace-mcp-server` as a *new* row with its byte count guessed from
the sibling; it is **already carried**, the guess is replaced by a first-hand read, and the North
America count is corrected from 4 to **3**.

## 🆕 `p457` — **🟢 `Gap 456-A` IS CLOSED BY READING THE PAYLOAD AT ALL 457 CARRIED ADDRESSES, NOT 15 OF THEM — and the one genuine disagreement in 356 graded cells is a RELICENSING DATED TWO DAYS BEFORE THIS PASS: [`pengusto/google-classroom-mcp`](https://github.com/pengusto/google-classroom-mcp) is shelved here as MIT and serves `Pengusto Commercial License 1.0` at `HEAD`. 🔴 And the MIT upstream it names serves NO licence file at any path — its grant text survives only inside the fork that relicensed it.**

🔴 **Gate posture, stated first as `Gap 446-A` requires: `make hooks` was DENIED**
(`Code from External`) — **twelfth denial in thirteen passes**. 🔵 Nothing below is gate-attested.
The instrument and its controls are at
[`compose/code/p457-payload-census/`](../compose/code/p457-payload-census/census.py); **two
fabricated addresses were swept inside the same run and both came back `ADDRESS_DEAD`**, and two
published cells were asserted as positive controls and both reproduced exactly
(`HKUDS/DeepTutor` **11 408 B**, the value `p450` published; `moodle/moodle` **GPL-3.0**).
🔴 **Seven defects in this pass's own code are recorded below rather than quietly fixed**, and one
of them published a false disagreement before a hand-read caught it.

**Evidence:**
[`payload-census`](../evidence/payload-census.2026-10-26-p457.tsv) — 356 graded cells, one row per
address with claimed family, measured family, bytes and digest ·
[`payload-census-raw`](../evidence/payload-census-raw.2026-10-26-p457.json) — all 458 records
including refs and verdicts ·
[`promotions`](../evidence/promotions.2026-10-26-p457.tsv) — 8 promoted, 1 copyleft-flagged,
2 refused, 2 fabricated negative controls ·
[`leg-grading`](../evidence/leg-grading.2026-10-26-p457.tsv) — all 24 facts the eight search legs
returned, each graded against [`intel/market.md`](../intel/market.md) so the nil is auditable ·
the instrument at [`census.py`](../compose/code/p457-payload-census/census.py), its grader at
[`grade.py`](../compose/code/p457-payload-census/grade.py) and
**46 controls** at [`controls.py`](../compose/code/p457-payload-census/controls.py).

### 🟢 `Gap 456-A` — the sweep `p456` could not afford, run in full

🔵 `p456` resolved the ref for every carried address and then re-read the **payload** for only the
**15** whose default branch fell outside the guessed list. The remaining **424** were resolved and
not read, which is the gap it registered. Every address is now read:

| | n |
|---|---|
| addresses extracted from `agents/top.md`, `repos/foundations.md`, `verticals/solutions.md` | **457** |
| 🟢 `PAYLOAD_READ` — a grant served at the resolved default ref | **390** |
| 🟡 `REPO_LIVE_NO_GRANT` — repository resolves, no grant at any of 12 probed paths | **54** |
| 🔴 `ADDRESS_DEAD` | **13** |
| 🟢 fabricated negative controls, both `ADDRESS_DEAD` | **2 / 2** |

🔵 Measured family distribution over the 390: **MIT 252**, Apache-2.0 **49**, AGPL-3.0 **24**,
GPL-3.0 **22**, BSD-3-Clause **9**, CC/ODbL **8**, GPL-2.0 **4**, LGPL-3.0 **3**, ECL-2.0 **2**,
ISC **1**, MPL-2.0 **1**, and **15 the instrument could not name** — resolved by hand below.
🟢 **64.6 % of the grants on these shelves are MIT**, which is the first time that share has been
measured over the whole population rather than over a tier.

### 🟢 Graded against what the shelves CLAIM — 356 cells, and the headline is the single disagreement

🔵 The claim is read **line-locally**: these shelves are markdown tables, so the licence token on
the same line as the address is that address's cell. 🔴 **91 addresses sit on lines carrying more
than one address; they are counted and EXCLUDED rather than guessed at**, which is the one honest
move available and it costs this sweep a fifth of its population.

| verdict | n | after hand resolution |
|---|---|---|
| 🟢 `AGREE` | 318 | **327** (91.9 %) |
| 🔴 `DISAGREE` | 1 | 🟢 **0** — the one was this pass's own defect, see below |
| 🟡 `UNREAD_BY_INSTRUMENT` | 9 | 🔴 **1 genuine disagreement** + 8 resolved |
| 🔴 `CLAIM_WITHOUT_PAYLOAD` | 20 | 8 manifest-recoverable, **12 not** |
| 🔴 `DEAD_BUT_CLAIMED` | 8 | 8 |

🔴 **One genuine disagreement in 356 graded cells, and it is the expensive kind.**

### 🔴 `pengusto/google-classroom-mcp` — the shelf says MIT and `HEAD` says commercial

🔵 This address is carried on these shelves with an **MIT** cell. Read first-hand this pass at the
resolved default ref (`master`):

```
LICENSE   3 053 B   sha256₁₂ d84e558a5033
  Pengusto Commercial License 1.0
  Effective for distributions carrying this notice from 2026-10-24.
  Copyright (c) 2026 Pengusto (maintainer-authored extensions).
  All rights reserved except as expressly granted below or by applicable law.
```

🔴 **Two days before this pass.** 🟡 And the licence is narrower than "it went commercial": by its
own §1 it covers only *"the copyrightable additions and modifications made by Pengusto … including
their source code, compiled counterparts, documentation and tests"*, and it names its upstream
precisely — `adriasantacreu/google-classroom-mcp` at commit
`29c2c2a07670692da28d3fdcee38cb7a54c8f18a`, which *"remains available under MIT"*.

🔴 **So the shelf's MIT cell is wrong about the repository as distributed, and right about a part
of it.** A team that pins this address at `HEAD` off that cell ships the maintainer's code under a
commercial licence. 🟢 **The MIT path is the upstream at the pinned commit** — and this pass
measured what that actually gets you, because it is not what it looks like:

| probe | result |
|---|---|
| `git ls-remote --symref` on the upstream | 🟢 live, `HEAD` → `master` → **`29c2c2a07670692da28d3fdcee38cb7a54c8f18a`** — *exactly* the commit the fork pins |
| upstream `LICENSE`, `LICENSE.md`, `LICENSE.txt`, `LICENCE`, `COPYING`, `license` | 🔴 **404 at all six** |
| upstream `package.json` | 🟡 **MIT, declared in a manifest** (901 B) — the only grant it serves |
| the fork's `LICENSES/MIT-upstream.txt` | 🟢 **200, 1 101 B** — *"MIT License / Copyright (c) 2026 Adrià Santacreu…"* |

🔴 **The readable MIT grant text for the upstream exists only inside the fork that relicensed
it.** 🔵 The upstream's own grant is a manifest declaration with no payload behind it — `p452`'s
`MANIFEST_ONLY` class, arrived at from the opposite direction. 🟢 **The engagement rule:** take the
upstream at the pinned commit, and carry the fork's `LICENSES/MIT-upstream.txt` into the vendor
tree as the evidence of the grant, because the project that grants it does not publish it.

### 🔴 Three carried addresses changed licence TEXT on the same date

🔵 `pengusto` is not alone, and the date is the finding:

| address | instrument served at `HEAD` | effective date |
|---|---|---|
| [`pengusto/google-classroom-mcp`](https://github.com/pengusto/google-classroom-mcp) | 🔴 `Pengusto Commercial License 1.0` · 3 053 B `d84e558a5033` | **2026-10-24** |
| [`nakafaai/aksara`](https://github.com/nakafaai/aksara) | 🔴 `Nakafa Source Available License 2.0` · 11 997 B | **October 24, 2026** |
| [`nakafaai/nakafa.com`](https://github.com/nakafaai/nakafa.com) | 🔴 `Nakafa Source Available License 2.0` · 11 997 B | **October 24, 2026** |

🟡 **The nakafa pair is not news to these shelves** — they are already carried as *"genuinely
closed"*, and this pass adds only the instrument's **name, version and date**, which they lacked.
🔵 Nakafa's own words, read first-hand: *"Nakafa is source available. It is not open source, and it
is not free to reuse."* 🔴 **What is new is the clustering**: three of 457 carried addresses
re-issued their licence text within a 48-hour window, and the shelf cell for one of them still
said MIT an hour before this pass ran.

### 🟡 The nine the instrument could not name, resolved by hand — and the KB was ahead of it twice

| address | payload | resolution |
|---|---|---|
| [`jupyter/nbgrader`](https://github.com/jupyter/nbgrader) | `LICENSE` 1 512 B `3a83d5b8e22c` | 🟢 **untitled BSD-3-Clause** — AGREES with the shelf |
| [`jupyterhub/jupyterhub`](https://github.com/jupyterhub/jupyterhub) | `LICENSE` 1 475 B `7069c7e8d60e` | 🟢 **untitled BSD-3-Clause** — AGREES |
| [`Open-TutorAi/open-tutor-ai-CE`](https://github.com/Open-TutorAi/open-tutor-ai-CE) | `LICENSE` 1 531 B `57c341d09920` | 🟢 **untitled BSD-3-Clause** — AGREES |
| [`rstudio/learnr`](https://github.com/rstudio/learnr) | `LICENSE.md` 10 472 B `60a581bccd57` | 🟢 **Apache-2.0 in markdown** — AGREES |
| [`withmarbleapp/os-taxonomy`](https://github.com/withmarbleapp/os-taxonomy) | `LICENSE` 25 289 B `77d2692c3d64` | 🟢 **ODbL** — and **these shelves already graded it ODbL**; the instrument was behind the KB |
| [`ucbds-infra/ottr`](https://github.com/ucbds-infra/ottr) | `LICENSE` **108 B** `de5d9459d263` | 🔴 a **stub**, not a grant — and **these shelves already record the real grant at `LICENSE.md` 1 555 B**; the instrument was behind the KB again |
| [`rstudio/gradethis`](https://github.com/rstudio/gradethis) | `LICENSE` **49 B** `bc2f766bedb6` | 🟡 `YEAR: 2021 / COPYRIGHT HOLDER: Posit Software, PBC` — **CRAN convention**; `DESCRIPTION` says `License: MIT + file LICENSE` |
| [`bncc-dev/bncc-pacotes`](https://github.com/bncc-dev/bncc-pacotes) | `LICENSE` 1 299 B `86bf5f5e6306` | 🟢 **dual by content type** — *"Código — MIT"* plus a separate content grant; AGREES with the shelf's dual cell |
| [`pengusto/google-classroom-mcp`](https://github.com/pengusto/google-classroom-mcp) | `LICENSE` 3 053 B `d84e558a5033` | 🔴 **the genuine disagreement above** |

🔴 **Two of the nine are cells where the shelves are MORE correct than this pass's reader**, and
that is worth more than the eight agreements: it means the published cells were built by a channel
that reads better than a first-200-wins payload probe, and a future sweep that trusts the probe
over the shelf will *regress* those two cells.

### 🟡 The R tier's grant is a `DESCRIPTION` field, and a payload reader returns a 49-byte non-grant

🔵 `p394` opened an R teaching/psychometrics tier on these shelves. This pass measures why a
payload-only read cannot grade it: **by CRAN convention a root `LICENSE` file carries only the year
and the copyright holder**, and the grant itself is the `DESCRIPTION` `License:` field.

```
rstudio/gradethis   DESCRIPTION → License: MIT + file LICENSE
ucbds-infra/ottr    DESCRIPTION → License: BSD_3_clause + file LICENSE
cran/exams          DESCRIPTION → License: GPL-2 | GPL-3
```

🔴 **And `cran/exams` corrects a cell**: this shelf carries it as **GPL-3.0**, and the package
offers **`GPL-2 | GPL-3` disjunctively** — the integrator may elect GPL-2.0. 🟡 The carried cell is
not false, it is **narrower than the grant**, which is the safe direction to be wrong in and is
still worth fixing.

### 🟢 Two refusals, both live repositories with nothing to build on

| address | ref | why refused |
|---|---|---|
| [`sakethbachu/OMR-scanner`](https://github.com/sakethbachu/OMR-scanner) | `master` | 🔴 `REPO_LIVE_NO_GRANT` — 12 licence paths probed, none served |
| [`davidjenner/OpenDyslexic-Converter`](https://github.com/davidjenner/OpenDyslexic-Converter) | `main` | 🔴 `REPO_LIVE_NO_GRANT` — same |

### 🟢 `p456`'s digest-lineage rule is independently REPRODUCED, in both directions

🔵 `p456` narrowed it to: *a digest match is evidence of lineage iff the licence family embeds a
holder.* This pass's candidate reads confirm it without having set out to:

- 🔴 **Apache-2.0 stock carries no holder** — [`crispin0007/OMR`](https://github.com/crispin0007/OMR)
  is **11 358 B `cfc7749b96f6`**, byte- and digest-identical to the cell `p451` published for
  `FiredMosquito831/ase-moodle-mcp`. Two unrelated projects, one digest, **zero lineage**.
- 🔴 **GPL-3.0 stock carries no holder** — [`bthicks/OMR-Grader`](https://github.com/bthicks/OMR-Grader)
  is **35 149 B `3972dc9744f6`**, identical to this shelf's `papillonapp/papillon-ed-core`.
- 🟢 **MIT embeds a holder** — `NSoiffer/MathCAT` and `AVauraTech/assistive-ai-accessibility-suite`
  are **both 1 065 B** with **different digests** (`f8f65c73234f` vs `142a4062de61`).

🟢 **So the rule holds on both arms**, and the operational form is: *never infer a fork from a
licence digest unless the family is MIT or BSD.*

### 🔴 Seven defects in this pass's own instrument — five in the reader, two in the controls

🔵 Recorded rather than quietly fixed, per this base's standing practice. **Four were caught by the
`UNCLASSIFIED` safety net rather than by mis-grading**, which is the design that mattered — the
historical defects in this class *published confident wrong families*.

| # | defect | what it would have published | how it was caught |
|---|---|---|---|
| 1 | 🔴 **untitled BSD blind spot** — a BSD-3 payload whose first 14 lines never contain the string `BSD` | 3 cells `UNGRANTED`/unnamed | 🟢 `UNCLASSIFIED` bucket + hand read. **This is the historical `P459` defect reappearing in a different instrument** |
| 2 | 🔴 **markdown-titled Apache-2.0** — `Apache License` / `==========` / `_Version 2.0, January 2004_` is not contiguous, so the title regex missed it | `rstudio/learnr` unnamed | 🟢 same |
| 3 | 🔴 **ODbL absent from the family table** | `os-taxonomy` unnamed | 🟢 same — and the **shelf already had it right** |
| 4 | 🔴 **first-200-wins path ordering** — the reader returns the first licence path that answers 200, so a 108 B root stub beats the real `LICENSE.md` | `ucbds-infra/ottr` graded off a stub | 🟢 the shelf's own cell contradicted it |
| 5 | 🔴 **false `DISAGREE` from claim-line family ordering** — `ZeKaiNie/universal-examprep-skill`'s row names `CC0` in prose and `MIT` as its grant; the grader ordered CC above MIT and **published a disagreement** | a correct cell reported as wrong | 🟢 hand read: the payload reproduces the published cell **byte- AND digest-exact** (1 065 B `21f44893f051`). **This is `p452`'s defect class in a new instrument** |

🟡 **Two more, in the CONTROL code rather than the reader** — and both were caught by the controls
failing on correct data, which is the direction a control is supposed to fail in:

| # | defect | what it asserted wrongly |
|---|---|---|
| 6 | 🔴 the region-contract control counted `### North America` **file-wide** | `n=3` and a red — but the contract is scoped to the canonical block, and a **SUPERSEDED** block legitimately carries its own children. Fixed to count **inside** the block |
| 7 | 🔴 the preservation control asserted **contiguous containment** of the prior body on all eight shelves | red on `intel/market.md`, which is amended **in place** by design, so contiguity cannot hold. Its real contract is **insert-only**, proved by `git diff --numstat` showing **0 deletions**; the per-line check replaced the contiguity one |

🔴 **Defect 5 is the one to carry forward**: it is the third time on these shelves that an
instrument has matched a *string* where a *meaning* was required, and the first two were `p452`'s
and `p454`'s. 🟢 The denominator saves it — one false disagreement out of 356 graded cells is a
0.3 % error rate, and it was found because every non-`AGREE` verdict was read by hand.

### 🔴 Gaps this pass registers

| gap | statement | cheapest closure |
|---|---|---|
| 🔴 `457-A` | **91 of 457 addresses were excluded from grading** because their claim line carries more than one address. A fifth of the population is ungraded and the exclusion is silent in the totals | parse the table **cell**, not the line |
| 🔴 `457-B` | **12 of 20 `CLAIM_WITHOUT_PAYLOAD` cells are unrecoverable on both the payload and the manifest channel.** These shelves state a licence for them and no channel this base owns can corroborate it | a third channel — the package registry `p451` opened — or demote the cells |
| 🟡 `457-C` | The three 2026-10-24 relicensings were found **by re-reading**, not by watching. There is no instrument that would notice the next one | a dated digest ledger: one row per address, re-read each pass, diff |
| 🟡 `457-D` | `p456` reported **16** dead addresses over 455; this pass measures **13** over 457. The two address sets were never reconciled, so neither number refutes the other | diff the two extractions |
| 🔴 `457-E` | `Gap 456-D` is **unclosed and was searched**: no EMEA institution-level adoption rate is sourceable — see [`intel/market.md`](../intel/market.md) for what was returned instead |  |
| 🟡 `457-F` | `Gap 456-E` (`tosuki/moodle-mcp`) is **not re-probed this pass** and stays open | one two-channel probe |


## 🆕 `p456` — **🔴 `Gap 455-A` IS REFUTED AT 439/439 WITH ZERO DIVERGENCES, and the ladder rewrite it licensed is what put a WITHDRAWN grant on this shelf: `p455`'s own LanisAPI row is MIT read off a branch named `deprecated-0.4.1`, for a project whose HEAD README says in German that it is deprecated. 🟢 The ref axis is now RESOLVED, not guessed — `git ls-remote` works from this host and has for seven passes.**

🔴 **Gate posture, stated first as `Gap 446-A` requires: `make hooks` was DENIED**
(`Code from External`) — **eleven denials in twelve passes**, and running the carried gate
bodies directly is denied by the same classifier. 🔵 Nothing below is gate-attested.
**31 controls** were implemented independently and run in both directions
([`compose/code/p456-ref-resolution/controls.py`](../compose/code/p456-ref-resolution/controls.py));
three assert payload digests earlier passes published, and **two of this pass's own expectation
errors were caught by them** before anything reached this shelf.

### 🟢 The channel that was open for seven passes

🔵 `Gap 449-A` established that `curl -sI https://github.com/...` returns **403** on every real
repository on this host. Every pass since read that as *"github.com is closed"* and **guessed** the
ref axis from a fixed list (`HEAD`, `main`, `master`, `develop`, `dev`, `development`, `trunk`).
🟢 It is not closed to git:

```
$ git ls-remote --symref https://github.com/lanis-mobile/LanisAPI HEAD
ref: refs/heads/deprecation-notice	HEAD
```

One request, authoritative, and it decides `ADDRESS_DEAD` without a 91-request 404 sweep —
and decides it **more strongly**, because it separates *"no such repository"* from *"repository
with no licence file"* without guessing a single path.

### 🔴 `Gap 455-A` settled at population scale, at zero extra requests

`ls-remote --symref` returns the commit `HEAD` points at **and** every branch's commit in the
same response, so the gap's claim reduces to one comparison asked over all **455** carried
addresses on this shelf, `repos/foundations.md` and `verticals/solutions.md`:

| | n |
|---|---|
| live addresses | **439** |
| 🟢 `HEAD` points at the resolved default branch | **439** |
| 🔴 `HEAD` diverges | **0** |

🔴 **`Gap 455-A` is false.** `p455` inferred it from **one** repository by comparing two README
byte-counts (`HEAD` 331 B vs `master` 3 554 B), concluding the refs were different commits and
therefore that `HEAD` was unmoored. Both byte-counts are real; the conclusion does not follow:

| what it is | measured |
|---|---|
| 🟢 `HEAD` | **is** the default branch `deprecation-notice` — 331 B README, **no LICENSE**, same sha |
| 🔴 `master` | **is not a branch of this repository.** `refs/heads/` holds exactly `deprecated-0.4.1` and `deprecation-notice`. GitHub keeps a **rename redirect**; `raw.githubusercontent` still serves it, resolving to `deprecated-0.4.1` — 3 554 B README, MIT, digest `0bc449776673`, **byte-identical to what `p455` published "at `master`"** |

🔵 The two READMEs differ because the two **branches** differ. `p455` compared `HEAD` against a
ref that is not a branch and attributed the difference to `HEAD`.
Evidence: [`evidence/ref-axis-head-vs-default.2026-10-26-p456.tsv`](../evidence/ref-axis-head-vs-default.2026-10-26-p456.tsv).

### 🔴 `p455`'s LanisAPI row is CORRECTED — the grant is real and the project has withdrawn it

`p455`'s rewrite was *"never treat 'live but no grant at this ref' as a verdict — record it and
keep walking."* Applied to LanisAPI it walked **past a correct `REPO_LIVE_NO_GRANT` at `HEAD`**,
reached the stale alias, and shelved MIT. 🔴 Read at the project's own `HEAD` this pass:

> *"Das Projekt wurde deprecated. Entwicklung findet jetzt [hier](https://github.com/lanis-mobile/liblanis-for-python) statt."*

🔴 **Four defects in one row**: the project is deprecated by its own HEAD; the grant was cited at
a ref that is not a branch; the branch it actually lives on is named `deprecated-0.4.1`; and the
owner `kurwjan` is itself a **stale owner alias** — `kurwjan/LanisAPI` and `lanis-mobile/LanisAPI`
resolve to the same commit `9c0bd764`, and the canonical owner is `lanis-mobile`.
🟢 **The pre-`p455` behaviour was correct.** The rule this pass installs:

> 🟢 Read the grant at the **resolved default branch**. **No grant there IS the verdict.** A grant
> at any other ref is *that ref's* grant, is labelled `GRANT_OFF_DEFAULT` or
> `GRANT_ONLY_AT_ALIAS`, and is **never** shelved as the project's licence.

🟢 **The blast radius is one cell, and that is the other half of the finding.** 15 of 455 carried
addresses have a default branch outside the guessed list — and for **14 of them the carried ladder
read `HEAD` and got the byte-identical payload**, same family, same digest. Only LanisAPI differed,
and it is the row `p455` added in the pass that raised the gap. The carried licence families are
right.

### 🟢 Three rows read first-hand at the resolved default branch

| agent / client | address | grant (`GRANT_AT_DEFAULT`, resolved ref) | region | what it does |
|---|---|---|---|---|
| 🆕 🟢 liblanis | [`lanis-mobile/liblanis-for-python`](https://github.com/lanis-mobile/liblanis-for-python) | **MIT** · `LICENSE` @`master` `1 079` B `66f943b0689f` · holder *"2026 lanis-mobile developers"* | EMEA | The successor named by LanisAPI's own HEAD: Python API for **Schulportal Hessen** (Lanis), the Hesse *Land* education portal. 🔴 **Pre-release and not a drop-in**: `pyproject` declares `liblanis` **`1.0.0a1`** and `requires-python >=3.14`; **PyPI returns 404** for `liblanis`, so 🔵 **no registry cross-check exists for this row** — the grant is a byte-level read and nothing corroborates it |
| 🆕 🟢 ai-tutor-agent | [`vulinh1704/ai-tutor-agent`](https://github.com/vulinh1704/ai-tutor-agent) | **MIT** · `LICENSE` @`main` `1 071` B `e70d1d08d60a` · holder *"2026 Vu Linh Truong"* | Global | FastAPI + LangGraph tutoring starter: Socratic hints, **rubric-based grading** (per-criterion points + feedback, validated against the rubric) and session memory. 🟢 **Totals are computed in code, never by the model** — the one design choice on this shelf that makes a grade auditable. Runs on OpenAI or Claude, with an offline demo mode. 🔴 No LMS integration |
| 🆕 🟢 moodle-mcp (triffon) | [`triffon/moodle-mcp`](https://github.com/triffon/moodle-mcp) | **MIT** · `LICENSE` @`main` `1 067` B `66fa873bd85d` · 🔴 holder *"2026 **Falkenslab**"* | EMEA | Fork of [`falkenslab/moodle-mcp`](https://github.com/falkenslab/moodle-mcp) exposing **~230 tools** against Moodle (upstream ~140), driven through a real browser logged in as the user. 🔴 **Ships upstream's copyright holder and asserts none of its own** — see the narrowed lineage rule below |

🔵 **Fabricated negative control:** `nope-p456-ref-resolution/nope-p456` resolved nothing on
`ls-remote` and returned `ADDRESS_DEAD`, so every `GRANT_AT_DEFAULT` above is a measurement and
not a property of the probe.

### 🔴 One refusal — a licence badge whose own link is broken

🔴 **Nothing here is padded.** This candidate was named MIT by the search channel and is refused
because no grant payload exists at an address that does exist.

| candidate | what the secondary channel said | what the probe found | verdict |
|---|---|---|---|
| 🔴 **tosuki/moodle-mcp** | Described as the MIT-licensed Moodle MCP server for university portals with Microsoft Teams SSO (2FA) | 🟡 `LIVE_NO_GRANT` at the resolved default branch `main`: README line 8 carries a **shields.io `License-MIT` badge linking to `LICENSE`**, and `package.json` declares `"license": "MIT"` — but **no payload at any of 13 grant paths** | 🔴 **NOT SHELVED.** `MANIFEST_ONLY`. A badge whose own link resolves to nothing is not a grant, and a manifest field is a declaration, not a licence. 🔵 Genuinely useful and LATAM-relevant (pt-BR submission strings, `Enviado para avaliação`) — see `Gap 456-E` |

### 🟢 A cross-channel confirmation nobody had asked for

🟢 16 of 455 addresses resolve nothing through `ls-remote`, and **every one is already carried on
these shelves as `ADDRESS_DEAD` or `ABSENT`** — determined by the 404 sweep, a completely
independent channel. Two channels, **455/455 agreement**, both fabricated negative controls
(`nope-p454-dapodik`, `nope-p455-version-axis`) correctly dead. 🔵 **So the `ADDRESS_DEAD` class on
these shelves is not an inference artefact** — a worry `Gap 454-H` left standing and that nothing
until now could settle.

### 🟡 `p455`'s digest-lineage rule is NARROWED by measurement, not retired

`p455` wrote, of two identical GPL-3.0 digests: *"both serve the stock GPL-3.0 text, so a digest
match here is evidence of a stock payload and **never** of shared lineage."* 🟡 Measured, that
holds only for **holder-free** families:

| payload | holder line in the text? | what an identical digest proves |
|---|---|---|
| 🔵 GPL-3.0, `35 149` B | 🔴 **none** — 0 `Copyright (c) YEAR HOLDER` lines | a stock payload. Nothing about lineage |
| 🟢 MIT, `1 067` B | 🟢 **yes** — `Copyright (c) 2026 Falkenslab`, in both | the **same holder string**, so it **is** lineage |

🟢 **The corrected rule:** a digest match is evidence of lineage **iff** the family embeds a
holder (MIT, BSD, ISC), and evidence of nothing when it is a stock copyleft text. `p455`'s
sentence is right about GPL-3.0 and wrong as stated generally.

### 🔴 Gaps this pass registers

- 🔴 **`Gap 456-A`** — the **424** cells whose default branch *is* in the guessed list were not
  re-read for **payload** at the resolved ref; only the 15 off-list cells were. The 439/439
  `HEAD`-is-default proof makes a divergence unlikely, but it is **unmeasured**.
- 🟡 **`Gap 456-B`** — `GRANT_ONLY_AT_ALIAS` is implemented and control-tested, but **no carried
  cell exercised it**: LanisAPI resolved to `GRANT_OFF_DEFAULT` because `deprecated-0.4.1` is a
  live branch. The class is unexercised on real data.
- 🟡 **`Gap 456-C`** — this pass's own address extractor swept `github.com/owner/repo` out of a
  **prose template** at `agents/top.md:567` and fed it to the census as an address. It was
  correctly reported `ADDRESS_DEAD` so nothing was published wrong, but the extractor cannot
  distinguish a cited address from a placeholder, and any later automated census inherits that.
- 🔴 **`Gap 456-E`** — `tosuki/moodle-mcp` is unshelveable only for want of a `LICENSE` its own
  badge already links to. Nobody has asked the maintainer.

## 🆕 `p455` — **🟢 EMEA GAINS A SUPPLY TIER THESE SHELVES HAVE NEVER CARRIED: eleven permissive clients to the four national school systems of France and the DACH countries, every grant read first-hand at `HEAD`. 🔴 And four candidates that every secondary source called real are REFUSED — one of them recommended by name as the maintained alternative to a shelved project, with nothing readable at the address its own registry record names.**

🔴 **Gate posture, stated first as `Gap 446-A` requires: `make hooks` was DENIED**
(`Code from External`) before any gate body ran — **ten denials in eleven passes**. 🔵 Nothing
below is gate-attested. The contracts were re-implemented independently and run in both
directions ([`compose/code/p455-version-axis/`](../compose/code/p455-version-axis/));
34 controls pass, and **three of this pass's own four instrument defects were caught by them
before anything was published**.

### 🟢 The tier EMEA was missing, and it is the one `Gap 454-F` predicted would have to be found on the supply side

`Gap 454-F` recorded that the prescribed market channel returns nothing education-specific for
EMEA, and that EMEA's opportunities therefore had to be sourced from **supply read first-hand**.
This pass did that deliberately, applying `Gap 453-B`'s measured rule — *prefer vocabulary whose
education sense is unambiguous, and whose name is LONG* — to Europe's national systems of record:
`pronote`, `ecoledirecte`, `schulportal hessen`, `webuntis`. All four are orthographically
distinctive, and all four returned assets at the first attempt.

| agent / client | address | grant (first-hand, `HEAD` this pass) | region | what it does |
|---|---|---|---|---|
| 🆕 🟢 pronotepy | [`bain3/pronotepy`](https://github.com/bain3/pronotepy) | **MIT** · `LICENSE` `1 062` B `4f074ab7dccb` · PyPI `2.15.7` declares `MIT` → 🟢 `AGREE` | EMEA | Python client for **PRONOTE** (Index Éducation), the gradebook/timetable system of most French secondary schools. 🟡 **Maintenance mode by the maintainers' own notice**: bug fixes and PRONOTE-compatibility updates only, no new features. Does **not** use the official HYPERPLANNING API |
| 🆕 🟢 EcoleDirecte API (PHP) | [`studoo-app/ecole-directe-api`](https://github.com/studoo-app/ecole-directe-api) | **MIT** · `LICENSE` `1 071` B `6c086a4639ac` · Packagist `studoo/ecole-directe-api@v0.1.5` declares `MIT` → 🟢 `AGREE` | EMEA | PHP client for **EcoleDirecte**, the second French school portal. 🔵 **The package vendor and the git owner differ** (`studoo` vs `studoo-app`) — resolved from the record's repository field, never from the name (`Gap 451`) |
| 🆕 🟡 ecoledirecte.js | [`a2br/ecoledirecte.js`](https://github.com/a2br/ecoledirecte.js) | **MIT** · `LICENSE` `1 073` B `e4ba09041791` | EMEA | TypeScript client for the EcoleDirecte private API. 🔴 **Unmaintained by the author's own notice since 2023-08-08** and expected to break as the API moves — shelved as a reference implementation, not a dependency |
| 🆕 🟢 LanisAPI | [`kurwjan/LanisAPI`](https://github.com/kurwjan/LanisAPI) | **MIT** · `LICENSE` **@`master`** `1 076` B `0bc449776673` | EMEA | Python client for **Schulportal Hessen** ("Lanis"), a German *Land*-level education portal: homework, substitution plans, calendar, conversations. 🔴 **The grant is not at `HEAD`** — see `Gap 455-A`, the defect this row produced |
| 🆕 🟢 lanis-rs | [`lanis-mobile/lanis-rs`](https://github.com/lanis-mobile/lanis-rs) | **GPL-3.0**, forward grant **`or-later`** · `LICENSE` `35 149` B `3972dc9744f6` · crates.io `0.3.0` declares `GPL-3.0` → 🟢 `AGREE` | EMEA | Rust API for the same portal. 🟡 Maintainers state it is early and expects *"drastic & breaking changes"*. 🔴 Copyleft: usable behind a service boundary, not vendorable |
| 🆕 🟢 maria | [`elderguardian/maria`](https://github.com/elderguardian/maria) | **GPL-3.0**, `or-later` · `LICENSE` `35 149` B `3972dc9744f6` | EMEA | TypeScript Lanis library: authentication, substitute-teacher plan, homework. 🔵 **Byte-identical licence digest to `lanis-rs`** — both serve the *stock* GPL-3.0 text, so a digest match here is evidence of a stock payload and **never** of shared lineage |
| 🆕 🟢 WebUntis (SchoolUtils) | [`SchoolUtils/WebUntis`](https://github.com/SchoolUtils/WebUntis) | **MIT** · 🔴 **`License`** `1 070` B `d2e54565d9bf` · npm `webuntis@2.2.1` declares `MIT` → 🟢 `AGREE` | EMEA | The reference Node/TS client for **WebUntis**, the timetable system used across Austrian, German and Swiss schools. 🔵 Grant served at mixed-case **`License`** — a path a `LICENSE`-only reader misses |
| 🆕 🟢 webuntis_headless | [`Tynobi-Company/webuntis_headless`](https://github.com/Tynobi-Company/webuntis_headless) | **MIT** · `LICENSE` `1 070` B `2b7c9c3fffa3` · npm `1.0.0` declares `MIT` → 🟢 `AGREE` | EMEA | Headless WebUntis sessions, timetables over a date range, lesson detail |
| 🆕 🟢 untis-api-client | [`arnim279/untis-api-client`](https://github.com/arnim279/untis-api-client) | **GPL-3.0** · `LICENSE` `35 562` B `72d2f09334f8` · npm `1.1.0` declares `GPL-3.0-or-later` → 🟢 `AGREE` **on the version axis** | EMEA | WebUntis client over the **public** JSON-RPC API (the others use the internal one). 🟢 `or-later` is declared *and* served, so it may be taken forward into a GPL-3.0 work |
| 🆕 🟢 untis-js | [`thatmarcel/untis-js`](https://github.com/thatmarcel/untis-js) | **MIT** (body form, no title) · `LICENSE` `1 068` B `a1139daad821` · npm `1.0.1` declares `MIT` → 🟢 `AGREE` | EMEA | ESM-only WebUntis client for Node |
| 🆕 🟢 WebUntisAPI.Client | [`Suiram1701/WebUntisAPI.Client`](https://github.com/Suiram1701/WebUntisAPI.Client) | **MIT** · `LICENSE.txt` `1 067` B `8b7a2e8d023e` | EMEA | .NET/NuGet WebUntis client. 🟡 **Carries the only rate limit any row on this shelf states**: never 10 req/s, no more than 1 800 req/h and in no case above 3 600 req/h — exceeding it *"could permanently block"* access |
| 🆕 🟢 WebUntisAPI (Java) | [`Keule0010/WebUntisAPI`](https://github.com/Keule0010/WebUntisAPI) | **MIT** · `LICENSE` `1 064` B `e29c116f5d80` | EMEA | Java wrapper over the WebUntis JSON-RPC 2.0 API; Java 8+ |

🔵 **Fabricated negative control:** `github.com/nope-p455-version-axis/nope-p455` and
`nope-p455-sweep/nope-p455` returned `ADDRESS_DEAD` on the full ladder, so every `READ` above is
a measurement and not a property of the probe.

🟢 **Two non-EMEA rows read first-hand this pass**, both already known to the trending shelves and
now carrying a dated grant: [`skyzh/tiny-llm`](https://github.com/skyzh/tiny-llm) (**Apache-2.0** ·
`11 357` B `c71d239df917`) and [`withmarbleapp/os-taxonomy`](https://github.com/withmarbleapp/os-taxonomy)
(🔴 **ODbL**, re-read `25 289` B `77d2692c3d64` — a share-alike *database* licence with **no code
grant**, which the title-anchored reader now classes `NOT-OSI` by name rather than leaving `UNREAD`).

### 🔴 Four refusals — and the first one is the expensive kind

🔴 **Nothing here is padded.** Each of these was named by a secondary source as a real,
licensed project; each is refused because the grant could not be read at an address that exists.

| candidate | what the secondary channel said | what the probe found | verdict |
|---|---|---|---|
| 🔴 **Pawnote** | Recommended **by the `pronotepy` maintainers themselves** as the actively-developed alternative. npm `pawnote@1.6.2` declares **`GPL-3.0-or-later`** and back-links `LiterateInk/Pawnote.js` | 🔴 `ADDRESS_DEAD` on **four case variants** (`LiterateInk/Pawnote.js`, `LiterateInk/pawnote`, `literateink/Pawnote.js`, `LiterateInk/Pawnote`), all 13 grant paths × 7 refs | 🔴 **NOT SHELVED.** `Gap 454-H`'s class exactly: a declared grant that can no longer be checked against anything. A live registry record with a populated back-link is **not** evidence that the code is readable |
| 🔴 **Pawdirecte** | Described as the maintained EcoleDirecte wrapper, Rust + JS, GPL-3.0, on npm and crates.io | 🔴 npm serves **HTTP 200 with an empty record**; crates.io **404** | 🔴 **NO ADDRESS RESOLVED** — and the empty 200 is `Gap 455-C` |
| 🔴 **Linkdirecte** | *"A newer SDK covering login with 2FA, grades, timetable and homework"*, wiki **updated July 2026** | 🔴 `Scolup/Linkdirecte` → `ADDRESS_DEAD` | 🔴 **NOT SHELVED.** A live wiki URL in a result set is not evidence of a readable repository |
| 🔴 **education-crm** | A search result carried an **"MIT mention"** for a school/student/teacher management platform | 🟡 `asadbekme/education-crm` → `REPO_LIVE_NO_GRANT`: the repository serves `README.md` and **no licence file at any of 13 paths** | 🔴 **NOT SHELVED as MIT.** An "MIT mention" in a directory listing is not a grant. This is the precise shape of the padding the encargo forbids |

### 🔴 `Gap 455-A` — `HEAD` is not the default branch, and a first-live-ref reader publishes a FALSE UNGRANTED

🔴 The fast probe ladder this pass built assumed what its own docstring asserted: that `HEAD` on
`raw.githubusercontent.com` follows the repository's default branch, so one probe covers every
non-`main` ref in `Gap 454`'s list. **It does not.** Measured first-hand on `kurwjan/LanisAPI`:

| ref | `LICENSE` | `README.md` |
|---|---|---|
| `HEAD` | 🔴 `404` (14 B) | 🟢 `200` — **331 B** |
| `master` | 🟢 `200` — **1 076 B** | 🟢 `200` — **3 554 B** |
| `main` | 🔴 `404` | 🔴 `404` |

🔴 **Two READMEs of two different sizes: `HEAD` and `master` are different commits**, and the
substantive tree — including the MIT grant — is on `master` only. So a ladder that accepts the
first ref whose README resolves reports `REPO_LIVE_NO_GRANT` for a repository carrying an **MIT
licence one ref over**. 🔵 That failure direction is the mirror of `Gap 454-B`'s: a false `UNREAD`
invites a wrong promotion, a false *ungranted* **discards a usable permissive dependency**.
🟢 Fixed here by never treating "live but no grant at this ref" as a verdict — the ladder records
it and keeps walking, and publishes it only once every ref is exhausted
([`fetch_fast.py`](../compose/code/p455-version-axis/fetch_fast.py)). 🔴 **Open:** the carried
probes were not audited for the same short-circuit, and `REPO_LIVE_NO_GRANT` cells already on
these shelves were not re-probed across refs.

## 🆕 `p454` — **🟢 `Gap 453-A`'s prescribed closure IS RUN over the 71 carried cells, and the answer the first run gave was WRONG: it reported 6 disagreements and 3 of them were the instrument's own. 🔴 Four defects in this pass's licence reader, and the first is INHERITED FROM THE GATE CODE — the 40-line window that `p450` installed to fix GPLv3 mis-grades GPLv2 as LGPL. 🟢 `Gap 453-D` CLOSES for Indonesia with four MIT rows read first-hand.**

🔴 **Gate posture, stated first as `Gap 446-A` requires: `make hooks` was DENIED** (`Code from
External`) before any gate body ran — **nine denials in ten passes**. 🔵 Nothing below is
gate-attested. 23 controls were re-implemented independently and run in **both** directions
([`compose/code/p454-carried-cell-value/controls.py`](../compose/code/p454-carried-cell-value/controls.py),
[`family_controls.py`](../compose/code/p454-carried-cell-value/family_controls.py)); eight of them
assert payload digests **earlier passes published**, which is how three of this pass's four reader
defects were caught.

### 🔴 `Gap 453-A` answered — and the headline is that the instrument lied first

`Gap 453-A` named this *"`p454`'s cheapest closure"*: 71 carried registry-sourced licence cells
swept by `p452` for **address** (63/71 `AGREE`, 0 `DISAGREE`) and **never for value**.

🔴 **The first run reported 6 `DISAGREE` (8.5 %) — nearly triple `p453`'s 3.0 % on novel
packages — and that number was an artefact.** Three of the six were the licence reader's:

| address | first run said | first-hand read says | verdict |
|---|---|---|---|
| [`oat-sa/tao-core`](https://github.com/oat-sa/tao-core) | 🔴 declared `GPL`, served **`LGPL`** | 🟢 payload is **`GNU GENERAL PUBLIC LICENSE Version 2`** (`LICENSE` 18 025 B `a01259a1b522`); Packagist `v56.14.9` declares **`GPL-2.0-only`** | 🟢 **`AGREE`** — the disagreement was manufactured |
| [`bncc-dev/bncc-pacotes`](https://github.com/bncc-dev/bncc-pacotes) ×2 | 🔴 declared `MIT`, served **`CC-BY`** | 🟡 payload is a **documented two-part notice**: code `MIT`, embedded data `CC BY 4.0` (`LICENSE` 1 299 B `86bf5f5e6306`) | 🟡 **`COMPOSITE`**, not a disagreement — and the registry's `MIT` is half-right |

🟢 **The corrected figures over all 71 carried cells**
([`evidence/carried-cell-licence-value.2026-10-26-p454.tsv`](../evidence/carried-cell-licence-value.2026-10-26-p454.tsv)):

| verdict | n | share | what it means |
|---|---|---|---|
| 🟢 `AGREE` | 41 | 57.7 % | registry value and payload at `HEAD` are the same family |
| 🟡 `MANIFEST_ONLY` | 10 | 14.1 % | registry declares a grant; **no payload at 13 paths** — 🔴 see the split below, this class conflates two facts |
| 🔵 `NO_ADDRESS` | 8 | 11.3 % | `p452`'s 6 `ABSENT` + 1 `NO_RECORD` + 1 `PAGES_ONLY` |
| 🟡 `REGISTRY_SILENT` | 5 | 7.0 % | payload grants; the registry field is empty |
| 🔴 `DISAGREE` | 3 | 4.2 % | registry value and payload differ |
| 🔴 `NO_GRANT_ANYWHERE` | 2 | 2.8 % | neither registry nor repository grants anything |
| 🟡 `COMPOSITE` | 2 | 2.8 % | one artefact, two grants, one registry field |

🔵 **And the comparison `Gap 453-A` was opened to make: 4.2 % carried vs 3.0 % novel is
indistinguishable at these denominators (3/71 vs 5/166).** So the hypothesis that this base's
*published* cells are cleaner than the open registry **is refuted** — and so is the opposite. The
licence field is equally unreliable whether a human curated it or a probe found it.

### 🔴 `MANIFEST_ONLY` conflated two different facts, and the split is the pass's bluntest number

🔴 **A verdict built from grant paths alone cannot tell "the repository exists and has no licence
file" from "the repository is gone".** Both return `404` on all 13 paths. 🟢 Re-probed on **13
NON-licence paths** (`README.md`, `package.json`, `composer.json`, `pyproject.toml`, …), the 12
`MANIFEST_ONLY` + `NO_GRANT_ANYWHERE` cells split:

| class | n | addresses |
|---|---|---|
| 🔴 **`ADDRESS_DEAD`** — repository gone at `HEAD` | **8** | `thanh01pmt/interactive-quiz-kit` *(npm declared MIT)*, `ale-alejandro/beadkit`, `mckaroff/graphlms` *(MIT)*, `santillana-ai/tutor-sdk` *(MIT)*, `creaditor/frontend` *(ISC)*, `parkseokjune/unist-blackboard-mcp` *(MIT)*, `dev-cucei-itrans/siiau-api-client` *(BSD-3-Clause)*, `imsglobal/caliper-php` *(LGPL-3.0)* |
| 🟡 `REPO_LIVE_NO_GRANT` — repository live, no grant anywhere | 4 | [`dmontgomery40/mcp-canvas-lms`](https://github.com/dmontgomery40/mcp-canvas-lms), [`general-mudkip/d2l-mcp-server`](https://github.com/general-mudkip/d2l-mcp-server), [`loyaniu/moodle-mcp`](https://github.com/loyaniu/moodle-mcp), [`vosslab/qti_package_maker`](https://github.com/vosslab/qti_package_maker) |

🔴 **So the honest figure for shelf decay is not 4.2 %: 16 of 71 carried cells (22.5 %) point at
nothing readable** — 8 with no address at all (`p452`'s `ABSENT`/`NO_RECORD`/`PAGES_ONLY`) and 8
with an address that is **dead at `HEAD`**. 🔵 That extends `Gap 452-B`, whose corrected
unreachability rate on *newly discovered* registry addresses was **8.8 %**: on **carried** cells it
is **11.3 %** dead plus 11.3 % addressless. 🟢 `imsglobal/caliper-php` is the one that should sting
— it is the IMS Global reference implementation of the **Caliper** analytics standard, and both
plausible successors (`1EdTech/caliper-php`, `IMSGlobal/caliper-php`) also `404`.

### 🔴 The three disagreements that survived a first-hand read

| address | registry says | payload at `HEAD` says | why it matters |
|---|---|---|---|
| [`aswanth9495/exam-guard`](https://github.com/aswanth9495/exam-guard) · [`scaler-opensource/exam-guard`](https://github.com/scaler-opensource/exam-guard) | npm `exam-guard@10.0.4` → **`ISC`** | **`Apache-2.0`** (`LICENSE` 11 357 B `c71d239df917`, both addresses) | 🟡 permissive↔permissive, but Apache-2.0 carries a **patent grant and a NOTICE duty** that ISC does not. 🟢 Third and fourth instances of the ISC-declared/Apache-served pattern `p453` first saw on `node-ecole-directe` |
| [`tl-its-umich-edu/caliper-php-public`](https://github.com/tl-its-umich-edu/caliper-php-public) | carried as **`proprietary`** | **`LGPL-3.0`** (`LICENSE` 7 438 B `8c401dfc8928`) | 🔴 **the under-granting direction, and it is new.** A team filtering on the registry field **discards** a genuinely LGPL asset. 🔴 And the registry record itself is **gone**: `repo.packagist.org/p2/…` and `/packages/….json` both **404** today, so the carried `proprietary` is no longer checkable at source |

### 🔴 A carried row is STALE, and the direction is the worst one available

🔵 These shelves carry [`nakafaai/nakafa.com`](https://github.com/nakafaai/nakafa.com) as
*"Nakafa Source Available `1.0`, eff. `2026-04-24` — NOT OSI"*, `7 705` B `de3d94045061`
(`p229`, re-cited by `p230` and `p348`).

🔴 **At `HEAD` today it is `Nakafa Source Available License 2.0`, effective `2026-10-24` — two
days ago — `11 997` B `97e8bdc2e3cd`**, and the payload is **byte-identical** at
[`nakafaai/aksara`](https://github.com/nakafaai/aksara). The whole estate re-versioned on the
same date:

| path | grant | bytes · `sha256_12` |
|---|---|---|
| `LICENSE` | 🔴 Nakafa **Source Available** License 2.0 | `11 997` · `97e8bdc2e3cd` |
| `CONTENT_LICENSE.md` | 🔴 Nakafa **Content** License 2.0 | `10 053` · `2af44ab89691` |
| `TRADEMARKS.md` | 🔴 Nakafa **Trademark and Brand Policy** 2.0 | `4 508` · `3ba64345e201` |

🔴 **`p453` held this exact payload in its hands and recorded it `UNREAD` / `POINTER`.** On a
shelf, `UNREAD` reads as *"grant not determined"* — which **invites a later pass to promote it** —
while the payload's own second sentence is *"It is not open source, and it is not free to reuse."*
🔵 Read first-hand: §4 forbids fork, mirror, redistribution, packaging, sublicensing, sale and
hosting without written permission, and permits a fork **only** to prepare a pull request. §13 is
the clause an engagement must read: a copy **lawfully received before** `2026-10-24` stays under
`1.0` **for that copy only**, and every act started on or after that date — *"including a fork,
publication, recording, post, Benefit, or AI use"* — is under `2.0`; version `1.0` is pinned at
commits `ec5cb15359fc…` (`nakafa.com`) and `9b8cbbd9cc82…` (Aksara).

🟢 **Standing rule this adds to `P453-A`:** a grant is **dated**, not just read. A carried licence
cell with no re-read date is an assertion about the past.

### 🟢 Promotions — Indonesia closes `Gap 453-D`, each row read first-hand at `HEAD` this pass

🟢 **`Gap 453-B`'s remedy is confirmed with a measured contrast, which is the first time this base
has had one.** Its rule was *"prefer vocabulary whose education sense is unambiguous — a named
system of record"*. Run over four legs × three registries:

| term | kind | candidates | education assets | precision |
|---|---|---|---|---|
| 🟢 `dapodik` | **distinctive proper name** (Indonesia's national school data system) | 4 | **4** | 🟢 **100 %** |
| 🟢 `e-stat` / `gakko kihon chosa` | named statistical service | 47 | 1 | 🟡 2 % |
| 🔴 `deped` | **short acronym** (Philippine education department) | 59 | **0** | 🔴 **0 %** — matched `deptrac`, `php-di`, `symfony/dependency-injection`, every `depend`-shaped package on Packagist |
| 🔴 `psa` | short acronym | — | 0 | 🔴 **0 %** — matched ConnectWise PSA, PureScript `psa`, Oracle `oci-psa` |

🔵 **So the remedy needs one amendment, and it is cheap: a named system of record only helps if
the NAME IS LONG.** `dapodik`, `ecoledirecte`, `pronote`, `vervalpd` are orthographically
distinctive; `deped`, `psa`, `npsn`, `uis` are three-to-five-letter strings that live inside
ordinary English software words.

| agent / client | address | grant (first-hand, `HEAD`) | region | what it does |
|---|---|---|---|---|
| 🆕 🟢 Dapodik WebService SDK | [`ardianryan/dapodik-sdk`](https://github.com/ardianryan/dapodik-sdk) | **MIT** · `LICENSE` `1 739` B `29e7d361ee3d` | APAC | Typed TS/JS SDK for the **Dapodik** web service (`dapo.kemendikdasmen.go.id`), Indonesia's national school/teacher/student register. npm `@smansage/dapodik-sdk@1.0.0`, modified `2026-08-30` |
| 🆕 🟢 VerValPD client | [`smantriplw/vervalpd-node`](https://github.com/smantriplw/vervalpd-node) | **MIT** · `LICENSE` `1 068` B `0ae5076b1e03` | APAC | Node client for **VerValPD** (`vervalpd.data.kemdikbud.go.id`), the student-identity verification system; `findStudent(query, limit, offset)` over an undocumented API |
| 🆕 🟢 Dapodik API (PHP) | [`adereksisusanto/dapodik-api-php`](https://github.com/adereksisusanto/dapodik-api-php) | **MIT** (body form, no title) · `LICENSE.md` `1 105` B `ce39902853af` | APAC | Packagist-published PHP client for the same register, with CI |
| 🆕 🟢 Dapodik teacher statistics | [`bantenprov/dapodik-data-guru`](https://github.com/bantenprov/dapodik-data-guru) | **MIT** · `LICENSE` `1 072` B `3508ba25c5ad` | APAC | Provincial (Banten) recapitulation of Dapodik **teacher** data — the aggregate tier above the register |
| 🆕 🟡 e-Stat MCP (Japan) | [`pipeworx-io/mcp-estat-japan`](https://github.com/pipeworx-io/mcp-estat-japan) | **MIT** · `LICENSE` `1 070` B `42501667035e` | APAC | MCP over **e-Stat**, Japan's official statistics portal (~5 000 tables incl. the School Basic Survey). 🟡 **Graded honestly: a general-government-statistics gateway, not an education asset** — education is one domain of many |

🔵 **Fabricated negative control:** `github.com/nope-p454-dapodik/nope-p454` returned
`NO_PAYLOAD` on all 9 grant paths and all 6 README paths, so the six reachable rows above are a
measurement and not a property of the probe.

### 🔴 Four reader defects, and the first one is the gate's

🔴 **(a) INHERITED, and it is the load-bearing one.** `Gap 450-C` defect (a) was *"a body grep
calls every GPLv3 payload LGPL"*; `p450`'s remedy — carried in
[`p453-vocabulary-ledger/verify.py`](../compose/code/p453-vocabulary-ledger/verify.py) — truncates
to the first **40 non-empty lines**. 🔴 **GPLv2's PREAMBLE recommends the LGPL at non-empty line
15**, inside that window: *"(Some other Free Software Foundation software is covered by the GNU
Lesser General Public License instead.)"* So the window fixes GPLv3 and **breaks GPLv2**, and the
defect stayed invisible for four passes because it was only ever validated on the version whose
mention falls **outside** the window. 🟢 The sound anchor is the **title block**.

🔴 **(b)-(d) this pass's own**, each caught by a first-hand read before anything was published:
the composite check keyed on **markdown heading count** (so `aksara`'s 15 numbered sections read
as a composite, and `bncc`'s genuine two-part notice lost its MIT half); `all rights reserved` was
treated as evidence of a closed grant (it is the **opening line of thousands of MIT payloads** —
[`davepacheco/node-extsprintf`](https://github.com/davepacheco/node-extsprintf) serves exactly
that and then grants MIT in the next sentence); and an in-repo **pointer** was graded `NOT-OSI`
([`ckeditor/ckeditor5`](https://github.com/ckeditor/ckeditor5) serves a `170` B root `LICENSE.md`
reading *"maintained in `packages/ckeditor5/LICENSE.md`"*, and the repo really does serve a
`17 983` B `COPYING.GPL`).

🟢 **Measured cost of the carried reader: 5 of 179 payloads (2.8 %) grade differently**
([`evidence/family-reader-delta.2026-10-26-p454.tsv`](../evidence/family-reader-delta.2026-10-26-p454.tsv)),
and **three of the five were `UNREAD`** — the verdict that invites a promotion. Two of those three
are genuinely closed: `nakafaai/aksara` above, and
[`asherlc/dofek`](https://github.com/asherlc/dofek) (`1 125` B `3307cb042fcc`), whose payload
grants *"viewing and reference purposes only"*, carries an explicit **no-AI-training clause**, and
defers to a **per-directory `LICENSE` override**.

🟢 **`Gap 453-E` (d) reproduced live as a control, not inferred:**
`raw.githubusercontent.com/ckeditor/ckeditor5/HEAD/LICENSE` returns **HTTP 404 with a 14-byte
body** whose content is the string `404: Not Found`. Every read in this pass gates on
`%{http_code}`, so no phantom grant was published — but a byte-reader would have recorded a
14-byte licence.

## 🆕 `p453` — **🟢 `Gap 452-A` IS ANSWERED WITH THE LARGEST DISCOVERY DENOMINATOR THIS BASE HAS EVER HAD, AND IT CONFIRMS `p452`'s PREDICTION IN BOTH DIRECTIONS: the eight prescribed identically-worded legs returned 13 tokens and ZERO at zero prior hits, while ten NEW-VOCABULARY legs on the same registry channel returned 182 candidates and 157 at zero. 🔴 And the finding that costs the most: 2 of those 157 are education assets and the rest are HOMONYMS — a live, permissively-granted address can pass every probe this base owns and still have nothing to do with education.**

🔴 **Gate posture, stated first as `Gap 446-A` requires: `make hooks` was DENIED.** The host refused
the recipe (`Code from External`) before any gate body ran — **eight denials in nine passes**.
🔵 Nothing below is gate-attested. The load-bearing contracts were re-implemented independently
(region-heading `CANON`/`VOCAB` read from `check_headings.py:17-19`, newest-first insertion read
from `check_newest_block.py`, frontmatter vocabulary, append-only byte containment,
table-header-as-data) and all are green.

### 🟢 `Gap 452-A` settled: the word list is the variable, now measured against its own control

`p452` left this as a **prediction with a mechanism**: *"a ninth identically-worded regional leg
will nil"*, and *"the cheaper and now-evidenced move is to vary the word list."* 🟢 **Both halves
were run in the same hour, which is what makes this a test and not another anecdote.**

| arm | legs | tokens / candidates | at **zero** prior hits | verdict |
|---|---|---|---|---|
| 🔴 the **prescribed** vocabulary (`{agents, trending, verticals, news} × {global, NA, EMEA, APAC, LATAM}`) | 8 | 13 graded tokens | 🔴 **0** | 🔴 **ninth consecutive nil — predicted, and confirmed** |
| 🟢 **new** vocabulary (pedagogy · assessment · credentialing · special-education · early-years · vocational · curriculum · ES · PT · FR) | 10 | **182** candidates | 🟢 **157** | 🟢 **the word list is the variable** |

🔵 Every prescribed-leg token carried prior hits, and the *thinnest* of them (`Ednova`, 8 files)
is the one that would expose a coverage hole first — so the nil is attributable to exhausted
vocabulary, not to a thin channel. Ledger:
[`evidence/vocabulary-spend-ledger.2026-10-26-p453.tsv`](../evidence/vocabulary-spend-ledger.2026-10-26-p453.tsv);
instrument [`compose/code/p453-vocabulary-ledger/`](../compose/code/p453-vocabulary-ledger/).
🟢 **The ledger is the instrument `Gap 452-A` said did not exist** — it records which vocabularies
have been spent, with the yield of each, so `p454` does not re-spend them blind.

### 🔴 And the expensive half of the answer: novelty is NOT relevance

🔴 **157 addresses at zero prior hits sounds like a discovery channel. It is not, and the measured
reason is homonymy.** The vocabulary that is unspent *in education* is heavily spent elsewhere:

| leg | what it was meant to find | what npm's text ranking actually returned |
|---|---|---|
| 🔴 `curriculum standards alignment` | curriculum mapping tools | **text-alignment libraries** — `ansi-align`, `wide-align`, `@udecode/plate-alignment`, `remark-lint-table-pipe-alignment`, `ndarray-base-dtype-alignment` |
| 🔴 `early years kindergarten literacy` | early-years learning tools | `@putout/plugin-apply-early-return`, `haraka-plugin-early_talker`, `end-of-stream`, `d3-time` — and `kindergarten` (MIT), which is an **authorization/permissions library** |
| 🔴 `educacao escolar aprendizagem` | Brazilian education tooling | **13 Laboratoria bootcamp `md-links` exercises** (cohort slugs `sap0xx`, `lim0xx`, `mex008`) |

🔴 **The worked example that proves the gate is insufficient, and it is the cleanest one this base
has produced:** [`food-x-technologies/escolar`](https://github.com/food-x-technologies/escolar)
is **live** at `HEAD`, serves a **real MIT payload** (`LICENSE` **1 075 B `sha256₁₂ 3b443e863252`**),
and its npm record **back-links the exact slug**. It passes the back-link probe (`p452`), the
reachability probe (`Gap 452-B`) and the grant read — **three of this base's instruments, all
green** — and its entire surface is *"Replace properties in json with file contents."* 🔴 **It is
not an education asset and no probe this base owns could say so.** Registered as `Gap 453-B`: the
promotion precondition needs a **third, SURFACE probe**, and only a first-hand `README` read at
`HEAD` supplies it. 🔵 Every row below passed that read; the ones that failed it are named as
rejections rather than quietly dropped.

### 🟢 Promotions — each read first-hand at `HEAD` this pass, and each surface read before shelving

🔵 Byte counts are `curl -w '%{size_download}'`, never shell command substitution, which strips
the trailing newline and runs every count one short (`Gap 450-C` defect (b)). Licence family is
read **title-anchored**, never by whole-body grep, which calls every GPLv3 file LGPL (defect (a)).

| repository | grant, read first-hand at `HEAD` | surface, read first-hand | region |
|---|---|---|---|
| [`interop-alliance/verifier-core`](https://github.com/interop-alliance/verifier-core) | 🟢 **MIT** — `LICENSE.md` **1 087 B `sha256₁₂ 6e7a616c4d70`** | Verifies **W3C Verifiable Credentials** in browser, Node.js and React Native (`verifyCredential`, `verifyPresentation`, batch `createVerifier`). 🟢 **The one credential-substrate row that is education-facing on its own terms: 10 `README` mentions of badge/learner/academic vocabulary**, where `digitalbazaar/vc` and `trustvc/w3c` have **0** | ⚪ **Global** |
| [`androz2091/node-ecole-directe`](https://github.com/androz2091/node-ecole-directe) | 🔴 **Apache-2.0** — `LICENSE` **11 357 B `sha256₁₂ c71d239df917`**, title `Apache License / Version 2.0`. 🔴 **npm declares `ISC` on every published version** — see `Gap 453-A` | Client for **ÉcoleDirecte**, a French national school system of record: authentication for **Élève** and **Famille** accounts, then `notes`, `devoirs`, `emplois du temps` and `vie scolaire` (retards, absences, sanctions) | 🟢 **EMEA** — France |
| [`t2-educacao/midas-ui`](https://github.com/t2-educacao/midas-ui) | 🟢 **MIT** — `LICENSE` **1 070 B `sha256₁₂ 3db74f670f09`** | `@t2-educacao/midas` — the React component library and design system of **T2 Educação**, a Brazilian education provider: accessible components, light/dark design tokens, Tabler icons, shared across its site, hub and student platform | 🟢 **LATAM** — Brazil |

🟡 **Watch tier, not build-on — stated with the reason, because the grant is the whole point:**

| repository | grant | why it is not a build-on row |
|---|---|---|
| [`papillonapp/papillon-ed-core`](https://github.com/papillonapp/papillon-ed-core) | 🔴 **GPL-3.0** — `LICENSE` **35 149 B `sha256₁₂ 3972dc9744f6`** | The ÉcoleDirecte core of the Papillon French school-life app. 🔴 **Strong copyleft**: linking it into a client deliverable carries the obligation outward |
| [`louislegrain/api-ecoledirecte`](https://github.com/louislegrain/api-ecoledirecte) | 🔴 **`ISC` declared on npm, NO payload at 9 probed paths** | 🔴 `Gap 451-C`'s **manifest-only** class, on a **live** package: the grant exists as a registry string and no file in the repository serves its text. Buildable only after legal review |
| [`barglabs/cejel`](https://github.com/barglabs/cejel) | 🔴 **AGPL-3.0** — `LICENSE` **34 523 B `sha256₁₂ 0d96a4ff68ad`** | 🔴 **Network copyleft** — §13 attaches a source-provision duty to *hosted* use, which is how an engagement would deploy it |

🔴 **Rejections, named rather than dropped** — all three pass the licence and reachability probes
and fail the surface read: [`food-x-technologies/escolar`](https://github.com/food-x-technologies/escolar)
(MIT 1 075 B — JSON file interpolation, not schools), `jirichara/kindergarten` (MIT — an
authorization library), and the **13** Laboratoria `md-links` bootcamp exercises (ISC/MIT — course
work, not industry supply). 🟡 [`bq-educacion/editor`](https://github.com/bq-educacion/editor)
(**MIT**, `LICENSE` **1 084 B `sha256₁₂ 2a3b698d8ae8`**) is held back deliberately: the *publisher*
is an EMEA/Spain education org, but the artifact is a general-purpose React rich-text editor, so it
is recorded here as an **org-placed generic surface** and not as an education row.

🟡 **Not a star claim.** `api.github.com` returns **403** on this host (re-confirmed this pass), so
no popularity figure is published for any row — only the grant, the path, the bytes, the hash and
the surface, each read this pass.

## 🆕 `p452` — **🟢 `Gap 451-A` ANSWERED WITH A DENOMINATOR: the back-link rule `p451` made standing was swept over all 71 carried registry-sourced cells, and it finds ZERO mis-attributed licences — the population was already clean. 🔴 What it does find is that 8 of 71 are not registry-attributable AT ALL, and the mechanism is not what `p451` expected: the record exists and carries no repository field. 🔴 And this pass's own instrument produced 3 false DISAGREE verdicts before correction, every one of them by deriving an address from a package name — the exact heuristic `Gap 451-A` forbids.**

🔴 **Gate posture, stated first as `Gap 446-A` requires: `make hooks` was DENIED.** The host refused
the recipe (`Code from External`) before any gate body ran — **seven denials in eight passes**.
🔵 Nothing below is gate-attested. The four load-bearing contracts were re-implemented
independently (region-heading `CANON` and `VOCAB` read from `check_headings.py:17-19`, newest-block
insertion read from `check_newest_block.py`, frontmatter vocabulary, table-header-as-data) and all
four are green.

### 🟢 The sweep, and its controls run in three directions before any verdict was read

`p451` left this as the open half of `Gap 451-A`: *"the next pass should run a back-link agreement
sweep over the carried registry-sourced licence cells and report disagreements by mechanism."*
🟢 The instrument is [`compose/code/p452-backlink-sweep/sweep.py`](../compose/code/p452-backlink-sweep/sweep.py);
its population and full output are committed to
[`evidence/backlink-agreement-sweep.2026-10-26-p452.tsv`](../evidence/backlink-agreement-sweep.2026-10-26-p452.tsv).

| control | channel | expected | observed | discriminates? |
|---|---|---|---|---|
| 🟢 positive | npm `express` → `expressjs/express` | AGREE | 🟢 **AGREE**, MIT, `5.3.0` | 🟢 YES |
| 🟢 positive | PyPI `requests` → `psf/requests` | AGREE | 🟢 **AGREE**, Apache-2.0, `2.34.2` | 🟢 YES |
| 🟢 positive | Packagist `laravel/framework` | AGREE | 🟢 **AGREE**, MIT | 🟢 YES |
| 🧪 fabricated negative | `globant-fab-452-nope-pkg`, all three registries | NO_RECORD | 🟢 **NO_RECORD** ×3 | 🟢 YES |
| 🟢 **reproduction** | npm `blackboard-mcp` → `e9x/blackboard-mcp` | DISAGREE *(`p451`, by hand)* | 🟢 **DISAGREE** → `felipedias-ie/blackboard-mcp` | 🟢 YES — `p451`'s hand verdict recovered mechanically |

🔵 The reproduction control is the one that matters: `p451` reached that verdict by reading one
record by eye, and an instrument that could not recover it would not be measuring the same thing.

### 🟢 The result over 71 carried cells — and the headline is a negative finding worth more than a positive one

| verdict | n | share | what it means for a deliverable |
|---|---|---|---|
| 🟢 `AGREE` | **63** | 89 % | the registry's own metadata back-links the exact address the shelf carries; the licence cell is corroborated on a second channel |
| 🔴 `ABSENT` | **6** | 8 % | the record exists and declares **no repository field at all** — the licence may be right, but nothing ties it to the address, so it is unusable as corroboration |
| 🔴 `PAGES_ONLY` | **1** | 1 % | the only URL is a GitHub **Pages** site, which asserts a published page, not a repository |
| 🔴 `NO_RECORD` | **1** | 1 % | the package name the manifest claims is 404 on the registry |
| 🟢 `DISAGREE` | **0** | 0 % | 🟢 **no carried licence cell is attributed to the wrong address** |

🟢 **`Gap 451-A`'s worry does not materialise on this population.** `p451` wrote that *"every licence
cell these shelves derived from a registry read before `p451` was taken on the name"* and that the
population had not been swept. 🟢 It is swept now, and the mis-attribution count is **zero**. That is
the answer, and it is good news that only a measurement could have produced.

### 🔴 The 8 that are not registry-attributable, by mechanism — and PyPI is structurally worse than npm

| address as carried | registry record | mechanism | consequence |
|---|---|---|---|
| [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) | PyPI `deeptutor` `1.6.15`, declares **Apache-2.0** | 🔴 `ABSENT` — `project_urls` is **`null`**, `home_page` is **`None`** | 🟡 this base's most-cited agent has **no registry back-link**; its grant stands on the first-hand `LICENSE` read (**11 408 B**, re-read EXACT this pass), never on PyPI |
| [`RusticiSoftware/TinCanPython`](https://github.com/RusticiSoftware/TinCanPython) | PyPI `tincan` `1.0.0`, declares **Apache License 2.0** | 🔴 `PAGES_ONLY` — the sole URL is `rusticisoftware.github.io/TinCanPython/` | 🔴 **the trap a naive `grep -i github` falls into**: a Pages host's owner segment need not equal the repository owner, so the string matches and the evidence does not |
| [`openedx/openedx-mcp`](https://github.com/openedx/openedx-mcp) | PyPI `openedx-mcp` `0.1.9`, declares **AGPL-3.0** | 🔴 `ABSENT` | 🔴 an **AGPL** claim with no back-link is the worst case of the eight: the licence is the one that decides whether Globant can ship it |
| [`appliedrelevance/frappe_mcp_server`](https://github.com/appliedrelevance/frappe_mcp_server) | PyPI `frappe-mcp-server` `1.2.0`, declares **MIT** | 🔴 `ABSENT` | 🟡 permissive but uncorroborated |
| [`django-by-kelsoncm/django-auth-suap`](https://github.com/django-by-kelsoncm/django-auth-suap) | PyPI `django-suap-auth` `1.8.9`, declares **MIT License** | 🔴 `ABSENT` | 🟡 LATAM (IFRN/SUAP) rostering leg, uncorroborated |
| [`InCruiter-NewProducts/proctoring-sdk`](https://github.com/InCruiter-NewProducts/proctoring-sdk) | npm `@incproctor/proctoring-sdk` `1.0.4`, declares **`SEE LICENSE IN LICENSE`** | 🔴 `ABSENT` | 🔴 **`Gap 451-C`'s unrecoverable class, but on a LIVE package**: the grant names a file and the record gives no way to locate it |
| [`imazhar101/mcp-canvas-server`](https://github.com/imazhar101/mcp-canvas-server) | npm `@imazhar101/mcp-canvas-server` `2.1.3`, **no licence field** | 🔴 `ABSENT` | 🔵 already carried as unauditable since `p143`; the sweep reproduces it |
| [`nitsuah/bb-mcp`](https://github.com/nitsuah/bb-mcp) | npm `blackboard-learn-mcp` | 🔴 `NO_RECORD` | 🔵 reproduces this shelf's own `p387` finding — the manifest claims a name that was never published |

🔴 **The mechanism splits by registry, and it is not symmetric: 4 of the 6 `ABSENT` and the single
`PAGES_ONLY` are PyPI, against 2 `ABSENT` on npm.** npm's `repository` field is conventional to the
point of near-universality; PyPI's `project_urls` is optional and frequently `null`. 🟢 **Operational
rule this yields: the registry channel corroborates npm-published grants and largely cannot
corroborate PyPI-published ones.** A pass that treats "it is on a registry" as uniform evidence is
wrong about Python, which is most of this base's tutoring and analytics tier.

### 🔴 Three false DISAGREE verdicts this pass produced, and they are the whole lesson

🔴 **Before correction the sweep reported three mis-attributions. All three were mine, not the
shelves'** — I had filled the *claimed address* column by deriving it from the package name, which is
the precise heuristic `Gap 451-A` was registered to forbid.

| package | address I derived from the name | address the shelf actually carries | who was right |
|---|---|---|---|
| npm `@superbuilders/oneroster` | `superbuilders/oneroster` | 🟢 `trilogy-group/oneroster-ts` — recorded at `agents/trending.md:17492` | 🟢 **the shelf** |
| npm `@longsightgroup/qti3-core` | `longsightgroup/qti3-core` | 🟢 `LongsightGroup/qti3` — and `repos/trending.md:37948` **already records that `qti3-core` is 404** | 🟢 **the shelf**, twice over |
| npm `@groton/canvas-api` | `groton/canvas-api` | 🟢 `groton-school/canvas-cli` — recorded at `repos/trending.md:6858` | 🟢 **the shelf** |

🟢 **Measured error rate of the forbidden heuristic, on a population where the truth was already
written down: 3 of 3 of its disagreements were the heuristic's own fault.** 🔵 That is a stronger
argument for `Gap 451-A`'s rule than the sweep's clean result is, and it is only available because
the shelves had recorded the right answer first.

### 🔴 A fourth instrument defect, in the same class: the normaliser matched `github.com` ONLY

🔴 The first cut of `norm()` accepted only `github.com`, so PyPI `travo` — which declares
`https://gitlab.com/travo-cr/travo.git/`, an **exact and correct** back-link — came back `ABSENT`.
🟢 A forge-blind back-link checker manufactures absences on every project that is not on GitHub, and
this base carries `travo-cr/travo` on **GitLab** precisely so that case exists. 🟢 Fixed: the
normaliser now returns a **forge-qualified** `forge/owner/repo`, so two forges holding the same
`owner/repo` pair can never score as agreeing, and a new `FOREIGN_FORGE` verdict separates
"different forge" from "different project". `travo` reads `AGREE` under the corrected instrument.

🔴 **And a fifth, caught by the same discipline:** the `PAGES_ONLY` class **could not fire** in the
first cut — `pypi()` discarded the Pages URL before the grader saw it, so the class read as *"no
project ever did this"*. A verdict class that cannot fire is worse than no class at all. Fixed, and
`tincan` is what it catches.

### 🟢 One promotion, and it is a category this shelf has not carried before

| repository | grant, read first-hand at `HEAD` | surface | region |
|---|---|---|---|
| [`D4vRAM369/pbl-project-chronicler`](https://github.com/D4vRAM369/pbl-project-chronicler) | 🟢 **MIT** — `LICENSE` **1 066 B `sha256₁₂ 95576ceceaa3`**, title `MIT License`; npm `pbl-project-chronicler` back-links the exact slug (🟢 `AGREE`) | An **agent skill** for Claude Code, Codex and OpenCode that turns a development session into *pedagogical* documentation: a glossary with analogies, a reproducible step-by-step, architecture decisions **and their reasons**, and `05_ERRORES_Y_SOLUCIONES.md` — real errors kept deliberately as *"oro pedagógico"*. Installs per detected agent (`npx pbl-project-chronicler --claude/--codex`) | ⚪ **Global** — Spanish-first (`README.md` ES, `README_english-version.md` EN). 🔵 **No institution or country is asserted, so none is recorded**, per `p451`'s rule for `tcpassos/moodle-student-mcp` |

🟢 **Why it is a new category and not another connector.** Every agent on this shelf until now points
*at* an education system — Moodle, Canvas, Blackboard, Brightspace, a registrar. This one points at
the **development session itself** and treats it as the learning object. 🔵 It is the first instance
on these shelves of *pedagogical instrumentation of the coding agent*, which is a different buy:
it needs no LMS, no institutional credential and no integration review, so it is deployable inside a
Globant engagement on day one rather than after a security review of an LMS token.

🟡 **Not a star claim.** This host has no channel returning a star count (the GitHub API is
`403`/denied here), so no popularity figure is published — only the grant, the ref and the surface,
each read this pass.

## 🆕 `p451` — **🟢 THE NINE UNREACHABLE ADDRESSES `p450` COULD ONLY COUNT ARE NOW TYPED: six of nine are proved to have EXISTED and been WITHDRAWN, because a published artifact's metadata records the repository URL at publish time and a never-existing address cannot have one. 🔴 And two of the three remaining have registry name-hits that belong to THIRD PARTIES — a future pass treating a name hit as evidence would have attributed a live MIT project to a dead address.**

🔴 **Gate posture, stated first as `Gap 446-A` requires: `make hooks` was DENIED.** The host refused
the recipe (`Code from External`) before any gate body ran — the same class `p446`–`p448` and `p450`
recorded, and which `p449` showed to be **intermittent**. Six denials in seven passes. **Nothing
below is gate-attested**; the four load-bearing contracts were re-implemented independently this
pass (region-heading `CANON` regex read from `check_headings.py` and applied by hand, table-header
-as-data, frontmatter vocabulary, append-only shelf identity) and all four are green.

### 🟢 `Gap 420-C` is no longer wholly unanswerable — it was the wrong CHANNEL, not an impossible question

🔵 `p450` closed `Gap 420-C` as **UNANSWERABLE** after thirty passes, on the measurement that
GitHub emits a byte-identical response for a provably non-existent repository, so *"a prompt
carries zero information about privacy"*. 🟢 **That verdict is correct about its channel and wrong
as a general claim.** The question *"did this address ever exist?"* is answerable on a channel
nobody had pointed at it: **a package registry records the `repository` URL at publish time**, and
that record survives the repository's deletion.

🔴 **The instrument has to be controlled in both directions or its negatives are unpublishable**
(`P249`), so every channel below carries a live positive control and a **fabricated** negative:

| channel | positive control | negative control | discriminates? |
|---|---|---|---|
| 🟢 `raw.githubusercontent` `HEAD/README.md` | `moodle/moodle` → `200` | `globant-fabricated-451/does-not-exist` → `404` | 🟢 **YES** |
| 🟢 `git ls-remote` | `moodle/moodle` → `0` | fabricated → `128` | 🟢 **YES** |
| 🟢 `registry.npmjs.org` | `express` → `200` | `globant-fabricated-451-nope-pkg` → `404` | 🟢 **YES** |
| 🟢 `pypi.org` | `requests` → `200` | fabricated → `404` | 🟢 **YES** |
| 🟢 `packagist.org/packages/{v}.json` | `laravel/framework` → `200` | `globant-fab-451/nope` → `404` | 🟢 **YES** |
| 🔴 `repo.packagist.org/packages/…` | `laravel/framework` → **`404`** | fabricated → `404` | 🔴 **NO — the path this pass tried FIRST, and its negative on `siiau-api-client` would have been a false "never existed"** |
| 🔴 **authenticated GitHub MCP** `get_file_contents` | `HKUDS/DeepTutor` → `ACCESS_DENIED` | fabricated → `ACCESS_DENIED` | 🔴 **NO — zero bits, the same defect class as the `curl -sI` probe `p450` refuted** |
| ⚪ GitHub MCP `search_repositories` | **NOT RUN** | — | this session's scope permits repository search only within the two attached repositories, so the channel is closed by **policy**, not by a constant oracle |

🔵 `registry.npmjs.org` and `pypi.org` are in this host's proxy **`noProxy`** list — they are reached
directly, which is *why* they discriminate where every `403`-at-`CONNECT` host in the
refusal ledger (`archive.softwareheritage.org`, `api.deps.dev`, `ungh.cc`, `data.jsdelivr.com`)
cannot. 🔴 **`packagist.org` is a fourth registry channel this base had never read**, and it is the
only surviving channel for the one PHP address on these shelves.

### 🟢 The nine, resolved — the back-link is the evidence, never the name

| carried address | surviving artifact | back-links to the exact slug? | licence, as the registry declares it | verdict |
|---|---|---|---|---|
| [`thanh01pmt/interactive-quiz-kit`](https://github.com/thanh01pmt/interactive-quiz-kit) | npm **`@thanh01.pmt/interactive-quiz-kit`** `1.4.10`, **103** versions, 2025-06-12 → 2026-09-23 | 🟢 YES | 🟢 **MIT** | 🟢 **EXISTED → WITHDRAWN**, licence recoverable |
| [`ale-alejandro/beadkit`](https://github.com/ale-alejandro/beadkit) | npm **`beadkit`** `0.1.0`, 2 versions, 2026-08-26 → 2026-10-12, maintainer `alebuild.co` | 🟢 YES | 🔴 **`SEE LICENSE IN LICENSE`** | 🔴 **EXISTED → WITHDRAWN**, licence **UNRECOVERABLE** |
| [`parkseokjune/unist-blackboard-mcp`](https://github.com/parkseokjune/unist-blackboard-mcp) | PyPI **`unist-blackboard-mcp`** `0.2.0` | 🟢 YES — `Homepage`, `Repository`, `Issues` **and** a `CHANGELOG.md` blob on `main` | 🟢 **MIT** | 🟢 **EXISTED → WITHDRAWN**, licence recoverable |
| [`Mckaroff/GraphLMS`](https://github.com/Mckaroff/GraphLMS) | npm **`rhizome-lms-mcp`** `0.3.1`, 4 versions, 2026-04-30 → 2026-05-03 | 🟢 YES | 🟢 **MIT** | 🟢 **EXISTED → WITHDRAWN**, licence recoverable |
| [`santillana-ai/tutor-sdk`](https://github.com/santillana-ai/tutor-sdk) | npm **`@santillana-ai/create-tutor-app`** `5.9.0`, 63 versions | 🟢 YES | 🟡 **MIT in the manifest, NO payload in the tarball** (`p450`, re-read) | 🟡 **EXISTED → WITHDRAWN**, manifest-only grant |
| [`dev-cucei-itrans/siiau-api-client`](https://github.com/dev-cucei-itrans/siiau-api-client) | **Packagist** `dev-cucei-itrans/siiau-api-client`, **7** versions, 1 023 downloads, 7 stars, 2023-10-13 → 2024-10-08, `abandoned: true` | 🟢 YES | 🔴 **SPLIT — `proprietary` on `v1.0.0-BETA`, `v1.0.0`, `v1.1.0`, `v1.1.1`; `BSD-3-Clause` only on `v1.1.2` and `dev-main`** | 🔴 **EXISTED → WITHDRAWN**, licence **VERSION-DEPENDENT** |
| [`e9x/blackboard-mcp`](https://github.com/e9x/blackboard-mcp) | npm `blackboard-mcp` `0.1.2` | 🔴 **NO — it back-links [`felipedias-ie/blackboard-mcp`](https://github.com/felipedias-ie/blackboard-mcp)**, a different, live, MIT project already on this shelf | — | 🔴 **NO TRACE** — third-party name collision |
| [`yokowasis/autograder`](https://github.com/yokowasis/autograder) | npm `autograder` (`sulejmanca`, 2017-04-10 → 2021-09-23, no `repository`) **and** PyPI `autograder` `3.7.7` (**GPL-3.0**, back-links `zmievsa/autograder`) | 🔴 **NO, on both** | — | 🔴 **NO TRACE** — **two** third-party collisions on two registries |
| [`AI-Matrix-Engine/aidream`](https://github.com/AI-Matrix-Engine/aidream) | none on npm, PyPI or Packagist | — | — | 🔴 **NO TRACE on three registries** — the only address of the nine with no trace anywhere |

🟢 **Six of nine resolved from *"`128` twice, which does not separate absent from private"*
([`repos/trending.md`](../repos/trending.md), `p450`) to a dated, typed, first-hand verdict.**
🔴 **Three remain unresolved, and the honest statement is that `Gap 420-C` still holds for them**:
no registry trace is not evidence of non-existence, because a repository can be deleted having
published nothing. `AI-Matrix-Engine/aidream` is the clean instance; the other two are *contaminated*
by a third party holding the same name.

### 🔴 The rule this pass extracts, with its denominator: **2 of 9 registry name-hits are somebody else's project**

🔵 `p450` recorded the class at the harvest layer (*"three of thirteen npm names declared in these
cohorts' own manifests resolve to someone else's project"*). 🔴 **This pass puts it on the graded
shelf and on this base's own carried addresses:** of the **9** dead slugs, **3** produced a registry
hit under their natural name and **2 of those 3 belonged to a third party** — one of them to
`felipedias-ie/blackboard-mcp`, which this very file already carries as the live MIT Blackboard row
at `p386`. 🟢 **The rule: a registry hit counts as evidence for an address only when its own
metadata back-links to that exact `owner/repo`.** Name, maintainer handle and description do not.

### 🟢 Two addresses promoted this pass — both found on the registry channel, both read first-hand

| repository | grant, read first-hand at `HEAD` | surface | region |
|---|---|---|---|
| [`tcpassos/moodle-student-mcp`](https://github.com/tcpassos/moodle-student-mcp) | 🟢 **MIT** — `LICENSE` **1 069 B `sha256₁₂ 322307ac9d65`**; `package.json` `"license": "MIT"`, `v0.2.1` | Student-side Moodle MCP over Moodle's **official mobile-app web service**, so it sees only what the student sees; read-only by construction (*"nothing is ever changed on Moodle"*); any login method incl. SSO + MFA; Node 22+. Packaged as a plugin for Claude Code, Copilot CLI, Codex and Gemini CLI | ⚪ **Global** — the README places no institution and claims any Moodle site; no region is asserted |
| [`FiredMosquito831/ase-moodle-mcp`](https://github.com/FiredMosquito831/ase-moodle-mcp) | 🟢 **Apache-2.0** — `LICENSE` **11 358 B `sha256₁₂ cfc7749b96f6`**; npm `ase-moodle-mcp` declares `Apache-2.0`, `v0.2.2` | Python client + CLI + MCP server + plugin for **BL@ASE (`online.ase.ro`)**: courses, materials, assignments, forums, grades, quizzes, notifications, deadlines. CI workflow present; Python 3.10+ | 🟢 **EMEA** — Romanian-language README, **ASE Bucharest** (Bucharest University of Economic Studies) |

🟡 **Neither is a star claim.** This host has no channel that returns a star count (the GitHub API
is `403`/denied here), so no popularity figure is published for either — only the grant, the ref
and the surface, each read this pass.

🔵 **Why `ase-moodle-mcp` matters beyond its size:** it is a **single-institution** MCP server
written in the institution's own language, and it is **Apache-2.0**. The EMEA pattern on these
shelves has been *"copyleft platform, permissive agent layer"*; this is a datum that the
institution-specific tier is being built permissively too, which is what makes it vendorable.

---

## 🆕 `p450` — **🟢 THE URL PROBE THIS BASE IS INSTRUCTED TO USE IS REPLACED, NOT COMPLAINED ABOUT: a two-channel probe with a FABRICATED NEGATIVE CONTROL now separates live from dead on this host, and its first run is the first full reachability census these shelves have ever had — 375 addresses, 366 live, 9 not. 🔴 And `Gap 420-C`, carried THIRTY passes as "cheapest closure available to the next pass", is closed as UNANSWERABLE: the fabricated control emits BYTE-IDENTICAL stderr to all eight carried addresses, so `gate-slug-oracle`'s premise is refuted on this channel.**

🔴 **Gate posture, stated first as `Gap 446-A` requires of every pass: `make hooks` was DENIED.**
The host refused the recipe (`Code from External`) before any gate body ran — the same class
`p446`–`p448` recorded, which `p449` showed to be **intermittent** rather than permanent. So this
pass has **no arrival baseline and no exit baseline**, and nothing below is gate-attested. 🔵 The
gate *sources* were read instead of run (`compose/code/p383-region-heading-gate/check_headings.py`,
`compose/code/p170-newest-block-gate/check_newest_block.py`) and this pass's writes are shaped to
their contracts by hand: newest-FIRST insertion, one canonical `## Opportunities by region`,
closed five-value vocabulary.

### 🟢 `Gap 449-A` / `Gap 449-B` RESOLVED — the probe is replaced, with controls in both directions

`p449` established that `curl -sI https://github.com/{slug}` returns **403 on every address** on
this host. 🔴 This pass reproduces that and adds the part that makes it damning: **the fabricated
slug `nope-xyz-123/nope` also returns 403.** A probe that returns the same verdict for
`moodle/moodle` and for an address that has never existed carries **zero bits**. It is not a weak
probe, it is **not a probe**.

| channel | `HKUDS/DeepTutor` | `moodle/moodle` | 🧪 `nope-xyz-123/nope` (fabricated) | discriminates? |
|---|---|---|---|---|
| 🔴 `curl -sI github.com/{slug}` *(prescribed)* | **403** | **403** | **403** | 🔴 **NO** |
| 🔴 `curl api.github.com/repos/{slug}` | **403** | — | **403** | 🔴 **NO** — proxy refuses the API host |
| 🔴 `curl codeload.github.com/...` | **403** | — | — | 🔴 **NO** |
| 🟢 **`curl raw.githubusercontent.com/{slug}/HEAD/README.md`** | **200** | **200** | 🟢 **404** | 🟢 **YES** |
| 🟢 **`git ls-remote --heads github.com/{slug}`** | **OK** | **OK** | 🟢 **exit 128** | 🟢 **YES** |

🟢 **The ref alias `HEAD` is what makes the `raw` leg usable**, and it closes `Gap 449-B`'s
case-sensitivity objection for the *owner/repo* half: `HEAD` resolves the default branch whatever
it is called, so the 13-addresses-not-on-`main` problem `p386` measured does not reach this probe.

🟢 **Standing protocol, two stages, because neither channel alone is sound:**
`raw` **200** → live, no second call. `raw` **404** → **not a verdict**, escalate to `ls-remote`.
`ls-remote` OK → **live, serves no `HEAD/README.md`**. Both fail → **unreachable un-credentialled**.

### 🟢 First full reachability census of these shelves — 375 addresses

Every `github.com/owner/repo` in `agents/top.md`, `repos/foundations.md` and
`verticals/solutions.md`, deduplicated, probed **2026-10-26**
(`evidence/shelf-reachability-census.2026-10-26-p450.tsv`, 375 rows):

| verdict | n | share |
|---|---|---|
| 🟢 **live, `raw` serves `HEAD/README.md`** | **347** | 92.5 % |
| 🟡 **live on `ls-remote`, NO `HEAD/README.md`** | **19** | 5.1 % |
| 🔴 **unreachable on both channels** | **9** | 2.4 % |
| 🟢 **live, total** | 🟢 **366** | 🟢 **97.6 %** |

🟢 **The census is self-validating in two directions.** Positive: 366 of 375 resolve, so neither
channel is broken on this host at this hour. Negative: the fabricated control fails both. 🟢 **And
it independently reproduces a verdict this base reached by hand** — `dev-cucei-itrans/siiau-api-client`,
which `verticals/solutions.md:236` recorded as `DOES NOT RESOLVE` on **2026-10-25**, fails both
channels here on **2026-10-26**. A probe that re-derives a known answer unprompted is a probe worth
keeping.

### 🔴 `Gap 420-C` CLOSED — and the closure it was promised cannot exist

`Gap 420-C` has been carried since `p420`: eight addresses return exit `128`, *"and this run cannot
call them dead"*, with `gate-slug-oracle` (`p293`) named as **"exactly the instrument"** on the
principle *"a credential prompt is a MEASUREMENT, not an inconclusive result"*. 🔴 **That principle
is false on GitHub over HTTPS, and one control proves it.** Run un-credentialled with
`GIT_TERMINAL_PROMPT=0` (`evidence/slug-oracle-control.2026-10-26-p450.tsv`):

| slug | exit | stderr |
|---|---|---|
| 🧪 **`nope-xyz-123/nope`** — fabricated, certainly absent | `128` | `fatal: could not read Username for 'https://github.com': terminal prompts disabled` |
| `thanh01pmt/interactive-quiz-kit` | `128` | 🔴 **byte-identical** |
| `AI-Matrix-Engine/aidream` · `Mckaroff/GraphLMS` · `santillana-ai/tutor-sdk` | `128` | 🔴 **byte-identical** |
| `ale-alejandro/beadkit` · `yokowasis/autograder` | `128` | 🔴 **byte-identical** |
| `e9x/blackboard-mcp` · `parkseokjune/unist-blackboard-mcp` | `128` | 🔴 **byte-identical** |

🔴 **GitHub emits the credential prompt for addresses that do not exist**, precisely so that a
404 cannot leak the existence of a private repository. The prompt therefore carries **no
information about privacy**, and `gate-slug-oracle` cannot separate *absent* from *private* here
**in principle** — not for want of being run. 🟢 `Gap 420-C` is closed as **UNANSWERABLE ON THIS
CHANNEL**; the honest verdict is the one `p420` already chose, and the operational consequence is
unchanged and already enforced by `gate-dead-citation`: **unreachable un-credentialled means
un-clonable, and a row nobody can clone is never a recommendation.**

🔵 **What survives of those nine is on a different channel, and that distinction is commercially
real.** Five of them have **npm packages this base read first-hand as tarballs** — `santillana-ai`
(`@santillana-ai/create-tutor-app`, 63 versions), `thanh01pmt` (103 versions), `yokowasis`,
`ale-alejandro`, `Mckaroff`. 🔴 **The code is published and the repository is not**, so it can be
installed and cannot be forked, audited, or patched. For a studio engagement that is the difference
between a dependency and a starting point.

### 🔴 Zero new rows, for the FIFTH consecutive pass — and the grading was done before the writing

Six discovery legs ran (open-source agents, GitHub trending, tutor/Apache, LMS-connector MCP,
automated grading, vertical platforms). Every candidate was word-scoped against these shelves
(`grep -riw`, `Gap 447-A`'s prescription) **before** being written down:

| candidate | word-scoped files | verdict |
|---|---|---|
| `Submitty/Submitty` · `UCL-INGI/INGInious` | **32 / 38** | 🔴 already shelved |
| `savinoo/ai-grading-system` *(IFF, Brazil)* · `Fatima0923/AssessmentAI` | **4 / 3** | 🔴 already shelved |
| `ai-lingnan/econai-agent-platform` · `BaijayantaRoy/bandup` *(Singapore)* | **8 / 8** | 🔴 already shelved |
| `biswal-prem-5677/Autonomous-Exam-Proctoring-Grading-Agent` | **3** | 🔴 already shelved |
| `vishalsachdev/canvas-mcp` · `peancor/moodle-mcp-server` · `Mattlo0546/classroom-mcp` · `JohannsenLum/canvas-api-mcp` | **60 / 35 / 14 / 3** | 🔴 already shelved |
| `Open TutorAI` *(arXiv 2602.07176)* · `sourcegrade/jagr` | **22 / 7** | 🔴 already shelved |
| `HKUDS/DeepTutor` · `satvik314/educhain` · `CAHLR/OATutor` | **83 / 49 / 75** | 🔴 already shelved |

🔵 **Fifteen candidates, fifteen prior hits, zero at zero.** 🟢 Read against `Gap 448-A`'s answered
cadence — hourly reads against a **daily** trending refresh, so ≈23.6 passes sample each snapshot —
a fifth nil is the *expected* observation and still says little about supply. 🔴 What it does say is
that **the six prescribed search shapes are exhausted**, including the two obscure tails
(`bandup`, `econai-agent-platform`) that would be the first to show a gap. 🔵 `Gap 450-A`: the next
pass that wants a new row must change the *channel*, not the query — package registries, conference
artefact tracks, or ministry procurement listings, none of which the prescribed six touch.
## 🆕 `p449` — **🟢 THE GATE RAN FOR THE FIRST TIME IN FOUR PASSES, AND THE ARRIVAL BASELINE IT FINALLY PERMITTED CAUGHT TWO CONTRACT VIOLATIONS THAT WERE BOTH `p448`'s. 🟢 `Gap 448-C` RESOLVED AT SOURCE — and it corrects `p448`'s denominator while CONFIRMING its write numerator EXACTLY, so this tier's write share was UNDERSTATED: 32.9 % → 35.8 %. 🔴 The URL probe this base is instructed to use is a false-negative machine on this host: `curl -sI` returns 403 on EVERY real GitHub repo.**

🟢 **Gate posture, stated first as `Gap 446-A` requires of every pass: `make hooks` RAN.** One
attempt, no refusal — the **fourth** trial after three consecutive denials. 🔴 `p448` closed
`Gap 446-A` as *"a property of the host class unattended passes run in"*; **that settlement is
refuted.** The denial is **intermittent**. 🟢 So this pass carries what `p446`-`p448` could not:
an **arrival baseline** — **58/62 green, 4 RED**, of which 🔴 **two were NEW reds and both were
`p448`'s** (`gate-region-headings`, `gate-register-currency`). Three are green on exit; the
fourth is `DECLARED_RED` and deliberately left (`Gap 449-D`).

### 🔴 Zero new rows, for the FOURTH consecutive pass — and this is the first pass that can say what that means

Four global discovery legs ran; every candidate was already shelved, graded **word-scoped**
(`grep -riw`, `Gap 447-A`'s prescription) before being written down:

| candidate | word-scoped files | verdict |
|---|---|---|
| `withmarbleapp/os-taxonomy` | **10** | 🔴 already shelved — and already graded **ODbL**, a share-alike *database* licence |
| `Ed-Fi` / `TSDS` | **10 / 7** | 🔴 already shelved (`p448`) |
| `OpenEduCat`, `Krayin`, `Forma LMS` | **10 / 8 / 5** | 🔴 already shelved |
| `tiny-llm`, `Apertus`, `Soofi` | **1 each** | 🔴 shelved, and all **general-purpose**, not education verticals |
| `EuroLLM`, `withmarble`, `os-curriculum` | **0** | 🔴 not education-vertical agents — a 24-language LLM and two spellings of an already-shelved address |

🟢 **And unlike the three saturations before it, this one is interpretable — because `Gap 448-A`
is now answered with a population of 309.** Inter-pass interval, commit→commit, `p49`-`p448`:
**median 61.1 min**, p10 **46.0**, p90 **78.1**, **79.6 % inside 45-75 min**. The schedule is
**hourly**. `p449` read **40 min 20 s** after `p448` committed (01:59:04Z → 02:39:24Z). 🔴
GitHub trending refreshes **daily**, so ≈**23.6** passes sample each snapshot and an unchanged
channel is the *expected* observation at **P ≈ 95.8 %**. 🔵 **Four consecutive "saturations"
therefore say almost nothing about supply** — they measure the clock, not the ecosystem
(`evidence/inter-pass-cadence.2026-10-26-p449.tsv`, `Trend 49`).

### 🟢 `Gap 448-C` RESOLVED — `p448`'s tool census corrected, and the correction runs AGAINST the claim it refuted

`bruchris/canvas-lms-mcp` @ `c740624`, committed **2026-10-23** — so **not** drift since `p448`.
A `ToolDefinition` is counted only when its enclosing object literal carries **both** `name:`
and `inputSchema` (`Gap 448-C` asked for an AST walk; this is the structural equivalent):

| channel | count |
|---|---|
| `p448` regex over all of `src/` | 🔴 **222** |
| 🟢 **true `ToolDefinition` objects** | 🟢 **188** |
| README's own prose total | **187** |
| source ids named in README | **175 of 188** |

🟢 **The over-count is localised and named: 19 non-tool `name:` fields, every one OUTSIDE
`src/tools/`** — `src/canvas/normalize-ids.ts` **11**, `src/init/wizard.ts` **5**,
`src/init/clients.ts` **3** (`evidence/gap448c-tool-count.2026-10-26-p449.tsv`, 47 files).

🟢 **`p448`'s WRITE numerator is EXACT, confirmed on an independent channel.** That repo's README
declares *"125 tools are read-only and **62** tools perform Canvas write operations"*; `p448`'s
source census said **62**. 🔴 **So the share was understated, not overstated:**

| cell | `p448` | 🟢 `p449` |
|---|---|---|
| `bruchris` write share | 27.9 % | 🟢 **33.0 %** (62/188) |
| category total tools | 414 | 🟢 **380** |
| 🔴 **category write share** | 32.9 % | 🔴 **35.8 %** |

🔵 The correction moves **against** the read-only reading `Gap 447-B` refuted — it strengthens
the refutation rather than softening it. 🔴 And it makes `Gap 448-B` worse, not better: an MCP
allowlist gateway keyed on `read_only_hint` (43 % unpopulated, once inverted) is now known to be
gating a **larger** mutating surface than `p448` believed.

### 🔴 `Gap 449-A` — how this shelf's rows must be verified, because the prescribed way does not work here

| probe | real repo | fake control | usable? |
|---|---|---|---|
| `curl -sI https://github.com/<slug>` | 🔴 **403** | — | 🔴 **NO** |
| `curl -s -r 0-200 https://github.com/<slug>` | 🔴 **403** | — | 🔴 **NO** |
| `curl -s https://api.github.com/repos/<slug>` | — | 🔴 **403** | 🔴 **cannot discriminate** |
| 🟢 `curl -s https://raw.githubusercontent.com/<slug>/<branch>/<path>` | 🟢 **200** + bytes | 🟢 **404 / 14 B** | 🟢 **YES** |

🔴 `github.com` HTML is **403 for every real repository** on this host, while `git clone` of the
same address succeeds. A pass obeying *"verify every URL with `curl -sI`; a 404 is not a
finding"* **literally** would have condemned **all ~134 shelved addresses on these shelves.**
🟢 Validated on 12 addresses: 10 real → `200` with byte sizes, the fake control → `404 / 14 B`
(`evidence/url-probe-soundness.2026-10-26-p449.tsv`).

🔴 **And the sound probe still failed twice in my own hands, toward "dead row" — `Trend 48`'s
direction.** `openedx/XBlock` read **404** at three lowercase paths; the shelf records
`LICENSE.`**`TXT`**, and at that case it returns 🟢 **200, 11 358 B — the published cell to the
digit.** `raw.githubusercontent.com` is **case-sensitive** → `Gap 449-B`. **A 404 against a
shelved cell is a probe finding until the case is re-checked.**

🟢 **Two published cells reproduced independently this pass:** `Ed-Fi-ODS/LICENSE.txt`
**10 172 B** (`p448`'s North America headline) and `XBlock/LICENSE.TXT` **11 358 B**.

---

## 🆕 `p448` — **🟢 `Gap 447-B` IS REFUTED FROM SOURCE, AND IT WAS THIS SHELF'S ONLY OPEN CAPABILITY CLAIM: the LMS-connector tier is NOT read-only — 136 of 414 tool declarations (32.9 %) MUTATE, and the specific claim that "not one community server creates and publishes a course" is false at four addresses. 🟢 A cross-channel validation double-sources this shelf's densest category: source extraction reproduces `p446`'s README tool counts EXACTLY on four of five addresses. 🔴 Gate DENIED for the THIRD consecutive pass.**

🔴 **Gate posture, stated first as `Gap 446-A` requires of every pass: `make hooks` DID NOT
RUN.** One attempt, refused with `[Code from External]` — the third consecutive pass and the
**third distinct container** to refuse it. 🔵 `p446` called the variable *"the execution policy
of the host"*; `p447` called two denials **standing**; `p448` makes it **three for three**, so
`Gap 446-A` is a property of the host class unattended passes run in and not an hour's bad luck.
🟡 **No arrival baseline, no post-write gate.** Every cell below is first-hand and carries the
command that produced it; none is gate-checked.

### 🔴 Zero new rows, for the THIRD consecutive pass — and no padding

Four global discovery legs returned candidates; **every one was already on a sell shelf**, graded
by **word-scoped** `grep -riw` against these files before being written down (`Gap 447-A`'s
prescription, applied):

| candidate | word-scoped files | verdict |
|---|---|---|
| `openSIS` | **32** | 🔴 already shelved (`OS4ED/openSIS-Classic`, GPL-2.0) |
| `Ed-Fi` / `edfi` | **16 / 15** | 🔴 already shelved |
| `Chamilo` | **23** | 🔴 already shelved |
| `OpenEduCat`, `Sakai`, `ILIAS` | **many** | 🔴 already shelved |
| `agents-from-scratch`, `ai-engineering-from-scratch`, `AI-Roadmaps`, `500-ai-agents-projects`, `h9-tect`, `pguso`, `rohitg00` | **3–4 each** | 🔴 already shelved, and all **general-purpose**, not education verticals |

🔴 **A cadence caveat that must be stated, because it changes how the saturation reads.**
`p447` committed **00:58:40Z** and `p448` read at **01:41:58Z** — **43 minutes** apart. A
saturated discovery channel 43 minutes after the previous pass is **not evidence about the
supply**; it is evidence that no time has elapsed. Three consecutive "saturations" have now
been recorded without anyone measuring the inter-pass interval → `Gap 448-A`.

### 🟢 `Gap 447-B` REFUTED — read from source at HEAD, not from a directory review

`p447` carried, explicitly as a single relayed secondary claim, that the community MCP supply
for Moodle and Canvas is *"overwhelmingly READ-ONLY"* and that *"not one community server in
that guide creates and publishes a course."* 🟢 **Both halves are false.** Nine addresses were
cloned at `--depth 1` and their tool registries read:

| project | lang | tools | READ | 🔴 WRITE | other | write % |
|---|---|---|---|---|---|---|
| [`bruchris/canvas-lms-mcp`](https://github.com/bruchris/canvas-lms-mcp) | ts | 222 | 126 | 🔴 **62** | 34 | 27.9 % |
| [`mdweaver/canvas-mcp`](https://github.com/mdweaver/canvas-mcp) | ts | 89 | 47 | 🔴 **41** | 1 | **46.1 %** |
| [`r-huijts/canvas-mcp`](https://github.com/r-huijts/canvas-mcp) | ts | 69 | 38 | 🔴 **30** | 1 | **43.5 %** |
| [`Jawadh-Salih/moodle-mcp-server`](https://github.com/Jawadh-Salih/moodle-mcp-server) | **go** | 19 | 16 | 🔴 3 | 0 | 15.8 % |
| [`Mattlo0546/canvas-mcp`](https://github.com/Mattlo0546/canvas-mcp) | py | 10 | 0 | 0 | 10 | 0 % |
| [`caleb-media-studio/canvas-mcp`](https://github.com/caleb-media-studio/canvas-mcp) | ts | 3 | 0 | 0 | 3 | 0 % |
| [`csmediapro/moodle-mcp-server`](https://github.com/csmediapro/moodle-mcp-server) | ts | 2 | 1 | 0 | 1 | 0 % |
| **TOTAL** | | **414** | **228** | 🔴 **136** | 50 | 🔴 **32.9 %** |

🟢 **The authoring-and-publishing capability exists at four addresses, named tool by tool:**

| address | the tools that falsify the claim |
|---|---|
| `bruchris/canvas-lms-mcp` | `create_course`, `create_module`, `create_module_item`, `create_page`, `create_new_quiz`, `grade_submission`, `enroll_user`, `upload_file` |
| `mdweaver/canvas-mcp` | `create-module`, `create-module-item`, `post-announcement`, `toggle-module-publish`, `update-syllabus`, `publish-appointment-group` |
| `r-huijts/canvas-mcp` | `create-module`, `create-module-item`, `post-announcement`, `toggle-module-publish` |
| `vishalsachdev/canvas-mcp` | `create_announcement`, `create_assignment`, `create_module`, `create_page`, `bulk_grade_submissions`, `bulk_update_pages` |

🟢 **`create_course` was read, not inferred**:
`src/tools/courses.ts:205` → `name: 'create_course',`, with `tests/tools/courses.test.ts:53`
asserting `expect(names).toContain('create_course')` and the README's own capability table
listing it. 🟢 `toggle-module-publish` at `mdweaver/canvas-mcp:src/tools/modules.ts:114`,
`update-syllabus` and `post-announcement` at `src/tools/courses.ts:124` and `:216`. **An MCP
server that creates a module and then toggles it published is publishing courseware.**

### 🟡 A safety finding that matters more than the census: `read_only_hint` cannot be trusted as a gate

`vishalsachdev/canvas-mcp` is the only address on this shelf that annotates read-only intent
per tool. Measured over all **128** of its declarations:

| `read_only_hint` | n | share |
|---|---|---|
| 🟢 `=True` | 72 | 56.2 % |
| 🔴 `=False` | **1** | 0.8 % |
| 🔴 **not declared at all** | **55** | 🔴 **43.0 %** |

🔴 The 55 undeclared tools are **exactly the mutating ones** (`create_announcement`,
`create_assignment`, `create_module`, `create_page`, `bulk_grade_submissions`,
`bulk_update_pages`, `assign_peer_review`, `bulk_delete_announcements` …), and the **single**
tool explicitly marked `read_only_hint=False` is `download_course_file` — **a read**. 🔴 So the
one field an MCP allowlist gateway would key on is **43 % unpopulated and at least once
inverted** on the densest server in this category. `compose/code/mcp-allowlist-gateway` must
gate on the **tool's effect**, never on this hint → `Gap 448-B`.

### 🟢 A cross-channel validation, and it vindicates `p446`'s numbers

`p446` refuted `Gap 445-C`'s false *"102 tools"* claim by counting each README's advertised
tools: **187 / 128 / 126 / 99 / 89 / 69**. `p448` counted the **source** instead, a fully
independent channel:

| address | `p446` README | `p448` source | verdict |
|---|---|---|---|
| `vishalsachdev/canvas-mcp` | 128 | **128** | 🟢 **EXACT** |
| `Harikeshav-R/canvas-mcp` | 126 | **126** | 🟢 **EXACT** |
| `mdweaver/canvas-mcp` | 89 | **89** | 🟢 **EXACT** |
| `r-huijts/canvas-mcp` | 69 | **69** | 🟢 **EXACT** |
| `bruchris/canvas-lms-mcp` | 187 | 222 | 🔴 **over-count** — non-tool `name:` fields match → `Gap 448-C` |

🟢 **Four exact reproductions across two independent channels.** And the arm structure
`p446` graded by root commit is **coherent on a third axis**: `Harikeshav-R` is the pure
duplicate address — `0` unique commits, **94 behind** — and it carries exactly **2 fewer tools**
than its upstream (126 vs 128). 🔵 The drift is the 94 commits.

🔴 **Instrument limits, stated rather than buried.** The extractor is regex over tool
registries, not an AST walk: it **over-counts** `bruchris` (222 vs a README-advertised 187) and
it needed three separate fixes before it saw three different registration idioms —
`@mcp.tool` **without parentheses** (130 occurrences in `vishalsachdev`, first run extracted
**1**), nested-paren decorator arguments, and a **Go** codebase (`Jawadh-Salih`, first run
extracted **0** because only `.py`/`.ts`/`.js` were scanned). 🔵 Each miss failed toward
*"no write tools here"* — the same direction as `Gap 447-A`'s substring defect, and the reason
the first census run would have **confirmed** `Gap 447-B` instead of refuting it. The
32.9 % write share is therefore a **lower bound**.

---

## 🆕 `p447` — **🔴 Gate posture: DENIED, no baseline (`Gap 446-A`, second consecutive pass). 🟢 ZERO new rows, and that is the result: the discovery channel returned only names already on this shelf, for the second hour running. 🟢 The shelf's pins were audited as a population instead — 17 of 18 still exact, and the one that moved did not move its grant.**

🔴 **No rows are added this pass, and no row is padded to meet a count.** Four global discovery
legs returned **nine** candidates; **all nine** were already on a sell shelf, each graded by
`grep` against this file before being written down. 🔵 `p446` nilled the same channel on 18 of
18. **Two consecutive saturations is a statement about the channel, not the supply.**

🟢 **The one candidate that was *known but not shelved* stays off, for a reason re-measured
today.** `lucanardinocchi/canvas-mcp` resolves (HEAD `f0dbbcb28ec8`) but carries **no `LICENSE`
and no `LICENSE.md`** — re-confirming `p441`'s `ABSENCE-ENUMERATED` grading at a **new HEAD**.
🔵 *Known is not shelved* paid `p442` seven rows; here the same distinction correctly pays
**none**, and the absence is stronger for having survived a HEAD move.

### 🟢 Pin-currency audit over this shelf — the first time it has been run as a population

| result | count | detail |
|---|---|---|
| 🟢 pin still exact after ~24 h | **17 of 18** | across `agents/top.md`, `repos/foundations.md`, `verticals/solutions.md` |
| 🔴 pin stale | **1 of 18** | `Apomera/AlloFlow` `6194e51e8f1f` → `1499a80fd362` |

🟢 **`Apomera/AlloFlow`'s row needs no change.** Its `LICENSE` is **35 442 B · `698099632698`**
at *both* the published pin and the live HEAD, reproducing `p433`'s published cell to the digit.
The row's AGPL-3.0 verdict and its *vendor-over-MCP* disposition **stand**; only the pin is a
day old. 🔵 This is `Gap 446-B`'s rule working exactly as `p446` wrote it: **the cell is the
identity, the pin is a date.**

🔴 **`vishalsachdev/canvas-mcp` is the exception that should be read as a warning on this
shelf**: three HEADs in ~24 h (`884d48cd0873` → `c47a611cfbed` → `08edff523e00`), with `p446`'s
pin already stale **25 minutes** after the commit it names. Full mechanism, and the rule that
replaces the obvious-but-wrong one, in `repos/trending.md` under `p447`.

🟢 **`p446`'s lineage finding reproduces independently** — `vishalsachdev` root `afe32c3e1721`
and `r-huijts` root `731aa116052b`, both to the digit from fresh blobless clones; and the tenth
address, `lucanardinocchi/canvas-mcp`, is a **singleton** (root `75ae284711d6`, 3 commits).
**Ten addresses, six projects, stands.**

---

## 🆕 `p446` — **`Gap 445-C` ANSWERED, and this shelf has been over-counting the LMS-MCP tier by 40 %: 🔴 the ten Canvas/Moodle addresses are SIX distinct projects. 🔵 And the hypothesis that found them was right for the wrong reason — the "six near-identical descriptions" do not exist; LINEAGE does.**

🔵 **Shape.** No WebSearch leg added a row to this shelf. The pass instead bought the audit
`Gap 445-C` prescribed, over the ten addresses `p445` measured, using **full history** rather
than a ref-set test — the instrument `gate-fork-direction` (`p404`) and `gate-group-lineage`
(`p405`) already require. **Ten blobless clones, ten HEADs resolved, ten licence payloads
fetched and digested, three cross-remote ancestry tests** — all first-hand, all **2026-10-25**.

### 🔴 The count an engagement reads first was wrong: six projects, not ten

Graded by **root commit** (a fork shares it) and confirmed by **licence payload cell** (a fork
inherits it byte-identically). Both columns are measured, not inferred:

| address | root commit | licence cell | commits | files | project |
|---|---|---|---|---|---|
| [`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp) | `afe32c3e1721` | MIT · 1 071 B · `5385a26e2fac` | **1 128** | 503 | 🟢 **ARM-1 upstream** |
| [`Harikeshav-R/canvas-mcp`](https://github.com/Harikeshav-R/canvas-mcp) | `afe32c3e1721` | MIT · 1 071 B · `5385a26e2fac` | 1 034 | 472 | 🔴 ARM-1 fork — **0 unique commits** |
| [`NelsonSpencer/canvas-mcp`](https://github.com/NelsonSpencer/canvas-mcp) | `afe32c3e1721` | MIT · 1 071 B · `5385a26e2fac` | 416 | 218 | 🔴 ARM-1 fork — **2 unique, 714 behind** |
| [`r-huijts/canvas-mcp`](https://github.com/r-huijts/canvas-mcp) | `731aa116052b` | MIT · 1 065 B · `ab5109aafdb8` | 60 | 31 | 🟡 **ARM-2 root** |
| [`mdweaver/canvas-mcp`](https://github.com/mdweaver/canvas-mcp) | `731aa116052b` | MIT · 1 065 B · `ab5109aafdb8` | 64 | 35 | 🟢 ARM-2 **descendant, 4 ahead** |
| [`bruchris/canvas-lms-mcp`](https://github.com/bruchris/canvas-lms-mcp) | `6d2e39a1cf7f` | MIT · 1 070 B · `c29329c5ef3b` | 430 | 501 | 🟢 independent |
| [`csmediapro/moodle-mcp-server`](https://github.com/csmediapro/moodle-mcp-server) | `c5209fe71c06` | 🔴 **AGPL-3.0** · 34 523 B · `0d96a4ff68ad` | 58 | 107 | 🟢 independent |
| [`Jawadh-Salih/moodle-mcp-server`](https://github.com/Jawadh-Salih/moodle-mcp-server) | `93ecc95525bf` | MIT · 1 063 B · `2cf91ec5272f` | 13 | 37 | 🟢 independent |
| [`caleb-media-studio/canvas-mcp`](https://github.com/caleb-media-studio/canvas-mcp) | `96daa3fa20a3` | MIT · 1 066 B · `e7b1808c2ef8` | 11 | 35 | 🟢 independent |
| [`Mattlo0546/canvas-mcp`](https://github.com/Mattlo0546/canvas-mcp) | `36161a6e38c8` | MIT · 1 067 B · `13c8ad755224` | 5 | 13 | 🟢 independent |

🟢 **Four distinct root commits carry one address each; two carry three and two.** So the tier
is **6 projects across 10 addresses**, and the two arms are established on **two independent
axes that agree** — shared root *and* byte-identical payload. 🔵 **`csmediapro`'s AGPL-3.0 cell
reproduces this base's own published figure** (34 523 B, `agents/trending.md` `p437`) from an
independent clone this hour, which is a reproduction result, not a new row.

### 🟢 Direction, graded by full history — which address an engagement should actually take

- **ARM-1 → take [`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp).**
  `Harikeshav-R`'s HEAD `db979a5ab5d7` is an **ancestor** of upstream HEAD — it contributes
  **nothing** that upstream does not already have, and is 94 commits behind.
  `NelsonSpencer`'s HEAD `92b7fbc9cd33` holds **2** commits upstream lacks while sitting **714
  behind**: a stale fork with a local patch, not an option.
- **ARM-2 → take [`mdweaver/canvas-mcp`](https://github.com/mdweaver/canvas-mcp), not the root.**
  `r-huijts`'s HEAD `711549f163ef` **is an ancestor** of `mdweaver`'s `739f07f6bb18`, which is
  **4 ahead** (HEAD 2026-10-01 against 2026-09-21). 🔵 This is the one case where the
  **fork is the maintained side**, which is why direction has to be measured and not read off
  star counts or publication order.

### 🔴 `Gap 445-C`'s own evidence was wrong, and that is worth more than the conclusion

The gap asserted *"six of the ten carry near-identical descriptions ('up to 102 tools and 8
agent skills'), which is a fork arm."* Measured first-hand from each README at HEAD, the
tool-count claims are **all different and none is 102**:

| `bruchris` | `vishalsachdev` | `Harikeshav-R` | `NelsonSpencer` | `mdweaver` | `r-huijts` | other four |
|---|---|---|---|---|---|---|
| 187 tools | 128 tools | 126 tools | 99 tools | 89 tools | 69 tools | no count |

🔴 **The description channel did not identify a single one of the five arm members** — it groups
`bruchris` (independent, 187) with the arm, and splits `vishalsachdev` (128) from
`Harikeshav-R` (126), which **are** the same project. 🟢 **The arms are real and the reason
given for them was not.** Recorded as `Gap 446-C`: a near-identical *description* is not
evidence of a fork, and this base should stop treating prose similarity as lineage — the
blobless clone costs ~1 s per repository and answers it outright.

### 🟡 Disposition for this shelf — the rows stay, the COUNT does not

🔵 **No row is deleted.** A fork with a local patch is still an address an engagement may be
handed, and `p405` already fixed the citable unit as the **family**. What changes is what this
file may claim: 🔴 **never "ten Canvas/Moodle MCP options"**. The honest sentence is **"six
projects, of which two are permissive single-maintainer arms; take `vishalsachdev` for Canvas,
and the Moodle side costs AGPL-3.0 or a 13-commit MIT alternative."**

### 🟡 A pinned HEAD is a timestamp, not an identity — measured twice this hour

🔴 **`vishalsachdev/canvas-mcp`'s HEAD moved DURING this pass.** `git ls-remote` returned
`884d48cd0873` at the start of the leg; the clone 90 seconds later checked out `c47a611cfbed`.
🟢 **Not a misread — proven by ancestry:** `884d48cd0873` is an **ancestor** of `c47a611cfbed`,
and its commit is dated **2026-10-25**. The repository took a push mid-leg.
🔵 **Second instance, against this base's own published pin:**
[`krzysztofbury/librus-mcp`](https://github.com/krzysztofbury/librus-mcp) is shelved below at
HEAD `e12e36f24224`; the live HEAD is **`56515efee01b`**, **1 commit ahead**, `e12e36f24224`
confirmed an ancestor. 🟢 **And its payload cell did not move at all** — root MIT re-measures
**1 071 B · `22e7ab2dbddc`**, identical to the published cell.
🟢 **So: verify a grant on the PAYLOAD CELL, which is stable, and read a HEAD pin as the date
the tree was seen.** Registered as `Gap 446-B`.

### 🟢 This pass's cell method was validated against a cell this base already published

🔵 Before publishing ten new cells, the method was checked against a known answer:
`krzysztofbury/librus-mcp`'s root payload re-measured **1 071 B** with **sha256-first-12 =
`22e7ab2dbddc`** — the published cell, to the digit. 🟢 `sha1` (`c9abf450e4ea`), `md5`
(`31aebbb6abd5`) and the git blob id (`90838b0fab0b`) all disagree, so the convention is
confirmed as **sha256-12 over raw file bytes** and this pass's ten cells are in it.

### 🟢 One shelf disposition below CHANGES, and the upstream itself supplied the reason

🔵 The `librus-mcp` row below carries `p442`'s disposition *"integrate over MCP, never vendor
the repository."* That is still right and is now **incomplete**: the upstream has published a
**9 662 B provenance review** (`LICENSE_REVIEW.md` · `6905cca1f0b4`, review dated **2026-10-05**)
which confirms the GPL-3.0 subtree from the other side *and* names a **third lane this base did
not have** — a flattened single-artefact build is **not** covered by its MIT grant. Full
first-hand read, with the dependency closure, on
[`repos/foundations.md`](../repos/foundations.md) `p446`.


## 🆕 `p445` — **ZERO rows added to this shelf, and the two things that makes it worth reading: 🔴 the agent-addressable discovery channel returned 0 new addresses from 10 candidates, and 🔴 this file's own LATAM rows must now be read differently, because the trend they were shelved under has been REFUTED**

🔵 **Why no rows.** The leg aimed at exactly this shelf's category — **LMS MCP servers**, the
agent-addressable shape, Canvas and Moodle — returned **ten** candidates and **not one** was
new to this base. Several are already placed on this file. Prior-mention counts, measured this
hour: `vishalsachdev/canvas-mcp` **77**, `bruchris/canvas-lms-mcp` **70**,
`csmediapro/moodle-mcp-server` **43**, `r-huijts/canvas-mcp` **41**,
`Jawadh-Salih/moodle-mcp-server` **35**, `mdweaver/canvas-mcp` **29**,
`Mattlo0546/canvas-mcp` **22**, `NelsonSpencer/canvas-mcp` **18**,
`caleb-media-studio/canvas-mcp` **17**, `Harikeshav-R/canvas-mcp` **4**. 🔵 With `p443`'s
28-of-29, that is two independently-shaped queries saturating at the same denominator — a
result about the **channel**, not the query. Full measurement: [`repos/trending.md`](../repos/trending.md) `p445`.

🔴 **A caution about this shelf's MCP rows, registered as `Gap 445-C`.** Six of those ten carry
near-identical descriptions ("up to 102 tools and 8 agent skills"), which is a **fork arm**,
not six projects. Nothing here has ever checked whether this file's MCP rows count forks as
distinct projects, and the field that would be wrong is the one an engagement reads first.

### 🔴 How to read this file's LATAM rows now — `Trend 44` is refuted, and `Pattern AW` still stands

`p444` shelved [`IFRN/suapi`](https://github.com/IFRN/suapi) and the two `ifrn-oficial` clients
as the evidence for a general rule: *where the institution publishes the integration code, it
publishes it without a grant.* That rule was measured on **five rows, one institution, one
country**, and this pass tested it over **3 932** addresses this base has verified first-hand:

| publisher class | n | grant | rate |
|---|---|---|---|
| INSTITUTIONAL | 36 | 26 | 🟡 **72.2 %** |
| NON-INSTITUTIONAL | 3 896 | 2 971 | **76.3 %** |

🔴 **Fisher exact p = 0.558 — indistinguishable from noise.** Hand-labelling all 36 institutional
rows (precision **75.0 %**; nine were suppliers or projects caught on an institution *word*) and
re-aggregating by **publisher** rather than by address gives **73.3 %** against **77.1 %**, on
an institutional n of **15**.

🟢 **So: "the institution does not licence" is IFRN-specific, not institution-generic.** The
sharp fact survives — `ifrn` + `ifrn-oficial` are still the only institutional publisher in the
entire corpus with **multiple addresses and zero grants** — and `Pattern AW` (use
`ivmelo/suap-api-php`, and ask IFRN in writing to licence `suapi`) is still the correct move.
🔴 **What does not survive is generalising it to the next institution an engagement meets.**
Assume nothing about a university's grant posture from the fact that it is a university; probe
it. Instrument, pre-registered predictions and verdicts:
[`agents/trending.md`](trending.md) `p445` and
[`compose/code/p445-publisher-class-census/README.md`](../compose/code/p445-publisher-class-census/README.md).

### 🟢 Re-verification of the two rows `p444` placed here, because it was free

| row | `p444` recorded | `p445` re-read 2026-10-25 | verdict |
|---|---|---|---|
| [`sebassg/sia-unal-mcp`](https://github.com/sebassg/sia-unal-mcp) | 🔴 NO GRANT FILE · `529e017f264c` · 0 of 35 paths | 🔴 **`ABSENCE-ENUMERATED` over 35 paths · same HEAD `529e017f264c`** · 2026-03-12 | 🟢 **reproduces** |
| [`ivmelo/suapbot`](https://github.com/ivmelo/suapbot) | 🟡 AGPL-3.0 · `LICENSE` 34 520 B | 🟡 **AGPL-3.0 · `LICENSE` 34 520 B · `76a97c878c9c`** · HEAD `d1f90f18ecf5` · 2017-08-24 · 121 files | 🟢 **reproduces** |

🔵 Both cells hold. `sia-unal-mcp` remains the highest-value ungranted address this base knows
— an MCP server over a Colombian national university's system of record, which is precisely the
component an engagement would want to vendor and precisely the one it cannot. 🟡 The experiment
that would resolve it (asking the author for a licence) requires an outward-facing message
under Globant's name and was **not** run by this unattended pass — `Gap 445-D`.

---

## 🆕 `p444` — **Two agent-addressable LATAM rows, and the better one cannot be shipped: an MCP server for a Colombian national university's system of record, live, TypeScript — and carrying NO GRANT**

🔵 **Why only two rows from 37 addresses.** `Gap 443-D` warned that the LATAM arm is
*integration surface, not agents*, and that `agents/top.md`'s LATAM count must not be read as
if every row were an AI system. `p444` probed 37 more LATAM addresses and that warning holds:
**35 are scrapers, wrappers, browser extensions and timetable viewers.** Only the two below are
agent-addressable, and they are shelved here with their grant state **in the first column**,
because for one of them the grant is the whole story.

| Agent / repo | Grant, read first-hand 2026-10-25 | Region | What it is, and whether Globant can build on it |
|---|---|---|---|
| 🔴 [`sebassg/sia-unal-mcp`](https://github.com/sebassg/sia-unal-mcp) | 🔴 **NO GRANT FILE** · `529e017f264c` · 0 of 35 paths is a licence path | **LATAM** (Colombia) | **MCP server for SIA UNAL** — Sistema de Información Académica, Universidad Nacional de Colombia, Sede Medellín. TypeScript (26 files), HEAD **2026-03-12**. 🔵 The **second** agent-addressable LATAM address this base has found, after `p443`'s `siu-guarani-mcp`, and the first for Colombia. 🔴 **NOT a build-on row: with no licence there is no grant of use, and an MCP server is exactly the component an engagement would want to vendor.** Shelved as *the proof the shape exists in Colombia* and as `Gap 444-C`'s highest-value ask. |
| 🟡 [`ivmelo/suapbot`](https://github.com/ivmelo/suapbot) | 🟡 **AGPL-3.0** · `LICENSE` 34 520 B · `76a97c878c9c` | **LATAM** (Brazil) | Telegram bot over **SUAP** (Instituto Federal network) serving grades, classes, absences, materials and virtual classrooms, 14 ★, 121 files. 🔴 HEAD **2017-08-24** — nine years stale, shelved as the *reference shape* for the notify-the-student agent, not as a dependency. 🟡 AGPL-3.0 reaches a hosted deployment, so it is a read-and-reimplement row, never a vendor row. |

🟢 **The build-on agent-shaped row for this tranche is on `repos/foundations.md`, not here:**
[`Open-Source-eUdeC/UdeCursos-bot`](https://github.com/Open-Source-eUdeC/UdeCursos-bot) — MIT,
HEAD 2024-03-17, Python — is the only LATAM portal-notifier with a permissive grant. It is a
bot rather than an LLM agent, which is why it is shelved as a foundation and not as an agent.
🔵 **That is the honest state of the LATAM agent column: one unlicensed MCP server, one
nine-year-old AGPL bot, and one MIT bot that is not an agent.**

---


# Agentes y repos AI — Education

> Curated open-source supply for education engagements. Every row below was read
> **first-hand on 2026-10-25**: existence via `git ls-remote`, licence family via the
> repository's own payload at the HEAD SHA shown, with byte size and `sha256` prefix.
> Focus: MIT / Apache-2.0 / BSD — the grants Globant can build on.

## How to read this file

The **curated tables come first** — they are the deliverable. The per-pass research
narrative that used to sit at the top of this file now lives in `agents/trending.md`,
which is the append-only record; nothing was lost, and `git log` holds every prior pass.

## ✅ Verified build-on tier — read 2026-10-25

Permissive grants (MIT / Apache-2.0 / BSD-3), each confirmed from the repository's own
licence payload at the commit shown. These are safe starting points for an engagement.

### 🆕 `p443` · 2026-10-25 — this shelf placed **5 of its 116 rows in LATAM**, and the supply that fixes it was **already inside this base**, unshelved. 🟢 The variable that found it is the **platform name**, not the language. 🟢 One row added here; five more on `repos/foundations.md`

🔴 **The census that should have been run passes ago**, over this file's own placed rows:
**APAC 41 · EMEA 35 · North America 19 · Global 16 · LATAM 5.** A base whose stated purpose is
that a LATAM engagement is served as well as an EMEA one was serving it at **one eighth** of
EMEA's rate.

🟢 **What bought it.** Not a Spanish or Portuguese leg — earlier passes ran those and concluded
*the language was the wrong variable*, and that conclusion stands. The variable that built this
file's EMEA national-platform line is **the name of the system the institutions actually run**:
Librus, IServ, Smartschool, EduPage, Skola24, DTU Learn are here because someone searched for
*those words*. LATAM's equivalents — **SIGAA** (Brazilian federal universities) and **SIU
Guaraní** (Argentine universities) — had never been entered. Entered once, sorted by stars, with
**no capability words added**, they returned a whole tier.

🔴 **And five of the six addresses were already in this base's own append-only record, on no
shelf.** The record is working; nothing was reading it. 🔴 **The promotion ledger cannot see
them either** — all six are `grep`-absent from it, and the measurement behind that
(**2 361** record addresses absent from the ledger, **69** of its 219 rows already shelved) is
`Gap 443-A`. Mechanism, the full 14-row measurement table, the three refused-ungranted
addresses and the `ipti/br.tag` README-vs-payload conflict:
[`agents/trending.md`](trending.md) `p443`. Recipe: `Pattern AV`.

🟢 **Why only ONE row lands here and five land on `repos/foundations.md`.** Of the tranche, only
`siu-guarani-mcp` is **agent-addressable** — it is an MCP server, so a tutoring or
administrative agent can call it today. The rest are APIs, scrapers and browser extensions:
integration surface, which is the foundations tier. 🟡 That distinction is registered as
`Gap 443-D` so this file's LATAM count is not read as five AI systems.

🔴 **The licence frontier, measured for LATAM for the first time:** the student-side tooling is
permissive (**6 of 8** academic-portal addresses) and **every** institutional platform that
holds student records is copyleft — GPL-2.0, GPL-3.0, GPL-3.0, AGPL-3.0, **0 of 4 permissive**.
🟢 So the sellable LATAM shape is *integrate over an interface, never vendor the platform*,
which is exactly what the one row below is for.


### 🆕 `p442` · 2026-10-25 — the ladder returns **one** row, and on **12 of 134** repositories that is not the whole grant. 🔴 One row sold here as MIT ships a complete **GPL-3.0** below its root. 🔴 And **19 of the 162 payload cells this base publishes did not reproduce** — repaired below, with a standing gate so they cannot come back

🔵 `Gap 441-A` bought. The tree channel now lives **in** the library every pass sources
(`lib/probe_payload.sh::probe_tree_paths` / `probe_repo_all`), not beside it. Mechanism, the
denominators and the mutation table: `compose/code/p442-shelf-tree-crosscheck/README.md`.
Recipe: `Pattern AU`.

**What the tree says that the ladder cannot.** 134 repositories — every one whose payload path
these three sell shelves publish — enumerated first-hand this hour:

| | n |
|---|---|
| exactly one own-grant path | 🟢 **121** |
| 🔴 **more than one** | 🔴 **12** |
| 🔴 of those, more than one **FAMILY** | 🔴 **4** |
| published path absent from the tree | 🟢 **0** |

🔴 **The four, measured first-hand. One of them is a build-on row.**

| repository | root grant (sold) | what else the tree carries | the commercial read |
|---|---|---|---|
| [`krzysztofbury/librus-mcp`](https://github.com/krzysztofbury/librus-mcp) | MIT · 1 071 B · `22e7ab2dbddc` | 🔴 **GPL-3.0** · `legacy_reference/LICENSE` **35 149 B** · `3972dc9744f6` · 🟢 `GRANT-PRESENT`, beside 20+ `.py` files | **integrate over MCP, never vendor the repository**: a copy of the tree carries GPL-3.0 on that subtree |
| [`Hiepler/EuConform`](https://github.com/Hiepler/EuConform) | MIT · 1 073 B · `65335056589f` | **EUPL-1.2** · `LICENSE-EUPL` **13 240 B** · `3dcf9c6f6119` | dual-licensed. EUPL-1.2 is the EMEA public-sector grant and this base has **no clause profile for it** (`Gap 442-C`) |
| [`withmarbleapp/os-taxonomy`](https://github.com/withmarbleapp/os-taxonomy) | ODbL · 25 289 B · `77d2692c3d64` | **CC BY-SA 4.0** · `LICENSE-CONTENT` **18 375 B** · `cde7883b9050` · `CONTENT-COPYLEFT:share-alike` | **two** share-alike obligations, not one — the database **and** the content |
| [`Apomera/AlloFlow`](https://github.com/Apomera/AlloFlow) | AGPL-3.0 | MIT ×2 + Apache-2.0 under `mathlive-assets/`, `sre-assets/` | 🟡 **vendored**, not the project's grant — the enumerator's own limit, `Gap 442-B` |

🟢 **And the inverse case, which is the stronger argument for enumerating.**
[`24kchengYe/human-skill-tree`](https://github.com/24kchengYe/human-skill-tree) has a root
`LICENSE` of **1 134 B · `3fb8cda58638`** that grades 🔴 `GRANT-BY-REFERENCE` — a notice, not a
grant — while the complete **AGPL-3.0 (34 523 B · `0d96a4ff68ad`)** sits at `app/LICENSE`. The
ladder's answer was not incomplete, it was **wrong about the project**. 🟢 Read first-hand, that
notice also carries a dual-licensing clause nothing here had joined: the `skills/` content is
**AGPL-3.0 *or* MIT at the user's option**, `app/` is AGPL-only. The row is below.

🔴 **The second finding is in this base's own cells, and it is measured, not inferred.** Every
published payload cell was re-measured twice — from the file, and through the library's
preserved `P834` defect: 🟢 **143 reproduce**, 🔴 **19 carry the capture signature** (byte count
short by the trailing-newline run, digest taken **of the stripped bytes**). For
`GarethManning/education-agent-skills` at its pinned commit, the file is **1 230 B ·
`f952182df4eb`** and `printf '%s' "$(cat LICENSE)"` is **1 229 B · `40db9b472090`** — the
published cell, to the digit.

| the 10 repositories whose cells were capture-measured | shelved by | cell now |
|---|---|---|
| [`Miaotofu01/Study-Mate`](https://github.com/Miaotofu01/Study-Mate) | `p433` | 1 064 B · `dc1997d82189` |
| [`Li-Evan/Bloom`](https://github.com/Li-Evan/Bloom) | `p438` | 1 069 B · `7d574cf3632e` |
| [`robotros/California-IEP-AI-project-kit`](https://github.com/robotros/California-IEP-AI-project-kit) | `p432` | 1 065 B · `43554d1189d8` |
| [`67tallchris/iep-builder`](https://github.com/67tallchris/iep-builder) | `p432` | 1 069 B · `aa8cfde0dc31` |
| [`dougdevitre/access-to-education`](https://github.com/dougdevitre/access-to-education) | `p432` | 1 069 B · `fc7c8b90fee1` |
| [`ezixen/PlannedEducation`](https://github.com/ezixen/PlannedEducation) | `p432` | 1 086 B · `53de23fdecc2` |
| [`rwrife/rubric-desk`](https://github.com/rwrife/rubric-desk) | `p432` | 1 063 B · `c186f5cb204a` |
| [`Apomera/AlloFlow`](https://github.com/Apomera/AlloFlow) | `p433` | 35 442 B · `698099632698` |
| [`GarethManning/education-agent-skills`](https://github.com/GarethManning/education-agent-skills) | `p438` | 1 230 B · `f952182df4eb` |
| [`ucbds-infra/ottr`](https://github.com/ucbds-infra/ottr) | — | 🟢 already correct (`LICENSE.md`, **not** the 108 B root stub) |

🔵 **The attribution matters more than the count.** `p432` wrote **5 of its 5** rows that way,
`p433` **2 of 5**, `p438` **2 of 11**, every other pass **0 of 113**. So the defect is not
lane-shaped, it is **intra-pass**: the same pass measured some rows through the library and
typed others by hand, and a reader cannot tell which cell is which by looking. 🟢 Hence a
primitive and a ratchet rather than a reminder — `cell_of_file` / `lib/measure --cell` own the
cell string now, and `make gate-cell-reproduction` (21 offline controls, 11 negative) reports
**162/162 green** on this commit and types any future unmeasured cell `CELL-UNMEASURED`.

### 🆕 `p441` · 2026-10-25 — every **BSD-3** row above and below is now verified CLAUSE-BY-CLAUSE, and three of them are invisible to a title-keyed scanner

🟢 `Gap 440-A` closed for BSD. All 12 BSD payloads this file and its siblings publish were
probed first-hand and graded against a **variant-aware** profile (BSD-2 and BSD-3 are
different licences under one family name): **11 of 12 `GRANT-PRESENT`.**

| repository | payload · `sha256₁₂` | verdict |
|---|---|---|
| [`Open-TutorAi/open-tutor-ai-CE`](https://github.com/Open-TutorAi/open-tutor-ai-CE) | `LICENSE` 1 531 B · `57c341d09920` | 🟢 `GRANT-PRESENT` 🔴 untitled |
| [`jupyterlab/jupyter-ai`](https://github.com/jupyterlab/jupyter-ai) | `LICENSE` 1 516 B · `a0be5735cdce` | 🟢 `GRANT-PRESENT` |
| [`QuantStack/jupyter-ai-tutor`](https://github.com/QuantStack/jupyter-ai-tutor) | `LICENSE` 1 532 B · `ccaa70decf0d` | 🟢 `GRANT-PRESENT` |
| [`ucbds-infra/otter-grader`](https://github.com/ucbds-infra/otter-grader) | `master/LICENSE` 1 560 B · `6af203d41a01` | 🟢 `GRANT-PRESENT` |
| [`ucbds-infra/ottr`](https://github.com/ucbds-infra/ottr) | 🔴 `LICENSE.md` 1 555 B · `1677c5307530` — **not** the 108 B `LICENSE` stub | 🟢 `GRANT-PRESENT` |
| [`jupyterhub/ltiauthenticator`](https://github.com/jupyterhub/ltiauthenticator) | `LICENSE` 1 528 B · `08eebd9662cb` | 🟢 `GRANT-PRESENT` |
| [`jupyterhub/jupyterhub`](https://github.com/jupyterhub/jupyterhub) | `LICENSE` 1 475 B · `7069c7e8d60e` | 🟢 `GRANT-PRESENT` 🔴 untitled |
| [`jupyter/nbgrader`](https://github.com/jupyter/nbgrader) | `LICENSE` 1 512 B · `3a83d5b8e22c` | 🟢 `GRANT-PRESENT` 🔴 untitled |
| [`jupyterlite/jupyterlite`](https://github.com/jupyterlite/jupyterlite) | `LICENSE` 1 525 B · `574f8a9cab1e` | 🟢 `GRANT-PRESENT` |
| [`OpenOLAT/qtiworks`](https://github.com/OpenOLAT/qtiworks) | `LICENSE.txt` 2 058 B · `a5c692f12090` | 🟢 `GRANT-PRESENT` |
| [`open-webui/open-webui`](https://github.com/open-webui/open-webui) | `LICENSE` 2 819 B · `5f1bd74c48bf` | 🟡 `GRANT-PRESENT` **+ branding clause + CLA — not a stock BSD-3 grant** |

🔴 **Three rows carry no title line**, so `titled_family()` — and every other title-keyed
tool — answers `UNKNOWN` for them. The family must come from a hardened classifier and be
**passed in** (`grant_presence.py --family BSD`); `P171` forbids re-answering it in the
grader. 🔵 Mechanism, the 87 controls and the mutation results:
`compose/code/p441-bsd-variant/README.md`. Recipe: `Pattern AT`.

| Agent / repo | Licence (verified) | HEAD @ 2026-10-25 | Licence payload | What it does | Region |
|---|---|---|---|---|---|
| [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | Apache-2.0 | `a31d82624c27` | `LICENSE` 11 408 B · `cd2f54e1e506` | Agent-native personalised tutoring: multi-mode learning, persistent learner memory, multi-agent orchestration. The reference tutoring agent. | Global |
| [huggingface/smolagents](https://github.com/huggingface/smolagents) | Apache-2.0 | `96f33faaf028` | `LICENSE` 11 357 B · `c71d239df917` | Minimal code-writing agent framework. The lightest base for a bespoke tutor or grader when DeepTutor is too much. | EMEA |
| [openedx/XBlock](https://github.com/openedx/XBlock) | Apache-2.0 | `c73c4bb42aa7` | `LICENSE.TXT` 11 358 B · `cfc7749b96f6` | Component SDK for Open edX. The supported seam for putting an AI component **inside** an AGPL LMS without touching its core. | Global |
| [pykt-team/pykt-toolkit](https://github.com/pykt-team/pykt-toolkit) | MIT | `ccbaf37b07e3` | `LICENSE` 1 066 B · `f5f955194636` | PyTorch knowledge-tracing library: DKT/SAKT/BKT family, standard datasets. The modelling layer under any adaptive-learning claim. | APAC |
| [CAHLR/OATutor](https://github.com/CAHLR/OATutor) | MIT | `e24c8456e5f7` | `LICENSE` 1 105 B · `5baaaf977a28` | Intelligent tutoring system with Bayesian Knowledge Tracing (UC Berkeley). Deployable ITS, strongest for maths. | North America |
| [learningequality/kolibri](https://github.com/learningequality/kolibri) | MIT | `44a4e68aac3e` | `LICENSE` 1 097 B · `3c056b34a476` | Offline-first learning platform for low-connectivity deployments. **The only MIT platform in the whole platform tier.** | Global |
| [satvik314/educhain](https://github.com/satvik314/educhain) | MIT | `38adb1e9459d` | `LICENSE` 1 092 B · `e3321a1b62cd` | LLM content generation for teaching: questions, lesson plans, courses from source material. | APAC |
| [openfun/richie](https://github.com/openfun/richie) | MIT | `7cf513c235ee` | `LICENSE` 1 079 B · `e4b2a3148135` | Django/React CMS for course portals; the MOOC front-end used by France Université Numérique. | EMEA |
| [DozenTwelve/Papermorph](https://github.com/DozenTwelve/Papermorph) | MIT | `dc4473f0db8a` | `LICENSE` 1 069 B · `41857092247a` | Emits SCORM 1.2 / 2004 packages. The shelf's only readable SCORM emitter — the interop bridge into legacy LMS estates. | Global |
| [semyonfox/canvas-mcp](https://github.com/semyonfox/canvas-mcp) | MIT | `e317c4b7bf10` | `LICENSE` 1 881 B · `fea4cd7cb04d` | MCP server over Canvas LMS. Licence file additionally names twelve upstream addresses with their grants. | North America |
| [kaushikgunasekaren/canvas-grader-mcp](https://github.com/kaushikgunasekaren/canvas-grader-mcp) | MIT | `c47e8b3ac2ae` | `LICENSE` 1 076 B · `2bcdae923d26` | Canvas grading agent that **produces a draft for human sign-off by default** — the staged human-in-the-loop artefact EU, Vietnamese and US-state oversight rules all ask for. | North America |
| [vTanco/google-classroom-mcp](https://github.com/vTanco/google-classroom-mcp) | MIT | `9ba0070eff2f` | `LICENSE` 1 145 B · `a01639b20880` | Teacher-side Google Classroom authoring: bulk coursework, per-student Drive copies, due dates — **created as draft**. See the licence note below: this address now carries the MIT lane. | EMEA |
| [Open-TutorAi/open-tutor-ai-CE](https://github.com/Open-TutorAi/open-tutor-ai-CE) | BSD-3-Clause 🟢 `GRANT-PRESENT` (`p441`, clause-by-clause) 🔴 payload is **untitled** | `196c547291da` | `LICENSE` 1 531 B · `57c341d09920` | Tutoring platform with voice, video and 3D avatars; Docker-first, runs local LLMs via Ollama. | EMEA |
| [panaversity/learn-agentic-ai](https://github.com/panaversity/learn-agentic-ai) | MIT | `dd7426f65b24` | `LICENSE` 1 068 B · `8ea022e30a9b` | Agentic-AI curriculum used at national teaching scale. Courseware, not a runtime — the fastest way to staff a team. | APAC |
| [Teachable-AI-Lab/tutor_gym](https://github.com/Teachable-AI-Lab/tutor_gym) | MIT | `772f5cdca5dd` | `LICENSE` 1 099 B · `8a0a4ba421a0` | Evaluation testbed that runs an LLM as **tutor** *and* as **student** inside existing ITSs — backends `ctat`, `apprentice`, **`oatutor`**. The scorer for the OATutor row above. 🟡 Last commit 2025-09-10; fork, do not depend. | North America |
| [shuangyan123/tutorbench](https://github.com/shuangyan123/tutorbench) | Apache-2.0 (code) | `f9d69c7ce3e1` | `LICENSE` 11 358 B · `cfc7749b96f6` | “Teachometry TutorBench” — scenario-based evaluation **and regression** engine for tutoring systems. Actively maintained (commit 2026-10-25). 🟡 Benchmark **content** is CC-BY-4.0 and the **name** is under a brand policy: three scopes, not one. | Global |
| [littlecookie0722/AI-Teaching-Agent](https://github.com/littlecookie0722/AI-Teaching-Agent) | MIT | `b90bd88a2899` | `LICENSE` 1 069 B · `297c4cba7b33` | Markdown teaching material → Lab / Exam / Grading artefacts, each raised as a `WAITING_REVIEW` task with the human approve/reject decision recorded. The draft-and-sign shape `Pattern AH` asks for, already implemented. | Global |
| [Miaotofu01/Study-Mate](https://github.com/Miaotofu01/Study-Mate) | MIT | `d8114f383632` | `LICENSE` 1 064 B · `dc1997d82189` | Self-study agent that plans a route through a subject, teaches it and builds projects alongside. 1 183 ★ / 56 forks. Chinese-first UI — the strongest **zh** learner-facing agent on this shelf. | APAC |
| [Li-Evan/Bloom](https://github.com/Li-Evan/Bloom) | MIT | `68788b5e7d34` | `LICENSE` 1 069 B · `7d574cf3632e` | Socratic tutor built on Bloom's 2-sigma framing; self-hostable FastAPI + React **and** packaged as a harness skill. 292 ★. Chinese-first, English supported. | APAC |
| [robotros/California-IEP-AI-project-kit](https://github.com/robotros/California-IEP-AI-project-kit) | MIT | `ff1ae0ce30e7` | `LICENSE` 1 065 B · `43554d1189d8` | Two special-education roles (CA Essential Standards analyst, IEP goal generator) as pinned knowledge packs, sourced from CDE material, with an explicit "no autonomous student-record action, authorised system of record only" boundary. **The draft-and-sign architecture shipped as a kit.** | North America |
| [67tallchris/iep-builder](https://github.com/67tallchris/iep-builder) | MIT | `b39df0e9a4a1` | `LICENSE` 1 069 B · `aa8cfde0dc31` | Arizona K-8 IEP drafting tool — Svelte + Cloudflare Pages Functions + D1, **bring-your-own-key** AI. A working reference for a jurisdiction-pinned, no-vendor-key deployment. | North America |
| [dougdevitre/access-to-education](https://github.com/dougdevitre/access-to-education) | MIT | `f8abd70707ba` | `LICENSE` 1 069 B · `fc7c8b90fee1` | 69 files / ~120 k words of special-needs **parent-facing** material: IEP navigation, family–school communication, advocacy. Content under a code licence — rare, and the only MIT answer to the unserved-parent persona of `Trend 10`. | North America |
| [ezixen/PlannedEducation](https://github.com/ezixen/PlannedEducation) | MIT | `06fb12159f5e` | `LICENSE` 1 086 B · `53de23fdecc2` | Teacher's aid + AI-assisted grading companion + secure test-taking, privacy-first, self-hosted. Default branch is `dev`. 🟡 Zero stars, single author — read as a reference implementation, not a dependency. | Global |
| [rwrife/rubric-desk](https://github.com/rwrife/rubric-desk) | MIT | `010a44006014` | `LICENSE` 1 063 B · `c186f5cb204a` | Offline rubric scoring (Flutter; phone/tablet/Windows), no accounts and no cloud LMS. The marking surface for a deployment that cannot assume connectivity. 🟡 Created **today**; treat as a seed. | Global |
| [dmoshehun-prog/learn-from-materials](https://github.com/dmoshehun-prog/learn-from-materials) | MIT | `f8849746d85c` | `LICENSE.md` 1 122 B · `15ce43afa44a` | Material → **traceable** knowledge base → interactive learning page, from PDFs, books, slides, Word files and web pages. Built to the Agent Skills standard, so it composes into an existing harness instead of demanding a platform. **1 118 ★ / 104 forks — the highest-traction new education address on these shelves.** 🟡 The payload names `Copyright (c) 2025 virgiliojr94` while the owner is `dmoshehun-prog`: the MIT grant stands, the named holder is a third party. Provenance question, not a licence one — see `agents/trending.md` `p433`. | APAC |
| [122-syf-wcy/PhysicsOS](https://github.com/122-syf-wcy/PhysicsOS) | Apache-2.0 | `a25c6ee26583` | `LICENSE` 11 356 B · `f1a2e5fccede` | K-12 physics tutor that drives a **real physics engine**: the AI reads the problem, the engine renders it as an interactive scene and the result is computable and *checkable* rather than asserted. The grounding move applied to a subject where a wrong answer can be caught. 255 ★ / 17 forks; public-benefit (公益) project, TypeScript, DeepSeek-backed. | APAC |
| [cabbage2000-lab/textbook-writer-skills](https://github.com/cabbage2000-lab/textbook-writer-skills) | MIT | `e2b825072ba5` | `LICENSE` 1 064 B · `0d5a33d13ca9` | Courseware authoring as a **gated** UbD backward-design chain: teaching positioning → five-part gate → chapter-tree gate → four-stage chapter writing → review. Recomputes STEM claims, checks humanities citations against the source, and writes *"needs author confirmation"* where it cannot verify — the one authoring tool found that refuses to assert. Subject-agnostic core, pluggable subject profiles. 37 ★ / 12 forks. | APAC |
| [wenflow-org/wenflow](https://github.com/wenflow-org/wenflow) | MIT | `1c86890946a3` | `LICENSE` 1 067 B · `b6fac57d4710` | 问流 WenFlow — learning-path agent that starts from the learner's **stated problem** rather than a syllabus: dialogue clarifies the goal, then it emits an executable path, teaches in rounds, schedules forgetting-curve review and tracks learning load on four named measures (LSS / KTL / LF / LSB). Ships an 18-page admin back-office **and a virtual-learner simulator**, which is the rarest part — it can be regression-tested without a cohort. Vue3 + Node.js + SQLite, self-hostable. 59 ★ / 19 forks. 🟡 Author calls it an early experimental prototype; read as a reference architecture, not a dependency. | APAC |
| [zhangl1001/civil-ai](https://github.com/zhangl1001/civil-ai) | MIT | `37ba5e28532d` | `LICENSE` 1 067 B · `5731a2d3ccea` | Local-first **adaptive-tutoring agent foundation** — a reference implementation of the runtime seam (agent runtime + SQLite learning-evidence store) with a civil-service-exam app built on it, for iOS and web via Capacitor. The one row on this shelf that separates *tutoring substrate* from *subject application*, so the substrate is reusable. 41 ★ / 7 forks. 🟡 Single author, early; the value is the `learning-evidence` schema, not the exam content. | APAC |
| [chenning42/iserv-mcp](https://github.com/chenning42/iserv-mcp) | MIT | `8afdea14fbcd` | `LICENSE` 1 090 B · `5dc99bd5061f` | MCP server over **IServ** school portals — the platform German state schools actually run. Parent letters with full text and attachments, sick-notes and timetable; the one write tool (`mark_parentletter_read`) is gated behind `confirmed=true`. Unofficial, and the README says instances differ. 🟢 The parent-facing surface of `Trend 10` with a national platform behind it. | EMEA — Germany |
| [krzysztofbury/librus-mcp](https://github.com/krzysztofbury/librus-mcp) | MIT | `e12e36f24224` | `LICENSE` 1 071 B · `22e7ab2dbddc` | MCP server over **Librus Synergia**, the gradebook most Polish schools use: grades, attendance, timetable, homework, calendar, announcements, messages, formative assessments and school-year history, multi-login. v2.0 replaced the `librus-apix` backend with the native API; published to PyPI as `librus-mcp`. Pairs with `librus-python-api` on `repos/foundations.md` — 🔵 byte-identical MIT payload, same holder. 🔴 **`p442`: the root MIT grant is not the whole tree.** `legacy_reference/` carries a complete **GPL-3.0** (`legacy_reference/LICENSE` **35 149 B** · `3972dc9744f6`, 🟢 `GRANT-PRESENT`) beside 20+ `.py` files — the v1.x `librus-apix` implementation the native-API rewrite replaced. 🟢 **Integrate over the MCP interface; do not vendor the repository**, and if you must, delete `legacy_reference/` and record that you did. The ladder-based probe every earlier pass used returns one row and cannot see this. | EMEA — Poland |
| [MauroDruwel/Smartschool-MCP](https://github.com/MauroDruwel/Smartschool-MCP) | MIT | `ab3fa81f857f` | `LICENSE` 1 069 B · `b414ff32815f` | MCP server over **Smartschool**, the platform Flemish schools run. CI, coverage and a PyPI release (`smartschool-mcp`) — the most packaged of the national-platform connectors on this shelf. | EMEA — Belgium |
| [oliverhruby/edupage-mcp](https://github.com/oliverhruby/edupage-mcp) | MIT | `b35ce653d2c9` | `LICENSE` 1 070 B · `e99290e1540b` | MCP server over **EduPage**, the school system used across Slovakia and Central Europe. Tagged releases, quality-gate and security workflows, container scanning — the only CEE national-platform connector here with a security pipeline of its own. 🟡 A second address, `mhlavac/edupage-mcp`, is also carried on the trend record; this is the maintained one. | EMEA — Slovakia / CEE |
| [CarlSvejstrup/dtu-learn-mcp](https://github.com/CarlSvejstrup/dtu-learn-mcp) | MIT | `9444a1fd5199` | `LICENSE` 1 079 B · `4f21e3f0f9fc` | MCP server **and** CLI for **DTU Learn** (Brightspace / D2L): downloads a student's own courses, slides, files, announcements, assignments, deadlines, grades and Panopto lecture transcripts to the local machine — no server, no shared login. 🟢 The first Brightspace-side connector on this shelf that is MIT, against a platform tier that is otherwise vendor-only. | EMEA — Denmark |
| [Kretiandpleti/skola-24-haos-integration](https://github.com/Kretiandpleti/skola-24-haos-integration) | MIT | `fdbc9349b20f` | `LICENSE` 1 070 B · `8b34b498bb1f` | Home Assistant custom component for **Skola24**, the timetable system Swedish municipalities run: domain selection, per-student `SchemaID` as the stable identifier, signature regeneration to defeat stale cached selections, configurable week rollover. 🟡 **Not an MCP server** — it is the Nordic timetable channel, read first-hand, and the integration surface is Home Assistant. | EMEA — Sweden |
| [jibberswrld/fcps-school-mcp](https://github.com/jibberswrld/fcps-school-mcp) | MIT | `7d9dfbfc32bb` | `LICENSE` 1 073 B · `cd9e736254f8` | MCP server over **Schoology, StudentVUE and TJHSST Ion** at once — the three systems a single large US district (Fairfax County Public Schools) actually exposes to students. 🟢 The district-level analogue of the national connectors above, and the only StudentVUE reader on these shelves. | North America — United States |
| [zaikaman/SGU-Academic-MCP](https://github.com/zaikaman/SGU-Academic-MCP) | MIT | `d5209305d13e` | `LICENSE` 1 068 B · `0b02f0945515` | MCP server over a Vietnamese university's academic portal (Saigon University): schedule, grades, exam registration. CI pipeline, Ruff-checked. 🔵 Arrives in the jurisdiction whose **Decision 33/2026/QĐ-TTg** puts education AI in a 46-category high-risk register — the connector is the easy half, the oversight artefact is the engagement. | APAC — Vietnam |
| [jpmanson/siu-guarani-mcp](https://github.com/jpmanson/siu-guarani-mcp) | MIT | `248366400624` | `LICENSE` 1 074 B · `53d0fa710f43` | MCP server **and** CLI over **SIU Guaraní Autogestión**, the self-management portal Argentine universities run — the first LATAM national-platform connector on these shelves, against a region this file placed **5 of 116** rows in before this pass. Seventeen stdio tools over the **teaching-staff profile** (`perfil Docente`): terms, course sections, exam tables and schedules, enrolled students, grades, actas, and CSV/XLSX/JSON export, each with a CLI equivalent. 🟢 **Read-only by construction** — the attendance, topic and grade-loading forms are inspected and deliberately not submitted, with writes left on the roadmap, so it is the draft-and-sign boundary `Pattern AH` asks for rather than a system that can act on a student record. 🟢 **PII is gated behind an explicit `include_pii=True`** on the two roster tools, and credentials come from `GUARANI_USER`/`GUARANI_PASSWORD` in a git-ignored `.env`, with none embedded; `GUARANI_BASE_URL` defaults to the UNR instance and is per-institution configurable. Ships an Agent Plugin v1.0.0 manifest. Scrapes with plain HTTP + BeautifulSoup, no Selenium. 🟡 **1 ★, 6 commits, HEAD 2026-08-10, single author, and unofficial** — read it as the reference implementation of the LATAM connector seam, not as a dependency; the EMEA connectors above started at the same size. | LATAM — Argentina |
| [oaknational/oak-ai-lesson-assistant](https://github.com/oaknational/oak-ai-lesson-assistant) | MIT | `c6871efa8f08` | `LICENSE` 1 077 B · `d150aadcccd2` | **Oak National Academy's** own AI lesson-planning application, MIT, in the open. Built against England's national curriculum. 🟡 The README states it is intended primarily for Oak's internal use and the docs are not written for outside operators — read it as the reference implementation of a state-curriculum lesson assistant, not as a drop-in dependency. | EMEA — United Kingdom |
| [ls1intum/edutelligence](https://github.com/ls1intum/edutelligence) | MIT | `a7584174bd3d` | `LICENSE` 1 091 B · `6b9b9eda00d6` | TUM's suite of AI microservices for an LMS — automated assessment, exercise creation, competency modelling and intelligent tutoring — with a published **version-compatibility matrix** against the Artemis LMS it integrates with. 🟢 The one row on this shelf that ships an LMS-version contract instead of leaving integration risk to the buyer. | EMEA — Germany |
| [kit-sdq/autograder](https://github.com/kit-sdq/autograder) | MIT | `6f35f0b7a88d` | `LICENSE.md` 1 068 B · `30a0bc0d48b4` | KIT's static **and** dynamic analysis autograder for student Java code (Java 17+, Docker for the dynamic arm), with the implemented checks enumerated in-repo. 🟢 The grading-evidence layer for a CS-teaching engagement where a mark has to be explainable check by check. | EMEA — Germany |
| [dodona-edu/dolos](https://github.com/dodona-edu/dolos) | MIT | `2b82821c29d7` | `LICENSE` 1 084 B · `881163366572` | Ghent University's source-code plagiarism detector — CLI, web app and library, published to npm as `@dodona/dolos`. 🟢 The academic-integrity surface that every AI-in-assessment proposal gets asked about, under a grant that allows it to ship inside a deliverable. | EMEA — Belgium |
| [mitodl/open-learning-ai-tutor](https://github.com/mitodl/open-learning-ai-tutor) | MIT | `6a8028528afc` | `LICENSE` 1 069 B · `77a612c534cf` | The backend of **MIT Open Learning's** tutoring chatbot, running in production at `learn-ai.ol.mit.edu`, with the pedagogical engine described in a published paper (arXiv:2410.03781). 🟢 A tutor whose teaching strategy is documented and citable, from an institution a client has heard of — the strongest single credibility row added this pass. | North America — United States |
| [CogitoNTNU/TutorAI](https://github.com/CogitoNTNU/TutorAI) | MIT | `b9c990e14b22` | `LICENSE` 1 140 B · `c56df8d19cd5` | NTNU student-organisation tutoring agent (Django). 🔴 **Restored, not discovered**: an earlier pass promoted this row to this file and a later full-file rewrite dropped it — it survives in `archive/2026-10-21-p351-pre-rewrite/agents-top.md` and the EMEA supply claim in the archived `intel/market.md` rests on it. See `p435` below. | EMEA — Norway |
| [anthropics/k12-teacher-skills](https://github.com/anthropics/k12-teacher-skills) | Apache-2.0 | `31fd6dbb0c07` | `LICENSE` 11 357 B · `58d1e17ffe51` | Four K-12 teacher agent skills — lesson-plan creation, lesson differentiation and two more — **with the evaluation framework they were scored against** in the same repository. 🟢 Rare shape: a teacher-facing capability shipped together with its own evals, which is what `Trend 26` says moves the sellable unit from adoption to evidence. | North America |
| [ark-forge/mcp-eu-ai-act](https://github.com/ark-forge/mcp-eu-ai-act) | MIT | `933e56da71e7` | `LICENSE` 1 065 B · `002af8f9b59c` | EU AI Act compliance scanner as a CLI **and** an MCP server (`eu-ai-act-scanner` on PyPI) — the obligation-side tool for the Article 50 / Annex III education exposure this base tracks. 🔴 **Commercial coupling, named:** the README is a funnel to a €29/month hosted plan, so verify which checks the MIT code actually performs before quoting it to a client. Same error class as this base's `ai-shifu` commerce-coupling finding; the grant is MIT and read first-hand, the *feature surface* is the open question. 🔴 **`p437` CLOSED that open question, and the answer disqualifies it as an obligation oracle:** at `933e56da71e7` it hardcodes `"enforcement_deadline": "2026-08-02"` (`data/eu_ai_act_articles.json:5`), **asserts that value in its own test suite** (`tests/test_articles_db.py:297-299`), and contains **no reference to Regulation (EU) 2026/1744** anywhere in the tree. Its education scope is real (`data/eu_ai_act_articles.json:390`, Annex III cat. 3), which makes it worse: it will confidently tell an education client a conformity deadline passed in August 2026, when Annex III applies from **2 December 2027**. 🟢 Use [`tomdxb0004/eu-ai-act-risk-checker`](https://github.com/tomdxb0004/eu-ai-act-risk-checker) for dates; keep this one only for codebase scanning. | EMEA |
| [liuliu667/cram-engine](https://github.com/liuliu667/cram-engine) | MIT | `982cd31cc68e` | `LICENSE` 1 064 B · `c33ea68946e4` | 考试速通 — four-stage interactive exam-prep teacher built on learning-science principles (diagnose → teach → drill → review), packaged as an Agent Skill. 🟢 Verified at `p381` and **promoted off the backlog here**: its digest reproduces to the byte four days later. 176 ★. | APAC — China |
| [ZeKaiNie/universal-examprep-skill](https://github.com/ZeKaiNie/universal-examprep-skill) | MIT | `3a979e3bead9` | `LICENSE` 1 065 B · `21f44893f051` | Exam Cram Coach — cross-session memory plus **handout traceability** so an answer cites the source page it came from, which is the anti-hallucination move a teacher can actually check. The MIT grant is repeated verbatim at `full/` and `skills/universal-exam-cram-coach/`; 🟡 one 613 B **CC0-1.0** payload sits in a test-fixture corpus (`full/tests/fixtures/ingestion_gold/`) and is third-party content, not the project's grant. 318 ★. | APAC — China |
| [karanb192/algo-sensei](https://github.com/karanb192/algo-sensei) | MIT | `25ea970f82c5` | `LICENSE` 1 081 B · `3b2ca73e81ad` | LeetCode / DSA mentor that teaches by **pattern** rather than by solution, as an Agent Skill. The closest thing on these shelves to an interview-prep tutor with a named pedagogy. 298 ★. | North America |
| [assafkip/claudemy](https://github.com/assafkip/claudemy) | MIT | `438a6288fa74` | `LICENSE` 1 069 B · `262b47ee1fff` | Give it a topic, it researches the material and builds a course — an open alternative to a course marketplace rather than to an LMS. The cheapest route to a **client-branded course generator**. 449 ★. | EMEA — Israel |
| [flysheep-ai/education-skills](https://github.com/flysheep-ai/education-skills) | MIT | `b4c935210206` | `LICENSE` 1 068 B · `23b91d7c0aef` | A collection of teaching and learning-support Agent Skills, Chinese-first. 🟢 **The permissive counterpart to `GarethManning/education-agent-skills`**, which is CC BY-SA 4.0: when a deliverable may not inherit ShareAlike, this is the pack to start from. 118 ★. | APAC — China |
| [TovTechOrg/Tov-learn](https://github.com/TovTechOrg/Tov-learn) | MIT | `290af750671a` | `LICENSE` 1 064 B · `092d389ac156` | Interactive tutor as an Agent Skill with **spaced repetition** built in, so retention is scheduled rather than hoped for. Default branch is `master`. 36 ★ — read as a reference implementation. | EMEA — Israel |
| [24kchengYe/human-skill-tree](https://github.com/24kchengYe/human-skill-tree) | 🟡 **dual, by directory**: `skills/` content is **AGPL-3.0 *or* MIT at the user's option**; `app/` is **AGPL-3.0 only** | `be589ddd04c9` | 🔴 root `LICENSE` 1 134 B · `3fb8cda58638` is a **notice** (`GRANT-BY-REFERENCE`); the grant is `app/LICENSE` 34 523 B · `0d96a4ff68ad` | 30+ skill trees from K-12 to career and social intelligence. 🟢 **Take the `skills/` packs under the MIT option — that lane is in the licence text and this base had the repository typed AGPL.** 🔴 Never vendor `app/`: AGPL-3.0 §13 reaches a hosted deployment. Found by enumerating the tree (`p442`), not by reading the root. 583 ★. | APAC — China |


🆕 **`p442` added the last seven rows** — six permissive (`cram-engine`, `universal-examprep-skill`, `algo-sensei`, `claudemy`, `education-skills`, `Tov-learn`) and one **dual-by-directory** (`human-skill-tree`, whose MIT lane was found by enumerating the tree rather than by reading the root). 🟢 Every one of the seven cells was built with `lib/payload_measure.sh::cell_of_file`, so none can carry `P834`, and each payload was graded `GRANT-PRESENT` by `p439`'s clause instrument at the moment of shelving. 🔵 The registered count below is **not** updated from these seven: `make recount` reads a structurally bounded tier that ends above them and reports the same `23 / 36` STALE it reported on the inherited commit — an inherited register lag (`Gap 400-B`'s neighbourhood), not something this pass introduced.

**42 verified permissive rows.** 🆕 `p435` added the sixteen above: fifteen newly shelved and one **restored** after a full-file rewrite had dropped it. They open the **national and institutional school-platform connector** tier, which no pass had shelved, and **twelve of the sixteen are EMEA** — the region this base had been carrying a sub-regional adoption nil for. Every slug resolved under `git ls-remote` and every
licence was read from the repository's own payload — none was taken from a GitHub badge,
a package manifest, or a directory listing.

🆕 `p431` added the last three rows, which together open a tier this base did not carry:
**tutor evaluation**. `tutor_gym` scores a tutoring agent against `CAHLR/OATutor` — a row already
on this shelf — under a compatible MIT grant and with no adapter work, which is the cheapest
capability added here in weeks. 🟡 Note its MIT payload carries **no `MIT License` title line**;
a sweep keyed on that string reports UNKNOWN for a verbatim MIT grant.


### 🆕 `p432` — seven rows added, and they open the **special-education** tier

`p431` opened tutor evaluation. This pass went at the surface that NA law regulates hardest
and that no shelf in this repository had ever named: **special education / IEP**. Three of the
seven new rows are IEP-specific, and all three are MIT. 🔴 The honest reading is below in
`agents/trending.md`: that tier exists, but it is a **supply desert** — the three MIT addresses
carry 0, 0 and 1 star between them and the two most purpose-built tools in the category carry
**no licence at all**.

🔵 Two of the new rows (`Study-Mate`, `Bloom`) are APAC-built and Chinese-first, which continues
the `Trend 14` direction: APAC remains the net exporter of permissive education AI.

🔴 **Method correction that applies to every row on this file.** GitHub's own `license` field
was wrong in **both** directions in this pass's sample — see the corrections table below. It is a
detection heuristic, not a verdict. Read the payload.

### 🆕 `p433` — three rows added, all **promoted from this base's own backlog**, and a red gate fixed

`p432` opened the special-education tier from the frontier. This pass went at the frontier again
and found it **saturated**: a GitHub API sweep over 204 topic-pinned matches returned four
addresses absent from every shelf, none above 8 ★. 🟢 **The value was behind us, not ahead.**
Five high-traction addresses were already sitting in `repos/trending.md` and `agents/trending.md`
from earlier passes and had **never been promoted** — including a **1 118 ★** address, the
highest-traction new education repo these shelves have recorded. Three of the five are permissive
on a first-hand payload read and are now rows above; two are AGPL-3.0 and are graded in
`agents/trending.md` rather than shelved here.

🔴 **The trending shelves had become write-only** — addresses entered and none left. That is a
defect in method, not in data, and `Gap 433-A` registers the missing instrument: nothing in this
base promotes a trending row, or ages one out, so traction accumulates unread.

🔵 **All three new rows are APAC-built**, the fourth consecutive pass on which new permissive
education supply is APAC-origin. `Trend 14`'s direction is unchanged and worth saying before an
EMEA or LATAM engagement assumes a local-origin base exists: it does not, and because the grant
is permissive, origin is a support-and-language question rather than a licence one.

🔴 **A blocking gate was RED on the commit this pass inherited, and that is reported, not
quietly fixed.** `make commit-gates` exited `2` on `300b983`: `gate-tables` found two
`BLANK-SPLITS-TABLE` defects **on this file** — a stray blank line inside the verified build-on
table and another inside the corrections table below, each making the row after it render as a
new table's header. Both sides of each break carried identical column counts, so the breaks were
accidental; deleting the two blank lines restores one continuous table each, and the suite now
reports `10 shelves, no row is published as a header`. The defect was committed by `p432`.

### 🆕 `p434` — two rows promoted **by a gate**, not by hand, and `p433`'s saturation denominator corrected

`p433` promoted three backlog rows by hand and registered `Gap 433-A` for the missing
instrument. 🟢 **`p434` built it** (`compose/code/p434-promotion-gate`, 28 offline controls,
wired into `make hooks` as `gate-promotion`), and **the gate was RED on its first run** — it
found exactly these two MIT addresses stranded in the trend record, in no curated shelf. They
are the first two rows on this file promoted by an instrument rather than by a pass noticing.

🔴 **And it refutes the predicate `Gap 433-A` prescribed.** The gap asked for a gate keyed on a
**150 ★ threshold**. All five unpromoted addresses above that threshold were graded on
first-hand payloads this pass and **every one is non-permissive** — `Auto-Empirical-Research-Skills`
(**4 771 ★**, CC-BY-SA-4.0), `frametell` (400 ★, AGPL-3.0), `ai-agent-camp` (346 ★, **no licence
file at all**), `deep-student` (290 ★, AGPL-3.0), `sql-to-ER` (192 ★, AGPL-3.0) — while both
permissive rows sit **below** it at 59 ★ and 41 ★. 🔵 **Traction and permissiveness are
anti-correlated in this domain's new supply**, so a star threshold is a filter against the
findings: as prescribed it fires **0** times, star-free it fires **2**. The refuted form stays
runnable as `--predicate p433` so the refutation is reproducible.

🔴 **A second reason the prescription could not have worked: the star channel does not exist
from inside a run.** `api.github.com`, `github.com` HTML and `codeload.github.com` were each
re-measured at **HTTP 403** through this environment's proxy on 2026-10-25; only
`raw.githubusercontent.com` and the git smart-HTTP transport answer. The star figures quoted
above came from the agent session's own GitHub tool and are labelled as such in the gate's
grade table — 🔵 **they are not reproducible from `make`, which is precisely why the gate does
not depend on them.**

🟢 **`p433`'s promotion decision was substantively right and its denominator was wrong.** It
reported *"26 of 30 already named on a shelf; 4 absent, all ≤ 8 ★"*; re-running `p433`'s own
query returns a **4 771 ★** address as the top hit. Both are true at once, because "named on a
shelf" counted the **trending** shelves — the same shelves that pass declared write-only. The
backlog could not appear in a denominator that contains it. 🔵 Nothing permissive above the
threshold was missed, because there was nothing permissive above the threshold.

🔵 **Provenance note, in contrast to `p433`'s highest-traction row.** Both payloads name their
own owner (`Copyright (c) 2026 wenflow-org`, `Copyright (c) 2026 zhangl1001`), so neither
carries the third-party-holder question that `learn-from-materials` does.

🔵 Both rows are **APAC-built**, the fifth consecutive pass on which new permissive education
supply is APAC-origin. `Trend 14` is unchanged.

### 🆕 `p435` — sixteen rows added by a **completed census**, and one row restored that a rewrite had deleted

`Gap 434-A` asked for one thing: grade the unpromoted backlog, because `gate-promotion`
was judging a 2 457-address surface from a **7-row** grade table. 🟢 **All 2 450 ungraded
addresses are now graded, every grant read first-hand off the repository's own payload**
(`compose/code/p435-promotion-sweep`, evidence in
`evidence/promotion-backlog-grants.2026-10-25-p435.tsv`). 🔴 **What it found was not a
handful of stranded rows — it was a whole tier this shelf did not carry.**

**The tier: connectors for the platform a national school system actually runs.** Not
Moodle and not Canvas — `IServ` in Germany, `Librus Synergia` in Poland, `Smartschool` in
Flanders, `EduPage` across Slovakia and CEE, `Skola24` in Sweden, `DTU Learn` in Denmark,
`NEIS` in Korea, `Schoology + StudentVUE + Ion` in one large US district. Every one MIT,
every one with a HEAD commit inside the last month, and **every one already on this base's
trend record** — carried, dated, and never promoted.

🔴 **The honest reading: these were not discoveries.** The corpus held them. `p425` was
caught republishing an absence its own corpus refuted, and this is the same error at
population scale — the EMEA sub-regional nil that `Gap 434-C` has carried for three passes
was being measured against the curated shelves while twelve EMEA addresses sat in the
backlog. **An informed gap is information; an uninformed one looks exactly like coverage.**

### 🔴 `CogitoNTNU/TutorAI` was promoted to this file once already, and a rewrite deleted it

The row above marked *restored* is a defect, not a find. `agents/trending.md` records
**`Promoted:` `CogitoNTNU/TutorAI` … → `agents/top.md`** with a first-hand grant read
(MIT, 1 140 B) and a placement (EMEA, Norway, `stud.ntnu.no`). It is not on this file.
🟢 **It is on `archive/2026-10-21-p351-pre-rewrite/agents-top.md` and on
`archive/2026-10-21-p355-pre-rewrite/agents-top.md`** — so the row landed and a later
full-file rewrite dropped it.

🔴 **And it was load-bearing.** The archived `intel/market.md` cites it by name in the
sentence *"the EMEA supply side is now seven placed permissive rows and is no longer
regulation-only."* The claim stayed; the evidence under it was deleted.

🔴 **Two more claimed promotions from the same block never landed either** —
`Haozhe-Xing/agent_learning` and `kaveheng/GenAi-in-education`, both declared promoted to
`repos/foundations.md`, both absent from it, both in the unpromoted set. 🔵 Nineteen
`Promoted` claims exist across the two trend shelves in at least four different notations,
so a gate over them needs a **notation** first — registered as `Gap 435-B` with that cost
stated, rather than half-built here.

### 🟡 Declined this pass, with the reason — both permissive, both fresh, neither education

| Address | Grant (read first-hand) | Why it is not on this shelf |
|---|---|---|
| [`arvoreeducacao/seedling`](https://github.com/arvoreeducacao/seedling) | Apache-2.0 · `LICENSE` 11 358 B · `cfc7749b96f6` | A **coding-interview sandbox** (per-candidate Claude Code workspace, metered keys, live interviewer view). The owner is a Brazilian education company; the repository is a hiring tool. `Trend 25`'s error class — the owner's domain read as the artefact's purpose. |
| [`CENIA-DEV/multilingual-translator-app`](https://github.com/CENIA-DEV/multilingual-translator-app) | Apache-2.0 · `LICENSE` 11 357 B · `c71d239df917` | A translator served with PyTriton, from Chile's national AI centre. Nothing in the payload or the README makes it an education component. 🔵 Kept on the watch list because CENIA is a LATAM public-research supplier and the next artefact may be in scope. |

🔵 **Both were in the recency slate.** That is the point: `permissive + alive` is a filter,
not a verdict, and this pass's own candidates are the proof.

### 🔵 One identity collapse, caught before it became two rows

[`oaknational/oak-curriculum-api`](https://github.com/oaknational/oak-curriculum-api) and
`oaknational/oak-openapi` return the **same** HEAD under `git ls-remote`
(`0561df5aac12`), and the repository's own badges point at `oak-openapi`. Per this base's
`gate-identity` rule — equal HEAD means one repository — **one row is shelved**, on
`repos/foundations.md`, and the second spelling is recorded here rather than published as a
separate address.

## 🔁 Restored by `p436` — the LMS-connector tier that a full-file rewrite deleted

> 🔴 **These rows are not new findings.** Each was promoted in an earlier pass with its
> grant read first-hand at a pinned SHA, recorded on [`agents/trending.md`](trending.md),
> and then **silently dropped by a later full-file rewrite** — the mechanism `Gap 435-B`
> named. `p436` measured the whole population (**171** claimed-and-absent addresses, not
> the 3 the register knew), re-read every payload below on **2026-10-25**, and restored
> this tranche. The verdict for all 171 is committed in
> [`evidence/promotion-ledger.2026-10-25-p436.tsv`](../evidence/promotion-ledger.2026-10-25-p436.tsv),
> and `gate-promotion-ledger` now **fails** if any row here is dropped again.

> 🔵 **Why the tier matters commercially**: every row speaks to an LMS a client already
> runs — Canvas, Moodle, Blackboard, Google Classroom — so it is the shortest path from an
> AI mandate to something inside the system of record. 🔵 **Read the permissions wording
> before the capability wording**: most of this cohort is read-only on purpose, and the
> rows that write do so only on explicit opt-in.

| Agent / repo | Licence (verified) | HEAD @ 2026-10-25 | Licence payload | What it does | Region |
|---|---|---|---|---|---|
| [BxnIceLemon/minerva-mcp](https://github.com/BxnIceLemon/minerva-mcp) | ISC | `534b7dc7b78e` | `LICENSE` 741 B · `5d3787deebf3` | Unofficial MCP server **and** CLI for the University of Leeds' Minerva (Blackboard Learn Ultra) plus Gradescope. Minerva access is read-only; the only mutating actions are Gradescope upload and regrade. **The user types password and MFA into their own browser window — the server never sees them.** | EMEA |
| [UKplus8HRS/bb-mcp](https://github.com/UKplus8HRS/bb-mcp) | MIT | `d639765bc267` | `LICENSE` 1 067 B · `02049138f239` | Local MCP server for Blackboard Learn, **institution-agnostic by design** — assumes no particular university, identity provider or academic calendar. Playwright driving a visible Edge window. | EMEA |
| [AnonymousOnyx22/google-classroom-student-mcp](https://github.com/AnonymousOnyx22/google-classroom-student-mcp) | MIT | `f3c1bd8e6a11` | `LICENSE` 1 072 B · `ed912ca72d9e` | Student-side Google Classroom MCP: classes, assignments and what is still owed. No sign-up; the learner's credentials go only to Google. | North America |
| [Mugen-Ibi/Classroom-MCP](https://github.com/Mugen-Ibi/Classroom-MCP) | MIT | `5f746bdae197` | `LICENSE` 1 081 B · `b77185922cd4` | Cloudflare Worker MCP giving read-only Google Classroom (courses, published coursework, own submissions) to MCP clients, deployed **per user into their own account**. Documents the 7-day refresh-token expiry under Google OAuth External/Testing — the operational catch most of this cohort omits. | APAC |
| [Mattlo0546/classroom-mcp](https://github.com/Mattlo0546/classroom-mcp) | MIT | `46e4ff4195b6` | `LICENSE` 1 067 B · `13c8ad755224` | **A single Python file with no dependencies** (3.9+, macOS/Linux/Windows): read-only student Classroom view plus slide and doc download to PDF, one folder per course. The lowest-friction row in the cohort. | EMEA |
| [supachai-j/google-classroom-mcp-project](https://github.com/supachai-j/google-classroom-mcp-project) | MIT | `9490c0fc068b` | `LICENSE` 1 090 B · `125a8bf7ce31` | Teacher-side Classroom MCP — courses, rosters, submissions, reporting. **Read-only by design: grade write-back is deliberately unsupported**, with CSV export as the bulk path. The explicit-refusal pattern an oversight regime asks for. | APAC |
| [charlie2233/coursebinder-ai-ready-google-classroom-exporter](https://github.com/charlie2233/coursebinder-ai-ready-google-classroom-exporter) | MIT | `54e1eccaf943` | `LICENSE` 1 068 B · `7f208bdb3cc4` | Browser-extension exporter: turns the Classroom content a logged-in user can **already see** into a local AI-readable archive. Needs no API credential — the route in where API access is refused. | North America |
| [sinh-x/personal-google-mcp](https://github.com/sinh-x/personal-google-mcp) | MIT | `6e6a98d957e0` | `LICENSE` 1 068 B · `5ed26262319d` | **Rust** MCP server over personal Google services: Classroom and Drive, with course details and announcements as typed tools. The only non-JS/Python runtime in the cohort. | APAC |
| [praisethefacts/dsh-plugin-google-classroom](https://github.com/praisethefacts/dsh-plugin-google-classroom) | MIT | `4115d38621e4` | `LICENSE` 1 064 B · `c35e96e7d382` | Configuration-only harness bundle that serves a Classroom MCP's read-only tools into an agent harness. **The packaging pattern rather than a server** — the row to copy when wrapping any of the above for a fleet. | EMEA |
| [PrahanG/Google-Classroom-MCP](https://github.com/PrahanG/Google-Classroom-MCP) | MIT | `5c675c96b901` | `LICENSE` 1 060 B · `f06ff8fa5a6c` | Google Classroom MCP carrying **both JavaScript and Python implementations** in one tree. | APAC |
| [Shiv-D-Coder/google-mcp-agent](https://github.com/Shiv-D-Coder/google-mcp-agent) | MIT | `206bff862a0e` | `LICENSE` 1 069 B · `2deff4ab7dff` | FastMCP agent unifying Gmail, Drive and Classroom tools — the cohort's one row that treats Classroom as part of a wider workspace surface. | APAC |
| [Teci-AI/moodle-mcp-connector](https://github.com/Teci-AI/moodle-mcp-connector) | MIT | `2318b9927da5` | `LICENSE` 1 103 B · `c8bcb50d415c` | MCP server over **Moodle's own REST web services**: courses, structure, full text of Pages/Books/Labels/Lessons, quizzes, grades, deadlines, completion — and content create/edit **only when explicitly enabled**. The supported seam into a GPL LMS without forking it. | EMEA |
| [The-Morrow-Project/Morrow-Bridge](https://github.com/The-Morrow-Project/Morrow-Bridge) | MIT | `b5e9993c5d53` | `LICENSE` 1 071 B · `f37f80963047` | Monorepo connecting an assistant the learner already uses to **Canvas and Moodle** for building and reviewing real coursework. States its own maturity honestly: Canvas checked on live test courses, Moodle early, Blackboard not shipped. | North America |
| [Jacob-Met/canvaspilot](https://github.com/Jacob-Met/canvaspilot) | MIT | `e75196e94c6c` | `LICENSE` 1 075 B · `85144488dcaf` | Canvas MCP + CLI with a **stay-open session broker**: works where student personal access tokens are disabled and Canvas sits behind SSO/MFA — the access problem most Canvas MCPs cannot solve. | North America |
| [arthurcuri/mcp-instructure-canvas](https://github.com/arthurcuri/mcp-instructure-canvas) | MIT | `fc3c813e76d0` | `LICENSE` 1 074 B · `161c1c8666c3` | Canvas MCP plus Telegram deadline notification and activity help, **instance-configurable** (the examples use PUC Minas's Canvas). v0.5.3, Portuguese-language docs, Docker packaging and an end-to-end validation page. | LATAM |
| [angelonrevelo/bettercanvasmcp](https://github.com/angelonrevelo/bettercanvasmcp) | MIT | `1f5a5969e502` | `LICENSE` 1 070 B · `fe401a64566c` | Student-side Canvas MCP built on the observation that **the popular Canvas MCPs are instructor consoles a student token cannot drive**. Writes only on explicit opt-in, reports when Canvas refused, and treats `submissions/self` as the only completion proof. | APAC |
| [sweeden-ttu/canvas-lms-mcp](https://github.com/sweeden-ttu/canvas-lms-mcp) | MIT | `13f357361fe8` | `LICENSE` 1 056 B · `06dcddbb6908` | Canvas LMS MCP scoped to a **named institution** (Texas Tech) — the single-tenant shape, useful as the template for a campus deployment. | North America |
| [a-ariff/canvas-mcp](https://github.com/a-ariff/canvas-mcp) | MIT | `28496f9ca414` | `LICENSE` 1 064 B · `040d00e3cf79` | Local Canvas MCP whose stated point is that **the API key stays on the machine** instead of being handed to a hosted server. | APAC |
| [Kuria-Mbatia/Canvas-MCP-server](https://github.com/Kuria-Mbatia/Canvas-MCP-server) | MIT | `c2fee6cb2fc0` | `LICENSE` 1 063 B · `fd34175ea8f9` | Canvas MCP with **composite tools** rather than thin API wrappers: student dashboard, course health report, assignment context with rubric and module prerequisites, prioritised attention filter. The most product-shaped row in the cohort. | North America |
| [Shashwatpog/poke-canvas-mcp](https://github.com/Shashwatpog/poke-canvas-mcp) | MIT | `4917cf253ef7` | `LICENSE` 1 072 B · `b60d2cd596b7` | Canvas MCP targeting a **consumer assistant over iMessage** — read-only student scope. Evidence that the surface is already leaving the IDE. | APAC |

🟢 **Grant re-read, not restated**: all 20 payloads returned `200` on
`raw.githubusercontent.com` on 2026-10-25, and the digests **match the ones the trend
shelf recorded at promotion time** — independent confirmation that the original evidence
was sound and only the shelf write was lost. Families via `p228`'s earliest-title
classifier: **19 MIT, 1 ISC**. Regions placed on the commit-offset channel
(`gate-offset-region`), never on a region word.

🔵 **Cohort currency, stated because a permissive licence has a shelf life (`Trend 9`)**:
13 of 20 have a HEAD inside October 2026; the two oldest are
`Shiv-D-Coder/google-mcp-agent` (2025-07-27) and `Kuria-Mbatia/Canvas-MCP-server`
(2025-10-08). 🔵 **Regional spread: 8 APAC, 6 EMEA, 6 North America, 1 LATAM** — and the
LATAM row (`arthurcuri/mcp-instructure-canvas`, PUC Minas) is the only one shipping
Portuguese-language documentation.

## 🆕 `p437` — The **EU AI Act obligation-tooling tier**, graded by whether its encoded deadline survives the Digital Omnibus

🔵 **Why this is a tier and not a footnote.** This base's `intel/market.md` names the
December 2027 Annex III deadline as *"the highest-value and most defensible education
engagement available anywhere right now"*. An engagement sold on a deadline needs a tool that
knows the deadline. 🔴 **Most of them do not** — and the failure is invisible to a licence
read, a star count or a freshness check.

Every payload below read first-hand on 2026-10-25, trailing newline included (see the method
note in `agents/trending.md` `p437`).

| Agent / repo | Licence (verified) | HEAD @ 2026-10-25 | Licence payload | What it does | Region |
|---|---|---|---|---|---|
| [tomdxb0004/eu-ai-act-risk-checker](https://github.com/tomdxb0004/eu-ai-act-risk-checker) | MIT | `41da87feb238` | `LICENSE` 1 073 B · `b7b08f330649` | 🟢 **The one to build on.** Browser triage of risk tier, obligations, duty-holder and per-obligation date, every result citing its article. `engine.js:32` encodes `highRiskAnnexIII: '2027-12-02'` **citing Reg. (EU) 2026/1744**; `engine.js:44` carries education as Annex III point 3; `engine.js:170-186` implements the Art. 6(3) exception **including the profiling override**. No build step, no backend, no telemetry. | EMEA |
| [sjgant80-hub/fall-euaiact](https://github.com/sjgant80-hub/fall-euaiact) | MIT | `5d8d27b65f68` | `LICENSE` 1 067 B · `0ddf3b67a14a` | Single-file browser compliance tool; dates correct post-Omnibus (Annex III 2 Dec 2027, Annex I 2 Aug 2028, Art. 50(2) marking 2 Dec 2026). 🟡 **No education-specific scope** — a general instrument, correct but not vertical. | EMEA |
| [Hiepler/EuConform](https://github.com/Hiepler/EuConform) | MIT | `011a5ad9bea2` | `LICENSE` 1 073 B · `65335056589f` | Offline evidence toolkit: Art. 5 / Art. 6 / Annex III classification quiz, **Annex IV-style report generation**, CrowS-Pairs bias evaluation. 🟡 Dates stated only as *"high-risk obligations apply from 2027"* — not wrong, not actionable. The Annex IV report generator is the part worth taking. 🟡 **`p442`: dual-licensed.** Beside the MIT root the tree carries **EUPL-1.2** (`LICENSE-EUPL` **13 240 B** · `3dcf9c6f6119`) — the European Union Public Licence, which is reciprocal and is the grant an EMEA public-sector buyer will recognise. 🔵 Take the MIT lane for a commercial deliverable; cite the EUPL lane when the client **is** a public body. 🔴 This base has no clause profile for EUPL (`GRANT-UNCALIBRATED`, `Gap 442-C`). | EMEA |
| [microsoft/agent-governance-toolkit](https://github.com/microsoft/agent-governance-toolkit) | MIT | `70a4ab8e8a04` | `LICENSE` 1 074 B · `7df20dcdf919` | Agent-governance controls with an EU AI Act checklist that enumerates Annex III including education, and notes the domain set can shift by delegated act. 🟡 **Carries no dates at all**, so it can be neither stale nor current — pair it with the risk-checker for timing. | Global |
| [AbdelStark/eu-ai-act-toolkit](https://github.com/AbdelStark/eu-ai-act-toolkit) | MIT | `fff58f6e8906` | `LICENSE` 1 056 B · `1126322e2cc8` | TypeScript SDK + CLI + web app; `data/annexes.json` carries Annex III **category 3 education** with all four statutory use cases. 🔴 **But do not quote its deadlines:** `packages/cli/src/commands/gaps.ts:199` hardcodes `'high-risk': '2026-08-02'`, its test suite pins that value, and `grep -rn '1744'` returns **nothing**. Take its annex data, not its dates. | EMEA |

### 🔴 The pattern across this tier, which is the actual finding

Three of these five tools encode a high-risk date. **Two encode the superseded one.** The
projects share no code and no authors, so this is convergent error: the pre-Omnibus
`2 August 2026` is baked across the EU-AI-Act open-source ecosystem, and every one of these
repositories is MIT, actively maintained and recently updated. 🔴 **Licence, stars and
freshness all fail to separate the correct tools from the wrong ones.** The only screen that
works is reading the date out of the payload — three greps, written down in
`repos/trending.md` `p437` and wired as a gate in `compose/patterns.md` Pattern AO.

## 🆕 `p440` — The first row shelved with its grant verified **clause by clause**, and it is not a build-on row

🟢 One new address this pass, stated as one. It is listed here rather than in the
permissive tier above because its grant is **network copyleft**, and `p440` is the pass
that made that grant readable: until this hour every AGPL payload on this base graded
`GRANT-UNCALIBRATED`.

| Agent / repo | Licence (verified) | HEAD @ 2026-10-25 | Licence payload | Grant check | What it does | Region |
|---|---|---|---|---|---|---|
| [AnkitClassicVision/tutor-engine](https://github.com/AnkitClassicVision/tutor-engine) | 🔴 **AGPL-3.0** | `30cbe59f37c3` | `LICENSE` 34 523 B · `0d96a4ff68ad` (branch `main`) | 🟢 **GRANT-PRESENT** under the `AGPL-3.0` profile — all eight operative clauses, §13 included | Adaptive tutor for ages 5–14 **and their parents**: short missions generated from the child's *real schoolwork*, mastery inferred from independent work rather than from chat, **bring-your-own model**, per-family encryption. 🟡 Author labels it early release and warns AI feedback can be wrong. | Global |

🔴 **Why this is not a build-on row, in one sentence a client can act on.** AGPL §13 —
the clause whose presence was confirmed above — obliges whoever *runs a modified version
over a network* to offer that version's Corresponding Source to its users. A hosted
tutor is precisely the shape §13 reaches. 🟢 **Integrate over an interface; never
vendor.** Same posture this file already carries for `Apomera/AlloFlow`.

🔵 **What is genuinely new is the check, not the row.** Every permissive row in the
table at the top of this file was verified by reading its payload and naming its family.
This row is the first verified by asking whether the payload contains **the words that
perform the grant** — which is the question `P1065` settled at pass 254 for Creative
Commons content licences, `p439` carried to MIT / Apache-2.0 / ISC, and `p440` carried to
the GPL family. A payload can name AGPL-3.0 and be 287 B; this one is 34 523 B and
complete, and the difference is now a column rather than an assumption.

🟡 **And the row's own supply tier is thin, which is worth saying.** The parent-facing
persona (`Trend 10`) still has few maintained answers, and this one is early, single
author, and under the grant that most limits what a studio can ship. It is a reference
architecture for *bring-your-own-model, per-family encryption* — not a dependency.

---

## 🆕 `p439` — The tail tier gets a **second page** and the yield more than doubles; and one of its rows is a payload **shorter than the grant it names**, which the code-licence path never asks about

🟢 **`Gap 438-C` bought, and its hypothesis held.** `p438` measured coverage by rank depth
and predicted new supply below roughly 40 ★. `p439` bought the next two pages it priced —
`ai-tutor` ranks **61–80** and `education-ai` ranks **21–40** — and the new-rate rose from
**9/89 (10.1 %)** to 🟢 **23/40 (57.5 %)**. Coverage does not just decay with rank; on this
corpus it **collapses** past rank 60. Full slug-by-slug record in
`evidence/p439-topic-depth.2026-10-25-p439.tsv`.

🔴 **And the tail's real character is not low stars, it is NO GRANT AT ALL.** Of the 23 new
addresses, **10 (43 %) carry no licence payload of any kind**, 1 would not resolve a default
branch, and 1 is 🔴 CC-BY-NC-SA-4.0 (`rajantripathi/open-course-rag-benchmark`, `LICENSE`
936 B · `86d64326f24d` @ `3074eaa83b7f` — **non-commercial, excluded, not shelved**). 🟢 That
leaves **11 shelvable**, below. 🔵 This is the stopping rule `Gap 438-C` asked for, answered
with a number: buying depth past rank 60 buys mostly **ungranted** addresses, so the next
page is worth buying for its payloads and not for its rows.

Every payload read first-hand on **2026-10-25** through `compose/code/lib/probe_payload.sh`
(sourced, not re-implemented), every `sha256₁₂` independently re-measured off
`raw.githubusercontent.com`, every HEAD from `git ls-remote`. Stars are the topic listing's
own figure at read time.

| Agent / repo | Licence (verified) | HEAD @ 2026-10-25 | Licence payload | What it does | Region |
|---|---|---|---|---|---|
| [Abelo9996/LearnOS](https://github.com/Abelo9996/LearnOS) | MIT | `f528067d714b` | `LICENSE` 1 077 B · `4679aa0db6a3` | Open "AI university": per-learner tutors over a mastery-based progression rather than a fixed syllabus. 9 ★. | Global |
| [ShowayLiao/Engineering-Exam-AI-Tutor](https://github.com/ShowayLiao/Engineering-Exam-AI-Tutor) | Apache-2.0 | `b113c4b574a6` | `LICENSE` 11 357 B · `c71d239df917` | Engineering-exam tutor shipped as a prompt architecture rather than an app — the whole artefact is the instruction set, so it ports to any runtime. The only patent-granting licence in this tier. | APAC |
| [X-RayLuan/Openclaw-Study-Coach](https://github.com/X-RayLuan/Openclaw-Study-Coach) | MIT | `59c4793b01e8` | `LICENSE` 1 066 B · `b48efd882d37` | K-12 tutoring skill pack across subjects, graded by year level, **with a parent-facing guide** — the parent surface of `Trend 10` as a skill rather than a platform. 8 ★. | APAC |
| [lecrix/netem-ai-predictor](https://github.com/lecrix/netem-ai-predictor) | MIT | `22ee956a0783` | `LICENSE` 1 075 B · `04a5cd187b32` | Single-file, serverless exam-question simulator for China's postgraduate English entrance test (NETEM). 🟡 **`P26` applies**: the code grant is permissive, the hosted model it calls is not the grant's to give. 8 ★. | APAC |
| [Weichenleeeee123/oh-my-chinese-teacher](https://github.com/Weichenleeeee123/oh-my-chinese-teacher) | MIT | `3949339d2f41` | `LICENSE` 1 091 B · `d1e0c4117d88` | Gaokao essay coach: topic analysis, outline, then graded feedback against the exam's own rubric. A marking surface pinned to one national assessment. 7 ★. | APAC |
| [umitkacar/memogen-ielts-flashcards](https://github.com/umitkacar/memogen-ielts-flashcards) | MIT | `dac37aeea89b` | `LICENSE` 1 078 B · `7a318295ce1f` | IELTS vocabulary as 3D interactive flashcards on a spaced-repetition schedule. Pairs with `fsrs4anki` on the trend record for the scheduling half. 6 ★. | EMEA — Türkiye |
| [lowellran/Study_via_AI](https://github.com/lowellran/Study_via_AI) | MIT | `0e7dcf8486b4` | `LICENSE` 1 066 B · `8f0b227698a5` | Socratic tutor over a Markdown knowledge base, with its own testing loop. 6 ★. | Global |
| [thendralmagudapathi/RAG-for-NCERT](https://github.com/thendralmagudapathi/RAG-for-NCERT) | MIT | `e3f233daa4d1` | `LICENSE` 1 077 B · `627670c5c6f5` | RAG grounded on **NCERT Class 11–12 textbooks** — India's national curriculum. 🟢 The **fourth** curriculum-grounding instance on these shelves, after Brazil's BNCC (`p387`), `os-taxonomy` (`p384`) and British Columbia (`p388`), and the first for India. | APAC — India |
| [Devanik21/AI-Nano-Course-Generator](https://github.com/Devanik21/AI-Nano-Course-Generator) | MIT | `57d584879648` | `LICENSE` 1 066 B · `1e4635354929` | Generates AI/ML micro-courses: modules, explanations and auto-graded quizzes. 🟡 Holder/owner mismatch — see the note below this table. | APAC — India |
| [Devanik21/FluentFlow](https://github.com/Devanik21/FluentFlow) | MIT | `b5197cd14b29` | `LICENSE` 1 066 B · `1e4635354929` | Language-learning platform with adaptive practice and grammar feedback. 🟡 **Byte-identical payload to the row above** (`1e4635354929`), same holder string. | APAC — India |

### 🔴 `spragginsdesigns/ai-tutor-webapp` — shelved **nowhere**, and it is the most instructive row of the pass

`LICENSE` **552 B** · `sha256₁₂ 5809eb2eab28` @ `963dfa9c55c7`, read 2026-10-25. Graded by
this base's own census: `titled_family = Apache-2.0`, `scan_verdict = PERMISSIVE`,
🔴 `stock = True`, 🔴 `needs_a_human = False`. **Every instrument said "permissive, no human
needed."** Read, the payload is the Apache-2.0 **APPENDIX notice** — its own words are
*"You may obtain a copy of the License at"* a URL — and the holder it names is
🔴 **Vercel, Inc.**, the Next.js template's notice carried unchanged into a tutor app. Two
things a client pays for, neither visible in that row:

1. 🔴 **Nothing in the repository grants anything over the code its author wrote.** The only
   copyright line present belongs to a third party.
2. 🔴 **Apache-2.0 §4(a) obliges a redistributor to give recipients a copy of the License.**
   A repository shipping only the pointer has not done it, so the obligation lands on
   whoever vendors it next — on an engagement, the client.

🔴 **And this is NOT a new class — which makes it worse.** `P1065` (pass 254) settled on this
base that **a pointer to a licence is not a grant**, and
`pass258-content-licence-family/content_licence.py::is_grant()` already implements it by
exactly the right method: look for the words that *perform* the grant, not the name of the
licence. 🔴 **It is scoped to Creative Commons content licences and never travelled to the
code-licence path**, so `is_stock()` and `needs_a_human()` — the predicates that grade MIT,
Apache-2.0 and BSD — have never asked the question for a single code payload. 🔵 That is this
base's signature failure mode (`lib/README.md` on pass 77 re-importing `P171`; `Gap 394-B` on
a standing gate whose rule never reached the writing path), not a discovery. 🟢 `Gap 439-A`
carries `P1065` one directory across, to the licence families a client actually
redistributes: `compose/code/p439-grant-presence/` (25 controls), `make gate-grant-presence`,
with `make grant-presence-census` for the live population.

### 🟡 Holder/owner mismatch, carried as a provenance note and not a licence one

Both `Devanik21` rows name `Copyright (c) 2025 **Debanik21**` — one letter off the account
that owns them, and the payloads are byte-identical. The MIT grant stands; what does not
resolve is the **notice obligation**, which requires reproducing a holder name that matches
no GitHub account. 🔵 Same shape as `dmontgomery40`/`dmoshehun-prog` on the verified tier
(`p433`): recorded, not treated as a blocker.

## 🆕 `p438` — The **tail tier**: eight permissive agent skills reached by buying one extra page of topic depth, and one of them carries a clause two of this base's instruments cannot read

🔵 **Why these eight are a tier and not a list.** `p433`–`p437` each recorded the global
discovery leg returning only duplicates. 🟢 `p438` measured that claim by rank depth instead
of restating it — **0/20 new at ranks 1–20, 2/20 at 21–40, 7/20 at 41–60** — so the head is
held completely and the only unshelved education supply sits below roughly 40 ★. These are
those rows. 🟡 Individually they are single-purpose skills, not foundations, and **this pass
adds nothing to `repos/foundations.md`** rather than promoting them there to make a count.

Every payload below read first-hand on **2026-10-25** through `compose/code/lib/probe_payload.sh`
(sourced, not re-implemented), bytes including the trailing newline per `p437`'s convention,
and every `sha256₁₂` independently re-measured off `raw.githubusercontent.com`.

| Agent / repo | Licence (verified) | HEAD @ 2026-10-25 | Licence payload | What it does | Region |
|---|---|---|---|---|---|
| [briannajzhang/personal-tutor](https://github.com/briannajzhang/personal-tutor) | Apache-2.0 | `d6c39db08574` | `LICENSE` 11 357 B · `c71d239df917` | Long-lived personal-tutor skill for agent CLIs: persistent learner model across sessions. The only patent-granting licence in this tier. | Global |
| [canyrtcn/PractiSQL](https://github.com/canyrtcn/PractiSQL) | MIT | `4ca8e479ab0c` | `LICENSE` 1 079 B · `c03af9304b8b` | Desktop SQL-learning workspace: local SQLite, visual schema rendering, hands-on practice with a tutor loop. No hosted dependency. | Global |
| [eugeniughelbur/doceo](https://github.com/eugeniughelbur/doceo) | MIT | `4c99d933127b` | `LICENSE` 1 072 B · `94b7323d4984` | One-screen visual lessons with learner memory and a feedback loop. ⚠️ Default branch is **`master`** — resolved by `ls-remote --symref`, never assumed. | EMEA |
| [yarikleto/claude-teacher-plugin](https://github.com/yarikleto/claude-teacher-plugin) | MIT | `bc6abdd00eda` | `LICENSE` 1 065 B · `b6519647c247` | Agent-CLI plugin that teaches, quizzes and tracks a per-learner knowledge model across sessions. | EMEA |
| [liunor/nlp-agent](https://github.com/liunor/nlp-agent) | MIT | `09b3caab56cd` | `LICENSE` 1 073 B · `ef01967408a8` | NLP-course platform: dialogue practice, knowledge content, service observability on the teaching path. | APAC |
| [abdulrdeveloper/klar-AI](https://github.com/abdulrdeveloper/klar-AI) | MIT | `c6deeeeb2626` | `LICENSE` 1 073 B · `2351980f79fd` | Multi-model student chat tutor. ⚠️ **`P26` applies**: the code grant is permissive, the hosted models it calls are not the grant's to give. | Global |
| [smashburger-dev/socratic-workshop](https://github.com/smashburger-dev/socratic-workshop) | MIT | `e23164c4aa50` | `LICENSE` 1 072 B · `7f3dec641d9f` | Socratic questioning tutor, portable across two agent CLIs. The cheapest pedagogy layer on these shelves. | Global |
| [fangyuan-3149/book-learning-tutor](https://github.com/fangyuan-3149/book-learning-tutor) | MIT **+ scope addendum — read it** | `f0ef6fc3acd7` | `LICENSE` 1 503 B · `54ceeac19921` | Turns a local book into a course with per-lesson teaching. 🔴 The payload appends a Chinese-language clause: the repository ships **no** book content, the operator supplies the material and **carries the copyright liability for it** — which on an education engagement means the client. Build-on with that clause in the statement of work, not without it. | APAC |

### 🔴 Declined this pass, with the reason on the row

| repo | grant (read first-hand) | why not |
|---|---|---|
| [pruettlazaro143-a11y/smc-ai-tutor](https://github.com/pruettlazaro143-a11y/smc-ai-tutor) | 🔴 **CC-BY-NC-SA-4.0** · `LICENSE` 19 018 B · `600ca4e25fe1`, HEAD `0787a0e29bd2` | Non-commercial. `PROHIBITED` for any Globant delivery, and the figure on the listing page does not change that. |

### 🔵 A payload-digest coincidence that is NOT an identity claim

`briannajzhang/personal-tutor`'s Apache-2.0 payload is **`11 357 B · c71d239df917`** —
**byte-identical** to the payload already published on this file for
[huggingface/smolagents](https://github.com/huggingface/smolagents). 🟢 That is the expected
behaviour of a stock licence text and is recorded here explicitly because `p349`'s
payload-digest instrument exists to say exactly this: **a shared digest across slugs is a
shared TEXT, never a shared repository.** Two unrelated projects both shipping the canonical
Apache-2.0 file is a corroboration of the measurement, not a collision.

### 🔴 The screening amendment this tier forces, which applies to every row above it

`fangyuan-3149/book-learning-tutor` grades `stock = YES`, `scan_verdict = PERMISSIVE`,
`titled_family = MIT` — and `p1054_verdict = MIT-BODY-PLUS:unclassified-addition` with
`needs_a_human = no`, from the same `bespoke_census.grade()` call. 🔴 Over this base's **238**
committed licence payloads, **7 of the 9** addition-bearing payloads are routed as needing no
human read, including `p427`'s own two-family specimen. 🟢 **So the standing instruction for
this file is now three columns, not one**: a row is cleared on `titled_family` **and**
`p1054_verdict` **and** a read of any bytes above the family's stock band. Full evidence,
line numbers and the remedy's price are on `agents/trending.md` `p438` and registered as
`Gap 438-A`.

## 🔴 Licence corrections — rows that are NOT what a badge-read would tell you

These are the findings that change a build decision. All re-measured 2026-10-25.

| Address | Previously recorded | **Actually, at HEAD** | Consequence |
|---|---|---|---|
| [pengusto/google-classroom-mcp](https://github.com/pengusto/google-classroom-mcp) | MIT (read correctly in three earlier passes) | 🔴 **Proprietary — "Pengusto Commercial License 1.0"**, `LICENSE` 3 053 B · `d84e558a5033` @ `3609bf6c5372` | **Do not build on this.** §2 grants source inspection only; §3, "Paid commercial agreement required", reaches *"an educational institution or training provider, whether nonprofit or commercial"* **by name** — exactly the buyer these shelves serve. Relicensed 2026-10-23, effective 2026-10-24. |
| [GeminiLight/awesome-ai-llm4education](https://github.com/GeminiLight/awesome-ai-llm4education) | MIT | 🔴 **No licence file anywhere in the tree** (`git ls-tree -r` @ `48f2d16ca617` returns none) | Ungranted. Fine to *read* as a research index; cannot be redistributed or vendored. |
| [withmarbleapp/os-taxonomy](https://github.com/withmarbleapp/os-taxonomy) | newly trending, assumed permissive | 🟡 **ODbL** (Open Database License), `LICENSE` 25 289 B · `77d2692c3d64` @ `7bd8b6794cb7` | A **share-alike data** licence, not a code licence. A derived curriculum database inherits ODbL. Usable, but it is a copyleft obligation on client data — flag before adoption. 🔴 **`p442`: there are TWO obligations, not one.** The tree also carries the full **CC BY-SA 4.0** at `LICENSE-CONTENT` (**18 375 B** · `cde7883b9050`, `CONTENT-COPYLEFT:share-alike`), so the **database** is ODbL and the **content** is CC BY-SA. 🔵 A taxonomy delivered to a client inherits both, and they are different share-alike regimes with different triggers. |
| [frappe/lms](https://github.com/frappe/lms) | MIT per some 2026 roundups | 🔴 **AGPL-3.0**, `license.txt` 33 893 B · `db1a87ba81e8` | Network copyleft. The "MIT" claim circulating in listicles is wrong. |
| [sakaiproject/sakai](https://github.com/sakaiproject/sakai) | Apache-2.0 per some roundups | 🟡 **Educational Community License**, `LICENSE` 11 120 B · `0688f62d04f1` | ECL-2.0 is an Apache-2.0 derivative and OSI-approved — permissive in practice, but it is not Apache-2.0 and should not be recorded as such. |
| [sdrangan/llmgrader](https://github.com/sdrangan/llmgrader) | “Open autograding engine” per search results and roundups | 🔴 **“PySilicon Research License”**, `LICENSE` 1 224 B · `4c8368a01cb6` @ `c5efaea7e9aa` | **Do not build on this.** Clause 1 grants *“non-commercial research, academic, and educational purposes”* only; clause 2 forbids commercial use without written permission. A studio engagement is commercial. 🔵 The trap: the file is named `LICENSE` and **opens with the verbatim MIT sentence** — only clause 2 reveals it. |
| [eth-lre/MathTutorBench](https://github.com/eth-lre/MathTutorBench) | “Open-source benchmark” (EMNLP 2025) | 🔴 **No licence file anywhere in the tree** (`git ls-tree -r` @ `6faed173ec2b` returns none), and the README cites **two different** licences: a CC-BY-4.0 badge on line 3, CC-BY-**SA**-4.0 in the licence section at lines 199–203 | Ungranted **code** (`main.py`, `models/`, `reward_model/`) offered under a *content* licence, or under none. Cite it; do not vendor or ship it. BY vs BY-SA is the difference between no obligation and a share-alike one. |
| [plastic-labs/tutor-gpt](https://github.com/plastic-labs/tutor-gpt) | Often listed simply as an open-source AI tutor | 🟡 **GPL-3.0**, `LICENSE` 35 149 B · `3972dc9744f6` @ `5c2f92416c04` | Integrate over an interface; do not fork into a deliverable. 🔵 Its payload is **not** the stock FSF digest this base records for Moodle/Chamilo (35 147 B · `8ceb4b9ee5ad`) — recorded so a digest sweep does not treat the near-miss as a match. |
| [Apomera/AlloFlow](https://github.com/Apomera/AlloFlow) | GitHub `license` field: **`NOASSERTION`** ("Other"); repo topics advertise `agpl` | 🔴 **AGPL-3.0-or-later**, `LICENSE` 35 442 B · `698099632698` @ `6194e51e8f1f` — standard AGPLv3 body, SPDX header `AGPL-3.0-or-later`, no added clauses | Network copyleft, and this is a *hosted* differentiation engine — the exact shape AGPL reaches. Genuinely valuable (UDL, WCAG, AAC, text-to-speech, offline-first, i18n) and the only maintained accessibility-first differentiation tool found. **Integrate over an interface; never vendor.** |
| [GarethManning/education-agent-skills](https://github.com/GarethManning/education-agent-skills) | GitHub `license` field: **`NOASSERTION`**; one roundup reported "CC BY-SA 4.0" without citing the file | 🟡 **CC BY-SA 4.0** — terms **restated**, not granted in the file. `LICENSE` 1 230 B · `f952182df4eb` @ `135d6275e7db` 🔴 grades `CONTENT-POINTER: not-a-grant` under this base's own `P1065` instrument (`pass258-content-licence-family/content_licence.py`): the payload says of itself *"This is a human-readable notice. The full legal terms are available at …/by-sa/4.0/legalcode"*. 🔵 The **terms it restates are accurate** — commercial use and adaptation are both expressly permitted and ShareAlike applies — but the operative text is incorporated by URL, so what binds a client is the canonical CC BY-SA 4.0 (18 375 B; for a live full-text specimen see `withmarbleapp/os-taxonomy`'s `LICENSE-CONTENT`). 🔴 A second pointer, 978 B · `f8366f5391f4`, sits at `mcp-server/LICENSE` (US spelling, four lines shorter): **two pointers, no grant text anywhere in the tree** (`p442`) | 907 ★ / 128 forks — the highest-traction *new* education address this window. Usable commercially, but **ShareAlike**: a derived skill pack must ship under CC BY-SA 4.0. That is a content-copyleft obligation on a deliverable, and it is the first of its kind on these shelves. See `Trend 29`. |
| [grasped-dev/staircase](https://github.com/grasped-dev/staircase) | "IEP goals reasoned over a FalkorDB graph of ELA and math standards" (Graph Hacks 2026) | 🔴 **No licence file anywhere in the tree** — `git ls-tree -r` @ `9236fce606c2` over all 33 files returns none | Ungranted. The most interesting *technique* in the IEP tier (standards graph + goal reasoning) and it cannot be used. Cite the approach; rebuild it. |
| [eakarsu/ai-special-education-iep-compliance](https://github.com/eakarsu/ai-special-education-iep-compliance) | README presents a full IEP-compliance product: eight AI workflows over React / Node / Postgres | 🔴 **No licence file anywhere in the tree** — `git ls-tree -r` @ `ec2516b76699` over all 29 files returns none | Ungranted, 0 ★, no description field. The single most complete-sounding IEP tool on GitHub is unusable as a base. |

### The MIT Google Classroom lane survives — at a different address

`pengusto`'s pre-relicensing MIT payload was **1 145 B · `a01639b20880`**.
[`vTanco/google-classroom-mcp`](https://github.com/vTanco/google-classroom-mcp) carries a
`LICENSE` of **exactly those bytes** at HEAD `9ba0070eff2f` — confirmed by digest equality,
not by inference. The teacher-side MIT lane is therefore **not lost**; it moved.

**The general lesson, which costs nothing to apply:** a permissive grade has a shelf life.
Nothing in a badge, a manifest or a cached listing tells you a repo was relicensed two days
ago. Re-read the payload at the SHA before an engagement commits to it.

## ⚠️ The platform tier is almost entirely copyleft

This is the single most consequential structural fact for an education engagement, and it
was re-measured in full today. **The permissive arm of education open source is the agent
layer, not the platform layer.**

| Platform | Licence (verified @ 2026-10-25) | HEAD | Build-on? |
|---|---|---|---|
| [OpenOLAT/OpenOLAT](https://github.com/OpenOLAT/OpenOLAT) | 🟢 **Apache-2.0** · `LICENSE` 10 982 B · `6dbc5b605ed0` | `d073ad444fe5` | ✅ University-grade LMS, **the only Apache-2.0 one**. Strongly under-used. |
| [learningequality/kolibri](https://github.com/learningequality/kolibri) | 🟢 **MIT** · 1 097 B · `3c056b34a476` | `44a4e68aac3e` | ✅ Offline-first; the LATAM/rural answer. |
| [sakaiproject/sakai](https://github.com/sakaiproject/sakai) | 🟡 **ECL** (Apache-derived) · 11 120 B | `4debc94780cc` | ✅ with notice; higher-ed consortium. |
| [moodle/moodle](https://github.com/moodle/moodle) | 🔴 GPL-3.0 · `COPYING.txt` 35 147 B · `8ceb4b9ee5ad` | `46c042e7da65` | Integrate alongside; do not vendor. |
| [openedx/edx-platform](https://github.com/openedx/edx-platform) | 🔴 AGPL-3.0 · 35 136 B · `e12d78569742` | `87cd3811a425` | Use **XBlock** (Apache-2.0) as the seam. |
| [exelearning/exelearning](https://github.com/exelearning/exelearning) | 🔴 AGPL-3.0 · 34 523 B · `0d96a4ff68ad` | `c848eca0018d` | Spain Ministry of Education-led authoring tool. |
| [chamilo/chamilo-lms](https://github.com/chamilo/chamilo-lms) | 🔴 GPL-3.0 · 35 147 B · `8ceb4b9ee5ad` | `2e5139a816d3` | Lightest to self-host; strong LATAM footprint. |
| [frappe/lms](https://github.com/frappe/lms) | 🔴 AGPL-3.0 · 33 893 B · `db1a87ba81e8` | `5d6df8e3ed8e` | Modern UX, network copyleft. |
| [bigbluebutton/bigbluebutton](https://github.com/bigbluebutton/bigbluebutton) | 🔴 LGPL-3.0 · 7 652 B · `e3a994d82e64` | `ec452b65043b` | Virtual classroom; link, don't fork. |
| [openeducat/openeducat_erp](https://github.com/openeducat/openeducat_erp) | 🔴 LGPL-3.0 · 8 241 B · `528f84036800` | `46a5d7d40082` | LMS+SIS on Odoo. |

**Engagement rule that follows:** put the AI in the **agent/MCP layer** (MIT) and talk to the
platform over its API or its component SDK. Three of ten platforms are permissive; building
AI *into* the other seven inherits their copyleft.

> `moodle/moodle` and `chamilo/chamilo-lms` ship a **byte-identical** 35 147 B GPL-3.0
> payload (`8ceb4b9ee5ad`) — the stock FSF text, as expected. Noted so a future digest
> sweep does not read the collision as a fork relationship.

---

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
  🆕 **`p442` — the tree carries two more payloads, and one of them is a usable lane.**
  `LICENSE_HISTORY` is **2 872 B · `b1567cc97632`, MIT, holder "Copyright (c) 2023-2025 Timothy
  Jaeryang Baek"** — the grant that governed the project **before** the branded relicensing — and
  `LICENSE_NOTICE` is **721 B · `9de72254becb`**, which grades 🔴 `GRANT-BY-REFERENCE` (every MIT
  clause missing, `refs: see-file`): a pointer, not a grant. 🟢 **So a client who needs a clean
  MIT gateway has a second option besides switching project: fork at a commit covered by
  `LICENSE_HISTORY`.** 🔴 That is a claim about history, so it must be pinned to a commit and read
  there — this base has not done that, and will not sell it until it has (`Gap 442-D`).

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
| [e9x/blackboard-mcp](https://github.com/e9x/blackboard-mcp) · [parkseokjune/unist-blackboard-mcp](https://github.com/parkseokjune/unist-blackboard-mcp) | — `ls-remote` returns nothing | **DEAD / private** — both listed by search results as live MIT servers *(`p386`)*. 🆕 `p451` **SEPARATES THEM, and they are not the same case:** `parkseokjune/unist-blackboard-mcp` is 🟢 **EXISTED → WITHDRAWN** — PyPI `unist-blackboard-mcp` `0.2.0` declares **MIT** and back-links this exact slug in four `project_urls`, so the grant is recoverable; `e9x/blackboard-mcp` is 🔴 **NO TRACE** — the npm name `blackboard-mcp` belongs to [`felipedias-ie/blackboard-mcp`](https://github.com/felipedias-ie/blackboard-mcp), a third party, so nothing supports the `e9x` address either way |
**13 of the 58 live addresses are not on `main`** (`master`, `develop`, `dev`, `release`,
`development`, `release_11`, `19.0`) — 🆕 `p386` adds **four more refs** to that list from 22 new
probes: **`tcd`** (`lukecarroll15/blackboard-mcp`), **`master`** (`Loganxgreaves/blackboard-mcp`,
`aureuserp/aureuserp`), **`2.2`** (`krayin/laravel-crm`, a version branch with no `main`) and
**`trunk`** (`apache/ofbiz-framework`). Resolving the ref **before** reading the licence is not
optional; a `main`-assuming read returns "no licence" for every one of them.

