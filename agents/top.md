---
industry: education
region: Global
updated: 2026-10-23
---

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
| **OpenMAIC** 🆕 `p389` | [THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC) | `main` | 🟢 **MIT** *(1,066 B, "Copyright (c) 2026 THU-MAIC"; `package.json` also declares `"license": "MIT"`)* | **The whole classroom, generated.** 🔴 🆕 `p392` *(This row said "and the largest education-native repository in the open-source supply (~41.3k ★)". **Retired.** Read today through the one open channel: OpenMAIC **41.3k ★** — `p389`'s figure confirmed — against [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) at **42.2k ★**, which was already two rows below with no star count against it. The superlative was published because the comparison was unmeasured, not because it had been made.)* A topic or an uploaded document becomes a multi-agent lesson: an AI teacher with a voice, teaching assistants, simulated classmates, narrated slides, auto-graded quizzes, HTML interactives and a shared whiteboard, with **agentic mid-lesson chat about any slide element**. Grew out of **MAIC**, deployed inside Tsinghua and validated on **700+ real students**; paper in **JCST 2026**. 🟢 Three properties that decide a school deployment and that almost nothing else on this shelf has: **server-first** generation (v1.2.0) that survives closed tabs and restarts on PostgreSQL; **central model governance** — every AI use is a named *slot* in `openmaic.yml`, each slot pinned to a provider, with an option to **forbid user-supplied keys** outright and `video: null` to switch a capability off; and **export of a finished classroom as one offline HTML file** (or a PPTX that keeps every scene). 🟢 Local-model path is real: **Lemonade** for local inference, **FunASR** for local ASR. 🟢 **24 built-in skills** plus per-owner authored skills; the course agent works through validated tools (patch one scene atomically, reorder pages, import `.pptx` with layout) rather than rewriting opaque blobs. 🟢 Security is handled like a product, not an afterthought — five releases since September carry SSRF, DNS-rebinding and provider-redirect fixes under published GHSAs. 🔴 Current head is **v1.3.0-rc.1** (knowledge base, 2026-10-22) with **breaking upgrade conditions and no rollback below it**; pin **v1.2.1** (2026-10-18) for a pilot. 🔴 Needs Node ≥ 22.19, pnpm ≥ 10, PostgreSQL 16 and a long-running server — Vercel deployments are capped at the 1.1.x line. 🔵 🆕 `p392` **Measured: `41.3k ★` · 6.4k forks · 750 commits** *(github.com HTML · WebFetch · 2026-10-22)*. | APAC — Tsinghua University, China (EN + zh-CN) |
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
| **Brightspace / D2L** | [rohanmuppa/brightspace-mcp-server](https://github.com/rohanmuppa/brightspace-mcp-server) | `main` | 🟢 **MIT** *(1,068 B)* | 🆕 `p386`. 🔵 **Upstream of a fork family — count it once.** [`lmgveerhoek`](https://github.com/lmgveerhoek/brightspace-mcp-server) and [`matthewliu10`](https://github.com/matthewliu10/brightspace-mcp-server) publish **byte-identical** payloads still holding `© 2026 Rohan Muppa`; several more forks share the npm name. Grades, due dates, assignments, announcements, rosters, syllabus. Automated login is wired per school. |
| **Brightspace / D2L** | [AnonymousOnyx22/brightspace-d2l-mcp](https://github.com/AnonymousOnyx22/brightspace-d2l-mcp) | `main` | 🟢 **MIT** *(🔵 **1,200 B** — non-stock)* | 🆕 `p386`. The extra bytes are **attribution, not restriction**: an inline notice *"Portions of this software are derived from brightspace-mcp-server, Copyright (c) 2026 Rohan Muppa, used under the MIT License."* See **Pattern L step 11**. |
| **Brightspace / D2L** | [RobertLMcCrary/D2L-MCP](https://github.com/RobertLMcCrary/D2L-MCP) | `main` | 🟢 **MIT** *(🔵 **2,181 B** — **two stacked grants**)* | 🆕 `p386`. The payload is **two complete MIT licences**: its own (© 2026 Robert McCrary) **plus** *"Portions of this project are derived from d2l-cli: Copyright (c) 2026 Aaryan Kapoor."* 🟡 Shipping it means carrying **both** notices. Go, read-only, pre-1.0. |
| **Anki** | [ankimcp/anki-mcp-server](https://github.com/ankimcp/anki-mcp-server) | `main` | 🟢 **MIT** | Not an LMS — the spaced-repetition loop, which pairs with FSRS above. |

### 🆕 `p387` — Dated: which of these servers actually ships a release

Stars are unreadable here and always were a poor proxy. **A publish date is the signal a studio can
act on**: it dates the artefact the client would install. Method and every raw row:
[`registry-recency`](../evidence/registry-recency.2026-10-22-p387.tsv).

| server | package | latest | last published | read it as |
|---|---|---|---|---|
| [rohanmuppa/brightspace-mcp-server](https://github.com/rohanmuppa/brightspace-mcp-server) | npm `brightspace-mcp-server` | **5.0.8** | **2026-10-22** (today) | 🟢 the most actively published LMS MCP server on this shelf — and a **v5** line, not a weekend project |
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
  simply wrong. 🔵 **Why this one matters more than a badge mismatch.** A badge mismatch is caught by
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
| [rohanmuppa/brightspace-mcp-server](https://github.com/rohanmuppa/brightspace-mcp-server) | `main/LICENSE` | MIT — 1,068 B; `lmgveerhoek` and `matthewliu10` byte-identical *(`p386`)* |
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
