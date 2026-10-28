---
industry: education
region: Global
updated: 2026-10-28
---

## 🆕 `p511` — `2026-10-28` — **🟢 `make hooks` RAN, after sixteen denials in seventeen passes — AND IT IS RED: 45 of 63 gates green. The shelves have been un-attested for sixteen passes and the suite now says where. 🟢 `Gap 509-A` CLOSES and the reading it suspended is RETIRED, NOT RESTORED: DeepTutor carries 88 tags and `v1.7.0`, which is shipping. 🔴 `Gap 510-A` READ THE WRONG FEATURE: over all 22 star cells, a missing provenance suffix is a screen with 100 % recall and 29 % precision — the clean discriminator is ROUNDNESS, 4 of 4 re-read round cells WRONG against 15 of 15 non-round cells EXACT, and one of the four was OVERSTATED by 38. 🔴 One new MIT agent row, placed LATAM, and it breaks a nil `p509` declared.**

🟢 **Gate posture, stated first because it inverts seventeen passes of posture:
`make hooks` EXECUTED.** `93` suites ran, `p300`'s no-masking runner reports
**`45/63` gates green**, and the red list is named:
`gate-offline`, `gate-enumeration`, `gate-evidence-store`, `gate-shelf-consistency`,
`gate-region-headings`, `gate-register-currency`, `gate-fold-identity`, `gate-author-key`,
`gate-census-currency`, `gate-grant-path`, `gate-census-union`, `gate-i2-sweep-crosscheck`,
`gate-union-currency`, `gate-action-answered`, `gate-promotion`, `gate-promotion-ledger`,
`gate-cell-reproduction`, `recount`.
🔵 **Three of those gates independently reproduced defects this pass had already found by hand**,
which is the first cross-check this base has ever had between its prose discipline and its own suite.

🔴 **And the posture changed again INSIDE this pass: the verification re-run of `make hooks` after the repairs was DENIED (`Code from External`).** 🟡 **So the red verdict above is gate-attested and the two repairs below are NOT.** Both were therefore re-checked independently in this session's own code and are green: one bare `## Opportunities by region` block carrying exactly five `###` subsections, all from the closed vocabulary (`P383`); and the register's newest section at `p511` against the shelves' `p511` (`P418`). 🔵 **Recorded rather than smoothed over — a pass that can run the gate once and not twice must say which half of its own work the gate saw.**

### 🟢 `Gap 509-A` — CLOSED, and the reading it suspended is retired rather than restored

