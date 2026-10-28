---
industry: education
region: Global
updated: 2026-10-28
---

# Foundational education repos

> 🟢 **`p509` (`2026-10-28`) — A FOUNDATION ROW THAT LOOKED UNGRANTED IS MIT, AND THE DEFECT WAS A CAPITAL LETTER. 🟢 EVERY FOUNDATION'S LICENCE IS NOW BYTE-ATTESTED.**
> 🟢 **[`labmlai/annotated_deep_learning_paper_implementations`](https://github.com/labmlai/annotated_deep_learning_paper_implementations)
> — 67,603★, MIT, `archived: false`, 2,172 files — read from bytes for the first time on this base:
> `master/license`, 1,082 B, `sha256 22c7cae23a2b00cb`, opening `The MIT License (MIT)`.**
> 🔴 **It reached that reading through a false alarm worth recording.** A 19-path probe returned
> **no payload** while the API returned `spdx_id: MIT` — which looked like a **new licence state**
> that `T33` does not cover: *detector asserts a recognised grant, no payload exists*. 🟢 **The state
> does not exist. The grant is at lowercase bare `license`** — no extension, no capital — and the
> probe's path list carried `license.txt` but not `license`. 🔵 **A licence reader must be
> case-insensitive and must accept an extensionless name**, and this base's own foundations shelf is
> where that would first have gone wrong.
> 🟢 **Of 137 shelf addresses swept, 119 carry a grant and 81 are permissive**, each with bytes and
> sha256: [`licence-byte-census.2026-10-28-p509.tsv`](../evidence/licence-byte-census.2026-10-28-p509.tsv).
> 🔴 **Four foundation-adjacent addresses carry NO grant at all**, proven by tree enumeration rather
> than inferred from a 404: [`eth-lre/mathtutorbench`](https://github.com/eth-lre/mathtutorbench)
> (**46★**, 40 files, EMNLP 2025 Oral), [`kixlab/TutorCaseBench`](https://github.com/kixlab/TutorCaseBench)
> (**0★**, 11,059 files), [`h9-tect/AI-Roadmaps`](https://github.com/h9-tect/AI-Roadmaps) (**373★**)
> and [`jaltekruse/Free-Math`](https://github.com/jaltekruse/Free-Math) (**74★**, 558 files).
> 🔵 **Two of those are academic benchmarks this base cites for evaluation, and an unlicensed
> benchmark cannot ship inside a client deliverable** — it can only be *run against* one. That
> distinction belongs on the row, not in a footnote.
> 🔴 **`Gap 504-A` reconciliation: 13 queried / 13 returned on two batches**, `incomplete_results:
> false` both times; `archived: false` on all 13. 🟢 `openedx/edx-platform` was **not** in either
> batch this pass, so the four-pass silent-omission streak is neither extended nor broken.
> 🔴 **Gate posture: `make hooks` DENIED (`Code from External`).** Nothing here is gate-attested.

### 🟢 `p509` — the permissive foundation tier, byte-attested

🔵 **Why this table and not a licence word:** a client engagement that ships one of these inherits a
grant, and *"MIT"* in a cell is a claim about a file nobody on the engagement has read. These are the
bytes. Full set of 119 in the census TSV; the foundations tier is reproduced here.

| foundation | grant | bytes | sha256 (16) | branch read |
|---|---|---|---|---|
| [`labmlai/annotated_deep_learning_paper_implementations`](https://github.com/labmlai/annotated_deep_learning_paper_implementations) | 🟢 **MIT** | 1,082 | `22c7cae23a2b00cb` | `master/license` |
| [`huggingface/smolagents`](https://github.com/huggingface/smolagents) | 🟢 **Apache-2.0** | 11,357 | `c71d239df91726fc` | `main/LICENSE` |
| [`microsoft/autogen`](https://github.com/microsoft/autogen) | 🟢 **MIT** (code) | 1,141 | `c2cfccb812fe4821` | `main/LICENSE-CODE` |
| [`EleutherAI/lm-evaluation-harness`](https://github.com/EleutherAI/lm-evaluation-harness) | 🟢 **MIT** | 1,067 | `a806e42547620dff` | `main/LICENSE.md` |
| [`CAHLR/OATutor`](https://github.com/CAHLR/OATutor) | 🟢 **MIT** | 1,105 | `5baaaf977a28e9fd` | `main/LICENSE` |
| [`AI-for-Education/pedagogy-benchmark`](https://github.com/AI-for-Education/pedagogy-benchmark) | 🟢 **MIT** | 1,064 | `4cdfd8894a136670` | `main/LICENSE` |

🔴 **`microsoft/autogen` is the row to read twice.** Its root `LICENSE` is **CC-BY-4.0 (18,650 B)**
and its **code** grant is `LICENSE-CODE` **MIT (1,141 B)**. 🟢 The shelf's MIT reading is **correct**,
and a probe that stopped at the first filename would have "corrected" it to a content licence.
**Where a repo splits code and content, name the file the grant came from.**


> 🔴 **`p508` (`2026-10-28`) — NO NEW FOUNDATION, AND `Gap 504-A` IS FINALLY CHARACTERISED RATHER THAN RE-REPORTED: THE CONTROL THAT `p504` ASSERTED HAS NOW BEEN RUN.**
> 🟢 **`p504` wrote that on this channel *"a missing row and a nonexistent repo are the same
> observation."* This pass proves it.** `repo:openedx/edx-platform` queried alone returns
> *Validation Failed — "The listed users and repositories cannot be searched either because the
> resources do not exist or you do not have permission to view them"*, and
> `repo:zzzz-nonexistent-org-9931/nope-repo-9931` — **a repository that does not exist** — returns the
> **identical error string**. 🟢 Two further tightenings: the silent drop reproduces at **batch size
> 2** (`repo:openedx/edx-platform repo:moodle/moodle` → **1 returned, `incomplete_results: false`**),
> so it is **not** a pagination or batch-size effect; and `repo:openedx/frontend-app-learning` answers
> normally, so **exclusion stays per-repository**, re-attested a fourth consecutive pass.
> 🟢 **Two mechanical facts about the batch form, both new and both cheap to lose:** the explicit
> `repo:A OR repo:B` shape is now **REJECTED** by the validator (*"Logical operators only apply to
> text, not to qualifiers"*), while **space-separated repeated `repo:` qualifiers still behave as OR**
> — that is the batch form a future pass must use. Query budget: **~250 characters**, so batches run
> 7–10 slugs.
> 🔴 **And a query-shape defect worth more than either:** multi-term free-text legs **collapse to
> zero**. `LLM agent grading rubric assessment students stars:>80` → **`total_count: 0`** while these
> shelves carry six grading repositories; the Spanish-language leg
> (`educación inteligencia artificial docentes open source stars:>20`) → **0**. 🟢 **The productive
> discovery shape on this channel is `topic:` plus a star floor**, and LATAM-language discovery does
> not work through free text at all. Reads:
> [`query-shape.2026-10-28-p508.tsv`](../evidence/query-shape.2026-10-28-p508.tsv).
> 🟢 **Shelf re-read, 64 addresses: 64 queried / 64 returned.** No silent omission in any batch other
> than the known `openedx/edx-platform` exclusion, which was isolated deliberately.
> 🔴 **Channel posture inverted since `p506`:** `github.com` HTML is **403** this session,
> `api.github.com` is **403**, and **`raw.githubusercontent.com` is 200**. 🟢 `p506`'s
> *"the two broken channels are complementary"* survives, but only **one** of the two limbs is left:
> the bytes. Reads: [`channel-probe.2026-10-28-p508.tsv`](../evidence/channel-probe.2026-10-28-p508.tsv),
> [`api-shelf-read.2026-10-28-p508.tsv`](../evidence/api-shelf-read.2026-10-28-p508.tsv).
> 🔴 **Gate posture: `make hooks` DENIED (`Code from External`), fourteenth denial in fifteen passes.**

> 🟢 **`p507` (`2026-10-28`) — ONE NEW PERMISSIVE FOUNDATION, IN A CATEGORY THIS SHELF HAS NEVER CARRIED.**
> 🟢 **Added:** [`PetoiCamp/OpenCat-Quadruped-Robot`](https://github.com/PetoiCamp/OpenCat-Quadruped-Robot)
> — **5,518★ / 650 forks, MIT, `archived: false`**, pushed 2026-09-08. **Embodied STEM** — a
> classroom robot framework over Arduino, Raspberry Pi and block-coding, with simulation. Every
> other repo on this shelf teaches through a screen; this one is the first that teaches through a
> device, and it is MIT.
> 🟢 **Shelf re-read, 45 addresses on the API channel: 45 queried / 44 returned.**
> 🔴 **[`openedx/edx-platform`](https://github.com/openedx/edx-platform) silently omitted a THIRD
> consecutive pass** (`incomplete_results: false`). `Gap 504-A` is a **deterministic per-repository
> property of the search index**, not a transient — reconcile queried against returned every call.
> 🟢 **`archived` check:** `true` on exactly two addresses — [`menthorlabs/menthor`](https://github.com/menthorlabs/menthor)
> and [`ably-labs/realtime-quiz-framework`](https://github.com/ably-labs/realtime-quiz-framework) —
> **and both are already carried with an end-of-life flag.** 🔴 A probe this pass reported `menthor`
> as an unflagged live defect; **it was wrong**, because it grepped the slug and never read the
> sentence that already says *"but **archived** — carried as a 🇧🇷 LATAM data point, not a build
> target."* The premise was true and the conclusion false.
> Reads: [`api-shelf-read.2026-10-28-p507.tsv`](../evidence/api-shelf-read.2026-10-28-p507.tsv),
> [`new-addresses.2026-10-28-p507.tsv`](../evidence/new-addresses.2026-10-28-p507.tsv),
> [`probe-errors.2026-10-28-p507.tsv`](../evidence/probe-errors.2026-10-28-p507.tsv).

### 🟢 `p507` — added to the foundations shelf

| Repo | Licence | Why it is foundational | ★ / forks |
|---|---|---|---|
| [`PetoiCamp/OpenCat-Quadruped-Robot`](https://github.com/PetoiCamp/OpenCat-Quadruped-Robot) | 🟢 **MIT** (`license.spdx_id`, API-read) | 🟢 **The embodied-STEM base this shelf has lacked.** A quadruped robot-pet framework built for STEM teaching, coding and robotics education — Arduino + ESP32 + Raspberry Pi, block-coding for younger learners, reinforcement-learning and simulation paths for older ones. For a K-12 or STEM-lab engagement it is the only permissive starting point here that produces a **physical** learner artefact. Companion board: [`PetoiCamp/OpenCatEsp32-Quadruped-Robot`](https://github.com/PetoiCamp/OpenCatEsp32-Quadruped-Robot) (**521★**). | **5,518 / 650** |

🔴 **Not added, licence in every case** —
[`echo-loop/Echo-Loop`](https://github.com/echo-loop/Echo-Loop) (**4,549★, AGPL-3.0**),
[`penecho/penecho`](https://github.com/penecho/penecho) (**2,509★, AGPL-3.0**) and
[`TarrySingh/…-Tutorials`](https://github.com/TarrySingh/Artificial-Intelligence-Deep-Learning-Machine-Learning-Tutorials)
(**4,018★, `NOASSERTION` — no OSI licence detected**). 🔵 **Three of the five highest-starred new
education repos this pass are unusable as client bases.** That ratio, not the star counts, is the
finding.


> 🟢 **`p505` (`2026-10-28`) — THE STANDING CHECKS THIS SHELF INHERITED FROM `p504` WERE RUN, AND THEY PASSED.**
> 🟢 **`Gap 504-A` reconciliation applied to every call:** 4 slugs queried, **4 returned**,
> `incomplete_results: false` — no silent omission in this batch. 🟢 **`T29` `archived` check: `false`
> on all four addresses**, so no repeat of the `ably-labs/realtime-quiz-framework` defect.
> 🔴 **`Gap 483-K` is now known to be unclosable from this session by ANY address.** `p504` left
> `eur-lex.europa.eu/eli/reg/2026/1744/oj` for the next pass; it, `digital-strategy.ec.europa.eu`
> and five further `.europa.eu` hosts are **403 at the CONNECT**, attested by the proxy's own
> `connect_rejected` log. This is a **host-policy denial of the whole domain family**, not a
> resolution failure — so it is not a probe to retry, and the **31 July 2026** outlier cannot be
> checked at its own source. Quote **2 Dec 2027** / **2 Aug 2028** and name the reading.
> 🔴 **Three instrument gaps registered that bear on how this shelf grades rows** —
> `505-A` (`pushed_at` is not a shipping signal), `505-B` (`api.github.com` is 403 on raw `curl`
> though the MCP channel answers, so the channel table needs a channel column) and `505-C`
> (a lexicographic tag sort understates the newest release by six versions). Narrative:
> [`agents/trending.md`](../agents/trending.md) `p505`. Reads:
> [`api-reconciliation.2026-10-28-p505.tsv`](../evidence/api-reconciliation.2026-10-28-p505.tsv).

> 🟢 **`p506` (`2026-10-28`) — `Gap 504-C` IS CLOSED FROM BYTES, AND THE TWO BROKEN CHANNELS TURN OUT TO BE COMPLEMENTARY.**
> 🟢 **[`openedx/edx-platform`](https://github.com/openedx/edx-platform)'s licence is now READ AT ITS
> CURRENT PIN**, not inferred from an HTML sidebar: at `f73b7ae64dd5`, path `LICENSE`, **35,136
> bytes**, title block **`GNU AFFERO GENERAL PUBLIC LICENSE Version 3`**, sha256 `e12d78569742`,
> git blob `1eb391f38837`. 🟢 **The shelf's AGPL-3.0 reading is confirmed on this base's own
> authority — the bytes.**
> 🔵 **The generalisation is worth more than the closure:** the repository the API search channel
> **cannot enumerate at all** (`Gap 504-A`, reproduced for a **third** consecutive pass this pass —
> 129 queried, 128 returned, `"incomplete_results": false`) is **fully readable on
> `raw.githubusercontent.com`**. 🟢 **The two channels have complementary coverage**, so an address
> invisible to one is not an unverifiable address — it is a routing question.
>
> 🔴 **`p504` (`2026-10-28`) — A FOUNDATION ROW ON THIS SHELF IS INVISIBLE TO THE CHANNEL `p502` CALLED AUTHORITATIVE, AND ANOTHER WAS AN ARCHIVED REPOSITORY SOLD AS A BUILD BASE.**
> 🔴 **[`openedx/edx-platform`](https://github.com/openedx/edx-platform) cannot be read on the API
> search channel at all**: queried alone it raises **HTTP 422**, and batched with 24 other slugs it
> is **silently dropped from a payload that reports `"incomplete_results": false`** (`Gap 504-A`).
> The exclusion is **per-repository** — `openedx/frontend-app-learning` and
> `openedx/openedx-translations` both answer normally. The repo exists: `ls-remote` returns
> `refs/heads/master`. 🟢 **Every claim this file made about the row is correct** — AGPL-3.0, 8.2k★,
> 4.4k forks, branch `master`, all re-confirmed on the HTML channel — but its **pin had drifted and
> is re-pinned: `d9aaee456069` → `f73b7ae64dd5`**. 🔵 The licence at the new SHA is the sidebar, not
> bytes (`Gap 504-C`).
> 🔴 **[`ably-labs/realtime-quiz-framework`](https://github.com/ably-labs/realtime-quiz-framework)
> reads `archived: true`** and this file recommended it as *"the permissive base for live classroom
> response"* with no end-of-life flag. Flagged here and in
> [`verticals/solutions.md`](../verticals/solutions.md); **`archived` is now part of the standing
> batch read**, because it costs nothing on a call that already returns stars.
> 🟢 **`Gap 502-A` is CLOSED**: all **87** shelf addresses re-read on the API channel, and the
> carried figures held — **15 of 15 exact-integer cells identical**, every rounded cell right to its
> stated precision. The 31× `educhain` error was a **stale carry**, not a bad instrument.
> 🔵 **Eight rows on this shelf are served off a non-`main`/`master` ref** — `rosariosis` → `mobile`,
> `GibbonEdu/core` → `v31.0.00`, `openeducat_erp` → `19.0`, `tutors-sdk/tutors` → `development`,
> `bigbluebutton` → `v4.0.x-develop`, `ILIAS` → `release_11`, `oh-my-paper` → `v2`,
> `tutor` → `release`. A probe that assumes `main` reads the wrong tree on all eight.
> 🟡 **`Gap 502-D` was closed at `p503`, and `p504` REPRODUCED both reads on a different channel**
> (`raw.githubusercontent.com` via `curl`) to **byte-identical** results. 🔴 **What was still broken:
> the stale text on THIS shelf.** `p503` recorded it *"corrected by closure above"* but only edited
> the register — the shelf still read *"neither payload was byte-read"*. Fixed here; **a correction
> recorded in the register is not a correction applied to the shelf** (`Gap 504-E`).
> 🔴 **`learning-commons-org/evaluators` is NOT cleanly permissive**: MIT code and CC BY 4.0
> prompts, but **CC BY-NC-SA 4.0 on both annotated corpora**, which a paid engagement may not use.
> 🔴 **`learning-commons-org/knowledge-graph` cannot be licence-graded at repo level at all** —
> its data is Open / Open+Gated / Gated **per download**, and a compiled build inherits every
> included dataset's terms. Reads:
> [`noassertion-bytes.2026-10-28-p504.tsv`](../evidence/noassertion-bytes.2026-10-28-p504.tsv).
> Reads: [`api-shelf-reconciliation.2026-10-28-p504.tsv`](../evidence/api-shelf-reconciliation.2026-10-28-p504.tsv),
> [`api-silent-omission.2026-10-28-p504.tsv`](../evidence/api-silent-omission.2026-10-28-p504.tsv).

> 🟢 **`p501` (`2026-10-28`) — the retained canonical licence set is now VERIFIED INFRASTRUCTURE, not
> just retained bytes.** [`evidence/canonical/`](../evidence/canonical/)'s 12 payloads were
> re-resolved this pass: **12/12 byte-and-blob-SHA identical to `MANIFEST.tsv`**, and **11/11
> operatively identical to the same paths at the publisher's current ref**, with a negative control
> that fires on tampered expectations. 🔵 `spdx/license-list-data` HEAD is still the exact commit
> `p499` pinned (`f715b366…`), so the pin is the publisher's current state. 🔴 Two caveats a later
> pass must carry: amendment detection is **established but untested** (nothing has drifted yet), and
> **`MANIFEST.tsv`'s last column carries prose after the URL on one row** — parse the first token,
> never the whole cell (`Gap 501-D`). 🔴 `www.gnu.org` and `opensource.org` still return `000`, so
> every GNU-family canonical here remains **single-sourced from SPDX** (`Gap 499-C`, unmoved).
> Instrument: [`compose/code/p501-abstention-and-reresolve/`](../compose/code/p501-abstention-and-reresolve/);
> reads: [`canonical-reresolve.2026-10-28-p501.tsv`](../evidence/canonical-reresolve.2026-10-28-p501.tsv).
>
> 🔴 **And the discovery axis under every "foundational repo" claim on this shelf is one axis wide.**
> `topic:ai-in-education` returned **65% rows new to this base** against `topic:edtech`'s 19.2%
> (`Gap 501-A`). Nothing on this shelf is withdrawn — but *"foundational for education AI"* here means
> *"foundational among what `topic:edtech` and this base's named-project queries surfaced"*, and that
> is a narrower claim than the heading makes.

**Pass `p491` — reads of 2026-10-27.** `p490` (earlier the same day) rewrote this file; `p491`
**extends** it: **two new platform rows** read from bytes, **Fedena finally resolved**, and an
**arithmetic correction to p490's own census**. Pre-p490 sections remain in
[`archive/2026-10-27-p490-pre-rewrite/foundations.md`](../archive/2026-10-27-p490-pre-rewrite/foundations.md).
New evidence:
[`licence-and-stars.2026-10-27-p491.tsv`](../evidence/licence-and-stars.2026-10-27-p491.tsv).

These are the systems an education engagement starts *from* — the ones that already hold the
students, the courses, the enrolments and the grades. The AI goes on top; see
[`compose/patterns.md`](../compose/patterns.md).

Every license below was read from `raw.githubusercontent.com` at the pinned SHA. Evidence:
[`licence-and-stars.2026-10-27-p490.tsv`](../evidence/licence-and-stars.2026-10-27-p490.tsv).

## The licence picture is the headline

**The education platform layer is overwhelmingly copyleft.** Of **19** foundational platforms now
read from bytes, **3 are permissive** — and both platforms added this pass are copyleft, so the
permissive numerator has not moved in two passes while the denominator keeps growing. Every
incumbent LMS — Moodle, Open edX, Canvas — is GPL or AGPL. This is the single most commercially
important fact in this file: a hosted, closed derivative of the market-leading education platforms
is not available on any of them.

| | count | repos |
|---|---|---|
| Permissive (MIT / Apache-2.0) | **3** | `oppia`, `kolibri`, `OpenOLAT` |
| GPL / LGPL (hostable, derivative must share) | 10 | `moodle`, `chamilo`, `ILIAS`, `h5p`, `GibbonEdu`, `tao-core`, `rosariosis`, `bigbluebutton`, `openeducat_erp`, **`frappe/education`** |
| AGPL (network copyleft — reaches hosted SaaS) | 6 | `edx-platform`, `canvas-lms`, `frappe/lms`, `tutor`, `anki`, **`learnhouse`** |

🔴 **Arithmetic correction to `p490`.** `p490` published "16 foundational platforms … 3 are
permissive" with a census reading 3 + **8** + 5 = 16. Its own GPL/LGPL cell already *named nine
repos*, and its two tables already *listed seventeen rows* (3 permissive + 14 copyleft). The
count was off by one and the stated total was an undercount: p490's real figure was **17**, not
16. With this pass's two rows it is **19**. The permissive count of 3 was correct throughout and
is unaffected — but any downstream deck quoting "16 platforms" is quoting a miscount.

## Permissive — the ones you can build a closed derivative on

🔴 **Heading corrected `p493`** — it read *"the three"* while the table below it already held four
rows after `p492` added `openmeetings`, and `p493` restores a fifth. **A hard-coded count in a
heading goes stale silently; the table is the census, not the heading.**

| Repo | License | ★ | SHA read | Role |
|---|---|---|---|---|
| [oppia/oppia](https://github.com/oppia/oppia) | Apache-2.0 | **6,950** *(🟢 `p506`, API; `archived: false`)* | `bc73ecf9cf71` | Interactive lesson platform with built-in structured "explorations". Byte-identical to canonical Apache-2.0. Default branch is `develop`, not `main`. 🟢 **`p506`: this row is the SECOND RUNG of the permissive education tier** — [`agents/top.md`](../agents/top.md) claimed the next permissive education-specific row after `OpenMAIC` (41,705★) was `k12-teacher-skills` at 595★; **this row sits between them and that claim is retracted there.** The real step is **41,705 → 6,950, ~6×**. |
| [learningequality/kolibri](https://github.com/learningequality/kolibri) | MIT | 1,200 | `dbe14ef6c499` | **Offline-first** learning platform. The one row here designed for no-connectivity deployment — the decisive property for rural LATAM, Africa and APAC programmes. Default branch `develop`. |
| [dodona-edu/dolos](https://github.com/dodona-edu/dolos) | **MIT** | **355** | `74b101785bad` | **Source-code plagiarism / academic-integrity engine** — 1 084 B, `sha1 8f6f3815d28d`; **3,865 commits**, the most-maintained repo in this file. Ghent University (`dolos@ugent.be`). 🟢 **Restored `p493`: `p296` recorded this as *already a foundation row* and this KB's identity gate refused a duplicate promotion on that basis — then a later full-file rewrite deleted the row the gate had defended.** The gate worked; the rewrite did not. |
| [OpenOLAT/OpenOLAT](https://github.com/OpenOLAT/OpenOLAT) | Apache-2.0 | 448 | `3736d48fa685` | Full Java LMS, Apache-2.0 (10,982 B). The only permissively-licensed *full* LMS found. Swiss-origin, strong EMEA higher-ed footprint. |

## Copyleft — real systems, with the obligation named

| Repo | License | ★ | SHA read | Role / constraint |
|---|---|---|---|---|
| [bigbluebutton/bigbluebutton](https://github.com/bigbluebutton/bigbluebutton) | LGPL-3.0 | 9,300 | `ac97a8bfdc20` | Virtual classroom / web conferencing. LGPL — linking is permitted, so this is the most integration-friendly copyleft row. Default branch `v4.0.x-develop`. |
| [openedx/edx-platform](https://github.com/openedx/edx-platform) | 🟢 **AGPL-3.0** *(`p506`: **read from bytes** at `f73b7ae64dd5` — `LICENSE`, 35,136 B, title block `GNU AFFERO GENERAL PUBLIC LICENSE Version 3`, blob `1eb391f38837`; `Gap 504-C` CLOSED)* | 8,200 *(🔵 `p504`: HTML channel — **the API still cannot see this repo**, `Gap 504-A`, 3rd consecutive pass)* | 🟢 **`f73b7ae64dd5`** *(`p504` re-pin; stable at `p506`)* | The Open edX LMS + Studio. Dominant in higher ed and workforce. AGPL: hosting a modified copy for a client triggers source release. Default branch `master`. |
| [moodle/moodle](https://github.com/moodle/moodle) | GPL-3.0 | **7,556** *(🟢 `p504`, API; prior rounded cell 7,600)* | `46c042e7da65` | Largest installed base and the largest plugin ecosystem (2,000+). Grant is at `COPYING.txt`, **not** `LICENSE` — a root-`LICENSE` probe reports "no grant" here. |
| [instructure/canvas-lms](https://github.com/instructure/canvas-lms) | **AGPL-3.0** | 6,900 | `1c9f0bb8013e` | The open LMS by Instructure; heavy North America higher-ed share. AGPL. Default branch `master`. |
| [frappe/lms](https://github.com/frappe/lms) | **AGPL-3.0** | 3,400 | `6054772c0426` | Frappe-framework LMS. **Widely published as MIT — it is not.** Grant at `license.txt` (lowercase), 33,893 B, AGPL-3.0; the GitHub sidebar agrees. |
| [learnhouse/learnhouse](https://github.com/learnhouse/learnhouse) | **AGPL-3.0** | **2,427** *(🟢 `p504`, API; prior rounded cell 2,400)* | `2d75337273ac` | **New row `p491`.** "Next-gen open source learning platform" — modern course/content platform. At 2,400★ it outranks Kolibri and Chamilo, and was absent from this KB entirely. AGPL confirmed on both channels (`LICENSE`, 34,522 B; sidebar `AGPL-3.0 license`). Default branch **`dev`**. |
| [frappe/education](https://github.com/frappe/education) | GPL-3.0 *(declared only)* | 682 | `73ce33ef2719` | **New row `p491`.** Frappe school-management / SIS app — **a different product from `frappe/lms`, under a different license family.** Its grant is a **19-byte** `license.txt` reading `License: GNU GPL V3` with **no license text at all**; GitHub's classifier cannot resolve it and shows a bare "License" link. See the note below. Default branch `develop`. |
| [ankitects/anki](https://github.com/ankitects/anki) | **AGPL-3.0** | 32,300 | `d87cb22bf337` | Spaced-repetition engine; the reference implementation of SRS scheduling. AGPL. Useful as an algorithm reference even where the code can't be taken. |
| [overhangio/tutor](https://github.com/overhangio/tutor) | **AGPL-3.0** | 1,100 | `aa5d1a764b6c` | Docker-based Open edX distribution — the realistic way anyone actually deploys Open edX. Default branch `release`. |
| [chamilo/chamilo-lms](https://github.com/chamilo/chamilo-lms) | GPL-3.0 | 1,000 | `2d1e97ee4244` | LMS focused on ease of use and accessibility. Notable francophone + LATAM public-sector footprint. |
| [francoisjacquet/rosariosis](https://github.com/francoisjacquet/rosariosis) | GPL-2.0 | 647 | `fa5f4b66caf4` | Student Information System for school management. **Correct path — `RosarioSIS/RosarioSIS` is a 404** and was cited on this KB. |
| [GibbonEdu/core](https://github.com/GibbonEdu/core) | GPL-3.0 | 635 | `65f86bf061fa` | K-12 school management platform (teachers, students, parents, leadership). Default branch `v31.0.00`. |
| [ILIAS-eLearning/ILIAS](https://github.com/ILIAS-eLearning/ILIAS) | GPL-3.0 | 505 | `db9582e3cd3e` | German-origin LMS, strong DACH public-sector and university use. Default branch `release_11`. |
| [h5p/h5p-php-library](https://github.com/h5p/h5p-php-library) | GPL-3.0 | 152 | `1e21b7a2da4a` | Interactive content types (the H5P core). Embeds into Moodle/Canvas/Open edX; the standard way interactive exercises get authored. |
| [openeducat/openeducat_erp](https://github.com/openeducat/openeducat_erp) | LGPL-3.0 | 900 | `46a5d7d40082` | Education **ERP** on Odoo — admissions, fees, hostel, library, timetable. The Odoo-for-education answer. Default branch `19.0`. |
| [oat-sa/tao-core](https://github.com/oat-sa/tao-core) | GPL-2.0 | 64 | `d9b3da5e6b0a` | Computer-based **assessment** platform core (QTI). The serious open assessment/exam engine. |

## The 19-byte license, and why it matters more than it looks

`frappe/education`'s entire grant is the string `License: GNU GPL V3` — 19 bytes, no license body.
Three consequences, none of them academic:

1. **GitHub cannot classify it.** The sidebar shows a bare "License" link with no SPDX identifier,
   so every tool that trusts the GitHub license field — including this KB's page-fetch channel —
   reports *unknown*, not *GPL-3.0*.
2. **It is a declaration, not a text.** GPL-3.0 is enforced through its own terms; a repository
   that names the license without shipping it still signals GPL-3.0 intent, but a client's counsel
   will ask for the text. Treat the family as **GPL-3.0 and the paperwork as incomplete**.
3. **Two Frappe education products, two license families.** `frappe/lms` is **AGPL-3.0** (p490,
   read at `license.txt`, 33,893 B) and `frappe/education` is **GPL-3.0** (19 B). Anyone who
   generalises "Frappe education apps are X" is wrong whichever X they pick.

## Fedena: resolved, and the Apache-2.0 claim does not survive contact with the repository

`p490` recorded Fedena as "could not be confirmed … not carried as a row." It resolves — to **two**
repositories, both of which `git ls-remote` reaches:

| repo | ★ | grant at SHA | sidebar |
|---|---|---|---|
| [projectfedena/fedena](https://github.com/projectfedena/fedena) | 547 | 🔴 **none** (`68a84ac445bf`) | no license shown |
| [foradian/fedena](https://github.com/foradian/fedena) | 4 | 🔴 **none** (`333477b06f1d`) | no license shown |

Both are "Fedena SIS"; the 4★ one is a **fork** of the 547★ one. Neither ships a license file under
any of the nine names probed. The **Apache-2.0** that comparison tables and vendor blogs print for
Fedena traces to a single sentence in the README — *"Fedena is released under the Apache License
2.0"* — and a README sentence is not a grant.

🔴 **Not carried as a permissive row, and the reason is now evidential rather than "unresolved."**
This *strengthens* the finding below: the one candidate that would have broken "no permissive SIS
exists" turns out to have no license at all. Also note the 40,000-schools / 100-countries figures
attached to Fedena in listicles describe the **commercial hosted product**, not these repositories.

## Branch-name trap, worth its own note

**Twelve** of these repos do **not** default to `main` (p491 adds `learnhouse` → `dev` and
`frappe/education` → `develop`; p490's prose said "six" while its own list named ten):
`oppia`, `kolibri` and `frappe/education` (`develop`), `learnhouse` (`dev`),
`edx-platform` and `canvas-lms` (`master`), `tutor` (`release`), `openeducat_erp` (`19.0`),
`GibbonEdu/core` (`v31.0.00`), `ILIAS` (`release_11`), `bigbluebutton` (`v4.0.x-develop`),
`tao-core` (`develop`), and `projectfedena`/`foradian` `fedena` (`master`). Any raw-content fetch
that hardcodes `/main/` returns 404 on all of them — which reads as "file absent" rather than "wrong branch". Resolve the ref with
`git ls-remote --symref` first.

## Declared gaps

- **No permissive SIS exists — confirmed harder this pass.** Every student-information system
  found (`rosariosis` GPL-2.0, `GibbonEdu` GPL-3.0, `openeducat_erp` LGPL-3.0, `openSIS` GPL-2.0,
  `frappe/education` GPL-3.0-declared) is copyleft, and **Fedena — the only candidate published as
  Apache-2.0 — ships no license grant at all**. A client needing a closed-source SIS derivative has
  no open starting point. That is a build, not a fork.
- **No permissive assessment/QTI engine exists.** `tao-core` is GPL-2.0 and is the only
  substantial one.
- ~~**`Fedena` could not be confirmed.**~~ 🟢 **Closed this pass** — it resolves to two repos, both
  unlicensed. See the section above. The claim was not wrong about the repos existing; it was wrong
  about them being licensed.
- **Commit recency is still absent from this file.** The page-fetch channel does not expose the
  latest-commit date (every fetch this pass returned a commit *count* and no date), and
  `api.github.com` is 403 for unattached repos. So **no row here can be shown to be maintained** —
  `fedena` at 547★ may well be abandoned and this file cannot tell. Rows carry a pinned SHA, which
  proves existence and content but not liveness.


## 🆕 `p492` — `2026-10-28` — the permissive numerator moves 3 → 4

Evidence: [`licence-and-stars.2026-10-28-p492.tsv`](../evidence/licence-and-stars.2026-10-28-p492.tsv).
Narrative: [`repos/trending.md`](trending.md).

`p491` recorded that "the permissive numerator has not moved in two passes while the denominator
keeps growing." 🟢 **It moved this pass**, and in the layer where this file's only option was
copyleft.

| repo | licence | ★ | SHA read | note |
|---|---|---|---|---|
| [apache/openmeetings](https://github.com/apache/openmeetings) | **Apache-2.0** | 688 | `79b71bcb39f8` | Virtual classroom / web conferencing: video, IM, **whiteboard**, collaborative document editing; media via **Kurento Media Server**. Apache-2.0 read from **51 425 B** (`sha1 d30124557187`); the sidebar shows only an unnamed "License" link, the bytes are unambiguous. Latest release **`v9.1.0`, a security release**. Default branch `master`. **ASF governance** rather than a single maintainer. |

### The census, corrected

| | `p491` published | `p492` |
|---|---|---|
| platforms read from bytes | 19 | **20** |
| permissive (MIT / Apache-2.0 / BSD) | 3 | **4** |
| GPL / LGPL / AGPL and other copyleft | 16 | **16** |
| permissive *full LMS* | 1 (`OpenOLAT`) | **1** — unchanged; **OpenMeetings is not an LMS** |

🔵 **The standing finding survives the correction.** The education platform layer is still
**16 of 20 copyleft**, and every hard gap this file established **still holds**: **no permissive
SIS exists** (both `fedena` repos ship no grant at all) and **no permissive assessment/QTI engine
exists** (`tao-core` remains GPL-2.0). OpenMeetings closes a **conferencing** gap and nothing else.

### How to read this row against BigBlueButton — honestly, in both directions

| | [`bigbluebutton`](https://github.com/bigbluebutton/bigbluebutton) | [`apache/openmeetings`](https://github.com/apache/openmeetings) |
|---|---|---|
| ★ | **9,300** | 688 |
| licence | LGPL-3.0 — **linking permitted** | **Apache-2.0** |
| verdict | **still the default** for a live-classroom deployment | a **considered fallback**, not a recommendation |

**BigBlueButton is 13× larger and remains the right default.** LGPL already permits linking, which
is why this file calls it the friendliest copyleft here. The case OpenMeetings uniquely serves is
narrow and real: a deliverable that must ship **modified platform source inside a proprietary
product**, where LGPL's linking allowance does not help. **That case is rare — but this file
previously had no answer for it.** Verify the Kurento dependency and the `v9.1.0` security notes
before proposing it.

### 🔵 Recorded as a teaching resource, deliberately not a foundations row

[`labmlai/annotated_deep_learning_paper_implementations`](https://github.com/labmlai/annotated_deep_learning_paper_implementations)
— **MIT**, 1 082 B, `sha1 b3428e1f52c0` (`2be1800d141e`), **67,600★**. At 67.6k it is the
largest-starred MIT repo this KB has read and would top any table it entered. It holds **no
students, no courses, no enrolments, no grades** — it is 60+ annotated PyTorch paper
implementations, i.e. CS-education *content*. **A foundation here is a system that already holds
the records.** This is not one.

🔵 **Probe-list fix worth more than the row:** its licence file is lowercase **`license`**. A probe
trying only `LICENSE`/`LICENSE.md` reports "no licence" on an MIT repo — the `fedena`
false-negative mechanism in reverse. **Add lowercase `license` to the nine probed names.**

### 🟢 The maintenance gap is partly closed

This file has declared, for several passes, that "no row here can be shown to be maintained."
**That was too strong.** The page-fetch channel **does** expose tagged releases with dates —
`openmeetings v9.1.0`, `canvas-mcp v1.16.0` (Oct 2026), `DeepTutor v1.6.15` (`2026-10-19`),
`education-agent-skills v3.1.0` (`2026-10-22`). For any repo that tags releases, **liveness is
readable**. The remaining limit is real but narrower: repos that never tag have no signal, and
`api.github.com` stays 403 for unattached repos. **Next pass should read a release date for every
row in this file** — it is available and this file was not using it.


## 🆕 `p493` — `2026-10-28` — the census was measuring this KB's bookkeeping, not the ecosystem

Reads: [`licence-and-stars.2026-10-28-p493.tsv`](../evidence/licence-and-stars.2026-10-28-p493.tsv).
Narrative and the full list of dropped rows: [`agents/trending.md`](../agents/trending.md) `p493`.

🔴 **`p490` rewrote `agents/top.md` in full and `p383`/`p391`/`p392` rewrote this file in full.
A full-file rewrite re-derives its tables from the rewriting pass's own reads, so any row an
earlier pass promoted but that pass did not re-read is deleted without a marker.** Eight addresses
this KB had recorded as promoted are absent from both shelf files at HEAD `cb6a4be`; `dolos` is the
one that belongs here and it is restored above.

### The census, corrected again — and the correction is about the denominator's authority

| | `p491` | `p492` | `p493` |
|---|---|---|---|
| platforms read from bytes | 19 | 20 | **21** |
| permissive (MIT / Apache-2.0 / BSD) | 3 | 4 | **5** |
| copyleft | 16 | 16 | **16** |
| permissive *full LMS* | 1 | 1 | **1** — `OpenOLAT`, unchanged |

🔴 **Do not read the `4 → 5` as ecosystem movement.** `p492`'s `3 → 4` was a real find
(`apache/openmeetings`). **`p493`'s is a repair**: `dolos` was always in the ecosystem and was
previously in this file. Two passes in a row have now moved the permissive numerator for
**different reasons**, and conflating them would turn a bookkeeping fix into a false trend.

### What still holds, and what does not

🟢 **Holds, and `p493` re-confirms it:** the **full-LMS** layer is copyleft-bound —
`OpenOLAT` (Apache-2.0, 448★) is the only permissive full LMS, against Moodle (GPL-3.0),
Open edX (AGPL-3.0), Canvas (AGPL-3.0), `frappe/lms` (AGPL-3.0, widely mispublished as MIT) and
`learnhouse` (AGPL-3.0). **No permissive SIS exists** (both `fedena` repos ship no grant).
**No permissive assessment/QTI engine exists** (`tao-core`, GPL-2.0). These are the gaps that
actually constrain an engagement and none of them moved this pass.

🔴 **Does not hold:** the generalisation that *the education stack* is copyleft-bound. With the
restored rows (see [`repos/trending.md`](trending.md) `p493`), the courseware, tutoring-platform,
teacher-workflow, academic-integrity and evaluation layers each have a permissive option, and an
end-to-end all-permissive stack is assemblable for the first time — wired up as
[`compose/patterns.md`](../compose/patterns.md) `P493-1`. **The constraint is specific to the
LMS/SIS/assessment core, and saying so is both more accurate and more useful than the blanket
claim.**

### 🔵 Declared gap, unchanged and restated

**No permissive SIS and no permissive QTI assessment engine** — searched again this pass across the
brief's platform query (`open source platform education ERP SIS student information system MIT
Apache 2026`). 🔴 **The query returned no permissive candidate at all**: OpenEduCat (LGPL-3.0),
RosarioSIS (GPL-2.0), `frappe/education` (GPL-3.0), Unifiedtransform (GPL-3.0), openSIS and Gibbon
(GPL-3.0). **Every education ERP/SIS this KB can find is copyleft.** That is now a four-pass
consistent result and should be treated as a property of the sector, not of the search.

## 🆕 `p494` — `2026-10-28` — census unchanged, and the denominator's authority is re-tested

Reads: [`licence-and-stars.2026-10-28-p494.tsv`](../evidence/licence-and-stars.2026-10-28-p494.tsv).
Narrative: [`../agents/trending.md`](../agents/trending.md) `p494`.

🟢 **No new foundation rows, no drift, no licence changes.** `p493`'s correction — that this file's
permissive census was measuring **this KB's bookkeeping rather than the ecosystem** — stands, and
this pass re-tested it the only way that is meaningful: by looking for *more* dropped material.

🔴 **It found some, and this time it was prose, not a row.** `p493` proved that full-file rewrites
silently delete promoted **table rows**, and fixed eight. `p494` finds the same mechanism deleting
**paragraphs**: an entire APAC jurisdiction posture (Singapore's Model AI Governance Framework, its
generative-AI framework, its **agentic AI framework**, and AI Verify) was removed by `p315`'s rewrite
of [`../intel/market.md`](../intel/market.md) and left no marker. 🔴 **A dropped row can be found by
`grep`-ing a repo URL. A dropped paragraph has no key to grep for** — which makes prose loss the
larger and wholly undetected surface. See [`../intel/trends.md`](../intel/trends.md) `T14`.

🔵 **Why that belongs in this file.** This file's census is a count over rows, and `p493` established
that the count's authority depends on the shelf being complete rather than on the ecosystem being
small. `p494` extends the caution: **completeness cannot be audited for prose at all with the tools
this KB has**, so any claim in this file that rests on narrative context — rather than on a
byte-pinned row — carries that uncertainty. **The row-level census is sound; the prose around it is
not audited.**

### 🟢 Re-reads this pass

| repo | KB pin | `p494` read | verdict |
|---|---|---|---|
| [`dodona-edu/dolos`](https://github.com/dodona-edu/dolos) | MIT, `74b101785bad` | not re-read this pass | 🟢 `p493`'s restoration row stands; 3,865 commits |
| [`HugeCatLab/ChatTutor`](https://github.com/HugeCatLab/ChatTutor) | AGPL-3.0, 34 522 B | **AGPL-3.0**, **34 522 B**, `sha1 3cd688cb1bd7` @ `7d9e9052bc5a` | 🟢 **byte-identical** — re-read because a `p494` discovery query returned it as if new |

🔴 **Declared gap, unchanged and restated for a fifth pass.** [`OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT)
(Apache-2.0) remains **the only permissive full LMS**, and there is still **no permissive SIS and no
permissive QTI exam engine** — so `T2`'s binding constraint holds at the institutional layer and
nowhere else. An engagement needing enrolment plus a gradebook has one permissive answer; an
engagement needing a SIS or a standards-based exam engine has **none**, and the copyleft conversation
is unavoidable. **Say so in week one.**


## 🆕 `p495` — `2026-10-28` — the census is unchanged, and the LGPL anchor is byte-read for the first time

🟢 **No change to the permissive numerator or the denominator this pass.** No foundations candidate
was promoted, and the reason is a supply fact rather than an absence of effort: the mandated
vertical-platform query — `open source platform education ERP CRM MIT Apache` — **returned no
MIT- or Apache-licensed education platform for the third consecutive pass**. What it returns is
`OpenEduCat` (**LGPL-3.0**), `Apache OFBiz` (Apache-2.0 but **not education**), generic MIT CRMs
(not education), and `CK-ERP` (a 2010 release, licence unconfirmed, effectively dead).

🔵 **That is `p493`'s conclusion arriving from a third independent direction and it should now be
treated as structural:** in the education **platform** layer, the permissive licences are not
where the mature systems are. The mature systems are GPL/LGPL/AGPL, and the engagement question
is never "find a permissive LMS" but **"which obligation can this client carry."**

### 🟢 `openeducat_erp` — the row this shelf points LATAM and APAC engagements at, now verified from bytes

| field | before `p495` | `p495` first-hand read | channel |
|---|---|---|---|
| pin | `46a5d7d40082` | 🟢 `46a5d7d40082` — **unchanged** | `git ls-remote` |
| licence | `LGPL-3.0` *(shelf tag)* | 🟢 **LGPL-3.0 confirmed from the payload** — `8 241 B`, `sha1 2979df12244d`, 178 lines, titled *"GNU LESSER GENERAL PUBLIC LICENSE, Version 3"* | `raw.githubusercontent.com` |
| attribution | — | 🔴 **DEFECT: line 1 of `LICENSE` reads *"For copyright information, please see the COPYRIGHT file"* — and `COPYRIGHT` returns `404`** | `raw` probe |

🔴 **Why the dangling `COPYRIGHT` matters, and it is not pedantry.** LGPL-3.0 is a *conditional*
grant: §4 and the GPL-3.0 terms it incorporates require preserving copyright notices and stating
changes. 🔴 **The repository points its notice obligation at a file that does not exist**, so an
integrator cannot discharge the notice requirement from the grant alone — there is nothing
authoritative to reproduce. 🔵 **Practical instruction for an engagement:** reproduce the `LICENSE`
file verbatim, cite the **pin** (`46a5d7d40082`) as the provenance of what you received, and
**ask the maintainers for the `COPYRIGHT` file in writing** rather than reconstructing attribution
from commit authorship — which `p349`/`ACTION ZZ-bn` already established is not a reliable
ordering.

🔵 **This is the same genus as the *19-byte license* note above**: the licence *name* is not the
grant. The grant is the bytes, and the bytes here are correct but **incomplete by their own
reference**.

### 🟢 Pins re-read this pass

| repo | pin | verdict |
|---|---|---|
| [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | `46a5d7d40082` | 🟢 stable + licence byte-read |
| [`naufaldi/teacher-exam`](https://github.com/naufaldi/teacher-exam) | `ed5bf6359413` | 🟢 **MIT byte-pinned** — `1 071 B`, `sha1 25cb945a99ab` *(a trending row, not a foundations row — the generator is a hosted proprietary model)* |

### 🔴 Declared gap, restated and now *registered* rather than merely restated

🔴 **No permissive education platform exists at the ERP/SIS/LMS layer.** Searched again this pass
with the brief's own query; found nothing new. 🟢 **This absence is now a registered claim in**
[`../compose/code/p495-prose-claim-gate/claim_register.tsv`](../compose/code/p495-prose-claim-gate/claim_register.tsv)
**(`NO-PERMISSIVE-PLATFORM`)**, because `p494` established that a declared gap deleted by a later
rewrite is indistinguishable from coverage — and this gap is load-bearing: three patterns choose
their base on it.



## 🆕 `p496` — `2026-10-28` — the census does not move, and the vertical-platform leg is now **three passes empty**

🔵 **Nothing this pass promotes a foundations row, and that is the honest result rather than a quiet
one.** The eight addresses discovery produced (see [`../agents/top.md`](../agents/top.md) `p496`) are
all *application-layer* — IEP drafting, rubric grading, plain-language rendering. **None is
infrastructure**, so none belongs here. Recording that explicitly, because an unchanged file looks
identical to an unexamined one.

### 🟢 Pins re-read this pass — and two branch-name traps in one sweep

| repo | KB pin | `p496` `git ls-remote --symref` | default ref |
|---|---|---|---|
| [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | `46a5d7d40082` | `46a5d7d40082` | 🔵 **`refs/heads/19.0`** — a version branch |
| [`oppia/oppia`](https://github.com/oppia/oppia) | `bc73ecf9cf71` | `bc73ecf9cf71` | 🔵 **`refs/heads/develop`** |
| [`AI-for-Education/pedagogy-benchmark`](https://github.com/AI-for-Education/pedagogy-benchmark) | `21a43a395ab4` | `21a43a395ab4` | `refs/heads/main` |
| [`Selleo/mentingo`](https://github.com/Selleo/mentingo) | `e137ca47cbec` | `e137ca47cbec` | `refs/heads/main` |

🔴 **This file's branch-name note is stronger than it reads.** Two of the four anchors above do **not**
default to `main`, and they are the two a LATAM or APAC engagement is most likely to clone. A licence
or liveness probe that hard-codes `main` reports both as **nonexistent** — not as unlicensed, which
is the more dangerous of the two failure modes because "missing" tends to be retried while
"unlicensed" tends to be believed. 🟢 `git ls-remote --symref` resolves the real ref in one call and
every read in this pass uses it.

### 🔴 The vertical-platform leg returned a single vendor, for the third pass running

The brief's platform query (`open source platform education ERP SIS LMS MIT Apache self-hosted`)
returned **nine pages from one domain — `openeducat.org`** — in eight languages, and no second
platform at all.

🟢 **It does corroborate the byte read `p495` made:** OpenEduCat is **LGPL-3.0** (8 241 B,
`sha1 2979df12244d`), not the MIT or Apache the query asked for, and the vendor's own glossary page
is what states the permissive/copyleft distinction. 🔴 **So the query's own premise returned
nothing**: there is still **no permissive education ERP/SIS platform** on these shelves, and the
LGPL-3.0 anchor remains the recommendation for exactly the reason `p495` recorded — LGPL's obligation
attaches to the *module*, not to the whole deployment, which is survivable where AGPL is not.

### 🟡 Recorded, deliberately **not** a foundations row

[`SahilC/AutomaticEssayGrading`](https://github.com/SahilC/AutomaticEssayGrading) — **MIT**, 1 074 B,
`sha1 cd4c5b7304aa` at `8bf6dc6b678b`, 13★, 55 commits, default ref **`master`**. Classical ML essay
scoring: SVM, decision trees, random forests, LSTM. **No LLM anywhere in it.**

🔵 **Why it is worth a line despite being old and small:** it is a *comparator*, and this sector has
almost none. When a client asks why rubric scoring needs a model at all, this is the pre-LLM baseline
that answers the question with code rather than assertion. 🔴 **It is not a dependency** — it is
TensorFlow-era research code and this KB does not propose building on it.

### 🔴 Declared gap — restated, and now with the reason it keeps recurring

- 🔴 **No permissive (MIT / Apache / BSD) education ERP or SIS platform.** Third consecutive pass
  that the mandated platform query returns no such thing. The permissive answer in the *full-LMS*
  layer remains **OpenOLAT** (Apache-2.0) alone; in the *education-ERP* layer there is **no
  permissive answer at all**, and `openeducat_erp` (LGPL-3.0) is the recommendation by elimination.
- 🔴 **No foundational repository originated in LATAM or Africa.** Unchanged. 🔵 `p496` adds a
  supply-side datum rather than a search artefact: the function-shaped queries that broke the
  *agent*-layer drought this pass produced **zero** infrastructure addresses from either region.
  **The gap is in infrastructure supply, not in this KB's queries** — which is a different and more
  defensible sentence than the one this file carried before.

## 🆕 `p497` — `2026-10-28` — the census does not move, the **vertical-platform leg is four passes empty**, and the "no MIT ERP" question is now answered

Evidence: [`licence-and-stars.2026-10-28-p497.tsv`](../evidence/licence-and-stars.2026-10-28-p497.tsv),
[`branch-ref-census.2026-10-28-p497.tsv`](../evidence/branch-ref-census.2026-10-28-p497.tsv),
[`saturation-census.2026-10-28-p497.tsv`](../evidence/saturation-census.2026-10-28-p497.tsv).

### 🔴 The census is unchanged: 19 platforms, 3 permissive

**No platform row added or removed.** The vertical-platform discovery leg is now **four consecutive
passes empty** (`p494`–`p497`).

🟢 **But this pass asked the question the census implies and got an answer**, which is better than a
fourth empty leg: *does a permissively-licensed education ERP exist at all?* Searched explicitly.

| candidate | licence | verdict |
|---|---|---|
| [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | LGPL-3.0 | already the KB's row; the Odoo-for-education answer |
| ERPNext | GPL-3.0 | lists Education among its verticals; copyleft |
| Odoo Community | LGPL-3.0 | the thing OpenEduCat is built on |
| Dolibarr | GPL-3.0 | ERP+CRM, no education vertical |
| Apache OFBiz | **Apache-2.0** | 🔵 permissive **but has no education vertical** — ERP/CRM primitives only |

🔴 **Conclusion, and it is a conclusion rather than a backlog item: there is no permissively-licensed
education ERP.** The only permissive ERP found (OFBiz) has no education domain model, and every
system that *does* model students, enrolments, fees and timetables is GPL, LGPL or AGPL.

🟢 **This strengthens `T2` instead of narrowing it.** The copyleft constraint is not an artefact of
this KB's sampling at the LMS layer — it holds independently at the **ERP** layer, reached by a
different query. For a client needing a closed derivative of an education *ERP*, the honest answer is
**build the domain model, or accept LGPL-3.0 and keep the Odoo modules separable**. There is no third
option to find, and future passes should stop looking for one.

### 🔴 The branch-name trap: the note above needs upgrading from two variants to five

The *"Branch-name trap, worth its own note"* section above was written for `19.0`. It is now a
five-variant pattern, each resolved by `git ls-remote --symref` this pass:

| repo | `default_ref` | ★ | status |
|---|---|---|---|
| [`francoisjacquet/rosariosis`](https://github.com/francoisjacquet/rosariosis) | **`refs/heads/mobile`** | **647** | 🔴 **NEW `p497` — and it is a row in the table above.** This KB's own foundational SIS has a default ref that reads as a feature branch |
| [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | `refs/heads/19.0` | 900 | recorded; also a row above |
| [`oppia/oppia`](https://github.com/oppia/oppia) | `refs/heads/develop` | — | recorded `p496` |
| [`TaiRuiQu/oh-my-paper`](https://github.com/TaiRuiQu/oh-my-paper) | `refs/heads/v2` | 1 | NEW `p497` |
| [`AgnellusX1/GodsEye`](https://github.com/AgnellusX1/GodsEye) | `refs/heads/PreProduction` | 30 | NEW `p497`, archived |

🔴 **Two of the five are foundational rows in this very file** (`rosariosis`, `openeducat_erp`), so a
licence re-verification script that assumes `main` would report **this KB's own platform layer** as
partly nonexistent. 🔵 `mobile` and `PreProduction` are the variants to fear: they are
indistinguishable from feature branches by eye.

### 🟢 `rosariosis` re-read from bytes this pass — the row is correct

| field | KB record | `p497` read | verdict |
|---|---|---|---|
| HEAD SHA | `fa5f4b66caf4` | `fa5f4b66caf4` | 🟢 stable, 11th stable pin this pass |
| default ref | — | **`refs/heads/mobile`** | 🔴 newly recorded |
| licence | GPL-2.0 | **GPL-2.0**, 15 214 B, `sha1 58cb1cfbf839`, title block *"GNU GENERAL PUBLIC LICENSE Version 2, June 1991"* | 🟢 confirmed from bytes |
| ★ | 647 | **647** | 🟢 exact |

🟢 **Four of four recorded fields reproduce.** Set against `p496`'s finding that one of four re-read
byte counts did **not** reproduce, the running tally on `T14` (this KB's records are not
self-verifying) is now **seven of eight reproduced across two passes**. 🔵 The practice that surfaces
the errors is re-reading a pin before building on it — keep doing it.

### 🔵 The SIS axis, ranked for the first time

`topic:student-information-system` holds **180** repositories. The four above ~9★ —
`rosariosis` (647), `academico` (409), `openSIS-Classic` (347), `koakademy` (9) — are **all already
held here**. 🟢 The platform layer this file covers is enumerated at the top of its distribution; the
tail below ~80★ is student coursework and single-institution projects, which is why it produces no
rows. 🔴 **This axis is spent for discovery** — its value this pass was the `mobile` branch trap, not
a platform.

---

## 🆕 `p498` — `2026-10-28` — the permissive numerator moves, and the census denominator was wrong by one

🟢 **Added to the foundations shelf** — read as payloads at pinned commits:

| Repo | Licence | Why it is foundational | ★ / forks |
|---|---|---|---|
| [`virgiliojr94/book-to-skill`](https://github.com/virgiliojr94/book-to-skill) | **MIT** (1 068 B · blob `b000bdffeaa2`, at `LICENSE.md`) | The document-to-agent-knowledge step every education build needs and most rebuild badly. Python; default ref 🔴 `master`. | 36 339 / 3 858 |
| [`beltromatti/get-it`](https://github.com/beltromatti/get-it) | 🟡 **Apache-2.0, §6 edited** (11 359 B · blob `29492aec7faa`) | A working knowledge-graph + spaced-repetition loop over arbitrary source material — the learner-model substrate the permissive shelf has otherwise lacked. 🇮🇹 EMEA. | 1 138 / 136 |
| [`DozenTwelve/Papermorph`](https://github.com/DozenTwelve/Papermorph) | **MIT** (1 069 B · blob `f461737043ac`) | 🟢 **Emits SCORM.** The only new row that lands inside an institutional LMS without an integration project. | 982 / 135 |

🔴 **Not added, and the reason is the same reason twice:**
[`xiaoyang111222/cn-math-taxonomy`](https://github.com/xiaoyang111222/cn-math-taxonomy) is
**CC BY-NC 4.0** and [`CaviraOSS/PageLM`](https://github.com/CaviraOSS/PageLM) carries a bespoke
**"PageLM Community License"** with four non-commercial clauses. Both are content/curriculum assets.
🟡 [`menthorlabs/menthor`](https://github.com/menthorlabs/menthor) is genuinely **Apache-2.0**
(11 337 B · blob `08c875b2050c`, canonical §6) but **archived** — carried as a 🇧🇷 LATAM data point,
not a build target.

### 🔴 The census had an arithmetic error in it, and it was a refusal

🔵 This shelf's licence census has counted [`formalms/formalms`](https://github.com/formalms/formalms)
as having **no readable grant** for multiple passes, and `Gap 488-L` asked for it to be marked
unusable. 🟢 **It is GPL-2.0.** The grant sits at `html/license.txt` (18 346 B · blob
`e823963cd437`) and at `html/lib/System/license/license_english.txt` (15 146 B · blob
`b6e1c33e0499`) **with eight further language translations** — a project that serves its licence to
users through its own web UI, and therefore has no copy at the repository root where every previous
probe looked.

🔴 **So every `NO_LICENCE` denominator this shelf has published is one too high.** 🟢 The
re-probe ran tree-wide on all twelve zero-root-grant rows and **eleven of twelve held** — the defect
is real, and its yield is 1 in 12. Detail and the eleven pinned SHAs:
[`repos/trending.md`](trending.md) `p498`.

### 🟢 `learningequality/kolibri` — the one permissive institutional platform, finally read

🔵 `Gap 488-K`: *"the only permissive institutional platform on these shelves and has never been
read — no code read, no AI-surface census, no star or activity figure. The one row the brief's
licence preference points to is the least examined."* 🟢 Closed.

| | measured |
|---|---|
| grant | 🟢 **MIT**, 1 097 B, blob `6506702f35f3`, **one** grant path in the whole tree. *"Copyright (c) 2021 Learning Equality and other contributors"* |
| ref / HEAD | 🔴 default ref **`develop`** · HEAD `08e3ecace444` · last commit **2026-10-27** · `pushed_at` **2026-10-28T01:21:58Z** |
| scale | ★ **1 162** · forks **1 012** · open issues **574** · 185 MB · Python |
| code read | **6 040 tracked files** — 1 231 `.py`, 657 `.vue`, 1 183 `.js` |
| 🔴 **AI surface** | **zero.** One regex hit across all 3 071 Python/Vue/JS files, and it is a **false positive**: the word *"transformers"* in a comment about Django `from_db_value` field transformers, at `kolibri/core/content/viewsets/import_metadata.py:152` |
| 🟢 **AI-on-top surface** | `kolibri/plugins/` — **21 in-tree plugins**, a formal hook contract, and **21 `api_urls.py`** DRF surfaces |

🟢 **The plugin contract, read from the code** (`kolibri/plugins/__init__.py`,
`kolibri/plugins/hooks.py`, `kolibri/plugins/registry.py`):

- A plugin is **a Django app with a `kolibri_plugin` module**; enabling it adds its apps to
  `INSTALLED_APPS`.
- `KolibriPluginBase` exposes `url_module` and `api_url_module`, so a plugin mounts **its own URLs
  and its own DRF API** inside Kolibri.
- 🟢 **Plugins are enabled and disabled from the CLI or a UI**, and through
  `ENV_VAR_ENABLED_PLUGINS` / `ENV_VAR_DISABLED_PLUGINS` / `ENV_VAR_APPLIED_PLUGINS`. **That is an
  operational kill switch for an AI surface, with no rebuild** — which is the single most useful
  fact on this page for a ministry pilot or a regulator conversation.
- Hooks are singletons: `KolibriHook` with metaclass `KolibriHookMeta(SingletonMeta)` and an explicit
  `HookSingleInstanceError`. 🔴 **One registration per hook** — a real constraint if two vendors ship
  plugins into the same deployment.
- The project's own rule, in its own docs: *"a plugin should **never** modify internals of Kolibri or
  other plugins without using the hooks API."*
- 🟢 **Out-of-tree plugins are an exercised path, not a theory.** The repository ships four as
  `python_packages/`: `kolibri-oidc-provider-plugin`, `kolibri-sentry-plugin`,
  `kolibri-sync-extras-plugin`, `kolibri-context-translation-plugin`. An OIDC **provider** as a
  plugin is proof the extension surface reaches authentication.

🔵 **Why this matters more than the star count:** every recipe on
[`compose/patterns.md`](../compose/patterns.md) has treated Kolibri as a **content sink** — generate
packages centrally, ship them into offline channels. The code says it is a **host**. See `P498-1`.

🔵 **Not new here:** Kolibri's 0.87 fork-per-star was already recorded by `p489` as a deployment
proxy. This pass adds the licence payload, the activity, the code read and the extension contract —
not the ratio.

### 🆕 Registered

| gap | statement |
|---|---|
| 🟡 **`Gap 498-F`** | Kolibri's AI-surface census is a **keyword census** over Python/Vue/JS. A hosted inference call made through a generic HTTP client with no provider name in the source would not match. The verdict is "no provider-named integration", which is narrower than "no AI". |
| 🟡 **`Gap 498-G`** | Kolibri's **574 open issues** and `develop`-as-default both indicate an active trunk, but **no release cadence was read** — no tag list, no version file (the version is re-exported from `kolibri._version`, which was not resolved). `P498-1` therefore pins a commit, not a release. |
| 🔴 **`Gap 498-H`** | The three new permissive rows are **licence-and-description reads**. None was cloned and run, so "emits SCORM" is `Papermorph`'s claim, not a measurement. `Gap 484-A` still bounds everything on these shelves. |

---

## 🆕 `p499` — `2026-10-28` — **🟢 the permissive numerator finally moves, and it moves at the layer that matters: INTEROPERABILITY**

**Pass `p499` — reads of 2026-10-28.** This section **extends** the file; nothing above is rewritten.
Rows come from the promotion repair described in [`agents/trending.md`](../agents/trending.md)
`p499` (`Gap 499-A`). Every licence below was fetched from `raw.githubusercontent.com` at the pinned
SHA and graded on the operative-span instrument against the retained canonical set
([`evidence/canonical/MANIFEST.tsv`](../evidence/canonical/MANIFEST.tsv)).
Reads: [`new-rows-licence-bytes.2026-10-28-p499.tsv`](../evidence/new-rows-licence-bytes.2026-10-28-p499.tsv).

### 🟢 The headline this file has been waiting eight passes for

This file's standing lede is that **the education platform layer is overwhelmingly copyleft** — of
19 foundational platforms, 3 permissive — and that this is "the single most commercially important
fact in this file". 🟢 **It is still true of the LMS layer. It is not true of the layer above it.**

🟢 **The two interoperability standards that every education integration has to cross are both
permissive, and neither was on this shelf:**

| Layer | Repo | Licence (read from bytes) | ★ | Operative verdict | Why it changes the picture |
|---|---|---|---|---|---|
| 🟢 **LTI / IMS Global / Common Cartridge** | [`tsugiproject/tsugi`](https://github.com/tsugiproject/tsugi) | 🟢 **Apache-2.0**, 10 273 B `214d11084b7f` | **377** | 🟡 DEVIANT (−4: the `(a)`–`(d)` list enumerators in §4) | 🟢 **The LTI tool framework.** LTI is how anything reaches *inside* Moodle, Canvas, Open edX, Blackboard or D2L. Apache-2.0 means **the integration layer can be closed even when the LMS underneath is AGPL**. |
| 🟢 **SCORM / CMI runtime** | [`jcputney/scorm-again`](https://github.com/jcputney/scorm-again) | 🟢 **MIT**, 1 072 B `86ab328f0e5b` | **360** | 🟢 **IDENTICAL** | 🟢 A modern SCORM JavaScript runtime — SCORM 1.2, SCORM 2004, CMI, cross-frame. The other half of the standards boundary, and MIT. Active **2026-10-26**. |

🔵 **`tsugi`'s −4 was checked by hand before promotion, because an Apache deletion is exactly what
`p498` found in `get-it`.** It is **not** an alteration: the four §4 condition *bodies* are present
verbatim — "You must give any other recipients…", "You must cause any modified files…", "You must
retain, in the Source form…", "If the Work includes a \"NOTICE\" text file…" — and only the
parenthesised `(a)`/`(b)`/`(c)`/`(d)` enumerators are absent from the de-indented rendering. **The
conditions stand; the bullet letters do not.**

### 🟢 Six further platform rows, all read from bytes

| Layer | Repo | Licence | ★ | Operative verdict | Note |
|---|---|---|---|---|---|
| **LMS — permissive, new** | [`pacewisdomhq/TutorLoom`](https://github.com/pacewisdomhq/TutorLoom) | 🟢 **Apache-2.0**, 11 362 B `ef4bca4c9b34` | 52 | 🟢 IDENTICAL | 🟢 **Only the second permissive full LMS on these shelves** after `OpenOlat`. Multi-tenant, Django + React, self-hosted, markets itself as a Moodle alternative. 🔴 **Repo created 2026-10-07 — three weeks old, 13 forks, 10 open issues. Do not stake an engagement on it yet;** carry it as the row to re-read every pass. |
| **Skills / credentials** | [`iblai/lms`](https://github.com/iblai/lms) | 🟢 **MIT**, 1 063 B `18f76c220561` | 208 | 🟢 IDENTICAL | Skills-intelligence platform — competency tracking, digital credentials, course discovery. 🟢 The **competency/credential** layer had no permissive row before. Active 2026-10-27. |
| **Collaborative coding classroom** | [`SJRiz/pytogether`](https://github.com/SJRiz/pytogether) | 🟢 **MIT**, 1 073 B `52021a40fdff` | 261 | 🟢 IDENTICAL | Browser-based collaborative Python IDE with real-time editing — the teaching-lab primitive. |
| **Course CMS / microsites** | [`haxtheweb/haxcms-php`](https://github.com/haxtheweb/haxcms-php) | 🟢 **Apache-2.0**, 11 362 B `ecac353f6e80` | 130 | 🟢 IDENTICAL | HAX + CMS for course microsites, PHP backend. Pushed **2026-10-28**. Same stable as `elmsln`. |
| **Course reader** | [`tutors-sdk/tutors`](https://github.com/tutors-sdk/tutors) | 🟢 **MIT**, 1 088 B `3f578d9362e6` | 125 | 🟢 IDENTICAL | The Tutors Reader application. 🔵 Last push 2026-07-23. |
| **Language exchange** | [`langx/langx`](https://github.com/langx/langx) | 🟢 **BSD-3-Clause**, 1 520 B `8dd6541f1ce8` | 109 | 🟡 DEVIANT (clause-3 name substitution `of the copyright holder` → `LangX`) | Peer language practice; a HelloTalk alternative. 🔵 The substitution is **what BSD-3 instructs** the licensor to do, not an edit. Active 2026-10-28. |
| **Widgets / games over LTI** | [`ucfopen/Materia`](https://github.com/ucfopen/Materia) | 🔴 **AGPL-3.0**, 34 523 B `723f2b22cec6` | 52 | 🟢 IDENTICAL | Embeddable course widgets and games. Same UCF stable as `UDOIT` and `Obojobo`. 🔴 AGPL — hosted derivative must share. |
| **Offline-first content/services** | [`Wakoma/Lokal`](https://github.com/Wakoma/Lokal) | 🟢 **MIT**, 1 063 B `f3c821e1820c` | 53 | 🟢 IDENTICAL | Offline-first content and local network services, built for low-connectivity communities. 🟢 Pairs with `Kolibri` — see [`compose/patterns.md`](../compose/patterns.md) `P490-3`. 🔵 Last push 2025-11-15. |

### 🔵 The licence census, restated with this pass's rows

| | before `p499` | added `p499` | now |
|---|---|---|---|
| foundational platforms read from bytes | 19 | **+10** | **29** |
| 🟢 of which **permissive** (MIT / Apache-2.0 / BSD) | 3 | **+8** | **11** |
| permissive share | 15.8% | | 🟢 **37.9%** |

🔴 **Read this carefully — it is not a reversal of the copyleft finding.** Every *incumbent LMS*
remains GPL or AGPL: Moodle (GPL-3.0), Open edX (AGPL-3.0), Canvas (AGPL-3.0). What changed is
that the **standards, credential, authoring and client layers around them are permissive**. 🔵 The
correct strategic sentence is therefore: *you cannot close the LMS, but you can close everything
you build against it.*

### 🟢 `frappe/education`'s "*(declared only)*" qualifier is resolved

The row above records `GPL-3.0 *(declared only)*`. 🟢 Read from bytes this pass: `license.txt` at
`73ce33ef2719` is **19 bytes** and contains exactly `License: GNU GPL V3`. 🔵 So the repo **does**
state GPL-3.0 in its own bytes — the qualifier can go — but it **ships no licence text at all**,
which for GPL-3.0 is a conveyance problem in its own right. 🔴 **Two rows do the same thing** —
`codeforlife-education/rapid-router` and `codeforlife-education/codeforlife-portal`, both a
**121-byte `LICENSE.md`** reading *"Find our license here"* plus a link — which makes **grant by
reference a class on these shelves, not an anecdote.**

### 🆕 Declared gaps — `p499` (foundations)

| gap | statement | cost to close |
|---|---|---|
| 🔴 **`Gap 499-G`** | All ten rows above are **licence-and-description reads**. None was cloned, built or run — the same standing limit as `Gap 498-H`. "Tsugi crosses the LTI boundary" is the project's claim and the standard's definition, **not a measured integration.** | needs an execution-permitted session |
| 🟡 **`Gap 499-H`** | `TutorLoom` is **three weeks old** and its Apache-2.0 grant is clean, but **nothing about its maintenance is established** — no tag list read, no release, no contributor count. It is promoted as a watch row, and a pass that treats it as a deployable LMS will be wrong. | one read per pass |
| 🟡 **`Gap 499-I`** | The permissive share moved 15.8% → 37.9% because **this pass added rows at the layers it chose to look at**. That is a selection effect, not a measured change in the sector. The denominator is this shelf, not the market. | one pass, defined sampling frame |

---

## 🆕 `p500` — `2026-10-28` — the interoperability leg gains a row, and the census axis is declared exhausted

**Pass `p500` — reads of 2026-10-28.** This section **extends** the file; nothing above is
rewritten. Licences fetched from `raw.githubusercontent.com` at commit SHAs resolved with
`git ls-remote`. Reads:
[`pinned-sha-rows.2026-10-28-p500.tsv`](../evidence/pinned-sha-rows.2026-10-28-p500.tsv),
[`residual-promotion.2026-10-28-p500.tsv`](../evidence/residual-promotion.2026-10-28-p500.tsv).

### 🟢 Registered

| Layer | Repo | Licence @ pinned SHA | ★ | Operative body | Why this one |
|---|---|---|---|---|---|
| 🔴 **Realtime quiz / classroom response — UPSTREAM ARCHIVED** | [`ably-labs/realtime-quiz-framework`](https://github.com/ably-labs/realtime-quiz-framework) | 🟢 **Apache-2.0**, 11 357 B `c4c0cb0b30b5` | 77 | 🟢 **IDENTICAL** to the apache.org steward form | 🔴 **`p504`: `archived: true` on the API — this repository is FROZEN upstream, and this row recommended it with no end-of-life flag for ~20 passes.** Fork it or lift the pattern; do not expect fixes. The permissive base for live classroom response — the "everyone answers at once" problem (fan-out, join-mid-round, scoring) solved as a networking framework rather than a product. Pushed 2026-03-06: live, not fast-moving. |

### 🟢 The permissive census — and why the denominator stops moving here

The `topic:edtech` **50–400★** axis, enumerated by `p499` and re-joined against the three curated
shelves this pass, is **spent**. Of 52 rows, **21 are now shelved (40.4%)** — `p499` promoted 20
in its own pass — and of the **31** that remain:

| why unshelved | n |
|---|---|
| 🔴 copyleft (AGPL-3.0, GPL-3.0/2.0, LGPL-2.1, MPL-2.0, CERN-OHL-S-2.0) | 11 |
| 🔴 no resolvable grant at any root path | 6 |
| 🔴 dormant (no push since 2024 or earlier) | 9 |
| 🟡 permissive but dormant | 2 |
| 🟢 **permissive and live — promotable** | **4** |

**The whole remaining yield of this axis is four rows.** That is the honest reason this file's
permissive numerator has crept rather than jumped for ten passes: **not** curator inattention, but
a population that is mostly copyleft, unlicensed or abandoned. `Gap 500-A` asks the next discovery
pass for a different axis.

### 🟢 `OpenOLAT`'s Apache-2.0 grant stands — the deviation was ours

[`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT), re-read at `cd91a957ea2e`
(**10 982 B**), is this file's **only permissive full LMS**, so its licence was re-graded from
bytes rather than carried forward. Operative body **1 511** words against the apache.org steward's
**1 412**: the +99 is two appended paragraphs crediting the **OLAT Zentrum at the University of
Zurich** and **frentix GmbH**. 🟢 **No added condition — the Apache-2.0 grant is materially
unaltered.**

🔴 Two instrument faults are recorded against this one row. Its copy carries **no `APPENDIX`
heading**, so the marker-based operative cut removed nothing and graded attribution prose as
operative — `Gap 499-E` firing on the file's most load-bearing row. And every Apache verdict in
this file written before `p500` was scored against SPDX's 1431-word form alone, which manufactures
a **−19** phantom for any repository shipping the steward's 1412-word copy. `Gap 500-B` holds the
unmeasured blast radius; `Gap 500-C` holds the attribution-vs-restriction blindness.

### 🔴 Not registerable, recorded so the next pass does not re-read them

| Repo | ★ | Finding |
|---|---|---|
| [`canyongbs/advisingapp`](https://github.com/canyongbs/advisingapp) | 340 | **Elastic License 2.0** (3 860 B @ `4449f765bdd0`) — source-available, not OSI. Forbids hosted provision to third parties. |
| [`learning-commons-org/knowledge-graph`](https://github.com/learning-commons-org/knowledge-graph) | 164 | 🟢 code **MIT** (5 789 B @ `a7547180c47d`); 🔴 datasets licensed **per download**, not uniformly. Shelvable as code, not as data. |
| [`jaltekruse/Free-Math`](https://github.com/jaltekruse/Free-Math) | 74 | **No grant** at any of 7 root paths (all 404). All rights reserved. |
| [`abdullaitcenter-hue/comet-trail-archives`](https://github.com/abdullaitcenter-hue/comet-trail-archives) | 70 | **No grant** at any of 7 root paths. All rights reserved. |


## 🆕 `p502` — `2026-10-28` — **🟢 the record layer reaches this shelf, 35 passes after it was graded**

`Gap 467-I` was opened because *"no permissive row exists at the LRS / learning-analytics tier; an
xAPI analytics component cannot enter a proprietary deliverable from these shelves."* It was
**closed by grading nine rows** — and closure moved **nothing onto this shelf**. 🔴 This file has
carried an LMS/SIS census for ~35 passes with **no record layer in it at all**, while
[`intel/open-gaps.md`](../intel/open-gaps.md) carried the grades. 🔵 **A gap can be answered and
still leave the base unable to answer a client.** Registered as `Gap 502-C`; five rows promoted here.

Measurement this pass used a channel this base recorded as closed — the **GitHub REST API**, reachable
through the MCP server (`Gap 502-A`, and `agents/top.md`'s verification table is corrected). Licence
family is taken from `license.spdx_id` **and** confirmed against the first 200 bytes at a pinned SHA,
per the standing two-channel rule. 🔴 **Dates are from git only**: the API's `pushed_at` counts a push
to any ref and overstated one mainline here by **708 days** (`Gap 502-B`).

### Permissive — the record layer you can put in a closed deliverable

| Repo | Licence (bytes at the pinned SHA) | ★ | forks | mainline | region | What it is |
|---|---|---|---|---|---|---|
| [`adlnet/ADL_LRS`](https://github.com/adlnet/ADL_LRS) | **Apache-2.0** — 11,357 B `1128f8f91104` | **334** | 156 | 🔴 **502 d** `efa045e` | North America | The **US DoD ADL Initiative's** own Learning Record Store, Python/Django. 🔴 **Reference implementation, not a base** — `master` has not moved since `2025-06-13` |
| [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) | **Apache-2.0** — 11,356 B `58853eb8199b` | **144** | 41 | 🟢 **2 d** `6159416` | North America | SQL-backed LRS (Clojure, SQLite/Postgres). 🟢 **The live permissive LRS — build here.** Yet Analytics, `sqllrs.com` |
| [`adlnet/lrs-conformance-test-suite`](https://github.com/adlnet/lrs-conformance-test-suite) | **MIT** — 1,045 B `f1083e4aa47d` | 78 | 53 | 🔴 419 d `5bc232d` | North America | The **official xAPI conformance suite** (`lrstest.adlnet.gov`). 🟢 This is how you prove an LRS you built or forked is conformant — the acceptance instrument for the whole tier |
| [`adlnet/CATAPULT`](https://github.com/adlnet/CATAPULT) | **Apache-2.0** — 11,357 B `1128f8f91104` | 59 | 34 | 🔴 281 d `806c0ba` | North America | **cmi5** player + test suite. cmi5 is the xAPI profile that replaces SCORM for launch-and-track |
| [`openfun/warren`](https://github.com/openfun/warren) | **MIT** — 1,093 B `14a2c9fcad08` | 17 | 1 | 🔴 **708 d** `839fcbb` | **EMEA** | Learning-analytics visualisation over xAPI. 🔵 Region is read from the licence line itself — *"Copyright (c) 2023-present **France Université Numérique**"* — not inferred |
| [`yetanalytics/project-persephone`](https://github.com/yetanalytics/project-persephone) | **Apache-2.0** — 11,356 B `58853eb8199b` | 8 | 1 | 🟢 recent | North America | Validates xAPI Statements against **Profiles**. 🟢 New to this base. Small, but it is the piece that turns "we emit xAPI" into "we emit xAPI that conforms to a stated profile" |

🟢 Already carried, re-confirmed: [`openfun/ralph`](https://github.com/openfun/ralph) — MIT, 51★,
mainline **16 d** (`91fef11`), **EMEA** (France Université Numérique). `Gap 467-I` named it the
permissive exemplar; 🔴 **it is the third-largest permissive LRS on this shelf, not the first**, so
that closure understated its own tier by 2.8× on stars.

### 🔴 Two orderings that disagree, and the one a `pushed_at` read gets wrong

| | by stars | by mainline freshness |
|---|---|---|
| 1 | `ADL_LRS` **334** | `lrsql` **2 d** |
| 2 | `lrsql` 144 | `ralph` 16 d |
| 3 | `lrs-conformance-test-suite` 78 | `CATAPULT` 281 d |
| … | | `ADL_LRS` 🔴 **502 d** |

🔵 **The orderings are nearly inverted, and the API's convenient date field hides it:** `ADL_LRS`
reports `pushed_at` `2025-11-14` against a last `master` commit of `2025-06-13` — **154 days apart**.
🟢 **Shelf rule: cite `ADL_LRS` as the reference, build on `lrsql`, and prove conformance with
`lrs-conformance-test-suite` regardless of which you pick.**

### 🔵 One byte, two canonical Apache-2.0 payloads

`11,356 B` / `58853eb8199b` (Yet Analytics ×2) and `11,357 B` / `1128f8f91104` (ADL ×2) differ by a
single trailing byte in the appendix — **not a terms difference**. 🟢 The `1128f8f91104` payload is
**byte-identical to the one this base already recorded for
[`anthropics/k12-teacher-skills`](https://github.com/anthropics/k12-teacher-skills)**, an independent
confirmation of that earlier read from an unrelated org.

### Declared gaps

| id | statement |
|---|---|
| 🆕 **`Gap 502-C`** | **Graded ≠ shelved.** `Gap 467-I` closed by grading and promoted nothing for ~35 passes. Five rows land here; **26 of the 31 tier addresses read this pass are still unshelved.** 🔴 Open and general: *how many other closed gaps closed without a promotion?* No instrument here answers that |
| 🆕 **`Gap 502-D`** | **`NOASSERTION` is three states wearing one label** — no licence, custom licence, and a licence GitHub's matcher did not recognise — with opposite procurement consequences. [`learning-commons-org/knowledge-graph`](https://github.com/learning-commons-org/knowledge-graph) (164★) and [`learning-commons-org/evaluators`](https://github.com/learning-commons-org/evaluators) (87★) both return it, while their sibling `agent-skills` is cleanly Apache-2.0. 🟢 **CLOSED at `p503`; INDEPENDENTLY REPRODUCED at `p504` on a different channel** (`curl` against `raw.githubusercontent.com` at the HEAD SHA) with **byte-identical results** — same byte counts, same blob SHA-1s. 🔴 **But this very sentence was still live on this shelf at `p504`:** `p503`'s register entry says the stale text was *"corrected by closure above"*, and it corrected [`intel/open-gaps.md`](../intel/open-gaps.md) **without touching this file**. The register moved; the shelf did not. Corrected here now. Root cause of the `NOASSERTION`: both carry **`LICENSE.md`, a prose licensing FRAMEWORK rather than a canonical licence text**, which no matcher can classify — a **fourth** state beyond the three this gap named. `evaluators` (1 615 B, blob `86eebd7ebc43`, HEAD `b9d47891c1b8`) is 🟢 **MIT code + CC BY 4.0 prompts** but 🔴 **CC BY-NC-SA 4.0 on both annotated corpora (CLEAR, PERSUADE 2.0) — REFUSED for paid work**. `knowledge-graph` (5 789 B, blob `6320adcd726e`, HEAD `a7547180c47d`) is 🟢 **MIT code** over 🔴 **data that is NOT uniformly licensed at all**: per-dataset *and per-download* access types (Open / Open+Gated / Gated), where Gated carries no open licence and needs provider approval, a compiled build inherits every included dataset's obligations, and terms may change between releases. 🔴 **Neither is answerable at repo level** — see [`noassertion-bytes.2026-10-28-p504.tsv`](../evidence/noassertion-bytes.2026-10-28-p504.tsv) and `p503`'s closure in [`intel/open-gaps.md`](../intel/open-gaps.md). 🔴 **Original `p502` note, retained for the record:** neither payload was byte-read at `p502`, and they are the larger two |
| 🟡 carried | 🔴 **The whole record layer above is one region.** Five of six promoted rows are North America (US DoD and a Baltimore vendor); the sixth is EMEA and **708 days stale**. 🔴 **There is no APAC or LATAM LRS on this shelf, and none was found** — stated as a measured absence, not coverage |

### 🟢 `p490`'s `tao-core` correction survives a direct attack — and the attack is the reusable finding

`p490`'s correction table records that this base **overclaimed**
[`oat-sa/tao-core`](https://github.com/oat-sa/tao-core) as `GPL-2.0-or-later` when *"the `or-later`
election is **not** readable from the payload."* 🔴 A one-line grep appears to overturn that
immediately: the payload at `2f4f12f6dbad` (**18,025 B**, `sha1 946b7346e0ed`) **does** contain the
string *"any later version"* — twice.

🟢 **It does not overturn it. Both hits are canonical GPL-2.0 text, and neither is an election:**

| line | location | what it is |
|---|---|---|
| 245 | inside **§9 of the terms** | the clause describing what happens *if* a program specifies a version number — a conditional, not a choice |
| 299 | **after line 280, `END OF TERMS AND CONDITIONS`**, inside *"How to Apply These Terms to Your New Programs"* (line 282) | the **sample notice template** the FSF supplies for authors to copy |

🔵 **Rule, and it generalises to every GNU payload on these shelves: the `-or-later` election is
never readable from a canonical GNU licence body, because the canonical body contains the phrase
twice by construction.** The election lives in the *project's own* notice — source-file headers, a
`README`, or a declared SPDX identifier — never in the licence text. 🔴 A body scan for
*"any later version"* therefore returns **true for every GPL-2.0 and GPL-3.0 repository in
existence**, election or not, and would have mis-corrected a cell that was right.

🟢 **`p490`'s cell stands: `GPL-2.0`, election not readable.** 🔵 This also sharpens `Gap 467-B`,
which records readable `-or-later` elections on `i-educar`, `i-diario`, `moodle-sence`,
`LearningLocker` and `EdOptimize` — those must have been read from a channel **other than** the
licence body, and the gap should say which, or they inherit this same defect.

🟢 **Re-confirmed independently this pass:** [`frappe/education`](https://github.com/frappe/education)'s
grant payload is still the **19-byte** `license.txt` reading exactly `License: GNU GPL V3`
(`sha1 425d2be709a6`, at `develop` `73ce33ef2719`) — the fixture behind this file's *"19-byte
license"* section. 🔴 Its default branch is **`develop`, not `main`**; `main` does not resolve, which
is this file's branch-name trap in its original instance.

## 🆕 `p503` — `2026-10-28` — **🟢 `Gap 502-D`'s TWO PAYLOADS ARE RE-READ AND BOTH SHELF CELLS HOLD — the gap text next to them says *"neither payload was byte-read this pass"* while the rows above it carry the byte counts, so the GAP is stale, not the cells. 🟢 Both now carry a blob SHA-1, which is what a drift check needs and neither had. 🟢 One MIT simulator shelved. 🔴 And the LMS-plugin-registry axis `Gap 500-A` asked for is UNREACHABLE from this session, which is an informed gap, not an unmined one.**

Reads: [`licence-bytes.2026-10-28-p503.tsv`](../evidence/licence-bytes.2026-10-28-p503.tsv),
[`channel-boundary.2026-10-28-p503.tsv`](../evidence/channel-boundary.2026-10-28-p503.tsv).

### 🟢 `Gap 502-D` — re-resolved from bytes, and the terms are richer than one cell can hold

Both payloads re-fetched at the **same pinned commits this file already cites**, bytes and git
blob SHA-1 computed locally:

| repo | path | bytes | blob SHA-1 | pinned commit | vs the cell above |
|---|---|---|---|---|---|
| [`learning-commons-org/knowledge-graph`](https://github.com/learning-commons-org/knowledge-graph) | `LICENSE.md` | **5 789** | 🆕 blob `6320adcd726e` · sha256₁₆ `d849ffef4f9816cb` | `a7547180c47d` | 🟢 **byte count identical** |
| [`learning-commons-org/evaluators`](https://github.com/learning-commons-org/evaluators) | `LICENSE.md` | **1 615** | 🆕 blob `86eebd7ebc43` · sha256₁₆ `86c7be78af8ba536` | `b9d47891c1b8` | 🟢 **byte count identical** |

🔵 **Why the blob SHA-1 matters and the byte count does not suffice:** a byte count collides
trivially — any one-character substitution preserves it. The blob SHA-1 is what `p501`'s retention
check (`MANIFEST.tsv`) compares, and neither of these rows could be checked that way until now.

🟢 **`knowledge-graph`'s terms, in full, because the one-line cell flattens three states into one:**

| access type | grant | where the licence lives |
|---|---|---|
| **Open** | 🟢 CC BY 4.0 (most) or CC0 (a minority) | row-level attribution in the dataset |
| **Open + Gated** | 🟡 **split per download** — e.g. *Scope and sequence* Open while *Instructional materials* and *Assessment materials* are Gated | stated per download on the dataset page |
| **Gated** | 🔴 **not covered by any open licence**; access requires Data Provider approval under separate terms | on request from the publisher |

🔴 **The clause that decides whether this is shelvable for a paid engagement**, quoted:
*"If you compile datasets from the catalog into your own Knowledge Graph build, you take on the
licensing and attribution obligations of every dataset and download you include."* And:
*"Attribution travels with the data, not with Learning Commons."* 🟢 **Shelf rule, unchanged but now
grounded: build on the MIT code; treat every dataset as a separate procurement question, and never
publish a derivative build as uniformly CC BY 4.0.**

🔵 `evaluators` is the same shape with a sharper edge: **code MIT**, prompts and settings
**CC BY 4.0**, and the two annotated corpora it ships — **CLEAR** and **PERSUADE 2.0** —
**CC BY-NC-SA 4.0, non-commercial**. The code is billable; the rubric corpora are not.

### 🟢 Shelved — an MIT teaching simulator, with its limits stated

| Repo | Licence @ pinned SHA | ★ | Operative body | What it is | Region basis |
|---|---|---|---|---|---|
| [`xevrion/breakscale`](https://github.com/xevrion/breakscale) | 🟢 **MIT**, 1 080 B `c58de512f3ae` (blob `0c920ce1638e`, sha256₁₆ `33ea9e6b8b9621dc`) | **1 858** | 🟢 **IDENTICAL** to retained canonical MIT | A **load-it-until-it-breaks** system-design simulator: build an architecture on a canvas, drive traffic through it, watch the queueing behaviour explain the failure. TypeScript + React, `queueing-theory` in its own topics. | 🔴 **unplaced** — English artefact, `breakscale.tech`, no locale signal; recorded as unplaced rather than defaulted to a region |

🔴 **What it is not:** there is no AI in it, and the subject is one topic (distributed systems), so
it is **courseware machinery, not an education platform** — the reusable part is the
simulate-then-explain loop, which is the shape an agentic lab assistant needs and which this
shelf had no permissive instance of.

### 🔴 The registry axis is blocked, not unmined — three probes each

`Gap 500-A` asked for *"topic co-occurrence, LMS plugin registries, or a non-GitHub forge"* and
`Gap 502-E` named non-GitHub forges as the likeliest blind spot. Probed:

| channel | 3 probes | verdict |
|---|---|---|
| `download.moodle.org/api/1.3/pluginlist.php` | `000 000 000` | 🔴 **BLOCKED** by this session's network policy — the Moodle plugin registry cannot be read here |
| `codeberg.org/api/v1/repos/search` | `000 000 000` | 🔴 **BLOCKED** |
| `huggingface.co/api/models` | `000 000 000` | 🔴 **BLOCKED** |
| `api.npmjs.org/downloads/point/...` | `000 000 000` | 🔴 **BLOCKED** — no demand-side signal (downloads) is obtainable |
| `registry.npmjs.org/-/v1/search` (control) | `200 200 200` | 🟢 works |
| `gitlab.com/api/v4/projects?search=` | `200 200 429` | 🟢 **ANSWERS, rate-limited** |

🟢 **One non-GitHub forge is reachable** — `gitlab.com`'s REST API, and `git ls-remote` pins SHAs
there exactly as it does on GitHub (verified against `gitlab-org/gitlab-foss`). 🔴 **The registry
axis needs a network-policy change, not another pass** — same class as `Gap 499-C`'s `gnu.org`.
Registered as `Gap 503-B`.
