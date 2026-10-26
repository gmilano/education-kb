---
industry: education
region: Global
updated: 2026-10-26
---

## 🆕 `p457` — **🟢 A SUPPLY TIER THESE SHELVES HAVE NEVER CARRIED, AND IT IS THE ONE MOST OF THE WORLD'S SCHOOLS ACTUALLY RUN ON: paper assessment. Eight permissive rows — four OMR engines and four assistive/accessible-learning foundations — every grant read first-hand at the resolved default ref. 🔴 Plus the whole shelf re-read: 390 of 457 carried addresses serve a grant, and 64.6 % of them are MIT.**

🔴 **`make hooks` DENIED** (`Code from External`) — twelfth denial in thirteen passes. 🔵 Nothing
below is gate-attested; the instrument, its two fabricated negative controls and its two positive
controls are at [`compose/code/p457-payload-census/`](../compose/code/p457-payload-census/census.py).
🔴 **Seven defects in this pass's own code — five in the reader, two in the controls — are
published on [`agents/top.md`](../agents/top.md)** rather than hidden.

### 🔴 The absence this pass closes, and why it was invisible for 456 passes

🔵 Searched against these three shelves before searching the web: **`OMR`, `optical mark
recognition`, `bubble-sheet`, `mark recognition`, `phoneme`, `braille`, `sign language`,
`dyslexia`, `speech-to-text` — all NINE at ZERO mentions.** 🔴 **These shelves carry 457 addresses
for an industry whose dominant assessment instrument, across most of its install base, is a sheet
of paper** — and they carried nothing that reads one.

🟡 The mechanism is the one `p453` named: the vocabulary is the variable. Every discovery leg these
shelves have run was phrased in the language of *digital* education — LMS, MCP, tutor, autograder,
LTI, xAPI. **A school in Nepal grading NEET practice exams off an ADF scanner is not in that
vocabulary**, so it was never returned, and the silence read exactly like coverage.

### 🟢 Tier 7 — paper assessment (OMR). Every grant read at the resolved default ref this pass