`Gap 509-A` recorded that `p505`'s *"attention, not shipping"* reading of
[`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) rested on a `HEAD` pin that had moved, and
ordered the reading re-derived from `HEAD` **plus** a `sort -V` tag census before it was used again.
🟢 **Both reads are in:**

| read | value |
|---|---|
| `refs/heads/main` (`HEAD`) | **`1ea7df155447`** — 🔵 **the same SHA `p509` recorded**, so the pin is now stable `p509` → `p511` |
| tag count (`git ls-remote --tags`, peeled refs excluded) | **88** |
| latest tag, `sort -V` | **`v1.7.0`**, preceded by a dense `v1.6.5` … `v1.6.15` series |
| stars | **47,774** *(🟢 `p511`, API)* — `p510`'s cell is **47,725** (`p509` read 47,677), so **+49** since `p510` |

🔴 **The reading is retired.** 88 tags and a minor-version bump to `v1.7.0` is a project that ships;
*"attention, not shipping"* was an inference from a single unchanged pin and it does not survive a
tag census. 🔵 The general lesson `Gap 509-A` asked to be noted holds in the opposite direction too:
**a claim of the form "unchanged for N passes" decays silently, and so does the conclusion drawn
from it.**

🟡 **One honest caveat on the star cell itself:** DeepTutor was read **twice** this pass, about
twenty minutes apart — **47,769** then **47,774**. An "exact" star cell on this repository is exact
only at its timestamp, and every cell on these shelves should be read that way.

### 🟢 `Gap 510-A` — the tell was tested over the whole population, and the REAL discriminator is a different one

`p510` found two rounded star cells typeset exactly like exact reads and read the tell as
*"neither cell carried a `*(🟢 pNNN, API)*` provenance suffix."* 🟢 **This pass stopped treating that
as a diagnosis and measured it.** Every star cell on the live shelves was classified first — by
suffix, and by whether the number ends in two or more zeros — and **19 of the 22 were then re-read
on the API**, the classification fixed before any value was seen.

**Axis 1 — the provenance suffix. It is a sound screen and a poor verdict.**

| population | n | re-read | wrong |
|---|---|---|---|
| cells **carrying** a `*(🟢 pNNN, API)*` suffix | 8 | 5 | 🟢 **0** |
| cells **missing** the suffix | 14 | 14 | 🟡 **4** |

🟢 **Recall is perfect — all four wrong cells lack a suffix.** 🔴 **Precision is 4/14 ≈ 29 %**, so
*"no suffix"* flags ten cells that are exactly right. As a verdict it is nearly useless.

**Axis 2 — roundness. This is the discriminator, and on everything re-read it is clean.**

| cell shape | n | re-read | exact | wrong |
|---|---|---|---|---|
| **ends in `00`** | **5** | 4 | **0** | 🔴 **4** — `1,200`, `14,300`, `78,000`, `100` |
| does not | **17** | 15 | 🟢 **15** | **0** |

🔴 **Four of four re-read round cells were wrong. Fifteen of fifteen non-round cells agreed with the
API exactly.** A round star count on these shelves is not a measurement — it is a remembered
approximation wearing a measurement's typography. Corrected this pass:

| cell | shelf | was | is | delta |
|---|---|---|---|---|
| [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | [`repos/foundations.md`](../repos/foundations.md) | `1,200` | **1,162** | 🔴 **−38, the shelf OVERSTATED** — a "stars only grow" assumption can never catch this |
| [`EleutherAI/lm-evaluation-harness`](https://github.com/EleutherAI/lm-evaluation-harness) | [`verticals/solutions.md`](../verticals/solutions.md) | `14,300` | **14,341** | +41 |
| [`microsoft/ai-agents-for-beginners`](https://github.com/microsoft/ai-agents-for-beginners) | this file, **both** occurrences | `78,000` | **78,061** | +61 |
| [`Selleo/mentingo`](https://github.com/Selleo/mentingo) | this file | `100` | **101** | +1 |

🔴 **The fifth round cell is declared, not quietly left:** `anthropics/k12-teacher-skills` reads
**600** and carries a suffix, so the screen cleared it and the roundness test flags it. It was
**not** re-read this pass and is registered as `Gap 511-B`.

🟢 **The operative rule, replacing `Gap 510-A`'s:** a star cell ending in `00` is unread until
re-read, whatever suffix it carries; and every cell written from here on carries its
`*(🟢 pNNN, API)*` suffix so the screen keeps working. 🔵 `p510` was right that a tell existed and
right about which two cells were wrong; it read the wrong feature of them, and the feature it chose
would have cleared two of this pass's four defects.
Census: [`star-cell-recheck.2026-10-28-p511.tsv`](../evidence/star-cell-recheck.2026-10-28-p511.tsv).

### 🟢 The one new row — and it breaks a nil this base declared two passes ago

`p509` closed `Gap 508-E` with a regional finding stated as a nil: the LATAM-placeable repositories
the `topic:` channel can reach are *"all course materials or national-system integration, **none an
AI product**."* 🟢 **That nil no longer holds.**

| agent | licence (read first-hand) | ★ | region | why it is placeable |
|---|---|---|---|---|
| [`oluiscabral/studorama`](https://github.com/oluiscabral/studorama) | 🟢 **MIT** — `LICENSE` **1,064 B**, `sha256₁₆ 75ecd9ad0bb3b543`, holder *"Copyright (c) 2025 oluiscabral"* | **111** *(🟢 `p511`, API)* | 🟢 **LATAM** | Its `README` (12,965 B) declares **"Complete English and Portuguese (Brazil) localization"**, localized AI prompt content and *"Cultural Adaptation: region-specific content"* as **first-class product features**, not a translation afterthought |

🟢 **What it is:** a multi-provider AI study platform — **OpenAI, Google Gemini, Anthropic Claude,
DeepSeek, Ollama (local) and browser-local AI**, 15+ models, per-provider key management — built on
named study techniques rather than a chat box. `refs/heads/main` → **`2ddbb1122b5b`**, **10 tags**.
🔵 **The Ollama/local-model path is the part that matters commercially in LATAM**, where cloud
inference cost and data residency are the two objections an engagement meets first.
🔴 **Build-on caveat, stated plainly:** the licence holder is a personal handle, not an organisation,
and the hosted demo runs on Vercel. This is a **single-maintainer** project. Fork-and-own, do not
take a dependency.

🔵 **The region is placed on the product's own bytes, not on an inference about its author.** This
base has no evidence of the maintainer's nationality and does not need any: the pt-BR localization
is in the repository.

### 🔴 Three gates reproduced defects this pass found by hand — and one of them should NOT be obeyed

🔴 **`gate-shelf-consistency` reports three licence contradictions. All three are false positives,
and they are the defect class this register has already retracted twice.**

| gate finding | what the line actually says |
|---|---|
| `microsoft/autogen`: `CC-BY-4.0` (`agents/top.md:52`) vs `MIT` (`:1104`) | `:52` is narrative about **a defective probe** — *"A first-match-wins filename probe read `microsoft/autogen`…"*; `:1104` is this file's **documented AutoGen split** (the `LICENSE` file really is CC BY 4.0). Two different objects, both correct |
| `oat-sa/tao-core`: `GPL-2.0` (8 sites) vs `LGPL-2.1` (`agents/top.md:416`) | `:416` reads *"The **first reader run** this pass graded `oat-sa/tao-core` as…"* — a **retracted** reading, described as retracted on its own line |
| `openeducat/openeducat_erp`: five families at `intel/open-gaps.md:1269` | that line is **`Gap 460-D`**, whose content **is** the wrong grants a contradicting external source serves. Quoting a wrong value is the gap |

🟢 **No shelf prose was edited to make this gate green.** `p455` retracted a 20.6 % shelf-defect rate
over exactly this mechanism (*"adjacency is not attribution"*), and `p509` named its two shapes —
**line-level co-occurrence** and **sole-address prose rows**. The gate reproduces both.
🔵 Registered as `Gap 511-A` against the **gate**, not the shelves.

### 🔴 And this pass's own first probe reproduced the same defect, for a ninth recorded instance

🔴 **The star-cell extractor written for this pass reported
[`oppia/oppia`](https://github.com/oppia/oppia) at `41,705★` and
[`TrenTorch/TrenTorch`](https://github.com/TrenTorch/TrenTorch) at `385★`.** Both are wrong, and
neither was a shelf defect: `oppia`'s row correctly reads **6,950** *(🟢 `p506`, API)* and
`TrenTorch`'s correctly reads **741** *(🟢 `p510`, API)* — the extractor had captured a **different
repository's star figure from the same table cell's prose** (`OpenMAIC` at 41,705; `TrenTorch`'s own
`p484` historical value). 🟢 **Caught by the API control before anything was published, and the
shelves were right both times.** `Gap 509-B`'s precondition has now paid for itself in a **ninth**
consecutive instance and the shelves have been more precise than the instrument in four of them.

### 🟢 Every address written this pass is attested LIVE on the sound channel

🟢 **85 distinct `github.com/<owner>/<repo>` addresses appear in this pass's blocks across the nine
live files, and all 85 read `LIVE`** — a `ref:` line with a resolved default branch from
`git ls-remote --symref`, the one channel that discriminates. 🟢 **A known-bad control was run in
the same sweep and graded `UNREADABLE_ABSENT_OR_PRIVATE`**, per `Gap 509-B`'s precondition.
🔴 **No address was checked with `curl -sI`** — `p510` refuted that probe (403 for a live repo and
a deleted one alike) and `p511` refutes the `raw` 404 half of its replacement (`Gap 510-B`).
🔵 Among the 85, nine default to neither `main` nor `master` — `GibbonEdu/core` → `v31.0.00`,
`rosariosis` → `mobile`, `openeducat_erp` → `19.0`, `ILIAS` → `release_11`,
`bigbluebutton` → `v4.0.x-develop`, `overhangio/tutor` → `release`, `terracotta` and
`tutors-sdk/tutors` → `development`, `TrenTorch` → `TrenTorch-Dev` — which is why a probe that
assumes `main` reports phantom absences.
Reads: [`p511-url-liveness.2026-10-28-p511.tsv`](../evidence/p511-url-liveness.2026-10-28-p511.tsv).

# Education AI agents — build-on-able shelf

> 🟢 **`p510` (`2026-10-28`) — EVERY ADDRESS ON THIS SHELF IS NOW PROVEN LIVE, AND GETTING THERE MEANT DISCARDING THE VERIFICATION INSTRUMENT THIS BASE IS PRESCRIBED TO USE. 🔴 TEN STAR CELLS WERE WRONG, TWO OF THEM ROUNDED VALUES DRESSED AS EXACT READS, AND ONE OVERSTATED BY 36.**
> 🔴 **`curl -sI https://github.com/<slug>` is refuted as a liveness check on this channel**: run
> against a known-good **and** a known-bad target it returns **403 for both** — a live repository and
> one that never existed are the same byte. 🔴 **Any "URL verified" claim made with it verified
> nothing.** 🟢 **The replacement discriminates**: `git ls-remote --symref` for liveness and the true
> default branch, `raw.githubusercontent.com` for payloads (**200** live / **404** absent).
> 🟢 **All 154 distinct addresses across the six live shelves read `LIVE`** with a resolved default
> branch and a `HEAD` SHA — **zero dead, zero unreadable**, this base's first full-population
> liveness attestation:
> [`liveness-branch-census.2026-10-28-p510.tsv`](../evidence/liveness-branch-census.2026-10-28-p510.tsv),
> control: [`url-check-control.2026-10-28-p510.tsv`](../evidence/url-check-control.2026-10-28-p510.tsv).
> 🟡 **Stated honestly: the git channel is a sound POSITIVE test only** — an absent repository and a
> **private** one both answer with a credential prompt, so `LIVE` is assertable and `ABSENT` is not,
> and no row may be retired on this channel alone (`Gap 510-B`).
> 🔴 **24 bolded star cells re-read on the MCP channel: 13 current, 9 stale, 2 rounded.** Corrected
> here. The two rounded cells — [`rohitg00/ai-engineering-from-scratch`](https://github.com/rohitg00/ai-engineering-from-scratch)
> **74,800 → 75,238** and [`pguso/agents-from-scratch`](https://github.com/pguso/agents-from-scratch)
> **1,100 → 1,064** — were typeset exactly like exact reads. 🔴 **`pguso` OVERSTATED by 36 and the
> true count went DOWN**, which a "stars only grow" assumption can never catch. 🔵 **The tell was
> available and unread: neither cell carried a `*(🟢 pNNN, API)*` provenance suffix** (`Gap 510-A`).
> Census: [`star-cell-staleness.2026-10-28-p510.tsv`](../evidence/star-cell-staleness.2026-10-28-p510.tsv).
> 🟢 **`Gap 509-B` is CLOSED as code, not advice**:
> [`compose/code/p510-liveness-gate/`](../compose/code/p510-liveness-gate/) refuses to return a count
> unless a known-good and a known-bad control both behave — **8/8 offline controls green**. It fired
> twice on my own probes this pass, once on a star extractor that scored a bolded **HTTP 404** inside
> a dead-URL table as a 404-star row.
> 🔴 **Gate posture: `make hooks` DENIED (`Code from External`) — sixteenth denial in seventeen
> passes.** Nothing in this pass is gate-attested. 🔴 **Eight prescribed legs returned zero new
> addresses — a third consecutive pass.**

> 🟢 **`p509` (`2026-10-28`) — THE LICENCE COLUMN ON THESE SHELVES IS NOW BYTE-ATTESTED END TO END: 137 ADDRESSES SWEPT, 119 PAYLOADS READ WITH BYTES AND sha256, AND THE SHELVES WERE RIGHT EVERYWHERE A GRANT EXISTS. 🔴 EVERY CORRECTION THIS PASS IS TO THIS BASE'S OWN INSTRUMENTS, NOT TO ITS CONTENT.**
> 🟢 **`Gap 508-B` is DELIVERED, and wider than it asked.** It asked for *"bytes + sha256 for every
> PERMISSIVE row on these shelves (~20 addresses)"* as insurance while the `raw` limb is up.
> **Done for all 137 shelf addresses**: **119 carry a licence payload** (133 payload files in all),
> **81 of them permissive** (MIT / Apache-2.0 / BSD-3-Clause), each with a byte count and a sha256.
> Reads: [`licence-byte-census.2026-10-28-p509.tsv`](../evidence/licence-byte-census.2026-10-28-p509.tsv).
> 🟢 **The headline is a negative, and it is the valuable kind: no shelf licence cell was refuted.**
> The census independently reproduced this base's own prior readings — `educhain` **1,092 B
> `e3321a1b62cd7c46`** (p508's figure to the digit), `gegok12` **1,150 B `b8694396d7dc6439`**
> (p508's refutation of `p507` stands), `open-tutor-ai-CE` **BSD-3-Clause**, `chamilo` **GPL-3.0**.
> 🔴 **Seven probe defects, all mine, all caught by a control before anything was published** — and
> two of them would have written a false correction into a *correct* shelf row:
> [`probe-defects.2026-10-28-p509.tsv`](../evidence/probe-defects.2026-10-28-p509.tsv).
> **(1)** A first-match-wins filename probe read [`microsoft/autogen`](https://github.com/microsoft/autogen)
> as **CC-BY-4.0**; it serves **`LICENSE` (CC-BY-4.0, 18,650 B)** *and* **`LICENSE-CODE` (MIT,
> 1,141 B)** — the MIT shelf row is right, and **a licence probe must record every payload, not the
> first.** **(2)** `labmlai/annotated_deep_learning_paper_implementations` (**67,603★**) looked like a
> **new fourth licence state** — recognised `spdx_id: MIT` with no payload at 19 conventional paths.
> It is not a state, it is a **filename-case defect**: the grant is at lowercase bare **`license`**,
> **1,082 B, `sha256 22c7cae23a2b00cb`**. **(3)** **`NOTICE` is not a grant** — an Apache-2.0 §4(d)
> attribution notice — and counting it inflated the non-OSI tally from 6 to 18.
> **(4)** **A title-block anchor cannot see BSD-3-Clause**, which has no title line; `p455`'s anchor
> needs the three numbered conditions as a fallback. **(5)** **`git ls-remote` is not
> concurrency-safe here**: at `-P 10` it returned **NOREF for `HKUDS/DeepTutor`**, this base's
> flagship. **(6)** **`main`/`master` is the wrong assumption for 13.2% of this shelf** — see below.
> 🔴 **`T29` / `Gap 504-A` standing checks:** 13 queried / 13 returned across two batches,
> `incomplete_results: false` on both; `archived: false` on all 13.
> 🟢 **Shelf re-read:** `DeepTutor` **47,677★** (`p508`: 47,621, **+56**), `Apache-2.0`,
> `archived: false`, payload **11,408 B `cd2f54e1e5066644`** — *the flagship's licence read from
> bytes for the first time*. `OpenMAIC` **41,712** (**+3**). `book-to-skill` **36,415** (**+4**).
> `k12-teacher-skills` **600** (**+1**). `TorchLeet` **2,596** (**+1**). `educhain` **387** —
> **unchanged on a FIFTH read**, so `p490`'s 31× correction holds.
> 🔴 **And one carried claim is RETIRED: `DeepTutor`'s pin has MOVED.** `p505` recorded
> `a31d82624c27` *"unchanged for a 7th consecutive pass"*; `refs/heads/main` now resolves to
> **`1ea7df155447`**. The *"attention, not shipping"* reading no longer rests on a frozen `HEAD` and
> must be re-derived before it is quoted again.
> 🔴 **No new agent row, a second consecutive pass — and now confirmed on a DIFFERENT discovery
> shape.** `p508` declared agent-axis saturation from nine free-text legs. This pass added `topic:`
> legs (`Gap 508-E`'s remedy) and the four prescribed global legs plus all four regional legs: the
> only addresses new to this base are **`rphilipzhang/AI-PhD-S26`**, **`crodriguezn/python-2025`**
> and **`V0raOnline/arkinesis`** — **university course materials, not agents**, and not shelf-eligible.
> **Saturation survives a test it had not yet had.**
> Reads: [`search-legs.2026-10-28-p509.tsv`](../evidence/search-legs.2026-10-28-p509.tsv),
> [`api-shelf-read.2026-10-28-p509.tsv`](../evidence/api-shelf-read.2026-10-28-p509.tsv),
> [`channel-probe.2026-10-28-p509.tsv`](../evidence/channel-probe.2026-10-28-p509.tsv).
> 🔴 **Gate posture: `make hooks` DENIED (`Code from External`) — a fifteenth denial in sixteen
> passes.** Nothing in this pass is gate-attested.

### 🔴 `p509` — the default-branch finding, which invalidates a method this base has used throughout

🔵 **Every licence this base has read from `main/LICENSE` or `master/LICENSE` carried an unstated
assumption.** Resolved from `HEAD`'s symref, **18 of 136 shelf addresses (13.2%) default to neither
`main` nor `master`** — and they are not marginal rows, they are the verticals:

| address | default branch | address | default branch |
|---|---|---|---|
| [`frappe/erpnext`](https://github.com/frappe/erpnext) | `develop` | [`oppia/oppia`](https://github.com/oppia/oppia) | `develop` |
| [`frappe/lms`](https://github.com/frappe/lms) | `develop` | [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | `develop` |
| [`frappe/education`](https://github.com/frappe/education) | `develop` | [`oat-sa/tao-core`](https://github.com/oat-sa/tao-core) | `develop` |
| [`ILIAS-eLearning/ILIAS`](https://github.com/ILIAS-eLearning/ILIAS) | `release_11` | [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | `19.0` |
| [`bigbluebutton/bigbluebutton`](https://github.com/bigbluebutton/bigbluebutton) | `v4.0.x-develop` | [`overhangio/tutor`](https://github.com/overhangio/tutor) | `release` |
| [`GibbonEdu/core`](https://github.com/GibbonEdu/core) | `v31.0.00` | [`portabilis/i-educar`](https://github.com/portabilis/i-educar) | `2.12` |
| [`learnhouse/learnhouse`](https://github.com/learnhouse/learnhouse) | `dev` | [`tutors-sdk/tutors`](https://github.com/tutors-sdk/tutors) | `development` |
| [`francoisjacquet/rosariosis`](https://github.com/francoisjacquet/rosariosis) | `mobile` | [`TaiRuiQu/oh-my-paper`](https://github.com/TaiRuiQu/oh-my-paper) | `v2` |
| [`AgnellusX1/GodsEye`](https://github.com/AgnellusX1/GodsEye) | `PreProduction` | [`TrenTorch/TrenTorch`](https://github.com/TrenTorch/TrenTorch) | `TrenTorch-Dev` |

🟢 **Operative rule, and it is cheap: resolve `HEAD`'s symref before reading any path.** Six of
`p509`'s round-1 `NOPAYLOAD` verdicts were this defect alone. 🔴 **`francoisjacquet/rosariosis`
defaults to `mobile`** — a branch name that reads like a side branch and is the project's `HEAD`;
never infer a default branch from how its name sounds.

### 🔴 `p509` — proving a licence ABSENT needs the tree, not a path list

🔵 **`T33` gave three licence states. A path list can establish only two of them**: a payload that
answers, and a payload that does not answer *at the paths you guessed*. The third — **no grant at
all** — is a claim about **everything**, and only a tree enumeration can carry it.
🟢 **New channel for this base, and it is not gated:** `git clone --depth 1 --filter=blob:none
--no-checkout` plus `git ls-tree -r` enumerates a full tree without fetching blobs.
Reads: [`no-grant-tree-probe.2026-10-28-p509.tsv`](../evidence/no-grant-tree-probe.2026-10-28-p509.tsv).

| address | ★ | tree | verdict |
|---|---|---|---|
| [`labmlai/annotated_deep_learning_paper_implementations`](https://github.com/labmlai/annotated_deep_learning_paper_implementations) | 67,603 | 2,172 files, grant at **`license`** | 🟢 **MIT, 1,082 B `22c7cae23a2b00cb`** — the apparent fourth state was my probe |
| [`victor-lubn/Special-Education-Planning`](https://github.com/victor-lubn/Special-Education-Planning) | – | 2,387 files; 4 `licence` hits are **`licence.js`, `check-licence-dialog.component.ts`** | 🔴 **no grant.** The hits are **application code that implements a licence-check dialog** — `p455`'s *"adjacency is not attribution"* in its purest form |
| [`ictinnovations/ICTSchool`](https://github.com/ictinnovations/ICTSchool) | – | 2,313 files; every licence file under `public/bower_components/` | 🔴 **no own grant** — bootstrap, datatables, flot. **Vendored dependency licences are not the repo's grant** |
| [`kixlab/TutorCaseBench`](https://github.com/kixlab/TutorCaseBench) | **0** | 11,059 files, **no licence path** | 🔴 no grant, and no `license` object on the API either |
| 11 further addresses | – | **no licence path anywhere in tree** | 🔴 `GodsEye`, `project-samarth`, `comet-trail-archives`, `guru-latihan-dinamis`, `easy-iep`, `MCQ_Grading_Bot`, `mathtutorbench`, `AI-Roadmaps`, `Free-Math`, `essay-grader`, `essay-scoring-project`, `ai-spanish-tutor`, `gemini-handwriting-grader` |

🔴 **Two addresses carry a grant BY REFERENCE, and the reference is dead.**
[`codeforlife-education/codeforlife-portal`](https://github.com/codeforlife-education/codeforlife-portal)
and [`rapid-router`](https://github.com/codeforlife-education/rapid-router) both serve a **121-byte
`LICENSE.md`** reading *"Find our license here"* and pointing at
`codeforlife-workspace/main/LICENSE` — which answers **404**. 🟢 **A fourth state that IS real,
unlike the one that dissolved: `POINTER_DANGLING`.** Not an abstention, not an absence — an
**assertion with no referent**. Treat as no grant until the target resolves.
🔴 **And one more shape: [`frappe/education`](https://github.com/frappe/education)'s `license.txt`
is 19 bytes — `"License: GNU GPL V3"`.** A *declaration*, with no licence body. The family is
stated; the grant text is absent. Record it as **declared-not-served**.


> 🔴 **`p508` (`2026-10-28`) — NO NEW AGENT ROW, AND THE REASON IS SATURATION RATHER THAN A THIN SEARCH: ~80 ADDRESSES ACROSS NINE LEGS, **ZERO** THIS BASE DOES NOT ALREADY CARRY.**
> 🟢 **All four prescribed legs plus five `topic:` legs were run, and every permissive candidate they
> returned is already on these shelves or in this base's trending history** — `ankimcp/anki-mcp-server`
> (**537★ MIT**), `JuneYaooo/lineage-skill` (**462 Apache-2.0**), `ZeKaiNie/universal-examprep-skill`
> (**356 MIT**), `karanb192/algo-sensei` (**299 MIT**), `SenmuuuuW/universal-diagnostic-tutor-skill`
> (**252 MIT**), `orionsheep/wordlink` (**249 MIT**), `Fazmin/AILearningGuide` (**235 MIT**),
> `KeWang0622/kaogong-skill` (**210 MIT**), `liuliu667/cram-engine` (**176 MIT**),
> `SimonsTang/feifei-companion` (**110 Apache-2.0**), `wenflow-org/wenflow` (**61 MIT**),
> `ArnaudGuiovanna/tutor-mcp` (**57 MIT**), `HumphreySun98/Smart-Study-Agent` (**57 MIT**).
> 🔵 `p505` declared saturation on the **vertical** axis; **this is the first pass to declare it on the
> AGENT axis**, and the sweep is written down rather than left as silence:
> [`saturation-sweep.2026-10-28-p508.tsv`](../evidence/saturation-sweep.2026-10-28-p508.tsv).
> 🔴 **`p507`'s licence rule is too strong, and this pass narrows it from bytes.** `p507` wrote that
> `NOASSERTION` means *"GitHub detected no OSI licence, which is not a permissive grant and must never
> be shelved as one."* 🟢 **`NOASSERTION` is the detector ABSTAINING, not denying.** Two addresses on
> these shelves read `NOASSERTION` for **opposite** reasons:
> [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) serves an **Apache License** payload of
> **10,982 B** (`sha256 6dbc5b605ed0…`) with an appended *"Additional license statement for the
> openolat.org code base"* — a **modified Apache, with a real grant**; while
> [`Gego-K12/gegok12`](https://github.com/Gego-K12/gegok12) serves a **complete 1,150 B MIT grant**
> (`sha256 b8694396d7dc…`, holder *"Copyright (c) 2025 GegoSoft Technologies and GegoK12
> Contributors"*). 🔴 **Applied mechanically, `p507`'s rule deletes this KB's only permissive full
> LMS.** The operative rule is the one this base already had: **the payload decides, the detector
> field only routes.** Reads: [`licence-bytes.2026-10-28-p508.tsv`](../evidence/licence-bytes.2026-10-28-p508.tsv).
> 🟢 **Shelf re-read: 64 queried / 64 returned**, `incomplete_results: false` on every batch.
> `DeepTutor` **47,621★** (`p507`: 47,539, **+82**), `Apache-2.0`, `archived: false`.
> `THU-MAIC/OpenMAIC` **41,709★ MIT**. `book-to-skill` **36,411** (`p507`: 36,339, **+72**).
> `k12-teacher-skills` **599** (`p507`: 598, **+1**). `educhain` **387** — unchanged on a **fourth**
> read, so `p490`'s 31× correction holds. `TorchLeet` **2,595**, unchanged since `p507` added it.
> 🔴 **`archived: true` on 3 of 64** — [`menthorlabs/menthor`](https://github.com/menthorlabs/menthor)
> (582), [`ably-labs/realtime-quiz-framework`](https://github.com/ably-labs/realtime-quiz-framework)
> (77), [`AgnellusX1/GodsEye`](https://github.com/AgnellusX1/GodsEye) (30) — **and all three are
> already carried with an end-of-life flag.** `T29` holds for a fifth pass.
> 🔴 **Channel regression, stated plainly: `github.com` HTML is now 403 at the CONNECT**, which
> `p506` and `p507` still had. 🟢 **`raw.githubusercontent.com` answers 200** — the byte limb is the
> only non-MCP channel alive, and every licence reading above comes from it.
> 🔴 **Gate posture: `make hooks` DENIED (`Code from External`) — a fourteenth denial in fifteen
> passes.** Nothing in this pass is gate-attested.

> 🟢 **`p507` (`2026-10-28`) — ONE NEW PERMISSIVE AGENT ROW, AND THE APAC/EMEA ADOPTION FIGURES THIS SHELF SELLS INTO ARE NOW PLACED BY COUNTRY.**
> 🟢 **Added:** [`Exorust/TorchLeet`](https://github.com/Exorust/TorchLeet) — **2,595★, MIT,
> `archived: false`** — 65 ML/AI problems with **an auto-grader and an MCP AI tutor in one
> permissive repo**. It is the only new agent this pass whose licence permits a client build.
> 🔴 **Not added, and for the licence in every case:** [`echo-loop/Echo-Loop`](https://github.com/echo-loop/Echo-Loop)
> (**4,549★, AGPL-3.0**) and [`penecho/penecho`](https://github.com/penecho/penecho)
> (**2,509★, AGPL-3.0**) are the two fastest-growing education repos found this pass and **neither
> can be built on**; [`TarrySingh/…-Tutorials`](https://github.com/TarrySingh/Artificial-Intelligence-Deep-Learning-Machine-Learning-Tutorials)
> (**4,018★**) reads **`NOASSERTION`** — GitHub detected **no OSI licence**, which is not a
> permissive grant and must never be shelved as one.
> 🟢 **Shelf re-read: 45 queried / 44 returned.** `DeepTutor` **47,539★** (`p506`: 47,445, **+94**),
> `Apache-2.0`, `archived: false`. `k12-teacher-skills` **598**, unchanged since `p504`.
> `educhain` **387** — `p490`'s 31× correction holds on a third read.
> 🔴 **`openedx/edx-platform` silently omitted for a THIRD consecutive pass** with
> `incomplete_results: false`. `Gap 504-A` is now a **deterministic property of the index**, not an
> incident: reconcile queried against returned on every call.
> 🟢 **`Gap 488-Q` half-closes.** OECD **TALIS 2024 country notes** — the same instrument this base
> already quotes for 🇧🇷56/🇨🇱55/🇨🇴53/🇨🇷52 — carry **🇸🇬 ~75%, 🇦🇺 66%, 🇯🇵 <20%, 🇦🇪 ~75%,
> 🇸🇦 43%, 🇩🇰 36%, 🇫🇷 14%, 🇺🇸 43%**. The APAC rate was never missing; **the country notes were
> never queried.** 🔴 It stays half-open because TALIS 2024 is **2024 fieldwork** — the "pre-2026"
> half of the original objection survives. Re-registered as **`Gap 507-A`**.
> 🔴 **Every figure above is search-summary attested only: `oecd.org` and `ei-ie.org` are 403 at the
> CONNECT**, as is the entire non-GitHub web this session. 🔴 **And the OECD average is quoted as
> both 36% (OECD notes) and ~41% (Education International) for the same survey — quote 36% with the
> OECD attribution and never mix them.**
> 🔴 **Five probes gave five false answers this pass, all mine**, including one that nearly retired
> `p505`'s correct *"raw curl → 403"* row on the strength of a **200 from `api.github.com/`** that
> cannot read a repository. `Gap 506-B`'s known-good/known-bad control caught all five.
> Reads: [`api-shelf-read.2026-10-28-p507.tsv`](../evidence/api-shelf-read.2026-10-28-p507.tsv),
> [`new-addresses.2026-10-28-p507.tsv`](../evidence/new-addresses.2026-10-28-p507.tsv),
> [`probe-errors.2026-10-28-p507.tsv`](../evidence/probe-errors.2026-10-28-p507.tsv),
> [`talis-regional-placement.2026-10-28-p507.tsv`](../evidence/talis-regional-placement.2026-10-28-p507.tsv).

### 🟢 `p507` — the one new agent row

| Agent | Repo | Licence | ★ / forks | Archived | What it does |
|---|---|---|---|---|---|
| **TorchLeet** | [`Exorust/TorchLeet`](https://github.com/Exorust/TorchLeet) | 🟢 **MIT** | 2,595 / 323 | 🟢 `false` | 65 ML/AI problems from real interviews, Jupyter-based, with **an auto-grader and an MCP AI tutor**. 🟢 The MCP surface makes it composable with any agent on this shelf rather than a closed app; the auto-grader makes it the rare tutoring repo that **also carries assessment**. Pushed 2026-10-21. |

🔴 **Rejected this pass, with the reason stated rather than silence:**

| Repo | ★ | Licence | Why not shelved |
|---|---|---|---|
| [`echo-loop/Echo-Loop`](https://github.com/echo-loop/Echo-Loop) | 4,549 | 🔴 **AGPL-3.0** | 🔵 Strong design — intensive listening, shadowing, blind listening, retelling, spaced review — and **4,549★ in under six months**. 🔴 AGPL-3.0 reaches networked use; not a base Globant can build a client product on. **Carry as an 🇨🇳 APAC design reference.** |
| [`penecho/penecho`](https://github.com/penecho/penecho) | 2,509 | 🔴 **AGPL-3.0** | 🔵 The **non-chat** surface — handwriting, equations, diagrams, spatial reasoning — which is the right instrument for maths and early-years and the wrong one for a chat box. 🔴 Same licence bar. |
| [`TarrySingh/…-Tutorials`](https://github.com/TarrySingh/Artificial-Intelligence-Deep-Learning-Machine-Learning-Tutorials) | 4,018 | 🔴 **NOASSERTION** | 🔴 **No OSI licence detected.** Valuable as an **EU AI Act conformity-evidence curriculum** (EMEA), but all-rights-reserved until a grant is read at a pinned blob. |


> 🟢 **`p505` (`2026-10-28`) — THE SHELF WAS RIGHT AGAIN, AND THE ONE CLAIM THAT LOOKED REFUTED SURVIVED THE TEST THAT MATTERS.**
> 🟢 **`p506` re-read `DeepTutor` at 47,445★** (`p505`: 47,338, **+107**), `Apache-2.0`, `archived: false`.
> 🟢 **`DeepTutor` re-read at 47,338★** (`p504`: 47,230, **+108**), `Apache-2.0`, `archived: false`,
> 5,895 forks. Its pin `a31d82624c27` is **unchanged for a 7th consecutive pass**, and a census of
> **87 tags** version-sorted still maxes at **`v1.6.15`** — so this file's *"attention, not
> shipping"* reading now holds on **both** the branch ref and the tag ref.
> 🔴 **`Gap 505-A` — and it nearly wrote a false correction into this file.** The API returned
> `pushed_at: 2026-10-28T13:22:04Z`, twenty minutes before this pass. That reads exactly like a
> refutation of the byte-stability claim above. It is not: **`pushed_at` advances on a push to any
> ref** — side branch, tag, fork-sync — so it signifies neither a moved `HEAD` nor a new release.
> **Never grade shipping or staleness from it**; grade from `HEAD` plus a version-sorted tag census.
> 🔴 **`Gap 505-B` — `p502`'s channel correction is channel-specific.** It retired the verification
> row *"`api.github.com` — 403"* as false; measured this pass, the **MCP channel answers 200** while
> **raw `curl` to `api.github.com` is still 403**. Both rows are true of different channels, so the
> table below must carry a **channel** column or the next pass will re-retire a correct row.
> 🔴 **`Gap 505-C` — a lexicographic tag sort misreads the newest release.** `ls-remote --tags |
> tail` returns `v1.6.9` as the last of 87; `sort -V` returns `v1.6.15`. Off `tail`, DeepTutor reads
> as having *regressed* six releases.
> 🟢 **Standing checks applied:** `Gap 504-A` reconciliation **4 queried / 4 returned**; `T29`
> `archived: false` on all four addresses.
> 🔴 **`Gap 483-K` is not closable from this session by any address.** The whole `.europa.eu` family
> is **403 at the CONNECT**, attested by the proxy's own `connect_rejected` log — a host-policy
> denial, not a resolution failure. Quote **2 Dec 2027** / **2 Aug 2028** and name the reading.
> Reads: [`api-reconciliation.2026-10-28-p505.tsv`](../evidence/api-reconciliation.2026-10-28-p505.tsv).

> 🟢 **`p504` (`2026-10-28`) — THE FIGURES THIS FILE CARRIED WERE RIGHT, AND THE CHANNEL THAT PROVED IT IS LESS TRUSTWORTHY THAN `p502` SAID.**
> 🟢 **`Gap 502-A` is CLOSED.** All **87** live shelf addresses across this file,
> [`repos/foundations.md`](../repos/foundations.md) and
> [`verticals/solutions.md`](../verticals/solutions.md) were re-read on the API channel in four
> batched calls. **15 of 15 exact-integer cells came back identical**; every rounded cell agrees to
> its stated precision; the only exact cell that moved is `k12-teacher-skills` **595 → 598**.
> 🟢 **So `p490`'s 31× `educhain` error was never a measurement error** — it was a cycle-2 claim
> carried unexamined for ~500 passes. The defect class is **the carry**, and the fix is a re-read
> cadence, not a better reader.
> 🔴 **But the channel drops rows silently.** [`openedx/edx-platform`](https://github.com/openedx/edx-platform)
> — **8.2k★, AGPL-3.0**, a foundation row — is absent from the search index: **422 when queried
> alone, silently missing from a batch that reports `"incomplete_results": false`**. The exclusion
> is **per-repository** (the rest of the `openedx` org answers normally) and the repo demonstrably
> exists (`ls-remote` → `refs/heads/master`). **A missing row and a nonexistent repo are the same
> observation on this channel** (`Gap 504-A`) — so reconcile queried slugs against returned ones,
> every call. Forks are a second, separate omission class (`Gap 504-B`): `foradian/fedena` returns
> only with `fork:true`.
> 🔴 **And a live shelf was recommending an ARCHIVED repository**: `ably-labs/realtime-quiz-framework`
> reads `archived: true` and was carried on two shelves as "the permissive base" with no
> end-of-life flag. Fixed in both places; **`archived` is now part of the standing batch read**.
> Reads: [`api-shelf-reconciliation.2026-10-28-p504.tsv`](../evidence/api-shelf-reconciliation.2026-10-28-p504.tsv),
> [`api-silent-omission.2026-10-28-p504.tsv`](../evidence/api-silent-omission.2026-10-28-p504.tsv).

> 🟢 **`p502` (`2026-10-28`) — THE VERIFICATION TABLE BELOW TOLD YOU NOT TO USE A CHANNEL THAT WORKS.**
> Its row *"stars for arbitrary repos — `api.github.com` — **403, per-repository authorisation
> only**"* is **false as of this pass**: the GitHub REST API answers through this session's MCP
> channel and returns `stargazers_count`, `license.spdx_id`, `topics`, `forks_count` and `archived`
> for up to 100 repositories per call. The table is corrected in place below. 🔴 **This matters
> because `p490` found star cells in this base overstated by up to 31× (`educhain`: 12,000 → 387),
> an error class that one-HTML-fetch-at-a-time measurement produces and `stargazers_count` makes
> structurally impossible.** 🟢 ~~**Only 6 of this file's ~17 shelf rows were re-read on the new
> channel this pass** (`Gap 502-A`); the rest still carry HTML-era figures.~~
> **`Gap 502-A` CLOSED at `p504`:** all 87 shelf addresses re-read on the API channel and the
> carried figures were accurate — **15 of 15 exact-integer cells identical**, every rounded cell
> right to its stated precision. **The carry, not the channel, was the defect.**
> 🔴 **Do NOT take dates from the API.** Its `pushed_at` counts a push to *any* ref, so it reports
> [`openfun/warren`](https://github.com/openfun/warren) as pushed **today** against a `main` branch
> **708 days unmoved** — `Gap 396-G` HOLDS, now against three channels (`Gap 502-B`). Date with git.
> Reads: [`channel-crosscheck.2026-10-28-p502.tsv`](../evidence/channel-crosscheck.2026-10-28-p502.tsv),
> [`axis-saturation.2026-10-28-p502.tsv`](../evidence/axis-saturation.2026-10-28-p502.tsv).
> 🔵 **`p501`'s 65%-novelty finding does not survive a star floor:** `topic:ai-in-education` holds
> **3 repositories above 50★ and this base already carried all three**. Discovery above 50★ is
> saturated on every axis swept; `Gap 498-A`'s original reading is restored.

> 🟢 **`p501` (`2026-10-28`) — ONE PROMOTION, AND THE REASON IT WAS MISSED IS WORTH MORE THAN THE ROW.**
> [`GeminiLight/SocialCoach`](https://github.com/GeminiLight/SocialCoach) is **Apache-2.0 at 438★ with
> 57 forks** — the **fourth-largest education-specific permissive repository** this base holds, and it
> was invisible to eleven passes of discovery because it carries **`topic:ai-in-education`, not
> `topic:edtech`**. `p499` measured novelty at **19.2%** on the `edtech` axis and `Gap 498-A` read that
> as *"the supply is largely read"*. 🔴 **Measured this pass on the `ai-in-education` axis: 13 of 20 rows
> are NEW to this base — 65%, 3.4× `p499`'s figure.** The refutation of `Gap 498-A` was **axis-bound**,
> not sector-wide (`T22`, `Gap 501-A`). Reads:
> [`aie-axis-overlap.2026-10-28-p501.tsv`](../evidence/aie-axis-overlap.2026-10-28-p501.tsv),
> [`licence-bytes.2026-10-28-p501.tsv`](../evidence/licence-bytes.2026-10-28-p501.tsv).
> 🟢 `DeepTutor`'s HEAD is **unchanged for a fourth consecutive pass** (`a31d82624c27`); its star cell
> is refreshed to **47,000** and `v1.6.15` (`2026-10-19`) is still its newest release.

> 🔴 **`p493` (`2026-10-28`) — READ THIS BEFORE THE TABLES.** `p493` found that **eight
> repositories earlier passes recorded as promoted are absent from this file**, dropped by
> `p490`'s full-file rewrite without leaving a marker. They are **restored into the tables below**,
> each re-verified first-hand this pass. Two consequences for text that still stands elsewhere in
> this file: the gap *"no permissive education-specific agent above 1,000★ other than DeepTutor"*
> is **false** — [`THU-MAIC/OpenMAIC`](https://github.com/THU-MAIC/OpenMAIC) is **MIT at
> 41,700★** — and the evaluation tier's *"none of them is licensed"* is **false** —
> [`AI-for-Education/pedagogy-benchmark`](https://github.com/AI-for-Education/pedagogy-benchmark)
> is **MIT**. Both corrections are applied in place below. Narrative:
> [`agents/trending.md`](trending.md) `p493`; reads:
> [`licence-and-stars.2026-10-28-p493.tsv`](../evidence/licence-and-stars.2026-10-28-p493.tsv).

**Pass `p491` — reads of 2026-10-27.** `p490` (earlier the same day) rewrote this file to its
specified table shape; `p491` **extends** it and does not rewrite it. The p490 tables below stand
unchanged — every p490 SHA was re-resolved this pass and came back **identical**
(`DeepTutor a31d82624c27`, `mentingo e137ca47cbec`, `oppia bc73ecf9cf71`), so there is no upstream
drift to reconcile. The 57 pre-p490 pass-sections remain in
[`archive/2026-10-27-p490-pre-rewrite/top.md`](../archive/2026-10-27-p490-pre-rewrite/top.md).

**New this pass:** an **evaluation-instruments** table (below), which changes the standing claim
that no education-AI evaluation instrument exists — they exist, and **none of them carries a
license**. Evidence:
[`licence-and-stars.2026-10-27-p491.tsv`](../evidence/licence-and-stars.2026-10-27-p491.tsv).

## How every cell here was verified

| step | channel | result |
|---|---|---|
| repo exists + default branch | `git ls-remote --symref` | works; authoritative |
| license text | `raw.githubusercontent.com/<repo>/<SHA>/<path>` **at the pinned SHA** | works |
| stars + sidebar license | `github.com` repo page via page fetch | works |
| ~~existence~~ | `curl -sI https://github.com/<repo>` | **403 on every repo — do not use** |
| stars + licence + topics + forks + **`archived`**, 100 rows/call | **GitHub REST API via the MCP channel** | 🟢 **WORKS (`p502`)** — authoritative **for the rows it returns**; supersedes the two rows above for stars and licence family. 🔴 **`p504`: IT DROPS ROWS SILENTLY.** `openedx/edx-platform` is absent from the index: alone it raises **422**, batched it vanishes with `"incomplete_results": false` and no error. **Reconcile the returned `full_name` set against the queried slug set on every call** (`Gap 504-A`). 🔴 **Forks are excluded unless `fork:true`** (`Gap 504-B`). 🔵 `minimal_output` omits `license` — licence stays on the bytes reader. |
| ~~stars for arbitrary repos~~ | ~~`api.github.com` via `curl`~~ | 🔴 **403 — but this is a `curl` refusal, not an API refusal; see the row above (`Gap 502-A`)** |
| 🆕 rate/quota check | `curl https://api.github.com/` and `/rate_limit` | 🟢 **200 (`p506`)** — core limit 15 000. 🔴 **`Gap 505-B` is therefore WRONGLY STATED as a host-level denial:** the refusal is **PER-ENDPOINT**, not per-host. This table needs **endpoint** granularity, not a `channel` column |
| 🆕 repo metadata by slug | `curl https://api.github.com/repos/<repo>` | 🔴 **403 (`p506`, 3 of 3 tried)** — the endpoint that is actually denied. Use the MCP channel |
| 🆕 any non-GitHub host | `curl` **or** `WebFetch` | 🔴 **REFUSED AT THE CONNECT (`p506`, 10 hosts + 3 `WebFetch` `ENOTFOUND`)** — `ec.europa.eu`, `eurydice.eacea.ec.europa.eu`, `www.oecd.org`, `assets.publishing.service.gov.uk`, `explore-education-statistics.service.gov.uk`, `mgaleg.maryland.gov`, `arxiv.org`, `files.eric.ed.gov`, `www.sanoma.com`, `www.statista.com`. 🔵 **Generalises `Gap 483-K` from the `europa.eu` family to *every* host but `github.com` and `raw.githubusercontent.com`.** So `Gap 505-F`'s Maryland primary is **not closable here** |
| 🆕 open-web facts | **`WebSearch`** | 🟢 **the ONLY open-web channel in this session (`p506`)**. Everything it returns is `SEARCH-ATTESTED, PRIMARY UNREAD` — never grade a WebSearch snippet as a primary read |
| ~~mainline freshness~~ | ~~API `pushed_at` / `updated_at`~~ | 🔴 **DO NOT USE — `pushed_at` is branch-agnostic; 708 d error measured (`Gap 502-B`)** |
| mainline freshness | `git clone --depth 1`, committer date | 🟢 authoritative |

License family is anchored on the **first 200 bytes (the title block)**, never on a body scan —
see the reader defect recorded below. Evidence:
[`licence-and-stars.2026-10-27-p490.tsv`](../evidence/licence-and-stars.2026-10-27-p490.tsv).

## Permissive — Globant can build on these

**Eighteen rows** (🟢 `p511` promoted `studorama`, the first LATAM-placed row here; `p501` promoted `SocialCoach`), MIT / Apache-2.0 / BSD-3-Clause, each license read from bytes at the SHA shown.
🟢 **`p493` restored seven of them** (`OpenMAIC`, `k12-teacher-skills`, `dolos`, `open-tutor-ai-CE`,
`agent-skills`, `rumi-platform`, `Shiksha-Copilot`) after finding they had been promoted by earlier
passes and then dropped by `p490`'s full-file rewrite. 🔵 **`p492` added no row here** — the one new
permissive education agent it found has **0★** and is listed under *reference designs* below,
deliberately outside this shelf; `p493`'s five new finds are all below the floor too and are listed
in [`trending.md`](trending.md) rather than here.

| Agent | Repo | License | ★ | SHA read | What it does |
|---|---|---|---|---|---|
| DeepTutor | [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | Apache-2.0 | **47,725** *(🟢 `p510`, API; `p509` read 47,677; `p506` 47,445; `p505` 47,338; `p504` 47,230; `p502` 47,051)* | `1ea7df155447` *(🔴 `p509` retired `a31d82624c27`; `p510` re-attests `1ea7df155447` over the git protocol)* | Lifelong personalised tutoring; graph-enhanced RAG over course material. Largest education-AI repo on GitHub. 🟢 **`p501`: HEAD unchanged for a FOURTH consecutive pass (`p491`→`p501`); `v1.6.15` (`2026-10-19`) is still the newest release, so the star growth is attention, not shipping.** 🟢 **`p505` re-tested that reading on the ref it actually depends on:** a census of **87 tags**, version-sorted, still maxes at **`v1.6.15`**, and `HEAD` is unchanged for a **7th consecutive pass** — so the claim holds on both refs. 🔴 **`p505` also records why this nearly flipped:** the API returned `pushed_at: 2026-10-28T13:22:04Z`, which reads like shipping and is not (`Gap 505-A` — `pushed_at` advances on a push to any ref). Its own repo page links a design paper at `arxiv.org/abs/2604.26962` (upstream News item dated `2026-04-10`). 🔵 **Unverified — `arxiv.org` does not resolve from this session's network**, so this is an upstream-asserted identifier, not a read. **See license caveat below.** |
| OpenMAIC | [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) | **MIT** | **41,712** *(🟢 `p510`, API; `p509` read 41,712; `p502` 41,690; `p493` 41,700)* | `70859b42e714` | **Open Multi-Agent Interactive Classroom** — any topic or document becomes an interactive lesson with slides, quizzes and project-based work. 781 commits; `v1.3.0-rc.1` dated `2026-10-22`; licence 1 065 B, `sha1 56d5b3ffd6e8`. 🟢 **Restored `p493`** after being dropped by `p490`'s rewrite — this is the row that falsifies this file's own permissive-scarcity gap, and its MIT grant is cleaner than DeepTutor's. 🔵 Org is `THU-MAIC` and the partnership contact is a `mail.tsinghua.edu.cn` address; **Tsinghua attribution is inferred from those, not stated in prose.** 🔴 **Not an LMS** — no enrolment, gradebook or SIS integration is claimed. |
| smolagents | [huggingface/smolagents](https://github.com/huggingface/smolagents) | Apache-2.0 | **30,121** *(🟢 `p510`, API; `p504` 30,118; prior rounded cell read 30,100)* | `96f33faaf028` | Minimal code-writing agent loop. Not education-specific; the usual substrate for a custom tutor agent. |
| k12-teacher-skills | [anthropics/k12-teacher-skills](https://github.com/anthropics/k12-teacher-skills) | Apache-2.0 | **600** *(🟢 `p510`, API; `p509` read 600; `p504` 598; `p493` 595 — no longer the only exact cell that has moved: `p510` found 9)* | `31fd6dbb0c07` | Four K-12 teacher skills (lesson planning, differentiation and two more) **plus the eval rubrics for them**, co-developed with Learning Commons. Licence 11 357 B, `sha1 1128f8f91104`. 🟢 **Restored `p493`** — recorded "Now shelved" on `2026-10-18` and never actually present in this file. 🔴 **This is the asset `p492` declared licence-unverifiable;** it was measured in this KB twice before that. |
| SocialCoach | [GeminiLight/SocialCoach](https://github.com/GeminiLight/SocialCoach) | Apache-2.0 | **440** *(🟢 `p502`, API; `p501` read 438)* | `84f67257f5aa` | **Social-emotional learning coach** — role-play scenarios for conflict handling and communication, with personalised feedback. 239 commits, **57 forks**. 🟢 **Promoted `p501`**, and it is the first row on any shelf here in the **social-emotional / soft-skills layer** — `social-emotional` returned **0 hits across every live shelf** before this pass. Licence **11 358 B, blob `d645695673…`: byte-identical to apache.org's own copy**, graded **`0/0` operative against Apache-2.0** by [`p501`'s guarded grader](../compose/code/p501-abstention-and-reresolve/). 🔴 **No release and no tag** — 239 commits on `main` and nothing cut; treat as a watch row, not a deployable product (`Gap 499-H`'s shape). 🔴 Carries `topic:ai-in-education` and **not** `topic:edtech`, which is why 11 passes of `topic:edtech` sweeps never saw it (`T22`). |
| educhain | [satvik314/educhain](https://github.com/satvik314/educhain) | MIT | **387** | `38adb1e9459d` | Python package generating educational content (MCQs, lesson plans, flashcards) from an LLM. |
| dolos | [dodona-edu/dolos](https://github.com/dodona-edu/dolos) | MIT | **355** | `74b101785bad` | Source-code plagiarism detection; **3,865 commits**, the most-maintained address on this shelf. Ghent University. 🟢 **Restored `p493`** — `p296` tried to promote it, this KB's identity gate correctly refused the duplicate because a `foundations.md` row existed, and **that row was then deleted by a later rewrite too.** Licence 1 084 B, `sha1 8f6f3815d28d`. |
| Skill-Anything | [SYuan03/Skill-Anything](https://github.com/SYuan03/Skill-Anything) | MIT | 344 | `3cdc1c1f11dc` | Any source (PDF, video, web, audio) → interactive package with quizzes, flashcards, spaced repetition. |
| canvas-mcp | [vishalsachdev/canvas-mcp](https://github.com/vishalsachdev/canvas-mcp) | MIT | 309 | 🟢 **PIN THE TAG: `v1.16.0` = `b3f06c76e435`** *(`p495`)* — HEAD `47394125364b` is **unreleased code ahead of it** | MCP server over Canvas LMS. 🔴 **`p495`: `v1.16.0` IS A SECURITY FLOOR, not a drift preference. All FOUR advisories are patched at `1.16.0`; two are High — `GHSA-7pp5-29mw-9jq3` (sandbox escape, **CVSS 7.8**, affected `< 1.16.0`) and `GHSA-hmr8-mvr2-mvw5` (prompt injection → data disclosure / grade change, affected `≤ 1.12.0` and `1.13.0–1.15.0`, patched in two stages: write allowlist at `1.13.0`, untrusted file contents at `1.16.0`). 🔴 The sandbox fix REQUIRES **Node.js ≥ 22.18** — on an older Node the patched release is NOT patched. 🔴 Residual risk the advisory states as UNFIXED: outbound network blocking in local mode is best-effort, and executed code can still reach the caller's Canvas token. 🟢 HEAD stable since `p494` (no third move). 🟢 Advisory count re-read at the new SHA: still FOUR.** 🔴 **`p494`: drifted AGAIN — second move in ~24h, and it moved *within this pass's own window*. Licence byte-identical at all three SHAs (MIT, 1 071 B, `sha1 491fb891a4cf`), so every move so far is code-only. 🔴 Pin a RELEASE TAG here, not a branch HEAD.** 🔴 **`p492`: HEAD drifted from `32e5d1ca0175`; licence byte-identical at both SHAs (1 071 B, `sha1 491fb891a4cf`) so the drift is code-only. `v1.16.0` lists FOUR advisories, not one** — `GHSA-7mj9-4mcg-hvhv` (Canvas token handling), `GHSA-7pp5-29mw-9jq3` (local code sandbox), `GHSA-hmr8-mvr2-mvw5` (file content fencing), `GHSA-qf6c-jv93-38gv` (Windows download permissions). Tool count self-inconsistent upstream (description 102, README 128) — **stop quoting a number**. |
| OATutor | [CAHLR/OATutor](https://github.com/CAHLR/OATutor) | MIT | **274** | `e24c8456e5f7` | Intelligent tutoring system with Bayesian Knowledge Tracing; ReactJS + Firebase. UC Berkeley CAHLR. |
| KSoR | [panaversity/ksor](https://github.com/panaversity/ksor) | Apache-2.0 | 232 | `b50f28926fae` | SDK for governed, authoritative knowledge systems for humans and agents. Names education institutions as its target. |
| open-tutor-ai-CE | [Open-TutorAi/open-tutor-ai-CE](https://github.com/Open-TutorAi/open-tutor-ai-CE) | **BSD-3-Clause** | 114 | `196c547291da` | Educational and collaborative AI platform, community edition. 380 commits and **194 forks against 114★** — a fork-heavy ratio that reads as deployment, not stargazing. 🟢 **Restored `p493`**, and 🔵 **its family is confirmed from the bytes**: the 1 531-byte payload opens *"All rights reserved"*, which is the literal opening of canonical BSD and which a title-block reader can mistake for a reserved-rights notice; all three BSD conditions including no-endorsement are present. `sha1 a027c9bb4f47`. |
| mentingo | [Selleo/mentingo](https://github.com/Selleo/mentingo) | MIT | **101** *(🟢 `p511`, API; prior cell `100`, round)* | `e137ca47cbec` | Self-hostable LMS with AI mentoring and role-play. Tenant isolation enforced in Postgres RLS, not app code. |
| agent-skills (Learning Commons) | [learning-commons-org/agent-skills](https://github.com/learning-commons-org/agent-skills) | Apache-2.0 | 40 | `8b0599c24469` | The same four K-12 teacher skills from the education-consortium side, with `evals/` rubrics for pedagogy, rigour, format and scaffolding. `NOTICE` (268 B) names **Anthropic, PBC** and **Learning Commons**. Licence 10 173 B, `sha1 e88848668567`. 🟢 **Restored `p493`.** |
| rumi-platform | [Orenda-Project/rumi-platform](https://github.com/Orenda-Project/rumi-platform) | Apache-2.0 | 18 | `f2d62af1eb82` | **WhatsApp-delivered** learning in **15 languages**; 847 commits. Pakistan / Taleemabad. 🟢 **Restored `p493`** — the only no-app, no-browser delivery surface on this shelf, which matters wherever `T9`'s offline-first argument applies. Licence 11 287 B, `sha1 20312eb940f0`. |
| Shiksha-Copilot | [microsoft/Shiksha-Copilot](https://github.com/microsoft/Shiksha-Copilot) | MIT | 9 | `cf2a2e24c3d4` | Microsoft Research India, **VELLM** initiative, with the Sikshana Foundation. Lesson plans, examples, analogies, activities, assessments — **all routed to a teacher for review before classroom use**, which is the human-oversight shape `P490-2` argues for. 149 commits; licence 1 141 B, `sha1 689ec0681815`. 🟢 **Restored `p493`.** |
| AI Agents for Beginners | [microsoft/ai-agents-for-beginners](https://github.com/microsoft/ai-agents-for-beginners) | MIT | **78,059** *(🟢 `p510`, API; `p504` 78,039)* | `dd0f080d07d2` | 18-lesson agent course. **A curriculum, not a deployable agent** — listed because it is the most-starred thing in this space and is routinely miscatalogued as a product. |
| Studorama | [oluiscabral/studorama](https://github.com/oluiscabral/studorama) | **MIT** | **111** *(🟢 `p511`, API; `archived: false`)* | `2ddbb1122b5b` | 🆕 **New row `p511`, and the first LATAM-placed AI PRODUCT on this shelf** — multi-provider AI study platform (OpenAI, Gemini, Anthropic, DeepSeek, **Ollama local**, browser-local; 15+ models) built on named study techniques. Licence read from bytes: `LICENSE` **1,064 B**, `sha256₁₆ 75ecd9ad0bb3b543`. **10 tags.** Region placed on the product's own bytes — the `README` (12,965 B) declares **"Complete English and Portuguese (Brazil) localization"** and *"Cultural Adaptation: region-specific content"* as first-class features. 🔴 **Single maintainer**, licence holder is a personal handle: fork-and-own, do not take a dependency. 🟢 Breaks `p509`'s nil that the LATAM-reachable set contains *"none an AI product"*. |

## Copyleft — usable, but not for a hosted commercial derivative

| Agent | Repo | License | ★ | SHA read | Constraint |
|---|---|---|---|---|---|
| ChatTutor | [HugeCatLab/ChatTutor](https://github.com/HugeCatLab/ChatTutor) | **AGPL-3.0** | **1,316** *(🟢 `p502`, API; prior cell read 1,300)* | `7d9e9052bc5a` | Visual/interactive AI tutor, whiteboard + math canvas. AGPL reaches across the network: hosting it for a client triggers source obligations. |
| tutor-gpt | [plastic-labs/tutor-gpt](https://github.com/plastic-labs/tutor-gpt) | **GPL-3.0** | 932 *(🟢 `p504`, API — identical to the carried cell)* | `5c2f92416c04` | Theory-of-Mind tutoring agent. GPL, not permissive — several public listicles call this one "open source" without naming the family. |

## Corrections this pass — figures this KB published that were wrong

Each confirmed against two independent channels (license bytes at a pinned SHA, and the
repository's own sidebar).

| row | this KB published | measured `p490` | error |
|---|---|---|---|
| `satvik314/educhain` | `~12,000★` since cycle 2 | **387★** | **31×** overstated |
| `CAHLR/OATutor` | `~1,300★` (cycle 2), `~1,500★` (cycle 3) | **274★** | ~5× overstated |
| `frappe/lms` | `MIT` (and still claimed MIT by current web sources) | **AGPL-3.0** | wrong family; permissive→network copyleft |
| `oat-sa/tao-core` | `GPL-2.0-or-later` | **GPL-2.0** per bytes *and* sidebar; the `or-later` election is **not** readable from the payload | overclaimed |
| `RosarioSIS/RosarioSIS` | cited as a path | **404** — the repo is [`francoisjacquet/rosariosis`](https://github.com/francoisjacquet/rosariosis) | dead URL |
| `microsoft/autogen` | `MIT` | root `LICENSE` is **CC BY 4.0**; the code grant is **MIT at `LICENSE-CODE`** | right answer, reached without reading |

### The AutoGen split, stated plainly

`microsoft/autogen` serves **two** grants and a root-`LICENSE` reader gets the wrong one:

- `LICENSE` → `Attribution 4.0 International` (Creative Commons, 18,650 B) — the docs/content grant.
- `LICENSE-CODE` → `MIT License` — **the code grant.**

Any sweep on this KB that probes only `LICENSE` will file Microsoft agent repos as Creative
Commons. That is a false negative that removes a usable MIT row from the shelf.

### A defect in this pass's own reader, recorded rather than quietly fixed

The first reader run this pass graded [`oat-sa/tao-core`](https://github.com/oat-sa/tao-core) as
`LGPL-2.0`. It is `GPL-2.0`. Cause: the reader scanned the first 3,000 bytes, and **the GPLv2
preamble names the Lesser GPL** ("…the GNU Lesser General Public License instead…"), so a
body scan matches `LGPL` before it reaches the real family. The reader was re-anchored on the
200-byte title block and all 28 rows re-read; `tao-core` and `rosariosis` moved to `GPL-2.0`,
and the two genuine LGPL rows (`bigbluebutton` 7,652 B, `openeducat_erp` 8,241 B) held.

**Rule for later passes: anchor the family on the title block. A GNU preamble cross-references
the sibling licenses, so any body scan is a family false-positive generator.**

## The DeepTutor license caveat — carried forward, still true

🟢 **`p506` re-derived this figure and NAMED THE POPULATION the old one never stated — which was
the actual defect (`Gap 505-F`, closed).** Over the **permissive, education-specific rows on this
shelf** — **46 addresses, Σ 106,506★** — `DeepTutor` is **47,445 of 106.5k**, i.e. **44.5%**.
🔵 The carried `~118k` was sound but undefined: the same question answered over *every* shelf
address gives **601,119★** and over *all* permissive rows **415,299★**, a **5.6× spread** driven
entirely by whether general-purpose AI-learning-resource repos are counted. Exclusions are itemised
in [`permissive-tier.2026-10-28-p506.tsv`](../evidence/permissive-tier.2026-10-28-p506.tsv) so the
denominator is reproducible.

🔴 **`p493` correction to the figure this section opens with: DeepTutor is no longer 88% of this
shelf's star mass.** With `OpenMAIC` (MIT, 41,700★) restored, DeepTutor is under half of the
permissive tier. The concentration argument below needs restating, not repeating; the *provenance*
point it introduces is unaffected and still stands.

`HKUDS/DeepTutor` carries 47.4k★ *(🟢 `p506`, API: 47,445)* and its Apache-2.0 payload (11,408 B) is
**not** canonical Apache-2.0 (10,015 B operative span). Three function-word substitutions sit in
the operative body:

| § | canonical | DeepTutor |
|---|---|---|
| §1 *Contribution* | "submitted to Licensor" | "submitted to **the** Licensor" |
| §1 *Contributor* | "received by Licensor" | "received by **the** Licensor" |
| §4(d) NOTICE | "excluding **those** notices" | "excluding **any** notices" |

**Legal effect: nil** — "the Licensor" is "Licensor"; both NOTICE phrasings are the same
restrictive clause. No hunk touches the grant, patent or disclaimer sections.
**Supply-chain signal: not nil** — the appendix is replaced with an instruction to apply an
"Alarm" trademark header unrelated to the licensor (Data Intelligence Lab, University of Hong
Kong), and the same edited payload appears byte-identically in the derivative
[`3yangyang9/DeepTutor-AILearning`](https://github.com/3yangyang9/DeepTutor-AILearning) (136★),
which is how a copied license travels. Treat it as a provenance flag, not a license risk.

## Evaluation instruments — they exist, and 🟢 **one of them IS licensed** (`p493` correction)

`p490` recorded "no open-source education-AI evaluation harness above 60★ exists" and treated the
tier as empty. `p491` replaced that with a sharper claim — that the instruments exist and **not one
of them ships a license grant**.

🔴 **`p493`: that sharper claim is also false, and the counter-example was already in this KB.**
[`AI-for-Education/pedagogy-benchmark`](https://github.com/AI-for-Education/pedagogy-benchmark) is
**MIT** (1 064 B, `sha1 ac3710f1a312`, read at `21a43a395ab4`; sidebar and README agree). It was
read on `2026-10-18`, recorded in `agents/trending.md`, and never landed in this file — the same
dropped-row defect described in the banner at the top. **The tier is small and under-starred, not
unlicensed.**

| Instrument | Repo | Grant at SHA | ★ | What it measures |
|---|---|---|---|---|
| MathTutorBench | [eth-lre/mathtutorbench](https://github.com/eth-lre/mathtutorbench) | 🔴 **no license file** (`6faed173ec2b`) | 45 | Open-ended *pedagogical* capability of LLM tutors — 3 teacher skills, 7 tasks. EMNLP 2025 Oral (arXiv 2502.18940). |
| TutorCaseBench | [kixlab/TutorCaseBench](https://github.com/kixlab/TutorCaseBench) | 🔴 **no license file** (`6b9ac34262c7`) | 0 | Tutor behaviour with students showing challenging behaviours; 923 dialogues, 5 challenge types. KAIST. |
| **pedagogy-benchmark** | [AI-for-Education/pedagogy-benchmark](https://github.com/AI-for-Education/pedagogy-benchmark) | 🟢 **MIT**, 1 064 B (`21a43a395ab4`) | 13 | **Pedagogical knowledge of LLMs, from teacher-qualification exams**: 1,143 questions — **920 CDPK** (cross-domain pedagogical knowledge) and **223 SEND** (special educational needs and disabilities) — with harness support for "100+ models". Paper: *Benchmarking the Pedagogical Knowledge of Large Language Models*, `arXiv:2506.18710`. 🟢 **The licensed education-specific instrument this KB spent three passes declaring does not exist.** Restored `p493`. |
| lm-evaluation-harness | [EleutherAI/lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) | 🟢 **MIT**, 1,066 B (`d6de81643928`) | **14,341** *(🟢 `p510`, API; `p504` 14,338)* | Not education-specific — the general runtime. The permissive *runtime* in this tier. |

🔴 **MathTutorBench's own README contradicts itself on the license**: the badge reads
`License: CC BY 4.0` and the closing line of the same file says
*"Creative Commons Attribution-**ShareAlike** 4.0"*. The sidebar shows no license at all. Those
are two different licenses, **one of them copyleft**, and neither is a software grant — Creative
Commons licenses are content licenses and CC itself advises against using them for code.

**Consequence for an engagement, restated `p493`:** for `mathtutorbench` and `TutorCaseBench` the
old consequence holds — the *tasks* are publishable research you may read and reimplement, the
**repository code and data cannot be taken**, and no grant means no rights rather than
permissive-by-default. 🟢 **But the engagement no longer starts from nothing.**
`pedagogy-benchmark` is **MIT**, so its 1,143 exam-derived items and its 100+-model harness are
**takeable as code and data**. `P491-1` is therefore no longer a build-from-scratch on a bare
runtime: it starts from an MIT education-specific instrument and extends it, with
`lm-evaluation-harness` (MIT) underneath. 🔴 Its 13★ means no community and no security process —
use it as a corpus and a baseline, not as a dependency you expect to be maintained.

## Declared gaps — searched, nothing found

Stating these because silence looks identical to coverage.

- 🔴 ~~**No permissive education-specific agent above 1,000★ other than DeepTutor.**~~
  **RETRACTED `p493` — this was false, and false by ~40×.**
  [`THU-MAIC/OpenMAIC`](https://github.com/THU-MAIC/OpenMAIC) is **MIT at 41,700★** and
  education-specific. It was not missed by search: this KB read it, recorded it "Now shelved" on
  `2026-10-18`, cites it **51 times** in its own history, and `p490`'s rewrite dropped the row.
  🟢 **The defensible restatement, re-derived at `p506`:** the permissive tier is **concentrated,
  not empty** — two addresses (`DeepTutor` **47,445** Apache-2.0 *(`p506`)*, `OpenMAIC` **41,705**
  MIT *(`p506`)*) hold **89,150 of 106,506★ = 83.7%** of the permissive education-specific tier on
  this shelf.
  🔴 **`p506` RETRACTS the sentence that followed, and it was this file's own:** *"the next
  permissive education-specific row is `k12-teacher-skills` at 595★"*, and the **"595-to-41,700
  cliff"** called *"the real structural finding"*. 🔴 **Six permissive education-specific rows sit
  in that gap, all of them on this shelf** — [`oppia/oppia`](https://github.com/oppia/oppia)
  **6,950** (Apache-2.0), [`Miaotofu01/Study-Mate`](https://github.com/Miaotofu01/Study-Mate)
  **1,246** (MIT), [`dmoshehun-prog/learn-from-materials`](https://github.com/dmoshehun-prog/learn-from-materials)
  **1,190** (MIT), [`beltromatti/get-it`](https://github.com/beltromatti/get-it) **1,138**
  (Apache-2.0), [`DozenTwelve/Papermorph`](https://github.com/DozenTwelve/Papermorph) **992** (MIT)
  and [`anthropics/k12-teacher-skills`](https://github.com/anthropics/k12-teacher-skills) **598**
  (Apache-2.0). 🔵 **Oppia is not an obscure row** — it is a long-standing Apache-2.0 education
  platform carried on this shelf, [`repos/foundations.md`](../repos/foundations.md) *and*
  [`verticals/solutions.md`](../verticals/solutions.md). **The cliff sentence was written about this
  shelf without reading it.**
  🟢 **The true structural claim, which is a better one:** the step down from `OpenMAIC` is
  **41,705 → 6,950, about 6×, not 70×** — concentration **with a credible second tier**, which is
  stronger for a build-on-open proposal than a vacuum.
- 🟢 **`p493` — a permissively-licensed option now exists in four layers this file previously
  showed as copyleft-only or empty**: interactive classroom (`OpenMAIC`, MIT), tutoring platform
  (`open-tutor-ai-CE`, BSD-3-Clause), academic integrity (`dolos`, MIT) and evaluation
  (`pedagogy-benchmark`, MIT). 🔴 **The full-LMS layer is still copyleft-bound** — `OpenOLAT`
  (Apache-2.0) remains the only permissive full LMS, so `T2`'s binding constraint holds *there*
  and nowhere else. See [`repos/trending.md`](../repos/trending.md) `p493`.
- **No LATAM-origin or Africa-origin education agent reached this shelf's star floor.** Searched
  globally and per region; the regional supply is in deployments and national programmes
  (see `intel/market.md`), not in starred repositories. 🔵 **`p493` — the gap is now instantiated
  rather than asserted, and it is still open.**
  [`Jeanikt/tutor-ai-agent`](https://github.com/Jeanikt/tutor-ai-agent) ("Manu") is **MIT**
  (1 103 B, `987f3106ef6a`), a **Brazilian-Portuguese voice math tutor** covering 1st grade to
  university on TypeScript + LiveKit Agents — the first LATAM-origin education agent here with a
  readable grant and a real regional property. At **0★ and 3 commits it does not close the gap**;
  it shows the gap is a supply fact, not a search artefact. **Do not propose it as a dependency.**
  🔵 Africa-origin: still nothing, though `open-tutor-ai-CE` (Morocco) and `rumi-platform`
  (Pakistan) now put North-African and South-Asian origin on the shelf.
- 🔴 ~~**No *usable* open-source education-AI evaluation harness exists.**~~ **RETRACTED `p493`.**
  `mathtutorbench` (45★) and `TutorCaseBench` (0★) do carry no grant, and that part stands — but
  [`AI-for-Education/pedagogy-benchmark`](https://github.com/AI-for-Education/pedagogy-benchmark)
  is **MIT**, education-specific, and was read by this KB on `2026-10-18`. 🟢 **The usable
  instrument exists.** 🔵 **What remains true is the discovery point, and it is sharper now:** a
  star-ordered sweep is blind to this tier (13★) *and* this KB's own star-ordered shelf dropped the
  row — so the blindness was in the bookkeeping as much as in the sweep. See the table above.
- ~~**Commit recency is not on this table.**~~ 🟢 **Partly closed `p492` — a *release* date is
  readable even though a commit date is not.** The page-fetch channel does expose tagged releases
  with dates: `canvas-mcp v1.16.0` (Oct 2026), `DeepTutor v1.6.15` (`2026-10-19`),
  `education-agent-skills v3.1.0` (`2026-10-22`), `openmeetings v9.1.0`. That is a **real liveness
  signal** for any repo that tags releases, and this KB had been declaring it unavailable.
  **Remaining limit:** repos that do not tag releases still have no maintenance signal, and
  `api.github.com` is still 403 for unattached repos. Rows still carry a pinned SHA, which proves
  content; a release date now proves *liveness* where one exists.


## 🆕 `p492` — `2026-10-28` — reference designs, and why they are not shelf rows

Full reads and channel notes:
[`licence-and-stars.2026-10-28-p492.tsv`](../evidence/licence-and-stars.2026-10-28-p492.tsv);
narrative in [`agents/trending.md`](trending.md).

**Three corrections landed in the tables above, not here:** `canvas-mcp`'s drifted SHA and its
**four** advisories, `DeepTutor`'s star count plus its previously-unrecorded arXiv paper, and the
partial closure of the commit-recency gap via release dates.

### Reference designs — read these, do not depend on them

A repo with no community is not supply. It can still be the clearest statement of an architecture,
and this KB has been arguing for the architecture below without ever pointing at code.

| repo | licence @ SHA | ★ | read it for |
|---|---|---|---|
| [`vulinh1704/ai-tutor-agent`](https://github.com/vulinh1704/ai-tutor-agent) | **MIT**, 1 071 B, `sha1 2a558a4b5980` (`5511bf6dc707`) | 🔴 **0** (13 commits, one author) | **Rubric totals computed in code, never by the model** — per-criterion structured output validated against the rubric, arithmetic in Python. Plus an **answer-leak guard** (a hint that reveals the answer is regenerated under a stricter instruction, and replaced by a safe hint if it still leaks) and **session memory as an explicit LangGraph thread** (in-memory or SQLite). FastAPI + LangGraph + Pydantic; CI on Python 3.11–3.14; deterministic fake model for offline tests. |

🟢 **Why this is worth a row in a KB that refuses to pad.** Point 1 is the **human-oversight shape
the EU AI Act requires of a *provider*** of a high-risk assessment system — and
[`intel/market.md`](../intel/market.md) establishes that *for a Globant-built education AI system,
Globant is the provider*. "Do not let the model do the arithmetic" has been this KB's advice for
several passes; this is the first MIT implementation of it we can hand an engineer.

🔴 **Do not propose it as a dependency.** Zero stars, 13 commits, one author, no security process.
It is a **1 071-byte MIT grant over a design worth copying**, which is the entire claim.

### Not an education agent, recorded so it stops resurfacing

| repo | licence @ SHA | ★ | why it is excluded |
|---|---|---|---|
| [`labmlai/annotated_deep_learning_paper_implementations`](https://github.com/labmlai/annotated_deep_learning_paper_implementations) | **MIT**, 1 082 B, `sha1 b3428e1f52c0` (`2be1800d141e`) | **67,603** *(🟢 `p510`, API; `p509` read 67,603; prior cell 67,600)* | 60+ annotated PyTorch paper implementations. **CS-education teaching material, not a deployable agent** — the same miscatalogue this shelf already flags for `microsoft/ai-agents-for-beginners` (**78,061** *(🟢 `p511`, API)*). It would top this table on stars and teach a client nothing about tutoring. 🔵 Its licence file is lowercase **`license`**; probes trying only `LICENSE`/`LICENSE.md` would report "no licence" on an MIT repo. **Add lowercase `license` to every future probe list.** |

### 🔴 Gap restated by `p492` — and it was never a gap. Closed `p493`.

~~**Learning Commons' "Claude for Teachers" agent skills** (Lesson Plan Generation, Lesson
Differentiation; launched July 2026, publicly described as open-source) are **not listed** because
their licence could not be read: no repository resolved under the obvious paths, and
`learningcommons.org` **does not resolve from this session's network**.~~

🔴 **`p493`: both repositories were already measured in this KB, by name, before `p492` declared
this gap** — and both re-measured **byte-identically** this pass:

| repo | earlier read in this KB | `p493` read at SHA | verdict |
|---|---|---|---|
| [`anthropics/k12-teacher-skills`](https://github.com/anthropics/k12-teacher-skills) | Apache-2.0, 11 357 B | **11 357 B**, `sha1 1128f8f91104` (`31fd6dbb0c07`) | 🟢 identical |
| [`learning-commons-org/agent-skills`](https://github.com/learning-commons-org/agent-skills) | Apache-2.0, 10 173 B, `NOTICE` names Anthropic, PBC | **10 173 B**, `sha1 e88848668567` (`8b0599c24469`) | 🟢 identical |

Both are now **rows in the permissive table above**, where one of them had been recorded as "Now
shelved" since `2026-10-18`.

🔵 **The method failure is the transferable part.** `p492` searched the open web for a publisher's
site that does not resolve from this session, and concluded the licence was unreadable. It never
`grep`-ed the repository it was editing. **Rule for later passes: before declaring a gap, run
`grep -ri <subject>` over this repo. A gap declared over evidence the KB already holds is worse
than silence, because it tells the next pass not to look.**

## 🆕 `p494` — `2026-10-28` — no drift, no promotions, and the discovery channel has looped

Reads: [`licence-and-stars.2026-10-28-p494.tsv`](../evidence/licence-and-stars.2026-10-28-p494.tsv).
Narrative: [`trending.md`](trending.md) `p494`.

🟢 **`p493`'s eight restored rows are verified present in the tables above at this pass's HEAD.**
The restoration landed in the file, not just in the pass note — checked by `grep` per address, which
is the test `p493`'s own defect report implies.

### 🔴 Drift sweep — three pins stable, one moved **during this pass**

| repo | KB pin | `p494` `git ls-remote --symref` | verdict |
|---|---|---|---|
| [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) | `a31d82624c27` | `a31d82624c27`, `refs/heads/main` | 🟢 **4 consecutive passes byte-stable** (`p490`–`p494`) |
| [`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp) | `830bc2ef8389` | 🔴 **`47394125364b`**, `refs/heads/main` | 🔴 **DRIFTED AGAIN, mid-pass** — licence byte-identical at both SHAs (MIT, 1 071 B, `sha1 491fb891a4cf`), so code-only. **Shelf row above re-pinned.** |
| [`THU-MAIC/OpenMAIC`](https://github.com/THU-MAIC/OpenMAIC) | `70859b42e714` | `70859b42e714`, `refs/heads/main` | 🟢 `p493`'s restoration pin holds |
| [`HugeCatLab/ChatTutor`](https://github.com/HugeCatLab/ChatTutor) | `7d9e9052bc5a` | `7d9e9052bc5a`, `refs/heads/main` | 🟢 licence re-read from bytes: **AGPL-3.0**, `LICENSE`, **34 522 B**, `sha1 3cd688cb1bd7` — **byte-identical** to this KB's earlier read |

🔵 **The `ChatTutor` row above is now grant-pinned by `sha1`, not by licence tag.** That is what makes
its stated consequence defensible: **AGPL-3.0 reaches across the network, so hosting it for a client
triggers source obligations.** The permissive answer in this layer remains
[`open-tutor-ai-CE`](https://github.com/Open-TutorAi/open-tutor-ai-CE) (BSD-3-Clause) — see
[`../verticals/solutions.md`](../verticals/solutions.md).

### 🔴 No promotions, and the reason is a finding rather than an absence

Both brief-mandated ranking queries were run. **Not one address returned was new to this KB** —
`ChatTutor`, `Claw-ED`, `lineage-skill`, `llm-course`, `ML-For-Beginners`, `developer-roadmap`, the
general-purpose tier (`OpenClaw`, Hermes, Agent Zero, OpenHands, LangGraph, CrewAI) and `DeepTutor`
itself are all held, each already with its disposition recorded. Counts and dispositions:
[`../repos/trending.md`](../repos/trending.md) `p494`.

🟢 **Third consecutive pass with no promotion from discovery.** `p493` found five MIT addresses, all
below this shelf's star floor; `p494` found none at all. 🔵 **Read it as supply, not fatigue:** the
star-ordered education-agent surface is exhausted at this shelf's floor, which is the same conclusion
`p493` reached from the opposite direction. **The `595★ → 41,700★` cliff recorded in the gaps above
is therefore not an artefact of one pass's search — it has now survived three.**

### 🔵 A standing instruction in this file can only be discharged by a human

`p492` recorded `DeepTutor`'s design paper (`arXiv:2604.26962`) as an upstream-asserted lead with
*"do not cite the abstract to a client until someone has opened it."* Same for
`pedagogy-benchmark`'s `arXiv:2506.18710` behind the evaluation-instruments section above.

🔴 **Neither can be discharged from this session, on any pass.** Probed this pass:
`arxiv.org:443 — connect_rejected` (`curl` exit 56, `http=000`, three URLs). **That is this
session's egress proxy refusing the host — an allowlist decision, not a DNS failure and not
transient**, the same class of diagnosis `p492` landed for the GitHub `403`. 🔵 **Stop re-probing it,
and move both reads out of the pass backlog into a named human deliverable**, alongside the EUR-Lex
and Decision 33 primary reads named in [`../intel/market.md`](../intel/market.md) `p494`.


## 🆕 `p495` — `2026-10-28` — the advisory re-read `p494` ordered, and `v1.16.0` turns out to be a **security floor**

🔵 **`p494` closed with a standing instruction: _"re-read the advisories first, before any discovery
query."_ It was run first, and it was the right order** — the discovery queries again returned
nothing promotable (below), while the advisory read changed what this file tells an engineer to
deploy.

### 🟢 The count holds — and everything the KB did **not** have is the operational part

`p492` recorded four advisory IDs at `v1.16.0`. 🟢 **Re-read at the new SHA, the count is still
four** — so the number `p494` flagged as "not allowed to age" has aged correctly. 🔴 **But the four
IDs were all this KB held.** Severities, CVSS, affected ranges and patched versions were never read,
and they are the fields that decide a deployment:

| advisory | severity | affected | patched | what it is |
|---|---|---|---|---|
| `GHSA-hmr8-mvr2-mvw5` | 🔴 **High** | `≤ 1.12.0`, and `1.13.0`–`1.15.0` | **`1.13.0`** *(write allowlist + message previews)* then **`1.16.0`** *(`read_course_file` contents marked untrusted)* | A course member hides instructions in Canvas content that the instructor's assistant reads → course-data disclosure or **unauthorised grade change** |
| `GHSA-7pp5-29mw-9jq3` | 🔴 **High**, CVSS **7.8** `AV:L/AC:L/PR:L/UI:N/C:H/I:H/A:H` | `< 1.16.0` | **`1.16.0`** | `execute_typescript` ran caller-supplied TypeScript under `npx tsx` without blocking `child_process` → **OS command execution on the server** |
| `GHSA-7mj9-4mcg-hvhv` | 🟡 Moderate | — | — | Canvas **bearer token** sent to a URL chosen by the file-storage host on upload confirmation, and to off-origin file URLs on download |
| `GHSA-qf6c-jv93-38gv` | 🔵 Low | — | — | On Windows, downloaded course files are not owner-only — `os.chmod(0o600)` has no effect on NTFS |

All four were published **`2026-10-25`** and are listed on the repository's
[security advisories index](https://github.com/vishalsachdev/canvas-mcp/security/advisories)
(linked once, in prose: the advisory IDs above are deliberately **not** per-row links, because
four rows carrying the same repository address is what `gate-identity` exists to catch — and it
caught this table on its first run). 🟢 **Every one of them is patched at `v1.16.0`.**

### 🔴 Three consequences this file now carries

🟢 **1. `p494`'s pinning advice was right, and for a stronger reason than it gave.** `p494` said to
pin the release tag because branch HEAD drifts twice a day. 🔴 **The real reason is that anything
below `1.16.0` carries two High advisories, one of them remote-ish prompt injection that can change
grades.** `v1.16.0` = **`b3f06c76e43569f10f8f11833b4eb4ba2ee478ba`**, and `git ls-remote --tags`
confirms **no `v1.17.0` exists** — so `1.16.0` is simultaneously the newest release and the minimum
safe one, and HEAD (`47394125364b`) is **unreleased code sitting above it**. Pinning HEAD here means
shipping a client unreviewed commits *and* losing the ability to say which advisories are closed.

🔴 **2. A runtime prerequisite nobody had recorded: Node.js ≥ 22.18.** The `1.16.0` sandbox fix works
by running local code under **Node's permission model** (which blocks child processes, worker
threads, native addons, `process.binding` and file writes). That model requires **Node 22.18 or
later**. 🔴 **Deploy `v1.16.0` on an older Node and the advisory is not actually closed** — the
version string says patched and the mechanism is absent. This is now a hard line item in
[`../compose/patterns.md`](../compose/patterns.md) `P490-1` / `P495-1`.

🔴 **3. The advisory itself names residual risk as unfixed, and it is the risk that matters here.**
Quoting the `1.16.0` advisory: outbound network blocking in local mode is **best-effort**, and
**executed code can still access the caller's Canvas token**. 🔵 So "upgrade to `1.16.0`" is not a
complete answer for an engagement: on a Canvas tenant holding real student records, the
defensible posture is to **disable `execute_typescript` outright** and run the server with a
**scoped, short-lived Canvas token**, because the patch narrows the sandbox and does **not** take
the token out of its reach.

### 🟢 Pins: five of five stable, and the volatile one has stopped moving

| repo | KB pin | `p495` `git ls-remote` | verdict |
|---|---|---|---|
| [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) | `a31d82624c27` | `a31d82624c27` | 🟢 **5th consecutive pass byte-stable** (`p490`–`p495`) |
| [`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp) | `47394125364b` | `47394125364b` | 🟢 **stable** — no third move. 🔵 `p494` inferred a ~2-moves-per-day rate from two moves in ~24h; **one quiet pass is enough to say that was a burst, not a cadence** |
| [`THU-MAIC/OpenMAIC`](https://github.com/THU-MAIC/OpenMAIC) | `70859b42e714` | `70859b42e714` | 🟢 stable |
| [`HugeCatLab/ChatTutor`](https://github.com/HugeCatLab/ChatTutor) | `7d9e9052bc5a` | `7d9e9052bc5a` | 🟢 stable |
| [`Open-TutorAi/open-tutor-ai-CE`](https://github.com/Open-TutorAi/open-tutor-ai-CE) | `196c547291da` | `196c547291da` | 🟢 stable — the permissive answer in its layer |

### 🔴 No promotions, and the discovery channel has now looped *twice over*

🔴 **Fourth consecutive pass with no promotable find.** `p494` reported the ranking queries returning
this KB's own contents. 🔴 **`p495` found something worse and more precise: the channel is now
returning *unlicensed reskins* of repos this KB already holds.**

[`anandpatikat/guru-latihan-dinamis`](https://github.com/anandpatikat/guru-latihan-dinamis) was the
**first address in four passes that `grep -ril` could not find anywhere in this repository** — 0
files. It exists (`d37980fb15b0`). It is an Indonesian *Kurikulum Merdeka* print-ready assessment
generator, which is squarely in this KB's APAC interest. 🔴 **And it has no licence at all** —
`LICENSE` and `LICENSE.md` both return `404` at HEAD, so it is all-rights-reserved and Globant
cannot build on it. 🔵 **Its own README tagline names its upstream: `- naufaldi/teacher-exam`** —
which this KB **already holds**, in [`../repos/trending.md`](../repos/trending.md), correctly tagged
MIT. 🟢 **This pass byte-pins that upstream for the first time: MIT, `1 071 B`, `sha1 25cb945a99ab`,
© 2026 Naufaldi Rafif, at `ed5bf6359413`.**

🔵 **The transferable rule, and it is a licence rule rather than a search rule: a reskin inherits no
grant.** A derivative with no `LICENSE` is unusable **even when its upstream is MIT**, because the
MIT grant covers the upstream's bytes and says nothing about the fork's additions. 🔴 **The failure
mode is specific and plausible: a search returns the shinier derivative, the upstream's MIT tag is
found by name-matching, and an engagement builds on a repository nobody is licensed to use.**
Record the derivative as excluded *with its upstream named*, which is what this row does.

### 🔵 A gap that is now a conclusion, not a backlog item

🔴 **`EUR-Lex is proxy-refused.`** Probed twice this pass
(`eur-lex.europa.eu/eli/reg/2026/1744/oj` and the `legal-content` URL):
`http=000, curl exit 56 — connect_rejected`. 🔵 **Identical signature to `arxiv.org`**, which `p494`
established is an egress-allowlist refusal rather than an outage. **So the EU Digital Omnibus
primary read — carried as an open action for more than ten passes — can never be discharged from
this session on any pass.** It belongs on the same named human deliverable as the two arXiv papers
and the Vietnam Decision 33 official text. See [`trending.md`](trending.md) `p495`.


## 🆕 `p496` — `2026-10-28` — the discovery drought **broke**, and the layer it broke in is the one with the worst licence hygiene in the sector

🔵 **Standing order honoured.** `p495` made *verification before discovery* this KB's order of work.
Verification ran first and came back clean (below); discovery ran second — and for the first time in
five passes it returned **addresses this repository has never held**. Full reads:
[`licence-and-stars.2026-10-28-p496.tsv`](../evidence/licence-and-stars.2026-10-28-p496.tsv).

### 🟢 Drift sweep — **ten of ten stable**, and the volatile pin is now quiet for a second pass

| repo | KB pin | `p496` `git ls-remote --symref` | verdict |
|---|---|---|---|
| [`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp) | `47394125364b` | `47394125364b`, `refs/heads/main` | 🟢 **stable, second consecutive quiet pass.** 🔴 Pin **`v1.16.0` = `b3f06c76e435`** anyway — the security floor in `p495` is unchanged |
| [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) | `a31d82624c27` | `a31d82624c27`, `refs/heads/main` | 🟢 **6th consecutive pass byte-stable** (`p490`–`p496`) |
| [`THU-MAIC/OpenMAIC`](https://github.com/THU-MAIC/OpenMAIC) | `70859b42e714` | `70859b42e714`, `refs/heads/main` | 🟢 stable |
| [`HugeCatLab/ChatTutor`](https://github.com/HugeCatLab/ChatTutor) | `7d9e9052bc5a` | `7d9e9052bc5a`, `refs/heads/main` | 🟢 stable (AGPL-3.0) |
| [`Open-TutorAi/open-tutor-ai-CE`](https://github.com/Open-TutorAi/open-tutor-ai-CE) | `196c547291da` | `196c547291da`, `refs/heads/main` | 🟢 stable |
| [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | `46a5d7d40082` | `46a5d7d40082`, **`refs/heads/19.0`** | 🟢 stable. 🔵 Default ref is a **version branch, not `main`** — the branch-name trap `repos/foundations.md` records, confirmed again |
| [`Selleo/mentingo`](https://github.com/Selleo/mentingo) | `e137ca47cbec` | `e137ca47cbec`, `refs/heads/main` | 🟢 stable |
| [`oppia/oppia`](https://github.com/oppia/oppia) | `bc73ecf9cf71` | `bc73ecf9cf71`, **`refs/heads/develop`** | 🟢 stable. 🔵 Second version of the branch-name trap: default ref is `develop` |
| [`AI-for-Education/pedagogy-benchmark`](https://github.com/AI-for-Education/pedagogy-benchmark) | `21a43a395ab4` | `21a43a395ab4`, `refs/heads/main` | 🟢 stable — the MIT evaluation instrument holds |
| [`naufaldi/teacher-exam`](https://github.com/naufaldi/teacher-exam) | `ed5bf6359413` | `ed5bf6359413`, `refs/heads/main` | 🟢 stable, **and used as this pass's probe control** — see below |

🔵 **The `canvas-mcp` rate question is now settled.** `p494` inferred ~2 moves/day from a burst;
`p495` saw one quiet pass; `p496` makes it **two**. **Branch HEAD is not inherently volatile here —
it had a bad week.** The release-tag pin stands anyway, because it is a *security* floor and not a
drift preference.

### 🔴 A defect in this pass's own reader — caught by a control row, recorded rather than quietly fixed

This pass's first licence sweep reported **`404` at every path for every repository probed**, which
reads as a dramatic ecosystem finding: *a whole layer with no grants.* 🔴 **It was a shell-quoting
bug in the probe** (the status code and the body length were being concatenated — `404000` — so no
path could ever match `200`).

🟢 **What caught it was a control row**, not a review of the code: the same probe was pointed at
[`naufaldi/teacher-exam`](https://github.com/naufaldi/teacher-exam), whose licence `p495` had already
byte-pinned at **MIT, 1 071 B, `sha1 25cb945a99ab`**. The control came back `404` too — which is
impossible — and the sweep was rebuilt. The corrected probe reproduces `p495`'s bytes **exactly**,
which is what licenses the rest of this pass's reads.

🔵 **The method rule, stated so it outlives this pass.** This KB already runs a *branch* control
(`README.md → 200` to prove the tree was reached). That control would **not** have caught this bug,
because it fails in the same direction as everything else. 🔴 **A probe run needs a control with a
known *positive* answer — a specific byte count the KB has already recorded — or a silent reader
failure is indistinguishable from an ecosystem finding.** Every row in this pass's TSV carries both:
a `README:200` branch control and a repository whose bytes were known in advance.

🔴 **Why this is more than housekeeping:** `p495`'s headline finding was an *unlicensed reskin*. A
false `NO-GRANT` is exactly the error that manufactures that finding. Had the control row been
omitted, this pass would have published "the special-education layer is entirely unlicensed" — and
three of the eight addresses below would have been libelled.

### 🆕 The special-education / IEP layer — eight addresses new to this repository

🟢 **Every one of these was absent from all 5,547 files in this repository** (`grep -rl`, including
`evidence/` and `compose/code/`), which is the first time since `p491` that discovery has produced
more than one such address. 🔵 **They did not come from the brief's ranking queries.** Those were run
and saturated again (below). These came from **function-shaped** queries — *IEP*, *accommodations*,
*rubric grading* — rather than keyword-and-star-ordered ones.

🔴 **The licence split is the finding, and it is the inverse of the sector's general picture: five of
eight carry no grant at all.**

| repo | ★ | grant at SHA | disposition |
|---|---|---|---|
| [`jscott5811/IEP-and-Section-504-Plans-Skill`](https://github.com/jscott5811/IEP-and-Section-504-Plans-Skill) | 0 | 🟢 **MIT**, 1 068 B, `sha1 e8b3ee2c48a2` (`cd3a9018681f`) | 🟢 **Build on.** The **US federal baseline** this shelf lacked: IDEA **34 CFR Part 300** and **Section 504** of the Rehabilitation Act, with ED/OCR/OSERS sources cited by document and date. 2 commits. Same *pinned knowledge pack* architecture this KB already praises in `robotros/California-IEP-AI-project-kit` — but federal where that one is Californian |
| [`rtwergrfh-cmyk/iep`](https://github.com/rtwergrfh-cmyk/iep) | 0 | 🟢 **MIT**, 1 080 B, `sha1 fb30401f6782` (`264786ddb518`) | 🟢 **Build on, and read it for its posture.** "IEP Glance" renders an IEP PDF into one-page plain-language sheets per adult (teacher, para, substitute, family). 🟢 **No server and no AI service — entirely in-browser, rules-only.** Prints EN/ES. 🔵 **Mixed grant, stated honestly upstream:** project code MIT, `pdf.js` Apache-2.0, Nunito **SIL OFL 1.1** — the font licence is the one a compliance review will ask about. 1 commit |
| [`SahilC/AutomaticEssayGrading`](https://github.com/SahilC/AutomaticEssayGrading) | 13 | 🟢 **MIT**, 1 074 B, `sha1 cd4c5b7304aa` (`8bf6dc6b678b`) | 🟡 **Baseline, not a build target.** SVM / decision-tree / random-forest / LSTM essay scoring, 55 commits, **no LLM**. Worth one sentence to a client who assumes rubric scoring requires a model: this is the pre-LLM comparator |
| [`SudhanvaJ-bit/project-samarth`](https://github.com/SudhanvaJ-bit/project-samarth) | 1 | 🔴 **no licence at 6 paths** (`README.md → 200`), `d628b919449a` | 🔵 **Reference design — read it, do not depend on it.** See below; it is the most instructive thing in this haul |
| [`kennedyraju55/essay-grader`](https://github.com/kennedyraju55/essay-grader) | — | 🔴 **no licence at 6 paths** (`README.md → 200`), `504ddefc863a`, **`refs/heads/master`** | 🔴 **Excluded, and it is a misgrant.** The search channel asserted *"MIT-licensed"*; the payload has **no grant at any of six filenames**. Local-Gemma-via-Ollama rubric grading — the offline shape `T9` wants — and Globant **cannot use it** |
| [`avivkatz1/easy-iep`](https://github.com/avivkatz1/easy-iep) | — | 🔴 **no licence at 6 paths** (`README.md → 200`), `ec0d4f039b0a` | 🔴 Excluded. IEP-meeting preparation framed around **FERPA** and Illinois **SOPPA** — 🔵 the first appearance of SOPPA anywhere on these shelves, and it arrives unusable |
| [`victor-lubn/Special-Education-Planning`](https://github.com/victor-lubn/Special-Education-Planning) | — | 🔴 **no licence at 6 paths** (`README.md → 200`), `7baa4e1a9ecd` | 🔴 Excluded. Intake → SMART goals → accommodations → human review; avoids medical diagnosis |
| [`marckurniawan/essay-scoring-project`](https://github.com/marckurniawan/essay-scoring-project) | — | 🔴 **no licence at 6 paths** (`README.md → 200`), `80d6cfceb75e` | 🔴 Excluded. Gemini + teacher rubrics |

🔴 **No promotions to the permissive shelf table above, and the reason is the star floor, not the
grant.** The three MIT finds sit at **0, 0 and 13★**. They go on this file as a layer, not as shelf
rows, which keeps the `595★ → 41,700★` cliff recorded in the gaps section honest.

### 🔵 `project-samarth` — a reference design worth more than its licence lets you use

🔴 **It has no grant, so it is a read and nothing else.** What makes it worth reading is one
architectural decision, and it is the special-education analogue of the rule `P492-1` already builds
on (*"the model never does the arithmetic"*):

> A rule-based baseline of what the **RPwD Act 2016** requires for each disability category is merged
> with the model's suggestions, and **the model can add to the list; it cannot remove from it.**

🟢 **That is a monotonic compliance floor enforced in code rather than asked for in a prompt** —
generalised into a recipe as [`P496-1`](../compose/patterns.md). 🔵 Stack is LangGraph + Gemini 3.x
Flash + `gemini-embedding-2` + ChromaDB + FastAPI (Python 3.13) + React 19; NASET's 11-section IEP
format adapted to Indian law; field-level tracking of whether each edit was AI- or human-authored,
with the original model output preserved. 32 commits.

🔴 **And its own evaluation is the most useful thing on the page, because it is a declared failure:**
across **15 synthetic profiles, all 15 runs returned `Partial`** — its compliance agent has **never
once returned `compliant`**. Upstream also states drafts are stored **unencrypted** and that real
student data must not be used, and that the pipeline has never been compared against single-prompt
generation or against IEPs written by special educators. 🟢 **A compliance gate that never passes is
not a conservative gate, it is an uncalibrated one**, and `P496-1` is built to avoid exactly that.

### 🔴 The brief's ranking queries — run, and saturated for a **fifth** consecutive pass

Both global ranking legs were run. 🔴 **Not one promotable education agent.** What they return now is
a **category error rather than a repeat**, and naming the cause retires the complaint:

| address returned | ★ | grant at SHA | why it is not an education agent |
|---|---|---|---|
| [`rohitg00/ai-engineering-from-scratch`](https://github.com/rohitg00/ai-engineering-from-scratch) | **75,238** *(🟢 `p510`, API — replaces a ROUNDED cell of 74,800 that was never API-read)* | 🟢 MIT, 1 070 B, `sha1 5f16474bdbd6` (`3f9715c62a3b`) | "Learn AI Engineering" — **542 lessons, 20 phases**. A curriculum for engineers |
| [`pguso/agents-from-scratch`](https://github.com/pguso/agents-from-scratch) | **1,064** *(🟢 `p510`, API — replaces a ROUNDED cell of 1,100 that OVERSTATED by 36; the count went DOWN)* | 🟢 MIT, 1 091 B, `sha1 543c922b12f8` (`da3f9df28a9c`) | 12 lessons on building agents with a local LLM. Upstream says it plainly: **"Educational, not production."** 23 commits |
| [`h9-tect/AI-Roadmaps`](https://github.com/h9-tect/AI-Roadmaps) | — | 🔴 **no licence at 5 paths** (`19c63bdb7c86`) | A roadmap list. Unlicensed **and** out of category |

🟢 **The cause is a taxonomy collision, and it is in GitHub's own metadata.** The topic `ai-education`
and the keyword *"education"* in a star-ordered query select for **teaching AI to humans**, not
**applying AI to teaching**. Those two categories are disjoint, and the first is vastly larger and
more starred. 🔴 **That is why five passes of ranking queries returned curricula** — and why this
file already had to write exclusion rows for `microsoft/ai-agents-for-beginners` (**78,061** *(🟢 `p511`, API)*) and
`labmlai/annotated_deep_learning_paper_implementations` (67,600★) one repository at a time.

🔵 **Standing instruction for the next pass, and it is a change of query shape rather than more
effort:** drop *"education"* + star-ordering as a discovery leg. **Query the function** — `IEP`,
`accommodations`, `rubric`, `gradebook`, `attendance`, `SIS`, `proctoring`, `enrolment`. That is what
produced all eight new addresses above after five passes of nothing. 🟡 **Stated against itself:** the
licensed *head* of the special-education layer was already swept (`robotros`, `67tallchris/iep-builder`,
`dougdevitre/access-to-education`, all MIT, all held). This pass reached the **tail** of that same
layer, and the tail is where the grants stop.

### 🔴 A correction, and a drift, on the repository `P496-1` now depends on

[`robotros/California-IEP-AI-project-kit`](https://github.com/robotros/California-IEP-AI-project-kit)
is cited in [`compose/patterns.md`](../compose/patterns.md) `P496-1` as a state-overlay knowledge
pack, so its pin and its bytes were re-read this pass rather than carried.

| field | this KB's recorded value | `p496` read | verdict |
|---|---|---|---|
| HEAD | `ff1ae0ce30e7` | 🔴 **`33ad4d06f19b`** | **drifted** |
| `LICENSE` bytes @ `ff1ae0ce30e7` | **1 064 B**, `sha1 2524a8e74f10` | 🔴 **1 065 B**, `sha1 35b8efcd34d0` | **does not reproduce** |
| `LICENSE` bytes @ `33ad4d06f19b` | — | **1 065 B**, `sha1 35b8efcd34d0` | 🟢 **byte-identical to the old SHA — the drift is code-only** |
| licence family | MIT | 🟢 **MIT** (`MIT License` title line) | 🟢 unaffected |

🔴 **The byte count and `sha1` this KB published for this repository do not reproduce at the SHA this
KB itself cites.** Re-read three times, identical each time. 🟢 **And this pass's reader is
independently validated in two directions**: `naufaldi/teacher-exam` reproduces `p495`'s
**1 071 B / `sha1 25cb945a99ab`** exactly, and `braiinz94/braiinz-education` reproduces this KB's
**11 356 B** exactly. 🔵 **So the defect is in the recorded figure, not in the reading of it** — a
transcription error rather than an upstream change, since the payload is byte-identical across both
SHAs.

🟢 **Nothing commercial turns on it** — the grant is MIT either way, which is what `P496-1` relies
on. 🔵 **What it does establish is that this KB's byte-level records are not self-verifying**, which
is `T14` with a measurement attached: of the four recorded figures re-read this pass, **three
reproduced exactly and one did not**. 🔴 **Re-read a pinned byte count before building a
recommendation on it**, which is what this pass did and why the error surfaced at all.

## 🆕 `p497` — `2026-10-28` — a verification channel this file declares dead is **alive**, and the shelf gains its first **admissions-layer** asset

Full reads: [`licence-and-stars.2026-10-28-p497.tsv`](../evidence/licence-and-stars.2026-10-28-p497.tsv).
Census of 59 ranked addresses: [`saturation-census.2026-10-28-p497.tsv`](../evidence/saturation-census.2026-10-28-p497.tsv).
Narrative: [`trending.md`](trending.md) `p497`. Recipe: [`compose/patterns.md`](../compose/patterns.md) `P497-1`.

### 🟢 Correction to this file's own verification table

The table under *"How every cell here was verified"* above records:

> | stars for arbitrary repos | `api.github.com` | **403, per-repository authorisation only** |

🔴 **That row needs splitting, and the half that changed is the half this KB said mattered most.**
🔵 **Credit where it is due: `p162` already got this right** and published it as `T148` — the `403`
is *per-repository*, metadata is recoverable one `add_repo` at a time, **but
`/search/repositories` is "NOT repository-scoped, so NOT recoverable by attaching"**, so
*"ranking, star-ordered discovery and new-entrant detection"* were declared unrecoverable —
*"that limb of `T137` stands and is the one that matters for finding agents nobody has told us
about."*

🟢 **It is that exact limb which is now open.** The authenticated **search** API answers through
this session's **MCP** channel for **arbitrary** repositories — star-ordered, topic-filtered,
returning `stargazers_count`, `license.spdx_id`, `default_branch`, `pushed_at` and `topics` for
repositories this session has never attached. 🔵 **`T148` is not refuted; it is superseded on one
limb by a channel it did not test.** `p162` tested raw HTTP to `api.github.com` and was correct
about it — **re-probed this pass, direct `api.github.com` is still `403`.** The row should read:
**direct `api.github.com` → `403` (per-repository, as `T148` says); MCP-mediated search API →
works, including star-ordered ranking over arbitrary repositories.**

🔵 **Unchanged, and re-probed this pass:** `curl -sI https://github.com/<repo>` is still proxy
`403`. 🔵 **Also unchanged, and this is the important half:** **licence family is still read from
`raw.githubusercontent.com` at a pinned SHA, never from the API.** The API's `license` field and
`topics` array are upstream **self-assertions** — `oh-my-paper` literally carries a `mit-license`
topic — and a self-asserted grant is not a read. 🟢 The channel is calibrated: `DeepTutor` returns
**46,444★** against the **45,900** this file records from a `p492` page read, six days apart, same
direction.

### 🔴 No promotions, and this time the reason is measured rather than asserted

**Zero rows added to the permissive shelf.** Three addresses new to this repository were found and
**all three are below this shelf's floor** (5★, 1★, 2★); they are recorded under *reference designs*
below, the disposition `p492` established.

🔴 **What is new is that the saturation is now a number.** Five ranked topic axes, 59 addresses,
**56 already on these shelves — 94.9%**. The two axes that *are* this sector —
`topic:ai-tutor` and `topic:ai-education`, at every star level down to 100 — returned **zero**
addresses this KB does not hold. 🔵 **So the standing "discovery channel has looped" note in `p494`
and `p495` is upgraded from an observation to a measurement:** ranked education-AI supply above
~40★ is substantially enumerated here, and `p496`'s reading that the drought was a query-shape
artefact is only half right. The *mechanism* half holds — all three of this pass's finds came from
function-shaped administrative queries and none from a ranking leg.

### 🆕 Reference designs added this pass

🟢 **[`ASUCICREPO/Admissions-AI-Agent`](https://github.com/ASUCICREPO/Admissions-AI-Agent) — MIT,
1 123 B, `sha1 8a0aae668604`, SHA `fcbbbb2fe19f`, 5★.** Arizona State University's AI Cloud
Innovation Centre (copyright line: *"ASU Artificial Intelligence Cloud Innovation Centre, powered by
AWS"*). Admissions-counsellor agent: understands student needs, answers questions, hands off to
human advisers. AWS Bedrock AgentCore + Next.js, Salesforce CRM, WhatsApp via Twilio.

🔴 **This closes a gap this file did not know it had.** `admissions` appears in **59** markdown files
in this KB — all of it regulatory prose, because admissions is an **EU AI Act Annex III point 3**
high-risk function. **There was no buildable admissions asset anywhere on these shelves.** This KB
could state the law and name nothing to implement against it. 🟢 At 5★ it stays off the shelf, but a
named university innovation centre's architecture is a credible thing to read and re-implement, and
it is the only one held in this layer. 🔴 **Its stack is AWS-managed** (Bedrock AgentCore), so the
MIT grant covers the orchestration code, **not** a portable runtime — read it for the agent design
and the adviser-handoff boundary, not as a deployable.

🟢 **[`TaiRuiQu/oh-my-paper`](https://github.com/TaiRuiQu/oh-my-paper) — MIT, 1 094 B,
`sha1 f298820afe90`, SHA `96c5e24c0216`, `refs/heads/v2`, 1★.** K-12 platform: exam-paper
recognition, question bank and paper assembly, homework and exams, **AI-assisted marking**,
wrong-answer review, learning analytics, Docker self-host. APAC-origin, Chinese-language UI. 🔵 Sits
in the Annex III **grading** tier. At 1★ this is a watch item, not a dependency.

🔴 **[`wongcyrus/gemini-handwriting-grader`](https://github.com/wongcyrus/gemini-handwriting-grader)
— NO GRANT**, `404` at all five probed paths, SHA `2849fed23a6f`, 2★. Handwriting grading via Gemini
OCR into Excel/Word/PDF reports. `README.md → 200` at the same SHA proves the tree was reached, so
the absence is real. **Do not build on it.** Recorded so it stops resurfacing.

### 🔵 A caution against reading a licence trend off eleven addresses

`p496` found **five of eight** new addresses unlicensed and concluded the highest-legal-exposure
layer in education has the worst licence hygiene in the sector. This pass points the other way:
**both finds inside the Annex III designated layer are MIT, and the unlicensed one is a 2★ script.**

🔴 **Two passes and eleven addresses support neither generalisation.** Both are true statements about
their own samples. **Do not carry either to a client as a characteristic of the sector**; what is
safe to say is that licence hygiene in this sector's long tail is unpredictable per-repository, which
is why every row in this file is read from bytes.

### 🔴 A defect in this pass's own absence gate, recorded rather than quietly fixed

This KB's absence gate — `grep -rl <address>` across every file — was re-run **after** this pass had
written its evidence TSVs and returned **`NEW=0`**: all three finds reported as already present,
because the pass had just written them into its own evidence.

🔴 **The rule.** The gate is valid only against the tree **as the pass found it**: run it before
writing any artefact, or exclude the pass's own files. The census linked above does the latter, and
the exclusion is visible in its column header (`kb_files_mentioning_excl_p497`). 🔵 **It belongs
beside `p496`'s reader defect** — both are instruments returning the answer the pass is looking for.
`p496`'s false `404` manufactured an unlicensed layer; this one manufactures a drought. 🟢 Neither
would be caught by a control that can only fail in the same direction as the bug.

### 🔴 The branch-name trap is five variants, and one is a 647★ production system

`git ls-remote --symref` this pass added **`refs/heads/mobile`**
([`francoisjacquet/rosariosis`](https://github.com/francoisjacquet/rosariosis), **647★**, a live SIS
with attendance, gradebook and report cards), **`refs/heads/v2`** (`oh-my-paper`) and
**`refs/heads/PreProduction`** (`AgnellusX1/GodsEye`) to `p496`'s `19.0` and `develop`.

🔴 **A probe that hard-codes `main` now misreads five repositories on these shelves as nonexistent.**
`mobile` and `PreProduction` are the dangerous pair — they read as feature branches, so a human
reviewing the probe output would not flag them either. Census:
[`branch-ref-census.2026-10-28-p497.tsv`](../evidence/branch-ref-census.2026-10-28-p497.tsv).

### 🟢 Pins: ten of ten stable

Every SHA identical to `p496`. `DeepTutor` byte-stable across **seven** passes (`p490`–`p497`).
🟢 `canvas-mcp` quiet for a **third** consecutive pass, which retires `p494`'s "~2 moves/day"
reading. 🔴 **`v1.16.0` = `b3f06c76e435` remains the pin regardless — it is a security floor, and the
sandbox fix requires Node.js ≥ 22.18.** Sweep:
[`drift-sweep.2026-10-28-p497.tsv`](../evidence/drift-sweep.2026-10-28-p497.tsv).

---

## 🆕 `p498` — `2026-10-28` — four permissive additions, one licence cell corrected, and a §6 clause to read aloud

🔵 Every grant below was read as a **payload at a pinned commit**, not from a repository badge or a
search-result `license` field. Bytes and blob SHAs are given so the next pass can re-grade without
re-reading. Full enumeration: [`evidence/grant-paths.2026-10-28-p498.tsv`](../evidence/grant-paths.2026-10-28-p498.tsv).

### 🟢 Permissive — added to the shelf this pass

| Name | Repo | Licence | Description | ★ |
|---|---|---|---|---|
| book-to-skill | [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill) | **MIT** (1 068 B · blob `b000bdffeaa2` at `LICENSE.md`) | Turns a technical-book PDF into an agent skill — chunking, structuring and indexing a long source into a reference an agent can work from. Python. Default ref 🔴 **`master`**. | 36 339 |
| Papermorph | [DozenTwelve/Papermorph](https://github.com/DozenTwelve/Papermorph) | **MIT** (1 069 B · blob `f461737043ac`) | Books → animated, narrated, interactive web lessons. 🟢 **Emits SCORM**, so output lands inside an existing LMS instead of beside it. Vendored MathJax carries its own Apache-2.0. | 982 |
| claudemy | [assafkip/claudemy](https://github.com/assafkip/claudemy) | **MIT** (1 069 B · blob `ebe94bd95589`) | Topic → a sequenced course of ~2-minute audio lessons **with cited sources**. The citation requirement is the part worth copying. | 492 |
| get-it | [beltromatti/get-it](https://github.com/beltromatti/get-it) | 🟡 **Apache-2.0 with §6 altered** (11 359 B · blob `29492aec7faa`) | Source material → knowledge graph + flashcards + spaced repetition on a Feynman-technique loop. 🇮🇹 Built at GDG AI Hack Milan 2026. **Read the §6 caveat below before quoting the licence to a client.** | 1 138 |

### 🟡 Copyleft — usable, with the obligation named

| Name | Repo | Licence | Description | ★ |
|---|---|---|---|---|
| frametell | [sitor-ai/frametell](https://github.com/sitor-ai/frametell) | **AGPL-3.0** (34 523 B · blob `be3f7b28e564`), §13 *Remote Network Interaction* present | Explainer-video director agent, **local-first and model-agnostic** — which makes it the strongest fit on these shelves for an air-gapped or sovereign deployment, and the worst fit for a hosted multi-tenant product. | 423 |

🔴 **§13 means hosting it for a client triggers the source-offer to that client's users.** Run it as
a local authoring tool, or accept the obligation deliberately. The licence payload is **clean** —
same bytes as `classroomio`'s at a different blob, same operative body (see
[`agents/trending.md`](trending.md) `p498`).

### 🔴 Refused this pass — and both are content assets

| Name | Repo | Licence | Why refused |
|---|---|---|---|
| cn-math-taxonomy | [xiaoyang111222/cn-math-taxonomy](https://github.com/xiaoyang111222/cn-math-taxonomy) | 🔴 **CC BY-NC 4.0** (19 347 B · blob `fe463e0f7888`) | **Non-commercial.** Painful, because the asset is excellent: a 🇨🇳 K-12 maths / English / junior-physics knowledge graph with **1 644 knowledge points, 2 403 prerequisite edges and 6 723 items**, curriculum-aligned, shipping adaptive prerequisite diagnostics. **Globant cannot ship it into a paid engagement.** Cite it as prior art; build the graph. |
| PageLM | [CaviraOSS/PageLM](https://github.com/CaviraOSS/PageLM) | 🔴 **bespoke "PageLM Community License"** (8 563 B · blob `6759e05bb55c`) | **Not an OSI licence**, and four separate non-commercial clauses in the payload. A NotebookLM-shaped study platform — material in, quizzes/flashcards/notes/podcasts out. Read it as a product spec, not a dependency. |

🔵 **This is the sector's split, and it reproduced on a population disjoint from the one `p479`
measured it on:** the code is permissive, the curriculum and content are not. Of the eight addresses
graded this pass, **the two refused are exactly the two content assets.** Plan for building the
knowledge model, not acquiring it.

### 🔴 The `get-it` §6 caveat — five words deleted from a live Apache-2.0 grant

🔴 `beltromatti/get-it`'s §6 *Trademarks* reads *"except as required for **describing the origin of
the Work**…"*. The canonical clause reads *"except as required for **reasonable and customary use
in** describing the origin of the Work…"*. 🟢 Graded against two independent canonical payloads
(`menthorlabs/menthor` 11 337 B; `huggingface/smolagents` 11 357 B), both of which carry the five
words.

🔵 **What to do:** the row stays on the shelf — this narrows a trademark safe harbour, it does not
touch the patent or copyright grants. 🔴 **But if your deliverable names the upstream project in
client-facing material, that is the clause you are relying on**, and it has been edited. Raise it in
the licence review, in one sentence, and move on.

🔴 **And note how nearly it was missed:** `get-it`'s payload is **22 bytes longer** than the canonical
one it was compared against, because its appendix copyright line is longer than `menthor`'s. A
size-based check would have cleared it.

### 🟢 `Gap 488-X` — the `LICENSE`-is-not-the-grant class, measured

🟢 All **76** carried rows re-probed with a full tree enumeration. **Nine** carry two root-level
grant files; **one of 76 (1.3%)** actually splits its grant:

🔴 [`microsoft/autogen`](https://github.com/microsoft/autogen) — `LICENSE` is **CC BY 4.0**
(18 650 B · blob `2f244ac81403`); the code grant is **`LICENSE-CODE`, MIT** (1 141 B · blob
`9e841e7a26e4`). 🔴 **A first-hit `LICENSE` probe on this row returns a content licence, with no
patent grant, for a code repository.** Six of the other eight are `NOTICE` files (Apache §4(d)
attribution, not grants); [`Selleo/mentingo`](https://github.com/Selleo/mentingo)'s second path is a
**0-byte file**; [`chamilo/chamilo-lms`](https://github.com/chamilo/chamilo-lms)'s is a copyright
roll naming **eight holders across six countries** — not a grant, but the CLA conversation written
down.

🔵 **Rule:** enumerate every grant path, then classify by name before counting. Counting paths
overstates this class **9×**.

---

## 🆕 `p499` — `2026-10-28` — five agent rows promoted, each operatively verified

**Why these appear now.** `p499` measured this base's `topic:edtech` 50–400★ band and found that
**41 of 52 rows already sat in its own append-only narratives while only 1 had ever reached a
curated shelf** (`Gap 499-A`; the measurement is in
[`agents/trending.md`](trending.md) `p499`). Discovery was never the constraint — promotion was.
These five are the agent-layer half of the repair, read from bytes at the pinned SHA and graded on
the operative-span instrument introduced this pass
([`compose/code/p499-canonical-set/`](../compose/code/p499-canonical-set/)).

| Agent | Repo | Licence (read from bytes) | ★ | Operative verdict | What it does |
|---|---|---|---|---|---|
| **Bloom** | [`Li-Evan/Bloom`](https://github.com/Li-Evan/Bloom) | 🟢 **MIT**, 1 069 B `68788b5e7d34` | 294 | 🟢 **IDENTICAL** | Private AI tutor that adapts to how a learner actually learns and sequences the next lesson. Self-describes against **Bloom's 2-sigma** result. Topics declare `ai-agent` + `agent-skills`, so it is an agent proper, not a wrapper. |
| **OpenTutor** | [`zijinz456/OpenTutor`](https://github.com/zijinz456/OpenTutor) | 🟢 **MIT**, 1 068 B `dbaab74ffe76` | 154 | 🟢 **IDENTICAL** | Block-based adaptive-learning workspace that **runs locally** — upload any material, get a course. FastAPI. 🟢 **The only locally-running adaptive tutor on these shelves**, which matters for every data-residency conversation. |
| **OpenPronounce** | [`Halleck45/OpenPronounce`](https://github.com/Halleck45/OpenPronounce) | 🟢 **MIT**, 1 113 B `74bc17ea406e` | 166 | 🟡 DEVIANT (+2: the title words `The`/`MIT`) | Phoneme-level English pronunciation assessment, **Wav2Vec2 + DTW**, self-hosted. 🟢 A named model and a named algorithm, not a prompt — the most concretely specified AI component added this pass. 🔵 Last push **2026-08-15**. |
| **Mnemo** | [`onemnemo/mnemo`](https://github.com/onemnemo/mnemo) | 🟢 **Apache-2.0**, 11 326 B `6dce04a20fbc` | 122 | 🟢 **IDENTICAL** | Study / spaced-repetition application, Photino X + .NET 10. 🔵 The **permissive** counterpart to `anki` (AGPL-3.0), whose code these shelves have had to treat as algorithm-reference-only. |
| **AI flashcards** | [`kirill-markin/flashcards-open-source-app`](https://github.com/kirill-markin/flashcards-open-source-app) | 🟢 **MIT**, 1 070 B `98663982f0ae` | 102 | 🟢 **IDENTICAL** | AI-generated flashcards on **FSRS** scheduling; iOS, macOS, Android and web. Active **2026-10-28**. |

🟢 **All five are permissive and all five can ship in a closed hosted derivative.** Four of the
five were last pushed within the past eight days.

🔵 **`Mnemo` + the flashcards app together change a standing recommendation.** `verticals/solutions.md`
has carried `Anki` (AGPL-3.0) as "use as the algorithm reference even where the code can't ship".
There are now **two permissive spaced-repetition implementations** — one Apache-2.0, one MIT with
FSRS — so the AGPL constraint on that layer is no longer binding.

🔴 **Not promoted, and why.** [`RandMelville/claude-war-room`](https://github.com/RandMelville/claude-war-room)
(62★, MIT) carries the `edtech` topic and is **not an education project** — it is a five-agent
orchestrator written in Portuguese. 🔵 **The topic axis itself admits false members**, so a topic
count is not an education-supply count; this is the same popularity-filter problem as `Gap 488-E`,
on a different axis.

---

## 🆕 `p500` — `2026-10-28` — three MIT agents promoted off the trending backlog, and the grader that graded them is corrected

**Pass `p500` — reads of 2026-10-28.** This section **extends** the file; nothing above is
rewritten. Every licence below was fetched from `raw.githubusercontent.com` at a **pinned commit
SHA** resolved with `git ls-remote` (`api.github.com` is 403 under this session's network policy —
see [`gate-discrimination.2026-10-28-p500.tsv`](../evidence/gate-discrimination.2026-10-28-p500.tsv)).
Reads: [`pinned-sha-rows.2026-10-28-p500.tsv`](../evidence/pinned-sha-rows.2026-10-28-p500.tsv),
[`promo-licence-bytes.2026-10-28-p500.tsv`](../evidence/promo-licence-bytes.2026-10-28-p500.tsv).
Narrative: [`agents/trending.md`](trending.md) `p500`.

### 🟢 Registered — three agents that this base had already read and never shelved

| Agent | Repo | Licence @ pinned SHA | ★ | Operative body | What it is |
|---|---|---|---|---|---|
| **Claw-ED** | [`SirhanMacx/Claw-ED`](https://github.com/SirhanMacx/Claw-ED) | 🟢 **MIT**, 1 078 B `18f2e223cdd1` | 63 | 🟢 **IDENTICAL** | Local-first AI teaching assistant: editable lesson drafts, student materials and slides from the teacher's **own** curriculum and chosen model. Python 3.11+, self-described teacher-reviewed beta. 🟢 The local-first posture is the one that survives a district AI policy — see `T1`/`T13`. |
| **EduAgent** | [`Zenglian990/AI_Tutor_Release`](https://github.com/Zenglian990/AI_Tutor_Release) | 🟢 **MIT**, 1 068 B `2987df2be268` | 74 | 🟢 **IDENTICAL** | Open-source **RAG** tutor built for Chinese K-9 (repo says grades 1–9; its README says 1–12 — 🔴 unreconciled). The clearest permissive RAG-tutor reference implementation on an APAC curriculum. |
| **MindTrain** | [`shigella520/MindTrain`](https://github.com/shigella520/MindTrain) | 🟢 **MIT**, 1 067 B `7115c484c77e` | 128 | 🟢 **IDENTICAL** | AI knowledge-training platform with **pluggable schedulers** — the spaced-repetition/sequencing layer as a swappable component rather than a hardcoded policy. |

🔴 **Why this is worth noting rather than just doing:** `Claw-ED` is mentioned **39** times across
this KB's two trending files and `AI_Tutor_Release` **27**, and neither had ever reached a shelf.
That is the promotion gap `Gap 499-A` described, in its cleanest form.

### 🟢 A second licensed evaluation instrument — with a trap in the data

The standing claim that education-AI evaluation instruments are unlicensed was already falsified
by `p493` ([`AI-for-Education/pedagogy-benchmark`](https://github.com/AI-for-Education/pedagogy-benchmark),
MIT). A second now exists, and it is **not** shelved as a clean row:

| Instrument | Repo | Code | Content / corpora | ★ |
|---|---|---|---|---|
| **Learning Commons Evaluators** | [`learning-commons-org/evaluators`](https://github.com/learning-commons-org/evaluators) | 🟢 **MIT**, 1 615 B `b9d47891c1b8` | 🔴 prompts **CC BY 4.0**; annotated **CLEAR** + **PERSUADE 2.0** corpora **CC BY-NC-SA 4.0 — non-commercial** | 87 |

Evaluates LLM output against research-backed educational rubrics, in families — **Text
Complexity**, **Feedback**, **Academic Standards Alignment**, **Durable Skills** — with Python and
TypeScript SDKs and a web playground. 🟢 It closes `p493`'s open item on the Learning Commons rows.
🔴 **But an evaluator is its rubrics**, and the annotated corpora are non-commercial. Treat the MIT
code as usable and the shipped corpora as **not** usable in a paid engagement until `Gap 500-E`
is answered.

### 🔴 Excluded, with the reason recorded

- [`canyongbs/advisingapp`](https://github.com/canyongbs/advisingapp) — **340★**, an AI assistant
  for staff and **student success**, i.e. precisely the commercial shape of this industry. Read
  from bytes at `4449f765bdd0`: **Elastic License 2.0**, 3 860 B. Source-available, **not** OSI
  open source; it forbids offering the software to third parties as a hosted service. GitHub's
  `NOASSERTION` label concealed this. **Not shelvable, and not buildable on.**
- [`RandMelville/claude-war-room`](https://github.com/RandMelville/claude-war-room) — MIT, 62★, but
  a **false positive of `topic:edtech`**: a 5-agent feature-analysis orchestrator with no
  education function.
- [`wombats-writing-code/xoces`](https://github.com/wombats-writing-code/xoces) (MIT, 74★, last
  push **2017-07-24**) — permissive and dead.

### 🔴 The verdict column in this file is not fully trustworthy yet

Every **Apache-2.0** verdict recorded on this shelf before `p500` was graded against **one**
canonical form (SPDX, 1431 operative words) while the apache.org steward's own form is **1412** —
a 19-word difference between two legitimate texts. A repository shipping the steward's copy scores
a phantom **−19 DEVIANT**. `HKUDS/DeepTutor`'s recorded **−17** is really **+2**. The MIT rows in
this file are unaffected (MIT has one canonical form here and all three new rows are 0-delta), but
the Apache rows were **not** re-graded this pass. `Gap 500-B` carries it.


## 🆕 `p503` — `2026-10-28` — **🟢 THE PROMOTION GAP, MEASURED ON A NEW AXIS AND THEN HALVED BY LICENCE: of six rows with traction and no shelf, THREE are MIT and shelvable and THREE are legally unusable — one of them the fastest-growing education repository this base has ever tracked. 🔴 And the channel row `p502` added to the table above is TOO WIDE: the API answers `search`, it REFUSES `contents`, so licence bytes still come from `raw` alone.**

Reads: [`promotion-audit.2026-10-28-p503.tsv`](../evidence/promotion-audit.2026-10-28-p503.tsv),
[`licence-bytes.2026-10-28-p503.tsv`](../evidence/licence-bytes.2026-10-28-p503.tsv),
[`recency-axis.2026-10-28-p503.tsv`](../evidence/recency-axis.2026-10-28-p503.tsv),
[`channel-boundary.2026-10-28-p503.tsv`](../evidence/channel-boundary.2026-10-28-p503.tsv).

### 🔴 Correction to the verification table above, in its own words

`p502` added the row *"stars + licence + topics + forks, 100 rows/call — GitHub REST API via the
MCP channel — 🟢 WORKS, authoritative"*. 🟢 **True for `search`.** 🔴 **False for `contents`:**

```
mcp__github__get_file_contents(owner="learning-commons-org", repo="knowledge-graph", path="/")
→ Access denied: repository "learning-commons-org/knowledge-graph" is not configured
  for this session. Allowed repositories: gmilano/globant-kb, gmilano/education-kb
```

🔵 **The two endpoints have different authorisation models**: repository *search* answers for any
public repository; repository *contents* is scoped to the repositories attached to the session.
🟢 So the standing two-channel rule survives intact and its second channel is unchanged —
**family from the API, bytes from `raw.githubusercontent.com` at a `git ls-remote` SHA.** A
successor that reads `p502`'s row as *"the API can give me the licence file"* will get a refusal,
not a payload. Registered as `Gap 503-A`.

### 🟢 Shelved this pass — two MIT agents that have been in this base's history and on no shelf

Licence family from `license.spdx_id` (API) **and** from the payload at a pinned SHA (`raw`), with
the operative body compared token-for-token against this base's retained canonical MIT.

| Agent | Repo | Licence @ pinned SHA | ★ | Operative body | What it is | Region basis |
|---|---|---|---|---|---|---|
| **Study-Mate** | [`Miaotofu01/Study-Mate`](https://github.com/Miaotofu01/Study-Mate) | 🟢 **MIT**, 1 064 B `d8114f383632` (blob `1b105b8e1b6b`, sha256₁₆ `dc1997d8218985c9`) | **1 245** | 🟢 **IDENTICAL** (164 words, `745e05f91f85`) | Self-study companion that does the three things a tutor does and a chatbot does not: **plans a route**, teaches against it, and drives a project — with spaced repetition on the schedule. Topics declare `learning-agents`, not `chatbot`. | **APAC** — artefact language: description and README are Chinese-only |
| **learn-from-materials** | [`dmoshehun-prog/learn-from-materials`](https://github.com/dmoshehun-prog/learn-from-materials) | 🟢 **MIT**, 1 122 B `f8849746d85c` (blob `361465fb8b78`, sha256₁₆ `15ce43afa44a3cf4`) | **1 190** | 🟢 **IDENTICAL** | Turns a PDF, book or paper into an **interactive, traceable** learning page — every generated claim keeps a pointer back to the source span, with quizzing and note-taking on top. Ships a separate `NOTICE.md` (2 287 B, blob `461167a25e0e`). | **APAC** — bilingual 中文/English artefact |

🔵 **Why these two and not the rest of the slice:** both clear the licence bar on both channels,
both are pushed within the last ten days, and both are *agent-shaped* — a route-planner and a
source-grounded transformer, not a wrapper around a chat box. 🔴 **Neither has a test suite this
base could find, and neither declares a model boundary** — they assume a hosted LLM. For a district
or ministry engagement, see `T1`/`T13` on the local-first posture before proposing either.

### 🔴 Excluded this pass, with the reason recorded — and this is half the slice

| Repo | ★ | Read from bytes | Why it is not here |
|---|---|---|---|
| [`TrenTorch/TrenTorch`](https://github.com/TrenTorch/TrenTorch) | **741** *(🟢 `p510`, API; prior cell 739)* | 🔴 **PolyForm Noncommercial 1.0.0**, 4 635 B `898b8664cb38` (blob `d0fe054b67ee`, sha256₁₆ `a1530b506c55fef1`) | **Source-available, not open source.** The API reports `NOASSERTION`. 🔵 **Independently re-read this pass**: [`trending.md`](trending.md) recorded the same 4 635-byte payload on `2026-10-14` at **385★** — it is **739★** today, **+92% in 14 days**, the steepest growth in this slice. 🔴 The fastest-moving education repository in the window is the one Globant cannot bill against |
| [`JudgePeach/math-question-bank`](https://github.com/JudgePeach/math-question-bank) | 358 | 🔴 **AGPL-3.0**, 34 523 B `135b78b0f22c` (blob `be3f7b28e564`, sha256₁₆ `0d96a4ff68ad6d4b`), 6 tokens from canonical | Copyleft. Chinese high-school question bank with LaTeX rendering, LLM parsing and formula OCR — the **assessment-item layer** this shelf still lacks, behind a network-copyleft grant |
| [`artcc/freelingo`](https://github.com/artcc/freelingo) | 210 | 🔴 **AGPL-3.0**, 34 514 B `269feb00c09a` (blob `128919466b58`, sha256₁₆ `ea94d5765c590b11`), 9 tokens from canonical | Copyleft. Self-hosted language tutor with **Ollama-local** inference and CEFR plans — shelved as a *platform* in [`verticals/solutions.md`](../verticals/solutions.md) with the grant stated, never as a component to build on |

🔵 **The shape of the result:** 6 rows with traction and no shelf → **3 promotable, 3 walled**.
`p502` read the promotion gap as *"the real gap is not discovery, it is promotion"*; this pass
measures it and the gap is **half that size**. The other half needs a licence to change, not a
curator.

### 🔵 The axis itself: recency is a confirmation instrument, not a supply

| query | `total_count` | read | already in this base | novelty |
|---|---|---|---|---|
| `topic:education stars:>50 created:>2026-07-28` | 60 | 12 | **12** | **0%** |
| `topic:edtech stars:>25 created:>2026-04-01` | 20 | 12 | **12** | **0%** |
| `topic:ai-in-education stars:>50` (control, `p502`'s axis) | 3 | 3 | 3 | 0% |

🔴 **Slicing by creation date instead of by topic finds nothing new** — 0 of 24 on the top-star
slices of a 90-day and a 180-day window. 🟢 Which makes the finding above the useful one: the
base's problem on this axis is not that it has not *read* the supply, it is that **a third of what
it reads never reaches a shelf** (6 of 18 audited). Registered as `Gap 503-C`.