| repo | grant | ref | what it is | region |
|---|---|---|---|---|
| [`Udayraj123/OMRChecker`](https://github.com/Udayraj123/OMRChecker) | 🟢 **MIT** · `LICENSE` **1 104 B** `3d72ab01aefd` | 🔴 `master` | The canonical OMR engine: reads marked sheets *"fast and accurately using a scanner 🖨 or your phone 🤳"* — **a phone camera is a supported input**, which is the whole low-infrastructure case | ⚪ Global · India-origin |
| [`crispin0007/OMR`](https://github.com/crispin0007/OMR) | 🟢 **Apache-2.0** · `LICENSE` **11 358 B** `cfc7749b96f6` | `main` | Full exam pipeline, **offline on one Windows PC with no internet and no fees**: design answer sheets → scan from any ADF scanner → marks, ranks, **merit lists**, Excel + PDF scorecards, optional negative marking. Scoped by its own README to **Nepal CEE, NEET, JEE and school exams** | 🟢 **APAC** |
| [`sajidbuet/OMRFlow`](https://github.com/sajidbuet/OMRFlow) | 🟢 **MIT** · `LICENSE` **1 081 B** `71787b5c24e2` | `main` | Examination-administration grade: template design, **uncertain-mark review**, **attendance reconciliation**, MCQ scoring, **auditable** Excel results, entirely local | 🟢 **APAC** |
| [`power0matin/omr-bubble-sheet-marker`](https://github.com/power0matin/omr-bubble-sheet-marker) | 🟢 **MIT** · `LICENSE` **1 072 B** `440f3c6ab70c` | `main` | Offline marker for MCQ sheets as **PDF or image** (OpenCV + PyMuPDF). 🟡 **The thinnest row of the four** — the README is largely badges, and it is shelved as a component, not a platform | ⚪ Global |

🔴 **One copyleft flag, stated rather than shelved as permissive:**
[`bthicks/OMR-Grader`](https://github.com/bthicks/OMR-Grader) is **GPL-3.0** (`LICENSE.txt`
**35 149 B** `3972dc9744f6`) — a Python/OpenCV bubble-sheet grader. 🟡 Usable, but it carries the
obligation outward and so is not a vendoring candidate for a client deliverable.

🔴 **One refusal:** [`sakethbachu/OMR-scanner`](https://github.com/sakethbachu/OMR-scanner) is live
at `master` and serves **no grant at any of 12 probed paths**.

🟢 **Why this is a foundations tier and not a curiosity:** `crispin0007/OMR` and `sajidbuet/OMRFlow`
both state **offline, single-machine operation** as a feature, not a limitation. That is the exact
deployment envelope of the institutions these shelves' regional sections describe as
under-served — and it is the one envelope the entire MCP/LMS-connector tier on these shelves
**cannot** serve, because every row in it assumes a hosted LMS and a network.

### 🟢 Tier 8 — assistive and accessible-learning foundations

🔵 Accessibility is a **statutory** requirement in the two regions these shelves sell into hardest
(IDEA and Section 504 in the US; the European Accessibility Act in the EU), and it was carried here
only as the word *"accessibility"* in prose. These are the readable, permissive foundations:

| repo | grant | ref | what it is | region |
|---|---|---|---|---|
| [`NSoiffer/MathCAT`](https://github.com/NSoiffer/MathCAT) | 🟢 **MIT** · `LICENSE` **1 065 B** `f8f65c73234f` | `main` | **The strongest row in this tier.** MathML → speech **and braille** (**Nemeth, UEB Technical, CMU** and others) plus **navigation of math** by structure. Speech in **15 shipped languages** (Chinese Traditional, English, Finnish, French, German, Greek, Hungarian, Indonesian, Norwegian, Polish, Portuguese, Russian, Spanish, Swedish, Vietnamese); sourced from the **DAISY Consortium** | ⚪ Global |
| [`AVauraTech/assistive-ai-accessibility-suite`](https://github.com/AVauraTech/assistive-ai-accessibility-suite) | 🟢 **MIT** · `LICENSE` **1 065 B** `142a4062de61` | `main` | Eight assistive tools in **one browser tab with no cloud dependency**: ASL fingerspelling, eye-gaze control, air writing, live captions, braille studio, scene description, document reader, depth obstacle warning. **MediaPipe on-device via WASM**, optional VLM with offline fallback | ⚪ Global |
| [`open-source-accessibility/monarch-message`](https://github.com/open-source-accessibility/monarch-message) | 🟢 **MIT** · `LICENSE` **1 082 B** `43433fb8ca32` | `main` | Braille messenger for the **APH Monarch** — the American Printing House's refreshable multi-line braille tablet, a device with a real US school install base. 🟡 Small surface, concrete hardware target | 🟢 **North America** |
| [`Sais-gallego/braillevision-ocr`](https://github.com/Sais-gallego/braillevision-ocr) | 🟢 **MIT** · `LICENSE` **1 069 B** `4fdf172c6b2d` | `main` | **Braille OCR in the reverse direction**: decodes *embossed and printed* 6-dot cells into text and speaks it. Full Grade-1 English: alphabet, numeric prefix `⠼`, capital indicator `⠠`, punctuation | ⚪ Global |

🔴 **One refusal:** [`davidjenner/OpenDyslexic-Converter`](https://github.com/davidjenner/OpenDyslexic-Converter)
is live at `main` with **no grant served**.

🟢 **The composition that makes this a tier rather than four rows:** `MathCAT` turns the *content*
accessible, `braillevision-ocr` turns *existing paper* accessible, `monarch-message` reaches the
*device*, and the AVaura suite covers the *input* modalities. 🔵 Wired together they are the
accessibility layer for the OMR tier above — see
[`compose/patterns.md`](../compose/patterns.md) `P457-2`.

### 🟢 The whole shelf re-read — `Gap 456-A`'s numbers, in the form that matters here

🔵 Full result and grading on [`agents/top.md`](../agents/top.md). For a foundations reader the two
load-bearing numbers are:

- 🟢 **390 of 457** carried addresses serve a grant at their resolved default ref; **252 are MIT**
  (**64.6 %** of grants read) and **49 Apache-2.0** — so **77 %** of the readable supply on these
  shelves is in the two families a client can build on without a service boundary.
- 🔴 **54 are `REPO_LIVE_NO_GRANT`** and **13 are dead**. 🟡 Of the 20 whose cell states a licence
  with no payload behind it, **8 are recoverable from an in-repo manifest** — `package.json`,
  `pyproject.toml` or a CRAN `DESCRIPTION` — and **12 are recoverable from neither channel**
  (`Gap 457-B`).

🟡 **A correction to this shelf, in the safe direction:** [`cran/exams`](https://github.com/cran/exams)
is carried as **GPL-3.0** and its `DESCRIPTION` grants **`GPL-2 | GPL-3` disjunctively** — the
integrator may elect **GPL-2.0**. The cell is narrower than the grant, not wrong.


## 🆕 `p456` — **🟢 Every foundational platform on this shelf now carries its RESOLVED default branch, and for 11 of them it is not what a bare `git clone` would suggest: ILIAS checks out `release_11`, Tutor `release`, OpenEduCat `19.0`, BigBlueButton `v4.0.x-develop`. 🟢 And the licence families this shelf carries are CONFIRMED — 14 of 15 off-list cells re-read byte-identical.**

🔴 **`make hooks` DENIED** (`Code from External`) — eleventh denial in twelve passes. 🔵 Nothing
below is gate-attested; 31 controls run in both directions
([`compose/code/p456-ref-resolution/controls.py`](../compose/code/p456-ref-resolution/controls.py)).

### 🟢 The ref column this shelf has never had, and why it is a foundations fact

🔵 A foundational repo is one a client **vendors, forks or pins**. For 15 of the 455 addresses
carried across these shelves the **resolved default branch is outside the ref list every pass
since `p449` guessed** — so a recipe that names a repository without naming a ref gets whatever
the project's maintainers point `HEAD` at, which for these eleven platforms is a **release line**,
not a trunk:

| foundation | address | resolved default branch | grant re-read at that ref | re-read agrees with the carried cell? |
|---|---|---|---|---|
| ILIAS | [`ILIAS-eLearning/ILIAS`](https://github.com/ILIAS-eLearning/ILIAS) | 🔴 **`release_11`** | **GPL-3.0** · `LICENSE` | 🟢 byte-identical |
| BigBlueButton | [`bigbluebutton/bigbluebutton`](https://github.com/bigbluebutton/bigbluebutton) | 🔴 **`v4.0.x-develop`** | **LGPL-3.0** · `LICENSE` | 🟢 byte-identical |
| Tutor (Open edX) | [`overhangio/tutor`](https://github.com/overhangio/tutor) | 🔴 **`release`** | **AGPL-3.0** · `LICENSE.txt` | 🟢 byte-identical |
| OpenEduCat | [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | 🔴 **`19.0`** | **LGPL-3.0** · `LICENSE` | 🟢 byte-identical |
| Gibbon | [`GibbonEdu/core`](https://github.com/GibbonEdu/core) | 🔴 **`v31.0.00`** | **GPL-3.0** · `LICENSE` | 🟢 byte-identical |
| Edu-Sharing | [`edu-sharing/Edu-Sharing`](https://github.com/edu-sharing/Edu-Sharing) | 🔴 **`maven/fixes/10.0`** | **GPL-3.0** · `LICENSE.txt` | 🟢 byte-identical |
| i-Educar | [`portabilis/i-educar`](https://github.com/portabilis/i-educar) | 🔴 **`2.12`** | **GPL-2.0** · `LICENSE` | 🟢 byte-identical |
| RosarioSIS | [`francoisjacquet/rosariosis`](https://github.com/francoisjacquet/rosariosis) | 🔴 **`mobile`** | **GPL-2.0** · `LICENSE` | 🟢 byte-identical |
| Krayin CRM | [`krayin/laravel-crm`](https://github.com/krayin/laravel-crm) | 🔴 **`2.2`** | **MIT** · `LICENSE` | 🟢 byte-identical |
| TinCanPython (xAPI) | [`RusticiSoftware/TinCanPython`](https://github.com/RusticiSoftware/TinCanPython) | 🔴 **`3.x`** | **Apache-2.0** · `LICENSE` | 🟢 byte-identical |
| Caliper PHP | [`tl-its-umich-edu/caliper-php-public`](https://github.com/tl-its-umich-edu/caliper-php-public) | 🔴 **`public`** | **LGPL-3.0** · `LICENSE` | 🟢 byte-identical |

🔴 **The operational consequence, and it is not cosmetic:** `git clone https://github.com/ILIAS-eLearning/ILIAS`
gives you `release_11`, not a trunk — a *maintenance line* that will stop moving. `overhangio/tutor`
gives `release`, which tracks whatever Open edX named current. 🟢 **Every clone or vendor step in
[`compose/patterns.md`](../compose/patterns.md) must name `-b <ref>` explicitly**, and the refs are
the column above. 🔵 Four further off-list cells are not foundations and are recorded in the
evidence rather than here: `lukecarroll15/blackboard-mcp` (`tcd`), `michaelsboost/ArabEngo`
(`gh-pages`), `jibrilsettles-dot/Arabic-Tutor` (🔵 default branch
`claude/eager-newton-boy1g0` — an agent session branch left as the project's default, and it
carries **no grant**), and `lanis-mobile/LanisAPI` (`deprecation-notice`, the corrected row).

### 🟢 The licence families on this shelf are confirmed, by a channel that could have refuted them

🟢 **14 of the 15 off-list cells re-read byte-identical** — same family, same digest — against
`p455`'s own ladder reproduced in `p456`'s instrument. Only `lanis-mobile/LanisAPI` differed, and
that is the corrected row on [`agents/top.md`](../agents/top.md). 🔵 So the exotic default branches
were **never** the hazard `Gap 455-A` feared: `HEAD` on `raw.githubusercontent.com` followed the
resolved default branch for **439 of 439 live addresses, zero divergences**, and that is why the
carried reads were right. Evidence:
[`evidence/carried-default-off-list.2026-10-26-p456.tsv`](../evidence/carried-default-off-list.2026-10-26-p456.tsv),
[`evidence/ref-axis-head-vs-default.2026-10-26-p456.tsv`](../evidence/ref-axis-head-vs-default.2026-10-26-p456.tsv).

### 🟢 The dead-address class is confirmed cross-channel, 455/455

🟢 16 addresses resolve nothing through `ls-remote`, and **every one is already carried as
`ADDRESS_DEAD` or `ABSENT`** from the independent 404 sweep — including both fabricated negative
controls. 🔵 `Gap 454-H` left standing the worry that an `ADDRESS_DEAD` cell might be an artefact
of guessing paths and refs; two independent channels agreeing on all 455 settles it.

### 🔵 What this does not establish

🔴 **`Gap 456-A`:** the **424** cells whose default branch is inside the guessed list were checked
for *ref identity* (`HEAD` == default, 439/439) but **not re-read for payload** at the resolved
ref. A payload drift there would be invisible to this pass.

## 🆕 `p455` — **🟢 `Gap 454-C` IS ANSWERED: the licence reader gains a VERSION AXIS, and the `edu-sharing` pair that `p454`'s `canon()` graded `AGREE` now disagrees — `GPL-2.0` declared against `GPL-3.0` served, mutually incompatible. 🔴 And the sweep that answer was supposed to deliver produced 88 apparent family disagreements that are RETRACTED IN FULL, because the mechanism is this pass's extractor and the shelves were right.**

🔴 **`make hooks` DENIED** (`Code from External`) — tenth denial in eleven passes. 🔵 Contracts
re-implemented and run independently; 34 controls pass
([`controls.py`](../compose/code/p455-version-axis/controls.py)).

### 🟢 `Gap 454-C` closed on the axis it named

`Gap 454-C` stated the defect and its cost precisely: *"A family-level reader cannot grade a
version-level incompatibility, and this base has one live."* `canon()` collapsed `GPL-2.0` and
`GPL-3.0` onto the family `GPL`, so the one real mismatch on these shelves graded `AGREE`.

🟢 **[`family_version.py`](../compose/code/p455-version-axis/family_version.py)** keeps `p454`'s
title-block anchor — the only region of a payload a preamble cannot reach — and reads the version
from the same anchor, where the GNU licences state it. Measured on the pair the gap named:

| | declared | served at `HEAD` | `p454` `canon()` | `p455` `canon()` |
|---|---|---|---|---|
| [`edu-sharing/Edu-Sharing`](https://github.com/edu-sharing/Edu-Sharing) | npm `ngx-edu-sharing-api@10.0.1` → **`GNU GPL v2`** | **GPL *Version 3*** · `LICENSE.txt` `35 148` B `8b1ba204bb69` | 🔴 `GPL` vs `GPL` → **`AGREE`** | 🟢 `GPL-2.0` vs `GPL-3.0` → **`DISAGREE`**, and `compatible()` returns **`False`** |

🟢 **And a second axis the same title block does NOT carry, which decides whether the
incompatibility actually bites.** `GPL-2.0-only` cannot combine with `GPL-3.0`; `GPL-2.0-or-later`
can, because it may be taken forward. That election lives in the per-file notice and the
*How to Apply* appendix, never in the title block, so `only_or_later()` reads the whole payload and
returns **`UNSTATED`** when the payload does not say — guessing `or-later` invents a combination
right, guessing `only` invents a prohibition. 🟢 **Read first-hand this pass, it changes a live
verdict:** [`oat-sa/tao-core`](https://github.com/oat-sa/tao-core)'s GPLv2 (`18 025` B
`a01259a1b522`) is **`or-later`**, so TAO *may* be combined with GPL-3.0 code — where a
version-only reader would have called it a dead end.

### 🔴 The sweep's headline is RETRACTED, and the mechanism is worth more than the number was

The sweep ran over **481 distinct addresses** across all eight shelves whose shelf line names a
GNU family ([`evidence/gnu-version-axis.2026-10-26-p455.tsv`](../evidence/gnu-version-axis.2026-10-26-p455.tsv)).
Its first run reported **99 `FAMILY_DISAGREE` (20.6 %)**. 🔴 **That number is an artefact, and so
is the 88 that survived a first correction.** Three mechanisms, each found by reading the shelf
line the verdict was built on:

1. 🔴 **Line-level co-occurrence.** The extractor attributed every GNU token on a line to every
   address on it. These shelves are prose and multi-project tables, so it "found"
   [`learningequality/kolibri`](https://github.com/learningequality/kolibri) claiming `GPL-3.0`
   (Kolibri is **MIT**) and [`junit-team/junit4`](https://github.com/junit-team/junit4) claiming
   `GPL` — 🔴 **and this pass's own first write of that sentence called JUnit 4 "EPL" from
   background knowledge rather than a read; re-probed, `junit-team/junit4` serves NO grant at
   any of 13 root paths (`REPO_LIVE_NO_GRANT`), so the shelf's `GPL` is unsupported and so was
   the correction.** Corrected to cell-level attribution: 481 → 461 cells.
2. 🔴 **Sole-address prose rows.** The correction's fallback — *a row naming exactly one address is
   about that address* — is also unsound, because a prose sentence mentioning one repository and
   one licence is not a grant assertion about that repository.
3. 🔴 **Per-subtree grants, which a root-only reader cannot grade at all.** The decisive case:
   [`krzysztofbury/librus-mcp`](https://github.com/krzysztofbury/librus-mcp) is carried as **MIT at
   root** (`1 071` B `22e7ab2dbddc`) **and GPL-3.0 on its `legacy_reference/` subtree**
   (`35 149` B `3972dc9744f6`), with an explicit instruction — *integrate over MCP, never vendor
   the repository*. The sweep compared a root payload against a claim that was never about the root.

🔵 **And the finding that makes this a closure rather than a failure: a previous pass had already
built the taxonomy.** The trending shelves classify exactly this population —
`DEPENDENCY-SCOPED` for Kolibri (*"explicitly scoped to dependencies … the repo is MIT and the
prose says so"*) and `BOUNDARY-NAMED` for
[`peancor/moodle-mcp-server`](https://github.com/peancor/moodle-mcp-server) (*"it is MIT while
in-tree Moodle plugins are GPL-3.0 — the licence boundary **is** the architecture finding"*).
🔴 **Registered as `Gap 455-B`:** a GNU sweep must CONSUME that taxonomy, not re-derive it, and
no shelf carries a machine-readable grant column that would let it. **On a prose shelf, adjacency
is not attribution** — the same rule `Gap 451` set for registry names and `Gap 454-I` for table
shapes, now measured a third time on a third channel.

### 🟢 What the sweep DOES establish, with its denominator

| verdict | cells | share | what it means |
|---|---|---|---|
| 🟢 `AGREE` | 306 | 66.4 % | payload grade matches a cell-attributed shelf claim |
| 🔴 `FAMILY_DISAGREE` | 88 | 19.1 % | 🔴 **RETRACTED as instrument error** — an upper bound on *apparent* disagreement, not a shelf-defect rate |
| 🔴 `UNCHECKABLE` | 56 | 12.1 % | `ADDRESS_DEAD` or `REPO_LIVE_NO_GRANT`: the carried grant cannot be checked against anything. 🔵 Consistent with `Gap 454-H`'s **22.5 %** on a smaller, differently-selected population |
| 🟡 `UNDER_SPECIFIED` | 11 | 2.4 % | 🟢 **The sound new number.** The shelf states a bare `GPL`/`LGPL`/`AGPL` with no version while the payload serves one — so these 11 cells **cannot support a compatibility decision in either direction** |
| 🔵 `AMBIGUOUS` (refused) | 20 | — | no cell-level attribution anywhere; excluded from the denominator and **named** in the evidence file, because a silently-dropped cell looks exactly like one that agreed |

### 🔴 Two more defects of this pass's own instrument, both caught by controls before publication

🔴 **`Gap 455-D` — `canon()` could not normalise the commonest shorthand there is.** The
version-stripping rule was `\bv(\d)` → digit. `l` and `v` are both word characters, so there is no
boundary inside **`gplv3`**: `"GNU GPL v2"` (spaced) normalised correctly and `GPLv3` (compact)
fell through to the identity branch and compared unequal to everything. The compact form is what
npm and crates.io actually serve. 🔵 `p454`'s own `FAMILY_TOKENS` anticipated it (`\bgplv?[23]\b`);
this pass's `canon()` did not — a defect **inside one pass, between two files**.

🔴 **`Gap 455-C` — a `200` is not evidence of a well-formed record.** `registry.npmjs.org/pawnote`
was read **twenty times**: nineteen returned `1.6.2 / GPL-3.0-or-later / LiterateInk/Pawnote.js`,
and **one returned HTTP 200 with a body that parsed as JSON and carried no `dist-tags` at all**.
An unguarded parser records that as *"the package declares no licence"* — a silent false negative
on the channel every registry-sourced cell on these shelves rests on. 🟢 Fixed by asserting record
**shape**, not status ([`fetch.py`](../compose/code/p455-version-axis/fetch.py) `REQUIRED_SHAPE`).
🔵 And the repeat reads are the reason this is stated as a rate rather than a flap: 12 consecutive
reads of three registries were **STABLE**, so the channel is sound and the *single-read* discipline
was not.

🔴 **Two control defects were this pass's too**, and they failed in the safe direction: the first
cut expected `MIT` where `p454` correctly grades a titleless payload `MIT (body form, no title)`,
and asserted that every GNU grade must *differ* from `p454`'s — wrong for `AGPL`, whose only live
version is 3.0, so there was nothing to refine. 🟢 Both were the **expectation's** error, not the
reader's, and both were corrected before any verdict was published.

### 🔴 `Gap 454-A` is still open, and this pass deliberately did not close it

`Gap 454-A` records that the defective 40-line-window reader in
[`p453-vocabulary-ledger/verify.py`](../compose/code/p453-vocabulary-ledger/verify.py) is *"still
what the next pass will import unless it reads this row"*. 🔴 **This pass read the row and did not
patch that file** — it built `family_version.py` beside it instead, for `p454`'s stated reason:
gate-adjacent code should not be edited by a pass that cannot run the gate against it, and the
gate has now been denied ten times in eleven passes. 🟢 **The actionable form:** any later pass
should import `family()` and `canon()` from
[`p455-version-axis/family_version.py`](../compose/code/p455-version-axis/family_version.py),
which is title-anchored, version-bearing and control-covered, and treat `verify.py::family` as
superseded. 🔴 Until the gate runs, that is a convention and not an enforcement.

## 🆕 `p454` — **🟢 `Gap 453-D` CLOSES for APAC with Indonesia's national register reached by four permissive clients, and a fifth region gains a foundational OER repository. 🔴 And that repository is the pass's second licence correction: npm declares `GNU GPL v2`, the payload at `HEAD` is `GPL-3.0` — two incompatible licences under one hint.**

🔴 **`make hooks` DENIED** (`Code from External`) — ninth denial in ten passes. Nothing here is
gate-attested; the contracts were re-implemented and are listed in `intel/open-gaps.md`.

### 🟢 The APAC institution-registry layer — the region `Gap 453-D` named as unsearched

🔵 `Gap 453-D` recorded the layer as *"two regions deep and three never searched"*, with
**Indonesia, Japan, the Philippines** named. 🟢 **Indonesia closes.** Its national education data
system, **Dapodik** (*Data Pokok Pendidikan*, `dapo.kemendikdasmen.go.id`), is reachable from
permissively-granted code in three languages, and the student-identity tier (**VerValPD**) in a
fourth:

| repo | grant (first-hand, `HEAD`) | stratum | region |
|---|---|---|---|
| [`ardianryan/dapodik-sdk`](https://github.com/ardianryan/dapodik-sdk) | **MIT** · `1 739` B `29e7d361ee3d` | national register — typed SDK (TS/JS) | APAC |
| [`adereksisusanto/dapodik-api-php`](https://github.com/adereksisusanto/dapodik-api-php) | **MIT** · `1 105` B `ce39902853af` | national register — PHP client, CI-tested | APAC |
| [`smantriplw/vervalpd-node`](https://github.com/smantriplw/vervalpd-node) | **MIT** · `1 068` B `0ae5076b1e03` | student-identity verification (VerValPD) | APAC |
| [`bantenprov/dapodik-data-guru`](https://github.com/bantenprov/dapodik-data-guru) | **MIT** · `1 072` B `3508ba25c5ad` | provincial teacher-data aggregate | APAC |
| [`pipeworx-io/mcp-estat-japan`](https://github.com/pipeworx-io/mcp-estat-japan) | **MIT** · `1 070` B `42501667035e` | national statistics portal (e-Stat), education one domain of ~5 000 tables | APAC |

🟢 **Why this is a foundation and not a trend row: all four Indonesian grants are MIT, and they
stack.** The register (`dapodik-sdk` / `dapodik-api-php`), the identity tier (`vervalpd-node`) and
the aggregate tier (`dapodik-data-guru`) are three different strata of one national system, each
separately vendorable. That is the same shape `p453` closed for North America with IPEDS, and the
first time this base can say it for an APAC country.

### 🔴 EMEA/Global — a foundational OER repository, and a GPL **version** disagreement

| repo | registry hint | payload at `HEAD` | region |
|---|---|---|---|
| [`edu-sharing/Edu-Sharing`](https://github.com/edu-sharing/Edu-Sharing) | npm `ngx-edu-sharing-api@10.0.1` declares **`GNU GPL v2`** | 🔴 **`GNU GENERAL PUBLIC LICENSE Version 3`** · `LICENSE.txt` `35 148` B `8b1ba204bb69` | EMEA *(Germany)* |

🟢 **edu-sharing is a genuine foundational asset** — an open-source repository/federation layer for
**open educational resources**, with maintained Angular API and UI bindings (`ngx-edu-sharing-api`,
`ngx-edu-sharing-ui`, modified `2026-08-07`), used across German-speaking state education portals.

🔴 **But the licence hint is wrong in the one way that cannot be waved through: GPL-2.0 and
GPL-3.0 are mutually incompatible.** A deliverable assembled on the npm field's authority could
not lawfully combine edu-sharing with a GPL-2.0-only dependency. 🔵 And this base's **own** family
reader hides it: `canon()` collapses `GPL-2.0-only` and `GPL-3.0` onto the family `GPL`, so the
sweep graded the pair `AGREE`. 🔴 That is `Gap 454-C`, registered this pass — **a family-level
reader cannot grade a version-level incompatibility**, and three of this base's carried GPL cells
are family-level only.

### 🔵 Philippines — an INFORMED ABSENCE, with a denominator and a named cause

🔴 **No Philippine school-registry asset surfaced, and the reason is the search term, not the
country.** `deped` returned **59 candidates and 0 education assets**: on Packagist it matches the
substring `dep` in `deptrac/deptrac`, `php-di/php-di`, `symfony/dependency-injection`,
`shipmonk/composer-dependency-analyser` and every other dependency-shaped package. `psa`
(Philippine Statistics Authority) matched ConnectWise PSA, PureScript `psa` and Oracle `oci-psa`.

🟡 **What DID surface is a different stratum, and it is real:** the **PSGC** (Philippine Standard
Geographic Code) layer — [`pcofilada/psgc`](https://github.com/pcofilada/psgc),
[`jobuntux/psgc`](https://github.com/jobuntux/psgc),
[`anthonygacis/psgc-js`](https://github.com/anthonygacis/psgc-js),
[`aivangogh/ph-address`](https://github.com/aivangogh/ph-address) — administrative geography, the
same stratum as LATAM's `municipios-br`. 🔵 Grants **not** read first-hand this pass and therefore
**not** celled; they are candidates for `p455`, not rows.

🟢 **Stated so the absence is not mistaken for coverage:** the Philippine *school* register
(DepEd's EBEIS/LIS) is **not** reachable from any package registry this pass searched, and the
unambiguous vocabulary for it — a long, distinctive proper name — **has not been identified**.
That is the actionable half of the nil.

## 🆕 `p453` — **🟢 `Gap 452-D` IS CLOSED FOR NORTH AMERICA, AND IT WAS THE CHEAP GAP `p452` SAID IT WAS: five permissively-granted US institution-registry assets, all read first-hand at `HEAD`, where the prior pass could name none and had searched for none. 🔴 APAC is closed as an INFORMED ABSENCE instead: India's school directory exists at 1.47 M rows and NOT ONE of its packaged forms carries a permissive grant.**

🔴 **`make hooks` DENIED** (`Code from External`) — eighth denial in nine passes. Nothing here is
gate-attested; the load-bearing contracts were re-implemented independently and all are green.

### 🟢 The North America institution-registry layer — the gap `p452` opened, closed one pass later

🔵 `p452` registered `Gap 452-D` as *"the institution-registry layer is one country deep and four
of five regions have never been searched for it"*, and named the US series (NCES CCD, IPEDS) whose
*"packaged permissive form is simply unknown here"*. 🟢 It is known now.

| repository | grant, read first-hand at `HEAD` | what it actually is | region |
|---|---|---|---|
| [`bolewood/collegedata-fyi`](https://github.com/bolewood/collegedata-fyi) | 🟢 **MIT** — `LICENSE` **1 115 B `sha256₁₂ a3a16c648652`** | 🟢 **The strongest row of the five.** An open **Common Data Set** API and preservation archive: each school's CDS document found, extracted to a canonical schema (**1 105 fields** keyed by stable question number from the official 2025-26 template) and published beside the raw source, plus an NCES/IPEDS federal baseline keyed by zero-padded `UNITID`. Self-reported integrity audit of 2026-08-06: **6 322 institutions** in the federal directory, **4 071** archived CDS documents, **262 537** `cds_fields` rows | 🟢 **North America** — US |
| [`paulgp/ipeds-database`](https://github.com/paulgp/ipeds-database) | 🟢 **MIT** — `LICENSE` **1 056 B `sha256₁₂ 1126322e2cc8`** | Builds a harmonised **DuckDB** database from 20+ years of IPEDS in one command: **~27 M rows across 23 tables**, every US postsecondary institution **1997-2024** — admissions, enrolment, completions, tuition, aid, graduation rates, staffing | 🟢 **North America** — US |
| [`scienceforamerica/scipeds`](https://github.com/scienceforamerica/scipeds) | 🟢 **MIT** — `LICENSE` **1 088 B `sha256₁₂ e04b31a1be21`** *(body-form grant: no title line, opens at `Permission is hereby granted`)* | Python package that pre-processes and standardises IPEDS into a queryable store; carries **institutional-characteristics directory** data, which is the registry axis proper. `v0.0.9` adds 2025 data | 🟢 **North America** — US |
| [`UrbanInstitute/ipeds-scraper`](https://github.com/UrbanInstitute/ipeds-scraper) | 🟢 **MIT** — `LICENSE.md` **1 058 B `sha256₁₂ bac93c5411aa`** *(body-form)* | Downloads IPEDS complete data files and dictionaries — the ingestion leg under the two rows above. Institutional publisher (**Urban Institute**) | 🟢 **North America** — US |
| [`rhawrami/genpeds`](https://github.com/rhawrami/genpeds) | 🟢 **MIT** — `LICENSE.md` **1 071 B `sha256₁₂ c39fac37d50c`** *(body-form)* | Python API for requesting and cleaning IPEDS data, `pip`-installable | 🟢 **North America** — US |

🟢 **Why this is a foundations row and not an agents row.** None of the five is an agent. They are
the **system of record an engagement keys its rollout to** — the question *"which institutions
exist, and what is true of them"* — which `p452` identified as the layer this base had eight
platforms to *run* a school with and almost no data about *which schools exist*.

### 🔴 `ajhaller/IPEDS` — a grant that is neither present nor absent, and the mechanism is the R ecosystem

🔴 Its `LICENSE` is **43 B** — `YEAR: 2022` / `COPYRIGHT HOLDER: IPEDS authors`. 🔵 **That is not a
grant and not an absence**: `DESCRIPTION` declares `License: MIT + file LICENSE`, and the MIT text
is served from `LICENSE.md`. The R convention **splits the grant across two files**, so a payload
reader sees 43 B of metadata and a code-licence grader returns `UNREAD`.
🟢 **This base already records the sibling class** — `cran/catR` is carried as *"GPL (>= 3) —
`DESCRIPTION` only"* — so what `p453` adds is the **two-file composite** (`cran/shiny` is the
control instance, `YEAR`/`COPYRIGHT HOLDER` stub plus `MIT + file LICENSE`), not the ecosystem
itself. 🔴 Registered as `Gap 453-C`.

### 🔴 APAC: recorded as an informed absence, with the denominator that makes it informative

🔴 **India's school directory is the largest in the world and none of its packaged forms is
permissively granted.** Probed first-hand at `HEAD` this pass:

| address | grant at `HEAD` | consequence |
|---|---|---|
| [`deedy/cbse_schools_data`](https://github.com/deedy/cbse_schools_data) | 🟡 **CC-BY-SA-4.0** — `LICENSE` **20 131 B `sha256₁₂ 1f5de47ca3fb`** | ~20 367 CBSE schools (2018). 🔴 **Share-alike**: a derived registry inherits the obligation, so it is not a permissive base |
| [`learnram/ads-schools-data`](https://github.com/learnram/ads-schools-data) | 🔴 **no payload at 9 probed paths** | UDISE+-derived national directory, ~28 MB gzipped CSV — **ungranted** |
| [`dougj892/public-datasets`](https://github.com/dougj892/public-datasets) | 🔴 **no payload at 9 probed paths** | India education datasets — ungranted |
| [`unknownsteve7/UDISE_DATA_ANALYSIS`](https://github.com/unknownsteve7/UDISE_DATA_ANALYSIS) | 🔴 **no payload** | 4 GB pipeline over 1.47 M schools, 2023-24 + 2024-25 — ungranted |
| [`mukulyadav0118/india-school-education-analytics`](https://github.com/mukulyadav0118/india-school-education-analytics) | 🔴 **no payload** | UDISE+ 2025-26, seven states — ungranted |

🔵 **This is the kind of absence the encargo asks to be written down rather than left silent:
the supply exists, it is large, and 4 of 5 packaged forms grant nothing**, so an APAC engagement
keyed to a school registry must go to the UDISE+ portal's own terms, not to GitHub. 🔴 `Gap 453-D`
carries the unsearched remainder: **Global** and the rest of **APAC** (Japan, Indonesia,
Philippines) have still not been searched for this layer.

### 🟢 One LATAM data row, and it is a licence disagreement as well as a registry asset

| repository | grant | surface | region |
|---|---|---|---|
| [`nataliasm23/icones-bandeiras-br-uf`](https://github.com/nataliasm23/icones-bandeiras-br-uf) | 🔴 **CC0-1.0** — `LICENSE` **7 048 B `sha256₁₂ a2010f343487`**. 🔴 **npm `municipios-br@3.2.1` declares `MIT`** — see `Gap 453-A` | Brazilian municipality and UF (state) reference data with flag icons — the administrative-geography key a LATAM rollout joins a school list to | 🟢 **LATAM** — Brazil |

🔵 **CC0 is the right instrument for data and the wrong one to infer from a code manifest**: the
registry's `MIT` would have been published here as the grant had the payload not been read.

## 🆕 `p452` — **🟢 `Gap 450-C` ANSWERED WITH A NUMBER after carrying one pass: 394 carried byte cells re-read with the corrected method, 361 reproduce EXACTLY, and the uncorrected trailing-newline method accounts for 11 of them — 2.8 %, not a sweep-wide defect. 🔴 Getting that number took FOUR cuts of the extractor, and the first three each produced a confident phantom-drift list of 200, 104 and 5 rows. Every phantom was caught by a control, never by inspection.**

🔴 **`make hooks` DENIED** (`Code from External`) — seventh denial in eight passes. Nothing here is
gate-attested; the four load-bearing contracts were re-implemented by hand and all four are green.

### 🟢 `Gap 450-C`'s open question, and the answer

`p450` found that reading a payload through shell command substitution **strips the trailing
newline**, so every byte count taken that way runs **exactly one byte low** — silently, and
selectively, since a payload with no trailing newline measures identically both ways. 🔵 It left the
question: *"how many byte counts already on these shelves were produced by the uncorrected
method?"*, with the warning that a one-byte-low cell is indistinguishable from drift.

🟢 The instrument is
[`compose/code/p452-byte-census/extract_cells.py`](../compose/code/p452-byte-census/extract_cells.py);
the census output is committed to
[`evidence/byte-cell-census.2026-10-26-p452.tsv`](../evidence/byte-cell-census.2026-10-26-p452.tsv).
Every cell was re-read with `curl -w '%{size_download}'`, the method `p450` proved correct.

| verdict | n | share of 394 | reading |
|---|---|---|---|
| 🟢 `EXACT` | **361** | 91.6 % | the carried cell is reproduced to the byte |
| 🔴 `OFF_BY_ONE` | **13** *(11 confirmed by hand)* | 2.8 % | `measured − carried = 1`, and **every one of them ends in a trailing newline** — `p450`'s mechanism exactly |
| ⚪ `UNREACHABLE` | **12** | 3.0 % | `404` at `HEAD`; several are addresses this base already carries as withdrawn |
| 🟡 `OTHER_DELTA` | **8** *(5 genuine)* | 1.3 % | a real disagreement, listed below |

🟢 **The mechanism is confirmed and it is bounded.** Not one of the 361 `EXACT` cells is off by one,
and all 13 off-by-one cells end in a trailing newline — so the `+1` class is **not noise**, it is
`p450`'s defect, and it touched under 3 % of the population rather than the sweep `Gap 450-C` feared.

### 🔴 The eleven confirmed, each one a cell to correct rather than a drift to investigate

| address | carried | re-read | ends in newline? |
|---|---|---|---|
| [`packbackbooks/lti-1-3-php-library`](https://github.com/packbackbooks/lti-1-3-php-library) | 11 342 B | 🔴 **11 343 B** | 🟢 yes |
| [`Git-Kaushal/AI-Teacher-Training`](https://github.com/Git-Kaushal/AI-Teacher-Training) | 2 099 B | 🔴 **2 100 B** | 🟢 yes |
| [`Scaler-Opensource/exam-guard`](https://github.com/Scaler-Opensource/exam-guard) | 11 356 B | 🔴 **11 357 B** | 🟢 yes |
| [`digitalcredentials/vc`](https://github.com/digitalcredentials/vc) | 1 524 B | 🔴 **1 525 B** | 🟢 yes |
| [`SaadRahman01/moodle-mcp`](https://github.com/SaadRahman01/moodle-mcp) | 1 067 B | 🔴 **1 068 B** | 🟢 yes |
| [`laurauguc/grading_assistant`](https://github.com/laurauguc/grading_assistant) | 1 071 B | 🔴 **1 072 B** | 🟢 yes |
| [`paper-instruments/rubric`](https://github.com/paper-instruments/rubric) | 1 076 B | 🔴 **1 077 B** | 🟢 yes |
| [`baker-jr-john/automated-summary-evaluation-llm`](https://github.com/baker-jr-john/automated-summary-evaluation-llm) | 1 070 B | 🔴 **1 071 B** | 🟢 yes |
| [`open-edge-platform/education-ai-suite`](https://github.com/open-edge-platform/education-ai-suite) | 11 350 B | 🔴 **11 351 B** | 🟢 yes |
| [`0xnavarro/IA-PARA-TODOS`](https://github.com/0xnavarro/IA-PARA-TODOS) | 11 470 B | 🔴 **11 471 B** | 🟢 yes |
| [`ClassroomIO/ClassroomIO`](https://github.com/ClassroomIO/ClassroomIO) | 34 522 B | 🔴 **34 523 B** | 🟢 yes |

🟡 Two further `OFF_BY_ONE` rows are **withheld**, not published: `Ebimsv/AITutorAgent`, whose shelf
text in fact reads `1 072 B` — equal to the re-read, so the `1 071` my extractor paired with it came
off a multi-address line; and `GibbonEdu/core`, whose matched line is about `frappe/education`, so
the attribution cannot be confirmed. 🔵 A cell I cannot attribute is not a finding.

### 🟡 The five genuine disagreements — candidates for upstream drift, not for correction

| address | path | carried | re-read | δ |
|---|---|---|---|---|
| [`MysterionRise/adaptive-knowledge-graph`](https://github.com/MysterionRise/adaptive-knowledge-graph) | `LICENSE` | 1 520 B | 1 094 B | 🔴 **−426** |
| [`Django-CRM/Django-CRM`](https://github.com/Django-CRM/Django-CRM) | `LICENSE` | 1 069 B | 1 101 B | 🟡 **+32** |
| [`bncc-dev/bncc-dados`](https://github.com/bncc-dev/bncc-dados) | `LICENSE` | 1 073 B | 1 092 B | 🟡 **+19** |
| [`junit-team/junit4`](https://github.com/junit-team/junit4) | `LICENSE-junit.txt` | 11 374 B | 11 376 B | 🟡 **+2** |
| [`jagmarques/awesome-eu-ai-act`](https://github.com/jagmarques/awesome-eu-ai-act) | `LICENSE` | 7 047 B | 7 049 B | 🟡 **+2** |

🔵 A `+2` on an 11 KB Apache payload is the shape of a copyright-year edit; **−426 B** is not, and
`MysterionRise/adaptive-knowledge-graph` is the one row here that warrants a grant re-read rather
than a byte correction.

### 🔴 Four cuts of the extractor, and what each wrong cut would have published

🔴 **This is recorded in full because the failure mode is invisible without a control, and three
separate cuts of this instrument produced a fluent, specific, entirely wrong drift report.**

| cut | defect | phantom "drifts" | how it was caught |
|---|---|---|---|
| 🔴 1 | `(\d(?:SEP?\d{3})*)` — unanchored, separator **optional**: on `11 408 B` the engine skipped the leading digit and returned `1408` | **200 of 395**, in a telltale band of +10000 / +20000 / +30000 | 🟢 a hand-written control row asserting DeepTutor is **11 408 B** disagreed with the extracted `1 408` |
| 🔴 2 | negative lookbehind and mandatory separator added — but the separator class held only **spaces**: on `1,070 B` it matched `070` | **104**, all exactly +1000 / +11000 / +35000 | 🟢 `cat -A` on the raw shelf bytes showed the comma |
| 🔴 3 | comma added; one cell still failed | **1** | 🟢 an 8-value self-check: the shelf writes `**1.071 B**` with a **period** |
| 🟢 4 | all four separators; self-check gates the run | **0** | 🟢 8/8 self-check, then 361/394 `EXACT` |

🟢 **The finding underneath the bug, and it is why no earlier pass built this census: across 451
passes these shelves group thousands FOUR different ways** — U+202F narrow no-break space, plain
space, comma, and period. 🔴 Any single-separator reader silently truncates the other three **and
reports the truncation as upstream drift**. The extractor now carries all four and will not run at
all unless it reproduces eight cells read by hand, one for each separator form.

🔴 **A fifth defect, of a different kind: the path key is a basename.** `LICENSE` at the repository
root and `legacy_reference/LICENSE` on a vendored subtree collapse to one key, which paired
`krzysztofbury/librus-mcp`'s **35 149 B GPL-3.0 subtree** figure with its **1 071 B MIT root** cell
and reported a −34 078 B drift. 🟢 The root cell re-reads at **1 071 B `sha256₁₂ 22e7ab2dbddc`** —
byte-identical *and* hash-identical to what this base carries, and `p442`'s GPL-3.0 subtree finding
stands untouched. 🔵 **Four of the five withheld rows are this one defect**, so basename keying is
the single largest source of phantom drift in a census of this kind.

### 🟢 One foundational repository promoted — and it is reference DATA, not code

| repository | grant, read first-hand at `HEAD` | what it is | region |
|---|---|---|---|
| [`yasserstudio/geoalgeria`](https://github.com/yasserstudio/geoalgeria) | 🟢 **MIT** — `LICENSE` **1 101 B `sha256₁₂ 691e4ec845d7`**, title `MIT License`. 🔴 npm declares only `SEE LICENSE IN LICENSE`, so **the payload is the grant and the manifest is not** | A machine-readable registry of **Algeria's education estate**, published as scoped npm packages with GPS coordinates, contacts, capacity and boarding: 🟢 **11 858 schools** and kindergartens classified by cycle (primaire / CEM / lycée / préscolaire) from OpenStreetMap; 🟢 **1 932 vocational-training establishments** — 856 CFPA, 182 INSFP, 723 private accredited, 58 DFEPs — from **MFEP / takwin.dz**; 🟢 **177 higher-education institutions** — universities, grandes écoles, ENS, centres — with official sites, from **MESRS**. All **69 wilayas**. Trilingual `README` (EN / FR / AR). 10 versions, 2026-06-22 → 2026-10-21 | 🟢 **EMEA** — Algeria, asserted by the ministries it sources and the wilaya coverage |

🟢 **Why it belongs on a foundations shelf and not an agents shelf.** It executes nothing. It is the
layer every education engagement needs first and that this base has had almost nowhere: an
authoritative, permissively-licensed **master list of institutions** to key a deployment, a rollout
plan or a market sizing against. 🔵 **And it moves this base's EMEA coverage off Europe for the
first time** — the EMEA tier here has been Romania (`ase-moodle-mcp`), France, the Netherlands and
Germany; Algeria and the Maghreb were an unstated absence. 🔴 Stated plainly as `Gap 452-E`: the
*rest* of the Middle East and Africa remains absent, and this one address does not close it.

## 🆕 `p451` — **🟢 THE "CIRCULAR GRANT" THIS FILE HAS CARRIED SINCE `p390` IS NOW PROVED RATHER THAN INFERRED — and the proof makes it worse: npm's own record shows `beadkit` published TWO versions whose licence string names a file in a repository that no longer exists, so the grant is not merely unread, it is UNREADABLE BY ANYONE. 🔴 And a second address on this shelf tier turns out to have shipped FOUR `proprietary` versions before its last two went BSD-3-Clause.**

🔴 **`make hooks` was DENIED on this host this pass** (`Code from External`) — no cell below is
gate-attested. Stated first, per `Gap 446-A`. Six denials in seven passes.

### 🟢 `ale-alejandro/beadkit` — the circle closed, with dates

🔵 This file has recorded since `p390` that `beadkit`'s *"manifest reads `"SEE LICENSE IN LICENSE"`
— pointing at a file in a repository nobody can read"*, and `compose/patterns.md` carries it as the
worked example of the class. 🟢 **The registry record now supplies what the inference lacked:**

| measured 2026-10-26 | value |
|---|---|
| npm package | **`beadkit`**, **`0.1.0`** latest, **2** versions |
| window | **created 2026-08-26**, **last modified 2026-10-12** |
| maintainer | `alebuild.co` |
| `repository` back-link | 🟢 **`git+https://github.com/ale-alejandro/beadkit.git`** — the exact carried slug |
| declared licence | 🔴 **`SEE LICENSE IN LICENSE`** |
| the repository that holds `LICENSE` | 🔴 `404` on `raw`, `128` on `ls-remote`, byte-identical to a fabricated control |

🟢 **So the address was real** — a registry does not invent a back-link for 2 published versions —
🔴 **and the grant is unrecoverable on every channel this host has.** 🔴 **Not recommendable, and
for a stronger reason than "unverified": there is no longer any party able to verify it.** The
package is installable today; its licence is not knowable today. 🔵 For a Globant engagement that
is the worst of the three states — *available, attractive and unlicensable*.

### 🔴 `dev-cucei-itrans/siiau-api-client` — a licence that CHANGED mid-life, recoverable only from Packagist

🔵 [`verticals/solutions.md`](../verticals/solutions.md) has carried this address as the only SIS
integration SDK that ever existed for SIIAU, *"marked abandoned"* on Packagist. 🟢 **Read
first-hand this pass** (`packagist.org/packages/dev-cucei-itrans/siiau-api-client.json`, after the
positive control `laravel/framework` → `200`):

| version | published | licence as published |
|---|---|---|
| `v1.0.0-BETA` | 2023-10-20 | 🔴 **`proprietary`** |
| `v1.0.0` | 2023-10-23 | 🔴 **`proprietary`** |
| `v1.1.0` | 2024-08-13 | 🔴 **`proprietary`** |
| `v1.1.1` | 2024-08-14 | 🔴 **`proprietary`** |
| `v1.1.2` | 2024-08-25 | 🟢 **`BSD-3-Clause`** |
| `dev-main` | 2024-10-08 | 🟢 **`BSD-3-Clause`** |

🔵 Package created **2023-10-13**, **7** versions, **1 023** downloads, **7** stars recorded by
Packagist, `abandoned: true`. 🔴 **Four of seven published versions are `proprietary`**, and the
repository that could settle the intent is gone — **Packagist is now the only channel on which
this grant exists at all.**

🔴 **The consequence is a pinning rule, not a footnote:** a composer constraint such as `^1.0`
resolves into the **proprietary** band. 🟢 **Only `v1.1.2` or later is BSD-3-Clause**, and because
the repository is withdrawn, that boundary can never be re-read from source. 🔵 Any engagement
touching SIIAU must pin `>=1.1.2` **and** carry the Packagist record as its grant evidence, or
have no grant at all.

### 🟢 The classification this shelf tier gains: licence RECOVERABILITY, independent of licence

🔵 These shelves grade *what* a licence is. 🔴 **Six withdrawn addresses this pass show that is one
axis short** — a grant can be permissive and still unusable because nothing can serve its text:

| recoverability class | n (of the 6 withdrawn) | instances |
|---|---|---|
| 🟢 **Registry-recoverable** — a registry declares an SPDX identifier | **3** | `interactive-quiz-kit` (MIT) · `unist-blackboard-mcp` (MIT) · `GraphLMS` (MIT) |
| 🟡 **Manifest-only** — identifier declared, no payload ever shipped | **1** | `santillana-ai/tutor-sdk` (MIT in `@santillana-ai/create-tutor-app`, no payload in the tarball) |
| 🔴 **Version-dependent** — the identifier changes across published versions | **1** | `siiau-api-client` (`proprietary` → `BSD-3-Clause` at `v1.1.2`) |
| 🔴 **Unrecoverable** — the declaration points at a file nobody can serve | **1** | `beadkit` (`SEE LICENSE IN LICENSE`) |

🟢 **Only the first class is buildable on without a legal review**, and it is 3 of 6. 🔵 That ratio
is the reason this axis is worth carrying: *"MIT"* on a withdrawn address is three different
situations, and two of them are not a grant.

---

## 🆕 `p450` — **🔴 A ONE-PATH README PROBE WOULD HAVE CONDEMNED FOUR OF THIS SHELF'S MOST IMPORTANT PLATFORMS AS DEAD — `openedx/edx-platform`, `oppia/oppia`, `overhangio/tutor` and `h5p/h5p-php-library` all serve 404 at `HEAD/README.md` while being entirely alive. 🟢 And a licence instrument written THIS PASS was caught misreading GPL-3.0 as LGPL on 2 of 15 reads, because GPLv3's own closing paragraph recommends the LGPL; it was fixed before publication and both readings are kept side by side.**

🔴 **`make hooks` was DENIED on this host this pass** (`Code from External`), so no cell below is
gate-attested. Stated first, per `Gap 446-A`.

### 🔴 The false-negative class a single-path probe publishes as dead — 19 of 375 addresses

`agents/top.md`'s `p450` section establishes the two-stage probe. This is the half that matters to
*this* file: **19 live addresses serve nothing at `HEAD/README.md`** and are recovered only by the
`ls-remote` escalation (`evidence/shelf-reachability-census.2026-10-26-p450.tsv`):

| address | 🟢 README path, MEASURED | default ref | 🔴 verdict a one-path `README.md` probe prints |
|---|---|---|---|
| [openedx/edx-platform](https://github.com/openedx/edx-platform) | **`README.rst`** | `master` (294 heads) | 🔴 **DEAD** — the reference Open edX platform |
| [overhangio/tutor](https://github.com/overhangio/tutor) | **`README.rst`** | 🔴 **`release`** (17 heads) | 🔴 **DEAD** — the canonical Open edX deployer |
| [openedx/XBlock](https://github.com/openedx/XBlock) · [openedx/edx-ora2](https://github.com/openedx/edx-ora2) · [openedx/xblock-lti-consumer](https://github.com/openedx/xblock-lti-consumer) · [openedx/openedx-ai-extensions](https://github.com/openedx/openedx-ai-extensions) | **`README.rst`** ×4 | `master` ×3, `main` ×1 | 🔴 **DEAD ×4** — the whole XBlock extension surface, incl. ORA2 (open response assessment) |
| [raccoongang/openedx-ai-extensions](https://github.com/raccoongang/openedx-ai-extensions) · [aulasneo/tutor-contrib-let](https://github.com/aulasneo/tutor-contrib-let) | **`README.rst`** ×2 | `main` ×2 | 🔴 **DEAD ×2** — the EMEA and LATAM Open edX integrators |
| [inducer/relate](https://github.com/inducer/relate) · [dmitry-viskov/pylti1.3](https://github.com/dmitry-viskov/pylti1.3) | **`README.rst`** ×2 | `main`, `master` | 🔴 **DEAD ×2** — incl. the LTI 1.3 Python library, MIT, first-hand read this pass |
| [h5p/h5p-php-library](https://github.com/h5p/h5p-php-library) | 🟡 **`README.txt`** | `master` (60 heads) | 🔴 **DEAD** — embedded in nearly every LMS |
| [projectfedena/fedena](https://github.com/projectfedena/fedena) | 🟡 **`README.markdown`** | `master` | 🔴 **DEAD** — the open SIS of the India/APAC shelf |
| [anastasasenov/bbmcps](https://github.com/anastasasenov/bbmcps) · [arthtyagi/judge](https://github.com/arthtyagi/judge) · [ivmelo/suapbot](https://github.com/ivmelo/suapbot) · [juan-c-cardenas/sia-scraper](https://github.com/juan-c-cardenas/sia-scraper) | 🔴 **`readme.md`** — lowercase ×4 | `main` ×1, `master` ×3 | 🔴 **DEAD ×4** — and this is `Gap 449-B`'s case-sensitivity class, now MEASURED rather than asserted |
| [oppia/oppia](https://github.com/oppia/oppia) | 🔴 **none at 10 probed paths** | 🔴 **`develop`** (500 heads) | 🔴 **DEAD** — Apache-2.0, grant read first-hand this pass |
| [cran/catR](https://github.com/cran/catR) · [Seechange-edu/act-ai-tutor-backend](https://github.com/Seechange-edu/act-ai-tutor-backend) | 🔴 **none at 10 probed paths** | `master`, `main` | 🟡 live, and genuinely without a root README |

🟢 **Measured distribution of the 19 — this is the finding, not the anecdotes.** README path:
**`.rst` 10**, lowercase **`readme.md` 4**, none-at-10-paths **3**, `README.txt` **1**,
`README.markdown` **1**. Default ref: **`master` 11, `main` 5, `develop` 1, `release` 1** — 🔴 **only
5 of 19 are on `main`**, and two of the most consequential addresses on this shelf default to
`develop` (Oppia) and `release` (Tutor).

🔴 **Four of the nineteen are pure case collisions**, which settles the open half of `Gap 449-B`
with a number: `raw.githubusercontent.com` is **case-sensitive on the path** while GitHub's web UI
is not, so `readme.md` is invisible to a `README.md` probe. 🟢 That is **21 % of this file's
false-negative class** caused by one character of case.

🟡 **`Gap 420-B`'s mechanism, answered for ONE of its four cases and explicitly not the others.**
`Gap 420-B` asked why four refs that `ls-remote` lists serve nothing on `raw` at *"nine common
control paths"*. 🟢 **For `projectfedena/fedena` the mechanism is now named: its root README is
`README.markdown`**, an extension outside any nine-path control set — so the absence was the
probe's, not the repository's. 🔴 **The other three are NOT answered here and the difference is the
ref.** `Gap 420-B` probed *non-default* refs (`gh-pages`, `Version_8.0`,
`projectfedena-patch-1`, a feature branch); this pass probed **`HEAD` only**. For
`Seechange-edu/act-ai-tutor-backend` even `HEAD` serves nothing at ten paths, so that case is
reproduced and still unexplained. 🔵 The empty-orphan-vs-LFS question stays open; what is now
closed is the assumption that a nine-path control set is exhaustive. 🟢 **The general mechanism is
stated as a rule: `raw` is a PATH server, not a repository server** — it resolves
`{ref}/{exact-cased-path}` and nothing else, so the README's extension, its case, and the default
ref are three independent variables and a probe that fixes all three measures none of them.

🔴 **Consequence for the standing protocol, stated as a rule:** a 404 at one path is **never** a
reachability verdict on this shelf, because **1 in 20 live addresses here fails it** — and the
failures are concentrated in the platform tier, not the long tail. `T104`'s finding that *"a grant's
PATH is a function of the REF"* has a sibling: **a README's path is a function of the ecosystem.**

### 🟢 Fifteen grants re-read first-hand — and the instrument was wrong before it was right

Read through the `raw` channel at seven candidate paths each, **2026-10-26**
(`evidence/licence-title-anchored.2026-10-26-p450.tsv`, both classifiers kept side by side):

| repo | grant path | 🟢 family *(title-anchored)* | bytes |
|---|---|---|---|
| [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | `LICENSE` | 🟢 **Apache-2.0** | 11 408 |
| [oppia/oppia](https://github.com/oppia/oppia) | `LICENSE` | 🟢 **Apache-2.0** | 11 358 |
| [1EdTech/lti-1-3-php-library](https://github.com/1EdTech/lti-1-3-php-library) | `LICENSE` | 🟢 **Apache-2.0** | 11 343 |
| [satvik314/educhain](https://github.com/satvik314/educhain) | `LICENSE` | 🟢 **MIT** | 1 092 |
| [CAHLR/OATutor](https://github.com/CAHLR/OATutor) | `LICENSE` | 🟢 **MIT** | 1 105 |
| [CAHLR/pyBKT](https://github.com/CAHLR/pyBKT) | `LICENSE` | 🟢 **MIT** | 1 132 |
| [learningequality/kolibri](https://github.com/learningequality/kolibri) | `LICENSE` | 🟢 **MIT** | 1 097 |
| [vishalsachdev/canvas-mcp](https://github.com/vishalsachdev/canvas-mcp) | `LICENSE` | 🟢 **MIT** | 1 071 |
| [dmitry-viskov/pylti1.3](https://github.com/dmitry-viskov/pylti1.3) | `LICENSE` | 🟢 **MIT** | 1 070 |
| [Submitty/Submitty](https://github.com/Submitty/Submitty) | `LICENSE.md` | 🟢 **BSD** | 1 542 |
| [moodle/moodle](https://github.com/moodle/moodle) | `COPYING.txt` | 🔴 **GPL-3.0** | 35 147 |
| [h5p/h5p-php-library](https://github.com/h5p/h5p-php-library) | `LICENSE.txt` | 🔴 **GPL-3.0** | 35 146 |
| [openedx/edx-platform](https://github.com/openedx/edx-platform) | `LICENSE` | 🔴 **AGPL-3.0** | 35 136 |
| [overhangio/tutor](https://github.com/overhangio/tutor) | `LICENSE.txt` | 🔴 **AGPL-3.0** | 34 523 |
| [UCL-INGI/INGInious](https://github.com/UCL-INGI/INGInious) | `LICENSE` | 🔴 **AGPL-3.0** | 34 764 |

🔴 **The defect, declared because it was the instrument's and it nearly reached a table.** A
whole-body `grep -i "GNU LESSER"` classifier returned **LGPL** for `moodle/moodle` and
`h5p/h5p-php-library`. Both are **GPL-3.0**. The cause is in the licence text itself: GPLv3's
closing *"How to Apply"* paragraph reads *"…if your program is a subroutine library… use the GNU
Lesser General Public License instead of this License"*, so **every GPLv3 file matches an LGPL
whole-body grep.** 🟢 **Fix: anchor the family to the first six non-blank lines — the title — and
test LESSER before GENERAL.** 2 of 15 reads flipped; 13 were unaffected.

🟢 **Two independent confirmations fall out of the corrected read.** `moodle/moodle`'s grant is at
**`COPYING.txt`**, exactly where `T104` placed it, at **35 147 B**. And `h5p/h5p-php-library`'s
`LICENSE.txt` carries **the same GPLv3 text at 35 146 B — one byte short of Moodle's, the trailing
newline being the whole difference** — which corroborates
this file's line 954 (*"routinely described as MIT; it is not"*) on a channel that pass did not use.
🔵 That carried row is **confirmed, not amended**; the contradicting row lives in
`verticals/solutions.md` and is fixed there this pass.

### 🔴 A SECOND instrument defect, caught the same way, and it is the one that would have looked like drift

🔴 **Every byte count in the table above was one short on first measurement.** Reading a payload
through shell command substitution (`$(curl …)`) **strips the trailing newline**, so any grant file
ending in `\n` measured one byte under its true length. 🟢 **Fix: take the length from the transfer,
not from the captured string** — `curl -w '%{size_download}'`. 🔴 **The defect is silent and
selective**: `Ed-Fi-ODS`'s `LICENSE.txt` has **no** trailing newline, so it measured **10 172 B**
both ways and looked like a confirmation that the method was sound.

🟢 **The corrected method reproduces three cells this base published on earlier passes, to the
digit** — which is the test that matters under `gate-cell-reproduction`:

| cell | carried on these shelves | 🟢 `p450` authoritative re-read |
|---|---|---|
| `HKUDS/DeepTutor` `LICENSE` | **11 408 B** *(`repos/foundations.md`)* | 🟢 **11 408** — EXACT |
| `learningequality/kolibri` `LICENSE` | **1 097 B** | 🟢 **1 097** — EXACT |
| `Ed-Fi-Alliance-OSS/Ed-Fi-ODS` `LICENSE.txt` | **10 172 B** *(reproduced by `p449`)* | 🟢 **10 172** — EXACT |

🔴 **Had the uncorrected numbers been published, all three would have read one byte low** and a
future pass would have recorded drift on cells that never moved — a fabricated finding on a real
gate. 🔵 **Rule for any pass that measures a payload: the length is a property of the transfer, and
a string that has been through a shell is not the payload.** 🟢 The full GPL-3.0 text on these
shelves is **35 147 B** (Moodle `COPYING.txt`, Chamilo root `LICENSE`), which the corrected method
now agrees with.
## 🆕 `p449` — **🟢 TWO PUBLISHED PAYLOAD CELLS REPRODUCE TO THE DIGIT ON AN INDEPENDENT FETCH, including `p448`'s North American headline: `Ed-Fi-ODS` at 10 172 B and `XBlock` at 11 358 B. 🔴 But the probe that read them is case-sensitive and returned THREE false 404s against a live row first — and the probe this base is instructed to use (`curl -sI`) returns 403 on EVERY real GitHub repo on this host.**

🟢 **Gate posture, stated first as `Gap 446-A` requires: `make hooks` RAN** — fourth trial after
three denials, so `p448`'s settlement of that gap as *"a property of the host class"* is
**refuted**; the denial is **intermittent**. 🟢 Arrival baseline: **58/62 green, 4 RED**, 🔴 **two
of them NEW and both `p448`'s**. Three green on exit; the fourth is `DECLARED_RED` and left
(`Gap 449-D`).

### 🟢 Cell reproduction — the two most load-bearing grants on these shelves, re-read first-hand

| address | cell this shelf records | 🟢 `p449` independent fetch | verdict |
|---|---|---|---|
| [`Ed-Fi-Alliance-OSS/Ed-Fi-ODS`](https://github.com/Ed-Fi-Alliance-OSS/Ed-Fi-ODS) | Apache-2.0 · `LICENSE.txt` **10 172 B** | 🟢 **200 / 10 172 B** | 🟢 **EXACT** |
| [`openedx/XBlock`](https://github.com/openedx/XBlock) | Apache-2.0 · `LICENSE.TXT` **11 358 B** | 🟢 **200 / 11 358 B** | 🟢 **EXACT** |

🔵 `Ed-Fi-ODS` is `p448`'s headline — **the only permissively-licensed system of record on these
shelves**, reached through a state-shaped NA leg after six region-level nils. 🟢 It is now
double-sourced across two passes and two hosts. Nine further shelved rows returned `200` with
byte sizes in the same sweep; none is contradicted.

### 🔴 `Gap 449-A` — the prescribed probe cannot verify a single row on this host

| probe | real repo | fake control | usable? |
|---|---|---|---|
| `curl -sI https://github.com/<slug>` | 🔴 **403** | — | 🔴 **NO** |
| `curl -s -r 0-200 https://github.com/<slug>` | 🔴 **403** | — | 🔴 **NO** |
| `curl -s https://api.github.com/repos/<slug>` | — | 🔴 **403** | 🔴 **cannot discriminate** |
| 🟢 `curl -s https://raw.githubusercontent.com/<slug>/<branch>/<path>` | 🟢 **200** + bytes | 🟢 **404 / 14 B** | 🟢 **YES** |

🔴 `github.com` HTML is 403 for **every** real repository here while `git clone` of the same
address succeeds. Obeyed literally, *"verify every URL with `curl -sI`; a 404 is not a finding"*
would condemn **all ~134 addresses this base has shelved.** 🟢 The sound probe needs a **negative
control**, and it has one: `zzz-fake-org-p449/zzz-fake-repo` → `404 / 14 B`
(`evidence/url-probe-soundness.2026-10-26-p449.tsv`).

### 🔴 `Gap 449-B` — and it failed toward "dead row" three times before it succeeded, on a row that was never dead

`openedx/XBlock` read **404** at `master/LICENSE.txt`, `main/LICENSE.txt` and `main/LICENSE`.
🟢 This shelf records `LICENSE.`**`TXT`** — at that exact case, **200 / 11 358 B**. 🔴
`raw.githubusercontent.com` is **case-sensitive**: normalising case **manufactures** dead rows,
and this base has a `LICENSE.TXT`/`License.txt`/`LICENSE` mix across its rows. 🔵 Rule:
**probe the case the shelf recorded; a 404 against a shelved cell is a probe finding until the
case is re-checked.** The same instrument-defect direction `Trend 48` named — toward the answer
already believed, which here is *"the row is stale"*.

### 🔴 Zero new foundational rows, and the nil is reported with its interval attached

Four global legs returned only shelved addresses (`os-taxonomy` 10 word-scoped files, `Ed-Fi` 10,
`OpenEduCat` 10). 🔵 Per `Gap 448-A`, now answered: the schedule is **hourly** (median
**61.1 min**, n=309) against a **daily** trending channel, so an unchanged channel is expected at
**P ≈ 95.8 %** and this nil is **not** evidence about supply.

---

## 🆕 `p448` — **🟢 THE NORTH AMERICAN SYSTEM OF RECORD HAS A GRANT, AND IT IS APACHE-2.0: `Ed-Fi-ODS` read first-hand at `LICENSE.txt` 10 172 B · `59899c6091b5`, reached through the state channel that six consecutive region-level NA legs failed to find. 🟢 `openSIS`'s below-root grant REPRODUCES to the digit. 🔴 Gate DENIED, third consecutive pass.**

🔴 **Gate posture: `make hooks` DENIED** (`Gap 446-A`, third consecutive pass, third container).
Nothing below is gate-checked; every cell carries its command.

### 🟢 A new foundational row, and it is the one `Gap 447-D` was blocking

🔵 Texas's TEA has **mandated** that student-information vendors submit to TSDS through **API
transactions** built on TEDS, and TEDS is *"a collection of data standards based on the national
**Ed-Fi** core"* — so the NA state system of record **is** an Ed-Fi deployment. That makes
`Ed-Fi-ODS` a foundations row rather than an integration curiosity. Grant read this hour over
the `raw.githubusercontent.com` channel (the one channel `Gap 446-D` shows returns **200**):

| repo | grant path | bytes | `sha256`[:12] | licence | verdict |
|---|---|---|---|---|---|
| [`Ed-Fi-Alliance-OSS/Ed-Fi-ODS`](https://github.com/Ed-Fi-Alliance-OSS/Ed-Fi-ODS) | `LICENSE.txt` | **10 172** | `59899c6091b5` | 🟢 **Apache-2.0** | 🟢 **GRANT-PRESENT**, HEAD `4d626f9ab257` |
| same | `NOTICES.md` | **233 924** | `609e95c99d9b` | third-party notices | 🟡 a 234 kB notices file is a **dependency-closure obligation**, not a blocker |
| [`Ed-Fi-Alliance-OSS/Ed-Fi-ODS-Implementation`](https://github.com/Ed-Fi-Alliance-OSS/Ed-Fi-ODS-Implementation) | — | — | — | — | 🟢 reachable, HEAD `b6b72e594bc4` |

🟢 **Why this row is worth more than its licence line.** Every other system-of-record row on
these shelves is either copyleft (`SIGAA` GPL-3.0, `suapbot` AGPL-3.0, `openSIS` GPL-2.0,
`RosarioSIS` GPL-2.0) or carries **no grant at all** (`sia-unal-mcp`). 🟢 `Ed-Fi-ODS` is the
**first permissively-licensed system of record on this shelf** — and it is the one a US state
*requires* its vendors to speak to. 🔵 That is a **vendor-and-build** row, not a
read-and-reimplement row.

🟡 **Bounded, and the bound is named:** the 234 kB `NOTICES.md` means an Ed-Fi-derived
deliverable owes a dependency-closure pass before it ships
(`compose/code/dependency-licence-closure` is the existing instrument). Apache-2.0 at the root
does **not** clear the tree — that is `Trend 40`'s whole point.

### 🟢 `openSIS`'s below-root grant reproduces, and the absence re-enumerates

`p4xx` published `openSIS Classic`'s grant at `docs/License.txt` · **17 286 B** ·
`224ac3d403e3` · GPL-2.0. Re-read this hour, independently:

| check | result |
|---|---|
| `docs/License.txt` payload | 🟢 **17 286 B · `224ac3d403e3`** — reproduces the published cell **to the digit** |
| first line | `GNU GENERAL PUBLIC LICENSE` |
| root grant paths probed | 🔴 **9 of 9 return 404** (`LICENSE`, `LICENSE.md`, `LICENSE.txt`, `COPYING`, `COPYING.txt`, `license`, `license.txt`, `LICENCE`, `Licence.txt`) |
| README's own statement | *"openSIS is an Open Source Project licensed under the GNU General Public License"*, pointing at `docs/License.txt` |

🟢 **`ABSENCE-ENUMERATED` at root, `GRANT-PRESENT` below it** — a second, independent
confirmation of `Trend 40` (*the second grant lives below the root*), and a validation of the
raw-channel + `sha256`[:12] method **against an already-published cell** before any new cell
was written this pass.

### 🟢 Pinned rows on this shelf: all four HELD

| row | published pin | live HEAD | verdict |
|---|---|---|---|
| [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) | `d073ad444fe5` | `d073ad444fe5` | 🟢 **HELD** |
| [`frappe/lms`](https://github.com/frappe/lms) | `5d6df8e3ed8e` | `5d6df8e3ed8e` | 🟢 **HELD** |
| [`withmarbleapp/os-taxonomy`](https://github.com/withmarbleapp/os-taxonomy) | `7bd8b6794cb7` | `7bd8b6794cb7` | 🟢 **HELD** |
| [`GeminiLight/awesome-ai-llm4education`](https://github.com/GeminiLight/awesome-ai-llm4education) | `48f2d16ca617` | `48f2d16ca617` | 🟢 **HELD** |

🔴 **But do not read that 4-of-4 as reassurance, because this pass measured what it is worth.**
Those pins are **43 minutes** old (`p447` committed 00:58:40Z, `p448` read 01:41:58Z). Over the
proper denominator — **496** simulated pinnings across **36** of these repositories — only
**67.3 %** of pins survive 24 h. 🔴 `p447`'s published budget line (*"17 of 18 of this base's
pins survived 24 h, so this is a cheap minority repair"*) is **survivorship-biased** and is
corrected in `Pattern BA`. 🟢 The predictor that actually works, and the one to apply before
putting any row below into a client deliverable, is **age of the commit at the moment you pin
it**: ≥ 7 days → **97.4 %** survival; < 7 days → **48.9 %**.

🔵 **Instrument validation for that claim, against a cell this base already published:**
`Apomera/AlloFlow`'s two refs date to `2026-10-24T12:35:30-04:00` and
`2026-10-25T18:50:44-04:00` — reproducing `p447`'s published *"pinned 10-24 12:35 with HEAD at
10-25 18:50"* **to the minute**.

---

## 🆕 `p447` — **🔴 Gate posture: DENIED, no baseline (`Gap 446-A`). 🟢 No foundational repo changes grant this pass, and that is a MEASURED statement rather than an unexamined one: every pinned row on this shelf was re-resolved against its live HEAD, and the single mover's licence payload is byte-identical across the move.**

🟢 **Every pinned row on the three sell shelves was re-resolved this hour** —
`git ls-remote <slug> HEAD`, 18 line-scoped rows, no GitHub API (403 here). **17 of 18 pins are
still exact.** The foundations rows specifically (`OpenOLAT/OpenOLAT` `d073ad444fe5`,
`frappe/lms` `5d6df8e3ed8e`, `withmarbleapp/os-taxonomy` `7bd8b6794cb7`,
`GeminiLight/awesome-ai-llm4education` `48f2d16ca617`) are **all unchanged**.

🟢 **The one mover is not a foundations row, and its grant did not move:** `Apomera/AlloFlow`
`LICENSE` is **35 442 B · `698099632698`** at both refs. 🔵 Which means **no grant on this shelf
requires re-grading this pass** — stated as a measurement with its instrument, not as silence.

🔴 **What this shelf still cannot do, and it is worth naming here rather than only in the gap
register:** `make hooks` has now been **denied on two consecutive passes**, so none of the
above is gate-checked. 🟢 The mitigation is the one `Gap 446-A` prescribes — every cell is
published with the command that produced it, and the hash method (`sha256` first 12 over raw
bytes) was validated against an already-published cell (`p433`'s `698099632698`) **before** any
new cell was written.

🔴 **Discovery added nothing.** `OpenOLAT`, `sakaiproject/sakai`, `openeducat/openeducat_erp`
and `francoisjacquet/rosariosis` all re-returned from the global platform leg; **all four are
already on this shelf**. Second consecutive saturated hour.

---

## 🆕 `p446` — **🟢 An upstream this base has audited twice has now published its OWN provenance review, and it is first-hand readable: `krzysztofbury/librus-mcp` ships a 9 662 B `LICENSE_REVIEW.md` that confirms `p442`'s GPL-3.0 subtree finding from the other side — and names a THIRD lane this base did not have, in which the MIT grant does NOT hold**

🔵 **How this was found.** Not by a search leg. `p446` re-measured a published payload cell to
validate its own hashing method (`agents/top.md` `p446`), and the licence-path enumeration over
the live tree returned **three** paths where `p442` recorded two:

```
LICENSE                     1 071 B · 22e7ab2dbddc   MIT          (reproduces p442)
legacy_reference/LICENSE   35 149 B · 3972dc9744f6   GPL-3.0-only (reproduces p442)
LICENSE_REVIEW.md           9 662 B · 6905cca1f0b4   🆕 NEW — a provenance review
```

🟢 **`p442`'s two cells reproduce to the digit** from an independent blobless clone this hour,
which is the strongest confirmation this base has of its own subtree instrument.

### 🟢 What the upstream says, in its own words, and why it matters commercially

| what the review states | first-hand quote | consequence for an engagement |
|---|---|---|
| the GPL subtree is deliberate and quarantined | *"Original 1.x source … preserved under the original GPL-3.0-only license. **Excluded from every 2.0 build inventory.** No relicensing or runtime fallback."* | 🟢 **Installing the published wheel/sdist does not pull GPL-3.0.** `p442` could only say *"a tree copy carries it"*; this says the **distributed artefact is clean** |
| the licence HISTORY is non-monotone | *"The root originally used MIT, then switched to GPL-3.0-only in `1a59c56` because apix's distributed license contradicted its MIT package metadata."* | 🔴 **MIT → GPL-3.0 → MIT on one root path.** A single-cell read at any one commit is right about that commit and wrong about the project |
| 🔴 **a flattened bundle is NOT approved** | *"This review approves the independent MCP distributions and ordinary separate dependency installation, **not an all-MIT standalone bundle**. Anyone bundling the whole installed environment … must review their additional notices, LGPL source/relinking obligations and resource terms separately."* | 🔴 **This is the lane an engagement actually ships** — one container image, one PyInstaller binary, one vendored wheelhouse |
| the named hazard in that lane is `lxml` | *"Its binary wheels can bundle zlib (zlib license), **iconv (LGPL-2.1)**, libxml2, libxslt and libexslt (MIT) … Some schema-transformation resources are described as **unlicensed** in the upstream notice."* | 🔴 **LGPL-2.1 relinking obligations and an unlicensed resource set** arrive inside a wheel nobody reads |

### 🔴 The third lane, stated plainly, because this base has been publishing two

| lane | grant status | who does this |
|---|---|---|
| integrate over the MCP interface, process boundary | 🟢 MIT holds | the disposition `p442` published |
| `git clone` and vendor the tree | 🔴 GPL-3.0-only arrives at `legacy_reference/` | the hazard `p442` named |
| 🆕 **`pip install`, then flatten the environment into one shipped artefact** | 🔴 **outside the upstream's own approval**; LGPL-2.1 + unlicensed resources via `lxml` | 🔴 **the default delivery shape of a studio engagement** |

🟢 **Prescription, and it is cheap:** the MIT lane survives a container **if** the dependency
distributions keep their own licence files inside the image and are not relinked or
repackaged — which is the ordinary `pip install` layout, and breaks the moment anyone runs a
single-binary packer. 🔵 Put that sentence in the engagement's build review, not in its legal
review, because the thing that violates it is a `Dockerfile` optimisation.

### 🟢 Why this is a foundations finding and not an agents one

🔵 `librus-python-api` (MIT, on this file) is the dependency the review is *about*: the pin moved
`1.0.2 → 1.6.2 → 1.6.3` across **2026-10-09 / -19 / -22**, each step with its PyPI licence
expression re-inspected by the upstream and recorded with a date. 🟢 **That is a maintained
licence-provenance trail on a foundational dependency — the artefact this base asks engagements
to produce, published by a single-maintainer project.** It is the reference implementation of
`Pattern AX`'s per-platform licence probe, done by the supplier instead of the consumer, and it
is worth citing as such.

🔴 **One limit, stated:** the review is the upstream's own engineering inventory and says so
(*"not legal advice"*). It is **evidence of diligence**, not a warranty, and the 35 149 B
GPL-3.0 payload is still physically in the tree.


## 🆕 `p445` — **Three new SIGAA addresses, and all three land in the COPYLEFT tier — so the Brazilian system-of-record integration layer is now known to be real supply that cannot be vendored. 🔴 Zero permissive rows added, and the reason is measured: the mandated discovery legs returned 0 new addresses from 14 candidates**

🔵 **Where these came from.** `Gap 444-B` named three unrun legs — a Peruvian university's
**system-of-record** noun, a UdelaR platform noun for Uruguay, and Mexico beyond UANL. All
three were run. Mexico returned one address and it is **deleted**; Uruguay and Peru returned
nothing; and the **SIGAA** channel `p443` opened returned three addresses nobody here had
seen. Mechanism, the two nils and the saturation measurement:
[`repos/trending.md`](trending.md) `p445`.

### 🟡 Copyleft and current-enough to read — integrate over the interface, never vendor

Every cell read first-hand on **2026-10-25**: existence and real default ref via
`git ls-remote --symref`, **every** grant path via `git ls-tree -r` over a blobless shallow
clone, every payload measured from the file (so `P834`'s trailing-newline run is in the byte
count). Driver: `compose/code/p445-publisher-class-census/probe_tranche.sh`. Evidence:
[`evidence/verified-repos.2026-10-25-p445.tsv`](../evidence/verified-repos.2026-10-25-p445.tsv).

| Repo | Licence | HEAD | Payload | Region | Why it is here, and the bound on using it |
|---|---|---|---|---|---|
| [`fernandobrito/cursos_ufpb`](https://github.com/fernandobrito/cursos_ufpb) | 🟡 **GPL-3.0** | `cbdcf32a9188` · 2017-01-26 · 168 files | `LICENSE` 35 141 B · `589ed823e9a8` | **LATAM** (Brazil) | The **largest and most API-shaped** of the three: a Rails app that parses UFPB's **SIGAA** and exposes curriculum data at `/api/curricula`, via the author's own `sigaa_parser` gem. 🟢 The useful artefact is the **parser's logic and the endpoint shape**, which is what an engagement needs to rebuild. 🔴 GPL-3.0 reaches a distributed derivative, so this is a **read-and-reimplement** row |
| [`macielti/sigaa-cli`](https://github.com/macielti/sigaa-cli) | 🟡 **GPL-3.0** | `85b9a51f5603` · 2020-01-04 · 25 files | `LICENSE` 35 149 B · `3972dc9744f6` | **LATAM** (Brazil) | Python client/CLI that authenticates against **any** SIGAA instance by configurable base URL — so it is the **portable** one of the three rather than UFPB-specific. 🔴 Carries a registry defect worth knowing: its PyPI record's `license` field is **EMPTY** while the repository ships a complete GPL-3.0 payload, so every registry-reading scanner will report this strongly-copyleft package as unlicensed |
| [`fernandobrito/ufpb_sigaa_api_old`](https://github.com/fernandobrito/ufpb_sigaa_api_old) | 🟡 **GPL-3.0** | `4fa17f22c442` · 2016-02-07 · 14 files | `LICENSE` 35 141 B · `589ed823e9a8` | **LATAM** (Brazil) | Sinatra service over the same UFPB SIGAA curriculum data, self-described as dated and use-at-your-own-risk. 🔴 Ten years stale and superseded by the row above it. Shelved only as the **reference shape** for "SIGAA behind an HTTP API", never as a dependency |

🟢 **What the three together establish, which no single row does.** SIGAA — the system of
record at the Brazilian federal universities — **has** a public integration layer, in two
languages, with a working parser and a documented endpoint shape. 🔴 **And it is uniformly
GPL-3.0 and 6–10 years stale.** So the sellable shape at a Brazilian federal university is
*reimplement the parser against the interface these repositories document*, on a clean
permissive base, and the three rows above are **specification, not supply**. Recipe:
`Pattern AY`.

🔵 **This also sharpens `p444`'s correction of `Trend 42` rather than just agreeing with it.**
`p443` published *the student side of the glass is permissive, 6 of 8*; `p444` refuted it over
37 addresses (*permissive is 22 %, modal outcome is no licence*). This pass adds a third
reading: on **one platform, measured end to end, the student side is neither permissive nor
unlicensed — it is uniformly copyleft, 3 of 3.** The honest generalisation is that **the
licence distribution is a property of the PLATFORM's developer community, not of the side of
the glass**, which is `Trend 45`'s second half.

### 🔴 Zero permissive rows added, and the denominators are published rather than implied

| leg | candidates | 🟢 new to this base | permissive and new |
|---|---|---|---|
| 4 × mandated global English legs | 🔴 0 addresses returned | 🔴 **0** | 🔴 **0** |
| LMS MCP servers (Canvas + Moodle) | 10 | 🔴 **0** — all already here, up to **77** prior mentions | 🔴 **0** |
| SIGAA platform noun | 3 | 🟢 **3** | 🔴 **0** (all GPL-3.0) |
| SIIAU platform noun (Mexico) | 1 | 🔴 **0** — 🔴 `git ls-remote` **DOES NOT RESOLVE** | 🔴 **0** |
| UdelaR / `bedelías` noun (Uruguay) | 🔴 0 | 🔴 **0** | 🔴 **0** |
| Peru system-of-record noun | 🔴 0 | 🔴 **0** | 🔴 **0** |

🔵 **Read the top row before concluding the tier is saturated.** The ten MCP candidates were
not *rejected* — they were **already shelved**, several of them on this file and on
`agents/top.md`. Generic English discovery is exhausted for this base (`p443` got 1 of 29, this
pass got 0 of 10 on a differently-shaped query); the platform-noun channel is the one still
paying, and it has now paid on three consecutive passes.

---

## 🆕 `p444` — **The LATAM academic-portal tier triples, and two things the licence column alone would never have shown: 🔴 across the 37 addresses the PLATFORM-NAME legs returned, the permissive-and-maintained intersection is EXACTLY ONE — and 🟢 the best address of the pass came from a DIFFERENT leg shape entirely, which is the more useful finding**

🟢 **What was added and why it is small.** `p443` opened this tier with six Brazilian and
Argentine SIGAA/SIU-Guaraní addresses. `p444` ran the same channel at Mexico (SIASE), Brazil
(SUAP), Chile (U-Cursos, UCampus) and Colombia (SIA UNAL) and verified **37** addresses
first-hand. Eight carry a permissive grant. **Seven of those eight have not been touched since
2021.**

🔴 **The cross-tab is the finding, and no single column shows it.** Licence and recency,
measured over all 37 (`git log -1 --format=%cs` at the probed HEAD):

| grant | 🟢 live (HEAD 2026) | 🟡 2023–2025 | 🔴 dead (≤ 2022) | total |
|---|---|---|---|---|
| 🟢 **MIT / BSD** | 🟢 **1** | 1 | 🔴 **6** | 8 |
| GPL-3.0 | 2 | 3 | 4 | 9 |
| AGPL-3.0 | 0 | 0 | 2 | 2 |
| 🔴 **no grant at all** | 5 | 4 | 9 | 🔴 **18** |
| **total** | **8** | **8** | **21** | **37** |

🔵 **Read the top-left cell.** A screen on licence alone returns eight "build-on" addresses and
feels like a tier. A screen on licence **and** last commit returns **one**. This base has
screened on licence and stars for many passes; `p415` already measured stars as a weak positive
class, and this is the same lesson arriving through the recency axis. **Shelved below with the
true HEAD date in every row**, because a 2019 MIT scraper against a portal that has since
changed its HTML is not a starting point — it is a worked example.

### 🟢 The rows that are both permissive and current

🔵 **The second one is the methodological finding of this file.** `sia-unal-bridge` came from
the platform-name leg that `p443` prescribed. `django-auth-suap` came from a leg this pass ran
almost as an afterthought — the platform's **expanded name** (*"suap sistema unificado
administracao"*), asked to find whether the SUAP **platform itself** was open source. It is not;
but that leg returned **12 results of which 3 are production-grade**, and its best address is
better engineered than anything the bare-acronym leg found in four countries. **An ecosystem leg
and a name leg are not the same channel** (`Gap 444-E`).

| Repo | Licence | HEAD | Payload | Role in a build |
|---|---|---|---|---|
| 🟢 [django-by-kelsoncm/django-auth-suap](https://github.com/django-by-kelsoncm/django-auth-suap) | 🟢 **MIT** | `1f0b4e1a` · **2026-09-05** | `LICENSE.md` 1 065 B · `113d1a85e628` | 🟢 **LATAM — Brazil. The strongest LATAM address on these shelves, and the direct answer to this pass's IFRN finding.** Django **OAuth2 authentication backend for SUAP**, the Instituto Federal academic-management system — i.e. *the same job as `ifrn-oficial/cliente_suap_django`, which carries no grant at all*. 245 files: **98 `.py`, 92 `.rst` of Sphinx documentation**, published to **PyPI as `django-suap-auth`**, GitHub Actions CI + Codecov + pre-commit, `SECURITY.md`, bilingual PT-BR/EN README, declared support for **Django 5.2 and 6.0**, and an `audit/` submodule with middleware, migrations and an `audit_archive` management command. 🔵 This is the one row in the tranche that looks like a maintained library rather than a student utility, and it is the row an IFRN-network engagement should start from. |
| 🟢 [gabotachak/sia-unal-bridge](https://github.com/gabotachak/sia-unal-bridge) | 🟢 **MIT** | `c8c25ddaac12` · **2026-10-16** | `LICENSE` 1 085 B · `7521387e0869` | 🟢 **LATAM — Colombia.** JSON API over the SIA (Sistema de Información Académica) subject catalogue of the Universidad Nacional de Colombia. **301 files, Go (76) + TypeScript (42) + TSX (37)** — a deployed service with a front end, not a scraper script, and **the only address of the 37 platform-name hits that is simultaneously permissive and maintained**. Read first-hand 2026-10-25. |
| 🟢 [luizpicolo/suap_api](https://github.com/luizpicolo/suap_api) | 🟢 **MIT** | `718183f6` · 🟡 **2023-03-02** | `LICENSE.txt` 1 078 B · `798df9e7634a` | **LATAM — Brazil.** Ruby wrapper for the SUAP API, written against **IFMS** rather than IFRN — 🔵 the one address in the tranche that evidences the SUAP API is **shared across more than one Instituto Federal**, which is what makes a SUAP integration reusable beyond a single institution. 24 files. |

### 🟡 Permissive but stale — shelved as reference implementations, dated so nobody mistakes them

Each is a *worked example of the integration shape* for its platform, not a dependency to take.
🔴 **Every HEAD below predates 2025**; the portals they read have had five or more years to
change.

| Repo | Licence | HEAD | Payload | Role in a build |
|---|---|---|---|---|
| [Open-Source-eUdeC/UdeCursos-bot](https://github.com/Open-Source-eUdeC/UdeCursos-bot) | 🟢 **MIT** | `cab987ccd1a5` · 🟡 **2024-03-17** | `LICENSE` 1 074 B · `198619b5e4a3` | **LATAM — Chile.** Telegram bot over **UdeCursos**, Universidad de Concepción's course platform. 29 files, Python (18). The freshest permissive *agent-shaped* LATAM address: a working model of the notify-the-student pattern, 8 ★. |
| [ivmelo/suap-api-php](https://github.com/ivmelo/suap-api-php) | 🟢 **MIT** | `fc2a679fe78a` · 🔴 **2021-04-13** | `LICENSE` 1 071 B · `8dd4b842ad4d` | **LATAM — Brazil.** PHP wrapper for the **SUAP** API (Instituto Federal network). 34 ★ — the most-starred *licensed* SUAP address, and the licensed counterpart to IFRN's own unlicensed clients (see the publisher split in `agents/trending.md`). 7 files. |
| [Projeto-SIAC/suap-wrapper](https://github.com/Projeto-SIAC/suap-wrapper) | 🟢 **MIT** | `bfe75f6147c3` · 🔴 **2019-03-12** | `LICENSE` 1 061 B · `7d6794d36990` | **LATAM — Brazil.** JS wrapper for the SUAP API, 12 ★, 8 files. Second licensed SUAP read seam; useful as the Node-side shape where `suap-api-php` gives the PHP one. |
| [juan-c-cardenas/sia-scraper](https://github.com/juan-c-cardenas/sia-scraper) | 🟢 **MIT** | `e557dac6c26d` · 🔴 **2020-08-18** | `LICENSE` 1 085 B · `ca571ae2faa5` | **LATAM — Colombia.** SIA UNAL course-documentation scraper, 7 files, JS. The scrape-path counterpart to `sia-unal-bridge`'s API path, and the cheaper read when only the catalogue is needed. |
| [ramomar/siase-schedule-scraper](https://github.com/ramomar/siase-schedule-scraper) | 🟢 **MIT** | `d5713cf636d2` · 🔴 **2019-12-07** | `LICENSE` 1 077 B · `09c43d110fc7` | **LATAM — Mexico.** Timetable scraper for **SIASE** (UANL), JavaScript, 10 ★, 5 files. Smallest complete worked example of the SIASE read in the tranche. |
| [ramomar/uniswag-chrome](https://github.com/ramomar/uniswag-chrome) | 🟢 **MIT** | `c62306458f04` · 🔴 **2019-07-06** | `LICENSE` 1 070 B · `b36468e555d3` | **LATAM — Mexico.** SIASE integrated with Todoist and Google Drive as a Chrome extension, 21 files. 🔵 The only address in the tranche that pushes portal data **outward into a third-party productivity tool** — the shape an engagement is usually asked for, implemented once, in 2019. |
| [molguin92/UCampusViz](https://github.com/molguin92/UCampusViz) | 🟢 **BSD** · 1 514 B | `eabef308b7d8` · 🔴 **2019-01-16** | `LICENSE` 1 514 B · `3510752bf472` | **LATAM — Chile.** Course-prerequisite dependency graph for FCFM, Universidad de Chile. ⚠️ **Shelved with a caveat read from its own tree: 289 of its 297 files are `.html`** — it is a *generated artefact dump* with one `.py`, so it is evidence that the UCampus prerequisite graph is extractable, not a library to import. |

🔵 **Not promoted, and named so the absence is informed:** the 18 ungranted addresses
(`Gap 444-C`), among them an **MCP server** (`sebassg/sia-unal-mcp`, TypeScript, HEAD
2026-03-12) and **three official IFRN OAuth2 clients totalling 81 ★**. They are live, they are
relevant, and there is no right to use them. Every one is listed with its HEAD and grant state
in [`evidence/verified-repos.2026-10-25-p444.tsv`](../evidence/verified-repos.2026-10-25-p444.tsv).

---


# 🏗️ Foundational repos — Education

## 🆕 `p443` — **The tier grows by FIVE after six passes of zero, and not one of them came from a search this base had not already run. 🔴 They were in its own append-only record, unshelved, and invisible to the promotion ledger**

🟢 **The LATAM academic-portal integration tier.** Six consecutive passes wrote *"zero rows
added"* on this file while the shelf stood at **1 LATAM row of 8**. The addresses below close
that, and the discovery cost was one query: **the name of the platform the institutions
actually run**, sorted by stars, with no capability words added.

🔴 **Where they came from is the finding.** Five of the six were already written into
[`agents/trending.md`](../agents/trending.md) and [`trending.md`](trending.md) by earlier
passes and promoted by none; all six are `grep`-absent from
`evidence/promotion-ledger.2026-10-25-p436.tsv`. The measurement — **2 361** record addresses
absent from the ledger, **69** of its 219 rows already landed, so `PROMO_RATCHET = 148` counts
claims rather than findings — is `Gap 443-A`.

🔵 **Why these are foundations and not agents.** None of the five is an AI system. Each is the
**read seam** onto a national academic portal — the thing an agent has to call before it can
tutor, advise or chase a deadline. That is this file's job, and it is precisely how this base's
EMEA line began: `librus-python-api` sits here and `librus-mcp` sits on the agents shelf. The
agent-addressable half of this tranche (`jpmanson/siu-guarani-mcp`, MIT) is on
[`agents/top.md`](../agents/top.md) for the same reason.

🔴 **The licence frontier in LATAM, measured here for the first time, and it runs the wrong way
exactly as it does in EMEA:** of 8 academic-portal addresses **6 are permissive**; of the 4
institutional platforms that actually hold student records, **0 are** — GPL-2.0, GPL-3.0,
GPL-3.0, AGPL-3.0. 🟢 **So the foundation layer is buildable and the platform layer must be
integrated, never vendored.**

### 🟢 The five rows, read first-hand — tree-enumerated, file-measured

Grant paths from `git ls-tree -r` over a blobless clone (`p442`/`Pattern AU`), not a root
ladder; every payload fetched at the pinned SHA and measured from the file, so the
trailing-newline run is intact (`P834`). 🟢 **14 of 14** granted repositories in this tranche
carry **exactly one** own-grant path — no `librus-mcp`-style second grant anywhere in the arm.

| Repo | Licence | HEAD | Payload | Role in a build |
|---|---|---|---|---|
| [aquario-ufpb/aquario](https://github.com/aquario-ufpb/aquario) | **MIT** | `662a345962d2` | `LICENSE` 1 070 B · `ca675f365799` | **LATAM — Brazil.** UFPB's Computing Centre information hub: the largest and most active address in the tranche (86 ★, 948 files, HEAD **2026-10-21**). The one row here that is a *deployed institutional product* rather than a utility, so it is the reference for what a Brazilian federal-university front end is expected to contain. |
| [PucaVaz/sigaa-tools](https://github.com/PucaVaz/sigaa-tools) | **MIT** | `a5a86e0a9b28` | `LICENSE` 1 065 B · `75d9af3e2e90` | **LATAM — Brazil.** Python SIGAA tooling, 209 files, HEAD **2026-10-20** — 🟢 the **most recently maintained SIGAA read seam in existence**, which is what makes it the default starting point over the better-known archived API below. |
| [trindadetiago/sigaa-caiu](https://github.com/trindadetiago/sigaa-caiu) | **MIT** | `7373c6abac62` | `LICENSE` 1 071 B · `e69df76328c3` | **LATAM — Brazil.** SIGAA-derived study tooling, 48 files, HEAD **2026-09-02**. Live, small and readable — the cheapest row to fork when an engagement needs a bespoke SIGAA reader rather than a library. |
| [juliancasaburi/siu-guarani-promedio-extension](https://github.com/juliancasaburi/siu-guarani-promedio-extension) | **MIT** | `6962638adbdd` | `LICENSE` 1 073 B · `652d46c067d4` | **LATAM — Argentina.** Computes grade averages from a SIU Guaraní academic record (Chromium/Firefox). 🟢 Documents the **student-side** record layout, where `siu-guarani-mcp` covers the teaching-staff profile — together they span both SIU Guaraní personas. 🟡 HEAD **2025-07-08**: read the parsing, do not depend on the extension. |
| [GeovaneSchmitz/sigaa-api](https://github.com/GeovaneSchmitz/sigaa-api) | **MIT** | `a7aab3d605d7` | `LICENSE` 1 108 B · `ecb193695a94` | **LATAM — Brazil.** 🔴 **ARCHIVED by its owner on 2024-04-10 and read-only — shelved as a REFERENCE, never as a dependency**, and the README's own `ARQUIVAMENTO` section says so. Why it earns a row anyway: at 61 ★ / 23 forks / 247 commits / 232 files it is **the most complete SIGAA model that exists in the open** — classes, grades, absences, news, teacher search, class members, file downloads — and it is the only address here that states which instances it was tested against (**IFSC, IFFar, UFPB**). Read it to learn the portal; build on `sigaa-tools`. |

🔴 **One row in this tranche is deliberately NOT here.** `ipti/br.tag` — Brazil's live municipal
school-management platform — is on [`verticals/solutions.md`](../verticals/solutions.md)
instead, because its grant is **GPL-2.0** and because its **README states BSD-3-Clause**, a
two-channel conflict established first-hand at one commit and written up in
[`agents/trending.md`](../agents/trending.md) `p443`. 🔵 It is the sharpest argument on this
file for why a promotion test reads the payload and not the README: the README is the *more
permissive* of the two, which is the direction that costs a client money.

### 🔴 Refused in the same tranche, and the reason is recency, not licence

| repository | grant | HEAD | verdict |
|---|---|---|---|
| [luizpicolo/code](https://github.com/luizpicolo/code) | 🟢 MIT `1 074 B · a2874113b3b5` | 🔴 **2016-10-31** | Ten years cold |
| [rodrigmatrix/sigaa_ufc_android](https://github.com/rodrigmatrix/sigaa_ufc_android) | 🟢 Apache-2.0 `11 357 B · c71d239df917` | 🔴 **2021-03-19** | Permissive and dead |
| [ernestosrf/sigaa-horarios-extension](https://github.com/ernestosrf/sigaa-horarios-extension) | 🔴 **none in tree** (9 files) | 2025-07-23 | `REFUSED-UNGRANTED` |
| [Cristianojr9/sigaa-new-design](https://github.com/Cristianojr9/sigaa-new-design) | 🔴 **none in tree** (30 files) | 2020-08-20 | `REFUSED-UNGRANTED` |
| [G3-Devs/siu-auto-asistencia](https://github.com/G3-Devs/siu-auto-asistencia) | 🔴 **none in tree** (11 files) | 2026-04-18 | `REFUSED-UNGRANTED` |

🔵 **Two of the five were refused with a clean permissive grant in hand** — the
`davemckain/qtiworks` precedent on this file, and the right call both times. A licence-only
promotion test would have shelved them. 🟢 The three ungranted verdicts are from a **tree
enumeration**, not a root ladder, so they are absences of a grant *anywhere in the repository*.


## 🆕 `p442` — **Zero rows added, sixth pass running — and the tier's own cells were the finding: 5 of them did not reproduce, and one platform ships a 1 614 B POINTER beside its 35 147 B grant**

🔴 `p442` adds **no** foundation row. Its six new permissive addresses are **Agent Skills and
tutoring tools**, not things a deliverable vendors as a dependency; they are shelved on
`agents/top.md`. 🔵 The work this file got instead is **verification of what it already
sells**.

### 🔴 Five cells on this file were measured through a capture, and are repaired in this commit

All 162 payload cells across the three sell shelves were re-measured from the file and
through `lib/payload_measure.sh`'s preserved `P834` control. 🔴 **19 carried the capture
signature** — bytes short by the trailing-newline run, digest taken of the stripped bytes —
and **five of them are on this file**:

| row | published | 🟢 now |
|---|---|---|
| [`robotros/California-IEP-AI-project-kit`](https://github.com/robotros/California-IEP-AI-project-kit) | 1 064 B · `2524a8e74f10` | **1 065 B · `43554d1189d8`** |
| [`67tallchris/iep-builder`](https://github.com/67tallchris/iep-builder) | 1 068 B · `523f156051cf` | **1 069 B · `aa8cfde0dc31`** |
| [`dougdevitre/access-to-education`](https://github.com/dougdevitre/access-to-education) | 1 068 B · `68657618a157` | **1 069 B · `fc7c8b90fee1`** |
| [`ezixen/PlannedEducation`](https://github.com/ezixen/PlannedEducation) | 1 085 B · `4ec3cc564448` | **1 086 B · `53de23fdecc2`** |
| [`rwrife/rubric-desk`](https://github.com/rwrife/rubric-desk) | 1 062 B · `ec0b7dad19a4` | **1 063 B · `c186f5cb204a`** |

🟢 The grant itself was never in doubt for any of the five — MIT in every case, unchanged —
and that is the point worth taking: **a cell can be wrong in a way that does not change the
licence and still destroys the one thing a reader can check.**
`make gate-cell-reproduction` now holds it, and `lib/measure --cell` builds the string.

### 🔴 `chamilo/chamilo-lms` carries its grant TWICE, and one of the two is not a grant

Enumerating the tree (`Gap 441-A`'s fix, now in the shared library) returned two licence
paths for Chamilo: the root `LICENSE` — **35 147 B · `8ceb4b9ee5ad`**, the full GPL-3.0 this
file publishes — and **`license.txt`, 1 614 B · `0aaf39205490`**, which grades 🔴
`GRANT-BY-REFERENCE`: GPL-3.0 titled, **all six profiled clauses absent**, a URL in place of
the text.

🔵 **Nothing is wrong with the shelf row, and that is what makes this worth recording.** The
ladder in `lib/probe_payload.sh` emits `LICENSE` before `license.txt`, so it happened to land
on the complete text. 🔴 **The order of a hand-tuned filename list is the only thing that
stood between this file and publishing a 1 614 B pointer as Chamilo's grant** — and `p337`
already refuted that list's empirical basis by finding a real project whose only payload is a
**lowercase** `license.txt`. For a repository shaped like that one and licensed like this one,
the ladder picks the pointer.

## 🆕 `p440` — **Zero rows added, for the fourth pass running — and this time the screening question has an answer the previous three could not compute**

🔴 `p440` adds **no** foundation row. The pass's one new address,
[`AnkitClassicVision/tutor-engine`](https://github.com/AnkitClassicVision/tutor-engine),
is a self-hosted application under **AGPL-3.0**: nothing downstream can depend on it, and
network copyleft is the wrong grant to put in a tier whose whole purpose is *things a
deliverable may vendor*. It is shelved on `agents/top.md` with that posture attached.

### 🟢 The screening amendment: "can the grant be READ" is now answerable for copyleft too

`p439` added the screening question — 🔵 *before a dependency is shelved here, ask not
only which licence it names but whether the payload contains the words that perform the
grant.* 🔴 That question had a hole exactly where this file's risk is: `grant_presence.py`
carried profiles for **MIT, Apache-2.0 and ISC only**, so every GPL, AGPL, LGPL, BSD, MPL
and EPL payload returned `GRANT-UNCALIBRATED` — **101 of 218**. A foundation row under
GPL-2.0 could not be screened by the screening rule.

🟢 `p440` profiles the GPL family (AGPL-3.0, GPL-3.0, GPL-2.0), and the remainder falls to
**39 of 218**. For this file that means the 🔴 **Copyleft foundations** section below is
screenable for the first time, and the ten platform repositories behind it were read at
source this hour: **10 of 10 `GRANT-PRESENT`** (table on `verticals/solutions.md`).

🔵 **The amendment, stated so the next pass can apply it without re-deriving it:**

1. **Ask the grant question before the tier question.** A payload that names a family and
   does not contain its operative clauses is not a candidate for *any* tier — the row is
   `GRANT-TRUNCATED` or `GRANT-BY-REFERENCE`, and the obligation it names lands on
   whoever vendors it next. On this base's own corpus that is 🔴 **36 payloads**.
2. **Resolve the version before judging a GPL-family grant.** A complete GPL-2.0 licence
   is missing four of GPL-3.0's six operative clauses. Grading it against the wrong
   version condemns a valid grant — and the three GPL-2.0 platforms on these shelves
   (`i-educar`, `RosarioSIS`, `openSIS`) are the LATAM / low-cost SIS tier, so the error
   would have fallen entirely on one region's supply.
3. 🟡 **`LGPL` still declines, and two shelved platforms carry it.** LGPL-3.0
   incorporates GPL-3.0 by reference *by design*, so it needs a fourth verdict rather
   than a profile (`Gap 440-B`). **BigBlueButton** and **OpenEduCat** are
   `GRANT-UNCALIBRATED` and must not be read as cleared.
4. 🟢 **`BSD` is PROFILED as of `p441`, variant-aware — `GRANT-UNCALIBRATED` on the BSD
   slice falls 14 → 3, and the remaining three are KB markdown tables, not licence
   payloads.** `MPL` (9) and `EPL` (9) are still unprofiled and are the remainder of
   `Gap 440-A`. 🔴 **Two corrections to that gap's own text, both measured:**
   - Its denominator was **27 % high**: of the 14 BSD-titled fixtures, three are markdown
     tables naming a licence in a cell. The real payload count was **11**.
   - Its prescribed method — *resolve the variant from the clause structure* — is
     **unsound**. BSD-2 and BSD-3 differ in exactly one clause, and it is a clause the
     instrument grades, so a **BSD-3 truncated at that clause** resolves as a complete
     BSD-2 and returns `GRANT-PRESENT`. 🟢 The variant is now resolved from the payload's
     own **declaration** (the title line, the only BSD signal independent of the graded
     clauses), with the structural arm permitted to answer **only** in the direction that
     cannot be wrong — presence of the discriminator, never its absence.
   - 🔴 And the row the gap named,
     [`Open-TutorAi/open-tutor-ai-CE`](https://github.com/Open-TutorAi/open-tutor-ai-CE),
     carries **no title line**, so no BSD profile could have screened it: the blocker was
     the family answer, not the variant. It is now verified `GRANT-PRESENT` with the family
     supplied by `lib/license_family.sh` (`grant_presence.py --family BSD`).

---

## 🆕 `p439` — **Zero rows added, and the screening question is now a measured one: can a dependency's grant even be READ from the repository?**

🔴 **No foundation rows this pass.** All **23** new addresses `p439` discovered (`ai-tutor`
ranks 61–80, `education-ai` ranks 21–40) are single-purpose tutoring skills, exam coaches,
prompt packs or student apps. A foundation on this shelf is something another component can
**depend on**; none of these is. 🟡 They are shelved on `agents/top.md` where they belong,
and the count here stays where it was rather than being inflated to look like progress.

### 🟢 The screening amendment — a third question, before licence family

This shelf has screened candidate foundations on existence, then default branch, then
licence family. `p439` adds a question that must come **between** family and adoption, because
it is the one that defeated every instrument on this base at once:

> **Is the granting text actually present in the repository, or only named?**

🔴 Measured on live supply this pass: `spragginsdesigns/ai-tutor-webapp` ships `LICENSE`
**552 B** titled Apache-2.0 — the APPENDIX *notice*, holder **Vercel, Inc.**, pointing at a
URL. This base's census returned `titled_family = Apache-2.0`, `scan_verdict = PERMISSIVE`,
`stock = True`, `needs_a_human = False`. 🔵 **A scan cannot answer this question and a byte
count should not**: the same measurement over this base's corpus shows BSD stock payloads
spanning **221 B → 1 514 B** (n=8), so any single BSD floor either misses a truncated BSD-3
or condemns every valid BSD-0. 🟢 **`p441` re-measured that span on 11 fixture payloads and
12 live ones and widened it to 164 B → 2 819 B** — the conclusion is unchanged and the
clause-based profile it argued for is now built.

🔴 **And the question was already settled here, one directory away.** `P1065` (pass 254):
*a pointer to a licence is not a grant* — implemented in
`pass258-content-licence-family/content_licence.py::is_grant()` for **Creative Commons content
licences only**, and never carried into the code-licence path that grades MIT, Apache-2.0 and
BSD. 🔵 A rule that exists in one classifier is not a property of the screen.

🟢 **So the question is asked of clauses, and it is now a `make` target, not a habit**:

```
make gate-grant-presence     # 19 controls, offline, committed fixtures
make grant-presence-census   # the live corpus; a MEASUREMENT, always exits 0
```

**Why it matters specifically for a foundation.** A foundation is vendored, so its
obligations travel to whoever ships it next. Two of them cannot be discharged from a
by-reference payload at all: Apache-2.0 **§4(a)** requires giving recipients a copy of the
License — a repository holding only the pointer has not done it, and the duty lands on the
integrator — and MIT's notice obligation requires reproducing a holder name, which in the
Vercel case names a party that never wrote the code. 🔵 For a dependency the client will
redistribute, `GRANT-BY-REFERENCE` is a **procurement finding**, not a footnote.

### 🟢 Four existing foundation-tier and platform addresses re-measured, and the shelf held

Independent re-probe this hour, byte-for-byte and HEAD-for-HEAD against what these shelves
already carry — a staleness check run as a measurement rather than assumed:

| Address | Re-measured 2026-10-25 | Agrees with shelf |
|---|---|---|
| [HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor) | Apache-2.0, `LICENSE` 11 408 B, HEAD `a31d82624c27` | 🟢 yes |
| [frappe/lms](https://github.com/frappe/lms) | 🔴 AGPL-3.0, `license.txt` 33 893 B, HEAD `5d6df8e3ed8e`, branch **`develop`** | 🟢 yes |
| [OpenOLAT/OpenOLAT](https://github.com/OpenOLAT/OpenOLAT) | Apache-2.0, `LICENSE` 10 982 B, HEAD `d073ad444fe5`, branch **`master`** | 🟢 yes |
| [withmarbleapp/os-taxonomy](https://github.com/withmarbleapp/os-taxonomy) | 🟡 ODbL, `LICENSE` 25 289 B, HEAD `7bd8b6794cb7` | 🟢 yes |

🔴 **And the secondary sources are still wrong about the first one a client will Google.**
Three of this pass's own 2026 search results named Frappe LMS "the MIT-licensed option" for
self-hosted LMS. It is **AGPL-3.0**; the MIT belongs to `frappe/frappe`, the *framework*.
`p425`'s `T125` re-verified at source — and the same two-key confusion (framework permissive,
application copyleft) is the single most expensive licence error available in this industry's
platform tier.

---

## 🆕 `p438` — **This pass adds ZERO foundation rows, and that is the finding** — plus the screening amendment that applies to every row already here

🔴 **Stated rather than padded.** `p438` graded **nine** new addresses first-hand (eight
permissive: 7 MIT, 1 Apache-2.0) and shelved all eight on `agents/top.md`. 🔴 **None of them
belongs on this file.** A foundation on this shelf is a component other work is built *on* —
`learningequality/kolibri`, `openedx/XBlock`, `pykt-team/pykt-toolkit`, `OpenOLAT/OpenOLAT`.
The eight new rows are single-purpose agent skills topping out at **18 ★** on their listing
page: real grants, real code, and **nothing downstream can depend on them**. 🟢 Promoting
them here to reach a count is the failure mode this base has a standing rule against, so the
count stays where the evidence puts it: **zero**.

🔵 **What was searched, so a successor does not re-spend the leg.** Four channels at measured
depth — GitHub topic `ai-tutor` pages 1–3 (ranks 1–60), topic `education-ai` page 1, topic
`intelligent-tutoring-system` page 1 — **89 slugs dup-checked, 80 already shelved**. The
foundation-shaped candidates the legs returned were `open-spaced-repetition/fsrs4anki`,
`GarethManning/education-agent-skills`, `GeminiLight/gen-mentor`, `Selleo/mentingo`,
`luffycodes/Tutorbot-Spock` and `thm-mni-ii/feedbacksystem` — 🟢 **every one already carried
on these shelves**. The platform legs re-returned `OpenOLAT` (Apache-2.0), `Sakai` (ECL-2.0,
Apache-derived), `formalms`, `francoisjacquet/rosariosis` and `GibbonEdu/core`, all carried,
with the licence-source conflict on `formalms` (Apache-2.0 in one comparison, GPL-2.0 in
another) 🔵 **already resolved on this base from the payload rather than the comparison**.

### 🔴 The amendment: a foundation is cleared on **three** columns now, not one

`p438`'s specimen `fangyuan-3149/book-learning-tutor` grades `titled_family = MIT`,
`scan_verdict = PERMISSIVE`, `stock = YES` — and, from the **same** `bespoke_census.grade()`
call, `p1054_verdict = MIT-BODY-PLUS:unclassified-addition` with `needs_a_human = no`. 🔴 Over
the **238** licence payloads committed under `compose/code/**/fixtures/`, **7 of the 9**
addition-bearing payloads are routed `needs_a_human = no` — **`p427`'s own two-family
specimen among them**, the payload this base wrote a 24-control gate about because it carries
a notice obligation of two.

🟢 **Why that matters more on this file than on `agents/top.md`.** A foundation is the row a
client's product *inherits* from, so an unread clause in a foundation payload propagates into
everything built on it and surfaces years later in a diligence review. The qualifying test on
this shelf is therefore:

1. 🟢 `titled_family` ∈ {MIT, Apache-2.0, BSD-*, ISC} — necessary, **not** sufficient;
2. 🟢 `p1054_verdict` carries **no** unclassified addition — the column `needs_a_human`
   currently ignores;
3. 🟢 payload bytes inside the family's stock band, or the surplus **read by a person** —
   and read in whatever language it is written in, which `p427`'s English `SCOPE_MARKERS`
   cannot do.

🔵 Every row currently on this file passes 1 and 3 on first-hand reads already recorded here.
🟡 **Column 2 has never been applied to this shelf as a screen** — it is registered as
`Gap 438-A` with its price, not back-fitted into the rows this pass did not re-grade.

## 🆕 `p437` — The permissive foundation tier grows by one, and the qualifying test is **not** the licence

🟢 Five MIT-licensed EU-AI-Act compliance repositories were graded first-hand this pass
(payloads and HEADs in `agents/top.md` `p437`). On licence alone, all five qualify as
foundations. 🔴 **On fitness, one does.**

| repo | grant · payload | foundation? |
|---|---|---|
| [tomdxb0004/eu-ai-act-risk-checker](https://github.com/tomdxb0004/eu-ai-act-risk-checker) | 🟢 **MIT** · `LICENSE` 1 073 B · `b7b08f330649` @ `41da87feb238` | 🟢 **Yes.** Zero dependencies, no build step, no backend, no telemetry; `engine.js` is a pure function with no DOM access, so the classifier is directly embeddable in a Globant deliverable. Encodes Annex III = `2027-12-02` **with its citation inline**, carries education as Annex III point 3, and implements the Art. 6(3) profiling override |
| [Hiepler/EuConform](https://github.com/Hiepler/EuConform) | 🟢 **MIT** · 1 073 B · `65335056589f` @ `011a5ad9bea2` | 🟡 **Component, not foundation.** Take the Annex IV report generator and the bias-evaluation harness; its date handling is too vague to anchor a compliance gate |
| [microsoft/agent-governance-toolkit](https://github.com/microsoft/agent-governance-toolkit) | 🟢 **MIT** · 1 074 B · `7df20dcdf919` @ `70a4ab8e8a04` | 🟡 **Component.** Annex III checklist naming education, plus agent controls; carries no dates, so it must be paired with a dated classifier |
| [sjgant80-hub/fall-euaiact](https://github.com/sjgant80-hub/fall-euaiact) | 🟢 **MIT** · 1 067 B · `0ddf3b67a14a` @ `5d8d27b65f68` | 🟡 Dates correct; 🔴 **no education scope**. A cross-check, not a base |
| [AbdelStark/eu-ai-act-toolkit](https://github.com/AbdelStark/eu-ai-act-toolkit) | 🟢 **MIT** · 1 056 B · `1126322e2cc8` @ `fff58f6e8906` | 🔴 **No.** Encodes the superseded `2026-08-02` at `packages/cli/src/commands/gaps.ts:199` and pins it in tests. 🟢 Its `data/annexes.json` Annex III cat. 3 education block (all four statutory use cases) **is** worth vendoring as reference data — take the data, leave the logic |

### 🔴 Why this belongs on the *foundations* shelf and not only on the agents shelf

A foundation is something an engagement's architecture **rests on**, so a wrong constant in it
propagates into every deliverable built above. 🔵 This pass found that four of five
candidates would have passed this base's normal foundation screen — permissive grant, payload
read, active, recent — while carrying either a superseded statutory date or no date at all.
🟢 **The screen has been extended accordingly**: a repository whose output includes a
regulatory date is only a foundation if that date **cites the instrument that set it**. The
three-grep version of that test is in `repos/trending.md` `p437`.

🟡 **And the reach bound, stated as one:** this test was applied to EU instruments only. The
NA state-guidance trackers and the APAC instruments this base cites on `intel/market.md` have
**not** been screened the same way, and `intel/trends.md` Trend 35 names that as the next
measurement — including against this KB's own shelves.

> The bases worth starting from, with licences read from each repository's own payload at
> the HEAD SHA shown (2026-10-25). Permissive first — those are the ones Globant can build on.

## ✅ The permissive foundations — verified 2026-10-25

| Repo | Licence | HEAD | Payload | Role in a build |
|---|---|---|---|---|
| [OpenOLAT/OpenOLAT](https://github.com/OpenOLAT/OpenOLAT) | **Apache-2.0** | `d073ad444fe5` | `LICENSE` 10 982 B · `6dbc5b605ed0` | University-grade LMS and **the only Apache-2.0 platform in the tier**. The default base when the client needs a full LMS and cannot take copyleft. Badly under-used relative to its terms. |
| [learningequality/kolibri](https://github.com/learningequality/kolibri) | **MIT** | `44a4e68aac3e` | `LICENSE` 1 097 B · `3c056b34a476` | Offline-first learning platform. The only MIT platform; the answer to connectivity and equity constraints (LATAM, rural APAC, Africa). |
| [openedx/XBlock](https://github.com/openedx/XBlock) | **Apache-2.0** | `c73c4bb42aa7` | `LICENSE.TXT` 11 358 B · `cfc7749b96f6` | Component SDK for Open edX. **The licence seam**: ship an Apache-2.0 AI component into an AGPL-3.0 platform without the platform's terms reaching your code. |
| [pykt-team/pykt-toolkit](https://github.com/pykt-team/pykt-toolkit) | **MIT** | `ccbaf37b07e3` | `LICENSE` 1 066 B · `f5f955194636` | Knowledge tracing (DKT/SAKT/BKT family, standard datasets). The measurement layer that makes an "adaptive" claim defensible rather than rhetorical. |
| [huggingface/smolagents](https://github.com/huggingface/smolagents) | **Apache-2.0** | `96f33faaf028` | `LICENSE` 11 357 B · `c71d239df917` | Minimal agent framework, EU-domiciled. The base for a bespoke tutor/grader when a full tutoring platform is too much. |
| [openfun/richie](https://github.com/openfun/richie) | **MIT** | `7cf513c235ee` | `LICENSE` 1 079 B · `e4b2a3148135` | Django/React course-portal CMS (France Université Numérique). The public-sector MOOC front-end. |
| [sakaiproject/sakai](https://github.com/sakaiproject/sakai) | **ECL** (Apache-derived) | `4debc94780cc` | `LICENSE` 11 120 B · `0688f62d04f1` | Higher-ed consortium LMS. Permissive in practice — but record it as ECL-2.0, **not** Apache-2.0. |
| [Utdanningsdirektoratet/PAS2-Public](https://github.com/Utdanningsdirektoratet/PAS2-Public) | **Apache-2.0** | `489129c42c9d` | `LICENSE` 11 325 B · `cb5e8e7e5f4a` | 🆕 `p435`. **Norway's Directorate for Education (Udir) publishing the public code of its new exam and test administration services (PAS2)**, issue tracker and wiki open to the public. 🟢 A national assessment authority's own administration stack under a permissive grant — the single strongest EMEA public-sector row on this file, and the counterpart to Norway's own age-tiered AI restriction. Default branch is `master`. |
| [DFE-Digital/get-information-about-schools](https://github.com/DFE-Digital/get-information-about-schools) | **MIT** | `ad46faf42690` | `LICENCE` 1 116 B · `e18299fd1942` | 🆕 `p435`. England's **school registry** service (GIAS) — the authoritative establishment dataset behind every DfE service. 🔵 Note the grant is at `LICENCE`, the British spelling: a ladder that only tries `LICENSE` reports this UK government repository as ungranted. |
| [DFE-Digital/teaching-vacancies](https://github.com/DFE-Digital/teaching-vacancies) | **MIT** | `a2d4f5fdec58` | `LICENSE` 1 092 B · `c561ea849ed6` | 🆕 `p435`. The DfE's national teaching job service (Rails + PostgreSQL + Redis), source **and** infrastructure definitions. The reference for a public-sector education service a client can read end to end. |
| [DFE-Digital/education-benchmarking-and-insights](https://github.com/DFE-Digital/education-benchmarking-and-insights) | **MIT** | `3cdbf2cbf47b` | `LICENSE` 1 091 B · `5a22fb5576a5` | 🆕 `p435`. **FBIT** — the DfE's school financial benchmarking and insights tool: compare resource use against similar schools, interrogate the financial data, support governor oversight. 🟢 The one row on this file that is a *finance* analytics surface over school data, which is where a UK trust-level engagement starts. |
| [oaknational/oak-curriculum-api](https://github.com/oaknational/oak-curriculum-api) | **MIT** | `0561df5aac12` | `LICENSE` 1 077 B · `0eeb9d32caed` | 🆕 `p435`. **Oak National Academy's** curriculum API — England's national-curriculum content as a documented, versioned OpenAPI surface. 🟡 `oaknational/oak-openapi` is the **same repository** (identical HEAD under `git ls-remote`, and the repo's own badges use that name); one row, two spellings, shelved once. |
| [instructure/ims-lti](https://github.com/instructure/ims-lti) | **MIT** | `724f1ae45315` | `LICENSE.txt` 1 068 B · `f7e95fbe6fa9` | 🆕 `p435`. **Instructure's own** Ruby IMS-LTI implementation — the Canvas vendor publishing the integration library under MIT. 🟢 The vendor-maintained half of the LTI layer that `Trend 19` says goes stale at the standards body and is carried by the vendor fork. |
| [hyunbinseo/neis-school-info](https://github.com/hyunbinseo/neis-school-info) | **MIT** | `5c9ecede5208` | `LICENSE` 1 068 B · `e82e1769aaaf` | 🆕 `p435`. TypeScript client for **NEIS**, Korea's national education information open-data portal (`open.neis.go.kr`) — school basic information. 🟢 The APAC analogue of GIAS above: a national school registry reachable from code. 🟡 The README warns the upstream dataset is not routinely reconciled, so treat records as reported, not current. |
| [krzysztofbury/librus-python-api](https://github.com/krzysztofbury/librus-python-api) | **MIT** | `fba65fe807eb` | `LICENSE` 1 071 B · `22e7ab2dbddc` | 🆕 `p435`. The independent Python client for **Librus Synergia** that `librus-mcp` (on `agents/top.md`) is built on — the library layer under the Polish gradebook connector. 🔵 Byte-identical MIT payload to the server, same copyright holder: one author, two addresses, no third-party-holder question. |

**15 verified permissive foundations** in the platform/agent tiers above. Each resolved under
`git ls-remote` and each licence was read from the repository's own payload. 🆕 `p435` adds the
**eight** above — the **public-authority** tier: a national assessment authority (Udir), three
UK Department for Education services, England's national-curriculum API, Korea's national school
registry client, the Canvas vendor's own LTI library and the client library under the Polish
gradebook connector. 🆕 `p431` adds a further **4** in **Tier 9 — the evaluation layer** below,
for **19** permissive foundations in all.

## 🔁 Restored by `p436` — including the repository two open gaps are written against

> 🔴 **Restorations, not discoveries**, from the **171**-address population `p436`
> measured for `Gap 435-B`. Every payload below was re-read first-hand on **2026-10-25**.
> 🔴 **The most serious single row is `LongsightGroup/qti3`**: `Gap 238` was closed
> against it with a tested artefact and `Gap 240` is still open on it, yet it was on
> **no live shelf** — the rewrite deleted the evidence under two registered gap verdicts
> while the verdicts themselves survived. That is `Gap 435-B`'s mechanism reaching the
> gap register itself.

| Repo | Licence (verified) | HEAD @ 2026-10-25 | Licence payload | Why it is a foundation | Region |
|---|---|---|---|---|---|
| [Ed-Fi-Alliance-OSS/edfi-oneroster](https://github.com/Ed-Fi-Alliance-OSS/edfi-oneroster) | **Apache-2.0** | `db379e0c8757` | `LICENSE` 10 173 B · `a6cba85bc92e` | Serves a **OneRoster 1.2 API from an Ed-Fi ODS** (Data Standard 4.0, 5.x and 6.1). The roster-interoperability seam for US district data, and the row that lets an agent read enrolment without touching the SIS directly. | North America |
| [LongsightGroup/qti3](https://github.com/LongsightGroup/qti3) | **MIT** | `902996d89729` | `LICENSE.md` 1 072 B · `00ed05b90bf8` | QTI 3 toolkit whose `packages/core` implements the **full parametric-item mechanism** — template declaration parsing, a real `randomInteger` draw over min/max/step, answer keys derived from the draw, and a constraint-retry loop. **This is the repository `Gap 238`/`Gap 240` are written against**, and it had been off every live shelf. | North America |
| [OpenOLAT/qtiworks](https://github.com/OpenOLAT/qtiworks) | **BSD-3-Clause** | `57cdf4affa26` | `LICENSE.txt` 2 058 B · `a5c692f12090` | QTI 2.1 delivery engine with **JQTI+** and **MathAssess** (Edinburgh lineage). 🟢 **The live fork**: byte-identical payload to the abandoned `davemckain/qtiworks` and maintained to **2026-06-30** — see the decline note below. | EMEA |
| [amp-up-io/qti3-item-player](https://github.com/amp-up-io/qti3-item-player) | **MIT** | `2e304fd0efb0` | `LICENSE` 1 076 B · `7faa621251d7` | QTI 3 **item player** — the rendering half of the assessment boundary, pairing with `qti3`'s authoring and `qtiworks`' delivery. | North America |
| [Kennisnet/php-qti3](https://github.com/Kennisnet/php-qti3) | **MIT** | `cad6125a16ff` | `LICENSE` 1 066 B · `27fb6d463569` | PHP QTI 3 implementation published by **Kennisnet, the Dutch national education-ICT body** — a state education body shipping its own permissive assessment code, which is the EMEA supply tier this base kept recording as absent. | EMEA |
| [datakind/student-success-tool](https://github.com/datakind/student-success-tool) | **MIT** | `e35c41af1dc1` | `LICENSE.md` 1 080 B · `04c23f1c41cd` | DataKind's data-assisted advising tool for retention: a **deployed** intervention, with John Jay College reporting a 32 % rise in senior graduation over two years via its CUSP programme (the project's own claim). Backed by google.org. 🟡 HEAD 2025-09-08 — over a year old; check currency before building on it. | North America |
| [marcosroriz/sete](https://github.com/marcosroriz/sete) | **MIT** | `9f1f9c87ec93` | `LICENSE` 1 069 B · `0bbd32e7e09a` | **SETE** — school-transport e-governance from CECATE/UFG, with web, desktop and mobile builds; the desktop build exists specifically so municipalities **with restricted internet** can operate it. The clearest LATAM public-sector education system on this base. 🔴 HEAD 2023-03-20 — stale; treat as a reference design, not a live dependency. | LATAM |
| [AI-for-Education/edu-qurating](https://github.com/AI-for-Education/edu-qurating) | **MIT** | `e007badc4e66` | `LICENSE` 1 063 B · `e6081fef4354` | **Edu-QuRating** — educational-quality rating of pretraining text, with a paper (arXiv 2609.09425) and released models; began as a fork of Princeton NLP's QuRating, upstream kept under `upstream/` with history. The data-curation layer under any education-domain model work. 🟡 `+0000` does not place a region on the offset channel; recorded Global. | Global |

### 🔴 Declined in the same tranche — `davemckain/qtiworks`

🔴 **Not restored, and the reason is in its own README**: *"IMPORTANT! This project is no
longer supported and is going to be closed in early 2023."* HEAD **2023-01-04**.
🟢 **The payload is BSD-3-Clause and re-read clean (2 058 B, `a5c692f12090`) — the grant
was never the problem**, and a licence-only promotion test would have shelved it.
🟢 **`OpenOLAT/qtiworks` carries the identical payload digest and is maintained to
2026-06-30, so it is restored in its place.** 🔵 This one row is the concrete
demonstration of `Gap 435-A`'s finding that *permissive* is not *recommendable*: both
forks pass the licence test, one is dead, and only a README read separates them.
Recorded as `DECLINED-p436` in the ledger so it is never re-litigated.

🟡 **Stated reach bound**: the QTI layer is restored on **grant + currency + README**;
no suite was executed, because installing a third-party repository's dependencies is not
permitted in this environment — the same limit `P533` carried.

## 🔴 Copyleft foundations — usable, but integrate, do not vendor

| Repo | Licence | HEAD | Payload | Note |
|---|---|---|---|---|
| [moodle/moodle](https://github.com/moodle/moodle) | GPL-3.0 | `46c042e7da65` | `COPYING.txt` 35 147 B · `8ceb4b9ee5ad` | Largest installed base and plugin ecosystem worldwide. Talk to it over its API. |
| [openedx/edx-platform](https://github.com/openedx/edx-platform) | AGPL-3.0 | `87cd3811a425` | `LICENSE` 35 136 B · `e12d78569742` | Network copyleft. Use XBlock as the seam. |
| [chamilo/chamilo-lms](https://github.com/chamilo/chamilo-lms) | GPL-3.0 | `2e5139a816d3` | `LICENSE` 35 147 B · `8ceb4b9ee5ad` | Lightest self-host; strong LATAM footprint. |
| [exelearning/exelearning](https://github.com/exelearning/exelearning) | AGPL-3.0 | `c848eca0018d` | `LICENSE` 34 523 B · `0d96a4ff68ad` | Authoring tool led by Spain's Ministry of Education — state-backed EMEA credibility. |
| [frappe/lms](https://github.com/frappe/lms) | AGPL-3.0 | `5d6df8e3ed8e` | `license.txt` 33 893 B · `db1a87ba81e8` | 🔴 Listed as MIT by several 2026 roundups. **That is wrong** — read at source. |
| [bigbluebutton/bigbluebutton](https://github.com/bigbluebutton/bigbluebutton) | LGPL-3.0 | `ec452b65043b` | `LICENSE` 7 652 B · `e3a994d82e64` | Virtual classroom. Link against it; don't fork. |
| [openeducat/openeducat_erp](https://github.com/openeducat/openeducat_erp) | LGPL-3.0 | `46a5d7d40082` | `LICENSE` 8 241 B · `528f84036800` | LMS + SIS on Odoo — the closest thing to an education ERP. |

> Moodle and Chamilo ship a **byte-identical** GPL-3.0 payload (`8ceb4b9ee5ad`) — the stock
> FSF text. Recorded so a digest sweep does not misread the collision as a fork.


## 🆕 `p435` — The permissive foundation tier grew for the first time in six passes, and what grew it was a **census**, not a search

`p434`, `p433`, `p432` and the three before them all reported this tier unchanged. 🟢
**This pass added eight rows, and none came from a web search.** They came from grading the
2 450 unpromoted addresses this base already held (`Gap 434-A`, closed:
`compose/code/p435-promotion-sweep`, evidence in
`evidence/promotion-backlog-grants.2026-10-25-p435.tsv`).

### 🔴 The number that explains six passes of "unchanged"

| arm of the unpromoted backlog | n | share |
|---|---|---|
| **PERMISSIVE** (MIT 1 022 · Apache-2.0 330 · BSD/ISC/CC0/ECL/Unlicense 97) | **1 449** | **59.1 %** |
| `NO-GRANT` — 404 on all eight paths × two refs | 500 | 20.4 % |
| GPL / AGPL / LGPL family | 329 | 13.4 % |
| other / unrecognised | 172 | 7.0 % |
| **total probed** | **2 450** | 100 % |

🔴 **The permissive supply was never scarce — it was unexamined.** Six passes reported "no
growth" while 1 449 permissive addresses sat on the trend record ungraded. This also
sharpens `Trend 10` rather than refuting it: the permissive supply really is in the agent
and integration layers, and the **platform** tier is still almost entirely copyleft — what
changes is that the agent/integration layer turns out to be an order of magnitude larger
than this file's seven rows suggested.

### 🟢 What the eight rows have in common: a public authority wrote them

Udir's exam-administration services, three DfE services, Oak National Academy's curriculum
API, Korea's NEIS registry client — **state education bodies publishing their own
production code under MIT or Apache-2.0.** 🔵 That is a different kind of foundation from a
framework: it is the *schema and the service contract a national system already runs*, so a
build on top of it inherits the jurisdiction's own data model instead of inventing one.

### 🔵 And one ladder detail worth more than it looks

`DFE-Digital/get-information-about-schools` carries its grant at **`LICENCE`** — the
British spelling. `p228-shelf-gate`'s ladder tries it; a ladder that stops at `LICENSE`,
`LICENSE.md` and `LICENSE.txt` reports a UK government repository as **ungranted**. 🟢 The
ladder earns its eighth path here, on a real row, for the first time on these shelves.

### 🟡 The reach bound, stated as one

The recency channel (`head_dates.sh`) was run over the **permissive arm only**: 1 449
addresses dated, 0 failures. The 1 001 non-permissive rows carry `head_committed = -` in
the evidence file. 🔵 That is a deliberate bound, not a gap in the data — a stale AGPL row
is not more shelvable for being fresh.

## 🆕 `p434` — The permissive foundation tier is unchanged for a **fifth** pass, and this time the sweep says *why* with a number

`p434` promoted two permissive addresses to `agents/top.md`
([`wenflow-org/wenflow`](https://github.com/wenflow-org/wenflow), MIT, `LICENSE` 1 067 B ·
`b6fac57d4710`; [`zhangl1001/civil-ai`](https://github.com/zhangl1001/civil-ai), MIT,
`LICENSE` 1 067 B · `5731a2d3ccea`). 🔵 **Neither belongs on this file, for `p433`'s reason:**
both are agent-layer — a learning-path agent and an adaptive-tutoring *runtime seam*. They
compose onto a base; they are not one.

🔴 **The permissive foundation tier above is unchanged:** OpenOLAT (Apache-2.0), Kolibri (MIT),
XBlock (Apache-2.0), pykt-toolkit (MIT), smolagents (Apache-2.0). **Five rows, five passes, no
movement** — and `verticals/solutions.md` records the education-ERP sweep returning a **standing
nil for the third consecutive pass**.

🟢 **What is new is that the asymmetry `p433` described in prose now has a measured number.**
This pass graded the seven highest-traction addresses sitting unpromoted in the trending shelves
and **not one is a foundation, nor is one promotable**:

| ★ band | Addresses | Grants found | Foundations among them |
|---|---|---|---|
| ≥ 190 ★ | 5 | 🔴 3 × AGPL-3.0 · 1 × CC-BY-SA-4.0 · 1 × **no licence file** | **0** |
| < 100 ★ | 2 | 🟢 2 × MIT | **0** |

🔴 **So the asymmetry is sharper than "foundations move slowly".** In education's new supply,
**traction and permissiveness are anti-correlated** (`repos/trending.md`, `p434`): the biggest new
addresses are copyleft, content-licensed or ungranted, and the permissive ones are an order of
magnitude smaller — *and none of either kind is platform-shaped*. 🔵 **Pricing consequence,
unchanged in direction but now defensible with a count:** a proposal may assume it can adopt a
fresh permissive **agent**; it may not assume it can adopt a fresh permissive **platform**, and
it may not use stars as a proxy for adoptability at all. The highest-traction education address
this base has ever recorded is **4 771 ★ and CC-BY-SA-4.0**.

🟢 **Instrument added this pass**, and it is the reason this file can state the above as a
standing property rather than a pass observation: `compose/code/p434-promotion-gate`
(`make gate-promotion`, 28 offline controls, wired into `hooks`) fails whenever a **permissive**
address recorded in the trending shelves appears in **no** curated shelf. It was **red on its
first run** and is green after the two promotions, so this tier's completeness is now checked by
a gate instead of by a pass remembering to look.

## 🆕 `p433` — The permissive foundation tier did **not** grow, and that is the finding

`p433` promoted three permissive addresses into `agents/top.md` after first-hand payload reads —
[`learn-from-materials`](https://github.com/dmoshehun-prog/learn-from-materials) (MIT,
`LICENSE.md` 1 122 B · `15ce43afa44a`, **1 118 ★**),
[`PhysicsOS`](https://github.com/122-syf-wcy/PhysicsOS) (Apache-2.0, `LICENSE` 11 356 B ·
`f1a2e5fccede`) and
[`textbook-writer-skills`](https://github.com/cabbage2000-lab/textbook-writer-skills) (MIT,
`LICENSE` 1 064 B · `0d5a33d13ca9`). 🔵 **None of them belongs on this file**, and saying why is
the point: all three are **agents and skill packs**, not foundations. They compose *onto* a base;
they are not a base.

🔴 **The permissive foundation tier above is unchanged for the fourth consecutive pass:**
OpenOLAT (Apache-2.0), Kolibri (MIT), XBlock (Apache-2.0), pykt-toolkit (MIT), smolagents
(Apache-2.0). The `p433` ERP sweep (see `verticals/solutions.md`) independently confirms there is
**no MIT/Apache education ERP** to add, and the trending sweep returned no permissive platform.

🔵 **The asymmetry is worth naming for anyone sizing an engagement.** New permissive supply in this
industry arrives almost entirely as **agent-layer** work — small, fast-moving, APAC-origin, often
skill-pack shaped. The **foundation** layer moves on a scale of years and is majority copyleft.
A proposal that assumes it can pick a fresh permissive platform is mispriced; a proposal that
assumes it can pick a fresh permissive agent is usually right. `Trend 14` is the demand-side
reading of the same fact.

## 🆕 `p432` — Tier 10: the special-education / IEP layer, and why it is a tier of seeds

The surface North American law regulates hardest has the thinnest open-source supply measured
anywhere in this repository. These are the bases that exist, with grants read from each
repository's own payload at the HEAD shown (2026-10-25).

| Repo | Licence | HEAD | Payload | Role in a build |
|---|---|---|---|---|
| [robotros/California-IEP-AI-project-kit](https://github.com/robotros/California-IEP-AI-project-kit) | **MIT** | `ff1ae0ce30e7` | `LICENSE` 1 065 B · `43554d1189d8` | The **knowledge and boundary layer**. Two CA special-education roles as pinned knowledge packs with a declared draft-only / authorised-system-of-record boundary. Start an NA special-education engagement from this, not from a blank prompt. 🔴 Prose discipline, no runtime enforcement — adding that is the work. |
| [67tallchris/iep-builder](https://github.com/67tallchris/iep-builder) | **MIT** | `b39df0e9a4a1` | `LICENSE` 1 069 B · `aa8cfde0dc31` | The **deployment reference**: Svelte + Cloudflare Pages Functions + D1 with bring-your-own-key AI. Shows a per-district deployment that holds no vendor key and no central student store. Jurisdiction-pinned to Arizona K-8. |
| [dougdevitre/access-to-education](https://github.com/dougdevitre/access-to-education) | **MIT** | `f8abd70707ba` | `LICENSE` 1 069 B · `fc7c8b90fee1` | The **parent-facing corpus**: 69 files / ~120 k words on IEP navigation, family–school communication and advocacy, under a code licence. The only MIT answer to the unserved-parent persona of `Trend 10`. |
| [ezixen/PlannedEducation](https://github.com/ezixen/PlannedEducation) | **MIT** | `06fb12159f5e` | `LICENSE` 1 086 B · `53de23fdecc2` | Adjacent, not special-ed specific: grading companion + secure test-taking, privacy-first self-host. Default branch `dev`. |
| [rwrife/rubric-desk](https://github.com/rwrife/rubric-desk) | **MIT** | `010a44006014` | `LICENSE` 1 063 B · `c186f5cb204a` | The **offline marking surface** (Flutter; phone/tablet/Windows, no accounts, no cloud LMS). Pairs with `kolibri` wherever connectivity cannot be assumed. 🟡 Created 2026-10-25. |

**5 permissive additions**, taking this file to **16 permissive foundations** in all.

🟡 **Adjacent but copyleft — integrate, do not vendor:**
[`Apomera/AlloFlow`](https://github.com/Apomera/AlloFlow) is **AGPL-3.0-or-later**
(`LICENSE` 35 441 B · `d8d2ea7ef0a1` @ `6194e51e8f1f`, standard AGPLv3 body, SPDX header, no added
clauses) and is the only maintained accessibility-first differentiation engine found — UDL, WCAG,
AAC, text-to-speech, offline-first, i18n, commit on 2026-10-25. Network copyleft over a hosted
engine is the worst-case shape; reach it over an interface.

🔴 **Two addresses are excluded for cause, both proved by `git ls-tree -r` over the whole tree:**
[`grasped-dev/staircase`](https://github.com/grasped-dev/staircase) (@ `9236fce606c2`, 0 of 33 files)
and [`eakarsu/ai-special-education-iep-compliance`](https://github.com/eakarsu/ai-special-education-iep-compliance)
(@ `ec2516b76699`, 0 of 29 files) carry **no licence at all**. Between them they hold the tier's best
technique (a standards graph for goal reasoning) and its most complete-sounding product. Neither is
a base.

🔴 **The honest health warning on this entire tier.** Star counts are 0, 0, 1, 0 and 0. Two of the
five were created inside the eleven days before this pass. None has a second contributor. These are
**seeds to fork and own**, not dependencies to track — and that is a different commercial
conversation from the one `kolibri` or `OpenOLAT` supports. Said plainly to a client, it is also an
argument *for* the engagement rather than against it: there is no incumbent to displace.

🔴 **Declared gap:** the tier is entirely US. The sweep found **no** open-source tooling for
England's EHCP process or for the inclusive-education mandates of Brazil, Chile or Colombia — a nil
result, not a thin one.

---

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
| 🆕 `p394` [ucbds-infra/ottr](https://github.com/ucbds-infra/ottr) | 🔴 `master` · `693b3df` | 🟢 **BSD-3-Clause** *(🔴 the grant is at `LICENSE.md`, **1,555 B · `1677c5307530`**, re-read at this commit on 2026-10-25 and `GRANT-PRESENT` clause-by-clause; `LICENSE` itself is a **108 B** `YEAR:` / `COPYRIGHT HOLDER:` stub — `DESCRIPTION`: `BSD_3_clause + file LICENSE`. A probe that takes the first filename-ladder hit reads this repository as ungranted: `Gap 441-A`)* | **The R autograding extension for `otter-grader`** (row above), UC Berkeley Data Science Education Program — grades R scripts, Rmd documents and Jupyter notebooks with R kernels. HEAD **2026-07-06 — 108 d**. 🟢 So this tier's flagship autograder is permissive in **both** languages. 🔴 **3 ★**: the adoption sits on the Python parent, but this is the component an R course actually deploys. |
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

## 🆕 `p431` — Tier 9: the evaluation layer, which is what makes every other tier's claim checkable

Every tier above supplies something that **does** tutoring, grading or delivery. None of them
supplies anything that says whether the tutoring was any **good**. `Trend 8` has carried that as an
open measurement gap for many passes. Measured first-hand on 2026-10-25, the layer exists:

| Repo | Licence | HEAD | Payload | Role in a build |
|---|---|---|---|---|
| [shuangyan123/tutorbench](https://github.com/shuangyan123/tutorbench) | **Apache-2.0** (code) | `f9d69c7ce3e1` | `LICENSE` 11 358 B · `cfc7749b96f6` | Scenario-based evaluation **and regression** engine. Diagnoses a concrete pedagogical failure and keeps the evidence to re-test it after the fix. The CI gate for a tutoring deliverable. **Maintained** — commit 2026-10-25. |
| [Teachable-AI-Lab/tutor_gym](https://github.com/Teachable-AI-Lab/tutor_gym) | **MIT** | `772f5cdca5dd` | `LICENSE` 1 099 B · `8a0a4ba421a0` | Runs a model as tutor **and** as simulated student across existing ITSs (`ctat`, `apprentice`, `oatutor`). The acceptance-test fixture. 🟡 Stale since 2025-09-10 — fork it. |
| [DannyWeitekamp/tutorenvs](https://github.com/DannyWeitekamp/tutorenvs) | **MIT** | `eacba91d2b6b` | `LICENSE` 1 064 B · `eb1ef5e1a637` | `tutor_gym`'s upstream. Relevant only if the fork diverges; recorded for lineage. |
| [Teachable-AI-Lab/tutorenv](https://github.com/Teachable-AI-Lab/tutorenv) | **MIT** | `b90a4d01f2f1` | `LICENSE` 1 064 B · `eb1ef5e1a637` | Lineage root. Payload **byte-identical** to the row above — same grant, re-attributed at the fork. |

**4 verified permissive rows, bringing this file to 11 permissive foundations.**

🟢 **The composition that comes free.** `tutor_gym`'s `oatutor` backend binds to
[`CAHLR/OATutor`](https://github.com/CAHLR/OATutor) (MIT), already on this shelf, and `pykt-toolkit`
(MIT) already supplies knowledge tracing. **Tutor → measurement → evaluation is now MIT end to end**,
which is the first time this base can price an *evidence* deliverable without a licence caveat.

🔴 **What this tier does NOT cover, and it is the regulated half.** Every address above scores
**tutoring** — dialogue, hinting, diagnosis. **Nothing found scores grading.** The only grading-side
candidate measured, [`sdrangan/llmgrader`](https://github.com/sdrangan/llmgrader), is
**non-commercial** (see `agents/top.md`). NA, EMEA and APAC statutes all bite hardest on
**assessment**, so the surface with the most regulatory exposure is the one with no open harness.
Tracked as **`Gap 431-C`**.

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
