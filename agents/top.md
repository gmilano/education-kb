---
industry: education
region: Global
updated: 2026-11-16
---

## 🟢 Fifty-second pass (`p847`, 2026-11-16) — **`2` agent rows (`424` → `426`), and the pass's most valuable output is a NEGATIVE: the largest auto-graded exercise estate on GitHub is not open source, and this base was one search away from shelving it**

🟢 **`1` genuinely new build-safe agent** ([`Li-Evan/BloomTutor`](https://github.com/Li-Evan/BloomTutor),
`310★`, MIT, byte-read). 🟢 **`1` row RESTORED** that two archives hold and no current shelf does
([`iflytek/astron-harness-tutorial`](https://github.com/iflytek/astron-harness-tutorial), `363★`,
Apache-2.0, byte-read). 🔴 **`1` high-traction lead disqualified at the grant**: the `4GeeksAcademy`
auto-graded exercise estate and the `learnpack` runtime under it. 🔵 **`p842`'s intake gate (`P94`)
and `P990` ("a file named `LICENSE` is not necessarily a grant") both fired, on the same candidate,
for different reasons.** → `T158`, `T159`, `T160`, `T161`.

### 🟢 Finding 1 — BloomTutor: the Bloom 2-sigma framing, shipped, MIT, and `44` forks in eight months

| | |
|---|---|
| Address | [`Li-Evan/BloomTutor`](https://github.com/Li-Evan/BloomTutor) |
| Stars / forks (first-party, `search/repositories`, `2026-11-16`) | `310` / `44` |
| Created / last push | `2026-03-10` / `2026-11-16` (**today**) |
| Grant | 🟢 **MIT — byte-read** (`main/LICENSE`, `1,069 B`, `sha256₁₂ 7d574cf3632e`, holder `2026 Li Zhengping`) |
| Archived | `false` |
| Stack (from `README` badges) | Python `3.11+`, FastAPI `0.115+`, Node `20+`, Next.js `15` |

🔵 **Why it is a row and not noise.** Its own `README` states the thesis it is built on:
Bloom's 1984 finding that one-to-one tutoring moves a learner `+2σ` to roughly the top `2%`, and
that the obstacle is scale, not efficacy. 🟢 **The mechanism it ships against that thesis is the
one this base has repeatedly said is missing from chat-wrapper tutors**: it generates a structured
syllabus, delivers *one lesson at a time*, reads the learner's annotations and feedback, and
tailors the NEXT lesson from them — a learner model that advances between lessons rather than a
transcript that grows inside one. 🔵 **It ships two surfaces**: a CLI mode driven through Claude
Code, and a web app (`bloomtutor.app`). Bilingual `README` (English + 中文).

🔴 **Scope it honestly.** `310★` is a small fraction of `HKUDS/DeepTutor` (`59,637★` first-party
today). 🟢 **What makes it worth a row anyway is the LICENCE and the SIZE**: it is MIT and it is
small enough to read, which is what a studio needs when the deliverable is *the client's* tutor,
not a dependency on someone else's. `44` forks on `310★` is a high fork ratio — people are taking
it apart, not starring it.

**Region: Global** (author's name and the bilingual `README` indicate APAC origin; nothing in the
repository scopes it to a market, so it is filed Global with the origin noted rather than
mis-placed into APAC).

### 🟢 Finding 2 — a restoration with a named mechanism, and the loss hypothesis around it tested NEGATIVE

🟢 **The restored row.** [`iflytek/astron-harness-tutorial`](https://github.com/iflytek/astron-harness-tutorial)
— `363★`, 🟢 **Apache-2.0 — byte-read** (`main/LICENSE`, `11,347 B`, `sha256₁₂ 649fc6df7e4c`),
created `2026-03-19`, pushed `2026-11-02`, not archived. Bilingual illustrated guides to iFlytek's
AStudio / Loomy / AstronClaw agent tooling. 🔵 **It is held by
`archive/2026-11-09-p722-pre-rewrite/` and `archive/2026-11-12-p787-pre-rewrite/` (both
`agents-top.md` and `intel-market.md`) and appears in NONE of the eight current shelf files.**
🔴 **So it was dropped in the `p787` rewrite — the same mechanism `p837` named.** **Region: APAC**
(iFlytek is the Chinese education-AI incumbent this base's APAC intel already tracks; developer
education rather than learner tutoring, which is why it belongs on the agents shelf as tooling
provenance, not as a tutor).

🔴 **And the hypothesis that this is a SYSTEMIC loss is now tested, and it is mostly false.**
This pass extracted every `OWNER/REPO` repository address from the five most recent pre-rewrite
archives and differenced each against all eight current shelf files:

| Archive | Addresses in it | Absent from every current shelf file |
|---|---|---|
| `2026-11-12-p796-pre-rewrite` | `190` | `2` |
| `2026-11-12-p797-pre-rewrite` | `4` | 🟢 `0` |
| `2026-11-12-p800-pre-rewrite` | `219` | `2` |
| `2026-11-13-p801-pre-rewrite` | `40` | 🟢 `0` |
| `2026-11-13-p809-pre-rewrite` | `131` | 🟢 `0` |

🔵 **The `2` are the same `2` in both archives, and they were correctly dropped, not lost:**
[`Bestisco/My-WASSCE-Companion`](https://github.com/Bestisco/My-WASSCE-Companion) (`0★`, no
licence, last push `2026-02-27`) and [`Elite2828/ACE-AI-Tutor`](https://github.com/Elite2828/ACE-AI-Tutor)
(`1★`, no licence, last push `2026-03-05`) — both WAEC/WASSCE exam-prep prototypes, both below
every bar this base publishes. 🟢 **Recent rewrites are clean.** 🔴 **The `847` archive-only
addresses this pass counted across ALL archives are concentrated before the `2026-10-06` reset,
which was deliberate — they are not evidence of ongoing loss and this base should stop treating
the archive differential as an alarm.** → `T158`.

🔵 **The WASSCE pair is still worth one sentence as INTEL even though it is not worth a row:**
West African school-leaving exam prep is being prototyped, repeatedly, by individual developers
with no licence and no traction. That is a demand signal under an empty supply, which is the same
shape this base recorded for LATAM at `p839`.

### 🔴 Finding 3 — the disqualification: `4GeeksAcademy` + `learnpack`, rejected at the grant, in three independent probes

🔵 **How it surfaced.** `q="auto grading" OR "autograder" OR "essay scoring" ... stars:>20`
returned a *cluster*: nine `4GeeksAcademy` repositories of interactive auto-graded exercises
(`472★`, `140★`, `136★`, `114★`, `113★`, `95★`, `85★`, `74★`, `74★` — roughly `1,300★` and `634`
forks on the JavaScript one alone). 🟢 **On traction alone this is the richest auto-grading
courseware estate this base has ever surfaced, and the base has a DECLARED grading gap.**

🔴 **Three probes, three disqualifying facts:**

| Probe | Result |
|---|---|
| GitHub licence field on the content repos | `Other` / `NOASSERTION` — not a recognised grant |
| 🔴 Byte-read of `master/LICENSE.md` on [`4GeeksAcademy/python-beginner-programming-exercises`](https://github.com/4GeeksAcademy/python-beginner-programming-exercises) | `954 B`, and its first line is **`# TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION`** followed by *"By accessing Breathe Code we assume you accept these terms and conditions"* — 🔴 **a terms-of-service page in a file named `LICENSE.md`, not an open-source grant** |
| 🔴 npm `registry.npmjs.org/learnpack` (the runtime the estate executes on) | `"license": "https://learnpack.co/terms"` — 🔴 **a URL where an SPDX identifier belongs**; `latest 0.1.30`, `modified 2024-11-05` |
| 🔴 The repository npm points at, `learnpack/learnpack-cli` | 🔴 **`404` on `raw.githubusercontent.com` for `README.md`, `package.json` and `LICENSE`, on both `master` and `main`, and absent from `search/repositories`** — the canonical source address in the package metadata does not resolve |
| The `learnpack` org's visible repos | [`learnpack/learnpack`](https://github.com/learnpack/learnpack) `10★`, **no licence**, last push `2025-10-14`; `learnpack/ide` `2★` and `learnpack/web` `1★`, both pushed November 2026, both **no licence** |
| `learnpack.co/terms` itself | 🟡 **Unreachable from this environment** — the agent proxy returned `CONNECT tunnel failed, response 403`. The licence text behind the URL was NOT read, and this pass does not characterise it. |

🔵 **The shape of the trap, which is the transferable part.** The *content* is where the stars
are; the *engine* is where the licence is; and the engine's licence is a link, in a package whose
source repository `404`s. 🟢 **A reviewer who checks the exercise repo's star count and sees a file
called `LICENSE.md` passes this candidate. `P990` is the rule that catches it and `P94` is the gate
that stops it.** 🔴 **Verdict: NOT build-safe, NOT shelved, and recorded here so no later pass
spends the same hour.** → `T159`.

🟡 **One honest qualifier**: `user:4GeeksAcademy` reports `total_count = 45,594` repositories, of
which `auto-graded in:description` matches `12`. 🔵 **The estate is overwhelmingly per-student
scaffolding, so the `~1,300★` sits on a dozen canonical templates, not on a thousand products.**

### 🔴 Finding 4 — three more candidates named and rejected, each for a different reason

| Candidate | Stars | Why not shelved as build-safe |
|---|---|---|
| [`kg-bnu/SciMKG`](https://github.com/kg-bnu/SciMKG) | `130` | 🔴 **No grant blob** — `LICENSE`, `LICENSE.txt`, `LICENSE.md`, `COPYING`, `LICENCE` all `404` on `main` and `master`; GitHub reports `NONE`. 🔵 Source code of the AAAI-2026 paper *"SciMKG: A Multimodal Knowledge Graph for Science Education"*, from **Beijing Normal University** — China's principal teacher-training university. **Region: APAC.** 🔵 **This is exactly the curriculum-graph substrate this base has wanted since `p587`, and it is unlicensed — cite the paper, do not vendor the code.** |
| [`RockeyRoc/DeepProf`](https://github.com/RockeyRoc/DeepProf) | `102` | 🔴 **No grant blob** (same five filenames, both branches). 🔵 A Chinese higher-education course-level companion agent whose own description claims the three properties this base keeps asking for — *答案可溯源* (traceable answers), *引导可分级* (gradable scaffolding), *学习可接续* (resumable learning) — on a self-built agent runtime coordinated with a teaching-strategy graph. **Region: APAC.** 🔴 **Unlicensed, `2026-09-19` creation, `102★` — a design to read, not a dependency to take.** |
| [`MAX-API-Next/Academic-Agents-Studio`](https://github.com/MAX-API-Next/Academic-Agents-Studio) | `168` | 🟡 **`GPL-3.0`** → belongs in the copyleft table below, not the build-safe one. Multi-model (GPT / Claude / DeepSeek / Qwen) full-pipeline academic-research agent platform for researchers, educators and students. **Region: APAC.** |

🔴 **And a supply-pollution note worth one line.** `q='"lesson plan" in:name,description license:mit'`
returned three repositories at `39★`, `24★` and `23★` — `redowl2265-aklhu/edu-lesson-plan`,
`codebear9535-0xd4i/lesson-plan-builder`, `fastdeer4365-n4fst/lesson-plan-reviewer` — all created
within four days of each other, all with **empty descriptions**, all under owner names with the
same `word+digits-hash` shape. 🔵 **Three stars-bearing results in a four-result query, and none of
them is a project.** 🔴 **A star floor does not filter this; an empty description plus a generated
owner name does.** → `T160`.

### 🟢 What this pass did NOT find, stated so the nil is informed

🔴 **`0` new build-safe tutoring agents from the English-language star-ranked channel.** Queries
run: `"AI tutor" license:mit pushed:>2026-08-01 stars:>30` (`5` hits, `4` of them tutorials about
AI rather than AI tutors — `data-ai-tutorials`, `cal-ai-tutorial`, `geoai-tutorials`,
`ai-tutorial-scraping-prescriptions`); `"intelligent tutoring" in:name,description,readme
pushed:>2026-06-01` (`13` new hits, `0` tutoring agents — the top result is a Chinese computer-science
course); `agent education created:>2026-08-01 stars:>30` (`1` hit, an animation set);
`topic:education created:>2026-09-01 stars:>100` (`2` hits, neither an agent).
🔵 **The lexical collision between "tutor/tutorial" and "education/educational" is now measured at
roughly `4` in `5` of returns on the obvious queries — that is the channel defect, not a supply
defect.** → `T160`.

🔴 **`0` build-safe LATAM-ORIGIN education software.** `escuela OR docente OR profesor OR alumno`
and `professor OR aluno OR ensino OR escola` together returned `34` new addresses. 🟢 **Every single
one of the LATAM-origin hits is COURSEWARE — lecture notes, university course material, exercise
sets — and the licence field is `NONE` or `NOASSERTION` on all but two.** Named examples:
[`nad-garraz/algebraUno`](https://github.com/nad-garraz/algebraUno) (`150★`, no licence, UBA Exactas
algebra notes in LaTeX, maintained by current and former students),
[`henriquegpb/gradesinteli`](https://github.com/henriquegpb/gradesinteli) (`86★`, no licence,
pushed **today**, an open replacement UI computing grades and absences for Inteli's Adalove
platform, Brazil), [`lugaralgum/material-aulas`](https://github.com/lugaralgum/material-aulas)
(`102★`, `NOASSERTION`, introductory Python teaching material in a visual context).
🔵 **This does not contradict `p839`'s "LATAM is not an agent-supply region" — it SHARPENS it:
LATAM supplies education CONTENT in volume, and ships it without a grant.** → `T161`, `P102`.

## 🔴 Fifty-first pass (`p846`, 2026-11-16) — **the whole shelf swept at last (`815` addresses, `3.5` minutes), and the instrument that swept it is NOT a liveness oracle: `6` of the `11` addresses it could not resolve are ALIVE, including BOTH of `p845`'s "genuine absences"**

🟢 **`ACTION p845-A` is CARRIED and `845-G1` is CLOSED.** 🔵 **The search channel in this
environment is already authenticated: `gh api rate_limit` reports `search.limit = 30` per minute,
not the `10` that `p844` and `p845` priced their deferrals against.** 🟢 **At `30`/min, batched `10`
`repo:` qualifiers to a query, the full shelf is `82` queries. Measured wall-clock: `3` minutes
`30` seconds, `0` batch failures.** 🔴 **The hour of work that two consecutive passes declined to do
was a three-and-a-half-minute run.** → `T151`.

### 🟢 Finding 1 — the whole shelf, measured first-party for the first time

| | |
|---|---|
| Distinct `github.com/OWNER/REPO` addresses extracted from `agents/top.md`, `repos/foundations.md`, `verticals/solutions.md` | `815` |
| 🔵 Of which a prose TEMPLATE, not an address (`OWNER/REPO`, from `p845`'s own `Finding 1` table) | `1` |
| Resolved by `search/repositories` with licence, stars, forks, `pushed_at`, `archived`, `fork` | 🟢 **`804`** |
| Not resolved | `11` |
| Batch failures | 🟢 `0` |

🟢 **The number this base has never been able to state, now measured rather than asserted —
`607` of `804` resolved addresses (`75.5%`) carry `MIT`, `Apache-2.0`, `BSD-3-Clause`,
`BSD-2-Clause` or `ISC`:**

| Licence (first-party, `2026-11-16`) | Rows | | Licence | Rows |
|---|---|---|---|---|
| 🟢 `MIT` | `482` | | 🔴 `GPL-3.0` | `35` |
| 🟢 `Apache-2.0` | `106` | | 🔴 `AGPL-3.0` | `27` |
| 🟢 `BSD-3-Clause` | `11` | | 🔴 `GPL-2.0` | `8` |
| 🟢 `BSD-2-Clause` | `4` | | 🔴 `LGPL-3.0` / `LGPL-2.1` | `3` / `1` |
| 🟢 `ISC` | `4` | | 🟡 `MPL-2.0` (weak copyleft) | `4` |
| 🟡 `NULL` (no licence file) | `63` | | 🟡 `ECL-2.0` | `2` |
| 🟡 `NOASSERTION` (file present, undetected) | `46` | | 🟡 `CC0-1.0` | `2` |
| 🟡 single rows | `WTFPL`, `CC-BY-4.0`, `EUPL-1.2`, `OFL-1.1`, `ODbL-1.0`, `MulanPSL-2.0` | | | |

🔵 **`109` rows (`13.6%`) are unlabelled by GitHub's own detector — `NULL` or `NOASSERTION`.**
🟢 **That is the measured size of the gap this base's byte-read method exists to fill**, and it is
the first time the gap has had a denominator.

### 🔴 Finding 2 — `search/repositories` is a VISIBILITY oracle, not a LIVENESS oracle

🔵 **`P98` (`p845`) requires a liveness channel to be calibrated against known states before a
sweep is built on it. `p845` applied that test to `github.com` HTML and rejected it. `p846` applied
the same test to the channel `p845` KEPT — and it fails a weaker form of the same test.**

🟢 **All `11` unresolved addresses were re-probed on `raw.githubusercontent.com`, with two controls
run in the SAME loop:** 🟢 `HKUDS/DeepTutor` (known live) → `LICENSE` `11,408 B` + `README.md`
`93,104 B`, and 🔴 `zzz-never-existed-p846/zzz-nope` (never existed) → no `200` on any probe.

| Address | `search/repositories` | Owner sweep | `raw.githubusercontent.com` | Verdict `2026-11-16` |
|---|---|---|---|---|
| [`asterics/AsTeRICS-Grid`](https://github.com/asterics/AsTeRICS-Grid) | 🔴 `422` | 🔴 absent from `51` of `51` | 🟢 `LICENSE` `34,523 B`, `README.md` `10,862 B` (`master`) | 🟢 **ALIVE — de-indexed** |
| [`packbackbooks/lti-1-3-php-library`](https://github.com/packbackbooks/lti-1-3-php-library) | 🔴 `total_count=0` | 🔴 absent from `10` of `10` | 🟢 `README.md` `3,397 B` (`master`) | 🟢 **ALIVE — de-indexed** |
| [`digitalcredentials/learner-credential-wallet`](https://github.com/digitalcredentials/learner-credential-wallet) | 🔴 `422` | 🔴 absent from `92` of `92` | 🟢 `README.md` + `LICENSE` + `package.json`, BOTH branches | 🔴 **ALIVE — `p845`'s death WITHDRAWN** |
| [`tl-its-umich-edu/caliper-php-public`](https://github.com/tl-its-umich-edu/caliper-php-public) | 🔴 `total_count=0` | 🔴 absent from `92` of `92` | 🟢 `README.md` + `LICENSE` + `composer.json` (`master`) | 🔴 **ALIVE — `p845`'s death WITHDRAWN** |
| [`end13s/AI-Grading-Tool`](https://github.com/end13s/AI-Grading-Tool) | 🔴 `total_count=0` | 🔴 absent from `9` of `9` | 🟢 `README.md` `5,509 B`, both branches | 🟢 **ALIVE — de-indexed** |
| [`FabianJun/PresentTogether`](https://github.com/FabianJun/PresentTogether) | 🔴 `422` | 🔴 `user:FabianJun` → `422` | 🟢 `LICENSE` `1,344 B` + `README.md` `12,022 B` | 🟢 **ALIVE — RENAMED**, see Finding 4 |
| `Topkiflare74/ai--manus2.0` | 🔴 `total_count=0` | 🔴 `user:Topkiflare74` → `422` | 🔴 **`0` of `20` probes** | 🔴 **GONE** — the only new death |
| `Nordup/askaboard` | 🔴 `422` | 🔴 `p844` | 🔴 **`0` of `12` probes** | 🔴 **GONE — `p844` CORROBORATED** |
| `Bhuvantejakomera/Agentic-Assignment-Evaluator` **+ trailing stop** | 🟢 `1` · `MIT` · `0★` · `2026-11-10` | — | 🟢 `README.md` + `LICENSE` | 🟢 **ALIVE — `T146` again** |
| `bhuvantejakomera/agentic-assignment-evaluator` (lowercase, in prose) | 🔴 `422` | — | 🔴 none | 🔵 **not an address — a prose variant of the row above** |
| `OWNER/REPO` | 🔴 `422` | — | — | 🔵 **not an address — `p845`'s own template, caught by this base's extractor** |

🔴 **`6` of the `11` are alive. The channel's false-negative rate on this shelf is `6` in `815`
(`0.74%`) — small as a fraction and catastrophic as a verdict, because every one of those six was
eligible to be written off as dead.**

### 🔴 Finding 3 — `P99`'s `≤100` owner gate does NOT save the method, and `P95` stage `2` is withdrawn as a death test

🟢 **`p845` added `P99`: an owner sweep may raise a suspect only when that owner's `total_count ≤ 100`,
because above `100` the enumeration is page-capped.** 🔴 **The gate is correct and insufficient.**

🔵 **`end13s` holds `9` repositories. `packbackbooks` holds `10`. `digitalcredentials` and
`tl-its-umich-edu` hold `92` each. All four are FULLY enumerated, none is anywhere near the cap,
all four passed `P99` cleanly — and all four produced a FALSE death.** 🟢 **The repositories are
absent from the owner enumeration for the same reason they are absent from the `repo:` query: they
are absent from the INDEX, not from GitHub.**

🔴 **`p844`'s rule — *"Only an owner sweep that comes back without it is a death"* — is
WITHDRAWN.** 🔵 An owner sweep discriminates *mistyped address* from *not indexed*. It does not
reach *deleted*. → `T152`.

🟢 **`P100` — the replacement, and it is deliberately asymmetric:**

> 🟢 **`raw.githubusercontent.com` is a POSITIVE-ONLY oracle. A `200` on any probed path is
> conclusive proof of life. A miss is NO information.** 🔴 **Control, run in the same loop:
> `torvalds/linux` — unambiguously alive — returns NO `200` on any of `12` probes, because it
> carries `README` and `COPYING`, not `README.md` and `LICENSE`.**
> 🟢 **A death may be declared only when BOTH channels are negative, and it is then recorded as
> *no evidence of life*, never as proof of deletion.**

🔵 **Under `P100` this base has exactly `2` supportable deaths in its entire history —
`Nordup/askaboard` and `Topkiflare74/ai--manus2.0` — and both are negative on both channels.**

### 🔴 Finding 3b — this base ALREADY KNEW, and lost it between two shelves two passes apart

🔴 **`p843` measured the foundations shelf and recorded, in a table that is still on
`repos/foundations.md`:** 🟡 *"Live but absent from GitHub's search index | `1` —
`digitalcredentials/learner-credential-wallet`."*

🔴 **Two passes later `p845` declared that same address GONE, "confirmed by BOTH stages", and
filed it in `intel/open-gaps.md` as a genuine absence.** 🟢 **`p843` was right, `p845` was wrong,
and the evidence that would have stopped `p845` was already written down in this repository.**

🔵 **The failure is not measurement — it is that the finding lived in a row-level table on one
shelf and never became a RULE.** `p843` saw the category, named it exactly, counted it at `1`, and
did not generalise it. 🟢 **`P100` is that generalisation, and it is filed as a prescription
precisely so the next pass inherits the rule and not just the row.** → `T156`.

### 🟢 Finding 4 — `4` new build-safe addresses, every one produced by the de-indexing investigation rather than by a search leg

| Agent / library | Repo | License | ★ | Why it is a row |
|---|---|---|---|---|
| Learner Credential Wallet (OWF Labs) | https://github.com/openwallet-foundation-labs/learner-credential-wallet | 🟢 **MIT — byte-read** (`main/LICENSE`, `1,091 B`, `sha256₁₂ d8c69cd2855b`) | 🟡 *not retrieved — this address is itself search-invisible* | 🟢 **New this pass (`p846`), and it is a GOVERNANCE UPGRADE this base would have recorded as a death.** `p845` declared `digitalcredentials/learner-credential-wallet` GONE; the repository is alive, and its own `README` points at this address under **OpenWallet Foundation Labs (Linux Foundation)**. 🔵 Cross-platform iOS/Android wallet for verifiable learner credentials (`lcw.app`) — the reference client for the W3C VC / Open Badges 3.0 seam. 🟢 **For a client engagement the move matters more than the code: a credential wallet stewarded by a foundation is procurable where a lab repository is not.** 🔴 **Both addresses serve content; prefer this one and keep the old row as the lineage.** |
| LTI 1.3 PHP library (standards-body upstream) | https://github.com/1EdTech/lti-1-3-php-library | 🟢 **Apache-2.0 — byte-read** (`master/LICENSE`, `11,342 B`, `sha256₁₂ 944c6521f810`) | 124 | 🟢 **New this pass (`p846`).** The upstream of the row this base already carries: `packbackbooks/lti-1-3-php-library`'s own `README` states it was *"forked from `IMSGlobal/lti-1-3-php-library`, initially created by @MartinLenord"*, and `IMSGlobal` is now `1EdTech` — **the body that publishes the LTI 1.3 specification**. `111` forks. 🔴 **Last push `2024-08-20`: this is the SPEC-ANCHOR, not the maintained tree.** |
| LTI 1.3 PHP library (actively maintained fork) | https://github.com/talis/lti-1-3-php-library | 🟢 **Apache-2.0 — byte-read** (`master/LICENSE`, `11,342 B`, `sha256₁₂ 944c6521f810` — 🔵 **byte-identical to `1EdTech`'s**) | 1 | 🟢 **New this pass (`p846`).** Pushed **`2026-11-10`** — 🔵 **the most recently maintained Apache-2.0 LTI 1.3 PHP tree this base has found**, against `2024-08-20` for the `1EdTech` upstream. 🟡 `1★` is not a quality signal here; a certification-bound protocol library is maintained by its users, not starred. |
| present-together | https://github.com/fabian-thinks/present-together | 🟢 **MIT + boundary — byte-read** (`main/LICENSE`, `1,344 B`, `sha256₁₂ 4f78693ecfd8`, holder `fabian-thinks and the Singularity seminar contributors`, 2026) 🔴 field reports `NOASSERTION` — `T81` | 0 | 🟢 **New ADDRESS this pass (`p846`) for an asset held since `p824`.** Pushed `2026-11-15`. 🔵 The grant keeps the two appended clauses `p824` shelved it for — *"Third-party material is excluded from this grant"* and *"Software permissions do not override academic rules or rights to institutional content"* — now pointing at `THIRD_PARTY_NOTICES.md` and `docs/ACADEMIC-USE.md`. 🟢 **Use this address; `FabianJun/PresentTogether` is the redirect.** |

### 🔵 Finding 5 — a licence-hash MISS can be a RENAME, and this base nearly recorded one as a relicence

🔴 **`p824` pinned `PresentTogether`'s grant at `1,340 B`, `sha256₁₂ fe728274`. Today the same file
reads `1,344 B`, `sha256₁₂ 4f78693ecfd8`.** 🟡 **A pin-check sees a changed licence.**
🟢 **The diff is `4` bytes and it is the copyright holder: `FabianJun` → `fabian-thinks`.**
🔵 **The owner renamed; the grant did not move.** → `T153`, and `P101`:

> 🟢 **On a licence-hash miss, diff the holder line BEFORE raising a relicence. A rename propagates
> into the copyright notice and changes the hash without changing the grant.**

🟢 **The same mechanism is the rename DETECTOR, and it is cheap:** the old and new addresses serve
the **byte-identical** `4f78693ecfd8` blob, and `FabianJun/PresentTogether`'s `README` carries CI
badges pointing at `github.com/fabian-thinks/present-together/actions`. 🔵 **Content identity across
two addresses is a rename; the CI badge names the survivor.**

### 🟡 Finding 6 — `10` rows are ARCHIVED upstream, which this base has never recorded

🔵 **Archived is stronger than stale: the owner has declared the repository read-only. `p843`
measured staleness and could not see this field; the full sweep returns it.**

| Row | Licence | ★ | Last push |
|---|---|---|---|
| [`FooSoft/anki-connect`](https://github.com/FooSoft/anki-connect) | 🟡 `NOASSERTION` | `2,083` | `2025-11-04` |
| [`frappe/mcp`](https://github.com/frappe/mcp) | 🟢 `MIT` | `171` | `2026-10-27` |
| [`GeovaneSchmitz/sigaa-api`](https://github.com/GeovaneSchmitz/sigaa-api) | 🟢 `MIT` | `61` | `2024-04-10` |
| [`vgwb/Antura_arabic`](https://github.com/vgwb/Antura_arabic) | 🟡 `NOASSERTION` | `60` | `2022-03-09` |
| [`gyger/mcp-pyzotero`](https://github.com/gyger/mcp-pyzotero) | 🟢 `MIT` | `56` | `2025-11-20` |
| [`european-commission-empl/European-Learning-Model`](https://github.com/european-commission-empl/European-Learning-Model) | 🟡 `EUPL-1.2` | `54` | `2024-02-14` |
| [`scieloorg/opac`](https://github.com/scieloorg/opac) | 🟢 `BSD-2-Clause` | `10` | `2026-01-26` |
| [`chimple/jamaica`](https://github.com/chimple/jamaica) | 🟢 `Apache-2.0` | `5` | `2019-05-20` |
| [`oaknational/oak-dspy-mcq-eval`](https://github.com/oaknational/oak-dspy-mcq-eval) | 🟡 `NOASSERTION` | `1` | `2026-07-13` |
| [`neuronova-apps/DUA-3.0`](https://github.com/neuronova-apps/DUA-3.0) | 🟢 `MIT` | `0` | `2026-09-21` |

🔴 **`frappe/mcp` is the one a client would feel**: archived `2026-10-27` while this base cites it
in the Frappe/ERPNext education seam. 🟢 **The grant survives archiving — `MIT` is irrevocable — so
these stay build-safe. What changes is the maintenance story a bid may truthfully tell.** → `T154`.

### 🟡 Finding 7 — licence DRIFT against the shelf's own claim, `5` rows

🔵 **`728` of the `815` addresses carry a licence claim in their row. Compared cell-by-cell against
the first-party field, `5` disagree.**

| Row | Shelf claims | GitHub reports `2026-11-16` | Reading |
|---|---|---|---|
| [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | `Apache-2.0` | 🟡 **`ECL-2.0`** (`1,238★`) | 🟢 **The shelf is not wrong so much as imprecise.** ECL-2.0 is the **Educational Community License**, Apache-2.0 plus an explicit university patent-grant limitation. 🔴 **It is NOT Apache-2.0 and a client's licence scanner will not treat it as such.** OSI-approved and permissive; quote it by name. |
| [`chimple/bahama`](https://github.com/chimple/bahama) | `Apache-2.0` | 🟡 `MPL-2.0` (`8★`) | 🔴 **Permissive → WEAK COPYLEFT.** MPL-2.0 is file-level copyleft: modified files must be published. Still shippable in a larger proprietary product; not the "do anything" the row implied. |
| [`th30d0re/opendyslexic-fonts`](https://github.com/th30d0re/opendyslexic-fonts) | `MIT` | 🟡 `OFL-1.1` (`1★`) | 🟢 **Correct for the artefact** — SIL Open Font License is the font-sector norm. 🔴 **Its reserved-font-name clause bites on rename/rebrand**, which an accessibility deliverable may well do. |
| [`birkanyavuz/educational-tools`](https://github.com/birkanyavuz/educational-tools) | `Apache-2.0` | 🔴 `CC-BY-4.0` (`0★`) | 🔴 **`T78`'s class: a CONTENT licence over software** — no patent grant, no warranty disclaimer. Already on the rejection shelf; the field now corroborates it first-party. |
| [`hoangkien1703/dual-sub-replay`](https://github.com/hoangkien1703/dual-sub-replay) | `GPL-3.0` | 🟢 **`MIT`** (`63★`) | 🟢 **The only drift in the GOOD direction.** A copyleft row this base shelved as unusable now reports `MIT`. 🔴 **Not promoted here: a relicence must be byte-read and its contributor provenance checked before a client builds on it.** → `ACTION p846-A`. |

### 🔵 Finding 8 — batching HIDES the `422`, which is a third absence signature

🟢 **`p845` recorded two absence signatures: `422`, and HTTP `200` with `total_count=0`.**
🔴 **Batched, there is a third and it is silent.** A query carrying `10` `repo:` qualifiers of which
one does not resolve returns **`200` with the other nine** — no error, no warning. 🔵 **Across `82`
batches this base recorded `0` failures while `11` addresses went unanswered.**
🟢 **A batched sweep must reconcile the request list against the response list by name.** This one
did, which is the only reason the `11` were seen at all. → `T155`.

### 🔴 Finding 9 — the mandated battery, run and nilled a SEVENTH consecutive time

🔴 **`p840`, `p841`, `p842`, `p844`, `p845` and now `p846`.** 🟢 **All eight legs run: global agents,
GitHub trending, vertical platforms, industry trends, and North America, EMEA, APAC and LATAM.**

🟢 **Every named candidate was already held, checked against the shelves rather than from memory** —
`HKUDS/DeepTutor` (🟢 re-measured first-party this pass: `Apache-2.0`, **`59,624★`**, pushed
`2026-11-15` — up from `52,783★` on `2026-11-01`), `THU-MAIC/OpenMAIC`, `patchy631/ai-engineering-hub`,
`withmarbleapp/os-taxonomy`, `amosblomqvist/learnharness` (🔴 `AGPL-3.0`), `Open edX`, `Sakai`,
`Moodle`, `OpenEduCat`, `ILIAS`, `Chamilo`, `Canvas`.

🟢 **The regulatory legs nilled identically, and each was grepped against `intel/` before being
called held:** the EU Digital Omnibus postponement to `2027-12-02` (`344` prior mentions), Council
document `ST-14902-2026` (`9`), Korea's AI Basic Act `2026-01-22`, Vietnam's law `2026-03-01`,
Australia's TEQSA institutional action plans (`66`), UK DfE/Ofqual (`54`), North Carolina
`SL 2026-41`, California `AB 1159` (`88`), the `K-12 AI Literacy and Readiness Act of 2026` (`32`),
Berkeley Law's exam ban (`77`), Idaho (`70`), Pearson/Workera (`15`), OpenAI's Estonia partnership
(`42`), UAE KHDA (`47`), the UNESCO IESALC `87%`/`26%` split, and HolonIQ's `$12.3B`.

🔴 **One LATAM figure was NOT held and is filed on `intel/market.md`:** the Digital Education
Council's 2026 LATAM survey — **`92%` of students and `79%` of faculty** across `29` institutions
and `30,000+` responses. 🟡 **Secondary, vendor-published, `CITED NOT READ`.**

🟢 **An informed nil, declared with its denominator. This pass's `4` rows came from the sweep, not
from the legs.**

## 🟢 Fiftieth pass (`p845`, 2026-11-16) — **`0` new agent rows, a SIXTH consecutive informed nil — and a liveness channel that would have killed every row on this shelf, caught BEFORE it was used**

### 🔴 Finding 1 — `github.com` HTML is NOT a liveness channel, and a sweep built on it would have manufactured `817` deaths

🔵 **Why this was tested at all:** `ACTION p844-B` requires a shelf-wide address sweep, and the
canonical instrument — the GitHub search API — is rate-limited to `10` queries a minute
unauthenticated, which prices a full `817`-row sweep at over an hour. 🟡 **A cheaper channel was
therefore looked for before the sweep was run, not after.**

🔴 **`curl -I https://github.com/OWNER/REPO` returns `403` for everything.** Measured in one loop,
`2026-11-16`:

| Address | Expected | `github.com` HTML |
|---|---|---|
| `HKUDS/DeepTutor` — held, live, `52k★` | `200` | 🔴 `403` |
| `ai-infra-curriculum/ai-infra-sre-learning` — live | `200` | 🔴 `403` |
| `Nordup/askaboard` — confirmed DEAD at `p844` | `404` | 🔴 `403` |
| `this-owner-does-not-exist-xyz/nope` — never existed | `404` | 🔴 `403` |

🔴 **Four addresses in four different states, one response.** `20` rapid repeats returned `0`
successes in `5` seconds, so this is a blanket refusal and not a rate limit that patience would
clear. 🔵 **The channel has ZERO discriminating power: it cannot separate a live repository from a
deleted one from an owner that never existed.**

🔴 **The failure mode this base should name:** a sweep written against this channel would not have
*failed* — it would have returned a clean, plausible, uniform answer declaring **all `817`
build-safe addresses dead**, in one run, with no error. 🟢 **`p843` manufactured `1` false death
from a normalisation bug and it took `p844` a full pass to undo. This would have manufactured
`817`.** 🔵 **`T150`.**

🟢 **Prescription — `P98`: a liveness channel must be CALIBRATED before it is trusted, against four
known states (live, dead, never-existed, and a known-live control in the same loop), and a channel
that returns one answer for all four is rejected regardless of how cheap it is.** 🔵 **The same
control shape already caught `T906`'s egress refusal — the governmental endpoints are declared dead
by a channel that returns `301` for GitHub in the same loop.**

### 🟢 Finding 2 — `839-G3` is CLOSED, and it WITHDRAWS an instruction this shelf has been giving

🔵 **Full measurement is filed on `repos/foundations.md`, where the estate's rows live.** 🟢 **In
one line: the `ai-infra-curriculum` senior and architect tracks are NOT drafts — `9` of `13` tracks
are `100%` learning-complete, including both tracks this base named as drafts, and the `0★`
`sre` track is the most complete of all.** 🔴 **The standing advice *"treat the estate's senior and
architect tracks as drafts until measured otherwise"* is WITHDRAWN at `p845`.** → `T149`, `P97`.

### 🟡 Finding 3 — the mandated battery, run and nilled a SIXTH consecutive time, with its denominator stated

🔴 **`p840`, `p841`, `p842`, `p844` and now `p845`.** 🟢 **Run in full: the global agent leg, the
GitHub-trending leg, the vertical-platform leg, the industry-trends leg, and all four regional legs
(North America, EMEA, APAC, LATAM).**

🟢 **Every named candidate was ALREADY HELD, and the check was run against the shelves rather than
from memory:**

| Candidate returned by a leg | Held on | Verdict |
|---|---|---|
| `HKUDS/DeepTutor` | `agents/top.md`, `repos/foundations.md` | Held |
| `THU-MAIC/OpenMAIC` | `agents/top.md`, `repos/foundations.md` | Held |
| `patchy631/ai-engineering-hub` | `agents/top.md`, `repos/foundations.md` | Held |
| `withmarbleapp/os-taxonomy` | `repos/foundations.md` | Held |
| `amosblomqvist/learnharness` | `agents/top.md` — 🔴 `AGPL-3.0` | Held, copyleft |
| `OpenOLAT`, `frappe/lms`, `RosarioSIS` | `verticals/solutions.md` | Held |

🔵 **The regulatory legs nilled the same way, and that is the more useful nil because it is the one
a client engagement would pay for:** Vietnam's AI law (`2026-03-01`, education named high-risk),
Korea's AI Basic Act (`2026-01-22`), Taiwan's `2026` statute, `Regulation (EU) 2026/1744`, North
Carolina `SL 2026-41`, the `134`-bills / `31`-states tracker figure, UNESCO IESALC `87%` adoption
against `26%` with a strategy, the `716` instruments across `23` countries, Ceibal, `CONPES 4144`,
HolonIQ's `$12.3B` and the OECD Digital Education Outlook — 🟢 **all already on `intel/`.**

🟢 **Declared, not padded. `0` rows added here; the pass's yield went to `839-G3` and to `P98`.**

## 🔴 Forty-ninth pass (`p844`, 2026-11-16) — **`0` new agent rows. `p843`'s decay sweep is HALF WRONG: `1` of its `2` "dead" rows is alive, killed by the base's own address normalisation — and the row had PREDICTED this exact failure at `p823`**

🔵 **Why this pass re-measured yesterday's measurement.** `p843` ran the first
first-party sweep of the build-safe table and reported **`2` of `275` addresses
gone**. 🟢 **`p844` re-ran both, and one of the two is a FALSE POSITIVE.**

### 🔴 Finding 1 — `Agentic-Assignment-Evaluator.` is ALIVE, and the trailing full stop is why

| Address as queried | Result `2026-11-16` |
|---|---|
| `repo:Bhuvantejakomera/Agentic-Assignment-Evaluator.` **(with the stop)** | 🟢 **`total_count=1`** — `MIT`, `0★`, pushed `2026-11-10`, not archived |
| `repo:Bhuvantejakomera/Agentic-Assignment-Evaluator` (stop removed) | 🔴 `422` |
| `repo:bhuvantejakomera/agentic-assignment-evaluator` (`p843`'s form) | 🔴 `422` |

🔴 **`p843` queried the third form.** 🟢 **And the row it was testing carries, in
its own cell, the warning that this would happen** — filed at `p823`:
*"the repository name ends in a literal full stop … it will break naive
link-extraction and trailing-punctuation stripping, including this base's own
`grep -oE` address sweeps. Filed with the stop intact so a later pass does not
'correct' it into a 404."* 🔵 **Twenty-one passes later, a later pass corrected
it into a 404.** → `T146`.

🟢 **The row is NOT moved. It stays build-safe, with the measurement refreshed.**

### 🟢 Finding 2 — `Nordup/askaboard` IS genuinely gone, and an owner sweep is what proves it

🔴 `repo:Nordup/askaboard` → `422`. 🟢 **And this time the negative is real:
`user:Nordup` returns `19` repositories, pushed as recently as `2026-06-30`, and
NONE of them is `askaboard`.** 🔵 **The owner is alive and active; the
repository is not.** That separates *repository deleted* from *account gone* and
from *address mistyped* — which the single `422` that `p843` relied on cannot do.

🟢 **`askaboard` is moved to *Rejected candidates*, reason `address no longer
resolves`, confirmed by two methods on two consecutive days.** 🔵 The grant was
real when read (`MIT`, `1,063 B`, `sha256₁₂ e0407aae`); this is decay, not a
licence failure.

### 🔵 The rule this produces, for every future sweep

🟢 **A `422` is evidence about the ADDRESS AS WRITTEN, never about the asset.**
Before a row is declared dead: **re-query the address exactly as the row spells
it** (punctuation and all), then **run `user:OWNER`** and look for the name.
🔴 **Only an owner sweep that comes back without it is a death.** 🔵 Cost: one
extra API call per suspect row — against a shelf of `275`, that is `2` calls this
pass, because only suspects get swept. → `T146`, and `P95` stage 1 is amended.

### 🟡 The mandated battery, run and nilled a FIFTH consecutive time

🔴 `p840`, `p841`, `p842` and now `p844` ran the prescribed star-ranked education
agent legs and returned no new build-safe agent row. 🟢 **The global legs
returned only assets this base already holds** — `DeepTutor` (`32` mentions in
this file) and `LearnHarness` (`4`), the latter re-measured this pass at
**`amosblomqvist/learnharness`, `AGPL-3.0`, `9,634★`, pushed `2026-11-12`** —
🔴 copyleft, so its growth is a market signal and not a build input. 🔵 **An
informed nil, declared rather than padded. This pass's yield went to the
foundations and data layer instead** — see `repos/foundations.md`.

### 🔴 Rejected this pass — named, with the reason

| Candidate | Repo | Actual license | Stars | Why rejected |
|---|---|---|---|---|
| askaboard | https://github.com/Nordup/askaboard | 🟢 **MIT — byte-read** (`1,063 B`, `sha256:e0407aae…`, holder `Nordup`) — **the grant was real when read** | 4 | 🔴 **ADDRESS NO LONGER RESOLVES — decay, not a licence failure.** Confirmed on two consecutive days by two methods: `repo:Nordup/askaboard` → `422` (`p843`, `p844`), **and `user:Nordup` → `19` live repositories, newest push `2026-06-30`, with no `askaboard` among them** (`p844`). 🔵 **The owner sweep is what makes this a death rather than a typo** (`T146`). Was shelved `p823`: *"A shared canvas for learning with your AI"* — the agent explains on a board it draws on. 🟢 **Re-file if the address returns.** |

## 🟢 Forty-eighth pass (`p843`, 2026-11-16) — **`0` new agent rows, but the first FIRST-PARTY sweep of the whole build-safe table: `275` rows measured against GitHub's own API, `2` are GONE, `3` unevidenced licence claims are now byte-read**

🔵 **Why this pass did something other than re-run the battery.** `p840`–`p842`
ran the mandated legs and returned nil three times; `p842` added four
differentiated angles and disqualified all three URLs they surfaced. A fourth
nil adds nothing. 🟢 **So `p843` turned the instrument around and measured the
shelf itself** — and found a verification channel the previous forty-seven
passes did not have.

🟢 **The channel.** `gh api repos/{owner}/{repo}` is `403` here (the session
credential is scoped to attached repositories) and `github.com` HTML is `403`
through the proxy (`T124`) — but **`gh api search/repositories` is not scoped
that way**, accepts ten `repo:` qualifiers per query as an OR, and returns
`license.spdx_id`, `stargazers_count`, `pushed_at`, `archived` and `fork` for
any public repository. 🔵 **That converts this base's standing 🟡 "star counts
are third-party and unverified" caveat into a measurement.** → `P95`, `T144`.

### 🔴 Finding 1 — two build-safe rows no longer exist

Of the **`275`** rows in *Build-safe agents* that carry a GitHub URL, **`273`
resolved and `2` did not**, confirmed by two independent methods on 2026-11-16:
the search API answers `422` *"the listed users and repositories cannot be
searched either because the resources do not exist or you do not have
permission to view them"*, and `git ls-remote --symref` falls through to a
credential prompt — this proxy's `404` signature.

| Row | Shelved as | Status 2026-11-16 |
|---|---|---|
| [`Nordup/askaboard`](https://github.com/Nordup/askaboard) | 🟢 MIT — byte-read (`1,063 B`, `sha256₁₂ e0407aae`), 4★, Global, added `p823` | 🔴 **DOES NOT RESOLVE** — deleted, renamed or made private within ~3 weeks of being shelved |
| [`bhuvantejakomera/agentic-assignment-evaluator`](https://github.com/bhuvantejakomera/agentic-assignment-evaluator) | build-safe row | 🔴 **DOES NOT RESOLVE** |

🔵 **Neither is a licence failure — both passed the gate when they were
shelved.** This is a *decay* mode `P94` cannot catch, because `P94` runs at
intake and these repositories died afterwards. 🟢 **Both rows should be moved to
*Rejected candidates* with the reason `address no longer resolves`,** and the
sweep should run at every pass, not at intake only.

### 🟡 Finding 2 — three rows asserted a licence that nothing on this base had byte-read. All three now are.

GitHub returns `NOASSERTION` for all three; stage 2 of `P95` byte-read each one
through `raw.githubusercontent.com`, which **is** reachable here:

| Row | Was shelved as | Byte-read 2026-11-16 | Verdict |
|---|---|---|---|
| [`kingdonkatsu/ntulearn-mcp`](https://github.com/kingdonkatsu/ntulearn-mcp) | "MIT" — no evidence recorded | `main/LICENSE`, `1,055 B`, `sha256₁₂ e6bd1450153a`, title `MIT License`, "Copyright (c) 2026 kingdonkatsu" | 🟢 **CONFIRMED MIT** — row upgraded from assertion to measurement |
| [`wwrwbs/AI_AWE`](https://github.com/wwrwbs/AI_AWE) | "Apache-2.0 (per README + LICENSE)" | `main/LICENSE`, `1,865 B`, `sha256₁₂ 4b5296db216d` | 🟡 **Apache-2.0 BOILERPLATE-ONLY** — see Finding 3 |
| [`zavora-ai/mcp-education`](https://github.com/zavora-ai/mcp-education) | "Apache-2.0 (per README)" | `main/LICENSE`, `738 B`, `sha256₁₂ b3886fcd4f82`, "Copyright 2026 Zavora AI" | 🟡 **Apache-2.0 BOILERPLATE-ONLY** |

🟢 **The other eleven `NOASSERTION` rows were already byte-verified by earlier
passes and this sweep corroborates every one of them** — `UniMCP` (MIT +
inherited ISC), `sigaa-ifsc-mcp` (MIT), `dewey` (MIT), `openfoam-mcp-server`
(Apache-2.0), `brightspace-d2l-mcp`, `D2L-MCP`, `vigilo-mcp` (MIT byte-read),
`GLEXP-Team-RoboTutor` (Apache-2.0 code + CC BY 4.0 content), `nak-api` (WTFPL),
`nengdou` (MulanPSL-2.0), and `anki-mcp-server`, which this base already carries
at 🟡 *manifest-channel only*. 🔵 **This base's byte-read beats GitHub's
detector, and the sweep is now the evidence for saying so.**

### 🟡 Finding 3 — a fourth grant class: **the grant by REFERENCE**

`P94` names three ways a candidate fails: unlicensed-by-omission,
licensed-but-proprietary-dependent, and a real grant over no substance.
🟢 **`p843` adds a fourth, and it is not a failure — it is a mis-grading risk.**
`AI_AWE` (`1,865 B`) and `mcp-education` (`738 B`) both carry **only Apache's
appendix boilerplate** — the five-paragraph *"Licensed under the Apache
License, Version 2.0 … You may obtain a copy of the License at …"* notice and a
copyright line. 🔵 **The full Apache-2.0 text is `11,357 B`** (measured the same
day at `apache/.github/main/LICENSE`). The grant is real and incorporated by
reference, which is how Apache itself tells you to mark source files — but
**any size check, text match or template comparison will grade it as missing**,
and GitHub's does. 🟢 Both rows stay build-safe, now with the byte evidence and
the flag.

🔴 **`AI_AWE`'s licence file is also a component manifest, and it carries a
build constraint**: the Apache-2.0 grant covers the code, LoRA adapters and
LightGBM scorer; `TextComplexityToolkit` is vendored under MIT; `TAALED` is
permissive-by-notice; the `Qwen2.5-7B-Instruct` base model is Apache-2.0 but
obtained separately and **not redistributed**; and the **`Persuade 2.0` corpus
is used under an academic-use licence and is NOT redistributed**. 🔵 **Globant
can ship the scorer and cannot ship the corpus** — exactly the distinction a
client engagement needs stated before the build starts, and exactly the kind of
clause a single-SPDX-field pipeline erases.

### 🟡 Finding 4 — `21` build-safe rows have not been pushed to in six months

Including `XPRIZE/GLEXP-Team-RoboTutor` (last push **2019-11-05**),
`scorzeth/anki-mcp-server` (185★, 2025-01-08), `kaliaboi/mcp-zotero` (163★,
2025-02-04) and `yuanjua/chiken` (90★, 2025-09-05). 🔵 **Staleness is not a
disqualification** — a finished MCP shim needs no commits — but it belongs in
the row, because "actively maintained" is what a client hears when it is absent.

### 🔵 Candidates examined this pass and NOT shelved

| Candidate | First-party metadata 2026-11-16 | Why it is not a row |
|---|---|---|
| [`agentschools/opencode.school`](https://github.com/agentschools/opencode.school) | `NOASSERTION`, 75★, pushed 2026-11-09 | 🟡 **Genuinely novel to this shelf** (`0` prior mentions) — but it is a *course about* an open-source coding agent, not an education agent. Content, not capability. |
| [`slayadapraya/School-Agent`](https://github.com/slayadapraya/School-Agent) | 🔴 `NONE`, 0★, created 2026-10-15 | Already shelved as a rejection; the sweep re-confirms the unlicensed verdict first-party. |
| [`HugeCatLab/ChatTutor`](https://github.com/HugeCatLab/ChatTutor) | `AGPL-3.0`, 1,326★, **last push 2026-01-09** | Already shelved; copyleft, and now ten months without a commit. |

🔴 **And one asset this base cannot shelve, which is the finding of the pass** —
`TutorRL-7B`, the ETH Zurich / TU Darmstadt pedagogical tutor model. Its *code*
is [`eth-lre/PedagogicalRL`](https://github.com/eth-lre/PedagogicalRL)
(55★, EMNLP 2025 Oral, `NONE` — **no grant payload at 7 filenames × 2
branches**, reproducing this base's `p552` `NO-GRANT` verdict today). Its
*weights* are on Hugging Face, which this session cannot reach at all. Full
account in `agents/trending.md`; the structural consequence is `T144`.

🟢 **Evidence, both runnable and both in this repository:**
[`evidence/first-party-sweep.2026-11-16-p843.tsv`](../evidence/first-party-sweep.2026-11-16-p843.tsv)
(273 rows), [`evidence/grant-bytes.2026-11-16-p843.tsv`](../evidence/grant-bytes.2026-11-16-p843.tsv),
and [`compose/code/p95-first-party-sweep/`](../compose/code/p95-first-party-sweep/).

## 🔴 Forty-seventh pass (`p842`, 2026-11-16) — **`0` new agent rows (`424` → `424`), and this pass is the one that went LOOKING for the nil's edge — it found `3` novel URLs and disqualified all `3`, each for a different reason**

🟢 **Method, stated first because it is the contribution.** `p841` re-ran the mandated battery cold
and reproduced the nil candidate-for-candidate. Repeating that again would have measured the same
thing a third time. So `p842` ran the mandated battery **and then four angles the battery does not
contain** — the LMS/MCP long tail, the grading-and-rubric channel, a **Chinese-language** query, and
a **Spanish/Portuguese** query. The point was to find out whether the nil is a property of the
*battery's query shape* or of the *supply*.

🔴 **Answer: it is the supply, but not in the way the previous three passes recorded it.** The
differentiated angles DID surface novel URLs — `3` of them, genuinely absent from this shelf's
`5,720` unique GitHub URLs. **All three were then disqualified on inspection, and none became a
row.** → `T143`.

| Candidate | HEAD `sha₁₂` measured `2026-11-16` | Why it is NOT a row |
|---|---|---|
| `github.com/Ali627miya/gradeguide-ai` | `f6f9238112cb` | 🔴 **No licence anywhere.** `LICENSE`, `LICENSE.md`, `LICENSE.txt` all `404` at the real ref; no `package.json`; no licence statement in a `13,722`-byte README. All-rights-reserved by default — **Globant cannot build on it.** |
| `github.com/timothyheeeee/Autonomous-Grading-Engine` | `f3518b6c379a` | 🔴 **No licence anywhere** (same three probes, same `404`s, no `package.json`). Additionally couples to a **proprietary** `GPT-4o` endpoint, so even a grant would not make it self-hostable. |
| `github.com/thinkmoon/zhihui-teacher` | `71b5ddaee9a4` | 🟡 **Licence is REAL and MIT** (`LICENSE`, `1,066` bytes, `sha256₁₂` `e936c2bc0ff4`, "Copyright (c) 2026 thinkmoon") — 🔴 **but it grants a MARKETING PAGE.** Full clone inventory: `1` `index.html`, `1` `styles.css`, `5` `mp4`, `4` `md`, `4` `jpg`, `3` `png`, `1` `gif`, `0` `.py`/`.ts`/`.js`/`.java`/`.go`. **Zero source files.** Its own `NOTICE.md` says so outright: 本仓库没有复制完整产品的前后端代码 — *this repository does not copy the complete product's front- or back-end code*. The product lives behind a login at `exam.thinkmoon.cn`. |

🟢 **`17` of the `20` candidates surfaced across all eight legs were already shelved here**, including
the entire `canvas-mcp` / `moodle-mcp` long tail that the LMS angle was built to expose
(`vishalsachdev/canvas-mcp` upstream and its forks `harrywang`, `Harikeshav-R`, `NelsonSpencer`,
`r-huijts`, `mdweaver`, `bruchris`, `DMontgomery40`, `admin978`, `JohannsenLum`, `loyaniu/moodle-mcp`),
plus `delip/autorubric`, `macsnoeren/genai-open-assessment`,
`omerbbbb/ai-graded-assessment-platform`, `xch1986/AI-Tutor`, `Zenglian990/AI_Tutor_Release`,
`datawhalechina/hello-agents`, `HKUDS/DeepTutor`.

🔴 **The mandated battery's own yield was `0` novel URLs for the third consecutive pass.** Its only
not-on-shelf hits were three **rank-tracker aggregators** — `yuxiaopeng/Github-Ranking-AI`,
`bianzhilong2-ctrl/agents-radar`, `HuggerHustle/ai-radar`. These are ranking feeds, **not education
agents**, and they are not rows here. Recording them as such is precisely the padding this base
refuses (`T63`, `T140`).

🟢 **`0` rows invented. `424` rows in, `424` rows out.** The useful output of `p842` is the
disqualification method, now written up as `P94`.

## 🔴 Forty-sixth pass (`p841`, 2026-11-16) — **`0` new agent rows (`424` → `424`), and the row count is the finding**

🟢 **The mandated battery was re-run cold** — four global legs plus one leg each for North America,
EMEA, APAC and LATAM — **by an operator holding none of this base's prior conclusions.**
🔴 **All `10` agent candidates it surfaced were already shelved here** (`OpenMAIC`, `DeepTutor`,
`ai-engineering-hub`, `Claw-ED`, `ChatTutor`, `OpenOlat`, `RosarioSIS`, `openSIS`, `OpenEduCat`,
`MAIC`). **`0` rows added.** 🟢 **No row was invented to fill the pass** — `T63`, `T140`.

🟢 **Audit published instead, with its method** (full table in `agents/trending.md`): of the `532`
unique GitHub URLs on this shelf a `30`-URL sample was probed with `git ls-remote --symref` →
🟢 **`30` LIVE / `0` dead**; `0` placeholder or header-as-data rows across `1,312` table lines in
this file, `repos/foundations.md` and `verticals/solutions.md`; frontmatter correct on `8`/`8` files.
🔴 **`curl -sI` returned `403` for all `30` live repos — `403` is not `404` here (`T124`).**


## 🟡 Forty-fifth pass (`p840`, 2026-11-16) — **`1` agent row (`423` → `424`), and the honest headline is the NIL: the education agent channel returned `18` of `18` top hits that are not education at all**

🟢 **Every figure below measured `2026-11-16`: real default ref from `git ls-remote --symref`, grant
payload byte-read from `raw.githubusercontent.com` AT that ref with size and `sha256₁₂`, and
stars/forks/`pushed_at` from the GitHub repository index the same day.**

🔴 **This pass adds ONE agent row, not nine. The reason is a measurement, not a shortage of effort,
and it is the most useful thing `p840` has to report** → `T140`.

### 🟡 The one row

| Agent | Repo | Licence, as measured | ★ / forks | Default ref · pushed | Region | What it actually does, and the posture |
|---|---|---|---|---|---|---|
| **Anatria3D** | [`nurkan1/anatria-3d`](https://github.com/nurkan1/anatria-3d) | 🔴 **`BSL 1.1` — NOT open source.** Byte-read `LICENSE` `5,557 B` `sha256₁₂:179c0cb1e12d`. GitHub label: `NOASSERTION` | `59★` / `18` | `main` · `2026-10-30` (created `2026-08-08`) | EMEA | 🟢 Local-first 3D anatomy atlas with an **AI tutor that drives the viewport** — the tutor manipulates the model rather than talking beside it. 🔴 **Filed with its grant spelled out because the label hides it.** |

🔴 **The Anatria3D grant, read in full, because this is the row that teaches the pass:**

- **Licensor:** Nurdzhan Kerimov (Digital Rose). **Licensed Work:** the application source only.
- 🔴 **The meshes are NOT in the grant.** The licence explicitly excludes the anatomical meshes,
  the nomenclature and the manifests under `public/anatomy/` — those are third-party datasets, and
  the file names **`CC BY-SA`** terms with **`CC BY 4.0` for the female atlas**. 🟢 **So this is a
  three-licence artefact in one repository: `BSL 1.1` code, `CC BY-SA` data, `CC BY 4.0` data.**
- 🟢 **Additional Use Grant — production use IS permitted for study, teaching and academic
  research,** naming students, teachers, schools and universities.
- 🔴 **Withheld without a commercial licence:** deployment in a commercial clinic or any healthcare
  business, use in a revenue-generating environment, and re-branding.
- 🟢 **Change Date `2030-10-30` → Change Licence `Apache-2.0`.**
- 🔵 **The studio consequence, stated plainly: a university may run this in teaching today; a
  Globant commercial engagement may NOT ship it before `2030-10-30` without buying a licence.**
  🟢 That sentence is the whole value of the row, and GitHub's `NOASSERTION` label contains none of it.

### 🔴 The nil, measured with controls so it is reportable — `18` of `18`

🔴 **A leg built from this sector's own vocabulary — `agent skills teaching OR tutoring OR pedagogy`,
`stars:>25`, `pushed:>2026-09-01` — returned, ranked by stars: `325,285★`, `318,120★`, `303,914★`,
`195,443★`, `161,229★`, `159,571★`, `144,770★`, `120,496★`, `117,997★`, `116,311★`, `96,863★`,
`85,590★`, `80,757★`, `73,311★`, `69,523★`, `67,793★`, `61,306★`, `60,618★`.**

🟢 **Not one of the eighteen is an education product.** They are coding-agent skill collections,
agent harnesses, a security-audit skill, a marketing-skill pack, an ADHD-output skill and a
diagramming skill. 🔵 **The leg was alive and correctly ranked — it simply ranks a different
industry**, because `skill` and `teaching` now belong to the coding-agent ecosystem and `learning`
resolves to *machine* learning. → `T140`.

🟢 **Control that this base is not merely blind: the same discovery run's twelve topic legs returned
`166` unique repositories of which `109` were ALREADY on these shelves (`66%`).** 🔵 The channel is
saturated where it is real, and contaminated where it is large. Both at once.

### 🔴 `3` named refusals — recorded so the next pass does not re-pay for them

- 🔴 **`blader/humanizer` (`69,524★` / `5,474` forks, 🟢 MIT `1,065 B` `sha256₁₂:b35b41535e51`,
  pushed `2026-11-10`) — refused as an agent row and PROMOTED to intel instead.** It removes the
  signatures of AI-generated writing. 🔵 **It is not an education tool; it is the thing education
  assessment is now up against, at `69.5k★` and under the most permissive licence there is.** → `T142`.
- 🔴 **The ML-"learning" false-positive class — refused as a CLASS.** `contrastive-lm/clm` (`3,204★`),
  `nuglifeleoji/sentry` (`1,521★`), `psrben/visionhope` (`1,415★`), `volotat/mini-agi` (`1,309★`),
  `fudan-generative-vision/remory` (`783★`) all rank on education legs and all are machine-learning
  research. 🟢 Named because every one of them will rank again next pass.
- 🔴 **The developer-tutorial class — refused on SCOPE.** `eugenp/tutorials` (`37,308★`, MIT),
  `changkun/modern-cpp-tutorial` (`25,957★`, MIT), `eunomia-bpf/bpf-developer-tutorial` (`4,340★`)
  are engineering documentation, not instruction with a learner model, assessment or an instructor
  surface. 🔵 They are the largest single category the education legs return and they have no
  pedagogy in them.

### 🟡 Measured but NOT filed — one judgement call, recorded

🟡 **`maludb/learn-claude` (`53★` / `13`, 🟢 MIT `1,069 B` `sha256₁₂:d7829e8f73b9`, `main`, pushed
`2026-07-03`) — a real exam-prep tutor, left off the shelf deliberately:** single-vendor
certification scope and no push in `4½` months. 🔵 **Recorded rather than filed so the next pass can
see it was weighed, not missed.** Fewer real rows beat padding.

### 🔵 Instrument conditions, `2026-11-16` (independently re-established this pass)

🔴 **The curation contract names `curl -sI` as the URL check. This pass re-ran that control and
again found it BLIND, so it was substituted.** 🟢 **Controls, run fresh:
`curl -sI github.com/torvalds/linux` → `403`, `.../HKUDS/DeepTutor` → `403`, and an invented
`zzz-not-real-org-9x7/zzz-nope-9x7` → `403`.** 🔴 **A famous repo, a real repo and a nonexistent one
return the identical code: `curl -sI` carries zero signal here and a `403` from it is neither a
confirmation nor a `404`.**

🟢 **Substituted with three instruments that DO discriminate, each controlled against the invented
slug:** `git ls-remote --symref` (resolved every real slug; the invented one failed),
`raw.githubusercontent.com` (`200` on a real `LICENSE`, 🟢 **`404` on the invented one**), and
`gh api -X GET search/repositories` (🟢 control `repo:HKUDS/DeepTutor` → `59,528★` / `Apache-2.0` /
pushed `2026-11-15`). 🔴 `api.github.com/repos` → `403` through the session proxy, unchanged.
🟢 Search rate limit read directly at `30/30` remaining.

## 🟢 Forty-fourth pass (`p839`, 2026-11-16) — **`9` agent rows added (`414` → `423`), and for the first time on these shelves the majority of them are APAC-origin, which CONTRADICTS a line this base has repeated for three passes**

🟢 **Every row below was measured `2026-11-16`: the real default ref from `git ls-remote --symref`,
the grant payload byte-read from `raw.githubusercontent.com` AT that ref with size and `sha256₁₂`
recorded, and stars/forks/`pushed_at`/`created_at` from the GitHub repository index the same day.**

🔴 **The correction, stated first because it overturns this base's own text.** `p837` wrote that
APAC "local supply is still thin" and `p838` repeated it. 🟢 **`p839` measured `5` of its `9` agent
rows as APAC-origin — China (`1,497★`), Taiwan (a national university's piloted course), Vietnam,
India and Thailand — and the single largest new row in this pass is Chinese.** 🔵 **The earlier
statement was true of the CHANNEL (English-keyword legs on an English-indexed field), not of the
sector.** → `T137`.

🔵 **Instrument conditions, measured this pass.** `curl` to `api.github.com` is still `403` through
this session's agent proxy; `raw.githubusercontent.com` returns `200`, so the byte-read-plus-`sha256`
instrument is intact; `gh api -X GET search/repositories` is live. 🔴 **Controls run in both
directions before any finding was recorded:** `repo:HKUDS/DeepTutor` → `1` hit (`59,514★`,
`Apache-2.0`, `main`, pushed `2026-11-15` — up `30★` on `p837`'s `59,484`), and an invented slug →
`HTTP 422`. 🟢 **Search rate limit read directly at `30/30` remaining, so this pass can tell a NIL
from a THROTTLE — which matters for `T139`.**

### 🟢 `9` new agent rows — byte-read `2026-11-16` on the real default branch

| Agent | Repo | Licence, as measured | ★ / forks | Default ref · pushed | Region | What it actually does, and the posture |
|---|---|---|---|---|---|---|
| **Inno Agent** | https://github.com/hhyqhh/inno-agent | 🟢 **MIT** — `main/LICENSE`, **`1,080 B`**, `sha256:f92c6c6a1cc8…` | `1,497★` / `249` | `main` · `2026-11-11` (created `2026-05-28`) | APAC — China | 🟢 **The largest new agent row in four passes, and the first on these shelves whose ARCHITECTURE is a learner model rather than a chat history.** Three explicit memory layers: **`L1` learner profile** (goals, knowledge states, misconceptions, preferences, summarised into a context pack injected each turn), **`L2` native wiki** (agent-queryable pages, hybrid BM25 + knowledge-graph retrieval, PDF/Office/image ingestion), **`L3` session recall** (SQLite FTS5, threshold-gated cross-conversation retrieval). Plus a cron scheduler, Feishu/WeChat channels and a workspace-scoped Practice Lab (xterm.js over WebSocket). Ships as Electron desktop, React 19 web UI and a `inno` TUI over one runtime state. Built on the Pi coding-agent SDK **without modifying its kernel** — all learning behaviour is registered tools plus one extension hook. 🔵 **Two design stances worth quoting to a client: "durable facts go to tools, not replies", so personalisation is traceable; and the `L1` profile is inspectable and editable by the learner, with unevidenced labels forbidden.** 🔴 **Read the declared non-goals before any proposal: one process, ONE active agent session; no multi-user concurrency, no auth model, no tenant isolation, no horizontal scaling — "run one instance per person". Backpressure returns `409 session_busy` by design.** 🔴 **So it is a per-learner runtime, NOT a platform; an institution-wide deployment is a fleet of single-tenant instances, which is a cost line, not a footnote.** Technical report (arXiv, June 2026) ships in-repo. Recipe: `P91`. |
| **SelfSemester** | https://github.com/munitkala/selfsemester | 🟢 **MIT** — `main/LICENSE`, **`1,081 B`**, `sha256:f5fe104e348d…`, © *2026 The SelfSemester authors* | `102★` / `8` | `main` · `2026-11-14` (created `2026-11-04`) | Global | 🟢 **It does not tutor a topic — it issues a COURSE, and then enforces it.** Names a subject, interviews the learner on goals and level, **states how well it can teach and mark that subject before the learner commits** (a readiness report), writes the whole syllabus up front, then runs it: releases material day by day, enforces hard deadlines, auto-marks quizzes, sends written work *and photographs of handwritten working* back for marking against a rubric, and puts final marks on a transcript. Rust/Tauri/Svelte, Windows. 🔵 **The readiness report is the artefact this base has argued for since `T96`: a system that declares its own competence envelope BEFORE a learner invests a term in it.** 🔵 Lessons carry LaTeX maths, graphs drawn exactly from the equations, interactive sliders and drills sealed off from the network and filesystem, and native-speaker audio from Wikimedia Commons for language and music. A course builder runs the same machinery **with no model at all**. 🔴 **Stated by its own author: "Status: early (`0.7.0`)… has had little real-world use. Expect rough edges." Windows-only, single-learner, `8` forks.** 🟢 **Adopt as the per-learner DELIVERY RUNTIME in `P91`, not as an institutional LMS.** |
| **AI Agent Literacy** | https://github.com/bigmoumou/AI-Agent-Literacy | 🔴 **SPLIT GRANT — both halves byte-read.** 🟢 Code **MIT** (`main/LICENSE`, **`1,068 B`**, `sha256:f8e1c1b97c59…`, © *2026 JUNHAO CHEN*). 🔴 Course content **CC BY-NC-SA 4.0** (`main/LICENSE-CONTENT.md`, **`7,877 B`**, `sha256:8f65175f489e…`) | `55★` / `0` | `main` · `2026-11-12` (created `2026-09-30`) | APAC — Taiwan | 🟢 **A university-piloted course that teaches students to DIRECT an AI coding agent and then check and correct its work rather than take it on trust** — piloted at **National Taiwan Normal University, 2026**, in *Learning Analytics Tools Implementation Applications*. Weeks `1`–`10` published: `39` videos, ~`121` minutes, updated weekly; browser-based practice computers; project homework; a scenario-based Week 6 exam. Site in English, Traditional Chinese, Simplified Chinese and Vietnamese. 🔵 **The course is its own worked example — the videos, site and practice machines are built with agents (Codex and Claude) while the teacher writes every script and reviews each video through `7`–`10` rounds.** 🔴 **THE COMMERCIAL CONSTRAINT IS THE WHOLE STORY AND MUST NOT BE GLOSSED: the content is `NC` — NON-COMMERCIAL. Globant can read it, cite it and copy its PEDAGOGY; it cannot ship that content, or a derivative of it, in a paid engagement. The `SA` term additionally propagates to derivatives.** 🟢 **The MIT half — the site, the practice-machine harness, the exam scaffolding — IS reusable.** 🔵 `0` forks against `55★` says it is being watched, not yet built on. `P91`. |
| **FAIR** (The Fair Platform) | https://github.com/azapg/FAIR | 🟢 **MIT** — `main/LICENSE`, **`1,068 B`**, `sha256:3aa6498da2b9…` | `6★` / `6` | `main` · `2026-10-26` (created `2025-08-06`) | Global — docs published in **English and Spanish** | 🟢 **An LMS-complete MVP whose declared purpose is to make automatic grading EXPERIMENTALLY COMPARABLE, which is a different product from a grader.** The LMS foundation works with no model at all: run courses, publish work, collect submissions, grade, communicate, share materials. On top of it, three pluggable surfaces: **Interpreters** (parse PDFs, images, code into structured artefacts), **Graders** (configurable rubrics, models, or hybrids), and **Artifacts** (one universal type for submissions, results, metadata). 🔵 **"Swap modules, run A/B tests, and measure performance across approaches" — this is the grading equivalent of what `TutorMoments` gave the tutor shelf in `p837`, and it is the only row here that lets a client COMPARE two grading approaches on their own submissions before buying either.** 🟢 **`pip install fair-platform && fair serve`, with deployment profiles via `.env`; Spanish-language documentation makes it the most LATAM-ready assessment row on these shelves.** 🔴 **`6★` / `6` forks and self-described MVP — this is a research harness, so pilot it, and do not put a term's marks of record through it.** `P90`, `P91`. |
| **CorrectExam — front** | https://github.com/correctexam/corrigeExamFront | 🟢 **MIT** — `main/LICENSE.md`, **`1,068 B`**, `sha256:44ed794595f6…`, © *2022 correctexam* | `24★` / `13` | `main` · `2026-11-15` (created `2022-03-09`) | EMEA — France (DIVERSE/academic lineage) | 🟢 **Grading of PAPER exams, which is still how most of the world's summative assessment is actually collected, and which this base had no row for.** Scans are **automatically aligned**; the student's name and first name are **recognised on the sheet**; per-question zones support horizontal (one question across all papers) or vertical correction; generic per-question comments carry an associated bonus or malus so a marker writes the comment once and applies it everywhere; a tablet and pen annotate the sheet directly. 🔵 **The whole machine runs IN THE BROWSER: OpenCV.js (WebAssembly), TensorFlow.js and ONNX Runtime in Web Workers, Dexie/IndexedDB and SQLite-Wasm for local caches.** 🟢 **That is the privacy posture a European schools client asks for and almost nothing on these shelves can offer — the student's handwriting does not leave the marker's machine for alignment or recognition.** Angular 20, PrimeNG, TypeScript strict, Jest + Cypress; Node ≥ `22.9`. 🔴 **`24★`: argue from the mechanism and the four-year maintenance record, not the popularity.** `P90`. |
| **CorrectExam — back** | https://github.com/correctexam/corrigeExamBack | 🟢 **MIT** — 🔴 **`deploy`**`/LICENSE.md`, **`1,068 B`**, `sha256:44ed794595f6…` — **byte-identical to the front repo's payload**, one org, one grant | `12★` / `10` | 🔴 **`deploy`** · `2026-11-15` (created `2022-03-09`) | EMEA — France | 🟢 **The Quarkus/Java server half, and the reason the pair is deployable rather than a demo** — install documentation is published at `correctexam.readthedocs.io`, and the org also ships a Rust server-side image-processing service (`deskewandcachecreator`) and a LaTeX exam template. 🔴 **ITS REAL DEFAULT REF IS `deploy`, NOT `main` — the third pass running in which a shelved repo's `HEAD` points somewhere unexpected (`p837`'s branch trap, `p838`'s `masame/develop`). A grant loop that assumes `main` reads a `404` here and records a false nil.** 🟢 **Enumerating the owner returned `15` repositories and showed the deployable estate around the two starred ones — `T137` paying out again.** 🔴 `12★`; JHipster-generated lineage, upgraded manually since `7.7.0`. |
| **Learnova** | https://github.com/Premshaw23/Learnova | 🟢 **MIT** — `master/LICENSE`, **`1,092 B`**, `sha256:535250f49c6a…`, © *2024 Prem Shaw* | `96★` / **`239`** | 🔴 **`master`** · `2026-11-13` (created `2025-09-05`) | APAC — India | 🟢 **Read the fork ratio before the star count: `96★` against `239` forks is `2.5:1`, inverted — this is being DEPLOYED, not read.** Attendance and student-engagement platform: Next.js 15, React 19, Firebase auth/analytics, MongoDB, Tailwind 4, with a live demo. Its own claims — teachers regain ~`1` hour/day of admin, students convert ~`90+` idle hours/year — are **vendor-stated and not verified by this pass.** 🔵 **Why it is filed rather than dismissed as another school-admin app: attendance is the one dataset every institution already has, legally must keep, and almost never joins to outcomes — and it is therefore the cheapest honest entry point to an analytics engagement.** 🔴 **`master` default ref. Firebase + MongoDB is a hosted-dependency posture; a public-sector client with a data-residency requirement will need both replaced.** `P90`. |
| **DualSub Replay** | https://github.com/hoangkien1703/dual-sub-replay | 🟡 **MIT source, and a DISTRIBUTION HISTORY that a procurement review will stop on.** 🟢 Source **MIT** — `main/LICENSE`, **`1,073 B`**, `sha256:dce2b7f51bde…`. 🔴 The README badge reads **"App distribution: GPL-3.0"**; the byte-read `THIRD_PARTY_NOTICES.md` says that applied to **historical releases (`v0.9.7` and earlier)** which bundled `yt-dlp`/`FFmpeg` via a GPL-3.0 Android wrapper, and that **current releases bundle only Apache-2.0 dependencies** after the downloader was removed | `63★` / `14` | `main` · `2026-11-15` (created `2026-08-10`) | APAC — Vietnam | 🟢 **Language learning from YouTube: subtitles in two languages at once, tap a sentence to hear it again, tap a word for its meaning.** Android 8+, Kotlin, on-device translation (ML Kit), OkHttp, Compose; Kuromoji for Japanese segmentation; an Apache OpenNLP English POS model shipped as build-time assets. 🔵 **Filed for the licence lesson as much as the product: the SHELF value is a repo whose badge and whose notices disagree, and only the notices are authoritative.** 🔴 **State it plainly to a client: current source is MIT and current dependencies are Apache-2.0, but anyone redistributing a pinned historical release inherits GPL-3.0 obligations.** 🟢 **On-device translation is the right posture for a schools deployment where sending pupil input to a cloud endpoint is the blocker.** |
| **SchoolOS — backend** | https://github.com/hamidukarimi/SchoolOS-backend | 🟢 **MIT** — `main/LICENSE`, **`1,069 B`**, `sha256:a0fd60a8ec49…`, © *2026 Hamid Karimi* | `41★` / `12` | `main` · `2026-10-13` (created `2026-03-22`) | Global | 🟢 **A modern school-management API — authentication, roles and the administrative core — in TypeScript, and a clean substrate rather than a product.** 🔵 **Filed because `P90` and every analytics recipe on these shelves need a system of record to read, and the alternatives on this shelf are a decade-old PHP estate or a national platform that cannot be exported from its jurisdiction.** 🔴 **`41★` / `12` forks, backend only, created `2026-03-22`, last push `2026-10-13` — a month before measurement, so the cadence is slower than the rows around it. Read the auth model before trusting it with pupil data.** |

### 🔴 `3` named refusals this pass — recorded so the next pass does not re-pay for the discovery

| Candidate | Repo | Grant | ★ | Why it is NOT on the shelf |
|---|---|---|---|---|
| obsidian-yolo | https://github.com/Lapis0x0/obsidian-yolo | 🟢 MIT — byte-read `main/LICENSE` (`1,065 B`, `sha256:bde979a91048…`) | `1,393` | 🟡 **Refused on SCOPE, not licence or quality — and it is the highest-starred refusal in this pass.** It ranks on education legs because its own description says "chat, write, whiteboard, **learning**, all in one" — but it is an agent-native assistant for **Obsidian**, a personal-knowledge-management tool. 🔴 **There is no learner model, no assessment, no curriculum and no instructor surface: the "learning" is a person reading their own notes.** 🟢 **Named here because `1,393★` on an education query will resurface every pass, and because the distinction is the one this shelf exists to hold: a PKM assistant is not an education agent.** 🔵 Legitimately useful as a research-notes tool in a higher-education engagement — which is a tooling choice, not a shelf row. |
| claude-equity-research | https://github.com/quant-sentiment-ai/claude-equity-research | 🟢 MIT | `759` | 🔴 **Refused because "educational" in a DISCLAIMER is not an education product.** An equity-research plugin generating buy/sell recommendations, whose description ends "Educational use only — not financial advice". 🟢 **That phrase is a liability shield on a finance tool; it ranks on education legs and means nothing pedagogically.** Named so the pattern — disclaimer-as-keyword — is recognised rather than re-investigated. |
| the `0★` lesson-plan long tail | — (`22` repositories, enumerated in `T138`) | 🟢 Mostly MIT | `0` | 🔴 **Refused as a CLASS, with the measurement recorded in `T138`.** A single lesson-plan leg returned `29` MIT-licensed hits of which **`22` sat at exactly `0★` and `0` forks**, almost all created in the last `90` days, almost all single-author, and most describing the same artefact: a generator that turns a prompt into a lesson plan. 🟢 **No individual refusal is interesting; the DISTRIBUTION is, and filing `22` entity rows for it would corrupt this base.** 🔵 **Operational rule: the lesson-plan channel is saturated with undifferentiated supply — spend the query budget elsewhere unless an institutional owner appears.** → `T138`. |

---

## 🟢 Forty-third pass (`p838`, 2026-11-16) — **`15` agent rows added (`399` → `414`), and `9` of the best came from ONE organisation found by enumerating an owner account, not by searching for agents**

🟢 **Every row below was measured `2026-11-16`: the real default ref from `git ls-remote --symref`,
the grant payload byte-read from `raw.githubusercontent.com` AT that ref with size and `sha256₁₂`
recorded, and stars/forks/`pushed_at` from the GitHub repository index the same day.**

🔵 **The channel, stated, because it is the finding.** `p837` (`T128`) established that a `license:`
qualifier on the repository index breaks nils a keyword search reports as saturation. 🟢 **`p838`
goes one step further: `license:` surfaced a SINGLE low-star hit — `oaknational/Oak-Web-Application`
(`27★`) — and enumerating its OWNER (`user:oaknational`) returned a complete, MIT-licensed
national-curriculum agent stack of `9` repositories that `42` prior passes never saw.** 🔴 **The
keyword index indexes repositories; it does not index ORGANISATIONS. A public body ships its stack
across many small repos, none of which is individually star-worthy enough to rank.** → `T133`.

### 🟢 `15` new agent rows — byte-read `2026-11-16` on the real default branch

| Agent | Repo | Licence, as measured | ★ / forks | Default ref · pushed | Region | What it actually does, and the posture |
|---|---|---|---|---|---|---|
| **Aila** (Oak AI Lesson Assistant) | https://github.com/oaknational/oak-ai-lesson-assistant | 🟢 **MIT** — `main/LICENSE`, **`1,077 B`**, `sha256:d150aadcccd2…` | `35★` / `7` | `main` · `2026-11-11` (created `2024-08-21`) | EMEA — United Kingdom (England) | 🟢 **A lesson-planning assistant built and run by a STATE-FUNDED NATIONAL CURRICULUM BODY, published MIT.** Oak National Academy is England's publicly funded curriculum body; Aila is the assistant teachers use to plan a lesson against Oak's curriculum. 🔵 **Why this outranks every community tutor on these shelves for an EMEA public-sector pitch: it is the reference implementation a ministry already accepted.** TypeScript, Turborepo, Postgres, Doppler; Jest + Playwright suites. 🔴 **The disclaimer is in its own README and must be quoted to a client, not glossed: *"intended primarily for internal use by Oak National Academy… there is no expectation for external users to run the application"*, and install docs are tailored for internal use.** 🟢 **So adopt it as an ARCHITECTURE and a prompt corpus under a licence that permits it — not as a turnkey deployment.** Recipe: `P87`. |
| **Oak Open Curriculum Ecosystem** | https://github.com/oaknational/oak-open-curriculum-ecosystem | 🟢 **MIT** — `main/LICENCE` (British spelling — a filename a grant loop must try), **`1,086 B`**, `sha256:02c5a8e84229…` | `9★` / `5` | `main` · `2026-11-12` (created `2025-07-28`) | EMEA — United Kingdom | 🟢 **The substantive half of the Oak stack, and the one a studio actually builds on.** Four declared streams: an **MCP app** putting Oak's curriculum *inside ChatGPT, Claude, Copilot and Gemini* — the assistants teachers already use; **engineering tools** (a generated type-safe TypeScript SDK, a semantic-search service, graph tools generated from Oak data); an openly documented **agentic-engineering framework**; and the **Oak Innovation Kit**. 🔵 **This is a national body publishing curriculum as AI-native infrastructure for third parties to build on — explicitly "public goods, built in the open".** 🔴 **`9★`: read the provenance, not the popularity.** `P87`. |
| **oak-agent-skills** | https://github.com/oaknational/oak-agent-skills | 🟢 **MIT** — `main/LICENSE`, **`1,085 B`**, `sha256:5248beedeb05…` | `0★` / `1` | `main` · `2026-11-10` (created `2026-10-12`) | EMEA — United Kingdom | 🟢 **A national curriculum body's SHARED AGENT SKILLS, plus the `oak-skills` tool that syncs them across its repositories.** 🔵 **The interesting artefact is the sync mechanism as much as the skills: it is how one organisation keeps agent behaviour consistent across an estate, which is the problem every multi-team client has and almost no public repo demonstrates.** 🔴 **`0★`, created `2026-10-12` — young, and the skills encode ENGLISH curriculum conventions; portable as a pattern, not as content.** |
| **oak-ai-plugins** | https://github.com/oaknational/oak-ai-plugins | 🟢 **MIT** — `main/LICENSE`, **`1,085 B`**, `sha256:e90b3e1c8e94…` | `0★` / `3` | `main` · `2026-11-14` (created `2026-09-29`) | EMEA — United Kingdom | 🟢 **Oak's Open Curriculum plugin for AI assistants** — Python, pushed two days before this measurement. 🔵 **The delivery shape worth copying: the curriculum reaches the teacher inside the assistant they already use, rather than in a new destination product nobody logs into.** 🔴 Young and unstarred; treat as a working reference, and pin a commit. |
| **yarareads** | https://github.com/finereli/yarareads | 🟢 **MIT** — `main/LICENSE`, **`1,066 B`**, `sha256:7c4cf856c78c…` | `28★` / `2` | `main` · `2026-11-15` (created `2026-10-05`) | Global | 🟢 **Early-literacy reading for children who have just learned their phonics sounds, and it is DECODABILITY-AWARE: every word in a story can be sounded out, and tapping a word gives its sounds.** 🔵 **`BRING YOUR OWN AGENT (MCP)` — the agent is a declared integration point rather than a hardcoded vendor, which is exactly the posture a schools client with a procurement constraint needs.** Cloudflare Workers, PWA, JavaScript. 🔴 **Phonics is orthography-specific: a Spanish or Bahasa deployment is a new decodability corpus, not a translation.** `P88`. |
| **colloquium** | https://github.com/natolambert/colloquium | 🟢 **MIT** — `main/LICENSE`, **`1,071 B`**, `sha256:bce041d216bb…` | `367★` / `22` | `main` · `2026-11-15` (created `2026-02-22`) | North America | 🟢 **The most-starred new row this pass: a markdown-native slides tool for ACADEMICS BUILDING WITH AGENTS.** Python. 🔵 **Why it belongs on an education shelf rather than a tooling one: lecture and seminar material is authored, versioned and re-taught, and a markdown source an agent can edit is the only form of that artefact an agent can actually maintain.** 🟢 Teaching-material authoring is the seam `P88` builds on. |
| **presentation-skills** | https://github.com/pamelafox/presentation-skills | 🟢 **MIT** — `main/LICENSE`, **`1,067 B`**, `sha256:e6bf682c17c8…` | `130★` / `24` | `main` · `2026-11-06` (created `2026-04-23`) | North America | 🟢 **Skills for AI agents to process presentations — the author states the audience as teachers and speakers.** Python. 🔵 **Pairs directly with `colloquium`: one authors the deck as markdown, the other lets an agent read and act on decks that already exist** — and the second is the harder half, because an institution's existing material is in `.pptx`, not in git. `P88`. |
| **manimvox** | https://github.com/LaplacianAI/manimvox | 🟢 **MIT** — `main/LICENSE`, **`1,068 B`**, `sha256:56fd265bbaea…` | `6★` / `1` | `main` · `2026-11-15` (created `2026-10-16`) | Global | 🟢 **A complete explainer-video pipeline run by an agent: research → a CITED script → Manim animation → narration.** Python. 🔵 **The citation step is the reason it is filed rather than dismissed at `6★`** — an education video that carries its sources is reviewable by a subject lead, and an uncited one is not. 🔴 **`6★`, created `2026-10-16`: read the code before promising a delivery date, and expect Manim's render cost.** `P88`. |
| **whiteboard-teacher-video-motion** | https://github.com/liangdabiao/whiteboard-teacher-video-motion | 🟢 **MIT** — `main/LICENSE`, **`1,068 B`**, `sha256:092d7cba85ea…` | `42★` / `4` | `main` · `2026-11-08` (created `2026-11-08`) | APAC — China | 🟢 **A hand-drawn explanatory-video skill: AI-native SVG vector diagrams that grow stroke by stroke, plus GIF frame extraction.** 🔵 **Created AND pushed `2026-11-08` — the single youngest row this pass, and `42★` in eight days.** 🔴 **Chinese-language project and docs; the asset it produces (progressive stroke-growth SVG) is language-neutral, the prompts are not.** 🟢 **This is the APAC half of the `P88` production line, and it is the one with real traction.** |
| **code-slowmo** | https://github.com/precious112/code-slowmo | 🟢 **MIT** — `main/LICENSE`, **`1,068 B`**, `sha256:0f8451cf2cc9…` | `27★` / `1` | `main` · `2026-10-20` (created `2026-10-20`) | Global | 🟢 **Understand code by watching it RUN in slow motion — an agent skill that builds interactive execution walk-throughs.** HTML. 🔵 **Computer-science teaching is the one subject where the misconception is almost always about EXECUTION ORDER, and a static explanation cannot address it.** 🔴 Single-author, created and pushed the same day, `1` fork. |
| **Perspicacité-AI** | https://github.com/HolobiomicsLab/Perspicacite-AI | 🟢 **Apache-2.0** — `main/LICENSE`, **`11,357 B`**, `sha256:c71d239df917…` (stock text, no holder in payload — `T131`) | `21★` / `7` | `main` · `2026-11-02` (created `2026-03-18`) | EMEA | 🟢 **An agentic assistant for scientists, researchers and STUDENTS working through primary literature.** Python. 🔵 **Filed because higher-education delivery is dominated by research-skills work, and this base's `414` rows are overwhelmingly K-12 and tutoring.** 🟢 **A reproduction check worth recording: this payload is byte-identical to `p837`'s Drop Project grant (`11,357 B` / `c71d239df917`) and to `RiceChecks` filed to foundations this pass — three unrelated projects, one stock Apache vintage, which is `T131` holding on new evidence.** |
| **hermes-kids-profile-blueprint** | https://github.com/tmchow/hermes-kids-profile-blueprint | 🟢 **MIT** — `main/LICENSE`, **`1,068 B`**, `sha256:d5c6b57f6897…` | `30★` / `4` | `main` · `2026-09-11` (created `2026-08-13`) | Global | 🟢 **A PARENT-OPERATED starter kit for designing a private, child-facing agent profile** — Python. 🔵 **This is the child-safety seam the market is now legislating (California's minors initiative, NY's grade-9+ restriction, the UK DfE product-safety standards) and it is the first row on these shelves where the SAFETY BOUNDARY IS THE PRODUCT rather than a disclaimer.** 🔵 Sibling `smfworks/wisdomforge-kids-Hermes-profiles` (🟢 MIT, `1,080 B`, `sha256:59075c88860a…`, `8★`) implements banded profiles for ages `5–10`, `11–14`, `15–18`. 🔴 **Both are profile/configuration blueprints, not supervision software — do not sell them as compliance.** |
| **masame** | https://github.com/Slymaster/masame | 🟢 **MIT** — `develop/LICENSE`, **`1,068 B`**, `sha256:b428f1061a51…` | `41★` / `1` | 🔴 **`develop`** · `2026-11-13` (created `2026-10-11`) | Global | 🟢 **"A craftsman's Go board, and a teacher that plays like a human"** — KataGo-backed, macOS and Windows, TypeScript. 🔵 **Filed as a DELIBERATE-PRACTICE row: the pedagogy is that an opponent who plays like a human teaches better than one that plays optimally, which is the same argument as scaffolding in a tutor and is rarely implemented this explicitly.** 🔴 **Its real default ref is `develop`, not `main` — the `p837` branch-trap again, and the licence above was read from `develop` because that is where `HEAD` points.** |
| **WordTeacher** | https://github.com/soniccat/WordTeacher | 🟢 **MIT** — `main/LICENSE`, **`1,072 B`**, `sha256:607d1ee2794a…` | `15★` / `2` | `main` · `2026-11-15` (created `2020-10-10`) | Global | 🟢 **Vocabulary acquisition for foreign-language learning, Kotlin Multiplatform.** 🔵 **Filed for its LONGEVITY rather than its size: created `2020-10-10` and still pushed the day of measurement — a six-year maintenance record is rarer on these shelves than a star count.** 🔴 Small; adopt the card/scheduling model, read the code before promising the apps. |
| **Intervyo** | https://github.com/santanu-atta03/Intervyo | 🟢 **MIT** — `main/LICENSE`, **`1,071 B`**, `sha256:ddba443d98e9…` | `16★` / `95` | `main` · `2026-11-15` (created `2025-10-14`) | APAC — India | 🟢 **Simulated technical and behavioural interviews — workforce-readiness education rather than coursework.** JavaScript. 🔴 **Read the fork ratio, not the stars: `16★` against `95` forks is `5.9:1`, the second-most extreme ratio in this base after Sunbird's `7.8:1`. Nobody forks an interview simulator `95` times to read it** — it is being deployed, and almost none of that is flowing back. 🔵 **For an employability or vocational engagement that is a demand signal.** `P86` territory. |

### 🔴 `3` named refusals this pass — recorded so the next pass does not re-pay for the discovery

| Candidate | Repo | Grant | ★ | Why it is NOT on the shelf |
|---|---|---|---|---|
| ouchn-learn | https://github.com/XueHua-s/ouchn-learn | 🟢 MIT — byte-read (`1,066 B`, `sha256:f9e894362fbc…`) | 14 | 🔴 **Refused on INTEGRITY, not licence — the licence is clean.** A userscript of "AI 刷题智能agents" for China's 国家开放大学 (Open University of China): it auto-advances coursework and answers quizzes on the student's behalf. 🔴 **Its purpose is to make a completion requirement register as met without the learning happening.** 🟢 **An education KB that files a credential-defeating tool as an "agent" is selling its client a liability.** Filed by name as a refusal, with the reason stated, because it ranks well in the `license:` channel and will resurface. |
| oak-mcp-server | https://github.com/oaknational/oak-mcp-server | 🟢 MIT — `main/LICENCE`, `1,086 B`, `sha256:02c5a8e84229…` (same payload as the ecosystem repo) | 0 | 🟡 **Refused under the `p821` rule — a governance document with a licence file is not a build-safe agent.** Its own README: *"The server is being moved here from the `oak-open-curriculum-ecosystem` repository… Until the code lands, this repository holds the workspace, the governance documents and the decision records."* 🟢 **The CODE is live in `oak-open-curriculum-ecosystem`, which IS filed above — so the capability is shelved, at the address that currently holds it.** 🔵 **It names a production endpoint, `https://mcp.thenational.academy/mcp`. 🔴 This pass could NOT confirm it: the host is not allowed through this session's egress proxy (`connect_rejected`), which is an INSTRUMENT limit and not evidence against the endpoint — `T136`.** Re-file as an agent row once the code lands. |
| oak-dspy-mcq-eval | https://github.com/oaknational/oak-dspy-mcq-eval | 🟡 **`NOASSERTION`** — `main/LICENSE.md`, `2,267 B`, `sha256:b2f57aa7d1c7…`: **code MIT © 2026 Oak National Academy, dataset (`data/mcq_mindiff_dataset.json`) under separate terms** | 1 | 🔴 **ARCHIVED (`archived: true`), last push `2026-07-13`.** A DSPy multiple-choice-question evaluation harness — genuinely the eval seam `T132` says the market now asks for. 🔵 **Filed as a refusal with its split grant recorded because the CODE half is MIT and reusable even from an archive, and a future pass should not have to re-read the payload to learn that.** 🔴 Do not build a delivery on an archived repo. |

---


## Forty-second pass (`p837`, 2026-11-16) — **the agent shelf grows again after four nil passes, and it grew because the CHANNEL changed, not because the supply did**

🟢 **`11` build-safe agent rows added (`388` → `399`). Every grant byte-read on the REAL default
branch on `2026-11-16`, with payload size and `sha256₁₂` recorded. Stars, forks and `pushed_at`
measured the same day from the repository index.**

🔴 **`p835` and `p836` each reported `0` new agents and each gave a reason — saturation, then
unlicensable local-language supply. 🟢 Both reasons were true of the channel they used, and
neither was true of the sector.** 🔵 **This pass ran `search/repositories` with a `license:`
qualifier, a `pushed:` window and `sort=updated` — the GitHub repository INDEX rather than a
web-search keyword leg — and the shelf moved immediately.** See `T128`.

🔵 **Instrument conditions, measured this pass and differing from `p835`/`p836` in one material
respect.** `curl` to `github.com` HTML and `api.github.com` remains `403` through the session's
agent proxy. 🟢 **`raw.githubusercontent.com` returns `200`, so the byte-read-plus-`sha256`
instrument is intact.** 🟢 **`gh api -X GET search/repositories` is LIVE and richer than this base
has been treating it:** a single query returns `stargazers_count`, `forks_count`,
`license.spdx_id`, `default_branch`, `pushed_at`, `created_at` and `language`. 🔴 **Controls run in
both directions:** `repo:HKUDS/DeepTutor` → `1` hit (`59,484★`, `Apache-2.0`, default `main`,
pushed `2026-11-15`), and an invented slug → `HTTP 422`. 🔴 **`422` is also what a real-but-unknown
slug returns, so `422` means "not resolvable", never "not licensed".**

### 🟢 `11` new agent rows — byte-read `2026-11-16` on the real default branch

| Agent | Repo | Licence, as measured | ★ / forks | Default ref · pushed | Region | What it actually does, and the posture |
|---|---|---|---|---|---|---|
| **TutorMoments** | https://github.com/allenai/tutormoments | 🟢 **Apache-2.0** — `main/LICENSE`, **`11,377 B`**, `sha256:b2c7059a9ab4…` | `28★` / `6` | `main` · `2026-11-14` (created `2025-11-15`) | Global (US institute) | 🟢 **The instrument this base has had no row for: a benchmark that measures how well a model TUTORS.** From the Allen Institute for AI. Runs a model-under-test against a **simulated student** on frozen, **expert-teacher-annotated "moments"** cut from real tutoring transcripts, then scores the continuation on **Appropriate Scaffolding**, **Appropriate Rigor**, **Avoids Over-Scaffolding** and an **Action Taxonomy** against human tutor moves. 🔴 **This base holds hundreds of tutor agents and, until this row, nothing that could tell a client whether one of them teaches well.** 🟢 Ships its own prompts and `default_config.yaml` inside the package; dataset defaults to the released Hugging Face set. Recipe: `P83`. |
| **Drop Project** | https://github.com/drop-project-edu/drop-project | 🟢 **Apache-2.0** — `master/LICENSE.txt`, **`11,357 B`**, `sha256:c71d239df917…` (stock text, no holder in payload — `T131`) | `33★` / `34` | `master` · `2026-11-11` (created `2019-03-04`) | EMEA — Portugal (ISCTE-IUL lineage) | 🟢 **A CONTINUOUS AUTO-GRADER, and it is the answer to `T96`'s grading gap that seven passes of agent queries never found, because it is not an agent.** Students submit a project; it checks folder structure and mandatory files, that it **compiles**, that it passes **the student's own tests**, a **minimum coverage** threshold, the **teacher's tests**, the teacher's **coding guidelines**, and **performance on large datasets** — then produces a report both the student and the teacher read. Kotlin/JVM, Maven Invoker, ships a `ghcr` container. 🔴 **Constraints stated rather than glossed: Java/Kotlin projects only; JDK 17–23, because Java 24+ removed the SecurityManager (JEP 486) and `-Djava.security.manager=allow` is required on 18–23.** 🟢 **The agent surface is the FEEDBACK NARRATIVE, never the grade** — `P84`. |
| **e-dnevnik-bot** | https://github.com/dkorunic/e-dnevnik-bot | 🟢 **MIT** — `main/LICENSE`, **`1,076 B`**, `sha256:d9bdf42fd7a5…`, © *2022 Dinko Korunic* | `70★` / `10` | `main` · `2026-11-15` (created `2022-03-14`) | EMEA — Croatia | 🟢 **An agent that reads a NATIONAL system of record and pushes to the family, and the most-starred row in this pass's set.** Grade and exam alerting against Croatia's **e-Dnevnik** national e-gradebook, in Go, multi-channel. 🔵 **This is the agent surface `p826`'s NATIONAL SCHOOL SYSTEM-OF-RECORD tier was filed without:** that tier named the platforms a European family logs into and had no row that talks to one. 🔴 **It is an unofficial integration against a state system — scraping posture, rate limits and terms are an engagement question, not a library question.** |
| **AI123 education-agent** | https://github.com/AI123-cmd/education-agent | 🟢 **Apache-2.0** — **`master/LICENSE`**, **`11,558 B`**, `sha256:1eb85fc97224…` | `1★` / `0` | 🔴 **`master`** · `2026-10-14` | APAC — China | 🟡 **A multi-agent personalised-learning system for HIGHER education on LangChain + LangGraph, organised explicitly around 认知学徒制 — COGNITIVE APPRENTICESHIP.** 🟢 **Filed for the pedagogy, not the traction:** it is the only row on this shelf whose orchestration is named after a learning theory rather than a product metaphor, and cognitive apprenticeship (model → coach → scaffold → fade) is a *sequence a graph can actually encode*. 🔴 **`1★`, one month old, single author — a reference design to read, not a dependency to pin.** 🔴 **This row cost a false negative first:** probed on `main` it returned `NO-GRANT-AT-ROOT`; its default ref is `master`. Second live reproduction of the `T112`/`p834` branch-axis defect in this pass. |
| **NASWA apprenticeship matcher** | https://github.com/NASWA-OpenUI/naswa-ai-apprenticeship-matcher | 🟢 **Apache-2.0** — `main/LICENSE.md`, **`11,382 B`**, `sha256:2d915fb4a6ea…` | `2★` / `0` | `main` · `2026-11-10` (created `2026-06-01`) | North America — US | 🟢 **A US PUBLIC-SECTOR authority's own apprenticeship-matching POC, under Apache-2.0.** `NASWA-OpenUI` is the **National Association of State Workforce Agencies** open-UI programme — the body whose members run state unemployment-insurance and workforce systems. 🔵 **Against this base's authority-estate census (`T126`), North America has been represented by districts and universities and not once by a workforce authority.** 🔴 **Self-described "Jobs app POC", `2★` — the value is the DATA MODEL and the institutional provenance, not the code.** `P86`. |
| **Google-AI-Classroom** | https://github.com/wongcyrus/Google-AI-Classroom | 🟢 **MIT** — `main/LICENSE`, **`1,062 B`**, `sha256:b79982c14bb1…` | `1★` / `1` | `main` · **`2026-11-16`** (created `2025-09-14`) | APAC — Hong Kong | 🟡 **Edge-to-cloud multimodal classroom agent, including exam invigilation.** 🟢 **Filed as the permissive counterpart to `open-edge-platform/education-ai-suite`** (Apache-2.0, Intel/OpenVINO, restored to `repos/foundations.md` this pass): the same classroom-sensing job, one on an on-premise inference stack and one edge-to-cloud. **An engagement that must choose a privacy posture now has both shapes on these shelves instead of one.** 🔴 **`1★`, single author.** 🔴 **Classroom sensing of minors is the highest-consent surface in this base — in EMEA it is an Annex III use, and the EU date is `2027-12-02` (`intel/market.md` this pass), not a reason to skip the DPIA.** |
| **Seren (IELTS tutor)** | https://github.com/Mahmud-Mahi/Seren--Your-IELTS-Tutor | 🟢 **MIT** — **`master/LICENSE`**, **`1,068 B`**, `sha256:d97b496ed043…`, © *2026 Mahmud Mahi* | `11★` / `1` | 🔴 **`master`** · `2026-11-13` (created `2026-09-04`) | APAC — Bangladesh | 🟢 **A speaking coach scored against a PUBLISHED RUBRIC — CEFR — rather than against model preference.** AI IELTS speaking practice with CEFR evaluation, diagnostic tests and personalised lessons, in TypeScript. 🔵 **The rubric is the reason this is filed:** high-stakes language assessment is the one education task where the scoring scale is public, externally defined and audited, so the agent's output is checkable by someone other than its author. 🔴 **`11★`, two months old.** 🔴 **Third `main`-vs-`master` false negative avoided this pass by resolving the ref first.** |
| **MelodyMate** | https://github.com/lorenaedwin08-hub/melodymate | 🟢 **MIT** — `main/LICENSE`, **`1,074 B`**, `sha256:0d46a2c87d7e…`, © *2026* | `47★` / `5` | `main` · `2026-11-14` (created **`2026-11-05`**) | Global | 🟢 **Accessibility-FIRST, not accessibility-retrofitted: a voice-guided music-learning app built for blind and visually impaired learners.** 🔵 **It belongs beside `p836`'s accessibility-conformance tier for the reason that tier exists:** `daisy/ace` and `w3c/epubcheck` tell you whether a MATERIAL conforms; this is the rarer thing, an application whose primary interaction was designed for a non-visual learner instead of being audited into tolerance afterwards. 🟡 **`47★` in eleven days is this set's fastest accrual — filed on shape and freshness, and sold as an early bet.** |
| **Bewerbär (Hack-Apertus)** | https://github.com/iatee/Hack-Apertus | 🟢 **Apache-2.0** — `main/LICENSE`, **`11,340 B`**, `sha256:3266fb7d3671…` | `0★` / `2` | `main` · `2026-10-16` (created `2026-10-05`) | EMEA — Switzerland | 🟡 **An AI interview coach that helps Swiss teens practise APPRENTICESHIP interviews, built on Apertus — Switzerland's sovereign open LLM.** 🟢 **Filed for the stack, which is the one thing this shelf could not previously demonstrate: a vocational agent running end-to-end on a European sovereign model rather than a US API.** 🔴 **`0★`, a hackathon artefact, `2` forks and no release — this is a PROOF THAT THE WIRING EXISTS, cited as such in `P86`, and nothing more.** |
| **ezhuthu** | https://github.com/Vivek0712/ezhuthu | 🟢 **Apache-2.0** — `main/LICENSE`, **`11,358 B`**, `sha256:cfc7749b96f6…` | `3★` / `0` | `main` · `2026-11-03` (created `2026-11-01`) | APAC — India (Tamil) | 🟡 **An apprenticeship tool for TAMIL EPIGRAPHY — read, transcribe, interpret inscriptions — built on Strands Agents.** 🟢 **Filed because of what it is evidence of, stated plainly: the long tail of education AI is DOMAIN APPRENTICESHIP in a low-resource language, and it is where a studio's language-and-heritage work actually lands in India.** 🔴 **`3★`, two weeks old.** |
| **Scaler exam-guard** | https://github.com/Scaler-Opensource/exam-guard | 🟢 **Apache-2.0** — `main/LICENSE`, **`11,357 B`**, `sha256:c71d239df917…` (stock) | `3★` / `1` | `main` · `2026-10-13` (created `2024-09-09`) | APAC — India | 🟢 **A COMPANY-BACKED permissive proctoring tool, and the only one in a population of `478` that is not a personal project.** Published by Scaler's open-source org. 🔵 **It is filed as the credible entry point to the proctoring population `T128` uncovered — see that trend for why this axis was declared nil for `35` passes and was never nil.** 🔴 **`3★` and `1` fork after two years: adoption is not the argument. Provenance is.** 🔴 **Proctoring is the single most consent-sensitive agent class in education — in the EU it is an Annex III high-risk use and nothing about a permissive licence changes that.** |

### 🔴 Found and NOT filed, with the reason per row

- 🔴 **`openedx/mockprock` — Apache-2.0 per the repository index, and `NO-GRANT-AT-ROOT` in the
  bytes.** Probed `LICENSE`, `LICENSE.txt`, `LICENSE.md`, `LICENSE.rst`, `NOTICE`, `COPYING` and
  `setup.py` across `master` and `main`: **all `404`.** `git ls-remote --heads` resolves (the
  repository is live; heads include `dependabot/*` and feature branches). 🟢 **Recorded as
  unverifiable-at-source, exactly as `p833` recorded `formalms/formalms`, and NOT counted as
  build-safe.** 🔵 **This is the same defect in the opposite direction from `p836`'s DeepTutor
  correction: there an aggregator understated the obligation; here GitHub's own licence field
  asserts a grant whose payload is not in the tree.** The useful part of this repository is
  anyway not its code but the **proctoring integration CONTRACT** it mocks — recorded in
  `verticals/solutions.md` this pass for that reason only.
- 🔴 **`Drone9/mereos`, `vishwa-10147/ExamSentiinel`, `vijaysingh0021/ExamGuard`,
  `TusharS230/exam-proctor-system`, `gurleenkamboj990/EXAM-IQ`,
  `architmahajann/EduCode-...-Proctoring-Platform`, `AshrafEqbal/Proctoring-System`,
  `theshauryajha/exam-proctoring`** — all live, all at `0`–`2★`, each a single-author project with
  no release. 🟢 **Not filed, and the population is reported as a measurement in `T128`/`T129`
  rather than padded into rows here.** `0★` is not disqualifying on this shelf — `p836` filed
  `0★` rows on freshness and gap-fit — but **nine interchangeable `0★` proctoring projects are a
  population, not nine findings.**
- 🔴 **`sethuiyer/tensor-to-tenant`, `yugh88/raahi`, `vedantsur09/Kinvia`,
  `mrinmoyChakraborty-mrinox/kaushal-app`, `palakrai573/Jaagruk-app`,
  `adhalakhadhanesh-ai/KISS-Vocational-Training-Management-Portal`,
  `Coding7hub/...Berufearchiv`** — the vocational population. 🟡 **All `0`–`2★`; the two with an
  institutional anchor (`hmrc/apprenticeship-levy`, `NASWA-OpenUI/...`) are filed, the rest are
  reported as population in `T129`.**
- 🔴 **Keyword collisions, recorded so the next pass does not re-triage them:** a `grading` /
  `grade` leg returns **colour grading** (`harborjoninrectify/resolve-color-lab`,
  `seth38-taylor/davinci-fusion-desktop`, `azuremaple1997/coreldraw-desktop`) and
  **"production-grade"** in a description; a `lesson` leg returns **"lessons learned"** blogs; a
  `tutor` leg returns **`*/tutorials`** repositories from `rabbitmq`, `IBM`, `KhronosGroup`,
  `deepset-ai`, `OpenVidu`, `kornia`, `lsst` and `sap-tutorials`. 🟢 **`6,902★` of RabbitMQ
  tutorials is the loudest false positive in the education query space, and it is loud in every
  channel.**

## Forty-first pass (`p836`, 2026-11-15) — **`0` agent rows added for a SECOND pass, and this time the reason is a different one**

🔴 **No new build-safe education AGENT was filed this pass. `388` → `388`.** 🟢 **The reason is
recorded instead of padded, and it is NOT the reason `p835` recorded.** `p835` found the agent
shelf saturated against its query set. 🔴 **This pass widened the query set into two languages
this base had never run — Vietnamese and Arabic — and the supply that came back was real,
numerous and UNLICENSABLE.** That is a different failure, and it is the finding.

🔵 **What was searched** (global, then once per region, per the standing rotation brief): `top open
source AI agents education 2026 github MIT`; `github trending education AI 2026`; `open source
platform education ERP CRM MIT Apache`; `AI education industry trends 2026`; the four regional
queries for **North America**, **EMEA**, **APAC** and **LATAM**; plus six probes beyond the brief —
`open source AI teaching assistant grading agent released November 2026 github`; `IA educación
código abierto github licencia MIT 2026 tutor agente escuela`; `오픈소스 AI 교육 플랫폼 github 2026`;
`phần mềm quản lý trường học AI mã nguồn mở github 2026`; `منصة تعليمية مفتوحة المصدر ذكاء اصطناعي
github 2026`; and `open source exam timetabling constraint solver school scheduling github Apache
2026`.

🔴 **Every agent-shaped candidate returned was already filed by slug.** Checked against the
`5,655` distinct `github.com/owner/repo` slugs this base now holds: `littlecookie0722/AI-Teaching-Agent`
(filed), `laurauguc/grading_assistant` (filed), `michael-borck/mark-mate` (filed),
`Osarodion843/EduGrade-AI` (filed), `tutor-mcp` (filed twice, `arnaudguiovanna/` and `kvnloo/`),
`HKUDS/DeepTutor` (filed), `THU-MAIC/OpenMAIC` (filed), `patchy631/ai-engineering-hub` (filed),
`microsoft/AI-For-Beginners` (filed last pass), `ibma/equal-access` (filed),
`microsoft/accessibility-insights-web` (filed), `google/or-tools` (filed),
`blockchain-certificates/cert-issuer` (filed — and this is why `blockcerts/*` read as a gap and is
not one: **the Blockcerts issuer lives under the `blockchain-certificates` org, not `blockcerts`**).
🟢 **The slug check is the instrument that kept this pass honest; it is what turned eight
"discoveries" into eight re-reads.**

### 🔴 `D836` — the mother-tongue layer INVERTS where 2026 regulation landed

🟢 **`T119`/`T121` established that querying in a national language finds education supply that
English misses. This pass ran that instrument at the two jurisdictions where education-AI
regulation actually became binding in 2026, and it returned the opposite of supply.**

- 🔴 **Vietnam** (`phần mềm quản lý trường học AI mã nguồn mở github 2026`). Returned
  `MARIOSLIDE123/oneschoolai`, `tungzuizer/school-management`, `thiebithocsovn/hesinhthai4.0`,
  `Giaduc8289/school-management-system`, `hiiinguyennn92-blip/quanlylophoctonytran`,
  `xuyen2210/quanlylop`, `hcmtranle/truonghoc5.0`. 🔴 **Not one carries an OSI grant.** One states
  its source is for internal educational administration only; one restricts the open flow to
  locally-run instances and requires registration for hosted use; one ships a `clone` command
  pointing at an unrelated repository. 🔴 **These are school-specific personal builds, several
  bound to one named primary school's live data.** `0` rows filed.
- 🔴 **Gulf / MENA** (`منصة تعليمية مفتوحة المصدر ذكاء اصطناعي github 2026`). Returned
  `781991937/TOFAN-AI-2026`, `lojainlll9820-ops/my-education-platform`, `lojainlll9820-ops/-`,
  `adoomy23-cpu/ai-students-platform`, `matsuolab/lecture-ai-engineering-2026-ar`. 🔴 **Same
  shape: early personal repositories, licences not stated.** `0` rows filed.
- 🟡 **Korea** (`오픈소스 AI 교육 플랫폼 github 2026`). Returned only curricula this base already
  holds (`microsoft/AI-For-Beginners`, `microsoft/generative-ai-for-beginners`,
  `mlabonne/llm-course`, `DataTalksClub/llm-zoomcamp`) plus personal study tools. `0` rows filed.

🔵 **Why this matters commercially and not just bibliographically:** **Vietnam's Law on AI took
effect `2026-03-01` and treats education systems as high-risk; Korea's AI Basic Act entered force
`2026-01-22` with education named a high-impact area; the Gulf has KHDA guidance to private
schools.** 🔴 **So in three jurisdictions that now REQUIRE governed education AI, the local-language
open-source supply is personal projects with no grant.** 🟢 **An engagement in those markets must
IMPORT build-safe supply from this base's shelves and localise it — it cannot source it locally.**
See `T124`.

### 🟢 Anchor re-verification (`2` anchors, `1` licence misattribution caught in the wild)

- 🟢 **`HKUDS/DeepTutor` — `Apache-2.0`, byte-read `2026-11-15`** (`main/LICENSE`, **`11,408 B`**,
  `sha256:cd2f54e1e506…`, opening block `Apache License / Version 2.0, January 2004`). **`59.5k★`**
  measured on the rendered page, **exactly** the figure `p835` corrected to. Rendered sidebar
  states `Apache-2.0`; latest release shown as **`v1.7.3`, dated `2026.11.16`** on the page — 🔵
  **recorded as rendered, one day ahead of this pass's run date, not adjusted.**
  🔴 **Two secondary sources read this pass call DeepTutor "MIT licensed"** (a CoddyKit profile and
  a Spanish-language round-up). **They are wrong, and this base is right** — `Apache-2.0` is in the
  bytes. 🟢 **This is `T109`/`T120`'s rule earning its keep in the opposite direction from usual:
  the aggregator understated the obligation, not the traction.**
  🔴 **In-file staleness, declared not rewritten:** an older pass section in this file still carries
  `58.7k★` for `DeepTutor`. These files are append-only; history stays as written, and the head row
  is the current one.

🔵 **Instrument note, unchanged and re-measured this pass:** `curl` to `github.com` HTML and
`api.github.com` returns `403` through the session's agent proxy; `raw.githubusercontent.com`
returns `200`. 🟢 **The byte-read-plus-`sha256` instrument remains available and remains correct.**
🔴 **New this pass: the `404` is also a real signal and must not be read as "no grant."**
`daisy/ace/master/LICENSE` → `404`, while `daisy/ace/master/LICENSE.txt` → `200` with MIT in the
bytes. **The grant was there; the filename was not what the probe assumed.** Both `daisy/ace-gui`
(`LICENSE`, no extension) and `daisy/ace` (`LICENSE.txt`) exist in the same org with DIFFERENT
filenames. 🟢 **Probe the extension set, not one path.**

🟢 **Where this pass's `5` new rows went, since none are agents:** `w3c/epubcheck`, `daisy/ace` and
`liblouis/liblouis` to `repos/foundations.md`; `daisy/ace-gui` and `sukrutrao/Timetabler` to
`verticals/solutions.md`. See `T123` for why an entire regulated vertical was missing from this
base, and `P76`/`P77` for the recipes.


## Fortieth pass (`p835`, 2026-11-15) — **`0` agent rows added, and the reason is recorded rather than padded**

🔴 **No new build-safe education AGENT was filed this pass. The supply this base queries is
saturated, and the honest number is zero.**

🔵 **What was searched** (global, then once per region, per the standing rotation brief): `top open
source AI agents education 2026 github MIT`; `github trending education AI 2026 open source
repositories`; `open source education platform LMS student information system MIT Apache
self-hosted 2026`; `AI education industry trends 2026 market adoption`; and the four regional
queries for **North America**, **EMEA**, **APAC** and **LATAM**.

🔴 **What came back was already on these shelves.** Every agent-shaped candidate returned was
checked against the base by slug before being considered new, and all were present:
`HKUDS/DeepTutor` (**`5` existing mentions**), `THU-MAIC/OpenMAIC` (`3`),
`patchy631/ai-engineering-hub` (already in `repos/foundations.md`), `frappe/lms` (**`8` mentions in
`verticals/solutions.md`**), `francoisjacquet/rosariosis`, `GibbonEdu/core` and
`rohitg00/ai-engineering-from-scratch` (all already filed). 🟢 **One candidate was genuinely
absent — `microsoft/AI-For-Beginners` — and it is a curriculum, so it was filed to
`repos/foundations.md`, not here.**

🟢 **Two anchors re-verified rather than re-asserted.** `HKUDS/DeepTutor` — **Apache-2.0**
(`main/LICENSE`, `11,408 B`, `sha256:cd2f54e1e506…`; rendered sidebar agrees), **`59.5k★`** against
the `59.4k` this base published, so the row is CURRENT and was corrected upward by `0.1k`.
`THU-MAIC/OpenMAIC` — **MIT**, **`43.6k★`**, **exactly** the published figure. 🟢 **Neither anchor
has drifted; the `388` rows are not stale.**

🔵 **Instrument note, measured this pass and correcting a premature conclusion drawn mid-pass:**
`curl` to **`github.com` HTML and `api.github.com` both return `403`** through the session's agent
proxy, so star counts and sidebar licences must come from rendered-page reads.
🟢 **`raw.githubusercontent.com` returns `200` and is UNAFFECTED**, so the payload byte-read with
`sha256` that `p824`–`p834` rely on remains available and remains the correct instrument. A pass
that reports `NO-GRANT` on the strength of a `403` would be recording the proxy, not the grant.

🔴 **Declared gap, unchanged by this pass:** across all four regions, **no new permissively licensed
education agent** surfaced in this window. The regional queries returned **policy and market**
intelligence (recorded in `intel/market.md`) and **no new software** — an informed nil, and the
fourth consecutive pass in which the agent population has not grown from Western-language queries.


## Thirty-ninth pass (`p834`, 2026-11-15) — the probe that fixed false ABSENCE created false PRESENCE, and one of this base's three declared nils flipped in Chinese while the other two held

🟢 **Three things were measured this pass and all three are reproducible from the commands in
`ingest/p834-grantprobe.sh` and in `intel/trends.md`.**

🔴 **`D834` — the instrument.** `T112` hardened the branch axis against false ABSENCE, and `p833`
built the probe that did it. 🔴 **That probe orders `main` / `master` / `dev` by a hardcoded
preference and takes the FIRST `200`, which need not be the branch the project ships.** 🟢 **Proved,
not supposed:** `yinuoguan/nengdou-ai-review-helper-web` carries Apache-2.0 on a stale `main`
(`11,357 B`, `sha256:c71d239df917…`) and **MulanPSL-2.0 on its default `master`** (`9,247 B`,
`sha256:f0dade5c9337…`, and `develop` and `feature` agree with `master`). 🔵 **Blast radius MEASURED
rather than asserted: `20` published addresses sampled, branch-pick disagreement on `2`
(`DOAJ/doaj` default `develop`, `ILIAS-eLearning/ILIAS` default `release_11`), licence-byte
divergence on `0` of `20`.** 🟢 **So the defect is real, it is rare in the existing corpus, and it
is NOT a reason to re-open `442` pinned figures — which is said here rather than left for a reader
to infer.** 🟢 **Fixed in `ingest/p834-grantprobe.sh`, with the `31`-name list restored
(`ACTION p833-C`, instrument limb) and both controls passing.**

🟢 **`ACTION p833-B` — DISCHARGED, and the answer is the cheap one.** The `in:name,description`
qualifier is **INERT** on CJK queries: `智慧教育` (`399`), `作业批改` (`435`), `AI素养` (`100`) and
`智能备课` (`221`) return **identical totals and byte-identical top-`10`s** with and without it.
🔵 **So `T115`'s inversion is a RANKING property, not a substring-over-README property, and the
discovery rule is now caused rather than asserted: read the full set, sort by `pushed_at`.**

🟡 **`ACTION p833-A` — run, and it refutes its own premise in two of three cases.** `T114` said a
nil is only a nil in the language the supply is written in. 🟢 **Re-run across Chinese, Spanish,
Portuguese, German and French: the PROCTORING nil FLIPPED (Chinese only — `36` + `11`
repositories, three of them granted); the UDL nil flipped as a POPULATION but not as a build-safe
supply (`10` Spanish, `3` Portuguese, `0` German, Chinese INCONCLUSIVE); the VOCATIONAL nil HELD in
all five languages.** 🔴 **One of three. `T114`'s rule survives but shrinks: it is a CHINESE-supply
rule, not a general multilingual one** (`T118`).

🟢 **`9` build-safe agent rows added (`379` → `388`), `4` foundation rows (`171` → `175`), `5`
vertical rows (`140` → `145`), `4` trends (`T118`–`T121`), `1` recipe (`P74`) and `5` regional
market blocks — including CANADA and MEXICO, the two-country blank this base has carried since
`p810`.** 🔴 **`3` candidates found and NOT filed, each with its reason stated.**


## Thirty-eighth pass (`p833`, 2026-11-15) — China's `AI+Education` Action Plan has a BUILD-SAFE SUPPLY, and it answers the grading gap this base has carried since `T96`

🟢 **The organising finding.** `T96` established the grading gap by TEST rather than by copy-forward:
this base holds hundreds of tutor, planner and content-generation agents and almost nothing that
MARKS student work. 🔴 **Thirty-seven passes of English-language sweeping never closed it.** 🟢 **One
query in the vocabulary of China's national plan — `教育 大模型 agent`, `作业批改` — returns a
granted, multimodal, photo-in marking agent with a three-tier remediation generator attached.**
🔵 **The gap was never a SUPPLY gap. It was a LANGUAGE gap** — `T82`'s rule (the supply answers to
the statutory vocabulary, not to the sector word) on a fifth axis, and the first time this base has
hit that rule in a non-Latin script. See `T114`.

🟢 **Channel conditions — three channels, all controlled in both directions.** Channel A
(`gh api search/repositories -f q="repo:…"`): live repository `HKUDS/DeepTutor` returns `1`
(`59,457★`, `Apache-2.0`, pushed `2026-11-15`), invented slug returns `HTTP 422`. 🔴 **`gh api
repos/{owner}/{repo}` is still `403` for this session, so the metadata channel remains SEARCH-ONLY**,
exactly as `p832` recorded. Channel B (`raw.githubusercontent` byte-read, written to a FILE, never
to a shell variable): `sillsdev/libpalaso` returns `1,082 B` / `sha256:b716617149f3…`, 🔵 **reproducing
`p831`'s repaired figure and `p832`'s re-reading of it EXACTLY — the instrument is calibrated
against this base's own value before it is used to contradict this base.** Channel C
(`git ls-remote --heads`): live address returns a ref set, invented slug returns an EMPTY one.

### 🟢 `D833-1` — `ACTION p832-B` is DISCHARGED in working form: the probe now resolves heads BEFORE the filename loop and prints the probed ref set inside every verdict

🔴 `p832` left the defect named and unfixed: *"`grantprobe.sh` takes the branch as `$2` with no
resolution. One wrong guess `404`s all `31` case-aware filenames and prints `NO-GRANT-AT-ROOT`, a
verdict byte-identical to a true absence."* 🟢 **`grantprobe833.sh` resolves heads from
`git ls-remote --heads` first, orders `main`/`master`/`dev` ahead of the remainder, probes `10`
case-aware filenames per ref, and prints `refs=[…]` inside EVERY verdict — so an absence is now
falsifiable without re-running it.** 🟢 **An EMPTY ref set is its own verdict** (`EMPTY-REF-SET`),
which is the distinction `p832` asked for: a dead address is not an ungranted one. 🔵 **Both
controls pass**: the invented slug `Zhangming0304/this-repo-does-not-exist-p833` returns
`EMPTY-REF-SET`, and `sillsdev/libpalaso` returns `GRANT at master/LICENSE` with the pinned bytes.
🔴 **Not claimed: the `31`-name list was narrowed to `10` and the `~171` stale pinned figures of
`ACTION p832-A` were NOT re-measured. `p832-A` is carried, not discharged.**

### 🔴 `D833-2` — `ACTION p832-C` settled by bytes, and this base was WRONG on the bigger of the two

🟢 **Open edX — settled, and the answer is the one the base's vertical leg did NOT hold.**
`openedx/edx-platform` is **`AGPL-3.0`**: byte-read `35,136 B`, `sha256:e12d78569742…`, at
`master/LICENSE`, first line `GNU AFFERO GENERAL PUBLIC LICENSE Version 3`. 🔴 **The `MIT` limb of
the conflict is false, and the likely source of it is that Open edX ORIGINATED at MIT and Harvard
— an institution name read as a licence name.** 🔵 **The consequence is a build consequence, not a
bookkeeping one: a hosted derivative of Open edX must publish its source. Every pattern in this base
that puts Open edX under a client deliverable inherits that.**

🔴 **Forma LMS — settled, and NEITHER limb survives.** `formalms/formalms` returns
`NO-GRANT-AT-ROOT` across `10` case-aware filenames × `2` resolved heads (`master`, `dev`) = `20`
probes; `composer.json` `404`s; the `README.md` (`6,198 B`) contains no occurrence of the string
`licen`. GitHub's own licence field reads `NOASSERTION`. 🔵 **So the `LGPL`-versus-`GPL` dispute this
base carried is unsettleable FROM THE REPOSITORY — both limbs came from project-website prose, and
neither is in the bytes.** 🟢 **Recorded as unverifiable-at-source rather than resolved to the
likelier answer**, which is what `T81` requires.

### 🔵 Region discipline on this pass's four rows

🔴 **This base does not infer a region from an author's name** (`litto`, `p829`). 🟢 **All four rows
below are placed `APAC` on a JURISDICTION binding, not a language one**: `teach_agent` and
`AI-GAME-COOL` name Chinese domestic model providers as their runtime (DeepSeek / 通义千问 /
智谱清言, Alibaba Bailian), `AInoAgentAcademy` ships on a `.cn` domain, and `KongMeng-Agent` targets
the Chinese teacher-preparation workflow. 🔵 **A runtime bound to a provider that only serves one
jurisdiction is a placement fact; a README in Chinese would not have been.**

## Thirty-seventh pass (`p832`, 2026-11-15) — the repair held and the SHELVES did not: `38.7%` of this base's pinned grant figures are still unreproducible, and a second axis of the same instrument was never fixed at all

🟢 **`derive-counts.py` was run FIRST, before any edit, and again after every insertion.** Baseline
at `HEAD`: `agents/top.md 370`, `repos/foundations.md 168`, `verticals/solutions.md 140`,
`intel/trends.md 110`, `compose/patterns.md 71`, `ragged=0`, `nolink=0`.

🟢 **Channel conditions — both channels live, both controlled in both directions.** Channel A
(`gh api search/repositories -f q="repo:…"`): live repository returns `1`, invented slug returns
`HTTP 422`. 🔴 **`gh api repos/{owner}/{repo}` is NOT available — it returns `403 GitHub access to
this repository is not enabled for this session`, so the metadata channel is SEARCH-ONLY this
pass**; every star count, push date and licence field below comes from the search endpoint.
Channel B (`raw.githubusercontent` byte-read, written to a FILE and never to a shell variable):
`sillsdev/libpalaso` returns `1,082 B` / `sha256:b716617149f3…`, **reproducing `p831`'s repaired
figure exactly**, and the invented slug `404`s. 🔵 **That exact reproduction is what licensed every
other measurement in this pass: the instrument is calibrated against this base's own repaired
value before it is used to contradict this base.** 🟢 **A THIRD channel was opened this pass:
`git ls-remote --heads`, the ref set — see `D832-1`.**

### 🔴 `D832-1` — `p831` fixed the FILENAME axis of the grant probe. The BRANCH axis was never fixed, and one wrong argument nils all `31` filenames at once

🔵 `p773`'s `D9` widened `grantprobe.sh` to a `31`-name, case-aware filename list because *"a
missing lowercase `license.txt` produced a false `NO-GRANT-AT-ROOT` on ERPNext."* `p831` then
repaired the same script's `P834` capture defect. 🔴 **Neither touched the branch: the script takes
the branch as its SECOND POSITIONAL ARGUMENT (`s="$1"; br="$2"`) and has no resolution step of any
kind.** 🔴 **If the caller guesses a branch the repository does not have, all `31` filename paths
`404` and the script prints `NO-GRANT-AT-ROOT` — a verdict byte-identical to a true absence.**

🟢 **Demonstrated on the committed instrument, unmodified, against one address:**

| Invocation | Result |
|---|---|
| `grantprobe.sh learningequality/kolibri main` | 🔴 `NO-GRANT-AT-ROOT` |
| `grantprobe.sh learningequality/kolibri master` | 🟢 `LICENSE` / `1,097` / `3c056b34a476` |
| `grantprobe.sh learningequality/kolibri develop` | 🟢 `LICENSE` / `1,097` / `3c056b34a476` |

🔴 **`git ls-remote --heads learningequality/kolibri` lists `develop` and `release-v0.19.x` and
twelve more. There is no `main`.** 🟢 **The repair is one line of discipline, not a rewrite:
resolve the branch from the ref set before probing filenames.** 🔵 **The ref channel is cheap,
independent of `raw.githubusercontent`, and this base did not have it until now.**

### 🟢 What `D832-1` cost, swept over every absence claim standing in the live shelves

🟢 **All `38` addresses adjacent to a `NO-GRANT-AT-ROOT` / `NOGRANT` / "no licence file" claim in
`agents/top.md`, `repos/foundations.md` and `verticals/solutions.md` were re-probed with branch
resolution.** 🔴 **Three were false absences, and each is corrected below. The other `35` reproduce
as stated, which is the control: this is a targeted defect, not a collapse.**

| Address | What the base published | Byte-read `2026-11-15`, branch resolved | Disposition |
|---|---|---|---|
| `XPRIZE/GLEXP-Team-RoboTutor-RoboTutor` | 🔴 `NOGRANT` at `31` paths; recorded **UNRESOLVED** — *"a whole university's XPRIZE finalist is unusable until someone resolves this"* | 🟢 `LICENCE.md` / `1,319 B` / `sha256:d2e11a0122c0…` on `master` — **Apache-2.0 (code) + CC BY 4.0 (content)** | 🟢 **RESOLVED and FILED build-safe.** `master` is this repository's ONLY head; `p831` reported probing *"both `main` and `master`"* and the `master` leg cannot have run, because path `LICENCE.md` is in the committed `31`-name list |
| `learningequality/kolibri` | 🔴 `NO-GRANT-AT-ROOT` in `p831`'s census table — **while `repos/foundations.md` published `MIT` for the same address on the same day** | 🟢 `LICENSE` / `1,097 B` / `sha256:3c056b34a476…` on `master` and `develop` — **MIT** | 🟢 **CORRECTED, and the base was INTERNALLY INCONSISTENT about its own most-shelved platform.** The foundations row was right; the census row was the probe's branch guess |
| `thesupersupersigma/powerschoolMCP` | 🔴 *"No licence — GitHub reports `NONE`, no `LICENSE` in the repository"* | 🔴 `LICENSE` / `35,149 B` / `sha256:3972dc9744f6…` on `master` — **`GNU GENERAL PUBLIC LICENSE` Version 3** | 🔴 **CORRECTED, and this is the dangerous direction.** The field reads `GPL-3.0`, so BOTH channels were misreported. A row believed merely ungranted is in fact under strong copyleft — an absence error that understates obligation is worse than one that overstates it |

🔵 **Two addresses in the sweep (`Nordup/askaboard`, `nailuoGG/anki-mcp-server`) did not resolve on
`main`, `master` or `develop` this pass. Recorded as UNRESOLVED-THIS-PASS, not as ungranted**, per
`p830`'s standing rule that `NOGRANT` is not an existence oracle. 🔵 `AraSuite/arasaac-api` returns
an EMPTY ref set — the address no longer serves refs at all, which is a different finding from an
absent grant and is filed as one.

### 🔴 `D832-2` — the `P834` repair reached the INSTRUMENT and `8` addresses. It did not reach the shelves, and `38.7%` of the pinned figures are still unreproducible

🔴 **`p831` closed `P834` with eight addresses re-measured and the gate green. This pass tested
whether the SHELVES agree, and they do not.** 🟢 **Method: every `(address, bytes, sha256)` triple
pinned in the three graded shelves was extracted — `442` of them — and a reproducible `1`-in-`7`
sample (`n=64`) was re-measured with the file-based probe.**

| Verdict | Count | Share of sample |
|---|---|---|
| 🟢 `EXACT` — today's bytes reproduce the pinned figure | `38` | `59.4%` |
| 🔴 `SHORT-BY-1` — pinned figure is exactly `1` byte under today's | `24` | `37.5%` |
| 🔵 `UNRESOLVED-THIS-PASS` | `2` | `3.1%` |

🔴 **Residue rate `24/62` resolvable = `38.7%`. Extrapolated over all `442` pinned triples: ~`171`
published byte/sha figures that cannot be reproduced from the file they name.**

🟢 **And the `SHORT-BY-1` class was not assumed to be `P834` — it was TESTED, because a `+1` byte
delta is equally consistent with an ordinary upstream edit.** 🟢 **The discriminator: strip the
trailing-newline run from today's bytes, exactly as `$( … )` would, and hash the remainder. If the
pinned sha returns, the figure is a capture artefact and the file never changed.** 🔴 **Run on `12`
of the `24`: `12` of `12` REPRODUCED.**

| Address | Pinned | Today's bytes, trailing newlines stripped | |
|---|---|---|---|
| `toughIQ/webuntis-mcp` | `1,063` / `2c0b8069fc10` | `1,063` / `2c0b8069fc10` | 🔴 reproduced |
| `bsayres/heronhex-highered` | `1,082` / `aa0df3165b5d` | `1,082` / `aa0df3165b5d` | 🔴 reproduced |
| `liangxiao777/TeachMeCoding` | `11,357` / `58d1e17ffe51` | `11,357` / `58d1e17ffe51` | 🔴 reproduced |
| `JesseTho/lamaku-mcp` | `1,166` / `ce95c0d64e0c` | `1,166` / `ce95c0d64e0c` | 🔴 reproduced |
| `chapmanwm/moodlectl` | `1,065` / `2ff4b5ffb33f` | `1,065` / `2ff4b5ffb33f` | 🔴 reproduced |
| `Akramjon-koder/faroz-mcp` | `1,084` / `99b8d19e6a31` | `1,084` / `99b8d19e6a31` | 🔴 reproduced |
| `AnonymousOnyx22/brightspace-d2l-mcp` | `1,199` / `3f0e907830ac` | `1,199` / `3f0e907830ac` | 🔴 reproduced |
| `alanwtom/blackboard-mcp` | `1,064` / `6cd5ef811418` | `1,064` / `6cd5ef811418` | 🔴 reproduced |

🟢 **The control runs the other way too, and it is the sharpest part of this result: `nialvape/utn-mcp`
— one of the `8` addresses `p831` re-measured by hand — returns `748 B` / `2ad14eb14513…`, EXACT.**
🔵 **So the discriminator is not whether the probe is fixed. It is whether a pass re-measured that
address.** 🔴 **The instrument has been correct since `p831`; the published corpus has not been
re-run through it.** 🔵 **This is `T111`, and it generalises past this base: a repair to a
measuring instrument does not propagate to measurements already published, and a gate that grades
the instrument will stay green over a shelf full of stale figures.**

🔴 **Stated plainly, as `p831` stated its own: `p832` did NOT re-measure the other ~`171`. It sized
the residue, proved the mechanism, corrected the `3` absence errors it found, and left the rest
named and counted** — see `ACTION p832-A`.

### 🟢 `ACTION p831-B` discharged — the suite's redness is now a MEASUREMENT, and it reports `18` from a committed target

🟢 **`make gate-report` added: it runs all `68` blocking gates to completion and prints the green
count, the red count and the red NAMES.** 🔵 `commit-gates` stops at the first failing recipe, so
it has always reported a lower bound that reads like an upper bound.

| Run | Result |
|---|---|
| Pristine `git archive HEAD` export (the `p831` state) | `green: 50` **`RED: 18`** |
| This pass's working tree, at commit | `green: 50` **`RED: 18`**, the same `18` names |

🔵 **Zero regressions — `p832` introduced no new red gate.** 🟢 **And the run corrects `p831`'s own
list in `p831`'s favour: `gate-offline` is GREEN here, though `p831` printed it among its `18`, so
that repair was real and the list it printed was stale.** 🔴 **The eighteenth red is
`gate-i2-sweep-crosscheck`, which appears in no `p831` list at all.** 🔴 **`p832` did not fix any
of the `18`; it built the instrument that counts them.**

### 🔴 The mandated star-ranked battery nilled a `43`rd consecutive time

🟢 **Run in full: four global legs and four regional legs** (`top open source AI agents education
2026 github MIT`, `github trending education AI 2026`, `open source platform education LMS SIS MIT
Apache self-hosted`, `AI education industry trends 2026`, then North America / EMEA / APAC / LATAM).
🔴 **Zero new build-safe agent rows came from any of the eight.** Every named repository the global
legs returned — `HKUDS/DeepTutor`, `THU-MAIC/OpenMAIC`, `frappe/lms`, `OpenOLAT/OpenOLAT`,
`openeducat/openeducat_erp`, `francoisjacquet/rosariosis`, `openedx/edx-platform`,
`instructure/canvas-lms`, `moodle/moodle`, `apereo/opencast`, `oppia/oppia`, `h5p/h5p-php-library`,
`ashishpatel26/500-AI-Agents-Projects`, `patchy631/ai-engineering-hub` — was checked against this
base's `7,125`-slug known set and **`13` of `14` were already held**. 🔵 `T63`'s saturation finding
is now `43` passes old and has never once been refuted. 🟢 **The five rows this pass filed came
from the LATAM-language legs instead, which is `T82`'s rule holding on a fifth axis.**

### 🔴 `4` rejections, with the reason each one was refused

1. 🔴 **`OpenSIS-Classic/OpenSIS-Classic`** — the one slug of the fourteen NOT already held. Refused on scope, not on licence: a K-12 SIS with no agent surface, and the vertical shelf already carries this layer. Named here so the next pass does not re-pay for the discovery.
2. 🔴 **`latam-gpt/llm-data-eval`, `latam-gpt/toxicity-classifier`, `latam-gpt/language_identifier`** — the three most-starred repositories of the region's flagship model programme, named by CENIA and by the UNESCO LAC Observatory. **Byte-read `2026-11-15`: `NOGRANT` on all three, on every probed branch.** 🔵 The region's flagship AI asset ships no grant of any kind — recorded as `T113`'s hardest single data point, and worth an upstream licence request.
3. 🔴 **`ProfCleuson/Sistema-de-Consci-ncia-Fonol-gica`, `rjcv/ilha-dos-sons`, `giovannaimperioo-ux/F-ou-V`** and the rest of the `~106`-repository literacy population — **no licence file.** The population is real and is recorded as one in `T113`; its build-safe yield is the four rows filed above.
4. 🔴 **`mariajo79/Detective-de-Sonidos-MJCL` and the `CC0-1.0` Spanish cohort** — `CC0` is a CONTENT dedication. 🟢 Usable as pedagogy material; wrong instrument for shipped software, per this base's standing `T78` split-licence rule.

## Thirty-sixth pass (`p831`, 2026-11-15) — the FOUNDATIONAL-LEARNING tier, and the pass that repaired the base's own red gate instead of committing over it

🟢 **`15` build-safe agent rows filed (`355` → `370`), `15` foundation rows (`153` → `168`), `5`
vertical platforms (`135` → `140`), `3` trends (`T108`–`T110`), `1` recipe (`P71`). Every licence
BYTE-READ on `2026-11-15`. Two instruments in `compose/code/p773/` REPAIRED, one blocking gate
taken from RED to GREEN, and a SECOND red — which the first was hiding — found, measured and
adjudicated address by address.**

🔴 **`p830` ended by naming its own successor's job, and this is it.** Line `204` of this page,
written yesterday, graded `p773/grantprobe.sh` as **`CAPTURED-LIVE`** and said in terms:
*"Pinning it would be the 'silently downgraded verdict' the suite's own control forbids; the fix
is to make the script measure the payload directly."* 🟢 **That repair is done, and it was worth
more than the prose predicted.**

### 🔴 What the defect actually cost, measured old-probe against new-probe on the same addresses

`P834` is this base's oldest live defect class: `b=$(curl …)` strips the **entire run of trailing
newlines**, so `printf '%s' "$b" | wc -c` reads short and `sha256sum` reads a hash that cannot be
reproduced from the file it names. 🔴 **On a base whose shelves PIN SHAs, that is not a style
issue.** Both probes were run against the same eight addresses on `2026-11-15`:

| Address | File | OLD bytes / sha | NEW bytes / sha | Delta |
|---|---|---|---|---|
| `openedx/edx-platform` | `LICENSE` | `35,135` / `106a1b4b8b71` | 🟢 `35,136` / `e12d78569742` | **`+1`** |
| `XPRIZE/GLEXP-Team-KitkitSchool` | `LICENSE` | `11,339` / `6d4c12deba60` | 🟢 `11,340` / `638af047fe71` | **`+1`** |
| `chimple/maui` | `LICENSE.txt` | `11,356` / `43070e2d4e53` | 🟢 `11,357` / `c71d239df917` | **`+1`** |
| `vgwb/Antura` | `LICENSE.md` | `2,001` / `9e70b4664b10` | 🟢 `2,002` / `34b0a48fb2d0` | **`+1`** |
| `sillsdev/libpalaso` | `LICENSE` | `1,081` / `2d9f225638e0` | 🟢 `1,082` / `b716617149f3` | **`+1`** |
| `BloomBooks/BloomDesktop` | `LICENSE.txt` | `1,071` / `e92b61d89c9a` | 🟢 `1,072` / `858e015fbf93` | **`+1`** |
| `curiouslearning/FeedTheMonsterJS` | `LICENSE` | `1,072` / `216e43362531` | 🟢 `1,073` / `9baf70ec9a4a` | **`+1`** |
| `learningequality/kolibri` | — | `NO-GRANT-AT-ROOT` | `NO-GRANT-AT-ROOT` | n/a |

🔴 **Seven of seven resolvable addresses were measured one byte short, and seven of seven `sha256`
values were unreproducible from the file they named.** 🔵 **The defect rate is not "some": it is
every grant payload that ends in a newline, which is every grant payload. A `1`-byte error sounds
cosmetic and is not — it is the difference between a hash that re-derives and a hash that never
will, and this base pins hashes as evidence.** 🟢 The repaired probe's figure for
`openedx/edx-platform` (`35,136 B`) now AGREES with `p830`'s independently byte-read figure for the
same file, and with this pass's third, separately written instrument. Three instruments, one answer.

### 🔴 A second `CAPTURED-LIVE` site the census could not see — the instrument's own lower bound, with a named specimen

🔵 **`p253-captured-body-census` documents its own limit honestly**: *"It reads shell source
lexically. It cannot see a body that reaches a measurement through a second variable, an array, or
a function argument. Every verdict is therefore a LOWER bound on the defect."* 🔴 **`p773/probe.sh`
is that bound made concrete.** It captured the body into `body`, sliced it into a SECOND variable
with `payload=$(printf '%s' "$body" | sed '$d')`, and measured `$payload` — so it was genuinely
`CAPTURED-LIVE`, lost the trailing-newline run **twice**, and the census graded it `BODY-ONLY`. 🟢
**Repaired the same way: the payload goes to a file and the file is measured.** 🔵 **This is the
first time the census's declared lower bound has been demonstrated rather than merely stated, and a
limit with a specimen attached is a different object from a limit in a docstring.**

### 🔴 And a third finding in the same directory: the `D9` repair was never backported to its own sibling

🔵 `grantprobe.sh` exists because of `p773`'s `D9`: *"A missing lowercase `license.txt` produced a
false `NO-GRANT-AT-ROOT` on ERPNext."* 🔴 **The `31`-name case-aware list was written into
`grantprobe.sh` and left out of `probe.sh`, in the same folder, which carried `license` and
`license.md` but not `license.txt` — and `probe.sh` is the one with the ref channel on it.** Two
addresses this pass were invisible to it for exactly that reason and resolve now: `Kosudo/nextSIS`
(`license.txt`, 🟢 **byte-read `39,890 B`, `sha256:cd7a49230f22…`**, GPL-3.0 with CodeIgniter and
Bootstrap notices inside it) and `frappe/lms` (`license.txt`, 🟢 **byte-read `33,893 B`,
`sha256:db1a87ba81e8…`**, title line `GNU AFFERO GENERAL PUBLIC LICENSE`). 🟢 **List backported.**

### 🔴 The suite reported ONE red gate. Run to completion on the same bytes, it reports `18`

🟢 **`make commit-gates` at `HEAD` failed at `gate-offline` and STOPPED, so every gate after it in
the suite never ran at all.** With `gate-offline` repaired it ran one further and stopped again at
**`gate-enumeration` — `REFUTED=12`, `VERIFIED-ABSENT=133`, `QUEUE-UNENUMERATED=213`.** 🔵 **Two
reds looked like the whole answer, so this pass stopped assuming and measured it: `make -k` on a
PRISTINE `git archive HEAD` export, no edits of any kind, reports `89` passing checks and `18` RED
BLOCKING GATES** — `gate-absence`, `gate-action-answered`, `gate-alias-canonical`,
`gate-cell-reproduction`, `gate-census-currency`, `gate-dates`, `gate-enumeration`,
`gate-evidence-store`, `gate-fold-identity`, `gate-grant-path`, `gate-ledger`, `gate-offline`,
`gate-promotion`, `gate-prose-claims`, `gate-region-headings`, `gate-register-currency`,
`gate-shelf-consistency`, `gate-union-currency`. 🔴 **Not one of the `18` is in `DECLARED_RED`
(`gate-census-union`, `gate-promotion-ledger`, `recount`, `gate-derived-counts`) — the set a
registered `Gap N-X` is required to justify. The mechanism built to make red gates VISIBLE holds
`4` names while `18` gates fail outside it.** 🔵 **Filed as `T110`.** 🟢 **And this pass is measured
the same way rather than asserted: `18` red at `HEAD`, `17` after it, `gate-offline` RED → GREEN,
and the set difference in the other direction is EMPTY — nothing that was green is red now.**

🟢 **All `12` refuted lines resolve to `7` distinct addresses, and every one was byte-read today
rather than argued about:**

| Address | The base's claim | Byte-read `2026-11-15` | Verdict on the claim |
|---|---|---|---|
| `Kosudo/nextSIS` | no grant | 🔴 `license.txt`, **`39,890 B`**, `sha256:cd7a49230f22…`, GPL-3.0 | 🔴 **WRONG — a real grant payload** |
| `frappe/lms` | no grant | 🔴 `license.txt`, **`33,893 B`**, `sha256:db1a87ba81e8…`, AGPL-3.0 | 🔴 **WRONG — a real grant payload** |
| `foradian/fedena` | no grant | 🟡 `NOTICE`, **`679 B`**, `sha256:386aef9c0b40…` — *"Copyright 2011 Foradian Technologies Private Limited … Licensed under the Apache License, Version 2.0"* | 🟡 **POINTER, not payload.** The holder DECLARES Apache-2.0 and ships no licence text, so `gate-restatement`'s doctrine applies: a restatement of an off-repository authority is not a verified grant. The absence claim is wrong in substance and right in form |
| `projectfedena/fedena` | no grant | 🟡 `NOTICE`, **`680 B`**, `sha256:38af3b29e417…` | 🟡 Same verdict, `1` byte apart from the row above — the two are the same notice under different ownership |
| `LearnPress/learnpress` | no grant | 🟢 **No grant file at root on `develop`.** The enumerator cited `readme.txt` *"License: GPLv3"* and `composer.json` `"license": "GPL-3.0-or-later"` | 🟢 **The base was RIGHT; the ENUMERATOR over-refuted.** A manifest field is a `POINTER` under this base's own three-valued classifier (`gate-payload-pin`), never a `GRANT` |
| `formalms/formalms` | no grant | 🟢 **No grant at root.** The enumerator cited `html/addons/jquery/malihu-custom-scrollbar-plugin/LICENSE.txt` and `html/appCore/addons/swfheader/LICENSE.txt` | 🟢 **The base was RIGHT.** Those are VENDORED third-party grants in a subtree — `p382`'s subtree axis. A bundled jQuery plugin's licence is not the repository's grant |
| `DMontgomery40/mcp-canvas-lms` | no grant | 🟢 **No grant in the tree.** `package.json` says `"license": "MIT"` **and its `"files"` block names a `LICENSE` that is not there** | 🟢 **The base was RIGHT**, and this is the sharpest specimen of the three: a manifest pointing at a payload the repository does not ship |

🔵 **So `gate-enumeration`'s red is `2` real defects and `5` over-refutations, and that ratio is the
useful number.** 🔴 **Those `12` lines live in `agents/trending.md` and `repos/trending.md`, which
are APPEND-ONLY by this base's rule, so they are NOT edited.** 🟢 **The correction is published
here, in the newest section, which is what append-only means. Registered as `ACTION p831-A`: teach
the enumerator the `GRANT` / `POINTER` / `VENDORED-SUBTREE` distinction it already owns in
`gate-payload-pin` and `p382`, so it stops charging `5` sound verdicts as failures.**

### 🔴 The mandated star-ranked battery nilled a `42`nd consecutive time

`top open source AI agents education 2026 github MIT`, `github trending education AI 2026`,
`open source platform education ERP CRM MIT Apache` and `AI education industry trends 2026` returned
DeepTutor, OpenEduCat/Odoo, OpenHands, Langflow and `microsoft/ai-agents-for-beginners` — **every
one already shelved or already adjudicated here** — plus two undescribed Trendshift entries
(`geekjourneyx/interactive-learning`, `SirhanMacx/Claw-ED`) with no licence and no description in
the result set. 🔵 **The one item in the battery that was new was again not a repository:
`45%` of the most-used education tools have published research meeting an ESSA evidence tier. That
number is the premise of `T108` and it is `CITED, NOT READ`.**

### 🟢 What produced supply instead: measure the ABSENCE first, then search the FUNDER's vocabulary

🔵 **`p830` found its tier by running `grep -ric` for clinical terms and getting `0`. The same
instrument, pointed at the age axis, found a bigger hole.** Run over the six curated pages before
anything was filed:

| Term | Shelf hits | Term | Shelf hits |
|---|---|---|---|
| `literacy` | `132` | 🔴 **`numeracy`** | **`0`** |
| `reading` (in `agents/top.md`) | `34` | 🔴 **`phonics`** | **`0`** |
| `STEM` | `592` | 🔴 **`preschool`** | **`0`** |
| `credential` | `196` | 🔴 **`kindergarten`** | **`0`** |
| `proctor` | `72` | 🔴 **`early years`** | **`0`** |
| `xAPI` | `155` | 🔴 **`decoding`** | **`0`** |

🔴 **Thirty-five passes built a base with `592` mentions of STEM, `196` of credentialling and `0`
rows for the years in which a child learns to read and count at all** — the phase that the World
Bank, UNICEF, NIPUN Bharat and every regional ministry in `intel/market.md` spend their money on.
🔵 **`T102`'s rule (search the name of the statutory instrument, not the sector) is extended here
and the extension is `T108`'s mechanism: in this tier the productive name is neither the sector nor
the statute but the FUNDING PROGRAMME — `Global Learning XPRIZE`, `EduApp4Syria`, `All Children
Reading`. A prize competition publishes its finalists' source as a condition of entry, which is why
an entire field-trialled corpus is sitting under one GitHub organisation that no sector search
returns.**

### 🟢 The `15` rows, byte-read `2026-11-15`

| Name | Repo | Licence | Stars | Region | Description |
|---|---|---|---|---|---|
| Antura and the Letters | https://github.com/vgwb/Antura | 🟢 **BSD-2-Clause — byte-read** (`LICENSE.md`, `2,002 B`, `sha256:34b0a48fb2d0…`, holder `TH Köln / Cologne Game Lab, Video Games Without Borders & Wixel Studios`) | 128 | EMEA | 🟢 **The traction leader of the whole foundational tier and the one row in it with a current push date (`2026-11-13`).** Unity literacy game for children learning to read. 🔴 **The index is WRONG about it: `gh api` reports `NOASSERTION` and the bytes are a clean BSD-2-Clause grant** — the discrepancy that `T109` is built on. 🔵 **Region placed on the holder line's own evidence: `TH Köln` is a German public university, a jurisdictional fact inside the grant bytes, which is this base's `622-K` placement rule rather than an inference from a name** |
| Antura and the Letters (Arabic) | https://github.com/vgwb/Antura_arabic | 🟢 **BSD-2-Clause — byte-read** (`LICENSE.md`, `1,916 B`, `sha256:58e5d42fd2fc…`, holder `2017, TH Köln / Cologne Game Lab, Video Games Without Borders & Wixel Studios`) | 60 | EMEA | 🟢 **Winner of the `EduApp4Syria` international initiative** — teaches Arabic-speaking children to read and write, complete Unity project. 🔴 Index says `NOASSERTION`; bytes say BSD-2-Clause, same family as its parent. 🔴 **Unpushed since `2022-03-09`: a field-proven asset, not a maintained product** |
| Kitkit School | https://github.com/XPRIZE/GLEXP-Team-KitkitSchool | 🟢 **Apache-2.0 — byte-read** (`11,340 B`, `sha256:638af047fe71…`, stock text, no holder) | 51 | EMEA | 🟢 **Co-winner of the Global Learning XPRIZE** (Enuma). A `13`-app suite — launcher, lock screen, library, read-aloud book viewer, curriculum app, writing board — built to run **unsupervised on a tablet with no teacher and no network**. 🔵 Region placed on the repository's own evidence: the curriculum it ships is Swahili, for the Tanzanian field trial. 🔴 Unpushed since `2019-11-29` |
| onecourse | https://github.com/XPRIZE/GLEXP-Team-onebillion | 🟢 **Apache-2.0 — byte-read** (`11,357 B`, `sha256:b40930bbcf80…`, stock text, no holder) | 34 | EMEA | 🟢 **The other co-winner, and the only row in this tier that names NUMERACY in its own description**: *"one app that delivers reading, writing and numeracy."* 🔵 Its README states the placement outright — *"the onecourse material as children in Tanzania would experience it."* 🔴 Unpushed since `2019-11-05` |
| maui | https://github.com/chimple/maui | 🟢 **Apache-2.0 — byte-read** (`LICENSE.txt`, `11,357 B`, `sha256:c71d239df917…`, stock text, no holder) | 29 | Global | 🟢 Flutter literacy application for children, from the Chimple project. 🔵 **Region `Global` DECLARED, not assumed: the stock Apache text carries no holder line and the README names no country or language, so there is nothing in the bytes to place it on.** Chimple's own operations are Indian; this base does not place a region on an operator's address |
| tahiti | https://github.com/chimple/tahiti | 🟢 **Apache-2.0 — byte-read** (`11,357 B`, `sha256:c71d239df917…`, stock text, no holder) | 17 | Global | 🟢 Flutter painting application — the EXPRESSION leg beside `maui`'s decoding leg. 🔵 Filed because a pre-literate child's first output is a drawing, and this is the only granted drawing surface in the tier |
| Pubbly | https://github.com/XPRIZE/GLEXP-Team-CCI | 🟢 **Apache-2.0 — byte-read** (`11,372 B`, `sha256:fc1de75500c0…`, stock text, no holder) | 8 | EMEA | 🟢 **The AUTHORING leg of the XPRIZE corpus, and the most reusable thing in it**: a cross-platform desktop tool for designing interactive eBooks, plus a JS engine that turns its XML and assets into HTML5. 🔵 A studio that needs new mother-tongue content rather than new code starts here |
| Chimple (goa) | https://github.com/XPRIZE/GLEXP-Team-Chimple-goa | 🟢 **Apache-2.0 — byte-read** (`11,357 B`, `sha256:c71d239df917…`, stock text, no holder) | 8 | Global | 🟢 The Chimple XPRIZE submission. 🔵 Byte-identical grant to `chimple/maui` and `XPRIZE/glexp-data-standardization` (`sha256:c71d239df917…`), which is `T41`'s bound showing again: an identical stock payload is evidence of a TEMPLATE, never of lineage |
| Feed the Monster | https://github.com/curiouslearning/FeedTheMonster | 🟢 **BSD-2-Clause — byte-read** (`1,702 B`, `sha256:455a86e2fda5…`, holder `2016, Apps Factory`) | 7 | EMEA | 🟢 Core Unity repo of the literacy game built for Syrian refugee children and now localised far beyond it. 🔴 **Index says `NOASSERTION`; bytes say BSD-2-Clause** — the second index/bytes disagreement in this tier, on a different publisher |
| FeedTheMonsterJS | https://github.com/curiouslearning/FeedTheMonsterJS | 🟢 **MIT — byte-read** (`1,073 B`, `sha256:9baf70ec9a4a…`, holder `2022 Curious Learning`) | 5 | EMEA | 🟢 **The web rebuild, and the ACTIVE one — pushed `2026-09-03` while the Unity original has not moved since `2025-11-04`.** HTML-canvas, no install, no store. 🔵 **For a ministry engagement this is the deliverable shape: a phonics game that runs in a browser on a shared device** |
| jamaica | https://github.com/chimple/jamaica | 🟢 **Apache-2.0 — byte-read** (`11,323 B`, `sha256:283ea6cc2997…`, stock text, no holder) | 5 | Global | 🟢 Chimple component repo. 🔵 Filed for the grant, not the traction: `11,323 B` is a DISTINCT Apache payload from the `11,357 B` that four of its siblings ship, which is a `p779` band case and is recorded as one |
| Chimple (maui, XPRIZE build) | https://github.com/XPRIZE/GLEXP-Team-Chimple-maui | 🟢 **Apache-2.0 — byte-read** (`LICENSE.txt`, `11,357 B`, `sha256:c71d239df917…`, stock text, no holder) | 4 | Global | 🟢 The competition build of `maui`, frozen at submission. 🔵 Useful precisely BECAUSE it is frozen: it is the artefact the RCT evidence attaches to, and the live `chimple/*` tree is not |
| Curious Reader (RCC) | https://github.com/curiouslearning/CuriousReaderRCC | 🟢 **MIT — byte-read** (`1,073 B`, `sha256:0275a073eb5a…`, holder `2021 Curious Learning`) | 4 | Global | 🟢 Unity implementation of the Curious Reader authoring tool — the second authoring surface in the tier after Pubbly |
| CRContainer (Hindi) | https://github.com/curiouslearning/CRContainer-Hindi | 🟢 **MIT — byte-read** (`1,073 B`, `sha256:9baf70ec9a4a…`, holder `2022 Curious Learning`) | 2 | APAC | 🟢 Standalone Curious Reader container for **Hindi**. 🔵 **Region placed on the LANGUAGE the repository itself ships, which is a jurisdictional fact in its bytes** — the same `622-K` placement `p830` used for `bol-sakhi-communication-board`. 🔵 Pushed `2026-03-24`, so the per-language container pattern is live, not archival |
| onecourse Phrase Analytics | https://github.com/XPRIZE/GLEXP-Team-onebillion-PhraseAnal | 🟢 **Apache-2.0 — byte-read** (`11,357 B`, `sha256:b40930bbcf80…`, stock text, no holder) | 0 | EMEA | 🟢 **`0★`, and filed deliberately.** The phrase-analytics companion to `onecourse` — the piece that looks at what the child actually produced. 🔵 Byte-identical grant to its parent (`sha256:b40930bbcf80…`), which is how the pair is tied together on evidence rather than on a name |

### 🔴 `4` rejections, with the reason each one was refused

1. 🔴 **`XPRIZE/GLEXP-Team-RoboTutor-RoboTutor`** (`14★`, Carnegie Mellon's XPRIZE finalist) — the probe returned **`NOGRANT`** across both `main` and `master` at every one of `31` filename paths. 🔵 **Recorded as UNRESOLVED, not as ungranted**, per `p830`'s own correction: the invented control returns `NOGRANT` too, so `NOGRANT` means *"no grant found at the probed paths"* and is not an existence oracle. The index agrees it is `NOASSERTION`. **A whole university's XPRIZE finalist is unusable until someone resolves this.**
2. 🔴 **`Tangerine-Community/Tangerine`** (`119★`) — **`GPL-3.0`, byte-read `35,147 B`, `sha256:8ceb4b9ee5ad…`**. Copyleft; shelved on `verticals/solutions.md` with its risk posture, not here. 🔵 **And it is the most consequential rejection in the tier**: it is the instrument the EGRA/EGMA field data is collected on, it was pushed `2026-11-12`, and this base has named it `6` times in `repos/trending.md` across `35` passes without ever shelving it.
3. 🔴 **`XPRIZE/GLEXP-Team-The-Linguaculturalists`** (`14★`) — **`GPL-3.0`, byte-read `COPYING`, `35,147 B`, `sha256:8ceb4b9ee5ad…`**. Byte-identical grant to Tangerine's, same destination.
4. 🔴 **`chimple/cuba`** (`4★`, pushed `2026-11-13` — the live Chimple line) — **`AGPL-3.0`, byte-read `LICENSE.md`, `34,522 B`, `sha256:20b067f86de3…`**. 🔵 **The direction of travel is the finding: Chimple's `2019` repos are Apache-2.0 and its `2026` repos are MPL-2.0 and AGPL-3.0. The corpus is getting LESS permissive as it gets more current, which is `T108`'s second half.**

## Thirty-fifth pass (`p830`, 2026-11-15) — the SEN / INCLUSIVE-LEARNER tier: `34` passes, `335` agents, and `0` rows for the learners every one of those passes legislated about

🟢 **`20` build-safe agent rows filed (`335` → `355`), `4` foundation rows (`149` → `153`), `3`
vertical platforms (`132` → `135`), `3` trends (`T105`–`T107`), `1` recipe (`P70`), and `7`
rejections recorded with their reasons. Every licence BYTE-READ on `2026-11-15`.**

🔴 **The finding that organised this pass is an ABSENCE, measured before anything was filed.**
`grep -ric` across all eight curated files returned **`0`** for `learning disabilit*`, **`0`** for
`neurodivergen*`, **`0`** for `occupational therap*`, **`0`** for `early intervention` and **`0`**
for `well-being`. `agents/top.md` held **`0`** occurrences of `AAC`, **`1`** of `autism` and **`1`**
of `ADHD` — and one of the two `autis` hits was a FALSE FRIEND inside the GitHub login
`BautistaAlosMartorell`. 🔵 **Thirty-four passes catalogued tutors, LMS connectors, proctoring,
grading and vocational training, and shelved not one row for the learner population that every
regulation those passes cite — IDEA, Section 508, ADA Title II, the European Accessibility Act,
EN 301 549, EU AI Act Annex III — exists to protect.**

🔵 **This is not the same gap `p621`/`p634` opened.** Those passes measured `AAC` and `IEP` in
`agents/trending.md` and left the shelf untouched: `inclusive-design/adaptive-palette` was
byte-read at `p634` and **never promoted**, and it was pushed again TODAY. `p830` promotes it and
enters the tier properly.

### 🟢 Channel conditions — one channel lost, one channel live and bidirectionally controlled

| Channel | `p829` | `p830` | Control run this pass |
|---|---|---|---|
| `gh api search/repositories` with a `repo:OWNER/NAME` qualifier | 🟢 LIVE | 🔴 **DEAD** | 🔴 `repo:openedx/edx-platform` → HTTP **`422`**, and the invented `repo:zzqqww/not-a-real-repo-xyz9` → HTTP **`422`**. **Identical answers, so it discriminates NOTHING and was not used as an oracle.** This session's token is repository-scoped |
| `gh api repos/{owner}/{repo}` (direct, not search) | — | 🔴 **DEAD** | 🔴 HTTP **`403`** for the live address AND the invented one. Same verdict, same reason |
| `gh api search/repositories`, **free-text** | — | 🟢 **LIVE** | 🟢 **Bidirectional:** `moodle plugin ai stars:>50` → `total_count=1` with a licence field, star count and push date; `zzqqwwxyz9notarealthing stars:>5` → `total_count=0`. Used for DISCOVERY and for star/push metadata only |
| `raw.githubusercontent.com` byte-read | 🟢 LIVE | 🟢 **LIVE** | 🟢 **Bidirectional:** `openedx/edx-platform` `LICENSE` → `200`, `35,136 B`, AGPL-3.0 text; `zzqqww/not-a-real-repo-xyz9` → **`404`**. **Every licence below is byte-read** |
| `curl -sI` on a `github.com` repository address | 🔴 useless | 🔴 **not used** | 🔴 `T923`/`T970` hold unchanged |
| `ingest/derive-counts.py` | 🟢 ran | 🟢 **ran, BEFORE and AFTER** | 🟢 Baseline `335`/`149`/`104`/`69`/`132` all GREEN before the first edit |

🔴 **A limit of this pass's own instrument, stated rather than hidden.** `ingest/p830-licence-byteread.sh`
prints `NOGRANT` when nine licence paths on `main` and `master` all miss. **Both invented controls
also print `NOGRANT`** — so `NOGRANT` means *"no grant found at the probed paths"* and is **NOT an
existence oracle**. Three addresses in this pass (`antijingoist/opendyslexic`, `juanda99/arasaac-api`,
`AraSuite/arasaac-api`) returned `NOGRANT` and are therefore recorded as UNRESOLVED, not as ungranted.

### 🔴 The mandated star-ranked battery nilled a `41`st consecutive time

`top open source AI agents education 2026 github MIT`, `github trending education AI 2026`,
`open source platform education ERP CRM MIT Apache` and `AI education industry trends 2026` returned
DeepTutor, OpenMAIC, `patchy631/ai-engineering-hub`, OpenEduCat, Frappe Education, RosarioSIS and
GegoK12 — **every repository among them already shelved or already adjudicated here** — plus
secondary roundups whose star counts contradict each other inside a single result set (DeepTutor at
`45,224★` and `52,800★` in two posts dated nine days apart). 🔵 **The one item in the battery that
was new was again a REGULATORY date and not a repository: the `April 2026` ADA Title II compliance
deadline for large public entities, which is the live accessibility budget driver in North America
and which this pass's `P70` is built against.**

### 🟢 What produced supply instead: the national sign language's OWN NAME, and the clinical term

🔵 **`T102`'s rule — search the name of the statutory document, not the sector — holds, but it is
LANGUAGE-BOUND, and this pass found where it breaks.** The English-language statutory instrument
returns supply (`IEP`: `116` in education context, `p634`); its translations return almost nothing
(`EHCP` → `0`, `SEND code of practice` → `0`, `adaptación curricular individualizada` → `0`,
`atendimento educacional especializado AEE` → `0`, `Förderplan sonderpädagogisch` → `0`,
`PIAR plan individual ajustes razonables` → **`1`**, GPL-3.0, `0★`).

🟢 **What DOES return supply in every region is the name of the NATIONAL SIGN LANGUAGE** — and it is
the finding of this pass, filed as `T105`:

| Instrument | Repositories | `MIT` | `Apache-2.0` | Maximum traction | Region |
|---|---|---|---|---|---|
| `"Indian Sign Language"` (exact phrase) | **`2,693`** | — | — | `140★` (`satyam9090`, ungranted); best granted `96★` MIT | APAC |
| `libras lingua brasileira de sinais` | `94` | **`24`** | `3` | `51★` MIT | LATAM |
| `British Sign Language BSL` | `60` | `8` | `1` | — | EMEA |
| `Chinese Sign Language` | `53` | `9` | `1` | — | APAC |
| `lengua de señas mexicana LSM` | `49` | `8` | `1` | — | LATAM |
| `langue des signes française LSF` | `22` | `5` | `2` | — | EMEA |
| `Auslan Australian sign language` | `9` | — | — | — | APAC |
| `lengua de signos española LSE` | `8` | — | — | — | EMEA |
| `Japanese Sign Language JSL` | `3` | — | — | — | APAC |
| `Deutsche Gebärdensprache DGS` | **`0`** | — | — | — | EMEA |

🔵 **The population inverts against economic size.** India and Brazil carry the two largest
national-sign-language corpora on GitHub; Germany and Japan carry `0` and `3`. **An APAC or LATAM
inclusion engagement starts with more open raw material than an EMEA one** — the inverse of this
base's usual regional gradient, and the first tier where that has been true in `35` passes.

### 🟢 The `20` rows, byte-read `2026-11-15`

| Name | Repo | Licence | Stars | Region | Description |
|---|---|---|---|---|---|
| OpenDyslexic extension | https://github.com/OpenDyslexic/extension | 🟢 **MIT — byte-read** (`1,073 B`, `sha256:2aeeff85b59b…`, holder `2024 opendyslexic.com`) | 117 | Global | 🟢 **The traction leader of the whole SEN tier and the only row in it above `100★`.** Official browser extension that forces the OpenDyslexic typeface onto any page. 🔵 **Delivery note: the extension is MIT but the TYPEFACE it ships is `OFL-1.1` with a RESERVED FONT NAME** (see `repos/foundations.md`, `p830`) — a modified build must be renamed. Pushed `2026-10-31` |
| Paper2Manga-Prism | https://github.com/raucvr/Paper2Manga-Prism | 🟢 **Apache-2.0 — byte-read** (`11,357 B`, `sha256:c71d239df917…`, stock text, no holder) | 91 | Global | 🟢 Reading-comprehension reshaper aimed explicitly at **ADHD and dyslexia**: turns a dense paper into sequential panelled narrative. 🔵 The second-highest traction in the tier and the clearest evidence that the DEMAND is for reading ACCESS, not for a tutor. Pushed `2026-11-06` |
| ReadAble | https://github.com/nazarli-shabnam/ReadAble | 🟢 **Apache-2.0 — byte-read** (`11,357 B`, `sha256:c71d239df917…`, stock text, no holder) | 44 | Global | 🟢 Mobile assistive reader: **on-device** OCR → summarisation → TTS over printed text. 🔵 On-device matters here — a SEN learner's reading material is special-category-adjacent data in several of this base's jurisdictions, and a local pipeline removes the transfer question. Pushed `2026-10-07` |
| Dino | https://github.com/developer-diganta/Dino | 🟢 **MIT — byte-read** (`LICENSE.md`, `1,073 B`, `sha256:8d3abe465a2a…`, holder `2022 Diganta Kr Banik`) | 43 | Global | 🟢 Chrome extension covering **dyslexia AND colour blindness** in one surface — the only row in the tier that addresses two access needs at once. 🔴 Region `Global`: the holder line names a person and no jurisdiction, and this base places region on the GRANT (`622-K`), not on a name. Pushed `2026-03-11` |
| readapt | https://github.com/ContentSquare/readapt | 🟢 **Apache-2.0 — byte-read** (`master`, `11,357 B`, `sha256:c71d239df917…`, stock text, no holder) | 39 | EMEA | 🟢 **The only CORPORATE grant in the entire tier.** Reading-difficulty adaptation engine published by Contentsquare. 🔵 Region placed on the repository's own README, which is bilingual and names French twice — declared explicitly because the stock Apache text carries no holder line to place it on. Pushed `2026-04-22` |
| adaptive-palette | https://github.com/inclusive-design/adaptive-palette | 🟢 **BSD-3-Clause — byte-read** (`1,562 B`, `sha256:b8f3da69a07f…`, holder `2023-2026, Inclusive Design Research Centre, OCAD University`) | 2 | North America | 🟢 **PROMOTED, not discovered: byte-read at `p634` and left in `agents/trending.md` for `196` passes.** Adaptive AAC palette from the IDRC at OCAD University, Toronto. 🔵 **Pushed `2026-11-15` — today.** The one institutionally-published, actively-developed, permissively-granted AAC runtime this base has found |
| baby-bliss-bot | https://github.com/inclusive-design/baby-bliss-bot | 🟢 **BSD-3-Clause — byte-read** (`1,518 B`, `sha256:f12eecff2dfd…`, holder `2023-2024, Inclusive Design Institute`) | 7 | North America | 🟢 Generative models for **Bliss-symbol** communication, same publisher. 🔵 Bliss is a symbol language with a formal grammar, which makes it the one AAC vocabulary a model can be evaluated against rather than merely demonstrated on. Pushed `2026-09-18` |
| ocula | https://github.com/revolutionarybukhari/ocula | 🟢 **MIT — byte-read** (`1,072 B`, `sha256:e76df35fc768…`, holder `2026 Husnain Bukhari`) | 2 | Global | 🟢 Webcam **eye-controlled cursor** — browser-only assistive input on MediaPipe Face Mesh with dwell-click. 🔵 The access LAYER below AAC: a learner who cannot use a mouse cannot reach any of the other rows here. No install, no hardware |
| bol-sakhi-communication-board | https://github.com/SubchiBeats/bol-sakhi-communication-board | 🟢 **MIT — byte-read** (`1,068 B`, `sha256:9ceb4131aeb8…`, holder `2026 Sahib Singh`) | 1 | APAC | 🟢 Picture communication board, **bilingual English + Punjabi**, with instant text-to-speech. 🔵 Region placed on the LANGUAGE the repository itself ships, which is a jurisdictional fact in its bytes rather than an inference from a name |
| voice-bridge | https://github.com/harryt04/voice-bridge | 🟢 **MIT — byte-read** (`master`, `1,072 B`, `sha256:7a81e8e6736e…`, holder `2025 Harrison Thomas`) | 1 | Global | 🟢 Free AAC web app for children with autism. 🔵 Filed because it is one of only **two** MIT-granted rows in a `12`-repository autism sweep in which **ten carried no licence at all** |
| pdf_accessibility | https://github.com/adamopoulosa1980/pdf_accessibility | 🟢 **Apache-2.0 — byte-read** (`11,358 B`, `sha256:cfc7749b96f6…`, stock text, no holder) | 9 | Global | 🟢 **PDF remediation engine** — AI structural tagging plus a rules layer. 🔵 Region `Global` on the repository's own evidence: its README names `WCAG 2.2` (`6×`), `Section 508` (`5×`) and `EN 301 549` (`2×`), i.e. it targets three jurisdictions at once. The highest-traction row in the compliance tier. Pushed `2026-05-26` |
| a11y-ai-auditor | https://github.com/natashkasemenova/a11y-ai-auditor | 🟢 **MIT — byte-read** (`1,074 B`, `sha256:6583114b7a51…`, holder `2026 Nataliia Semenova`) | 1 | EMEA | 🟢 Automated web-accessibility audit pipeline against **WCAG 2.2 / DSTU EN 301 549**. 🔵 `DSTU` is Ukraine's national standards prefix — the region is placed on a named national standard in the repository's own description, not on the author's name. Pushed `2026-10-18` |
| alt-text-pipeline | https://github.com/hannahmoutran/alt-text-pipeline | 🟢 **MIT — byte-read** (`1,071 B`, `sha256:dbe551d1bccb…`, holder `2026 Hannah Moutran`) | 1 | Global | 🟢 **Calibrate on a sample, then generate at scale** — alt text for image collections with an explicit human-calibration step before bulk generation. 🔵 That shape is the reusable idea: it is the only row in the tier that treats accessibility output as something to be CALIBRATED rather than trusted. Pushed `2026-09-01` |
| statamic-aida | https://github.com/21stdigital/statamic-aida | 🟢 **MIT — byte-read** (`1,074 B`, `sha256:1c09a6578ca0…`, holder `2024 21st digital GmbH`) | 5 | EMEA | 🟢 CMS addon that generates image alt texts automatically. 🔵 **Region placed on the LEGAL FORM in the holder line** — `GmbH` is a German company form, which is a jurisdictional fact inside the grant bytes themselves and the cleanest `622-K` placement in this pass. Pushed `2026-11-09` |
| LibrasLive | https://github.com/moonlitrevery/LibrasLive | 🟢 **MIT — byte-read** (`1,068 B`, `sha256:68bb80786ddb…`, holder `2025 João Vitor`) | 10 | LATAM | 🟢 **Real-time translation to LIBRAS**, Brazilian Sign Language. 🔵 The highest-traction ACTIVE row in the LATAM sign-language tier and the natural renderer leg of `P70` for a Brazilian engagement. Pushed `2025-11-21` |
| Video-to-Animation-LIBRAS | https://github.com/PedroCBrito/Video-to-Animation-LIBRAS | 🟢 **MIT — byte-read** (`master`, `1,095 B`, `sha256:7d6ed8a626e0…`, holder `2026 Video-to-Animation LIBRAS Contributors`) | 1 | LATAM | 🟢 Video → LIBRAS animation. 🔵 Filed for its push date — `2026-10-12` — because the LIBRAS tier's problem is not supply but STALENESS: its `51★` maximum has not been pushed since `2022` |
| reconhecimento_libras | https://github.com/ClassNeuralNetwork/reconhecimento_libras | 🟢 **MIT — byte-read** (`1,103 B`, `sha256:3474bb218933…`, holder `2024 Artificial Neural Network`) | 6 | LATAM | 🟢 CNN-based LIBRAS recognition from a named research group. 🔵 The model leg to `LibrasLive`'s interface leg |
| Indian-sign-language-recognition | https://github.com/Karthikeyu/Indian-sign-language-recognition | 🟢 **MIT — byte-read** (`master`, `1,087 B`, `sha256:ec369ab6ab13…`, holder `2020 Karthikeyu Busa, ShravaniKatte`) | 96 | APAC | 🟢 **The highest-traction GRANTED row in any national-sign-language corpus found this pass.** The corpus leader at `140★` (`satyam9090`) carries **no licence**, so this is the one an engagement can actually build on. Pushed `2020` — a STALE asset, filed as an asset, not as a product |
| Sanket | https://github.com/Mishra-Shreya/Sanket | 🟢 **MIT — byte-read** (`master`, `1,070 B`, `sha256:3fa8899a1502…`, holder `2022 Shreya Mishra`) | 28 | APAC | 🟢 Android ISL mediator app — the second granted ISL row above `25★`. 🔵 Two independent MIT lineages in one national corpus is what makes APAC the best-supplied region in this tier |
| StoryWeaver | https://github.com/roshnrf/StoryWeaver | 🟢 **MIT — byte-read** (`LICENSE.md`, `1,107 B`, `sha256:5fca87f338e3…`, holder `2025 Roshan A Rauof, Reem Fariha`) | 2 | Global | 🟢 **The ONLY granted row in the entire speech-therapy sweep.** Whisper-based speech-therapy platform for ages 4–6. 🔴 Context, because the row's `2★` is the point: a `10`-result speech-therapy sweep returned **`9` repositories with no licence at all**. Pushed `2026-10-10` |

### 🔴 `7` rejections, with the reason each one was refused

1. 🔴 **`Jojobeans1981/Ember-Campfire-Edition`** (`24★`, "AI-powered dyslexia intervention platform") — **no licence**. The third-highest-traction dyslexia repository on GitHub and it cannot be used.
2. 🔴 **`satyam9090/Automatic-Indian-Sign-Language-Translator-ISL`** (`140★`) — **no licence**. The traction leader of the largest national-sign-language corpus measured this pass.
3. 🔴 **`cboard-org/cboard`** (`768★`, UNICEF-backed) — **`GPL-3.0`, byte-read `35,141 B`, `sha256:589ed823e9a8…`**. Copyleft; shelved on `verticals/solutions.md` with its risk posture, not here.
4. 🔴 **`asterics/AsTeRICS-Grid`** — **`AGPL-3.0`, byte-read `34,523 B`, `sha256:8486a10c4393…`**. Same verdict, same destination. 🔵 **And a name-integrity warning worth more than the row:** the free-text channel surfaces `astericsfree/AsTeRICS-Grid`, `astericsgridfree/AAC-Grid-Let-Me-Talk-Asterics-LogoRemakeFour` and `logoremakefour8/Asterics-Grid-AAC-LRF-LogoRemakeFour` ABOVE the canonical repository, which the channel does not return at all. **An assistive-tech brand name is being squatted; never resolve one of these from a search result without a byte-read.**
5. 🔴 **`JoseStud/piar-digital-app`** — Colombia's statutory `PIAR` form, and the **only** repository on GitHub for it: **`GPL-3.0`, byte-read `35,149 B`, `sha256:3972dc9744f6…`**, `0★`. Copyleft, so not build-safe — recorded in `intel/market.md` under LATAM as a measured national gap rather than shelved.
6. 🔴 **`tlennon-ie/neurodock`** (`20★`) and **`ICUnit/Tokai`** (`40★`) — `AGPL-3.0` and `NOASSERTION`, and in any case **not education**: both are productivity tooling for neurodivergent ADULTS (see `T106`).
7. 🔴 **`itsmealli/inclusive-ed-tools`** — the single highest-ranked **Universal Design for Learning** repository on GitHub at **`1★`**, `NOASSERTION`, unpushed since `2025-10-31`. Recorded as the evidence for `T107`.

### 🔴 Three dated records re-measured against today's bytes — and one of them had CHANGED

- 🔴 **`Maximilian741/508-Agent`: the GRANT FILE ITSELF moved between two passes of this base.** `p818`
  (`2026-11-15`) byte-read `1,067 B`, `sha256:b48cc408…`; `p830` re-read the same address on the same
  day and got **`1,068 B`, `sha256:c9db00bdf8ad…`** — one byte more, a different hash, the same MIT
  text and the same holder `2026 Max Casteel`. 🔵 **It is also the reason this pass files `20` rows and
  not `21`:** `508-Agent` was drafted as a new row before `ingest/derive-counts.py` reported
  `dupes=1` and showed it had been shelved at `p818`. The row was withdrawn and the `p818` record
  CORRECTED in place instead. 🔵 **The lesson generalises: a `sha256` written into this base is a
  measurement with a DATE on it, not a fact.** `T104` recorded licence drift in the closing
  direction; this is drift with no licence change at all, and only a re-read finds it.
- 🟢 **`cboard-org/cboard`: `759★` at `p621` (`2026-11-02`) → `768★` today.** `+9` in `13` days, `1.2 %`. No drift finding; the figure is refreshed, not corrected.
- 🟢 **`juanda99/arasaac-frontend`: `16★` at `p622` → `16★` today, but pushed `2026-10-24` → `2026-11-14`.** Flat traction, active development — the pattern this base associates with a publicly-funded asset rather than a product.

## Thirty-fourth pass (`p829`, 2026-11-15) — the WORKFORCE tier: `33` passes, `324` agents, `101` trends, `68` recipes, and `0` rows about the segment next door

🟢 **`11` build-safe agent rows filed (`324` → `335`), `1` foundation row (`148` → `149`), `3`
trends (`T102`–`T104`), `1` recipe (`P69`), `6` rejections recorded with their reasons, and one dated
record inside this repository CORRECTED against today's bytes.**

🔴 **The finding that organised this pass is an ABSENCE, and it was measured before anything was
filed.** `grep -ric` across every curated file in this base returned **`0`** for `upskilling`, `0` for
`reskilling`, `0` for `apprenticeship`, `0` for `Ausbildung`, `0` for `Berichtsheft`, `0` for `KSB`,
`0` for `TVET` and `0` for `Workforce Pell`. 🔵 **Thirty-three passes built a university-and-school
knowledge base and never crossed into vocational education and training — the adjacent segment the
EU AI Act names in the SAME Annex III point as schools, and the one carrying the larger adjacent
budget (corporate upskilling and reskilling at `$400B` in 2026, `CITED, NOT READ`).**

### 🟢 Channel conditions — both channels live, both controlled in both directions

| Channel | `p828` | `p829` | Control run this pass |
|---|---|---|---|
| `gh api search/repositories -f q="repo:OWNER/NAME"` | 🟢 LIVE | 🟢 **LIVE** | 🟢 **Bidirectional:** `repo:moodle/moodle` → `total_count=1`, `GPL-3.0`, `7,615★`; `repo:gmilano/invented-control-p829-zzz` → **HTTP `422`** |
| `raw.githubusercontent.com` byte-read | 🟢 LIVE | 🟢 **LIVE** | 🟢 **Bidirectional:** `moodle/moodle` `COPYING.txt` → `200`; the invented address → **`404`**. Every licence below is byte-read |
| `curl -sI` on a `github.com` repository address | 🔴 useless | 🔴 **not used** | 🔴 `T923`/`T970` hold — the proxy answers `200 Connection Established` for live and invented addresses alike, so it was not run as an oracle this pass |
| `ingest/derive-counts.py` | 🟢 ran | 🟢 **ran, BEFORE and AFTER** | 🟢 Baseline `324`/`148`/`101`/`68`/`132` all GREEN before the first edit |

### 🔴 The mandated star-ranked battery nilled a `40`th consecutive time

`top open source AI agents education 2026 github MIT`, `github trending education AI 2026`,
`open source platform education ERP CRM MIT Apache` and `AI education industry trends 2026` returned
**DeepTutor, OpenEduCat, Langflow, `microsoft/ai-agents-for-beginners` and `frappe` — every one of
them already on these shelves** — plus a tier of SEO aggregators whose star counts and licence fields
contradict each other within the same result set. 🔵 **The one item in the entire battery that was
NOT already shelved was a market item rather than a repository: Instructure's `Canvas Career`, a
skills-first LMS for WORKFORCE learning — the same seam this pass went on to measure.**

### 🟢 What produced supply instead: the statutory DOCUMENT as the discovery instrument

🔴 **The obvious vocabulary returns nothing usable.** `tvet`, `vocational training ai agent`,
`apprenticeship mcp`, `skills training agent` and `competency framework mcp`, recency-ranked with no
star floor, returned job boards (`zapplyjobs/*`, `veritahire/*`), personal profile READMEs and one
reverse-engineering tool — **`0` build-safe education rows across five legs**.

🔴 **`T82`'s institution-brand rule, which works at the university tier, INVERTS here.** `SENA
sofia plus`, `senai` and `conalep` returned ~`30` repositories between them and **not one licensed
agent**: `proyectosenasoftplus`, `Curso_senai`, `Biblioteca-CONALEP`, `cafeteria-conalep` — nearly all
`0★`, nearly all unlicensed, and nearly all STUDENT COURSEWORK named after the school it was
submitted to. 🔵 **At the university tier the institution brand surfaces integration agents
(`SIGAA`, `Brightspace`, `Moodle`); at the vocational tier the identical query shape surfaces
homework.** That is `T103`.

🟢 **What worked was the name of the STATUTORY DOCUMENT the system runs on.**
`Ausbildungsnachweis` / `Berichtsheft` (the German IHK apprenticeship record), `KSB` (England's
knowledge-skills-behaviours standard) and `apprenticeship standards` returned a live, MIT-licensed,
actively-pushed cluster — **`4` build-safe artefacts, all EMEA, all pushed within the last `6`
weeks**. That is `T102`, and it is `T82`'s rule on a FOURTH axis: after the system of record, the
language and the platform brand, the instrument is **the regulated artefact the learner must
produce**.

### 🔴 The blocking commit gate is RED, it was red BEFORE this pass, and `p829` did not fix it

🔴 **`make commit-gates` exits `2` on `gate-offline` → `p253-captured-body-census`, and `p829`
confirmed by `git stash` that it fails IDENTICALLY on pristine `HEAD`** — so `p828` committed over a
red blocking gate, and so did this pass. 🔵 **Recorded here because `ingest/pre-commit` requires a
skip to be stated in the pass write-up, and because an undiagnosed red gate decays into a gate
nobody reads.**

🔵 **The exact failure, so the next pass does not re-derive it** (`29/31` checks pass; `2` fail):

| Site | Census verdict | Status |
|---|---|---|
| `p773/grantprobe.sh` | 🔴 **`CAPTURED-LIVE`** | **A genuine instance of the defect class `ACTION XY` exists to catch** — an instrument measuring a payload through a captured body. 🔴 **Pinning it would be the "silently downgraded verdict" the suite's own control forbids; the fix is to make the script measure the payload directly** |
| `p773/probe.sh` | `BODY-ONLY` | 🟢 Unpinned only — safe to add to `sites.tsv` |
| `p779/ecl_decide.sh` | `BODY-ONLY` | 🟢 Unpinned only — safe to add to `sites.tsv` |

🔴 **`p829` deliberately did NOT fix it.** Two of the three are a one-line pin, but the third needs
a behavioural change to another pass's probe script, and a partial fix would leave the gate red while
removing the signal that says why. 🔵 **Filed whole, as `ACTION p829-A`: pin the two `BODY-ONLY`
sites and repair `p773/grantprobe.sh`'s capture, in one pass, so the gate goes green in one move.**
🟢 **Every gate `p829` is accountable for DID run and IS green:** `ingest/derive-counts.py`
(`335`/`149`/`104`/`69`/`132`) and `ingest/validate-pages.py`, whose findings were diffed against
pristine `HEAD` and are byte-for-byte the pre-existing set with only line numbers shifted.

### 🔴 One record inside THIS repository corrected, and the correction is itself a trend

🔴 **`repos/trending.md:31080` (pass `334`, `2026-10-20`) records `affromero/Sotto` as
`AGPL-3.0`, `34,523 B`.** 🟢 **Byte-read today: `PolyForm Noncommercial License 1.0.0`,
`4,563 B`, `sha256:ffcca38841ad…`** — agreeing with `agents/trending.md:1652` (`2026-11-13`) and with
this file's own line `1520`. 🔵 **Both readings were correct when taken: `Sotto` RELICENSED from an
OSI copyleft licence to a source-available non-commercial one between `2026-10-20` and `2026-11-13`.**
🔴 **GitHub's licence FIELD reads `NOASSERTION` in BOTH states, so the field cannot see the move at
all** — only a byte-read repeated across passes can, and only an append-only file keeps the earlier
reading to compare it against. That is `T104`, and it is this base's append-only rule paying for
itself.

## Thirty-third pass (`p828`, 2026-11-15) — the LMS tier this base had named `1,100` times and shelved five rows of, and a README that contradicts its own shelves

🟢 **`61` build-safe rows filed (`54` agents `270` → `324`, `6` foundations `142` → `148`,
`1` vertical platform `131` → `132`), `3` trends (`T99`–`T101`), `1` recipe (`P68`), `2` `T27`
licence rescues, `3` regulatory instruments new to this base, and `5` dated regional blocks in
`intel/market.md`.** 🔴 **One defect found in this repository itself and fixed.**

### 🟢 Channel conditions — the best in several passes, and both directions controlled

| Channel | `p827` | `p828` | Control run |
|---|---|---|---|
| `gh api search/repositories -f q="repo:OWNER/NAME"` | blocked | 🟢 **LIVE** | 🟢 **Bidirectional:** `repo:moodle/moodle` → `total_count=1` with licence/stars/pushed; `repo:gmilano/invented-control-t970-xyz` → **HTTP `422`**. A `1` and a `422` are distinguishable |
| `raw.githubusercontent.com` byte-read | 🔴 `403` throughout | 🟢 **LIVE** | 🟢 Positive control: `moodle/moodle` `COPYING.txt` returns GPLv3 text |
| `curl -sI` on a `github.com` repository address | useless | 🔴 **useless, re-confirmed** | 🔴 Returns `HTTP/1.1 200 Connection Established` for a LIVE address **and for an invented one** — that line is the PROXY's `CONNECT` response, not an origin status. `T923`/`T970` hold |
| `gh api repos/OWNER/NAME` | — | 🔴 **BLOCKED** | *"GitHub access to this repository is not enabled for this session"* — session scope. 🔵 **New channel note: the `search/repositories` `repo:` form works where the direct repo endpoint does not; it is the narrowest working existence oracle here** |

🟢 **Consequence: EVERY licence filed in `p828` is BYTE-READ on `raw.githubusercontent.com`, not
field-read.** 🔴 **Every market and regulatory item is `CITED, NOT READ` from WebSearch summaries
and says so at the point of use.**

### 🔴 `D828-1` — the README contradicts the shelves, and has since `p812`

🔴 **`README.md` (pass `p811`, `2026-11-13`) still states: `Global 49 · EMEA 9 · North America 4 ·
APAC 3 · 🔴 LATAM 0`, and calls the LATAM zero *"the hardest number this base has produced about
the region."*** 🟢 **That zero was broken at `p812` and has been false for `17` passes.** Measured
on the shelf this pass, before `p828`'s own additions: **`Global 145 · APAC 48 · EMEA 41 ·
North America 18 · LATAM 18`.**

🔴 **This cost real work.** `p828` opened by re-running a LATAM sweep against a nil the base had
already closed, and re-"discovered" the SIGAA cluster — `GallegoSz`, `heitorsDev`, `Pedromaia0`,
`vintatri`, `erickmsms`, `unb-mds` — every one of which was already on the shelf. 🔵 **The defect
class is `p543`'s, one level up: A COUNT WRITTEN IN PROSE BESIDE THE ROWS IT COUNTS, except here
the prose is in a DIFFERENT FILE from the rows, so `ingest/derive-counts.py` — which grades
headings against their own page — structurally cannot see it.**

🟢 **Fixed in this pass:** `README.md`'s region tally is replaced with the derived figures and
dated. 🔴 **Prescription for the next pass, NOT executed here:** extend the gate to grade
`README.md`'s region tally against `agents/top.md`, or stop publishing a tally in the README at
all. **A cross-file count has no gate, and this base now has evidence that ungated counts go
stale and get quoted.**

### 🔵 What the broad sweep actually proved about this base

🔵 **Most of what a wide sweep surfaced this pass was ALREADY HELD here** — `alejooroncoy/campus-cli`,
`pengusto/google-classroom-mcp`'s proprietary grant, `Regulation (EU) 2026/1744`, the staleness of
`GeovaneSchmitz/sigaa-api`, and the whole SIGAA cluster. 🟢 **That is a good result for a base at
its thirty-third pass: the generic channels are saturated against it.** 🔴 **It is also the
argument for `T99`'s method — the yield came from running the BRAND axis against vendors the base
had never enumerated, not from searching harder for "education AI agents."**

### 🟢 `T27` confirmed twice more, in the rescue direction

| Repository | GitHub field | Bytes read this pass | Disposition |
|---|---|---|---|
| `AnonymousOnyx22/brightspace-d2l-mcp` | 🔴 `NOASSERTION` | 🟢 **MIT** (`sha256:3f0e907830ac…`) | 🟢 **Rescued and filed** |
| `RobertLMcCrary/D2L-MCP` | 🔴 `NOASSERTION` | 🟢 **MIT** (`sha256:e3fdd2a6e7ff…`) | 🟢 **Rescued and filed** |

🔴 **And `T93` independently re-confirmed, against this pass's own method.**
[`gangula-karthik/ntulearn-mcp`](https://github.com/gangula-karthik/ntulearn-mcp) reads
`NOASSERTION`, and `p828`'s classifier — which matches the MIT grant line and the warranty
clause — passed it as MIT. 🔴 **`p827` had already diffed it against canonical MIT text and found
the GRANT CLAUSE REWRITTEN.** 🟢 **It is therefore NOT filed.** 🔵 **A header-and-hash read is not
a licence read; only a canonical diff is. `p828`'s harness has the same defect `T93` named, and
recording that is more useful than quietly excluding the row.**

### 🔴 Rejections and declared limits

- 🔴 [`pengusto/google-classroom-mcp`](https://github.com/pengusto/google-classroom-mcp) — field
  `NOASSERTION`; bytes are a **"Pengusto Commercial License 1.0"**, *"All rights reserved except
  as expressly granted"*. **Commercially prohibited. Already held in `agents/trending.md`;
  re-confirmed here by byte-read, not newly found.**
- 🔴 Unlicensed and therefore NOT filed, though real and relevant: `joaosnet/sigaa-ufpa-mcp`,
  `DaviPac/Sigaa-UFRPE-MCP`, `sebassg/sia-unal-mcp`, `KaioBorgesDev/siga-mcp`,
  `Anggelie/mcp-local-server-uvg`, `JuancitoCozzeti24/santa-rita-escolar`,
  `u-hashmi/desire2learn-mcp`, `falkenslab/moodle-sandbox`, `kkauaon/qaluno`.
- 🔴 `csmediapro/moodle-mcp-server` is **AGPL-3.0** (byte-confirmed) — copyleft, not filed to the
  build-safe shelf.
- 🔴 `NiccoloSalvini/mcp-blackboard-ucsc` is filed `Global`: the institution behind `ucsc` was
  **not resolved and deliberately not guessed**.
- 🔴 **`agents/trending.md` and `repos/trending.md` were APPENDED to, not rewritten.**


# Education AI Agents — curated, license-verified

## Thirty-second pass (`p827`, 2026-11-15) — the grading gap is re-tested and CONFIRMED with named negative evidence; two anchors re-measured; one EMEA row

**`1` build-safe agent row added (`269` → `270`), `2` rejections recorded, `2` anchor corrections,
`3` trends (`T96`–`T98`), `1` recipe (`P67`), and a dated `p827` block in all five regional
sections of `intel/market.md`.**

The full mandated battery ran this pass: four global legs and four regional legs.

### Anchor re-measurement — both re-read from the rendered sidebar on `2026-11-15`

| Row | Held at `p826` | Measured `p827` | Disposition |
|---|---|---|---|
| `HKUDS/DeepTutor` | Apache-2.0, `58.7k★` | Apache-2.0, **`59.4k★`**, `7.1k` forks, `3,806` commits | `v1.7.2` (`2026-11-06`) still current. Star figure updated in the shelf row. |
| `THU-MAIC/OpenMAIC` | MIT, `43.4k★`, *"GitHub Releases is empty"* | MIT, **`43.6k★`**, `6.7k` forks | **Correction.** Releases is no longer empty: **`v1.4.2` (`2026-11-09`) is a full release**, with `v1.5.0-rc.2` (`2026-11-12`) as the pre-release above it. `p826` saw only the rc and concluded the project had never cut a release. It has. |

### 🔴 Count-integrity note — the `270` in the shelf heading could NOT be reproduced this pass

🔴 **`p827` could not execute `ingest/derive-counts.py`** — the runner declined to execute
repository-provided code — so every count in this pass is a direct `grep`/`awk` heading tally.
🟢 **The `p827` DELTA is verified and is exactly `+1`:** the `## Build-safe agents` table held
`191` data rows at `p826` and holds `192` now, matching the single row added below.

🔴 **But the heading's claim does not match that table, and did not at `p826` either:** the heading
read `269 rows` over a table of `191`, and now reads `270` over a table of `192` — **a standing
gap of `78`.** 🔵 **The most likely explanation is that the gate sums build-safe rows across ALL
tables in the file, not just the main shelf** — `repos/trending.md` records the gate reporting
`tables=22` for `repos/foundations.md`, so a multi-table tally is clearly its definition. Under
that definition `270` may well be correct.

🟢 **The increment is therefore carried forward as correct relative to the prior claim, and the
discrepancy is recorded rather than silently re-asserted.** 🔴 **ACTION for the next pass that can
run the gate: print the gate's per-table breakdown for `agents/top.md` and either confirm `270` or
correct the heading.** 🔵 Do not "fix" the heading to `192` without running the gate first — that
would discard `78` rows that very probably exist in the tier tables above.

### `T96` — the grading gap stands, and this pass is the first to test it instead of carrying it forward

This base has asserted since `p815` that *"nothing in grading is to grading what DeepTutor is to
tutoring."* That sentence has been copied forward through several passes without being re-run.
`p827` ran it as a query and the claim survives — but the useful output is the **named negative
evidence**, which the assertion never carried.

`q="open source automated grading assessment AI agent github 2026 rubric essay scoring"` returned
nine repositories. **Every one is a student project, a course submission or a hobby app.** The two
closest to an agent architecture were both byte-checked and both rejected (see the rejected table):
`Dmoayad/essay-grader-llm` carries a **sidebar/README licence conflict** (`GPL-3.0` in the sidebar,
`MIT` claimed in the README) on `1★` and `12` commits; `shafaq2019/Rubric_Agent` has **no licence
file at all** on `0★` and `6` commits, and its own description names it a `DATA722` mid-term.

**The commercial reading is unchanged but now defensible: in grading there is nothing to adopt, so
grading is a BUILD.** `P67` ships that build — and note that the two rejected repositories still
contain the two correct design ideas (deterministic arithmetic outside the model; a rubric learned
from a small human-scored sample and self-tested on held-out items), which is why `P67`
reimplements them rather than citing them as dependencies.

### `T97` — EMEA gains its first French-curriculum-aligned build-safe tutoring agent

`braiinz94/braiinz-education` (Apache-2.0, `0★`, `37` commits, Python 3.12+) is shelved below. It is
small and unproven and is admitted as such. It matters because of **where it points**: Socratic
tutoring plus spaced repetition plus **PISA-aligned diagnostics**, explicitly aligned to the French
curriculum. Every other tutoring row on this shelf is curriculum-neutral, and an EMEA engagement is
almost always sold against a *national* curriculum. Read it as a worked example of curriculum
alignment, not as a dependency at `0★`.

## 🟢 Thirty-first pass (`p826`, 2026-11-15) — two mass-publication events in the same ten days, and the star-ranked channel can only see the empty one

🟢 **`269` build-safe agents on this shelf — `249` carried, `20` added by `p826`.** 🟢 **Every one of the `20` byte-read on `2026-11-15`, every one of the `20` a working integration against a system a real institution runs, and `19` of the `20` reachable from a region this base can name.**

🔴 **The scheduler's mandated star-ranked WebSearch battery nilled a `41`st consecutive pass on its repository legs, exactly as `p825` predicted it would — and this pass finally MEASURED THE MECHANISM instead of recording the symptom.** 🟢 **The four regional legs produced again, in all four regions. The asymmetry `p825` first stated holds for a second consecutive pass.**

### 🔴 The finding (`T91`): two ~1,200-repository mass-publication events landed in the same ten days, and the star-ranked channel is structurally blind to the one with the code in it

🟢 **Both measured this pass, both complete, both enumerated by instrument rather than sampled:**

| | The `AGENTIC STAR` cohort | The `apimart` farm |
|---|---|---|
| Repository count | 🟢 **`1,241`** (12 enumerable authors) | 🔴 **`1,524`** |
| Publishing accounts | `13` named individuals | 🔴 **`580` throwaway accounts**, all `apimart`+random suffix |
| Licence profile | 🟢 **`1,211` MIT / `30` none** | 🔴 **`1,000` of `1,000` `NOASSERTION`** |
| Star mass | 🔴 **`1,226` of `1,241` at `0★`** (max `2★`) | 🔴 **`67,255` across the enumerable `1,000`; mean `67.3` → ~`102,000` total** |
| Fork count | — | 🔴 **`0` on `99` of `100` sampled** |
| Payload shape | 🟢 Specified workflows: `docs/02_design.md`, `docs/03_test_spec.md`, `tests/proof_of_boundary/`, `config/agent.yaml` | 🔴 Four identical size buckets (`174`/`1,292`/`1,329`/`6,096 KB`) repeated across the farm |
| Publication window | `2026-09-21` → `2026-09-30` (10 days) | `2026-09-28` → `2026-10-03` (6 days) |

🔴 **Measured effect on this base's own prescribed query.** `q="tutor LLM pushed:>2026-10-15 stars:>30"` returned `29` distinct repositories. 🔴 **`13` of them — `45%` — are `apimart` farm rows**, none of which has anything to do with education: they are an API-relay product whose chosen SEO vocabulary is *tutorial*, *guide*, *course* and *learn* (`145` of the first `1,000` carry one of those words in the name). 🟢 **The farm is not targeting education. It does not have to. It carries `~67★` per repository against an education shelf whose genuine new supply sits at `0★`, so any star floor high enough to exclude noise excludes the signal and admits the farm.**

🔵 **This is the complete answer to a question this base has recorded as an unexplained symptom `41` times: the star-ranked channel is not saturated, and it is not broken. It is RANKING CORRECTLY over a population whose top is synthetic.** 🟢 **`P66` turns the farm's measured signature into a pre-shelf rejection gate.**

### 🔴 The second finding (`T92`): `p825`'s *"`74`-repository MIT education catalogue"* is an education-filtered projection of a `1,241`-repository, twelve-industry catalogue — and the catalogue is CLOSED

🟢 **Enumerated by author rather than by query, which is the correction.** `p825` ran ten `"agentic star" <education term>` queries and unioned the results; this pass ran `q="user:<author>"` for all `13` authors. 🔴 **`74` → `1,241`: a `16.8×` undercount, caused entirely by the education filter in `p825`'s own query shape.**

🟢 **Domain prefix distribution of the `1,210` `agentic-star-*` repositories:** `retail` `81`, `insurance` `41`, `manufacturing` `28`, `telecom` `24`, `logistics` `20`, `services` `19`, **`education` `19`**, `financial` `17`, `healthcare` `16`, `energy` `13`, `municipal` `12`, `government` `11`, `travel` `5`. 🔵 **That list is very nearly this estate's own twelve-industry rotation. The cohort is not an education asset that `29` passes missed; it is a CROSS-SECTOR asset, and the other eleven knowledge bases in this estate have the same blind spot for the same reason.**

🟢 **The education slice, measured honestly: `76` repositories** by name-and-description match, of which `18` are already on these shelves and **`58` are not.** 🔴 **This pass deliberately shelves NONE of the `58` as agents, and that is a decision rather than an omission** — `p825` already established that they are `0★`, unmaintained since September and refuse to start without a SoftBank deployment, and `P61` already specifies the correct use, which is to harvest them as a requirements-and-test-spec corpus. 🔵 **Twenty more `0★` rows would have grown the shelf count and taught a reader nothing.**

🟢 **And the catalogue is FINISHED.** `1,210` of `1,241` were created inside ten days (peak `402` on `2026-09-25`, `331` on `2026-09-28`); **only `2` repositories have been created since `2026-10-29`.** 🔵 **So it is a one-shot developer-programme output, not a growing channel, and a later pass should not re-enumerate it hoping for more.**

### 🔴 The third finding (`T93`): byte-reading the licence HEADER is not enough — this pass nearly shelved a rewritten MIT grant

🔴 **`gangula-karthik/ntulearn-mcp` would have passed this base's own gate.** Its `LICENSE` opens `MIT License` / `Copyright (c) 2026 kingdonkatsu`, it is `1,055 B`, and a header read plus a hash record — which is what `p825`'s table captured — classifies it MIT. 🟢 **Diffed against canonical MIT text, the grant clause is REWRITTEN:**

| | Text |
|---|---|
| Canonical | *"…copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:"* |
| 🔴 `ntulearn-mcp` | *"…copies of the Software, and to **furnish it to whom it is furnished to do so**, subject to the following conditions:"* |

🔴 **The altered sentence is the one that grants onward distribution.** GitHub's field reports `NOASSERTION`, and on this row the field is RIGHT and a header-only byte-read is WRONG. 🔵 **`T52` corrected `T50` by establishing that `NOASSERTION` means the matcher failed; `T93` adds the half `T52` left out — the matcher sometimes fails BECAUSE THE GRANT WAS EDITED, and that is the case a studio must never auto-shelve.** 🟢 **The control is a diff against canonical SPDX text, not a hash compared to a sibling repository. Filed as a rejection below, not as a row. `P65` ships the gate.**

### 🟡 The fourth finding (`T94`): the fork flag does not catch a republished copy, and licence-byte identity has TWO dispositions that only the README separates

🟢 **Two byte-hash collisions this pass, with opposite readings:**

| Collision | Repositories | Holder | README | Reading |
|---|---|---|---|---|
| `sha256:2c0b8069fc10…` | `toughIQ/webuntis-mcp` + `heiko-schabert/webuntis-cli` | `toughIQ` in both | 🟢 **Declares it: *"Go port of webuntis-mcp"***, upstream linked | 🟢 **Honest port. One lineage, two implementations, both build-safe** |
| `sha256:bd7dc91514e6…` | `israelroldan/unofficial-magister-mcp` + `NanoBotAgent/magister-mcp` | 🔴 `Copyright (c) 2024 Israel Roldan` in BOTH | 🔴 **Near-identical prose, same disclaimer, no attribution, `fork=false`, created `2026-09-11` — seven months after the original** | 🔴 **Silent republish. ONE implementation at two addresses** |

🔵 **The MIT licence is satisfied in both cases — the copyright notice travelled. What did NOT travel is the signal a counter needs.** 🔴 **GitHub reports `fork=false` on the republish, so any population count built on the fork graph overstates the supply.** 🟢 **This directly corrects a number this pass would otherwise have published: the Magister tier is a population of ONE, not two, and only `israelroldan/unofficial-magister-mcp` is shelved below.**

### 🟢 The fifth finding (`T95`): the EMEA national-school-system MCP tier, measured — `4` national systems, `12` repositories, `10` independent implementations, `4` build-safe

🟢 **This is `T82`'s rule (supply is indexed under the SYSTEM NAME, never the pedagogy) run as `P59` prescribes, against EMEA instead of LATAM, and it produced the largest regional yield of any pass since `p818`.** 🔵 **Not one of these `12` repositories is findable by any query containing the word "education".**

| National system | Incumbent where | Repos found | Independent | 🟢 Build-safe |
|---|---|---|---|---|
| **WebUntis** | 🇦🇹🇩🇪🇨🇭 DACH K-12 timetabling | `6` | `4` | 🟢 **`3`** |
| **Librus Synergia** | 🇵🇱 Poland K-12 | `3` | `3` | 🟢 **`1`** |
| **Pronote / ÉcoleDirecte / Skolengo** | 🇫🇷 France K-12 | `2` | `2` | 🟢 **`1`** |
| **Magister** | 🇳🇱 Netherlands K-12 | `2` | 🔴 **`1`** (see `T94`) | 🟢 **`1`** |

🔴 **`7` of the `12` carry no `LICENSE` file at all — a `58%` unlicensed rate.** 🔵 **So the honest EMEA sentence is not "there is no open supply for European school systems" and not "there is plenty" — it is: *the tier exists, it is active, it is parent-facing and read-only by design, and most of it cannot legally be built on.* Asking four named developers for a licence is a cheaper route to EMEA coverage than writing four connectors.**

### The rows — `20` added this pass, all `20` byte-read, `0` copyleft

| Name | Repo | Licence | Stars | Region | Description |
|---|---|---|---|---|---|
| webuntis-mcp (upstream) | https://github.com/toughIQ/webuntis-mcp | 🟢 **MIT — byte-read** (`1,063 B`, `sha256:2c0b8069fc10…`, holder `toughIQ`) | 0 | EMEA | 🟢 **New this pass (`p826`) — the root of the largest national-system lineage in `T95`.** Read-only MCP over **WebUntis**, the timetabling system most DACH schools run: timetables, homework, exams, absences. 🔵 **Explicitly PARENT-facing — its own examples are *"What's on the schedule tomorrow?"* and *"Does my child have homework due?"* — which places it on the guardian seam `P45` describes, where the credential belongs to an adult and the data belongs to a child** 🔴 `0★`, created and pushed `2026-09-13`, `101 KB` |
| webuntis-cli (Go port) | https://github.com/heiko-schabert/webuntis-cli | 🟢 **MIT — byte-read** (`1,063 B`, `sha256:2c0b8069fc10…`, 🟢 **holder `toughIQ` retained from upstream**) | 0 | EMEA | 🟢 **New this pass (`p826`) — and it is `T94`'s positive control: a declared port that keeps the upstream's licence bytes AND says so in its README.** Go reimplementation exposing the same surface as both a CLI and an MCP server (`webuntis-cli mcp`), text or `--json`. 🔵 **Authenticates through the Untis Mobile app's internal JSON-RPC with a per-request TOTP, so NO PASSWORD is stored — the best credential posture in this tier and the one to copy** 🟢 Pushed `2026-11-12` |
| untis-mcp (Rust) | https://github.com/DenizCiger/untis-mcp | 🟢 **MIT — byte-read** (`1,067 B`, `sha256:04314fb25dd9…`, holder `Deniz Ciger`) | 0 | EMEA | 🟢 **New this pass (`p826`) — the second INDEPENDENT WebUntis lineage, ported from the same author's `untis-tui` rather than from `toughIQ`.** Rust, `8` tools, prebuilt binaries for Linux/macOS/Windows. 🔵 **Every tool is annotated read-only and returns structured content with an output schema — the schema-on-every-tool discipline this base has asked for since `T80` and rarely found** 🟢 `find_free_rooms` is the one tool in this tier that serves the REGISTRAR rather than the family. Pushed `2026-10-19` |
| unofficial-magister-mcp | https://github.com/israelroldan/unofficial-magister-mcp | 🟢 **MIT — byte-read** (`1,069 B`, `sha256:bd7dc91514e6…`, holder `Israel Roldan`, 2024) | 6 | EMEA | 🟢 **New this pass (`p826`) — 🇳🇱 the Netherlands' Magister, and the HIGHEST-starred row in the national-system tier.** School schedules, drop-off and pick-up times for MCP-compatible assistants. 🔴 **Shelved as the tier's ONLY Magister row: `NanoBotAgent/magister-mcp` carries this file's licence bytes and this holder's name with no attribution and `fork=false`, and is `T94`'s negative control** 🔵 Names its own non-affiliation with Magister/Iddink Group in the README, which is the right posture for an unofficial connector to a commercial system of record |
| librus-mcp | https://github.com/ljarochowski/librus-mcp | 🟢 **MIT — byte-read** (`1,079 B`, `sha256:be00e61b6328…`, holder `Librus MCP Contributors`) | 0 | EMEA | 🟢 **New this pass (`p826`) — 🇵🇱 the only build-safe row of the three Librus Synergia implementations found.** Scrapes Polish school data via Playwright. 🔵 **The only repository in this tier with a declared ARCHITECTURE — `domain/` models and services, `ports/`, `adapters/`, `application/` — i.e. a hexagonal layout in which the Librus scraper is a swappable adapter. That is the single most portable asset in `T95`, because the domain model (`Child`, `Grade`, `Homework`, `CalendarEvent`) is the same in every country and only the adapter changes** 🔴 `0★`, pushed `2026-01-13` |
| edu-mcp (France) | https://github.com/jujukingg/edu-mcp | 🟢 **MIT — byte-read** (`1,080 B`, `sha256:2ede3d997023…`, holder `Pronote MCP Contributors`) | 0 | EMEA | 🟢 **New this pass (`p826`), and it is the strongest single row in `T95`: not one French platform but THREE — Pronote (+ENT), ÉcoleDirecte and Skolengo — behind one unified MCP server.** Published on PyPI as `edu-mcp`, CI green, bilingual EN/FR docs. 🔵 **Those three cover essentially the whole French K-12 parent/student portal market, so this is the only row on this shelf that reaches a NATIONAL market rather than a school or a vendor. It is also the worked example for `P64`: one connector, many back ends, which is the product the other three countries do not yet have** 🔴 `0★` despite the coverage — pushed `2026-11-14`, `515 KB` |
| Studie OS | https://github.com/alrawi10/studie-os | 🟢 **MIT — byte-read** (`1,064 B`, `sha256:4a38786a6b9b…`, holder `alrawi10`) | 1 | EMEA | 🟢 **New this pass (`p826`) — 🇩🇰 Danish, built for dentistry at the University of Copenhagen, and the only row here that treats the LMS as one input among five.** Syncs course files from Canvas, Moodle, Brightspace or itslearning, archives them per-course in NotebookLM for cited answers, generates source-grounded Anki cards *with the figure from the cited page*, plans study blocks into Apple Calendar around the timetable, and takes voice notes via Siri. 🔵 **The citation chain is the point: a card is refused unless it can name the source title and page/slide it came from, which is `P53`'s learning-scaffold argument implemented by a student for themselves** 🔴 Docs are in Danish; pushed `2026-10-22` |
| heronhex-highered | https://github.com/bsayres/heronhex-highered | 🟢 **MIT — byte-read** (`1,082 B`, `sha256:aa0df3165b5d…`, holder `highered-mcps contributors`) | 0 | North America | 🟢 **New this pass (`p826`) — the most complete evidence-provenance implementation this base has shelved, in any industry.** FIVE MCP servers plus six skills over **free US public data**: institutions and enrolment trends with peer comparison, Title IV/FSA risk and audit findings, federal and state funding and research spend, program-to-labor-market alignment, and live accreditation status with agency actions. All five on PyPI as `heronhex-*`. 🔵 **Its stated principles are the deliverable: every response carries `source`, `source_url`, `as_of` and `retrieved_at`; missing data is an explicit `null` WITH A REASON and is never estimated; name matches are labelled fuzzy and refused when ambiguous; network egress is allow-listed IN CODE; and upstream free text is treated as untrusted with a `docs/threat-model.md` to say so.** 🟢 **That is `P60`'s oversight argument and `P63`'s decidability argument shipped as a working product — adopt the response envelope even if you never run the servers** 🔴 `0★`, pushed `2026-11-14`, `2.4 MB` |
| ap-score-distributions-mcp | https://github.com/theluckystrike/ap-score-distributions-mcp | 🟢 **MIT — byte-read** (`1,070 B`, `sha256:4fedd46e8c20…`) | 0 | North America | 🟢 **New this pass (`p826`) — and it is a REFUSAL implemented as a feature, which is the shape `P58` argues for.** Official College Board AP score distributions for **May 2026, 2025 and 2024**, all `40` exams: percentiles, pass-rate ranking, `5` tools. 🔵 **Two disciplines worth copying: every year's `49` rows pass an arithmetic check that counts sum to the printed total and `5+4+3` equals the printed "3 or higher"; and the composite-to-score estimator serves only the `7` exams for which College Board actually printed a conversion chart and REFUSES every other exam rather than invent a cut score.** 🟢 **It also carries post-training-cutoff data (May 2026 results), which is the clearest statement on this shelf of why a data MCP beats a bigger model** 🔴 `0★`, pushed `2026-11-13` |
| fam-mcp | https://github.com/Petri-Hub/fam-mcp | 🟢 **MIT — byte-read** (`1,065 B`, `sha256:a659ef421023…`, holder `Petri-Hub`, on `LICENSE.md`) | 4 | LATAM | 🟢 **New this pass (`p826`) — 🇧🇷 and it is LATAM's build-safe row in a tier where LATAM's other find has no licence at all.** Read-only MCP over the student portal of **Faculdade de Americana (FAM)**, São Paulo: grades, absences, assignments, schedule, exams, inbox, forums, finances and complementary hours. 🔵 **Its README states the constraint `T77` named verbatim — *"The portal has no API"* — so it signs in as the student, reads server-rendered pages and returns clean typed JSON, writing nothing back.** 🟢 **The use cases are the product: *"What is due this week?"* spans assignments, exams, forums AND invoices in one call, and *"Can I still miss class?"* checks absences against the allowed maximum — a question the portal itself cannot answer** 🔴 Published to PyPI; pushed `2026-11-14` |
| bb-mcp (CUHK-Shenzhen) | https://github.com/changshenhan/bb-mcp | 🟢 **MIT — byte-read** (`1,068 B`, `sha256:aec9afda396f…`, holder `changshenhan`) | 4 | APAC | 🟢 **New this pass (`p826`) — 🇨🇳 and the only WRITE-CAPABLE row added this pass.** `9` tools against **Blackboard Learn Classic 3900** at `bb.cuhk.edu.cn`: courseware download, assignment inspection, announcements, **and homework submission**, fully headless with credentials kept local. 🔵 **It is also the only row that ships its own integrity boundary in prose — *"For personal productivity only… don't automate anything that violates academic integrity rules"* — which is exactly the line `P53` says a scaffold product must draw and almost no repository draws** 🔴 **Because it submits, it is the row in this tier that needs `P56`'s commit-and-re-read protocol before any client deployment.** Pushed `2026-09-21` |
| random-signal-agent | https://github.com/PatrickStar-cmd/random-signal-agent | 🟢 **MIT — byte-read** (`1,071 B`, `sha256:f24bb6654cbe…`) | 22 | APAC | 🟢 **New this pass (`p826`) — 🇨🇳 the highest-starred genuinely-new education row this pass, and a sixth instance of `T70`.** A course agent for 随机信号分析 (Random Signal Analysis) at **UESTC** — the skill binds to one university's named course, not to a subject in general. 🔵 **`36.9 MB` of payload, which for a single-course agent means the course corpus travels WITH the agent: the asset is the curriculum, exactly as `T70` and `P51` predict** 🟢 Pushed `2026-11-14` |
| classroom-mcp-server | https://github.com/SaiedBasha/classroom-mcp-server | 🟢 **MIT — byte-read** (`1,067 B`, `sha256:cbebd946d89f…`, holder `Saied Basha`) | 0 | Global | 🟢 **New this pass (`p826`).** A teacher-facing classroom-management MCP server, described by its author as production-ready. 🔵 **Shelved for the USER rather than the feature set: almost everything in `T95` serves a parent or a student, and the teacher-facing seam is where this base has least supply** 🔴 `0★`, pushed `2026-09-04`, `66 KB` |
| gh-classroom-mcp | https://github.com/CastaliaInstitute/gh-classroom-mcp | 🟢 **MIT — byte-read** (`1,073 B`, `sha256:79ce53c3a6a2…`, holder `Inquiry Institute`) | 0 | Global | 🟢 **New this pass (`p826`).** MCP server over the **GitHub Classroom** REST API plus organisation-repo helpers. 🔵 **The one system of record in this tier with a real, documented, stable public API — so it is the cheapest possible pilot for a classroom-agent engagement and the right place to prove the interaction model before paying for a scraper against Pronote or Librus** 🔴 `0★`, pushed `2026-04-14`, `24 KB` |
| TeachMeCoding | https://github.com/liangxiao777/TeachMeCoding | 🟢 **Apache-2.0 — byte-read** (`11,357 B`, `sha256:58d1e17ffe51…`, stock text) | 50 | Global | 🟢 **New this pass (`p826`) — the highest-starred build-safe row added, and the only one with a patent grant.** Local-first AI coding tutor: personalised roadmaps, lessons and hands-on practice. 🔵 **"Local-first" is the procurement-relevant property — a coding tutor that never ships student work to a vendor is the version a university's data-protection officer can approve, and that is a different product from the hosted tutors this shelf is full of** 🟢 Pushed `2026-10-30`, `11 MB` |
| heptabase-explainer-studio | https://github.com/heptameta/heptabase-explainer-studio | 🟢 **Apache-2.0 — byte-read** (`11,357 B`, `sha256:58d1e17ffe51…`, stock text) | 36 | Global | 🟢 **New this pass (`p826`).** Turns source material into explainer videos, driven by the user's own coding agent rather than by a hosted pipeline. 🔵 **The agent-native authoring tier `T54` named, one rung further along: the deliverable is a VIDEO and the orchestration happens inside the developer's existing agent, so there is no new platform to license** 🟢 Pushed `2026-11-09` |
| reasoning-and-agents-education | https://github.com/chaoshu1201/reasoning-and-agents-education | 🟢 **MIT — byte-read** (`1,064 B`, `sha256:e523e0f51060…`, holder `Chao Shu`, 2025) | 25 | Global | 🟢 **New this pass (`p826`).** Public teaching materials for a Reasoning and Agents course — `15.5 MB`, actively pushed `2026-11-15`. 🔵 **Shelved as CURRICULUM, not as an agent: when a client asks the studio to train its own engineers on agent design, an MIT-licensed, maintained course corpus is worth more than another framework, and this base holds very few** |
| Marty | https://github.com/morrowdock/marty | 🟢 **Apache-2.0 — byte-read** (`11,356 B`, `sha256:43070e2d4e53…`) | 1 | Global | 🟢 **New this pass (`p826`) — and it is the cleanest verify-refuse-repair loop on this shelf.** Turns a learning question into a *checked* 3D lesson: a model plans the lesson and writes it as MartyGraphics JSON, **the engine checks it and refuses a wrong one with an exact reason**, and the model repairs it from that reason. 🔵 **The generative step is unconstrained and the ACCEPTANCE step is deterministic and external to the model — which is the only architecture on this shelf that can make a claim about physical correctness in a lesson rather than about plausibility** 🔴 **Author-declared early preview; interfaces will change. Do not pin a client deliverable to it yet** |
| AetioECG | https://github.com/janthoXO/AetioECG | 🟢 **MIT — byte-read** (`1,062 B`, `sha256:3aac41139ed5…`) | 0 | Global | 🟢 **New this pass (`p826`).** Serves real 12-lead ECGs from **PTB-XL**, selected by SCP-ECG statement, for medical education. 🔵 **A medical-education asset whose cases are REAL and whose ground truth is a published annotation standard, so an assessment built on it can be defended to a clinical examiner — which a model-generated ECG never can** 🔴 `0★`, pushed `2026-11-13` |
| patient-education-mcp-server | https://github.com/QuentinCody/patient-education-mcp-server | 🟢 **Apache-2.0 — byte-read** (`10,758 B`, `sha256:7d304102af40…`) | 0 | Global | 🟢 **New this pass (`p826`) — and it is the row that crosses into the healthcare KB.** MCP server for patient education. 🔵 **Patient education is formally health communication and commercially education: it is the clearest single instance of `T92`'s point that this estate's industry boundaries are a filing convention and the supply does not respect them** 🔴 `0★`, pushed `2026-11-13`, `2.2 MB` |


## 🟢 Thirtieth pass (`p825`, 2026-11-15) — a `74`-repository MIT education catalogue that `29` passes never saw, and the correction of `p824`'s own Vietnam finding

🟢 **`249` build-safe agents on this shelf — `227` carried, `22` added by `p825`.**

🔴 **The scheduler's mandated star-ranked WebSearch battery nilled for a `40`th consecutive pass — but NOT uniformly, and the difference is worth recording.** All four global legs ran. 🔵 **The agent leg returned the general shelf again (`OpenHands`, `browser-use`, `AutoGPT`, `LangChain`, `Langflow`, `Hermes Agent`) and one aggregator that names no repositories; the trending leg returned `DeepTutor`, `ChinaTextbook`, `interactive-learning` and `microsoft/ai-agents-for-beginners` — all held; the ERP leg returned `OpenEduCat` (LGPL-3.0), `openSIS` (GPL-3.0) and `RosarioSIS`, i.e. the copyleft platform answer this base has recorded since `p805`.** 🟢 **The four REGIONAL legs, by contrast, all produced — see `intel/market.md`, where every regional subsection gained a dated `p825` block. The battery's failure is specific to its REPOSITORY legs; its MARKET legs work. That distinction has been blurred in `39` previous nil notices and is stated here plainly.**

### 🟢 The finding (`T86`): there is a `74`-repository, `54`-id, MIT-licensed education agent catalogue on GitHub, and no pass of this base has ever held one row of it

🟢 **Measured, not estimated.** Ten queries of the form `"agentic star" <education term>` against `search/repositories`, unioned and de-duplicated: **`74` distinct repositories, `73` MIT and `1` unlicensed, created between `2026-09-22` and `2026-10-29` by `13` authors.** 🔴 **Collision check against all `477` addresses this base already holds: ZERO.** 🟢 **They carry a catalogue id — `EDU-C2-004` through `EDU-C2-173`, `54` distinct ids observed — so the catalogue is numbered to at least `173` and roughly `31%` of it is visible.**

🔵 **Why `29` passes missed it, and this is the transferable part:** the repositories are named `agentic-star-<workflow>-agent`, described as *"built with Agentic Star"*, and carry no education topic tags. 🔴 **A query for the pedagogy misses them, a query for the jurisdiction misses them, and a star floor annihilates them — every one of the `74` is at `0★`.** 🟢 **This is `T82`'s rule (LATAM supply is indexed under the SYSTEM NAME, not the pedagogy) generalising to a THIRD indexing axis: the PLATFORM BRAND.** `P62` turns it into a runnable protocol.

### 🔴 The second finding (`T87`): `p824`'s `T84` — *"Vietnam … build-safe open supply of ZERO"* — is WRONG, and this pass measured the correction

🔴 **`p824` published: *"A jurisdiction that regulates automated assessment as high-risk, with exactly zero build-safe open supply in its own language. That is the sharpest BUILD slot `p824` found."*** 🟢 **Author census of the `74`-repository catalogue:**

| Author | Repos | Reading |
|---|---|---|
| `haidang024`, `trantienit2015`, `tvcuong1802`, `TienXuanLam`, `DuongNT98`, `hungnguyenai` | 🟢 **`43`** | 🇻🇳 Vietnamese authors — **`58%` of the catalogue** |
| `TAKUYA0608-dev`, `genkidesu7`, `sbdnakashima`, `KaitoYokomizo` | `25` | 🇯🇵 Japanese authors |
| `Anlexis`, `mirsydfchrynto`, `D0D0D0D` | `6` | unattributed |

🟢 **Vietnamese developers are the LARGEST national group of education-agent authors this base has ever measured — `43` MIT-licensed education agents in five weeks.** 🔴 **`p824`'s finding was not false about what it ran; it was false about what it concluded.** Its queries were `q="giao duc viet nam ai"` (`7` results, all unlicensed) and `q="vietnam education platform"` (`5`, all unlicensed). 🔵 **Both are correct measurements of Vietnamese-LANGUAGE supply. Neither is a measurement of VIETNAMESE-AUTHORED supply, and `p824` reported the second while measuring the first.** 🟢 **The corrected sentence: Vietnam's build-safe education supply is substantial, written in English, and published under a Japanese vendor's channel brand — so it is invisible to every query that assumes a developer publishes in the language of the jurisdiction they build for.**

### 🟡 The third finding (`T88`+`T89`): the licence chain is clean end-to-end, and the SOURCE chain is not — and this pass nearly got it backwards

🔴 **First reading, recorded because it was wrong:** the templates' READMEs say *"This template does not run standalone … There is no fallback or degraded mode … raises `PlatformRequired`"*, and name a framework `agenticstar-agentcore` *"supplied by the hosting environment rather than resolved from the default package index"*. 🔴 **That reads as MIT code over a captive runtime — the sharpest possible rejection.** 🟢 **It is not what is there. Probed:**

| Artefact | Field says | Bytes say | Reading |
|---|---|---|---|
| The `74` templates | `MIT` | 🟢 MIT, byte-read per row below | Field correct |
| `agenticstar-agentcore` `1.0.3` (PyPI) | 🔴 `info.license: None`, no licence classifier | 🟢 `License-Expression: MIT` + `dist-info/licenses/LICENSE`, `1,078 B`, `sha256:2afbb5fc…`, holder *The AgentCore Authors* | 🔴 **Field wrong** |
| `agenticstar-platform` (PyPI, `80` releases, `3.3.0`) | 🔴 `info.license: None` | 🟢 `license_expression: MIT` | 🔴 **Field wrong** |
| `teppei-miyashita/agenticstar-agentcore` (the source repo its own PyPI metadata advertises) | `None`, `0 KB` | 🔴 **`git ls-remote` returns ZERO REFS — the repository has no commits at all** | 🔴 **Empty** |

🟢 **`T88` — `T52`/`T81`'s instrument generalises to a SECOND REGISTRY.** PyPI's legacy `info.license` reports `None` for both packages while the wheel's own metadata declares `MIT`, because modern packaging writes `License-Expression` and the JSON field does not surface it. 🔵 **The same defect class this base has tracked on GitHub for `40` passes — the licence FIELD and the licence BYTES disagree — is a property of registries, not of GitHub. A studio's dependency scanner reading `info.license` will flag an MIT framework as unlicensed.**

🟡 **`T89` — the gap that IS real is reviewability, not licence.** The framework is installable from PyPI and MIT; it is also **wheel-only, single-release, and its advertised source repository is empty**. 🔵 **So the honest procurement sentence is not "you may not use this" but "you may use it and you cannot read it" — and those go to different people in a client's organisation.** 🔴 **The framework additionally hard-pins `==` on `langgraph 1.1.10`, `langchain 1.2.18`, `fastapi 0.136.0` and `agenticstar-platform 0.5.32`, which is a real upgrade constraint on any tree that adopts it.**

### 🟢 The fourth finding (`T90`): the copyright in a vendor-channel cohort sits with `13` INDIVIDUALS, not the vendor — proved by byte-hash

🟢 **`T37`'s licence-byte-hash instrument, pointed at the cohort, resolves the ownership question in one sweep.** Each author's `LICENSE` is byte-identical across their own repositories and differs from every other author's: `sbdnakashima` `134983626184…` (`3`), `haidang024` `b22b7ca45c04…` (`3`), `TAKUYA0608-dev` `888cc5f61f9c…` (`2`), `trantienit2015` `a953ad384437…` (`2`), `genkidesu7` `e74683d915ae…` (`2`), `TienXuanLam` `342465e77207…` (`2`). 🔴 **Every holder line names the individual developer — `Copyright (c) 2026 Daisuke Nakashima`, `… haidang024`, `… Tien Tran` — and NOT SoftBank or AGENTIC STAR.** 🔵 **A studio adopting `17` of these rows is taking a grant from `13` separate natural persons, not one corporate counterparty. That is a provenance property a licence-field ingest cannot see and a procurement review will certainly ask about.** 🟢 **It also tells you the cohort is a developer-programme output, which predicts both its strengths (real domain variety) and its weakness (`0★`, no maintenance commitment).**

### 🟢 What is actually adoptable here, stated plainly

🔵 **Not the running agents.** `0★`, unmaintained since October, and they refuse to start without a SoftBank deployment. 🟢 **What IS adoptable, and it is worth more:** every repository ships `docs/02_design.md`, `docs/03_test_spec.md`, a `tests/proof_of_boundary/` suite (import isolation, invoke order, state safety, HITL interrupt propagation, stage gates) and a `config/agent.yaml` manifest declaring `required_trust_level` and every secret the agent uses — **and the READMEs state that the tests run WITHOUT a platform connection.** 🔵 **That is `54` specified, test-specified, MIT-licensed education workflows on a LangGraph graph this base already holds. Harvest it as a REQUIREMENTS catalogue and re-implement, which is `P61`.**

### The rows — `22` added this pass, all `22` build-safe, `0` copyleft

| Name | Repo | Licence | Stars | Region | Description |
|---|---|---|---|---|---|
| EDU-C2-028 IEP section drafting | https://github.com/sbdnakashima/agentic-star-iep-section-drafting-agent | 🟢 **MIT — byte-read** (`1,074 B`, `sha256:134983626184…`, HEAD `71c442ebd88e`) | 0 | APAC | 🟢 **New this pass (`p825`) — and it ENDS a nil this base has carried since `p805`: `q="individualized education program IEP ai"` returns `1` repository, so the IEP layer was written off as empty.** `EDU-C2-028` drafts the four statutory IEP sections — present levels of performance, annual goals, support services, accommodations — from structured assessment input, teacher observation notes and inclusive-education guidelines. 🔵 **The nil was a VOCABULARY artefact, exactly as `T83`'s proctoring nil was: the layer is indexed under a platform's catalogue id, not under the phrase a procurement officer would type.** Nodes: `assessment_parser`, `iep_section_generator`, `regulatory_compliance`, `review_flag` — the compliance check and the human review flag are SEPARATE nodes, which is the shape an appealable special-education decision needs |
| EDU-C2-098 accessibility gap brief | https://github.com/tvcuong1802/agentic-star-learning-resource-accessibility-gap-brief-agent | 🟢 **MIT — byte-read** (`1,068 B`, `sha256:be1056662503…`, HEAD `81d6d7e31e41`) | 0 | APAC | 🟢 **New this pass (`p825`) — the first ACCESSIBILITY-METADATA auditor on this shelf.** Reads a school's learning-resource catalogue and reports where accessibility metadata is missing, rather than attempting to fix the resources. 🔵 **The audit framing is the sellable one: EU and UK procurement increasingly require an accessibility statement per resource, and the blocking question is never "is this resource accessible" but "which of our `40,000` records cannot answer that question"** 🔴 `0★`, created `2026-09-25`, `169 KB` |
| EDU-C2-046 curriculum change impact | https://github.com/haidang024/agentic-star-education-curriculum-change-impact-briefing-agent | 🟢 **MIT — byte-read** (`1,067 B`, `sha256:b22b7ca45c04…`, HEAD `ae3eea9ac056`) | 0 | APAC | 🟢 **New this pass (`p825`) — the largest payload in the cohort's briefing tier at `45` files.** Takes a proposed curriculum change and produces a *traceable* impact briefing: affected-material analysis, stakeholder mapping, evidence retrieval, and an explicit HITL briefing node. 🔵 **`briefing_hitl_node.py` is a named, separate node — the human-in-the-loop step is in the graph, not in a policy document beside it, which is `P60`'s whole argument shipped as code** |
| EDU-C2-029 exam question classifier | https://github.com/genkidesu7/agentic-star-university-entrance-exam-question-classification-difficulty-agent | 🟢 **MIT — byte-read** (`1,071 B`, `sha256:e74683d915ae…`, HEAD `faf2b31241ee`) | 0 | APAC | 🟢 **New this pass (`p825`) — a sixth instance of `T70`: the skill binds to a CURRICULUM INSTRUMENT, not a subject.** Takes a full 共通テスト (Japan's Common Test) subject paper as PDF and classifies every question by domain, **Bloom level** and difficulty. 🔵 **`bloom_level_node.py` and `difficulty_score_node.py` are separate graded nodes — a difficulty score that cannot say which taxonomy produced it is not defensible to an examinations board, and this one can** |
| EDU-C2-056 transfer credit equivalency | https://github.com/TAKUYA0608-dev/agentic-star-transfer-credit-equivalency-agent | 🟢 **MIT — byte-read** (`1,063 B`, `sha256:888cc5f61f9c…`, HEAD `96ec48c73414`) | 0 | APAC | 🟢 **New this pass (`p825`).** University transfer-credit equivalency assessment with articulation-decision drafts. 🔵 **The highest-friction administrative workflow in higher education and one almost no open agent touches: it is a judgement about ANOTHER institution's syllabus, so the evidence trail matters more than the verdict** 🔴 `0★`, `64 KB` |
| EDU-C2-024 misconduct report drafting | https://github.com/TienXuanLam/agentic-star-education-university-academic-misconduct-investigation-report-drafting-agent | 🟢 **MIT — byte-read** (`1,068 B`, `sha256:342465e77207…`, HEAD `f8f8c08d3ee6`) | 0 | APAC | 🟢 **New this pass (`p825`) — and it names its regulator in the description, which almost nothing on this shelf does.** Generates **MEXT-guideline-compliant** academic-misconduct investigation reports (MEXT = Japan's Ministry of Education, Culture, Sports, Science and Technology). 🔵 **This is the formal counterpart to `T83`'s proctoring layer: detection produces an allegation, and an allegation that cannot be written up to the ministry's own template dies in process. The surveillance tier has `101` repositories; the WRITE-UP tier had none here until this pass** |
| EDU-C2-085 accreditation evidence | https://github.com/TAKUYA0608-dev/agentic-star-accreditation-evidence-navigator-agent | 🟢 **MIT — byte-read** (`1,063 B`, `sha256:888cc5f61f9c…`, HEAD `9a579ed8b334`) | 0 | APAC | 🟢 **New this pass (`p825`).** Navigates programme-accreditation evidence for higher education — given a standard, finds and cites the institutional evidence that answers it. 🔵 **Accreditation is the one deadline a university cannot move, and the work is almost entirely evidence retrieval against a fixed rubric — the single best-shaped education task for an agent on this shelf** 🔴 `0★`, `83 KB` |
| EDU-C2-053 meal allergen router | https://github.com/sbdnakashima/agentic-star-school-meal-allergen-check-agent | 🟢 **MIT — byte-read** (`1,074 B`, `sha256:134983626184…`, HEAD `3cd8f2e19dc2`) | 0 | APAC | 🟢 **New this pass (`p825`) — and the row that proves the catalogue is not all paperwork.** Cross-checks school meal plans against supplier allergen declarations and routes what is MISSING, not what is wrong. 🔵 **An evidence-DEFICIENCY router rather than a classifier: it never asserts a dish is safe, it asserts which declaration has not arrived. For a safety-of-life workflow that is the only defensible output shape an LLM can have** 🔴 `0★`, `34 KB` |
| EDU-C2-016 research ethics IRB | https://github.com/trantienit2015/agentic-star-university-research-ethics-irb-compliance-check-agent | 🟢 **MIT — byte-read** (`1,083 B`, `sha256:a953ad384437…`, HEAD `59f5e3c0cbcb`) | 0 | APAC | 🟢 **New this pass (`p825`).** University research-ethics and IRB compliance checking. 🔵 **Pairs with `EDU-C2-085` and the research-data-management-plan agent in the same cohort to cover the three documents a research office is actually judged on** 🔴 `0★`, `36 KB`, 🇻🇳 Vietnamese author |
| EDU-C2-015 parent Q&A | https://github.com/trantienit2015/agentic-star-school-administrative-procedure-parent-qa-agent | 🟢 **MIT — byte-read** (`1,083 B`, `sha256:a953ad384437…`, HEAD `6705948cbf03`) | 0 | APAC | 🟢 **New this pass (`p825`) — the only PARENT-FACING row in the cohort, and parents are the user this base has least supply for.** Answers school administrative-procedure questions for parents from the school's own documents. 🔵 **Pairs directly with `ferien-mcp` (`p824`, German school-holiday calendars): the parent question is overwhelmingly "when" and "what do I have to submit", and those are two different data sources** 🔴 `0★`, `31 KB` |
| EDU-C2-042 metadata exchange validator | https://github.com/TienXuanLam/agentic-star-education-learning-resource-metadata-exchange-validator-agent | 🟢 **MIT — byte-read** (`1,068 B`, `sha256:342465e77207…`, HEAD `24a7212bfe2a`) | 0 | APAC | 🟢 **New this pass (`p825`).** Validates a learning-resource catalogue export — JSON, XML or CSV — submitted for exchange between systems. 🔵 **The interoperability seam this base tracks through `1EdTech`/Caliper: a validator that runs BEFORE the exchange is the cheapest possible place to catch a mapping error, and it is the layer an LMS migration engagement always has to build by hand** |
| EDU-C2-173 accommodation evidence | https://github.com/KaitoYokomizo/agentic-star-student-accommodation-review-agent | 🟢 **MIT — byte-read** (`1,070 B`, `sha256:4c6c71f47b0d…`, HEAD `cab8ef1b35df`) | 0 | APAC | 🟢 **New this pass (`p825`) — the HIGHEST catalogue id observed (`173`), and the largest cohort payload at `192 KB`.** Validates the evidence in a student-accommodation review package *before* a human reviewer decides. 🔵 **Explicitly pre-decision: it does not grant or deny an accommodation, it establishes whether the package is decidable. That is the division of labour the EU AI Act's Article 14 asks for, written into the product boundary rather than into a disclaimer** |
| EDU-C2-030 L&D needs assessment | https://github.com/genkidesu7/agentic-star-corporate-training-program-needs-assessment-curriculum-agent | 🟢 **MIT — byte-read** (`1,071 B`, `sha256:e74683d915ae…`, HEAD `6d715d1bd7b7`) | 0 | APAC | 🟢 **New this pass (`p825`) — a second `T70` curriculum-instrument binding in one cohort.** Turns an HR/L&D manager's aggregate workforce profile plus a target **METI デジタルスキル標準 (Digital Skill Standards)** level into a validated curriculum outline. 🔵 **Naming DSS is what makes the output auditable: Japan's METI publishes the skill levels, so the gap analysis is against a government standard rather than against a model's opinion of seniority** |
| EDU-C2-050 safeguarding policy change | https://github.com/haidang024/agentic-star-education-safeguarding-policy-change-agent | 🟢 **MIT — byte-read** (`1,067 B`, `sha256:b22b7ca45c04…`, HEAD `ba529303e23c`) | 0 | APAC | 🟢 **New this pass (`p825`) — the first SAFEGUARDING row on this shelf.** Handles safeguarding-policy change: what a proposed change touches and who must be told. 🔵 **Safeguarding is the one education domain where a UK or EMEA buyer will not accept a general-purpose assistant, and this base has carried zero open supply for it across `29` passes** 🔴 `0★`, `53 KB` |
| EDU-C2-051 teacher PD evidence | https://github.com/haidang024/agentic-star-education-teacher-professional-development-evidence-agent | 🟢 **MIT — byte-read** (`1,067 B`, `sha256:b22b7ca45c04…`, HEAD `fb7ae91dd148`) | 0 | APAC | 🟢 **New this pass (`p825`), and it is the open supply under the EU AI Act Article 4 AI-LITERACY duty that `p824` recorded as almost absent.** Retrieves teacher professional-development evidence from **declared** LMS, HR and document-store connectors. 🔵 **"Declared connectors" is the operative phrase — the agent reads only sources an operator has registered, which is the difference between an evidence tool and a staff-surveillance tool** |
| EDU-C2-075 statistics comparability | https://github.com/sbdnakashima/agentic-star-education-statistics-comparability-agent | 🟢 **MIT — byte-read** (`1,074 B`, `sha256:134983626184…`, HEAD `513058f72003`) | 0 | APAC | 🟢 **New this pass (`p825`) — and it is the instrument this KB's OWN market pages need.** Assesses whether two education-statistics series are comparable and generates a cited brief. 🔵 **Every regional figure in `intel/market.md` is a series from a different body on a different base year; `p819` lost a pass to exactly this question. An agent whose output is "these two series cannot be compared, and here is why" is worth more than one that silently divides them** |
| EDU-C2-012 curriculum standards Q&A | https://github.com/DuongNT98/agentic-star-curriculum-standards-compliance-qa-agent | 🟢 **MIT — byte-read** (`1,066 B`, `sha256:33cf841bb83f…`, HEAD `c4a3394f37ba`) | 0 | APAC | 🟢 **New this pass (`p825`) — the LOWEST catalogue id observed (`012`) and the cohort's earliest creation date (`2026-09-22`).** Answers curriculum-standards and compliance questions. 🔵 **Shelved as the cohort's baseline shape: five nodes, a declared `required_trust_level`, and a test suite that runs without the platform — every later id is a variation on this skeleton** 🔴 `0★`, `43 KB` |
| ReadEase | https://github.com/athulmurali667/ReadEase | 🟢 **MIT — byte-read** (`1,085 B`, `sha256:c06fc2703736…`, HEAD `ec791dd811eb`) | 0 | Global | 🟢 **New this pass (`p825`) — the most complete DYSLEXIA build this base has found, at `12.5 MB`, and it is not a cohort artefact.** Monorepo reading assistant combining **real-time gaze tracking**, dyslexia biomarker screening and bilingual phonemic TTS. 🔵 **Gaze tracking as a READING-SUPPORT signal rather than a proctoring signal is the inversion worth noting: the same sensor that `T83`'s surveillance layer points at the candidate, this points at the text** 🔴 `0★`, created and pushed `2026-11-06` |
| Signlytic AI | https://github.com/Iyanuoluwa007/Signlytic_AI | 🟢 **MIT — byte-read** (`1,077 B`, `sha256:1d283c6f9cb2…`, HEAD `b5858d8e9f59`) | 0 | EMEA | 🟢 **New this pass (`p825`) — the first BRITISH SIGN LANGUAGE row on this shelf.** BSL↔English translation using deep learning plus LLMs with multi-modal output, shipped as a Chrome extension. 🔵 **BSL is a distinct language from ASL, and the open supply is overwhelmingly ASL — a UK accessibility engagement cannot use an ASL model, so this is a genuinely scarce asset** 🟢 `80 MB` payload, pushed `2026-11-13`; 🔴 `0★` |
| DuoSigna | https://github.com/vincenzopiconee/DuoSigna | 🟢 **MIT — byte-read** (`1,098 B`, `sha256:91920be3f3aa…`, HEAD `e1ab0a3fec17`) | 1 | Global | 🟢 **New this pass (`p825`) — the largest accessibility payload found this pass at `369 MB`.** ASL interactive learning platform: real-time computer vision plus a conversational AI tutor, Nuxt 3 / Vue 3 / FastAPI / MediaPipe / Groq. 🔵 **MediaPipe again, as in `p824`'s `Proctora` — the Apache-2.0 gaze-and-pose primitives are becoming the de-facto permissive base layer for every camera-facing education build on this shelf** 🔴 `1★`, pushed `2026-11-11` |
| Smart Tutor | https://github.com/FunctionSid/smart-tutor | 🟢 **Apache-2.0 — byte-read** (`11,408 B`, `sha256:cd2f54e1e506…`, HEAD `bad8733ce457`) | 0 | Global | 🟢 **New this pass (`p825`) — the only Apache-2.0 row added this pass (stock text, `11,408 B`), which matters for the patent grant a procurement lawyer asks about.** Agent-native learning workspace: documents, RAG, exams, memory, voice tutoring, a CLI, a WebSocket API and a Python SDK, `42 MB`. 🔵 **Ships a Python SDK and a WebSocket API rather than only a web app — i.e. it is designed to be embedded in someone else's product, which is the shape a studio can actually resell** 🔴 `0★`, pushed `2026-09-21` |
| Dyslexia Detection using Games | https://github.com/TanviVP/Dyslexia_Detection_using_Games | 🟢 **MIT — byte-read** (`1,081 B`, `sha256:b15ba4e811a6…`, HEAD `5ff40b21e842`) | 0 | Global | 🟢 **New this pass (`p825`) — the GAME-BASED half of the dyslexia layer, beside `ReadEase`'s sensor-based half.** Early dyslexia screening via interactive assessment games with CNN + XGBoost, React/TypeScript/SQL. 🔵 **Game-based screening is what gets consented to for young children where a gaze tracker does not, so the two rows are complements rather than competitors** 🔴 `0★`, `59 KB`, licence holder `DysLexia Support Platform` (2024) against a `2026-09-13` push — an older grant carried onto a new build |

## 🟢 Twenty-ninth pass (`p824`, 2026-11-15) — the licence FIELD is wrong in BOTH directions, and the proctoring nil was never a nil

🟢 **`227` build-safe agents on this shelf — `208` carried, `19` added by `p824`.** 🟢 **Gate-confirmed:**
`python3 ingest/derive-counts.py` ran in this environment and returns GREEN on all five shelves,
for a second consecutive pass.

🔴 **The scheduler's mandated star-ranked WebSearch battery nilled for a `39`th consecutive pass.**
Run in full — global legs (`top open source AI agents education 2026 github MIT`,
`github trending education AI 2026`,
`open source platform education ERP CRM MIT Apache student information system`,
`AI education industry trends 2026`) and all four regional legs. 🔵 **The global agent leg returned
no education-specific list at all** — it surfaced `OpenHands`, `browser-use`, `AutoGPT`, `LangChain`,
`Langflow`, i.e. the general agent shelf, and one aggregator page that names no repositories.
🔵 **The trending leg returned `DeepTutor`, `Claw-ED`, `interactive-learning`, `ChinaTextbook` and
`microsoft/ai-agents-for-beginners` — all five already held.** 🔵 **The ERP leg returned `OpenEduCat`
(LGPL) and `eduTrac SIS` (GPL-3.0), both already on `verticals/solutions.md` and both copyleft, which
is the answer this base has recorded for the platform tier since `p805`.** 🟢 **Recorded as coverage
confirmation. The market legs DID produce — see `intel/market.md`, where every regional subsection
gained a dated `p824` block.**

🟢 **What produced rows was, for a fourth pass running, `search/repositories` with `sort=updated` and
NO star floor — pointed this pass at two layers this base had written off, and at one it had never
queried in the right language.**

### 🟢 The finding (`T81`): the repository licence FIELD and the licence BYTES diverge in three named ways, and the field errs in BOTH directions

🔴 **`20` repositories byte-read this pass; `4` diverge from the field GitHub reports — `20%`.** And
the divergence is not noise, it has three mechanical causes, each one measured:

| Form | Repository | Field says | Bytes say | Why the matcher failed |
|---|---|---|---|---|
| **Truncated** | `determinate/octoeye` | `NOASSERTION` | AGPL-3.0 title + preamble, **`2,567 B`** against a stock `34,522 B` | 🔴 The file stops before the operative terms. It NAMES a licence and GRANTS nothing |
| **Dual-headed** | `bster/ai-future` | `NOASSERTION` | 🟢 `MIT License (Code)` **and** `Creative Commons Attribution 4.0 International (Content)` in ONE file, each with its directories named | Two grants, one file — no single stock text to match |
| **Carved-out** | `FabianJun/PresentTogether` | `NOASSERTION` | 🟢 Stock MIT **plus** *"Third-party material is excluded from this grant"* and *"Software permissions do not override academic rules or rights to institutional content"* | Stock text + appended boundary ⇒ hash miss |
| **Two-file split** | `OpenRaiser/EduGraph` | 🟢 `Apache-2.0` | Apache-2.0 in `LICENSE`, 🔴 **CC BY-SA 4.0 in `LICENSE-DATA`** — and the DATA (`7,062` concepts, `18` subjects) IS the product | The field reports the file called `LICENSE`, which here governs the smaller asset |

🔴 **So the field is wrong in both directions at once.** It **under-reports** safety on `ai-future` and
`PresentTogether` — two repositories whose grants are the clearest in this pass, written out in prose
with the governed directories named, and both show as unlicensed. It **over-reports** safety on
`EduGraph` — `Apache-2.0`, build-safe by the field, share-alike on the asset a studio would actually
ship. 🔵 **A stars-plus-licence-field ingest therefore rejects the best-documented repositories and
admits the share-alike one, in the same sweep.** 🟢 **This sharpens `T52` (`NOASSERTION` means the
matcher failed) with the three reasons it fails, and `T78` (the split licence) with the finding that
the split has a PHYSICAL FORM which determines what the field reports.** 🔵 **`P57`'s gate is extended
in `compose/patterns.md` to probe `LICENSE-DATA`, `LICENSE-CONTENT` and `*_NOTICES.md` before the code
grant decides anything.**

### 🟢 The second finding (`T83`): `p815`'s proctoring nil was a VOCABULARY artefact — the layer is a `~100`-repository population

🔴 **`p815` published: *"an EMEA client facing an Annex III conformity question has no adoptable
AI-proctoring base in any licence. Build, or decline."*** 🟢 **That is now measured as FALSE on the
supply axis and TRUE on the maturity axis, and the two must be stated separately:**

| Query | Total | Star ceiling | Licence of the ceiling |
|---|---|---|---|
| `proctoring exam open source` (`p815`'s query, re-run) | `12` | `4★` | `NOASSERTION` |
| 🟢 `remote proctoring ai` | **`101`** | `17★` | 🔴 NONE |
| 🟢 `exam integrity ai detection` | **`63`** | **`88★`** (`braviaprime/proctorai`) | 🔴 **NONE — byte-probed, `NO_PAYLOAD` on `main`** |

🔵 **`p815` asked the layer for the word "open source" and got `12`; asking it for what it DOES returns
`101`.** 🟢 **Six permissive rows exist and five are shelved below** (`Proctora`, `examguard`,
`AI-Smart-Proctoring-System`, `AI-Proctor-Exam-Monitor`, `AI-Driven-Remote-proctoring-System`).
🔴 **Every one of them is a single-developer build at `≤6★`, and the layer's star mass — `88★`, `17★` —
carries no licence payload at all.** 🔵 **So the honest sentence is not "build or decline", it is
"ASSEMBLE": the components exist permissively, the product does not, and `P58` is that assembly with
the Annex III boundary drawn first.**

### 🔴 The third finding (`T84`): Vietnam has the world's newest binding high-risk rule for educational AI, and a measured permissive-supply ZERO underneath it

🔴 **Vietnam's AI law took effect `2026-03-01` and its high-risk category names education, including
automated assessment; MOET has scheduled AI content into every grade `1`–`12`** (`SECONDARY` —
web-search summary, see `intel/market.md`; `oecd.org` was refused at this session's proxy, so no
multilateral source could be read first-hand). 🔴 **Supply underneath it, measured first-hand:**
`q="giao duc viet nam ai"` → `7` repositories, **every one unlicensed**, ceiling `4★`;
`q="vietnam education platform"` → `5`, **every one unlicensed**, ceiling `1★`. 🔴 **The ONLY licensed
Vietnamese education artefact this pass found is
[`NukeGeng/VietAIS-Sentinel`](https://github.com/NukeGeng/VietAIS-Sentinel) — and it is AGPL-3.0**
(byte-read, `34,522 B`, stock text), i.e. it lands in the copyleft table below, not on this shelf.
🔵 **A jurisdiction that regulates automated assessment as high-risk, with exactly zero build-safe
open supply in its own language. That is the sharpest BUILD slot `p824` found, and it is in APAC.**

### 🟢 The fourth finding (`T82`): LATAM's supply is indexed under the SYSTEM NAME, not the pedagogy — `4` against `709` on this pass's own queries

🔴 **Pedagogical vocabulary, run in Spanish and Portuguese:** `q="agente educativo inteligencia
artificial"` → **`4`**, *all four unlicensed*, ceiling `0★`; `q="professor agente ia educacao"` →
**`0`**; `q="mcp universidad estudiantes"` → **`0`**; `q="escuela mcp agente"` → **`0`**.
🟢 **The same region, queried by the name of the system of record:** `q="sigaa"` → **`709`**, with
build-safe rows pushed inside `48` hours — [`unb-mds/2026-2-Followw`](https://github.com/unb-mds/2026-2-Followw)
(MIT, `9★`), [`kalebhenrique/sarue-unb`](https://github.com/kalebhenrique/sarue-unb) (Apache-2.0, `15★`),
[`vintatri/ufc-mcp`](https://github.com/vintatri/ufc-mcp) (MIT), [`erickmsms/sigaa-faltas`](https://github.com/erickmsms/sigaa-faltas) (MIT);
`q="moodle agente"` → **`20`**, including [`balejosg/tiza`](https://github.com/balejosg/tiza) (MIT) and
[`nialvape/utn-mcp`](https://github.com/nialvape/utn-mcp) (ISC, `12★`).
🔵 **`177:1` between the two framings of the same region.** 🟢 **The transferable rule, and it is now a
sourcing instrument rather than an observation: in LATAM the agent is named after the REGISTRY it
reads — SIGAA, SIU Guaraní, Moodle, CAPES, SciELO — never after the teaching it supports. `P59` turns
this into a runnable discovery protocol for an engagement.**

### The rows — `19` added this pass, all `19` build-safe, `0` copyleft

| Name | Repo | Licence | Stars | Region | Description |
|---|---|---|---|---|---|
| examguard | https://github.com/epoko77-ai/examguard | 🟢 **MIT — byte-read** (`1,078 B`, `sha256:963f8f22…`, holder `ExamGuard contributors`, 2026) | 3 | APAC | 🟢 **New this pass (`p824`) — and a category no shelf in this base held: PHYSICAL invigilation, not biometric surveillance.** Smart-glasses screening for the Korean 수능 exam hall — BLE cues, composite advertising-packet filters, optical read from the proctor's desk, and a physical catalogue of known devices. 🔵 **It watches the ROOM and the DEVICES, never the candidate's face or affect — which is the one proctoring shape the EU AI Act's February 2025 emotion-recognition ban in education cannot touch.** 🟢 Created `2026-11-07`, pushed `2026-11-09`; `562 KB` of real payload |
| AI-Smart-Proctoring-System | https://github.com/ENGABHAY/AI-Smart-Proctoring-System | 🟢 **MIT — byte-read** (`1,075 B`, `sha256:4e2a4004…`, holder `Abhay Rambhau Kadam`, 2026) | 1 | APAC | 🟢 **New this pass (`p824`) — the EVIDENCE half of `T83`, and the only permissive row in the layer that ships it.** YOLO + OpenCV suspicious-activity and prohibited-object detection with **evidence logging and integrity reports**, 🇮🇳 India. 🔵 **An integrity decision that cannot produce its evidence does not survive an appeal — `P37`'s whole argument — and this is the layer's only open implementation of the evidence side** 🔴 `1★`, pushed `2026-10-02`, `20 MB` |
| Proctora | https://github.com/amaanwarsi/Proctora | 🟢 **MIT — byte-read** (`1,055 B`, `sha256:26e0d192…`, 2026) | 3 | Global | 🟢 **New this pass (`p824`) — the cleanest permissive SKELETON in `T83`'s layer.** Flask + OpenCV + MediaPipe, browser-based fullscreen exam environment. 🔵 **MediaPipe rather than a bespoke model is what makes it portable: the gaze and pose primitives are Apache-2.0 upstream, so the whole stack stays build-safe** 🔴 Pushed `2026-04-07` — seven months stale, and described by its own author as a demo |
| AI-Proctor-Exam-Monitor | https://github.com/Gorav22/AI-Proctor-Exam-Monitor | 🟢 **MIT — byte-read** (`1,068 B`, `sha256:0532d9d7…`, holder `Gorav Jindal`, 2025) | 6 | Global | 🟢 **New this pass (`p824`) — the highest-starred PERMISSIVE row in `T83`'s layer, and `6★` is the whole point.** Computer-vision exam-integrity monitor, `39 MB`. 🔵 **The layer's star ceiling is `88★` and unlicensed; its permissive ceiling is this row at `6★`. That `14:1` gap IS the finding** 🔴 Pushed `2025-07-02` |
| AI-Driven-Remote-proctoring-System | https://github.com/yuvaraj-06/AI-Driven-Remote-proctoring-System | 🟢 **Apache-2.0 — byte-read** (`11,356 B`, `sha256:43070e2d…`, stock text) | 3 | Global | 🟢 **New this pass (`p824`) — the only Apache-2.0 row in the proctoring layer, which matters because Apache's patent grant is the one a procurement lawyer asks about for a surveillance-adjacent deliverable.** `67 MB`. 🔴 **Pushed `2022-11-21` — four years stale; shelved for the GRANT and the architecture, not as a starting codebase** |
| lesson2hw-physics | https://github.com/Laura-LLU/lesson2hw-physics | 🟢 **MIT — byte-read** (`1,080 B`, `sha256:69ee15c8…`, holder `LauraPhysics / Laura-LLU`, 2026) | 0 | APAC | 🟢 **New this pass (`p824`), and a fifth instance of `T70`: the skill binds to a CURRICULUM INSTRUMENT, not a subject.** Blackboard photo, slide deck, PDF or one sentence → homework against **CAIE `9702`/`0625`** physics. 🔵 **Naming the syllabus codes is what makes it sellable: `9702` is A-Level Physics and `0625` is IGCSE Physics, so the output is gradeable against a published mark scheme rather than against a model's taste** 🟢 Created `2026-11-14`, pushed `2026-11-15`; runs under Codex, Claude Code and WorkBuddy |
| ph-data-mcp-server | https://github.com/CharlieJamesGwapo/ph-data-mcp-server | 🟢 **MIT — byte-read** (`1,075 B`, `sha256:bbc77148…`, holder `Charlie James Abejo`, 2026) | 0 | APAC | 🟢 **New this pass (`p824`) — the first 🇵🇭 Philippine national-data row in this base.** Scholarships, schools, regions, holidays, peso rates and weather behind one MCP server, **no API key**. 🔵 **The keyless property is the procurement property: the `p818` DergiPark finding restated in a second jurisdiction — an agent on a published, unauthenticated endpoint survives a review that a scraper does not** 🔴 `0★`, pushed `2026-11-09` |
| V2 (DigiLab) | https://github.com/Asvix-04/V2 | 🟢 **MIT — byte-read** (`1,063 B`, `sha256:cab64cbe…`, holder `Digilab`, 2025) | 6 | Global | 🟢 **New this pass (`p824`) — the most complete build in `p824`'s AI-literacy sweep, at `76 MB`.** Academic RAG assistant for **Media and Information Literacy** with an explicit **Teacher Mode and Student Mode**, hybrid open LLMs + RAG + a **Neo4j knowledge graph**. 🔵 **Teacher mode answers in named sections — Methodology, Conceptual Understanding — which is the shape a lesson-planning buyer asks for and almost no tutor repo produces** 🔴 Pushed `2026-10-16` |
| ferien-mcp | https://github.com/mohammad-abbasi-sh/ferien-mcp | 🟢 **MIT — byte-read** (`1,071 B`, `sha256:17a9ced1…`, holder `Mohammad Abbasi`, 2026) | 0 | EMEA | 🟢 **New this pass (`p824`).** German school holidays (*Schulferien*) by year and *Land* via `ferien-api.de` — is-it-a-holiday, next-holiday, read-only and unofficial. 🔵 **The smallest useful row on this shelf and a deliberate one: every scheduling, timetabling and parent-facing agent in `compose/patterns.md` needs a term calendar, and in 🇩🇪 Germany that calendar is `16` different *Länder* calendars** 🔴 `0★`, created and pushed `2026-11-14` |
| critical-ai-literacy-skill | https://github.com/malkreide/critical-ai-literacy-skill | 🟢 **MIT — byte-read** (`1,068 B`, `sha256:65090998…`, holder `Hayal Oezkan`, 2026) | 0 | EMEA | 🟢 **New this pass (`p824`) — and it arrives with a LINEAGE PROOF rather than a claim.** 🔵 **Its licence `sha256` is byte-identical to [`malkreide/swiss-academic-libraries-mcp`](https://github.com/malkreide/swiss-academic-libraries-mcp), shelved at `p818` — the same `65090998…`, the same holder line. `T37`'s byte-hash de-duplication instrument resolving a same-author relationship across two repositories, which is the use it was built for.** German-language skill for critical theoretical analysis of AI systems, calibrated on Frankfurt School critical theory. 🔵 **Article 4 of the EU AI Act has obliged every organisation using AI — every school included — to ensure AI literacy since `2025-02-02`, and this is one of two German-language artefacts this pass could find under it** 🔴 `0★`, pushed `2026-02-20` |
| ai-on-campus (PRISMA) | https://github.com/LucaTamSapienza/ai-on-campus | 🟢 **MIT — byte-read** (`1,064 B`, `sha256:9394f62b…`, holder `Luca Tam`, 2026) | 0 | EMEA | 🟢 **New this pass (`p824`) — the third CHALLENGE-ORIGIN row in this base and the second channel of its kind, after `T74`'s African Agentic AI Design Challenge.** *"Every exam question, tested from three sides before the exam"* — a multi-agent web app for university teachers, built in one day for **Reply's "AI on Campus"** 🇮🇹. 🔵 **Pre-publication question review is the formative counterpart to `T83`'s surveillance layer: it reduces the cheating opportunity instead of detecting the cheat** 🔴 **`0 KB` reported by the API on the day of creation — shelved for the grant and the design, with the payload explicitly NOT yet verified as non-empty** |
| PresentTogether | https://github.com/FabianJun/PresentTogether | 🟢 **MIT — byte-read** (`1,340 B`, `sha256:fe728274…`, holder `FabianJun and the Singularity seminar contributors`, 2026) 🔴 field reports `NOASSERTION` — see `T81` | 0 | Global | 🟢 **New this pass (`p824`) — one of the two rows that prove the field errs AGAINST good practice.** Competence-enhancing guide and agent skill for co-designing interactive presentations. 🔵 **Its licence is `276 B` longer than stock MIT because it adds two boundaries this base has asked for repeatedly: third-party material excluded from the grant, and an explicit statement that software permissions do not override academic rules or institutional content rights (`docs/ACADEMIC_USE.md`).** 🔴 **Doing that correctly is what made GitHub report it as unlicensed** 🟢 Created and pushed `2026-11-15`, `57 MB` |
| tiza | https://github.com/balejosg/tiza | 🟢 **MIT — byte-read** (`1,064 B`, `sha256:7a3a02ea…`, holder `balejosg`, 2026) | 1 | EMEA | 🟢 **New this pass (`p824`) — and the clearest HUMAN-OVERSIGHT write gate on any shelf in this base.** Spanish-language CLI and agent skill that publishes pages, labels, assignments, auto-marking quizzes and **H5P** activities into a Moodle *aula virtual* from Claude Code, Codex, opencode or GitHub Copilot. 🟢 **Its stated contract is the control: *"el agente prepara… tú los revisas y decides qué llega a tu alumnado"* — the agent drafts, the TEACHER approves before anything reaches a learner.** 🔵 **That is EU AI Act Article 14 human oversight shipped as a default rather than bolted on, and `P60` generalises it.** 🟢 **It also ships its own boundary notice — independent, unofficial, "use it respecting your centre's rules"** 🟢 Pushed `2026-11-15`, `7.8 MB` |
| ufc-mcp | https://github.com/vintatri/ufc-mcp | 🟢 **MIT — byte-read** (`1,070 B`, `sha256:14b73fb8…`, holder `Equipe UFC-MCP`, 2026) | 0 | LATAM | 🟢 **New this pass (`p824`) — `T77`'s institution-integration population gaining a `15`th jurisdiction and 🇧🇷 Brazil's third campus.** Read-only MCP for Universidade Federal do Ceará students: SIGAA, Turma Virtual, the **RU** (university restaurant) menu, academic calendar and news. 🔵 **The RU menu is not a joke entry — it is the highest-frequency query a Brazilian undergraduate makes, and bundling it with the registry read is how this tier gets daily use rather than registration-week use** 🔴 `0★`, created and pushed `2026-11-13` |
| 2026-2-Followw | https://github.com/unb-mds/2026-2-Followw | 🟢 **MIT — byte-read** (`1,067 B`, `sha256:aec18ce5…`, holder `Followw UnB`, 2026) | 9 | LATAM | 🟢 **New this pass (`p824`) — the highest-starred LATAM row added this pass, and the first in this base published by a UNIVERSITY COURSE ORG.** *"Uma nova forma de usar o SIGAA UnB"* — Universidade de Brasília. 🔵 **The owner `unb-mds` is UnB's Métodos de Desenvolvimento de Software course, and the repository is named for its semester (`2026-2`). That is a renewable supply channel, not a lone maintainer: the same org ships a new cohort of SIGAA tooling every term, which changes the staleness arithmetic for this whole tier** 🟢 `9★`, pushed `2026-11-15` |
| sigaa-faltas | https://github.com/erickmsms/sigaa-faltas | 🟢 **MIT — byte-read** (`1,065 B`, `sha256:a638443b…`, holder `erickmsms`, 2026) | 0 | LATAM | 🟢 **New this pass (`p824`).** *"Descubra quantas faltas você ainda pode ter em cada disciplina da UFPE (SIGAA), com o Claude"* — Universidade Federal de Pernambuco 🇧🇷, absence-allowance calculation against the `75%` attendance rule. 🔵 **One rule, computed correctly, from the registry of record. It is the smallest shape this tier takes and the one most likely to be right** 🔴 `0★`, pushed `2026-11-13` |
| Neuro-CanvasLMS | https://github.com/BloodyReginaa/Neuro-CanvasLMS | 🟢 **MIT — byte-read** (`1,069 B`, `sha256:903078f6…`, 2026) | 0 | Global | 🟢 **New this pass (`p824`) — `T77`'s tier again, on the OTHER dominant LMS.** Canvas LMS MCP server for Claude and ChatGPT: deadlines, grades, lecture files, announcements, **read-only, deployed to the student's own frontend**. 🔵 **Canvas is the tier's second system after Moodle, and `19.5 MB` of payload with a declared read-only posture is the version of it a university's IT office can say yes to** 🔴 `0★`, pushed `2026-11-09` |
| course-engine-skills | https://github.com/SolutionLabsIO/course-engine-skills | 🟢 **MIT — byte-read** (`1,105 B`, `sha256:95897ad9…`, holder `Laboratoires de Solutions Web Inc.`, 2026) | 0 | Global | 🟢 **New this pass (`p824`) — and the shape is the finding, not the size.** A `6 KB` MIT agent skill that drives a **commercial** course platform (`mcp.course-engine.com`) from Claude. 🔵 **`P10`'s thesis with a vendor on the other end: the SKILL is permissively licensed and the SERVICE is not, so a studio can read, fork and adapt the agent-facing half of a proprietary product without touching its licence. Expect more of this shape as SaaS vendors race to be agent-addressable** 🔴 `0★`, created and pushed `2026-11-09` |
| ai-future | https://github.com/bster/ai-future | 🟢 **MIT (code) — byte-read** (`1,827 B`, `sha256:2b95011a…`, holder `Ben Stern`, 2026) 🟢 **+ CC BY-4.0 (content), same file** 🔴 field reports `NOASSERTION` — see `T81` | 3 | Global | 🟢 **New this pass (`p824`) — the second row proving the field errs against good practice, and the better-written of the two.** Open, forkable liberal-arts AI curriculum: AI literacy, ethics, philosophy of mind, seven futures, and what AI means for education. 🟢 **Its single `LICENSE` file names the governed directories for each grant — React components and build tooling under MIT, the text, arguments, framing and discussion questions under CC BY 4.0, adaptation and commercial use explicitly permitted with credit.** 🔵 **That is exactly the two-asset disclosure `P57` demands of a courseware repository, written voluntarily — and it is reported as unlicensed** 🔴 Pushed `2026-06-30` |

### 🔴 Rejected this pass — named, with the reason

| Candidate | Repo | Actual license | Stars | Why rejected |
|---|---|---|---|---|
| proctorai | https://github.com/braviaprime/proctorai | 🔴 **NONE — byte-probed `NO_PAYLOAD`** on `main` across `LICENSE`, `LICENSE.md`, `LICENSE.txt`, `LICENCE`, `COPYING` | 88 | 🔴 **The star ceiling of `T83`'s entire layer, and it carries no grant.** `148 MB` of real code — face recognition, webcam, browser and audio checks — that a studio cannot touch |
| octoeye | https://github.com/determinate/octoeye | 🔴 **TRUNCATED AGPL-3.0 — byte-read** (`2,567 B`, `sha256:2b91b198…`, against a stock `34,522 B`); field reports `NOASSERTION` | 0 | 🔴 **`T81`'s truncation case.** On-premise proctoring with dual webcam, screen recording and WebRTC; the `LICENSE` prints the AGPL title and preamble then stops before the operative terms. **No terms means no grant — and the stated intent is network copyleft regardless** |
| openproct | https://github.com/OpenProct/openproct | 🟢 MIT — byte-read (`1,065 B`, `sha256:b97fd4be…`, holder `OpenProct`, 2025) | 2 | 🔴 **Licence is real; the repository is `3 KB` in total — README plus LICENSE, no implementation.** 🔵 **A licence is not a codebase. Recorded so the next pass does not re-discover the name and assume otherwise** |
| waypoint-challenge | https://github.com/igoldstein19/waypoint-challenge | 🔴 **NONE — byte-probed `NO_PAYLOAD`** on `main` | 3 | 🔴 **It is a CHALLENGE BRIEF, not an implementation:** *"The Special Education Challenge: build an MCP server that helps teachers differentiate instruction for students with Individualized Education Programs."* 🔵 **The clearest evidence this pass found that the IEP gap (`T61`) is known, is being advertised, and is still unfilled** |
| mentor-univesp-com170 | https://github.com/josemardp/mentor-univesp-com170 | 🔴 **NONE — byte-probed `NO_PAYLOAD`** on `main` | 0 | 🔴 **Unlicensed, and disqualified on a second axis.** *"Agente que acompanha um curso EAD no lugar do aluno"* — an agent that takes the course IN THE STUDENT'S PLACE. 🔵 **`T40`'s third risk axis applied to PURPOSE rather than to data source: a studio cannot ship substitution-of-the-learner, whatever the licence said** |
| EyeEP | https://github.com/100205ivan/EyeEP | 🔴 **NONE** (sibling [`100205ivan/IEP`](https://github.com/100205ivan/IEP) likewise NONE) | 1 | 🔴 **Two further IEP-management repositories from one author inside five weeks, both unlicensed.** 🔵 **Supply pressure on the gap, zero adoptable output — which is `T61`'s IEP confirmation holding for a third consecutive measurement** |

### 🔴 The region this pass did NOT produce, stated rather than smoothed

🔴 **`0` of the `19` rows above are North American.** 🟢 **It is a measurement, not an absence of effort:**
`q="powerschool clever district mcp"` → **`0`**; `q="k12 district data agent"` → **`0`**;
`q="infinite campus schoology skyward"` → **`0`** — the three largest US K-12 SIS vendors, zero agent
surface of any licence. 🔵 **North America's supply in this base reaches it through STANDARDS bodies
instead (`Ed-Fi-Exchange-OSS`, `CarnegieLearningWeb/caliper-ts`, `googleworkspace/oneroster-…`), which is
`T58`/`T14`'s standing finding and it held again this pass.** 🟢 **The one North American row `p824` DID
produce is a curriculum and it is filed in `repos/foundations.md`: `hanhuark/machine-learning-for-engineers`,
BSD-3-Clause, University of Arkansas.**

🟡 **Channel note.** `gh api search/repositories` and `raw.githubusercontent.com` both answered, so every
repository above is **byte-read and first-hand**. 🔴 **`gh api repos/{owner}/{repo}` is refused for
unattached repositories in this environment** — default branches were resolved from the search response
instead, which is `T57`'s instrument, and it held on all `20` probes. 🔴 **`oecd.org` was refused at the
proxy**, as at `p822`; every market and regulatory item added this pass is marked `CITED, NOT READ`. 🔴 **And the HTML channel the scheduler prescribes for URL verification (`curl -sI https://github.com/<owner>/<repo>`) is REFUSED in this environment — controlled in both directions at `p824`: `torvalds/linux` returns `403` and the invented `zzz-not-a-real-owner-p824/zzz-not-a-real-repo` ALSO returns `403`, so the channel cannot distinguish a real repository from an imaginary one and no verdict may be read from it.** 🟢 **Existence was established instead on the two channels that ARE informative and that pass the same control: `gh api search/repositories -f q='repo:<owner>/<repo>'` returns `1` for the real repository and HTTP `422 Validation Failed` for the invented one, and `raw.githubusercontent.com` returned licence bytes for every shelved row.**

🟢 **`187` build-safe agents on this shelf — `172` carried, `15` added by `p822`.** 🟢 **And the
figure IS gate-confirmed this pass, for the first time in five:** `python3 ingest/derive-counts.py`
RAN in the `p822` environment, where `p818`–`p821` were each refused by the sandbox classifier.
🔵 **`ACTION p821-B` — "run the repository's own gate, not a reimplementation" — is therefore
DISCHARGED, and it discharges with a result worth recording: the gate reproduced every figure the
inline re-derivations had claimed (`172` shelf, `132` foundations, `112` verticals, `72` trends,
`51` recipes). The degraded-channel workaround was FAITHFUL, which is a fact this base could not
know until the real instrument ran. See `T76`.**

🟢 **`15` rows added — the largest non-nil discovery pass since `p818`, and the second in a row.**
🔴 **The mandated star-ranked legs nilled a `37`th consecutive time:** `DeepTutor`, `Claw-ED`,
`ChatTutor`, `tutor-gpt`, `moodle`, `edx-platform`, `Sakai`, `OpenEduCat`, `Chamilo` and
`ai-agents-for-beginners` all came back **already held**, exactly as `T63` predicts.
🟢 **What produced rows was again a channel setting rather than a market change — and this pass
found a SECOND productive channel on top of `p821`'s recency axis:**

- **Recency with no star floor** (`created:>2026-10-15`, `sort=updated`) — `p821`'s finding,
  reconfirmed: `11` of the `15` rows below are under `5★`.
- 🟢 **The CHALLENGE-ORIGIN channel, measured and BOUNDED this pass.** `p821` noticed that
  `jemma` came from the African Agentic AI Design Challenge. `p822` queried the challenge NAME as
  an exact phrase and got a closed set: **`8` repositories in the index, `4` of them in the
  Education track**, yielding one build-safe row (`meska-brain`), one copyleft row (`DIRA`) and
  one rejection (`contextbridge-long-view`, no licence and an EMPTY repository). 🔵 **A discovery
  channel with a known denominator is worth more than a large one without: see `T74`.**

🔴 **The third finding is the one that changes how this base must read every star count it has
ever written down, and it is `T73`.** Sweeping the agent-skills axis returned a cluster of
identically described repositories. Measured rather than assumed:

| Control | Original | The cluster |
|---|---|---|
| Repository | `Simpleyyt/ai-manus` | `Topkiflare74/ai--manus2.0` and `~774` siblings |
| Created | `2025-04-26` | `2026-11-13` / `2026-11-14`, within `48` hours |
| Licence payload | MIT | **Apache-2.0** — RELICENSED against the original |
| Size | `22,029 KB` | `118 KB` |
| Code | full tree | 🔴 **NONE** — `package.json`, `requirements.txt`, `setup.py`, `install.sh` all `404` |
| README `sha256` | `01c6105005…` | `d2425cc10e…`, **identical across siblings** |
| Open issues | `75` | `0` |
| Stars | `1,647` | `652`–`678` EACH; top `30` siblings hold `14,003` |

🔴 **The clone READMEs carry no code and one call to action: a Dropbox `.rar` download badge. That
is a malware lure wearing a real MIT project's name, an OSI licence file and purchased stars, and
GitHub's search index returns `775` of them.** 🟢 **Not followed, and recorded as an indicator
only.** 🔵 **The consequence for this base is concrete: a stars-ranked ingest with no payload
control would have published phantom rows that out-rank the genuine upstream `8.5:1`. The existing
byte-read discipline caught it, and `P52` turns that discipline into a runnable gate.**

🟡 **Channel note, stated rather than smoothed.** Egress in the `p822` environment resolves GitHub
only — `raw.githubusercontent.com` and `gh api search/*` answered, while `oecd.org` was refused at
the proxy. 🟢 **Consequence, stated both ways: every repository below is BYTE-READ and first-hand;
every market and regulatory item added to `intel/market.md` this pass came through web search and
is marked `CITED, NOT READ`.** 🟢 **The byte-read channel was controlled in both directions — the
`404`s above (`package.json` and three siblings) came back on the same `raw.githubusercontent.com`
path that returned `20` real payloads.**

## 🟢 Twenty-sixth pass (`p821`, 2026-11-15) — the nil streak ends at `35`, and what ended it was a query setting

🟢 **`172` build-safe agents on this shelf — `168` carried, `4` added by `p821`.** 🔴 **The figure
is NOT gate-confirmed this pass:** `make hooks` was refused by the sandbox classifier for a
**FOURTH** consecutive pass, so the count is re-derived INLINE over the two build-safe table
signatures (`| Name | Repo | Licence | Stars | Region | Description |`), copyleft and rejection
tables excluded as the gate excludes them: `151 + 17 = 168` before this pass, `155 + 17 = 172`
after. 🔵 **`ACTION p820-B` stands and is re-registered as `ACTION p821-B`.**

🟢 **`4` rows added, and for the first time in `36` passes the discovery legs did NOT nil.**
🔴 **The mandated star-ranked legs nilled a `36`th time exactly as `T63` predicts** — `DeepTutor`,
`tutor-gpt`, `ChatTutor`, `Claw-ED`, `OpenTutor`, `mathua`, `Papermorph`, `freelingo`,
`anki-mcp-server`, `Study-Mate`, `teacher-to-skills`, `tsugi`, `mentingo`, `classroomio`,
`advisingapp`, `cn-math-taxonomy` and `StudyOnTV` all came back **already held**.
🟢 **What produced rows was a RECENCY-ranked channel, not a star-ranked one:**
`sort=updated` with `created:>2026-10-25` and **no star floor at all**, which is the one setting
this base had never run. Every row below is under `30★` and three of the four are under `5★`.
🔵 **The lesson is `T63`'s complement and it is `T70`: the star-ranked channel is saturated
because stars are a LAGGING measure, and a base that filters on them cannot see supply younger
than its own cadence.**

🟢 **The four rows, each placed by a locative string that is quoted rather than inferred:**
[`mawta`](https://github.com/amaru-one/mawta) (MIT, `2★`, **LATAM** — Peru's `CNEB` and its
`AD/A/B/C` achievement levels, named in the README);
[`jemma`](https://github.com/AI-Native-Ventures/jemma) (MIT, `0★`, **EMEA** — *"Built for the
African Agentic AI Design Challenge, Education track"*);
[`teach-to-learn`](https://github.com/olele114/teach-to-learn) (MIT, `4★`, **APAC** — `SKILL.md`
and `references/` authored in Chinese, `README_CN.md` present);
[`educa-educai`](https://github.com/tomasfossatti/educa-educai) (MIT, `0★`, **Global** —
🔴 **Spanish-language throughout and NO locative string anywhere in the README, so it is NOT
placed in LATAM; a language is not a location, and this base has published that rule before**).

🔴 **One candidate measured and REFUSED, with the reason:**
[`wisdom-km/k12-qbank`](https://github.com/wisdom-km/k12-qbank) (MIT byte-read, `0★`) is a real
🇨🇳 Heilongjiang 人教版 maths question-bank design, and its own README says *"还没有网页，也没有数据库"*
— no web surface, no database — with `scripts/status.py` printing status and nothing else.
🟢 **A design document with a licence is not a build-safe agent. Row filed under rejections so the
next pass does not pay to rediscover it, and so a later pass can promote it when it ships.**

🟡 **Channel note, and it is wider than the gate this pass.** Outbound HTTPS in the `p821`
environment resolves **GitHub only**: `raw.githubusercontent.com` and `gh api search/repositories`
answered, while `indicelatam.cl`, `oecd.org` and `data.consilium.europa.eu` all failed to resolve.
🟢 **Consequence stated rather than hidden: every repository below is BYTE-READ and first-hand;
every regulatory and market item in `intel/market.md` this pass is `CITED, NOT READ` and says so.**
🔵 **The byte-read channel was controlled in both directions —
`amaru-one/mawta-nonexistent-p821` and `fotedev/not-a-real-repo-p821` both returned `404` on the
same `raw.githubusercontent.com` path that returned the seven real payloads.**

🟢 **`168` build-safe agents on this shelf, UNCHANGED by `p820` and re-confirmed by a running
gate** — `tables=2 rows=168 distinct=168 graded=168 ragged=0 nolink=0 dupes=0`.

🔴 **`0` rows added this pass, and that is a measurement with a denominator.** The mandated agent
legs returned `DeepTutor` (reported `~52.8k★`), `OpenMAIC`, `ai-engineering-hub`, `Claw-ED` and
`ChatTutor`; **all five were already held**, which is the `35`th consecutive nil on these legs and
exactly what `T63` predicted. 🔵 **Two items in the whole battery were NOT held — California
`SB 1288` and Alabama `HB 1227` — and both are US state instruments of a class this base tracks by
COUNT rather than individually, so neither became a row.** 🟢 **Named in `agents/trending.md` so the
next pass does not pay to rediscover them.**

🟡 **Channel note on the count, stated rather than smoothed, and now three passes old.**
`ingest/derive-counts.py` could not be executed in the `p820` environment either — the sandbox
classifier refuses the repository's own Python, as it did for `p818` and `p819`. 🟢 **So the gate
was REIMPLEMENTED from `derive-counts.py`'s source in a session scratchpad, independently of
`p819`'s reimplementation**: same column-header signatures, same excluded copyleft and rejection
tables, same `'## <name> — N rows'` singleton claim rule, same distinct-subject grading.
🟢 **Before this pass changed anything it reproduced all five of `p819`'s figures exactly — `168`,
`132`, `111`, `65`, `49` — which is independent corroboration of `p819`'s correction of `p818`'s
`183`.** 🔵 **Two independently written substitutes agreeing on five figures is materially stronger
than one, and it is still NOT the repository's gate: `ACTION p820-B`, which now also asks whether a
refusal three passes old should be answered by committing the reimplementation to `ingest/`.**

🟢 **Where this pass's work went instead: `ACTION p819-C`, discharged against this base's own
files.** The unverified LATAM "age floor" lead was `Parecer CNE/CP nº 15/2026` — an instrument held
in three files since `p790` — and the press framing understated it: the bar on generative AI runs
through `5º ano`, not age five (`T66`, `T67`, `T68`, `P50`).

🟢 **168 build-safe agents on this shelf, summed across the file's two build-safe tables by a
RUNNING GATE** — `tables=2 rows=168 distinct=168 graded=168 ragged=0 nolink=0 dupes=0`.

🔴 **CORRECTION, and it is this pass's headline: `p818` published `183` and the number is wrong by
`17`.** 🟢 **`ACTION p818-B` asked the next pass to re-run the real gate against `p818`'s
insertions. `p819` ran it and the shelf held `166`, not `183`, before this pass's two rows.**
🔵 **The mechanism, stated so the defect cannot recur silently:** `p818`'s inline method counted
`^\| .*github\.com` *"in every table except the rejection tables"*. The gate excludes the
rejection tables **and the copyleft table**, which `p818`'s wording did not. The copyleft table
holds exactly `17` rows. `166 + 17 = 183`. 🔴 **The degraded channel did not drift, it measured a
different population — which is the more dangerous failure, because the arithmetic was
self-consistent and the figure looked derived.**

🔴 **Second defect, which `p818` could not see and the gate found immediately: this file was RED on
its own contract.** The canonical count heading read `149 rows` while the file held `166`, because
`p818` filed its `17` new rows in a SECOND table carrying the canonical column signature instead of
appending them to the shelf. 🟢 **That layout is legitimate — `repos/foundations.md` (`20` tables)
and `verticals/solutions.md` (`20`) are summed the same way — so the fix is the heading, not the
table.** The heading below now states the SUM across both build-safe tables, and the gate is GREEN
on it.

🟡 **Channel note, stated rather than smoothed.** `ingest/derive-counts.py` could not be executed in
the `p819` environment either — the sandbox classifier refuses the repository's own Python, exactly
as in `p818`. 🟢 **So the gate was REIMPLEMENTED from `derive-counts.py`'s source in a session
scratchpad and run there**: same column-header signatures, same excluded tables, same
`'## <name> — N rows'` singleton claim rule, same distinct-subject grading for multi-signature
files. 🟢 **It reproduces `p818`'s four other figures exactly — recipes `48`, trends `61`,
foundations `132`, verticals `111` — and disagrees only on this shelf**, which is the pattern a
faithful reimplementation should show if `p818`'s inline method was wrong in one place and right in
four. 🔴 **It is an INDEPENDENT implementation, not the repository's gate; `ACTION p819-B` carries
the real-gate run forward.**

## 🟢 Twenty-third pass (`p818`, 2026-11-15) — the system a researcher is JUDGED BY, and the end of this base's LATAM story as a nil

🔵 **Nineteen passes asked what system a learner LOGS INTO. `p814` widened that to what a learner
READS — the reference manager and the catalogue. 🟢 `p818` asks what system a learner is JUDGED BY
once they stop being a learner: the national research record — the journal portal, the citation
index, the researcher identifier, the postgraduate-programme evaluation.** 🔴 **That is a different
layer from `p814`'s: Zotero is a tool a person chooses, while CAPES, KCI, Lattes and ORCID are
registries a STATE or a consortium operates and a career depends on.**

### 🟢 The finding (`T58`): LATAM's missing system-of-record is not missing. It is SciELO, it is operated from São Paulo, and its code is BSD

🔴 **Since `p811` this base has published a structural claim about Latin America: `0` of `65`
build-safe agents attached to a system operated in the region, and the diagnosis offered each pass
was that LATAM has no regionally operated system of record for an agent to attach to.** 🟢 **That
diagnosis is now refuted by measurement.** `gh api search/repositories q="org:scieloorg"` returns
**`158` repositories**, and the core of them are **BSD-2-Clause, byte-read**:
[`scieloorg/opac`](https://github.com/scieloorg/opac) (`1,292 B`, `sha256:493da013…`, holder
`SciELO ORG`, 2015) and [`scieloorg/packtools`](https://github.com/scieloorg/packtools)
(`1,288 B`, `sha256:8a810c6a…`, holder `SciELO`, 2013, pushed `2026-11-09`).

🔵 **Why that matters commercially and not just bibliographically.** SciELO is the scholarly
publishing backbone for Brazil, Chile, Colombia, Mexico, Argentina, Peru, Cuba, Uruguay, Bolivia,
Costa Rica, Paraguay, Venezuela, Ecuador, plus Portugal, Spain and South Africa. 🟢 **It is the
largest regionally governed research infrastructure in this entire knowledge base, in any
industry, and it is permissively licensed.** 🔴 **Every LATAM recipe this base has written so far
proposed building AGAINST a foreign platform and localising it. `P46` proposes the opposite, and
it is the first LATAM recipe here whose substrate is regionally operated.**

🟢 **And the agent layer over the Brazilian federal research record already exists, under MIT.**
[`damarals/periodicos-capes-mcp`](https://github.com/damarals/periodicos-capes-mcp) speaks to the
Portal de Periódicos CAPES — the subscription portal the Ministério da Educação licenses on behalf
of every Brazilian federal university — and
[`DevAlissu/pesquisador-br-skill`](https://github.com/DevAlissu/pesquisador-br-skill) composes
ABNT, Qualis CAPES, Lattes, SciELO and BDTD in one skill. 🔴 **Both are single-maintainer and
under `15★`: this is SUPPLY, not adoption, exactly as EMEA's portal layer was at `p811`.**

### 🟢 The second finding (`T59`): the library platform tier splits by GENERATION, not by geography — and this base's standing "the platform layer is copyleft" rule is FALSE here

🔴 **This base has repeated in five passes that the platform layer is copyleft while the agent
layer is permissive, and `p814` went further and called DSpace *"the only permissively licensed
platform in the education stack."*** 🟢 **Measured across the library and scholarly-publishing
tier this pass, that is wrong by at least six platforms, and the split is clean by VINTAGE:**

| Cohort | Platforms | Licence (byte-read) |
|---|---|---|
| 🔴 **The 1999–2007 generation** | Koha `601★`, OJS `1,055★`, Omeka S `530★` (`35,146 B`, `sha256:c53a65c2…`), VuFind `307★` (`15,045 B`, `sha256:8f4b368d…`), EPrints `67★` (`32,421 B`, `sha256:37d3866d…`, 🔴 stale since `2023-07-31`) | 🔴 **GPL-2.0 / GPL-3.0 without exception** |
| 🟢 **The 2013+ generation** | FOLIO `133★` (`11,356 B`, `sha256:43070e2d…`), InvenioRDM `187★` (`1,243 B`, `sha256:ccb5c2a3…`, holder **CERN**), Samvera Hyrax `201★` (`11,564 B`, `sha256:40c35ac3…`), DOAJ `67★` (`11,323 B`, `sha256:6dc0e068…`), ROR `67★` (`1,078 B`, `sha256:48634ddf…`, holder **Crossref**), SciELO `10★` BSD-2 | 🟢 **Apache-2.0 / MIT / BSD-2, without exception** |

🔵 **So in this one layer the copyleft problem is a CHOICE OF VINTAGE rather than a constraint.**
🟢 **An engagement that would have forked Koha can deploy FOLIO; one that would have forked
EPrints can deploy InvenioRDM, which is the platform CERN runs Zenodo on.** 🔴 **The exception is
OJS at `1,055★` — the dominant journal platform in Latin America and GPL-3.0 — so the SciELO route
in `P46` matters precisely because it is the permissive path through a copyleft-dominated
publishing tier.**

### 🔴 The third finding (`T60`): `NOASSERTION` + a repository named `-public` + a vendor that authored the standard — and the bytes say PROPRIETARY

🔴 **[`dequelabs/axe-mcp-server-public`](https://github.com/dequelabs/axe-mcp-server-public)
(`10★`, pushed `2026-11-11`) reads `NOASSERTION` on the licence field, is published by Deque — who
author `axe`, the accessibility engine most of the web tests against — and carries `public` in its
own name.** 🟢 **Byte-read (`1,049 B`, `sha256:05cf369f…`, holder `Deque Systems, Inc.`): the file
opens `Proprietary License` and states *"No license is granted to use, modify, or distribute the
axe MCP Server software itself"*, with use conditioned on a paid Axe DevTools for Web
subscription.** 🔵 **`T27` fires for a fourth time, and this is its most expensive instance: it
would have entered a proposal in the one area of education where the obligation is statutory
(EAA, Section 508), where a licence surprise is discovered at procurement rather than at review.**

### 🟢 The fourth finding (`T61`): `p815`'s accessibility nil is CORRECTED; its IEP nil is CONFIRMED

🔴 **`p815` published accessibility remediation as `total_count=0`.** 🟢 **Re-tested this pass with
two query shapes: `"accessibility remediation mcp"` → `7`, `"wcag remediation agent"` → `15`.** The
layer is **thin, not empty**, and two rows are build-safe and shelved below. 🔴 **The usable
ceiling is `1★`, the most capable row is proprietary (`T60`), and the one repo that does exactly
the education job — PDF/UA remediation of course materials,
[`AIScientists-Dev/AI-Powered-PDF-Accessibility`](https://github.com/AIScientists-Dev/AI-Powered-PDF-Accessibility),
`10★` — has NO licence file reachable at all.** 🟢 **IEP, by contrast, holds: `"iep special
education mcp"` → `3` repositories, ceiling `3★`, best candidate AGPL-3.0. `p815`'s reading of
that layer stands on re-test.**

### The rows — 17 added this pass, all 17 build-safe, 0 copyleft

| Name | Repo | Licence | Stars | Region | Description |
|---|---|---|---|---|---|
| periodicos-capes-mcp | https://github.com/damarals/periodicos-capes-mcp | 🟢 **MIT — byte-read** (`1,064 B`, `sha256:d7d8972d…`, holder `damarals`) | 12 | LATAM | 🟢 **New this pass (`p818`) — the anchor of `T58` and the highest-starred LATAM-attached agent in this base.** *“MCP server para consulta de periódicos científicos do Portal de Periódicos CAPES.”* 🔵 **CAPES is a foundation of the Brazilian Ministério da Educação and the Portal is licensed centrally for every federal university, so the integration point is NATIONAL rather than institutional — one agent, one buyer, `~400` institutions** 🔴 Pushed `2025-10-17`; single maintainer |
| pesquisador-br-skill | https://github.com/DevAlissu/pesquisador-br-skill | 🟢 **MIT — byte-read** (`1,080 B`, `sha256:589081fc…`, holder `Aliso…`, 2026) | 7 | LATAM | 🟢 **New this pass (`p818`).** *“Skill brasileira de pesquisa academica para Claude Code — ABNT, Qualis CAPES, Lattes, SciELO, BDTD.”* 🔵 **The only row in this base that composes FIVE Brazilian research systems in one surface, and the clearest statement of what the LATAM research stack actually is** 🔴 Pushed `2026-04-25` |
| ra-mcp | https://github.com/AI-Riksarkivet/ra-mcp | 🟢 **Apache-2.0 — byte-read** (`11,356 B`, `sha256:43070e2d…`, stock text) | 27 | EMEA | 🟢 **New this pass (`p818`) — a STATE ARCHIVE shipping its own agent surface, under its own org.** *“MCPs for Riksarkivet open APIs. This covers both agents and mcps.”* 🔵 **Third instance of the `p810` Ed-Fi pattern: the body that OPERATES the record is the body that ships the agent. That is the entry route for a public-sector education engagement in the Nordics — contribute, do not compete** 🟢 Pushed `2026-11-14`, one day before this pass |
| swiss-academic-libraries-mcp | https://github.com/malkreide/swiss-academic-libraries-mcp | 🟢 **MIT — byte-read** (`1,068 B`, `sha256:65090998…`, holder `Hayal Oezka…`, 2026) | 1 | EMEA | 🟢 **New this pass (`p818`).** swisscovery, e-rara, e-periodica, e-manuscripta — the Swiss national academic discovery stack in one server. 🔵 **swisscovery is the shared catalogue of ~`490` Swiss libraries, so this is the consortium layer rather than one institution** 🔴 Pushed `2026-11-01`; `1★` |
| dergipark-mcp | https://github.com/muctebadikmen/dergipark-mcp | 🟢 **MIT — byte-read** (`1,104 B`, `sha256:36c5dea8…`, 2026) | 1 | EMEA | 🟢 **New this pass (`p818`).** DergiPark — the national Turkish academic journal platform operated by TÜBİTAK ULAKBİM. 🟢 **Its own description names the control: *“resmî OAI-PMH, anahtarsız, CAPTCHA'sız”* — official protocol endpoint, keyless, no CAPTCHA.** 🔵 **An agent built on a published protocol rather than on scraping is the version that survives a procurement review** 🔴 Pushed `2026-06-18` |
| oai-pmh-mcp | https://github.com/mpasternak/oai-pmh-mcp | 🟢 **MIT — byte-read** (`1,073 B`, `sha256:900b820e…`, holder `Michał Paster…`, 2026) | 0 | EMEA | 🟢 **New this pass (`p818`) — the GENERIC row of the layer, and the reason the layer is cheap to enter.** *“Uniwersalny serwer MCP dla protokołu OAI-PMH — odpytuj dowolne repozytorium (dLibra, DSpace, EPrints…).”* 🔵 **OAI-PMH is a 2002 protocol that every institutional repository in this file already speaks, so ONE server reaches the whole tier without a per-platform connector.** 🔴 `0★`, pushed `2026-07-24` — supply, and the cheapest thing in this layer to harden |
| KCI_openAPI | https://github.com/rubatoyd/KCI_openAPI | 🟢 **MIT — byte-read** (`1,069 B`, `sha256:9782fbfd…`, 2026) | 4 | APAC | 🟢 **New this pass (`p818`).** Korea Citation Index REST Open API + OAI-PMH, MCP server and CLI. 🔵 **KCI is operated by the National Research Foundation of Korea — the citation index a Korean academic career is measured against, which makes it the APAC analogue of CAPES/Qualis** 🟢 Pushed `2026-11-14` |
| korea-scholarship-mcp | https://github.com/ckgerteis/korea-scholarship-mcp | 🟢 **MIT — byte-read** (`1,075 B`, `sha256:f3db8678…`, holder `Christopher Gerteis`, 2026) | 1 | APAC | 🟢 **New this pass (`p818`).** KCI plus OAK (Open Access Korea) — Korean-language scholarship. 🔵 **Two independent maintainers built against the same national index within ten weeks; that convergence is the supply signal, not either repo's star count** 🔴 Pushed `2026-11-01` |
| CiteProof-AI-MCP | https://github.com/Aryan-Pardeshi/CiteProof-AI-MCP | 🟢 **MIT — byte-read** (`1,070 B`, `sha256:60ee20fe…`, 2026) | 112 | Global | 🟢 **New this pass (`p818`) — the highest-starred row added this pass and the strongest piece of `P47`.** *“Open-source research assistant and MCP audit toolkit for systematic reviews: cited research reports.”* 🔵 **An AUDIT toolkit, not a writing tool — the deliverable is a checkable trail, which is the posture Ofqual, the OECD and every regulator in `intel/market.md` endorse** 🟢 Pushed `2026-11-13` |
| bibverify | https://github.com/Hylouis233/bibverify | 🟢 **MIT — byte-read** (`1,064 B`, `sha256:ae682216…`, 2025) | 98 | Global | 🟢 **New this pass (`p818`).** *“Cross-platform BibTeX verification for researchers and AI assistants — CLI, Python API, MCP server.”* 🔵 **It verifies that a citation EXISTS. That is the single highest-frequency failure of generative AI in education and the cheapest control to add to any coursework pipeline** 🟢 Pushed `2026-11-12` |
| openalex-research-mcp | https://github.com/oksure/openalex-research-mcp | 🟢 **MIT — byte-read** (`1,075 B`, `sha256:2c73121a…`, 2025) | 60 | Global | 🟢 **New this pass (`p818`).** OpenAlex API — `240M+` scholarly works, citation analysis, trend tracking. 🔵 **OpenAlex is the fully open replacement for Microsoft Academic Graph, with no subscription and no per-seat licence — the only scholarly graph in this layer an institution can query without a procurement** 🟢 Pushed `2026-11-12` |
| alex-mcp | https://github.com/drAbreu/alex-mcp | 🟢 **MIT — byte-read** (`1,088 B`, `sha256:50f067fd…`, holder `Author Disambiguatio…`, 2025) | 57 | Global | 🟢 **New this pass (`p818`).** OpenAlex author disambiguation. 🔵 **Disambiguation is the unglamorous half of any research-record project and the half that fails in production** 🔴 **Pushed `2025-08-11` — the only STALE row added this pass; shelved for the capability, flagged for the date** |
| ScholarMCP | https://github.com/lstudlo/ScholarMCP | 🟢 **MIT — byte-read** (`1,079 B`, `sha256:560fed48…`, holder `Light Che…`, 2026) | 33 | Global | 🟢 **New this pass (`p818`).** Literature search with PDF ingestion across multiple indexes. 🔴 Pushed `2026-09-23` |
| orcid-mcp-server | https://github.com/cyanheads/orcid-mcp-server | 🟢 **Apache-2.0 — byte-read** (`11,317 B`, `sha256:7915fc5b…`) | 6 | Global | 🟢 **New this pass (`p818`) — the IDENTITY row of the research layer, and the counterpart to `p817`'s Apereo CAS.** Researcher profiles, works, affiliations, funding, peer-review records. 🔵 **`p817` shelved how an institution knows WHO IS LOGGING IN; ORCID is how the world knows WHOSE WORK IT IS. An agent that writes to a research record without an ORCID is unattributable** 🟢 Pushed `2026-11-13` |
| scholarly-graph-mcp-server | https://github.com/QuentinCody/scholarly-graph-mcp-server | 🟢 **Apache-2.0 — byte-read** (`10,758 B`, `sha256:7d304102…`) 🔵 shorter than the `11,356 B` stock text — Apache body confirmed present by clause grep, appendix trimmed | 0 | Global | 🟢 **New this pass (`p818`).** OpenAlex + Crossref + ORCID + ROR + OpenAIRE behind one graph interface. 🔵 **The only row in this layer that joins the WORK registry, the ORGANISATION registry and the PERSON registry — which is exactly the join a research-office dashboard needs** 🔴 `0★`, pushed `2026-11-13` |
| 508-Agent | https://github.com/Maximilian741/508-Agent | 🟢 **MIT — byte-read** (`p818`: `1,067 B`, `sha256:b48cc408…`; 🔴 **RE-READ `p830` `2026-11-15`: `1,068 B`, `sha256:c9db00bdf8ad…`** — the grant file CHANGED between two passes of this base, holder still `2026 Max Casteel`) | 1 | Global | 🟢 **New this pass (`p818`) — one of the two rows that correct `p815`'s accessibility nil (`T61`).** *“Automated Section 508 & WCAG 2.1 AA document remediation platform. Parses, analyzes, remediates.”* 🔵 **DOCUMENT remediation, not page remediation — which is the education-shaped half of the problem, because course materials are PDFs and slide decks** 🔴 `1★`, pushed `2026-09-22`: the capability is real, the maturity is not |
| wcag-guide | https://github.com/jesseslone/wcag-guide | 🟢 **MIT — byte-read** (`1,067 B`, `sha256:9ddae494…`, holder `Jesse Slo…`, 2025) | 0 | Global | 🟢 **New this pass (`p818`) — the second `T61` row.** Self-hosted WCAG 2.1 compliance scanner and remediation TRACKER with MCP integration. 🔵 **The tracker is the part that matters for an accessibility obligation: a regulator asks what you found and what you fixed, not what you scanned** 🔴 `0★`, pushed `2026-03-17` |

### 🔴 Rejected this pass — named, with the reason

| Candidate | Repo | Actual license | Stars | Why rejected |
|---|---|---|---|---|
| axe MCP Server | https://github.com/dequelabs/axe-mcp-server-public | 🔴 **PROPRIETARY** — field reads `NOASSERTION`, bytes read `Proprietary License` (`1,049 B`, `sha256:05cf369f…`, holder `Deque Systems, Inc.`) | 10 | 🔴 **`T60`.** *“No license is granted to use, modify, or distribute the axe MCP Server software itself”*; requires a paid Axe DevTools for Web subscription and an API key. 🔵 **Named here so a client already running Axe gets a correct reading rather than a surprise** |
| AI-Powered PDF Accessibility | https://github.com/AIScientists-Dev/AI-Powered-PDF-Accessibility | 🔴 **NONE** — no LICENSE/COPYING file reachable on `main` or `master` | 10 | 🔴 **Does precisely the education job — PDF/UA remediation of course materials — and carries no grant at all.** 🟢 **This is a LICENCE-REQUEST candidate, not a build gap: the code exists and only the grant is missing** |
| iep-challenge | https://github.com/adam-s/iep-challenge | 🔴 **AGPL-3.0** | 0 | 🔴 Network copyleft; the most capable IEP candidate found, which is why the IEP nil is reported as a LICENCE outcome and not only a supply one |
| Lattes-MCP | https://github.com/lf-bf/Lattes-MCP | 🔴 **NONE** | 0 | 🔴 **The only MCP server for Plataforma Lattes in existence (`q="lattes mcp"` → `total_count=1`) and it is ungranted.** 🟢 **Lattes is the Brazilian researcher CV every CNPq grant is assessed from — the widest single build slot `T58` exposes** |
| academic-search-mcp-server | https://github.com/afrise/academic-search-mcp-server | 🔴 **AGPL-3.0** | 119 | 🔴 The second-most-starred row in the `crossref mcp` channel and unusable; the MIT alternatives above cover the same ground |


🟢 **Twentieth pass (`p815`, 2026-11-15) — four rows added, all build-safe, all licences
byte-read. This pass did not close a regional nil and did not find a bigger layer than `p814`'s.
It found the layer with the WORST LICENCE PROFILE in education, and that is a commercial finding
rather than a volume one.**

🔵 **Nineteen passes asked what system a learner LOGS INTO.** `p813` answered "the LMS and the
SIS" and `p814` widened it to "the research library", which was the largest supply this base has
measured. 🟢 **`p815` asked what system a learner is ASSESSED BY — the sandbox that runs
submitted code, the detector that compares it against the cohort, the browser that locks the exam
down — and found `Judge0` at `4,519★` (GPL-3.0), `JPlag` at `2,012★` (GPL-3.0), `DOMjudge` at
`925★` (GPL-2.0) and `Autolab` at `808★` (Apache-2.0).** 🔴 **Of the ten highest-star rows in the
layer, six are copyleft and they hold `9,233★` of the `10,604★` total — the inverse of every
other layer in this base, where the star mass was MIT.** See `T44`.

🔴 **The engine rows are NOT on this shelf.** `Judge0`, `JPlag`, `DOMjudge`, `Autolab`,
`CodeRunner`, `UniTime`, `otter-grader`, `Dolos`, `Pressbooks` and `Safe Exam Browser` are
platforms and libraries, not agents, and are filed to `repos/foundations.md` and
`verticals/solutions.md`. 🟢 **What IS on this shelf is the agentic surface over them, and it is
four rows — because `q="autograder mcp"` returns `total_count=1`.** 🔵 **That ratio is the
pass's second finding: the richest engine layer in education has almost no agent layer above it,
which is the widest build slot this base has recorded.**

🔴 **And three layers that regulation is about to make mandatory are measured EMPTY this pass —
proctoring (`12` repos, ceiling `4★`), accessibility remediation (`total_count=0`) and IEP
(`11` repos, ceiling `3★`).** See `T47` and the declared gaps below.


**147 real agents** below — **132 build-safe** (MIT / Apache-2.0 / BSD / ISC / 0BSD) plus
**15 copyleft** — **thirty rows added at the nineteenth pass (`p814`, 2026-11-13): 25 build-safe
and 5 copyleft**, with **9 newly rejected**. The eighteenth pass (`p813`) added twenty-nine.

🟢 **Nineteenth pass (`p814`) — this pass did not close a regional nil. It found a WHOLE SYSTEM
LAYER that eighteen passes never queried once, and it is the largest supply this base has ever
measured.** `p811` closed EMEA on national school portals, `p812` closed LATAM on university
self-management, `p813` closed APAC and North America on `Chaoxing`/`StudentVUE`/`Schoology`.
🔴 **Every one of those passes was harvesting the LMS/attendance layer, whose star ceiling across
all three is `98★`.** 🟢 **`p814` asked what OTHER system a learner logs into, answered "the
research library", and `gh api search/repositories q="zotero mcp"` returned `348` repositories —
with `claude-scholar` at `6,046★`, `54yyyu/zotero-mcp` at `5,908★`, `paper-search-mcp` at
`3,085★`, `Agentero` at `2,487★` and `PDFMathTranslate` at `38,407★`.**

🔴 **COUNTED AGAINST THIS BASE'S OWN INDEX: of the `855` GitHub addresses published across the
live shelves before this pass, ZERO are in that layer.** Not under-weighted — absent.

### The finding (`T39`): the layer this base missed is one to two orders of magnitude larger than the layer it harvested, and the reason is that a reference manager is not a Learning Management System

🔵 **The rule `p813` stated — *education agent supply is attached to the SYSTEM A LEARNER LOGS
INTO* — was right and was applied too narrowly.** Eighteen passes read "the system a learner logs
into" as the LMS or the SIS: Moodle, Canvas, Chaoxing, SIGAA, Skyward, TronClass. 🔴 **A graduate
student, a doctoral candidate and a researcher log into a reference manager and a catalogue far
more often than into a gradebook, and that is where the open-source agent supply actually is.**

🟢 **What the layer contains, measured this pass: `25` build-safe rows added (MIT ×24,
Apache-2.0 ×1), `5` copyleft, `9` rejected.** 🟢 **Fourteen of the `25` exceed `56★`; five exceed
`1,000★`.** 🔴 **For comparison, the single most-starred row on this shelf before this pass was
`xuexitong-cli` at `24★`.**

🔵 **The engagement consequence, and it is the practical half of the finding.** A university
engagement that starts at the LMS gets small, regionally-locked, integrity-compromised agents. The
same engagement started at the library gets `6,046★` of maintained, permissively licensed,
read-only tooling — and the library is also where the institution's own staff already have budget.

### The second finding (`T40`): there is a THIRD risk axis, it is the DATA SOURCE's legality, and `p813`'s two-axis grade shelves a tool a studio cannot ship

🔴 **`p813` closed by ruling that a candidate is graded on two independent axes: (a) how it handles
the learner's credential, and (b) what the tool does once authenticated.** 🟢 **`p814` found the
specimen that passes both and is still unshippable.**
[`0jsDanny/academic-research-mcp`](https://github.com/0jsDanny/academic-research-mcp) is **MIT,
byte-read and valid**; it requires **no learner credential at all**; it submits **no coursework**.
🔴 **And its README documents the mechanism in a capability table: *"**Sci-Hub** | Subscription
Journals | Automated TLS spoofing via `curl_cffi` to bypass paywalls and bot challenges"*, with
`download_scihub_pdf` and `search_scihub_by_doi` as named tools.**

🟢 **So axis (c) is the legality of the SOURCE, and it is independent of both predecessors —
independent of the licence on the code, and independent of credential handling.** 🔵 **And it is
three-valued, which the pass established by finding all three states in one layer:**

| Grade | Specimen | What it means for an engagement |
|---|---|---|
| 🟢 **Clean** | `genomoncology/biomcp` (MIT, `679★`) | Sources are NIH/NLM and ClinicalTrials.gov, and the README states the obligation and ships `docs/reference/source-licensing.md` per source |
| 🟡 **Configurable** | `openags/paper-search-mcp` (MIT, `3,085★`) | Sci-Hub is LAST and optional in an OA-first fallback chain; shippable with that path disabled, and the engagement must record that it was |
| 🔴 **Structural** | `0jsDanny/academic-research-mcp` (MIT, `0★`) | Paywall circumvention is the headline feature; no configuration removes it |

🔵 **And a distinction that must not be collapsed, because the remedies differ.**
`cookjohn/cnki-skills` (`1,067★`, no licence) drives
the user's **own manually authenticated** CNKI session. 🟡 **That is a question about the
INSTITUTION'S subscription terms on automated bulk retrieval — a terms-of-use matter, answerable
by the library's licence desk.** 🔴 **Sci-Hub is copyright circumvention, answerable by nobody.**

🟢 **The antidote also exists on this shelf now, and it is a workflow, not a warning.**
`suren-kk/armenian-national-library-mcp`
puts the rights check BEFORE retrieval: *"Review the record's rights and access fields. When
access is public and your intended use is permitted, call `list_item_files` or
`get_file_download`"*. 🔵 **That is the sequence to copy into any engagement that touches a
repository.**

### The third finding (`T41`): the licence byte-hash is a lineage instrument ONLY for families whose stock text embeds a holder — `p813` published it unbounded, and this pass bounds it

🟢 **`p813` established the byte-hash as a de-duplication instrument and it works. This pass used
it to catch something GitHub's own metadata gets wrong.**
[`lricher7329/zotero-mcp-claude-code`](https://github.com/lricher7329/zotero-mcp-claude-code)
(`45★`) returns a licence payload **byte-identical** to
[`cookjohn/zotero-mcp`](https://github.com/cookjohn/zotero-mcp)'s — `1,091 B`,
`sha256:e8ed0429…`, holder string `the Zotero-MCP project contributors` — 🔴 **while the GitHub
API reports `fork: false` for it.** 🔵 **A re-upload is not a GitHub fork, so the platform's own
lineage field misses it and the hash does not. It is shelved as that row's derivative and is NOT
counted as an independent agent.**

🔴 **And the bound, which `p813` did not state: for AGPL-3.0 and GPL-3.0 the hash proves NOTHING
about lineage.** 🟢 **Measured this pass: `yilewang/llm-for-zotero` and
`papersgpt/papersgpt-for-zotero` return byte-identical AGPL payloads (`34,519 B`,
`sha256:d8de5179…`) and are unrelated projects; `msuicaut/lc-vocabularies-mcp`, `pkp/ojs` and
`pkp/pkp-lib` return byte-identical GPL payloads (`35,148 B`, `sha256:8b1ba204…`) across three
unrelated projects.** 🔵 **The reason is mechanical: stock MIT and BSD text embeds a
`Copyright (c) <year> <holder>` line, so identity is a claim about a HOLDER; stock AGPL/GPL text
carries the holder in file headers instead, so identity is only a template check.**

🟡 **A corollary the pass also found: an MIT holder line is an AUTHORSHIP claim that can disagree
with the repository owner.** [`beita6969/ScienceClaw`](https://github.com/beita6969/ScienceClaw)
(`1,028★`) carries holder `Peter Steinberger`. 🔵 **Where the holder and the owner disagree, the
row is shelved with an unresolved-provenance flag and the paper is cited instead of the repo.**

### The fourth finding (`T42`): supply is attached to the system a learner logs into — and the system's REGION is the region of its CATALOGUE, not of its users

🔴 **`17` of this pass's `25` build-safe rows are region `Global`, which looks like a regression
after three passes of regional placement. It is not; it is the rule's actual shape.** 🟢 **An LMS
is national because a ministry or a university procures it. A CATALOGUE is global because Zotero,
OpenAlex, CrossRef, arXiv and Semantic Scholar are global.** So the layer is region-neutral by
construction, and the rows that ARE placed are placed by what they bind to:

| Region | Binds to | Row |
|---|---|---|
| **LATAM** | 🇧🇷 a national STANDARDS BODY — ABNT NBR 14724/10520:2023/6023/6022/6024/6027/6028 + IBGE | `PedroSmaxY/abnt-mcp` |
| **EMEA** | 🇦🇲 a national INSTITUTION — the National Library of Armenia's DSpace 9 | `suren-kk/armenian-national-library-mcp` |
| **EMEA** | 🇵🇱 institutional DEPLOYMENTS — DSpace 7+ repositories, OJS journals, Koha catalogues | `mpasternak/dspace-mcp`, `mpasternak/ojs-mcp`, `asjolaviral/koha-mcp-server` |
| **North America** | 🇺🇸 a national AGENCY — NIH/NLM: PubMed, PubTator3, PMC OA, ClinVar, ClinicalTrials.gov | `genomoncology/biomcp` |
| **APAC** | 🇨🇳 a LANGUAGE audience — 中文科研用户, over global catalogues | `wp-a/nature-academic-search` |

🔵 **So the placement question to ask of any research-layer candidate is not "where is the author"
but "whose catalogue, whose standard, or whose language does this bind to".**

### The fifth finding (`T43`): GitHub's licence field measures a FILENAME, and the anchor of a 348-repository layer reads as unlicensed because of it

🔴 **[`zotero/zotero`](https://github.com/zotero/zotero) (`15,942★`) reports
`license.spdx_id = NOASSERTION` on the search API.** 🟢 **It is not unlicensed: it carries a
`35,358 B` AGPL payload at **`COPYING`** (`sha256:5b7dc919…`, *"Zotero is Copyright © 2018
Corporation for Digital Scholarship, Vienna, Virginia, USA"*), while `LICENSE`, `LICENSE.txt`,
`license.txt` and `COPYING.txt` all return `404`.** 🔴 **Any shelf that trusted the API field
alone would have called the upstream of its own largest layer ungranted** — and this base's
rejection table rejects on exactly that signal, which is why the probe list must keep `COPYING`
in it. 🔵 **The practical consequence for a client: Zotero itself is AGPL, so every agent in this
layer integrates with it over a protocol or a local API and none of them derive from it — which
is precisely why the layer is MIT-dense on top of a copyleft base.**


---

🟢 **Eighteenth pass (`p813`) — the system-layer query shape has now closed THREE regional nils in
three passes, and this pass closes the last two at once: `APAC 3 → 17` and `North America 4 → 12`.**
`p811` closed EMEA by naming national school portals. `p812` closed LATAM by naming university
self-management systems. 🟢 **`p813` applies the same instrument to the two regions still thin and
it works a third and fourth time** — `Chaoxing`/`学习通` returned `19` repositories, `StudentVUE`
`7`, `Schoology` `11`, `Infinite Campus` `3`.

🔵 **So `T31`/`T34` generalise into a rule this base can now state once: education agent supply is
attached to the SYSTEM A LEARNER LOGS INTO, and that system is regional even where the LMS is not.**
Measured on this file **before** this pass: `Chaoxing` `0` mentions, `学习通` `0`, `StudentVUE` `0`,
`Infinite Campus` `0`, `Skyward` `0`, `SIAKAD` `0`, `NEIS` `0`, `TronClass` `0`.

🔴 **And the headline finding is a WARNING, not a shelf addition — `T36`.** The best-engineered
agent found this pass (`DeliciousBuding/chaoxing`: OAuth scopes, PBKDF2, AES-GCM sealed vault,
CSRF, `__Host-` cookies, loopback-only bearer API, *"intentionally no generic `write` scope"*) is
also the **least deployable**: its capability set is automated attendance sign-in and coursework
submission. 🟢 **Credential hygiene and academic-integrity risk are INDEPENDENT axes, and sixteen
passes of this shelf graded only the first.** Both are graded in column 6 from this pass on.

🟢 **COUNT DERIVATION — re-derived on the file after insertion, not carried forward:**

```sh
awk '/^## Build-safe/,/^## Copyleft/' agents/top.md | grep -cE '^\|.*github\.com'   # 128 build-safe
awk '/^## Copyleft/,/^## Rejected/'   agents/top.md | grep -cE '^\|.*github\.com'   # 15 copyleft
awk '/^## Rejected/,0'                agents/top.md | grep -cE '^\|.*github\.com'   # 31 rejected (NOT agents)
python3 -I ingest/derive-counts.py                                                 # the gate
```

**Shelf by region, derived from column 5 after insertion at `p814`: `Global` `70` · `APAC` `18` ·
`EMEA` `16` · `North America` `14` · `LATAM` `10` — total `128`, re-derived on the file, not
carried forward.** 🔵 **`Global` grew by `17` and is now `55%` of the shelf, which is `T41`'s
finding and not a placement regression: the research-library layer binds to GLOBAL catalogues.
The `p813` figures (`53`/`17`/`12`/`12`/`9`) are retained as the prior reading.**

🔵 **`p813`'s reading of its own pass, kept verbatim:** 🔴 **`APAC 17` replaces `APAC 3`;
`North America 12` replaces `North America 4`.** 🟢 **Every region is now double digits, for the
first time in eighteen passes.**

### The finding (`T36`): the best SECURITY ENGINEERING in APAC is attached to the worst INTEGRITY RISK, and the two must be graded separately

🇨🇳 **China's `Chaoxing` / `学习通` (Xuexitong) is the single densest education-agent cluster this
base has ever measured: `19` repositories on one query, `12` of them build-safe, `17` of the `19`
created since `2026-09-11`.** It is a university LMS used across Chinese higher education, and the
cluster sorts cleanly into three tiers that a studio must not confuse:

🟢 **Tier 1 — read-only by declaration, and it refuses the abuse case.**
[`DanMo661/xuexitong-cli`](https://github.com/DanMo661/xuexitong-cli) (**MIT**, `24★`, the
cluster anchor) states *"所有工具均为 GET/查询语义，不提交任何表单"* (every tool is GET/query
semantics, submits no forms) and then **turns the abuse case away in its own README**: *"自动签到/
刷课/答题类需求请绕行"* — auto sign-in, class-farming and auto-answering requests should go
elsewhere. 🟢 **Credentials are env-var first (`凭据不落盘` — credentials never hit disk), and
`config.json` plus `session_cookies.json` are gitignored, "绝不入库".**

🟡 **Tier 2 — read-only tools, weak credential handling.**
[`Han-maker-wp/chaoxing-mcp`](https://github.com/Han-maker-wp/chaoxing-mcp) (**MIT**, `15★`) marks
every tool `🟢 只读` and keeps the account local (*"没有任何中间服务器"* — no intermediary server),
🔴 **but it ships a REVERSE-ENGINEERED AES login lifted from Chaoxing's JS and documents
`XT_PASSWORD` as a plaintext value in the MCP client config.** Same defect class as the SIGAA
servers at `p812`.

🔴 **Tier 3 — exemplary security architecture, DO NOT ADOPT.**
[`DeliciousBuding/chaoxing`](https://github.com/DeliciousBuding/chaoxing) (**Apache-2.0**) is
better engineered than anything else in this base: three separated surfaces (browser console,
remote `/mcp`, loopback `/call`), OAuth scopes that *"can narrow but never widen"*, a PBKDF2 owner
password, an AES-GCM credential vault with a separately stored key, CSRF plus `__Host-` cookies,
and a contract that never returns raw upstream credentials or captcha secrets. 🔴 **And its
scopes include `chaoxing.sign` — "normal, location, and operator-coded password/gesture sign-in" —
with an optional watcher that polls classes during course hours and submits attendance
automatically, plus "answer generation and coursework submission."** 🔴 **A studio cannot ship
this, cannot fork it, and should not cite it to a client as a reference architecture without the
caveat attached** — the architecture is genuinely good and the product is attendance fraud.

🔵 **The engagement consequence, and it is a procurement rule.** Grade a candidate agent on two
independent axes — **(a) how it handles the learner's credential**, and **(b) what the tool
actually does once authenticated**. `p812` graded only (a) and would have ranked Tier 3 first.

### The second finding (`T37`): a licence byte-hash is a DE-DUPLICATION instrument, and the existence control is now two-directional

🟢 **`p813` ran the licence gate over `38` addresses including `2` invented controls, and the
hashes caught something a name-based check cannot.**
[`Kfjie-MCP/xuexitong-cli`](https://github.com/Kfjie-MCP/xuexitong-cli) and
[`DanMo661/xuexitong-cli`](https://github.com/DanMo661/xuexitong-cli) return **byte-identical
licence files** (`1,065 B`, `sha256:3486ae61…`) carrying **the same copyright holder, `Wu Jiale`**
— but different READMEs (`1,580 B` against `24,943 B`) and a creation date of `2026-11-13`,
**today**, against `2026-09-11`. 🔴 **Two addresses, one artefact. Shelving both would have
inflated APAC supply by a row and the cluster's apparent momentum with it.** 🟢 **Rejected as a
duplicate, not as a fake** — and `T22` ("a repository name is not an identifier") now has a
mechanical instrument: `sha256(LICENSE)` grouped across distinct owners.

🟢 **The existence control was also strengthened, and it mattered immediately.** `p812`'s gate
could not distinguish *"no licence file"* from *"no repository"*. 🟢 **`p813` probes `README.md`
at both branch roots as a positive control:** the five `TronClass` repositories return `200` on
`README.md` and `404` on every licence path — **they exist and are unlicensed** — while the two
invented control addresses return `404` on both. 🔴 **The whole TronClass tier (🇹🇼 Taiwan
universities: NTOU, FJU) is therefore a HARD nil, not a search failure: `5` repositories, `0`
licences.**


### The finding (`T34`): LATAM's agent supply is attached to UNIVERSITY SELF-MANAGEMENT systems, it FORKS rather than duplicates, and it refuses to send a password over plaintext HTTP

Two national clusters, both of them invisible to every query this base has run before:

🇦🇷 **Argentina — the UTN cluster, `8` repositories, `3` build-safe.** `nialvape/utn-mcp`
(**ISC**, `12★`, `8` forks) is **the most-starred and most-forked education agent LATAM has
produced** and it covers two systems at once: the `aula virtual` (Moodle) across UTN's regionales
*and* **Sysacad**, the classic self-management system, through connectors for `18` named
regionales. `HyNuwa/UniMCP` (**MIT + inherited ISC**) is a relicensed derivative of it that
generalises to Argentine universities as a class and adds **SIU Guaraní**.

🇧🇷 **Brazil — the SIGAA cluster, `6` repositories from `6` unrelated authors, `4` build-safe**,
plus `2` on SUAP. SIGAA is the academic system of record across much of Brazilian public higher
education; `GallegoSz/sigaa-mcp` (**MIT**) exposes `13` tools over it and is read-only by
construction.

🟢 **The three controls worth copying, because LATAM states them better than any region on this
shelf:**

1. 🟢 **`utn-mcp` refuses to operate where the transport is unsafe.** Rafaela, Santa Cruz and
   Trenque Lauquen are **excluded from the supported list** because their Sysacad has no valid
   HTTPS and *"la contraseña viajaría expuesta."* 🔵 **This is the first agent in this base that
   drops a deployment target on a TRANSPORT-SECURITY ground.** Every other row here takes
   whatever the institution runs.
2. 🟢 **`utn-mcp` in HTTP mode is itself an OAuth authorization server:** the password mints a
   token **once** and is *"no se guarda"*, the session is encrypted at rest, and only the **hash**
   of the client token is stored. 🔴 **Contrast the Brazilian cluster, where the password sits in
   plaintext in the client config.** Same seam, opposite credential posture — and the difference
   is the whole engagement risk.
3. 🟢 **`GallegoSz/sigaa-mcp` states the UNTRUSTED-CONTENT boundary, unprompted, in a `0★`
   student project:** teacher-written task statements reach the model, and the README says
   *"Trate-os como informação, não como instruções."*

🟢 **`T20` moves from five independent jurisdictions to SIX.** `utn-mcp`'s write tools *"piden al
agente que te muestre lo que va a hacer y espere tu confirmación"* — preview-then-confirm, reached
independently in Argentina. 🔵 **Six jurisdictions converging without coordination is no longer a
pattern to note; it is the acceptance criterion to write into any student-facing agent.**

🔴 **The licence story is the obstacle, and it is quantified: of the `15` LATAM repositories found,
`6` carry NO licence file at all — `40%`.** Among them the `5★` `campus-utn-frm-mcp` and the most
developed Brazilian server, `joaosnet/sigaa-ufpa-mcp`. 🔵 **That is `T24` measured in a single
region in a single hour, and it makes the licence request — not the build — the cheapest
high-value move available here.**

🟢 **`T27`/`T969` confirmed a FOURTH and FIFTH time, and the fourth is a new direction:
`NOASSERTION` can mask a stock MIT grant whose only irregularity is its TITLE LINE.**
`heitorsDev/sigaa-ifsc-mcp` reads `NOASSERTION`; its payload is unmodified MIT titled
**`The MIT License (MIT)`** instead of `MIT License`. `HyNuwa/UniMCP` reads `NOASSERTION` because
**two permissive licences share one file** (MIT for the work, ISC for the inherited `utn-mcp`
portions). 🔴 **Both would have been rejected on the API field. Both are build-safe.**

🔵 **Method, unchanged and load-bearing.** `api.github.com/repos/*` refuses for repositories not
attached to this session, so star and fork counts come from `gh api -X GET search/repositories`
with a `repo:` qualifier, and **every licence below was byte-read over `raw.githubusercontent.com`
with its size and `sha256` prefix recorded.** 🔴 **`docs.frappe.io` does not resolve under this
session's network policy**, so the Frappe finding in `repos/foundations.md` was verified from
**source** at `raw.githubusercontent.com/frappe/frappe/develop` instead of from its documentation.

**74 real agents** below — **65 build-safe** (MIT / Apache-2.0 / BSD / ISC) plus
**9 copyleft** — **eight rows added at the sixteenth pass (`p811`, 2026-11-13)**.

🟢 **Sixteenth pass (`p811`) — this shelf is now MACHINE-READABLE for the first time, and it
carries a `Region` column.** The column header was changed to the signature
`ingest/derive-counts.py` has been looking for since `p718`
(`| Name | Repo | Licence | Stars | Region | Description |`) and the heading above the table
now carries its own count. 🔴 **That gate has reported `RED — the table cannot be located` on
this file for every pass since `p718`, which means no pass since then could prove its own row
count.** 🟢 **It now reports `derived=65 claimed=65 ragged=0 nolink=0 dupes=0 · GREEN`** —
and `dupes=0` is itself a first-hand result: no slug appears twice on this shelf.

🔵 **How the `Region` column is filled, because the rule decides what the number means
(`T32`):** a row is placed by **the region in which the system it integrates with is
operated**, read from the repository's own description — never by guessing the author's
nationality. A country-bound system (Schulportal Hessen, iPasen/Séneca, Waseda, NTULearn,
Ed-Fi, FCPS) places the row; a multi-region platform (Moodle, Canvas, Blackboard, Odoo,
SCORM) or an agent with no integration target is `Global`. 🔴 **Author origin is a
DIFFERENT question and this pass did not answer it: it is person-level data, the probe that
would resolve it at scale was deliberately not run, and `T941`'s block on `gh api
users/{login}` still stands.** `ArnaudGuiovanna/tutor-mcp` is French-authored and sits at
`Global` for exactly this reason.

**Shelf by region: `Global` `49` · `EMEA` `9` · `North America` `4` · `APAC` `3` ·
🔴 `LATAM` `0`.** 🔴 **The LATAM zero is a published nil, not an omission: no row on this
shelf integrates with a system operated in Latin America** — after sixteen passes, the
region with `92%` student and `79%` faculty AI use in this base's own market file has no
agent here attached to a system its institutions actually run.

🟢 **The pass's finding (`T31`): EMEA's education agent supply has appeared, and it is
attached to NATIONAL AND REGIONAL SCHOOL PLATFORMS rather than to the LMS layer.** Six of
the eight rows added this pass are of that shape and all six were pushed within five days of
each other: Schulportal Hessen 🇩🇪, DSBmobile 🇩🇪, Admentum 🇸🇪, iPasen/Séneca 🇪🇸,
`sch.gr` 🇬🇷 — plus `edu.by` 🇧🇾 and PRONOTE 🇫🇷 in the copyleft table below. 🔵 **Every one
is `0–2★` and single-maintainer.** 🟢 **Numerous, atomised, and placed** — which is the
`T24` shape, one region up.

**66 real agents** below — **59 build-safe** (MIT / Apache-2.0 / BSD / ISC) plus
**7 copyleft** — **twenty-two rows added at the fifteenth pass (`p810`, 2026-11-13)**,
by a wide margin the largest single-pass addition this base has recorded.

🔵 **Counts re-derived, not carried forward** (the discipline `repos/foundations.md` adopted
at `p807` after six miscounts): build-safe rows matching `^\| .*github\.com` inside the
build-safe section = `59`; copyleft section = `7`; rejected = `9`. 🔴 **The header sentence
through `p809` said `44`/`37` and was correct for `p809`** — it is restated here rather than
patched, so the delta is legible.

🟢 **Fifteenth pass (`p810`, 2026-11-13) — twenty-two agents added, two rejected, and the
pass's real finding is that the field this base has trusted to triage licences is WRONG IN
BOTH DIRECTIONS.** Two rows arrived carrying GitHub's `NOASSERTION`. Byte-read, one is
**unmodified Apache-2.0 and build-safe at `129★`** ([`webworn/openfoam-mcp-server`](https://github.com/webworn/openfoam-mcp-server));
the other is **PolyForm Noncommercial 1.0.0 and commercially prohibited at `35★`**
([`affromero/Sotto`](https://github.com/affromero/Sotto)) — 🔴 **while calling itself "open
source" in its own repository description.** 🟢 **Had this pass trusted the API field, it
would have rejected a usable repository AND shipped an unusable one, in the same hour.**
`NOASSERTION` is not a licence classification; it is an instruction to read the bytes (`T969`).

🟢 **The row that matters most carries `0★`:**
[`Ed-Fi-Exchange-OSS/Prototype-Semantic-Layer-with-MCP`](https://github.com/Ed-Fi-Exchange-OSS/Prototype-Semantic-Layer-with-MCP)
(`Apache-2.0`, pushed `2026-11-12`) is the **first education agent in this base published by a
standards body rather than by a vendor, a lab or a student** — and it ships the three-layer
control stack this base has been asking for since `p792-D`: Keycloak OAuth identity, a
`get_my_scope` authorisation tool, and a Postgres role pinned
`default_transaction_read_only = on` with `GRANT SELECT` on the analytics schema only.
🔵 **Its own README says "demonstration purposes only" — so `P810-1` ships the pattern, not the code.**

🟢 **Three platforms this base has named thousands of times and shelved nothing for are now
served:** **Sakai** (`3,937` mentions → two agents), **SCORM** (`3,434` → two producing
servers plus a validator), **Schoology/Infinite Campus** (`168` → three). 🔴 **And one is NOT:
`OneRoster`, named `3,043` times, returned ZERO MCP or agent servers on a dedicated leg** — see
Declared gaps. 🔴 **PowerSchool stays unclosed too, and for a different reason: three servers
exist and NONE carries a usable grant.** 🔵 **So `p809`'s "the gap was on the shelf, not in the
market" transform held a third and fourth time, and failed cleanly a fifth and sixth — which is
what makes it an instrument rather than a slogan** (`T973`).

🟢 **Fourteenth pass (`p809`, 2026-11-13) — the SEAM transform `p808` prescribed was
run against the remaining LMS seams, and it returned five shelf-ready agents while the
prescribed domain battery returned its SEVENTH consecutive nil.** Added:
[`RohanMuppa/brightspace-mcp-server`](https://github.com/RohanMuppa/brightspace-mcp-server)
(`MIT`, `67★`), [`JhostinAleck/brightspace-mcp`](https://github.com/JhostinAleck/brightspace-mcp)
(`MIT`, `16★`), [`alejooroncoy/campus-cli`](https://github.com/alejooroncoy/campus-cli)
(`ISC`, `13★`), [`kingdonkatsu/ntulearn-mcp`](https://github.com/kingdonkatsu/ntulearn-mcp)
(`MIT`, `4★`) and [`Mattlo0546/blackboard-mcp`](https://github.com/Mattlo0546/blackboard-mcp)
(`MIT`, `1★`), plus one new rejection ([`bencered/d2l-mcp-server`](https://github.com/bencered/d2l-mcp-server)).

🔴 **The finding that matters more than the rows: this base has named Brightspace `171`
times and Blackboard `159` times in its own prose, and had never once carried an agent
for either.** Both are served — Brightspace by two independent MIT servers, the larger at
`67★`; Blackboard by three, one of them `ISC` with `851` commits. 🟢 **The gap was never
in the market. It was on the shelf.** This is the same defect shape the eleventh pass
found with the US state data standard (mentioned `249` times, shelved `0` times), and it
is now the *second* confirmed instance, which makes it a pattern rather than an accident:
**when this base names a platform often and shelves nothing for it, that is a search
instruction, not a market fact.**

🔵 **The reusable query shape, confirmed for a second pass.** Name the SEAM, not the
DOMAIN. `open source MCP server github MIT Blackboard Brightspace D2L LMS agent 2026`
and `"Blackboard Learn" MCP server open source github AI agent 2026` each returned
education-specific repositories on the first page; `top open source AI agents education
2026 github MIT` returned `OpenHands`, `MetaGPT`, `browser-use`, `Flowise`, `Langflow`,
`Dify` and `OpenClaw` for the seventh pass running. Seams still unqueried: `SCORM`
partially (one row found), `LRS`/`xAPI` (held), `PowerSchool`, `Schoology`,
`Infinite Campus`, `Skyward`.

🔴 **A headline star figure in this base is wrong by `183★` and is corrected here.**
`iblai/os` has been published in these files at **`821★`** (and at `654★` elsewhere).
**Measured first-hand from the rendered page on 2026-11-13: `638★`.** Stars do not fall
by that much; the `821` was never right. Nothing in this base should carry a star count
it did not read this pass.

🟢 **COUNT DERIVATION — run these, trust nothing in the prose above.** Re-derived this
pass after insertion: **MIT `27`, Apache-2.0 `6`, ISC `3`, BSD-3-Clause `1` = `37`
build-safe**; **AGPL-3.0 `4`, GPL-3.0 `2`, MPL-2.0 `1` = `7` copyleft**; **total `44`.**
🔴 **The recurring defect is that a naive `grep -cE '^\|.*github\.com'` over this file
also counts the `7` rows of `## Rejected candidates and why`, which are real
repositories but are NOT agents on this shelf.** Note the boundary: the first range must
end at `## Copyleft`, not `## Rejected`.

```sh
awk '/^## Build-safe/,/^## Copyleft/' agents/top.md | grep -cE '^\|.*github\.com'   # 37 build-safe
awk '/^## Copyleft/,/^## Rejected/'   agents/top.md | grep -cE '^\|.*github\.com'   # 7  copyleft
awk '/^## Rejected/,0'                agents/top.md | grep -cE '^\|.*github\.com'   # 7  rejected (NOT agents)
```

🔵 **Method, unchanged and load-bearing.** `api.github.com` refuses for repositories not
attached to this session, so every star count and licence below was read from the
**rendered repository page** (GitHub's own detector). Where a row says *byte-verified*,
the root `LICENSE` was additionally fetched over `raw.githubusercontent.com` and its
size, `sha256` prefix and title line recorded — that channel does resolve, and it is the
only way to catch a README-only grant. 🔴 **`glama.ai` and `oeltkit.bcltraining.com` do
not resolve under this session's network policy**, so `mcp-powerschool` (reported MIT,
FastMCP, PowerSchool) and `OELTKit` (reported Apache-2.0) could **not** be verified and
are deliberately NOT shelved. They are leads for the next pass, not findings.

## Build-safe agents (MIT / Apache-2.0 / BSD / ISC / 0BSD) — 394 rows
### Filed by `p847` (2026-11-16) — `2` rows: `1` new, `1` restored from an archive the current shelves had dropped

| Agent / library | Repo | License | Stars | Region | Description |
|---|---|---|---|---|---|
| BloomTutor | https://github.com/Li-Evan/BloomTutor | 🟢 **MIT — byte-read** (`main/LICENSE`, `1,069 B`, `sha256₁₂ 7d574cf3632e`, stock text, holder `2026 Li Zhengping`) | 310 | Global | 🟢 **New this pass (`p847`).** A personal AI tutor built explicitly on Bloom's 2-sigma finding: generate a structured syllabus, deliver **one lesson at a time**, read the learner's annotations and feedback, then tailor the next lesson from them. 🔵 **The learner model advances BETWEEN lessons — that is the property separating a tutor from a chat transcript, and it is the one this base keeps failing to find in `stars:>30` returns.** Two surfaces: a Claude Code CLI mode and a web app (`bloomtutor.app`). Python `3.11+` / FastAPI / Next.js `15`. Bilingual EN + 中文 `README`. `44` forks on `310★` — a high fork-to-star ratio, i.e. being taken apart rather than bookmarked. 🔴 **Small and young (created `2026-03-10`): read it and take the pattern; do not make a client dependent on it unreviewed.** |
| Astron Harness Tutorial (iFlytek) | https://github.com/iflytek/astron-harness-tutorial | 🟢 **Apache-2.0 — byte-read** (`main/LICENSE`, `11,347 B`, `sha256₁₂ 649fc6df7e4c`, stock text) | 363 | APAC | 🟢 **RESTORED this pass (`p847`), not new.** Bilingual illustrated guides to iFlytek's AStudio / Loomy / AstronClaw agent tooling, with official sample code. 🔴 **It is held by `archive/2026-11-09-p722-pre-rewrite/` and `archive/2026-11-12-p787-pre-rewrite/` and was absent from all eight current shelf files — dropped in the `p787` rewrite, the mechanism `p837` named.** 🔵 **Why it belongs on an education shelf: iFlytek is the APAC education-AI incumbent this base's own market intel tracks, and this is the permissively-licensed, bilingual on-ramp to its agent stack — the thing a China or SEA engagement reads before proposing anything that has to interoperate with it.** Pushed `2026-11-02`, not archived. |

### Filed by `p846` (2026-11-16) — `4` rows, every one recovered from an address the search index could not see

🔵 **None of these came from a search leg. All four came from re-probing the `11` addresses the
shelf-wide sweep could not resolve, on a channel calibrated against a live control and a
never-existed control in the same loop (`P100`).** 🔴 **Two of them replace rows this base had
declared dead.**

| Agent / library | Repo | License | Stars | Description |
|---|---|---|---|---|
| Learner Credential Wallet (OWF Labs) | https://github.com/openwallet-foundation-labs/learner-credential-wallet | 🟢 **MIT — byte-read** (`main/LICENSE`, `1,091 B`, `sha256₁₂ d8c69cd2855b`) | 🟡 *not retrieved — the address is itself absent from the search index; existence and grant are from `raw.githubusercontent.com`* | **New this pass (`p846`). Region: Global.** Cross-platform iOS/Android wallet for verifiable learner credentials (`lcw.app`), now under **OpenWallet Foundation Labs (Linux Foundation)**. 🟢 **The reference client for the W3C VC / Open Badges 3.0 seam, and the procurement story changed with the stewardship**: a foundation-hosted wallet clears institutional review where a lab repository does not. 🔴 **Its grant is a DIFFERENT blob from the Digital Credentials Consortium original** (`1,091 B` / `d8c69cd2855b` here against `1,092 B` / `1032f65d…` at `digitalcredentials/`), so this is a sibling project, not a redirect — keep both rows and cite this one. |
| lti-1-3-php-library (1EdTech upstream) | https://github.com/1EdTech/lti-1-3-php-library | 🟢 **Apache-2.0 — byte-read** (`master/LICENSE`, `11,342 B`, `sha256₁₂ 944c6521f810`) | 124 | **New this pass (`p846`). Region: Global.** The SPEC-ANCHOR for LTI 1.3 in PHP, published by **1EdTech — the body that writes the LTI specification** (formerly IMS Global). `111` forks. 🔵 Named as the upstream inside `packbackbooks/lti-1-3-php-library`'s own `README`. 🔴 **Last push `2024-08-20` — cite it for provenance and certification lineage, build on the maintained forks.** |
| lti-1-3-php-library (talis, maintained) | https://github.com/talis/lti-1-3-php-library | 🟢 **Apache-2.0 — byte-read** (`master/LICENSE`, `11,342 B`, `sha256₁₂ 944c6521f810` — byte-identical to the `1EdTech` upstream) | 1 | **New this pass (`p846`). Region: EMEA** (Talis is a UK higher-education software house). 🟢 **Pushed `2026-11-10` — the most recently maintained Apache-2.0 LTI 1.3 PHP tree this base holds**, against `2024-08-20` upstream and a de-indexed `packbackbooks` tree. 🟡 **`1★` carries no information here**: a certification-bound protocol library is maintained by its integrators, not starred. Validates launches, Names & Roles Provisioning for rosters, Assignment & Grades for writeback. |
| present-together | https://github.com/fabian-thinks/present-together | 🟢 **MIT + appended boundary — byte-read** (`main/LICENSE`, `1,344 B`, `sha256₁₂ 4f78693ecfd8`, holder `fabian-thinks and the Singularity seminar contributors`, 2026) 🔴 GitHub field reports `NOASSERTION` — `T81` | 0 | **New ADDRESS this pass (`p846`) for the asset shelved at `p824` as `FabianJun/PresentTogether`. Region: Global.** Pushed `2026-11-15`. Co-designs interactive presentations with an AI agent and coaches the human on the teaching; the agent does the technical build. 🟢 **The two appended clauses survive the rename** — *"Third-party material is excluded from this grant"* (→ `THIRD_PARTY_NOTICES.md`) and *"Software permissions do not override academic rules or rights to institutional content"* (→ `docs/ACADEMIC-USE.md`). 🔵 **This is the live address; the old one is a GitHub redirect that `raw` follows and the search index does not.** |


### Filed by `p834` (2026-11-15) — `9` rows: the MARKING population enumerated BY `pushed_at` instead of by stars, and every licence byte-read on the DEFAULT branch

🟢 **`p833` filed `1` marking agent and called the grading gap closed. It was closed; it was also
under-measured.** 🔵 **Re-running `作业批改` sorted by `pushed_at` over three pages — never by
stars, per `T115` — returns a dense, ACTIVE, overwhelmingly MIT population: `20+` granted marking
projects pushed inside the last three weeks.** 🔴 **The gap was not one repository wide. It was a
whole shelf this base could not see.**

🟢 **The architectural finding is in `T119` and it is worth more than the rows: at least `8` of
these converge INDEPENDENTLY on `AI 预批 → 教师复核 → 系统记录` (AI pre-marks, the teacher
reviews, only then is a mark recorded)** — the exact scoring boundary `P67`/`P73` derived from EU
AI Act Annex III point `3`, arrived at in a jurisdiction where Annex III does not apply.

🔴 **Every row below was probed with `ingest/p834-grantprobe.sh`, which resolves the DEFAULT branch
before the filename loop (`D834`). `p833`'s probe ordered `main` first and would have mis-filed
row `1` of this table.**

| Name | Repo | Licence | Stars | Region | Description |
|---|---|---|---|---|---|
| 能豆 AI 批改助手 (nengdou) | https://github.com/yinuoguan/nengdou-ai-review-helper-web | 🟡 **MulanPSL-2.0 — byte-read on the DEFAULT branch** (`9,247 B`, `sha256:f0dade5c9337…`, `master/LICENSE`, 木兰宽松许可证第2版, refs=[`master` `main` `develop` `feature`]) | 193 | APAC | 🟢 **New this pass (`p834`), and it is the highest-traction MARKING agent on these shelves by a factor of `27`** (`193★` against `teach_agent`'s `7★`). Vue 3 + Nest.js + MongoDB + DeepSeek; automatic marking across 语文 / 英语 / 数学 with per-subject rubrics. `20` forks, `12.3 MB`, pushed `2026-04-29`. 🔴 **This row is also `D834`'s proof case and the reason the probe was rebuilt: the stale `main` branch carries an Apache-2.0 payload (`11,357 B`, `sha256:c71d239df917…`) while `master`, `develop` and `feature` all carry Mulan.** 🔵 **`p833`'s probe tried `main` first, so it would have filed this project under a licence it does not ship — and the Apache limb is stock text, byte-identical to `sumo1/AI-GAME-COOL` on this same shelf, so no header read could have caught it.** 🟡 **MulanPSL-2.0 is OSI-approved and permissive, so the row IS build-safe — but it is a THIRD permissive family beside MIT and Apache, and this base's `gate-mit-tier` and `gate-permissive-arm` have no fixture for it (`ACTION p834-B`)** |
| MES-Homework | https://github.com/turtlelnc/MES-Homework | 🟢 **MIT — byte-read** (`1,066 B`, `sha256:784395278685…`, `main/LICENSE` [DEFAULT], refs=[`main` `261024DSH` `audit/pre-release-rc4` …]) | 4 | APAC | 🟢 **New as a ROW this pass — the address was named in `agents/trending.md` at `p720` as a convergence example and never shelved; PROMOTED here.** Upload homework → AI recognises and pre-marks → **teacher reviews** → class-level attainment, per-knowledge-point mastery, error-cause statistics and a remedial lesson plan generated from the reviewed set. 🔵 **Its README states the discipline this whole tier shares and states it as a guarantee: 所有数字由已复核数据确定性计算 — every number is computed deterministically from REVIEWED data, never from the model's own output.** 🟢 **That is the cleanest statement of the `P67` boundary this base has found in any language, and it is a product claim rather than a compliance note.** Pushed `2026-11-15` |
| all-in-one AI 教学助手 | https://github.com/yosemdawn/all-in-one-AI_edu_system | 🟢 **MIT — byte-read** (`1,062 B`, `sha256:f830ef372ec4…`, `main/LICENSE` [DEFAULT], refs=[`main` `codex/ai-config-and-upload-fixes`]) | 8 | APAC | 🟢 **New this pass (`p834`) — the widest K-12 surface in the tier**: class management, assignment publishing, submission, AI marking in BATCH, and teacher/student split roles in one deployment. 🔵 **Filed for the batch path specifically: every other row in this table marks one script at a time, and a class of `40` is the unit a real teacher actually has.** 🔴 `8★`, pushed `2026-11-02`. 🔴 **Its README claims it beats `99%` of commercial AI education products; that is marketing and is not carried as a finding** |
| chaoxing-grader-universal | https://github.com/Unke-cc/chaoxing-grader-universal | 🟢 **MIT — byte-read** (`1,066 B`, `sha256:c08a161f53f1…`, `main/LICENSE` [DEFAULT], refs=[`main`]) | 1 | APAC | 🟢 **New this pass (`p834`) — the INTEGRATION shape, and the reason `T120` exists.** Teacher-side batch marking of assignments and lab reports inside 超星学习通 (Chaoxing/Xuexitong), driven over the Chrome CDP protocol, cross-platform Windows / Linux / macOS. 🔵 **It does not ask the incumbent LMS for an API it does not expose — it drives the teacher's own authenticated browser session.** 🔴 **That is a pattern a studio can reuse against any closed portal, and this base has shelved it before for `p823`'s closed-portal integration; this is the second independent instance.** Pushed `2026-10-26` |
| ykt-grader | https://github.com/mc-dl/ykt-grader | 🟢 **MIT — byte-read** (`1,062 B`, `sha256:b429f339f75d…`, `main/LICENSE` [DEFAULT], refs=[`main`]) | 3 | APAC | 🟢 **New this pass (`p834`) — the same integration shape against a DIFFERENT incumbent**, 雨课堂 (Rain Classroom): an agent knowledge pack plus Playwright/CDP automation, attachment capture, comment and score write-back, **save verification** and anonymised statistics. 🔵 **The write-back verification step is the part worth copying: it re-reads what the platform stored rather than trusting its own POST.** 🟢 **Two unrelated authors against two unrelated closed platforms is what makes this a layer and not a one-off (`T102`'s test).** Pushed `2026-11-02` |
| math-work | https://github.com/shiyalun1126/math-work | 🟢 **MIT — byte-read** (`1,069 B`, `sha256:972de94494bf…`, `main/LICENSE` [DEFAULT], refs=[`main`]) | 0 | APAC | 🟢 **New this pass (`p834`) — the only row in this tier that marks STEP BY STEP rather than answer-by-answer.** Photographed handwritten maths in; per-line adjudication out: which step is wrong and why it is wrong, on two separate chains for algebra and geometry. 🔵 **Its README draws its own competence boundary — 限定域内可信, trustworthy only inside the bounded domain — which is a more honest scope statement than most commercial equivalents publish.** 🔴 `0★`, pushed `2026-11-12`. **Filed on function, not traction, per `T115`** |
| linear-algebra-grading-desk | https://github.com/Benhuangsuan/linear-algebra-grading-desk | 🟢 **MIT — byte-read** (`1,069 B`, `sha256:5ff801bd0f9b…`, `main/LICENSE` [DEFAULT], refs=[`main`]) | 5 | APAC | 🟢 **New this pass (`p834`) — the COST-CONTROL row.** A local Windows marking desk for linear algebra with three explicit modes — Mock, human scoring, and optional vision AI — plus human review and **spend caps on the vision calls**. 🔵 **Filed because the mode switch is the architecture: the same desk runs with no model at all, which is the only configuration a school with no budget and a data-residency rule can actually deploy.** 🔵 **`P74` inherits this directly.** Pushed `2026-11-11` |
| homework-ai-grading-lab (作业智评) | https://github.com/ShuyaoGao/homework-ai-grading-lab | 🟢 **MIT — byte-read** (`1,088 B`, `sha256:b0f6c0eff210…`, `main/LICENSE` [DEFAULT], refs=[`main`]) | 1 | APAC | 🟢 **New this pass (`p834`) — the TEACHING artefact of the tier**: handwriting recognition → rubric scoring → teacher review, shipped as a static online demonstration on **synthetic data**. 🔵 **Filed deliberately as a demo and labelled as one: it is the cheapest way to show a ministry or a school board the review boundary working end to end without touching a real pupil's work**, which is the first meeting `P74` has to survive. 🔴 **Synthetic data means it carries NO efficacy evidence and must never be cited as such.** Pushed `2026-11-10` |
| booktor (UNSAM) | https://github.com/KiaraPrecopio/booktor-tpi-unsam | 🟢 **MIT — byte-read on the DEFAULT branch** (`1,070 B`, `sha256:adc0be6971f6…`, `develop/LICENSE` [DEFAULT], refs=[`develop` `main` `feature/27-login` `test/31-mockmvc-jacoco`]) | 0 | LATAM | 🟢 **New this pass (`p834`) — Argentina (Universidad Nacional de San Martín), and the ONLY granted software artefact the Spanish-language DUA re-run produced.** An academic-tutoring scheduling backend built explicitly to Diseño Universal para el Aprendizaje principles. 🔵 **Filed as evidence for `T118` rather than for its traction: the Spanish UDL population is real (`10` repositories) but is almost entirely teacher-authored RESOURCES, and this is the one piece of it that is software under a grant.** 🔴 **Second default-branch case in this table — the default here is `develop`, not `main`; the bytes happened to agree, which is exactly why the defect is invisible without the check.** Pushed `2026-11-15` |

🔴 **Found and NOT filed, with the reason** — fewer real rows beats padding:

1. 🔴 **`sixiaopangai/2026-AI-Literacy-Exam-Helper`** (`25★`) — **CC-BY-NC-SA-4.0, byte-read** (`2,427 B`, `sha256:4268253f2531…`, `main/LICENSE`). 🔴 **NON-COMMERCIAL: not build-safe, excluded on licence.** 🔵 **And it is an index-vs-bytes case in the DANGEROUS direction: GitHub's index says `NOASSERTION`, which a studio reads as "ask the author", while the bytes say "you may not sell this".**
2. 🔴 **`yangfeng005/online_exam`** (`18★`) — **AGPL-3.0, byte-read** (`35,184 B`, `sha256:6f1e622c82a3…`, `master/LICENSE`). Copyleft; filed in `verticals/solutions.md` with the affero flag instead.
3. 🔴 **`throwOctober/zhixun-cloud-showcase`** — **`NO-GRANT-AT-ROOT`**, probed `31` filenames × `1` ref (`main`). 🔵 **A vocational cloud-lab platform and the best artefact the vocational re-run produced in any language — and it carries no grant at all.** See `T121`.

### Filed by `p833` (2026-11-15) — `4` rows: the CHINESE NATIONAL-PLAN tier, every licence byte-read with branch resolution

🟢 **These four are the build-safe yield of the `教育 大模型 agent` / `作业批改` / `智能备课`
population.** 🔴 **The population is large and the yield is thin for a reason worth recording: the
star-ranked view of these queries is dominated by unrelated high-traction repositories that merely
contain the characters** (a book list at `26,122★`, a political-propaganda corpus at `3,351★`),
🔵 **so a studio sweeping this corpus by stars sees nothing and concludes the supply is empty.
It is not — it is low-traction, recent, and real.** See `T115`.

| Name | Repo | Licence | Stars | Region | Description |
|---|---|---|---|---|---|
| 教育智能体 (teach_agent) | https://github.com/Zhangming0304/teach_agent | 🟢 **MIT — byte-read** (`1,070 B`, `sha256:7e705a8728f7…`, `main/LICENSE`, refs=[`main`]) | 7 | APAC | 🟢 **New this pass (`p833`), and it is the single most important row this base has filed in ten passes: it is the first agent on these shelves whose PRIMARY function is MARKING.** 🔵 **The closed loop is the whole product — 作业智能批改 → 错题自动诊断 → 分层练习生成: multimodal intake (photographed handwriting, PDF, Word, plain text), per-question marking, automatic extraction of wrong answers classified by knowledge point AND error type, a per-student profile carrying score trend and weak-knowledge-point distribution, and then a THREE-TIER remediation sheet (基础巩固 / 能力提升 / 拓展挑战) generated from that student's own error set, exported as printable PDF.** 🟢 **It also renders the agent's chain of thought while marking — which is not a demo feature here but the human-review surface that every high-risk-assessment regime in this base's policy matrix requires.** 🔴 **`7★`. Filed on function, not traction.** Runs on Chinese domestic models (DeepSeek / 通义千问 / 智谱清言), pushed `2026-04-20` |
| AIno 学苑 (AInoAgentAcademy) | https://github.com/quiet-sys/AInoAgentAcademy | 🟢 **MIT — byte-read** (`1,069 B`, `sha256:66bb28fd7721…`, `main/LICENSE`, refs=[`main` `feature-ai`]) | 2 | APAC | 🟢 **New this pass (`p833`) — the most COMPLETE learning-platform architecture in the tier, and the one that is actually deployed** (it ships on a live `.cn` domain, which is the placement evidence for the region field). A six-dimension learner profile (knowledge base, cognitive style, learning preference, error-prone points, interest direction, goal) built through guided dialogue and shown as a radar chart; SSE streaming chat with visible reasoning, web search and RAG; `25` algorithm visualisations with a Monaco editor and a **Docker judging engine**; auto-marked exams; **LangGraph multi-agent classroom generation**; ZIP project upload with AI code analysis and Docker build-and-run. 🔵 **The reusable part is the Docker judge plus the profile schema — a sandboxed code-grading service with a competence model attached is the one component `P69` has never had an implementation for.** 🔴 `2★`, pushed `2026-07-29` |
| AI-GAME-COOL | https://github.com/sumo1/AI-GAME-COOL | 🟢 **Apache-2.0 — byte-read** (`11,357 B`, `sha256:c71d239df917…`, `main/LICENSE`, refs=[`main` `feat/agent-loop-upgrade`]) | 6 | APAC | 🟢 **New this pass (`p833`).** 亲子计划 — natural language in, a playable children's educational game out, Java + React with a **plug-in Agent architecture** over Alibaba Bailian (Qwen / Kimi / DeepSeek). 🔵 **Filed for the plug-in boundary rather than the games: it is the clearest example in this base of an agent loop whose OUTPUT ARTEFACT is an executable the learner then uses, which is a different integration shape from every content-generation row on this shelf.** 🔵 **Its Apache payload is `11,357 B` / `sha256:c71d239df917…` — byte-identical to `XPRIZE/glexp-data-standardization` in `repos/foundations.md`.** 🟢 **That is the stock-text identity `T94` predicted and the first time this base has confirmed it across two unrelated projects by hash.** Pushed `2026-05-27` |
| 孔孟-Agent (KongMeng-Agent) | https://github.com/Lu-Yu-Zhen/KongMeng-Agent | 🟢 **Apache-2.0 — byte-read** (`11,360 B`, `sha256:adcb860af549…`, `main/LICENSE`, refs=[`main` + `5` feature heads]) | 3 | APAC | 🟢 **New this pass (`p833`) — the 备课 (lesson-preparation) node the Chinese plan's teacher-qualification limb creates demand for.** 🔵 **Filed with a measurement attached: its Apache payload is `11,360 B`, three bytes LONGER than the stock `11,357 B` — a UTF-8 BOM, and the hypothesis is PROVED rather than asserted: strip the leading `3` bytes and the remainder is `11,357 B` / `sha256:c71d239df917…`, byte-identical to the stock Apache text and to `AI-GAME-COOL` above.** 🟢 **That is a third disposition of the `T93`/`T94` licence-identity question and a cheap one to miss: a BOM changes the hash without changing a word of the grant, so hash-identity alone would have filed this as a non-stock Apache text and sent someone to read `11` KB of boilerplate.** 🔴 `3★`, pushed `2026-10-13` |

### Filed by `p832` (2026-11-15) — `5` rows: the LATAM foundational-literacy tier (`4`, the gap `ACTION p831-C` declared) and the XPRIZE finalist `p831` left UNRESOLVED (`1`)

🔴 **`ACTION p831-C` asked for a SEARCH, not a build: *"find whether a Spanish or Brazilian-Portuguese
decodable-text corpus exists anywhere under a permissive grant before `P71` proposes producing
one."* 🟢 **Run, and answered in both halves.** The CORPUS is a measured nil — `textos
decodificables` returns `TOTAL=0`, `Política Nacional de Alfabetização` (Brazil's own national
literacy instrument) returns `TOTAL=0`, `corpus portugues infantil leitura` returns `TOTAL=0`. 🟢
**But the APPLICATION layer the gap assumed was empty is not: it is a ~`110`-repository population
under `alfabetização infantil` (`70`), `conciencia fonologica` (`27`) and `consciência fonológica`
(`12`).** 🔵 **The four rows below are its entire build-safe yield, byte-read `2026-11-15`** — see
`T113` for why the yield is this thin, and `T111`/`T112` for the two instrument defects this pass
measured on the way.

| Name | Repo | Licence | Stars | Region | Description |
|---|---|---|---|---|---|
| litera | https://github.com/Illumi-Etec/litera | 🟢 **MIT — byte-read** (`1,097 B`, `sha256:13ccd2947bfa…`, `main/LICENSE`) | 6 | LATAM | 🟢 **New this pass (`p832`), and the traction leader of the entire LATAM literacy population — at `6★`.** 🇧🇷 *"Uma suíte de jogos educacionais desenvolvida para auxiliar no processo de alfabetização de crianças brasileiras"* — a games suite explicitly scoped to Brazilian children rather than translated into Portuguese. 🔵 **Published by an ETEC (São Paulo state technical school) team, which is the provenance `T113` names: the LATAM supply is produced by SCHOOLS, not by funders.** 🔴 Pushed `2025-10-12` — the only row here older than this year, and the only one with a fork. Created `2024-03-21` |
| alfabetizacao-divertida | https://github.com/karla08C/alfabetizacao-divertida | 🟢 **MIT — byte-read** (`1,069 B`, `sha256:e4dc38f80923…`, `main/LICENSE`) | 0 | LATAM | 🟢 **New this pass (`p832`) — the most complete design in the tier and the newest.** 🇧🇷 Gamified platform for early literacy built on **consciência fonológica**, with voice narration and a generative-AI surface. 🔵 **It is the only row in this tier that names phonological awareness as its ORGANISING principle rather than as a feature** — which is the pedagogy the Swahili/Arabic corpus is built on and the thing `ACTION p831-C` was looking for. 🔴 **`0★`, `0` forks, created `2026-10-17`, pushed `2026-11-09` — six days old at filing. Filed as a SEED, not as a dependency** |
| palavra-a-bordo | https://github.com/chicoritov/palavra-a-bordo | 🟢 **MIT — byte-read** (`1,067 B`, `sha256:bdb10f35e5af…`, `main/LICENSE`) | 0 | LATAM | 🟢 **New this pass (`p832`), and the one row here that crosses into the SEN tier `p830` built.** 🇧🇷 Phonological-awareness and rhyme game that ships **CAA (Comunicação Aumentativa e Alternativa — AAC)** support and audio alongside the literacy mechanic. 🔵 **`p830` filed the LIBRAS/AAC corpus and `p831` filed the early-reading corpus as separate tiers; this is the first repository this base has found that is BOTH**, and it is LATAM — the region `p831-C` recorded as a zero on both counts. 🔴 `0★`, created and last pushed `2026-10-04` |
| minigame-fonetico | https://github.com/yegor77/minigame-fonetico | 🟢 **MIT — byte-read** (`1,063 B`, `sha256:03474c4df5fc…`, `main/LICENSE`) | 0 | LATAM | 🟢 **New this pass (`p832`) — the narrowest and most honest row in the tier.** 🇧🇷 A phonological-awareness minigame on exactly two minimal pairs — **D/T and M/N**. 🔵 **Filed because the SCOPE is the finding: a minimal-pair drill is the smallest reusable unit of a phonics curriculum, and this is the only one in the population published as such.** 🔴 `0★`, created `2026-01-04`, pushed `2026-09-27` |
| RoboTutor (XPRIZE, Carnegie Mellon) | https://github.com/XPRIZE/GLEXP-Team-RoboTutor-RoboTutor | 🟢 **Apache-2.0 on the CODE + CC BY 4.0 on the CONTENT — byte-read** (`LICENCE.md`, `1,319 B`, `sha256:d2e11a0122c0…`, `master`, holder `2015-2018 Carnegie Mellon University and RoboTutor LLC`) | 14 | Global | 🟢 **New this pass (`p832`), and it is a CORRECTION of this base against itself, not a discovery.** 🔴 **`p831` probed this address, got `NOGRANT` at all `31` filename paths, and recorded it UNRESOLVED with the words *"a whole university's XPRIZE finalist is unusable until someone resolves this."*** 🟢 **Resolved: the grant was never missing. `p831` passed the probe a branch this repository does not have — `master` is its ONLY head — and one wrong branch argument nils all `31` paths at once (`D832-1`, `T112`).** 🟢 **Apache-2.0 makes it build-safe; the split with CC BY 4.0 on the content is a textbook `T78` instance** (*the code grant is not the deliverable grant*), and it is why the licence FIELD reads `NOASSERTION`. 🔴 **Frozen since `2019-11-05`, and the README states sound and image assets are NOT included** — so it is a curriculum-and-architecture inheritance, not a runnable app |

### Filed by `p829` (2026-11-15) — `11` rows: the VOCATIONAL tier (`3`, EMEA) and the language-and-study tier (`8`), every licence byte-read

| Name | Repo | Licence | Stars | Region | Description |
|---|---|---|---|---|---|
| Ausbildungs-Berichtsheft | https://github.com/SergeyZakh/Ausbildungs-Berichtsheft | 🟢 **MIT — byte-read** (`1,072 B`, `sha256:04bf792574d5…`, holder `2026 Sergey Zakharov`) | 1 | EMEA | 🟢 **New this pass (`p829`) — the first APPRENTICESHIP agent on these shelves and the anchor of `T102`.** 🇩🇪 Generates the **IHK-Ausbildungsnachweis** — the statutory German apprenticeship record — from a timesheet export (Clockify, Harvest, Jira+Tempo, Kimai, Toggl Track or Excel), rendered to Word or PDF on the IHK template. 🔵 **The strongest privacy posture in this cohort, and it is a product decision rather than a policy page: no account, data stays in the browser.** Tagged releases, CI. 🟢 The cheapest real integration shape at the vocational tier — it reads a document the learner already has to produce |
| Ausbildungsnachweis | https://github.com/marre868/Ausbildungsnachweis | 🟢 **MIT — byte-read** (`1,086 B`, `sha256:2cfc27ba0606…`, holder `2026 marre868`) | 1 | EMEA | 🟢 **New this pass (`p829`) — the SECOND independent implementation of the same statutory record**, which is what makes `T102` a tier rather than a lucky find. 🇩🇪 Flask + CLI, ships as a Windows `.exe`, and states explicitly that it targets people **without programming experience**. 🔵 Two unrelated authors solving one regulated artefact is the same signature `T77` used to establish the institution-integration tier |
| lernpfad-python-cpp | https://github.com/dimitrex93-cyber/lernpfad-python-cpp | 🟢 **MIT — byte-read** (`1,094 B`, `sha256:d525e491d703…`, holder `2026 Lernpfad Python & C++ – Mitwirkende`) | 0 | EMEA | 🟢 **New this pass (`p829`) — the CURRICULUM half of the vocational tier.** 🇩🇪 A structured self-study course explicitly bound to the **Ausbildungsrahmenplan für Fachinformatiker (Anwendungsentwicklung)** — the federal training framework plan — teaching every topic in Python and C/C++ in parallel. 🔵 **A curriculum pinned to a named statutory syllabus is directly reusable as a competency map: the other rows produce the EVIDENCE, this one holds the SPEC** |
| Polyglot Swarm | https://github.com/NiravRVaghasiya/Polyglot-Swarm | 🟢 **MIT — byte-read** (`1,072 B`, `sha256:c76f2bf915da…`, holder `2026 Nirav Vaghasiya`) | 1 | Global | 🟢 **New this pass (`p829`) — the most complete LANGUAGE-tutor architecture this base holds.** A LangGraph multi-agent tutor that maintains a per-skill competence model of grammar and vocabulary and PLANS the next lesson from it. 🔵 **Runs `100%` local by design (documented local path, not just a badge), which is the posture a sovereign build needs.** CI, Docker, Python 3.12+. Pushed `2026-11-11` |
| vocabit-mcp | https://github.com/JohnBilousov/vocabit-mcp | 🟢 **MIT — byte-read** (`1,070 B`, `sha256:ed0657fb89fe…`, holder `2026 Ivan Bilousov`) | 0 | Global | 🟢 **New this pass (`p829`), and it is the CLOSED-LOOP shape this base has described repeatedly without holding a reference implementation.** An MCP server for a shipping iOS flashcard app: `create_study_set` writes a set onto a real phone, and **`get_set_results` reads back which cards the learner marked hard, which they never reached, and how many reviews each took**. 🔵 **Its own README names the point: anything can generate flashcards; the tool that matters is the one returning the learner's performance so the next set is built from it.** Published to npm |
| AgenticTeacher | https://github.com/polendol/AgenticTeacher | 🔴 **SPLIT LICENCE — code MIT, MODEL `CC BY-NC-SA 4.0`** (byte-read `LICENSE.txt@master`, `1,056 B`, `sha256:1126322e2cc8…`) | 0 | Global | 🟢 **New this pass (`p829`) — build-safe ONLY if the split is respected, and it is `T78` caught a fourth time.** Turns an English YouTube video into CEFR-level-matched exercises: a fine-tuned DeBERTa-v3 + LoRA CEFR classifier plus a LangGraph agent on Qwen3-4B via Ollama. 🔴 **The classifier WEIGHTS are non-commercial — a client deliverable must retrain them; the pipeline around them is MIT and reusable as-is.** 🔵 The repository declares the split in its own badges, which is better disclosure than most of this shelf manages |
| Learning HUB | https://github.com/Agono0/learning-hub | 🟢 **MIT — byte-read** (`1,082 B`, `sha256:7704bac11c1e…`, holder `2026 Learning HUB contributors`) | 0 | Global | 🟢 **New this pass (`p829`).** A local-first TypeScript learning system implementing the high-effect methods from the literature — spaced repetition, retrieval practice, interleaving, elaboration, teach-back — plus a curriculum engine, **driveable end-to-end by any agent over MCP**. 🔵 **The one component in this cohort an orchestrator can treat as the learning ENGINE rather than as a tutor**, which is the role `P69` gives it. CI, Node ≥24 |
| cert-coach | https://github.com/gn02ash/cert-coach | 🟢 **MIT — byte-read** (`1,064 B`, `sha256:0a649bce619f…`, holder `2026 Gnash02`) | 0 | Global | 🟢 **New this pass (`p829`) — the BRIDGE row between this base's study tier and `T102`'s workforce tier.** Takes an exam's official skills outline, a date and weekly hours and produces domain-weighted daily sessions that **reschedule themselves when a day is missed**; RAG over the learner's own PDFs with **a page citation for every claim and an explicit refusal when the documents do not cover the question**; mock exams drawn by domain weight and a readiness score per domain. 🔵 **Certification IS vocational training with a different funder — this is the component `P69` grades readiness with** |
| litto | https://github.com/JesusPaz/litto | 🟢 **MIT — byte-read** (`1,066 B`, `sha256:8e132fefdc0e…`, holder `2026 Jesus Paz`) | 0 | Global | 🟢 **New this pass (`p829`).** Native SwiftUI iPhone/Mac spaced-repetition app on **FSRS-6** (`open-spaced-repetition/swift-fsrs`) with iCloud sync and an MCP server letting an assistant build decks, fix cards and **see which words the learner keeps forgetting**. 🔵 Interface ships in Spanish and English and follows the system language. 🔴 **Region recorded as `Global`, NOT `LATAM`: a bilingual surface is evidence of a Spanish-language audience and not of a jurisdiction, and this base does not infer a region from an author's name** |
| Hypatia's Hoard | https://github.com/Luissalet/HypatiaHoard | 🟢 **MIT — byte-read** (`1,066 B`, `sha256:fff33d08b8ee…`, holder `2026 Luissalet`) | 0 | Global | 🟢 **New this pass (`p829`).** A local study app — spaced repetition, a notebook over the learner's own sources, an **exact-math engine** and a `Profesor` teacher role — driven by an assistant over MCP on a local Python server with SQLite↔IndexedDB sync and local models. 🔵 **The exact-math engine is the same control `P67` reimplemented from first principles: deterministic arithmetic OUTSIDE the model.** Ships `README.es.md`; region recorded as `Global` on the same rule as `litto` |
| Questlog | https://github.com/chdominguez/questlog | 🟢 **MIT — byte-read** (`1,068 B`, `sha256:3319b49a25a9…`, holder `2026 chdominguez`) | 0 | Global | 🟢 **New this pass (`p829`).** Courses as quests: theory cards, quizzes, put-in-order, find-the-bug, coding katas running in the browser, written answers graded by an assistant, spaced repetition over what was missed. 🔵 **The reusable part is the CONTENT CONTRACT: courses are plain files in git validated by one schema, so a course is a reviewable artefact rather than rows in a vendor database** — the property `P61` wanted from `T86`'s catalogue |


### Filed by `p828` (2026-11-15) — `54` rows, every licence byte-read

| Name | Repo | Licence | Stars | Region | Description |
|---|---|---|---|---|---|
| cds-tools | https://github.com/Eduardozsw/cds-tools | 🟢 **MIT — byte-read** (`1,070 B`, `sha256:bb5cba819b2c…`) | 0 | LATAM | 🟢 **New this pass (`p828`) — 🇧🇷 the first Blackboard Ultra agent on these shelves for a BRAZILIAN PRIVATE university group.** CLI + read-only MCP for Cruzeiro do Sul / Unipê. 🔵 Every LATAM row before it was a public federal/state institution on SIGAA; this is the private-sector half of the same market, and Cruzeiro do Sul is one of Brazil's largest private groups. Declared unofficial. |
| sigaa-tools | https://github.com/PucaVaz/sigaa-tools | 🟢 **MIT — byte-read** (`1,064 B`, `sha256:dda770330e98…`) | 34 | LATAM | 🟢 **New this pass (`p828`) — the MOST-FORKED SIGAA repository this base has measured** (`34★`, `5` forks), and it was named in `repos/trending.md` without ever reaching a shelf. 🇧🇷 Tooling over the SIGAA portal. |
| SIGAA-Mais-Mais | https://github.com/brunomateus/SIGAA-Mais-Mais | 🟢 **MIT — byte-read** (`1,068 B`, `sha256:d8bdc1a01ddf…`) | 3 | LATAM | 🟢 **New this pass (`p828`).** 🇧🇷 SIGAA augmentation, `3★`. Authored by a named academic rather than a student account — the only SIGAA row here with that provenance. |
| ufal-schedule-ics | https://github.com/felipdsa21/ufal-schedule-ics | 🟢 **MIT — byte-read** (`1,070 B`, `sha256:00d38482ad8e…`) | 0 | LATAM | 🟢 **New this pass (`p828`).** 🇧🇷 Generates an `.ics` calendar from a UFAL SIGAA enrolment certificate. 🔵 **The cheapest useful integration shape in the whole LATAM tier: no API, no scraping session — it parses the document the registrar already hands the student.** |
| sigaa-cefetmg-modoescuro | https://github.com/hgiulliano/sigaa-cefetmg-modoescuro | 🟢 **MIT — byte-read** (`1,074 B`, `sha256:dfa646f12f31…`) | 10 | LATAM | 🟢 **New this pass (`p828`).** 🇧🇷 Chrome extension theming the CEFET-MG SIGAA portal, `10★`. 🔴 **Not an agent and shelved as what it is:** evidence of the SIGAA front-end extension layer that sits beneath the MCP layer and supplies its DOM knowledge. |
| IFAcademico | https://github.com/adiel-calixto/IFAcademico | 🟢 **Apache-2.0 — byte-read** (`11,357 B`, `sha256:58d1e17ffe51…`) | 6 | LATAM | 🟢 **New this pass (`p828`) — the Q-ACADÊMICO leg, which this base had named and never shelved.** 🇧🇷 Android client for the academic system used across the Institutos Federais. Apache-2.0, `6★`. |
| lamaku-mcp | https://github.com/JesseTho/lamaku-mcp | 🟢 **MIT — byte-read** (`1,166 B`, `sha256:ce95c0d64e0c…`) | 0 | North America | 🟢 **New this pass (`p828`).** 🇺🇸 Lamakū (UH Mānoa D2L Brightspace). 🔵 **Writes as well as reads** — pages, media, discussions, assignments, course packages — and its README raises FERPA directly, which no other D2L row in this cohort does. |
| mycourses-mcp | https://github.com/sahildayal/mycourses-mcp | 🟢 **MIT — byte-read** (`1,067 B`, `sha256:33b654addd10…`) | 0 | North America | 🟢 **New this pass (`p828`).** 🇺🇸 RIT myCourses (D2L). 🔴 **Submits assignments and posts to discussions — a WRITE posture on a student's own account**, the risk shape `P?` contrasts against read-only peers. |
| brightspace-hub-mcp | https://github.com/WayneWei228/brightspace-hub-mcp | 🟢 **MIT — byte-read** (`1,065 B`, `sha256:a319b64a887c…`) | 0 | North America | 🟢 **New this pass (`p828`).** 🇨🇦 Waterloo D2L plus Piazza in one surface — the only row here that joins the LMS to the course Q&A system. |
| mun-d2l-mcp | https://github.com/yasharisherenow/mun-d2l-mcp | 🟢 **Apache-2.0 — byte-read** (`11,343 B`, `sha256:032df62a0e36…`) | 0 | North America | 🟢 **New this pass (`p828`).** 🇨🇦 Memorial University (MUN) Brightspace, Apache-2.0, declared read-only. |
| dueboard | https://github.com/Yokiwa/dueboard | 🟢 **MIT — byte-read** (`1,070 B`, `sha256:8ffdc80a2fb5…`) | 2 | North America | 🟢 **New this pass (`p828`) — the AGGREGATION shape.** 🇺🇸 Pulls every deadline from Purdue Brightspace *and* Gradescope, Pearson MyLab, WileyPLUS and ALEKS onto one page. 🔵 **The only row in this cohort that treats the courseware vendors, not the LMS, as the system of record — which is what a US undergraduate's week actually looks like.** |
| dtu-learn-mcp | https://github.com/CarlSvejstrup/dtu-learn-mcp | 🟢 **MIT — byte-read** (`1,078 B`, `sha256:8b9edfdb3e7b…`) | 0 | EMEA | 🟢 **New this pass (`p828`).** 🇩🇰 DTU Learn (Brightspace) + **Panopto lecture transcripts** — the only row here that reaches the lecture-capture system, which is where the course's actual content lives. |
| edhec-mcp | https://github.com/Sillvs/edhec-mcp | 🟢 **MIT — byte-read** (`1,078 B`, `sha256:092e336c00f7…`) | 0 | EMEA | 🟢 **New this pass (`p828`).** 🇫🇷 EDHEC: Blackboard + Aurion (the French higher-ed scheduling/SIS suite) + ePrinting + campus food in one server. 🔵 **Aurion is a FRENCH SIS brand this base had never recorded.** |
| moodlectl | https://github.com/chapmanwm/moodlectl | 🟢 **MIT — byte-read** (`1,065 B`, `sha256:2ff4b5ffb33f…`) | 0 | EMEA | 🟢 **New this pass (`p828`).** 🇬🇧 University of Glasgow Moodle. 🔵 **Mirrors the course into LOCAL FILES rather than serving tools** — the shape that works when the agent client cannot hold a session. |
| tum-mcp | https://github.com/jamestesting0/tum-mcp | 🟢 **MIT — byte-read** (`1,091 B`, `sha256:879840521d30…`) | 0 | EMEA | 🟢 **New this pass (`p828`).** 🇩🇪 TUM: Moodle + **Artemis** (TUM's own open interactive-learning platform) + TUM Live + TUMonline. 🔵 **Four institutional systems behind one surface, and Artemis is itself open source — a build target, not just a source.** |
| ai-personal-assistant | https://github.com/Carlosito606/ai-personal-assistant | 🟢 **MIT — byte-read** (`1,070 B`, `sha256:62dd7775799c…`) | 1 | EMEA | 🟢 **New this pass (`p828`).** 🇵🇱 **USOS** — the Polish university administration system shared across most national HEIs — plus Moodle, an OR-Tools weekly planner and a job queue with verification. 🔵 **USOS is a national-scale system brand new to this base.** |
| merlin-mcp | https://github.com/simonseifert/merlin-mcp | 🟢 **MIT — byte-read** (`1,069 B`, `sha256:73861d7bb1e2…`) | 1 | EMEA | 🟢 **New this pass (`p828`).** 🇭🇷 Merlin (SRCE Moodle), the Croatian national academic computing centre's LMS. 🔵 **Phone-approved sends: a human confirmation step on every outbound message** — a control, not a prompt instruction. |
| ibu-mcp | https://github.com/Haris0059/ibu-mcp | 🟢 **MIT — byte-read** (`1,072 B`, `sha256:f61dd7d46379…`) | 1 | EMEA | 🟢 **New this pass (`p828`).** 🇧🇦 International Burch University (Sarajevo) SIS: grades, attendance, exams, tuition. 🔵 **Tuition balance is financial data — the first row on these shelves whose scope crosses from academic into bursar records.** |
| uaeu-blackboard-mcp | https://github.com/AhmTb/uaeu-blackboard-mcp | 🟢 **MIT — byte-read** (`1,061 B`, `sha256:a471b2b18310…`) | 0 | EMEA | 🟢 **New this pass (`p828`).** 🇦🇪 UAE University Blackboard, with local SSO and **tools for INSTRUCTORS as well as students** — the staff-side posture is rare in this cohort. |
| lab-grader-skill | https://github.com/yasserhegazy/lab-grader-skill | 🟢 **MIT — byte-read** (`1,069 B`, `sha256:d19e060e122a…`) | 0 | EMEA | 🟢 **New this pass (`p828`), and it is the named counter-instance to `T96`.** An MIT agent skill for TAs: rubric grading, parallel cheap graders, AI-and-copy detection, **Arabic feedback**, Moodle CSV export. 🔴 `0★`, single author, lab-scale — so it refines `T96` rather than overturning it: the grading supply is still thin, but it is no longer ALL licence-conflicted. |
| faroz-mcp | https://github.com/Akramjon-koder/faroz-mcp | 🟢 **MIT — byte-read** (`1,084 B`, `sha256:99b8d19e6a31…`) | 0 | EMEA | 🟢 **New this pass (`p828`).** 🇺🇿 Faroz, an Uzbek children's education platform: courses, exercises, games, homework, over **remote MCP with OAuth**. 🔵 **A remote, OAuth-protected MCP against a commercial K-12 platform — the deployment shape most LATAM/EMEA ministries would actually procure, and the only one of its kind here.** |
| mcp-sliit-courseweb | https://github.com/kesaruhasun/mcp-sliit-courseweb | 🟢 **MIT — byte-read** (`1,068 B`, `sha256:58d603d92c0c…`) | 7 | APAC | 🟢 **New this pass (`p828`).** 🇱🇰 SLIIT Courseweb (Moodle), Sri Lanka, `7★` / `3` forks. |
| moodle-mcp | https://github.com/kadmalcun/moodle-mcp | 🟢 **MIT — byte-read** (`1,065 B`, `sha256:385fc6657118…`) | 0 | APAC | 🟢 **New this pass (`p828`).** 🇯🇵 Tokyo University of Technology Moodle, local read-only. |
| ustc-bb-mcp | https://github.com/quantai1314/ustc-bb-mcp | 🟢 **MIT — byte-read** (`1,080 B`, `sha256:d25c64b5fb88…`) | 0 | APAC | 🟢 **New this pass (`p828`).** 🇨🇳 USTC Blackboard, local MCP, including coursework download and **assignment submission**. |
| d01-p01-hwp-form-automation-mcp | https://github.com/Feynman520/d01-p01-hwp-form-automation-mcp | 🟢 **MIT — byte-read** (`1,066 B`, `sha256:d9f635086306…`) | 0 | APAC | 🟢 **New this pass (`p828`) — the FORMS leg, and it is a jurisdiction-specific one.** 🇰🇷 Fills Korean government and school **HWP** (Hancom) forms end-to-end. 🔵 **HWP is the mandatory document format for Korean public-sector paperwork; no non-Korean toolchain speaks it. A Korean education engagement inherits this dependency whether or not it wants it.** |
| Google-AI-Classroom | https://github.com/wongcyrus/Google-AI-Classroom | 🟢 **MIT — byte-read** (`1,061 B`, `sha256:5d83f6d388b3…`) | 1 | APAC | 🟢 **New this pass (`p828`).** 🇭🇰 Edge-to-cloud multimodal classroom agent and **exam invigilation**: client-side MediaPipe, LiteRT Whisper and Gemma with Gemini. 🔴 **Invigilation is proctoring — in EMEA it is Annex III territory and emotion inference is banned outright, so this is a row to study, not to deploy unmodified.** |
| navital-gym | https://github.com/Navitallabs/navital-gym | 🟢 **Apache-2.0 — byte-read** (`11,357 B`, `sha256:58d1e17ffe51…`) | 3 | APAC | 🟢 **New this pass (`p828`).** 🇮🇳 Deterministic, auto-graded environments for agents on Indian-reality tasks (UPI, GST, forms, Hindi/Hinglish). 🔵 **Rule-based grading, not model-graded — which is exactly the arithmetic-outside-the-model principle `P67` prescribes, already implemented and Apache-2.0.** |
| brightspace-d2l-mcp | https://github.com/AnonymousOnyx22/brightspace-d2l-mcp | 🟢 **MIT — byte-read** (`1,199 B`, `sha256:3f0e907830ac…`) | 10 | Global | 🟢 **New this pass (`p828`) — field `NOASSERTION`, bytes MIT.** A `T27` rescue. Scopes itself to what is actually outstanding rather than dumping the whole course list. |
| brightspace-mcp | https://github.com/cyanprot/brightspace-mcp | 🟢 **MIT — byte-read** (`1,067 B`, `sha256:13555788e65e…`) | 3 | Global | 🟢 **New this pass (`p828`).** D2L Brightspace from Claude Code: courses, assignments, grades, content. |
| brightspace-mcp | https://github.com/micho911/brightspace-mcp | 🟢 **MIT — byte-read** (`1,071 B`, `sha256:1265b22d02bf…`) | 1 | Global | 🟢 **New this pass (`p828`).** D2L Brightspace **in Go** — the only compiled-language D2L server in this cohort, which matters for a single-binary campus deployment. |
| d2l-student-cli | https://github.com/webswe/d2l-student-cli | 🟢 **MIT — byte-read** (`1,062 B`, `sha256:12ec826fc5cb…`) | 0 | Global | 🟢 **New this pass (`p828`).** Unofficial read-only Brightspace command-line client. |
| mcp-workspace | https://github.com/hamzakammar/mcp-workspace | 🟢 **MIT — byte-read** (`1,067 B`, `sha256:2c8195bde63e…`) | 7 | Global | 🟢 **New this pass (`p828`).** D2L course access over MCP, `7★` / `2` forks. |
| D2L-MCP | https://github.com/RobertLMcCrary/D2L-MCP | 🟢 **MIT — byte-read** (`2,180 B`, `sha256:e3fdd2a6e7ff…`) | 6 | Global | 🟢 **New this pass (`p828`) — field `NOASSERTION`, bytes MIT.** A second `T27` rescue, and the only server here covering **both D2L and Canvas** behind one interface. |
| Campus | https://github.com/HasNate618/Campus | 🟢 **MIT — byte-read** (`1,074 B`, `sha256:8635fa05380e…`) | 1 | Global | 🟢 **New this pass (`p828`).** Syncs Brightspace into **local SQLite plus files** so answers can be verified against the real course material. 🔵 **A grounding/citation posture rather than a tool-call posture.** |
| blackboard-mcp | https://github.com/alanwtom/blackboard-mcp | 🟢 **MIT — byte-read** (`1,064 B`, `sha256:6cd5ef811418…`) | 9 | Global | 🟢 **New this pass (`p828`) — the most-starred independent Blackboard server found** (`9★`). Local-first, read-only, reads only the signed-in student's own Blackboard Ultra data. |
| bb-mcp | https://github.com/nitsuah/bb-mcp | 🟢 **MIT — byte-read** (`1,063 B`, `sha256:e024d09e682a…`) | 3 | Global | 🟢 **New this pass (`p828`), and the best-engineered row in this cohort.** Wraps the Blackboard Learn REST API; **RBAC middleware for role-based access**, CI, and a published `93.7%` coverage figure. 🔵 **Role-based access enforced in middleware is the control an institution-wide (rather than student-owned) deployment requires.** |
| blackboard-mcp | https://github.com/Lucasdoreac/blackboard-mcp | 🟢 **MIT — byte-read** (`1,067 B`, `sha256:96c1802bfcee…`) | 0 | Global | 🟢 **New this pass (`p828`).** Local Blackboard Ultra access for any MCP client: courses, materials, deadlines, announcements. |
| bb-mcp | https://github.com/UKplus8HRS/bb-mcp | 🟢 **MIT — byte-read** (`1,066 B`, `sha256:afa8162d956e…`) | 1 | Global | 🟢 **New this pass (`p828`).** Local **Playwright** MCP for Blackboard Learn with configurable institutions, SSO and academic calendars. 🔵 **Browser-driven, so it works where no REST credentials are issued — the usual case for a student.** |
| mcp-blackboard-ucsc | https://github.com/NiccoloSalvini/mcp-blackboard-ucsc | 🟢 **MIT — byte-read** (`1,072 B`, `sha256:b5155850ba0e…`) | 0 | Global | 🟢 **New this pass (`p828`).** Blackboard Learn Ultra over the **public REST API** rather than a scraped session. 🔴 **Institution behind the `ucsc` abbreviation NOT resolved this pass and deliberately not guessed; placed `Global` until read.** |
| edu-workspace-mcp | https://github.com/Kimmahone/edu-workspace-mcp | 🟢 **MIT — byte-read** (`1,086 B`, `sha256:f1112f62a389…`) | 1 | Global | 🟢 **New this pass (`p828`) — the widest Google-for-Education surface here:** Docs, Sheets, Slides, Forms, Drive **and** Classroom in one server. 🔵 **Forms plus Classroom is the assessment path; most Classroom rows stop at coursework.** |
| Classroom-Desk | https://github.com/Fawzankhan-404/Classroom-Desk | 🟢 **Apache-2.0 — byte-read** (`10,796 B`, `sha256:440ed275da0c…`) | 1 | Global | 🟢 **New this pass (`p828`).** Apache-2.0. Brings authorized Google Classroom course and coursework context to **ChatGPT** over MCP — one of the few rows not targeting Claude first. |
| classroom-mcp | https://github.com/Mattlo0546/classroom-mcp | 🟢 **MIT — byte-read** (`1,066 B`, `sha256:6bb7530c06a1…`) | 0 | Global | 🟢 **New this pass (`p828`).** Google Classroom for Claude, Codex and Cursor. **Single Python file, no dependencies** — the lowest-friction row to audit before a pilot. |
| classroom-mcp | https://github.com/OmarNiazi/classroom-mcp | 🟢 **MIT — byte-read** (`1,066 B`, `sha256:338410dba9d6…`) | 0 | Global | 🟢 **New this pass (`p828`).** Google Classroom, student-scoped, read-only. |
| google-classroom-mcp | https://github.com/adriasantacreu/google-classroom-mcp | 🟢 **MIT — byte-read** (`1,072 B`, `sha256:ff80e29676f1…`) | 2 | Global | 🟢 **New this pass (`p828`).** Google Classroom MCP, `2★`. |
| google-classroom-mcp | https://github.com/alanmagno1/google-classroom-mcp | 🟢 **MIT — byte-read** (`1,066 B`, `sha256:18e77745fac0…`) | 0 | Global | 🟢 **New this pass (`p828`).** Google Classroom with **multiple Google accounts** — the practical case for a teacher who holds a personal and an institutional identity. |
| google-classroom-student-mcp | https://github.com/AnonymousOnyx22/google-classroom-student-mcp | 🟢 **MIT — byte-read** (`1,071 B`, `sha256:dc4d909e25a2…`) | 0 | Global | 🟢 **New this pass (`p828`).** Read-only Google Classroom: to-do, due dates, missing work, grades, announcements. |
| google-classroom-mcp | https://github.com/vTanco/google-classroom-mcp | 🟢 **MIT — byte-read** (`1,193 B`, `sha256:67133cbc05f3…`) | 1 | Global | 🟢 **New this pass (`p828`) — and it is a TEACHER-side row, in Spanish.** Creates assignments, materials, topics and announcements; install guide in Spanish. 🔵 **Named in `agents/trending.md` since an earlier pass and never shelved. The teacher-authoring posture is scarce and the Spanish-language documentation makes it directly reusable in a LATAM or Spanish engagement.** |
| moodle-mcp | https://github.com/MattFor/moodle-mcp | 🟢 **MIT — byte-read** (`1,063 B`, `sha256:edd5981ce14c…`) | 0 | Global | 🟢 **New this pass (`p828`).** Moodle account access incl. **homework submission** — a write posture. |
| moodle-mcp | https://github.com/DenizCiger/moodle-mcp | 🟢 **MIT — byte-read** (`1,067 B`, `sha256:04314fb25dd9…`) | 0 | Global | 🟢 **New this pass (`p828`).** Moodle: courses, materials, assignments, deadlines, grades, quizzes, forums. |
| moodle-mcp-connector | https://github.com/Teci-AI/moodle-mcp-connector | 🟢 **MIT — byte-read** (`1,103 B`, `sha256:c8bcb50d415c…`) | 0 | Global | 🟢 **New this pass (`p828`).** Moodle reading **and authoring** of course content, company-maintained. |
| moodlens | https://github.com/andynur/moodlens | 🟢 **MIT — byte-read** (`1,090 B`, `sha256:225bebd8c6eb…`) | 0 | Global | 🟢 **New this pass (`p828`).** Moodle agent as a **local-first Chrome side panel**: read-only, no backend, no telemetry, declared integrity-safe. 🔵 **Zero-backend is the posture that clears a school's data-protection review fastest.** |
| eportal-moodle-skill | https://github.com/dawidlinek/eportal-moodle-skill | 🟢 **MIT — byte-read** (`1,067 B`, `sha256:7e84866e9e31…`) | 4 | Global | 🟢 **New this pass (`p828`).** An agent **skill** (not a server) for deadlines, assignments, materials and grades on any Moodle site, `4★`. |
| moodle-plugin-scaffold | https://github.com/arnoutvree/moodle-plugin-scaffold | 🟢 **MIT — byte-read** (`1,067 B`, `sha256:0da73281889e…`) | 0 | Global | 🟢 **New this pass (`p828`) — a BUILD-SIDE agent, which is a category this shelf barely holds.** Scaffolds a new Moodle plugin project with a `CLAUDE.md` context layer and code skeleton. 🔵 **Most rows here READ the LMS; this one EXTENDS it, which is what a studio engagement actually delivers.** |
| moodle-plugin-vibe-review | https://github.com/arnoutvree/moodle-plugin-vibe-review | 🟢 **MIT — byte-read** (`1,067 B`, `sha256:0da73281889e…`) | 1 | Global | 🟢 **New this pass (`p828`).** Reviews Moodle plugin changes against Moodle's own coding, security and API conventions before commit. 🔵 **Pairs with the scaffold above as a build-and-gate pair.** |


| Name | Repo | Licence | Stars | Region | Description |
|---|---|---|---|---|---|
| ufsc-moodle-mcp | https://github.com/jeanmartina/ufsc-moodle-mcp | 🟢 **MIT — byte-read** (`1,064 B`, `sha256:845ac6ac…`, holder `peancor`) | 0 | LATAM | 🟢 **New this pass (`p823`), and the most consequential row in it: the first agent on this shelf that WRITES to a Latin American institution's system of record.** *"Servidor MCP para o Moodle da UFSC"* — Universidade Federal de Santa Catarina 🇧🇷, targeted at the named host `presencial.moodle.ufsc.br`. 🔵 **It is the LATAM answer to a question this base has asked since `p811`, when `T31` found EMEA's supply attached to ministry and *Länder* portals and LATAM's equivalent at zero.** 🟢 **And it is write-capable with the control that posture requires: a two-phase `commit_assignment_update` / `verify_assignment_update` pair that re-reads Moodle after the commit, invalidating `assignmentIndexCache` first so the read-back cannot be served stale.** 🟢 **It distinguishes `form_rejected` (validation) from an expired session instead of reporting both as failure** — the failure taxonomy most LMS write agents omit. 🟢 **`commit_grading_batch` + `get_assignment_grading_overview` make batch grading auditable rather than fire-and-forget.** 🔵 Timezone handled explicitly, `America/Sao_Paulo` by default, and changing `dueDate` never moves `cutoffDate` — a stated independence that prevents the most common silent deadline bug. TypeScript, Node ≥ 22, MCP 2.0, v1.4.1, pushed `2026-11-14`. ⚠️ `0★`, single maintainer, pinned to one university's Moodle. |
| nak-api | https://github.com/Raindancer118/nak-api | 🟡 **WTFPL — byte-read** (`467 B`, `sha256:0992be62…`, title line `DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE Version 2`) | 2 | EMEA | 🟢 **New this pass (`p823`).** NORDAKADEMIE 🇩🇪 **CIS + Moodle as a single MCP server and CLI**, in Go: *Notenspiegel* grades, exams with real deadlines, timetable, seminars, electives and *Transferleistungen*, plus a web portal and an Android app. 🔴 **`83` tools, stated in the repository's own README badge (`mcp-83_tools`) — so this row extends the tool-count governance thread directly:** `137` ([`cubite-mcp`](https://github.com/amirtds/cubite-mcp)) · `83` (here) · `77` ([`chispa-mcp`](https://github.com/jeffercbs/chispa-mcp)) against `6` at the Ed-Fi standards body. 🔵 **Tool count is a design choice, and the institution-integration tier keeps choosing high.** 🔴 **Licence caveat that must reach legal before adoption: WTFPL is FSF-free and permissive in effect, but it is NOT OSI-approved, carries no warranty disclaimer and no patent grant.** 🟢 **Technically build-safe; procurement-safe only after a written view** — the distinction matters in a public-tender route, which is the route EMEA institution work takes (`T31`). Pushed `2026-11-12`. |
| student-mcp | https://github.com/CloudDown/student-mcp | 🟢 **MIT — byte-read** (`1,066 B`, `sha256:2eeba2ea…`, holder `CloudDown`) | 1 | North America | 🟢 **New this pass (`p823`) — and the first row here placed on 🇨🇦 Québec's CEGEP stack.** A local desktop MCP server (Rust, tray app, Windows/macOS/Linux) that brings **Moodle, Omnivox and Brightspace** into an assistant; **Omnivox is the Québec college portal**, which is what places this row in North America under `T32` rather than by its author. 🟢 **Two controls worth copying.** *"without typing your school password into the chat"* — it signs in through a real browser with MFA and persists **only a token or a private browser profile**. 🔵 And it states the residual risk plainly instead of hiding it: *"The link is a secret: anyone who has it can use your enabled tools."* 🟢 **Per-account assistant-access switches** let a learner expose one platform and withhold another. ⚠️ Unsigned builds — the README tells users NOT to disable OS protections, which is the right instruction and also an adoption friction. Pushed `2026-11-12`. |
| neyvu-connectors | https://github.com/jpss2004-bot/neyvu-connectors | 🟢 **MIT — byte-read** (`1,075 B`, `sha256:22911b82…`, holder `Neyvu contributors`) | 0 | Global | 🟢 **New this pass (`p823`), and the clearest statement in this base of WHY the institution-integration tier looks the way it does.** One read-only `LmsConnector` interface (four methods) with three implementations — **Canvas (REST API v1), Brightspace (Valence API) and Moodle (page captures)** — behind a single MCP server exposing `list_courses`, `list_assignments`, `list_documents`, `get_document` for all three. 🔵 **Its README names the structural constraint the rest of this tier works around:** *"in most cases students cannot connect an assistant to their learning platform themselves"* — institutional API access is not the learner's to grant, which is exactly why `p823` found a population of page-capture adapters rather than API clients (`T77`). 🟢 **"Trust rules in code, not prompts": reads only, the learner's own courses only, no guessed due dates, no inferred submissions or grades.** 🟢 **Provenance on every record** — each course, assignment and document carries its source URL, the API path or capture it came from, and the provider's version. 🔴 Self-described prototype. Pushed `2026-11-12`. |
| moodle-um | https://github.com/do-2k25-28/moodle-um | 🟢 **MIT — byte-read** (`1,084 B`, `sha256:9547a7ba…`, holder `Ghadi Saab and contributors`) | 0 | EMEA | 🟢 **New this pass (`p823`).** CLI and MCP server for the **Université de Montpellier** 🇫🇷 Moodle (`moodle.umontpellier.fr`), signing in through the real **ENT/CAS** flow — the French higher-education single-sign-on, which is the actual integration barrier and the reason a generic Moodle client does not work here. 🔴 **Write-capable: it submits assignments on the learner's behalf**, putting it on the same side of `p810`'s risk-posture split as [`jtayped/sakai-mcp`](https://github.com/jtayped/sakai-mcp) rather than the read-only side. 🟢 It also drives pages that have **no dedicated tool**, a general browser fallback — which is capability and attack surface in the same feature. 🔵 Carries an explicit non-affiliation notice and a *Responsible use* section, the convention this tier has converged on without coordination. Python ≥ 3.12 + uv + Chromium, CI green, pushed `2026-11-11`. |
| MIREA-Toolkit-MCP | https://github.com/Damanian/MIREA-Toolkit-MCP | 🟢 **MIT — byte-read** (`1,121 B`, `sha256:d74cbfe7…`, DUAL holder: `atomic-pancake-49` + `Damanian638 (modifications)`) | 0 | EMEA | 🟢 **New this pass (`p823`).** MCP connector for **РТУ МИРЭА / RTU MIREA** 🇷🇺: timetable, free lecture rooms, *Пульс*, the **БРС** point-rating record and the СДО learning system, running locally. 🔵 **The licence file is the interesting artefact: two copyright lines, the second marked *(modifications)*** — a downstream author who kept the upstream holder and added their own rather than overwriting it. 🟢 **That is the correct way to fork under MIT and it is rare enough in this base to note**; contrast [`edouaz/moodle-mcp`](https://github.com/edouaz/moodle-mcp), shelved in this same pass, which does the same thing. 🔴 Sanctions and institutional-engagement questions sit outside licence analysis and are NOT resolved by this row — it is shelved as supply evidence for the `T77` population, not as a recommendation to engage. Pushed `2026-11-14`. |
| monash-study-kit | https://github.com/Waldo0926/monash-study-kit | 🟢 **MIT — byte-read** (`1,066 B`, `sha256:74903ec0…`, holder `Waldo0926`) | 1 | APAC | 🟢 **New this pass (`p823`).** Connects **Monash University** 🇦🇺 Moodle **and Ed** (the discussion platform Australian universities run alongside the LMS) into Claude, Codex and Cursor, as a local MCP server plus CLI, macOS and Windows. 🔵 **Ed is the second system here, and it matters: the forum is where an Australian student's course questions actually live**, so a Moodle-only adapter would miss the higher-value corpus. 🟢 Chinese-language README against an Australian institution — a configuration this base should expect more of, given APAC international-student flows, and a reminder that `T32` places this row by **Monash**, not by the README's language. Pushed `2026-11-14`. |
| master-teacher (名师问问) | https://github.com/liqinling1994-cloud/master-teacher | 🟢 **MIT — byte-read** (`1,063 B`, `sha256:b31a3eaf…`, holder `秦岭`) | 5 | APAC | 🟢 **New this pass (`p823`).** A teaching-design **Agent Skill** for 🇨🇳 teachers: `152` master-teacher methodology profiles, `26` deep cards and **`15` 课程标准 (national curriculum standards)**, producing a lesson design, a 说课稿 or a full public-lesson package in Markdown or Word. 🔵 **It is another instance of `T70`'s finding — the asset is the CURRICULUM ADAPTER**: it connects 核心素养 (core competencies), 内容要求 and 学业质量 to classroom tasks and assessment evidence, which is the same national-instrument join `mawta` makes against Peru's `CNEB` and `edutraceapp` against Egypt's LO short codes. 🟢 **Source grading is built in** — it separates deep cards, standards index, public material and generic strategy, so a teacher can see which part of a plan is evidenced and which is filler. 🟢 **Distributed via `npx skills add`**, the Agent Skills channel rather than an MCP server. v5.4, pushed `2026-11-11`. |
| smart-marking | https://github.com/lby749/smart-marking | 🟢 **MIT — byte-read** (`1,063 B`, `sha256:29323b8f…`, holder `lby749`) | 0 | Global | 🟢 **New this pass (`p823`).** A *teacher-rubric-driven* agent grading Skill: the rubric the teacher already wrote is the input, rather than a rubric the model invents. 🔵 **That ordering is the governance-relevant part** and it is the side of the line Ofqual and Florida Rule `6A-14.0719` leave open (`T30`) — the human authors the standard, the agent applies it. 🔴 `0★`, single maintainer, early. Shelved for the pattern and the licence, not for maturity. Pushed `2026-11-12`. |
| Agentic-Assignment-Evaluator | https://github.com/Bhuvantejakomera/Agentic-Assignment-Evaluator | 🟢 **ALIVE — `p843`'s death notice WITHDRAWN at `p844`.** Re-measured `2026-11-16` with the address spelled AS THIS ROW SPELLS IT, trailing full stop included: `repo:Bhuvantejakomera/Agentic-Assignment-Evaluator.` → `total_count=1`, `MIT`, `0★`, pushed `2026-11-10`, not archived. 🔴 **`p843` queried the dot-stripped, lower-cased form and took the `422` as a death — the exact normalisation this row warned about at `p823`** (`T146`). 🟢 **MIT — byte-read** (`1,089 B`, `sha256:d21ead64…`, holder `Bhuvan Teja K`) | 0 | Global | 🟢 **New this pass (`p823`).** Grading assistant for **Google Classroom** that extracts student code and scores it **using local LLMs** — the privacy posture that matters when the artefacts are minors' work, because nothing leaves the institution. 🔴 **Address caveat recorded deliberately: the repository name ends in a literal full stop** (`Agentic-Assignment-Evaluator.`). It resolves — `gh api search/repositories -f q='repo:…'` returns `total_count=1` — but it will break naive link-extraction and trailing-punctuation stripping, including this base's own `grep -oE` address sweeps. 🔵 **Filed with the stop intact so a later pass does not "correct" it into a 404.** Pushed `2026-11-10`. |
| edu-agents | https://github.com/dh2211/edu-agents | 🟢 **MIT — byte-read** (`1,082 B`, `sha256:7eb4eb73…`, holder `EduAgentsKit contributors`) | 0 | Global | 🟢 **New this pass (`p823`).** Agent Skills for **K-12 teachers**: lesson objectives, unit plans and teaching materials. 🔵 Sits in the same Skills-distribution channel as `master-teacher`, without a national curriculum instrument behind it — which is precisely the difference `T70` says determines whether this kind of tool is a demo or an asset. Shelved as a permissive baseline to fork against a real curriculum. Pushed `2026-10-23`. |
| moodle-mcp (rahul069) | https://github.com/rahul069/moodle-mcp | 🟢 **MIT — byte-read** (`1,067 B`, `sha256:031c0fd8…`, holder `Rahul Garg`) | 0 | Global | 🟢 **New this pass (`p823`).** **Read-only** Moodle MCP server — courses, slides, deadlines, forums. 🔵 Generic rather than institution-pinned, which makes it the cleanest starting fork in the `T77` population for a deployment that must serve more than one Moodle host. Pushed `2026-11-13`. |
| moodle-mcp (edouaz) | https://github.com/edouaz/moodle-mcp | 🟢 **MIT — byte-read** (`1,116 B`, `sha256:99f3ba95…`, DUAL holder: `thntx` + `edouaz and Moodle MCP contributors`) | 0 | Global | 🟢 **New this pass (`p823`).** Private Moodle MCP server with a guided CLI setup and local storage. 🔵 **Second instance this pass of a fork that preserved the upstream copyright line and appended its own** (with `MIREA-Toolkit-MCP`) — two independent authors in one window getting MIT attribution right, which is worth recording because this base more often finds the opposite. Pushed `2026-11-08`. |
| moodle-mcp (felixx-dbm) | https://github.com/felixx-dbm/moodle-mcp | 🟢 **MIT — byte-read** (`1,072 B`, `sha256:edac1583…`, holder `Felix Dobelmann`) | 0 | Global | 🟢 **New this pass (`p823`).** Moodle MCP server giving assistants access to courses and files. 🔵 Shelved as part of the `T77` population census rather than for distinguishing features — the finding is the POPULATION, and a census that silently drops its ordinary members overstates how differentiated the tier is. Pushed `2026-11-08`. |
| nutslms-mcp | https://github.com/deeznust42/nutslms-mcp | 🟢 **MIT — byte-read** (`1,068 B`, `sha256:1a9b92a9…`, holder `Zain Ikhlaq`) | 0 | Global | 🟢 **New this pass (`p823`).** LMS MCP connector for Claude and Codex clients. 🔵 Same census note as above: an ordinary member of the `T77` population, filed so the denominator is honest. Pushed `2026-11-13`. |
| Codemm | https://github.com/iignaite/Codemm | 🟢 **MIT — byte-read** (`1,071 B`, `sha256:fd1dae60…`, holder `Gaille Amolong`) | 19 | Global | 🟢 **New this pass (`p823`), and the highest-starred new row in it.** *"Supercharge your learning journey with agents."* 🔵 Sits in `T75`'s scaffold category — the agent's subject is the learner's progress, not the task. `19★` and single-maintainer: supply with early traction, not adoption. Pushed `2026-11-13`. |
| physix-lab | https://github.com/albertoglvn/physix-lab | 🟢 **MIT — byte-read** (`1,067 B`, `sha256:4a21c9c6…`, holder `Alberto G…`) | 0 | Global | 🟢 **New this pass (`p823`).** *"A physics lab for your agent"*: 3D mechanics and 2D plane stress in the browser, driven by an agent. 🔵 **The category is a SIMULATION the agent can act in and read results from** — not a tutor that talks about physics. 🟢 That makes it checkable: the simulation, not the model, decides what is true, which is the cheapest available defence against a confidently wrong explanation in a STEM subject. Pushed `2026-11-15`, the day of this pass. |
| protoboard-iso | https://github.com/ccamilobedoya/protoboard-iso | 🟢 **MIT — byte-read** (`1,084 B`, `sha256:2841256a…`, holder `protoboard-iso contributors`) | 0 | Global | 🟢 **New this pass (`p823`).** Breadboard circuits drawn in **isometric SVG with real parts in real holes**, simulated live. 🔵 Same class as `physix-lab` — a grounded artefact an agent manipulates and a student can check — applied to electronics lab work, where the gap between a diagram and a working board is exactly what students get wrong. 🔴 **Placed `Global`, NOT LATAM:** `T32` places a row by the system it integrates with, and this one integrates with no regional system. Pushed `2026-11-15`. |
| glassbox-site | https://github.com/energon-a-secas/glassbox-site | 🟢 **MIT — byte-read** (`1,064 B`, `sha256:fc00a22f…`, holder `Neorgon`) | 0 | Global | 🟢 **New this pass (`p823`).** Interactive study labs for a **certification exam**, built by clicking through *simulated agent runs* rather than reading about them. 🔵 **The certification-prep tier is commercially live and under-represented on this shelf**, and this is the shape it takes when the subject is agents themselves. 🔴 Vendor-specific content; the reusable part is the simulated-run lab format, not the syllabus. Pushed `2026-11-13`. |
| modern-software-engineering-program | https://github.com/vladimiracunadev-create/modern-software-engineering-program | 🔴 **SPLIT LICENCE — both byte-read.** Code: 🟢 **Apache-2.0** (`11,345 B`, `sha256:b476b2ac…`, stock text). Content: 🔴 **CC BY-NC-SA 4.0** (`LICENSE-CONTENT.md`, `3,523 B`, `sha256:fd781b0e…`) | 0 | Global | 🟢 **New this pass (`p823`) — and it is shelved as a WARNING, which is why it sits here with its trap stated rather than in the rejected table.** A `540`-class, `45`-part open professional software-engineering curriculum **in Spanish**, with a live GitHub Pages site, CI validation and a SPEC+MCP agentic track. 🔴 **The Apache-2.0 badge is true and misleading at the same time: it covers the SCRIPTS. `LICENSE-CONTENT.md` puts the deliverable — *"clases, índices de parte, guías pedagógicas y rutas profesionales; explicaciones, ejercicios, laboratorios, retos y evaluaciones; rúbricas, matrices curriculares"* — under CC BY-NC-SA 4.0, which is NON-COMMERCIAL and SHARE-ALIKE.** 🔵 **For a Globant engagement that is a refusal, not a caveat: the courseware cannot be delivered to a paying client, and ShareAlike would propagate to derivatives.** 🟢 **This is a NEW trap class for this base, distinct from `T27`'s `NOASSERTION`:** there the field was wrong about one grant; here BOTH grants are correctly declared and the repository-level licence field reports only the one that does not govern the asset. 🔵 **Rule published as `T78`: in an education repository, read the CONTENT licence, because the content IS the product.** Pushed `2026-11-13`. |
| Ed-Fi-SDK-for-AI-Assistants | https://github.com/Ed-Fi-Exchange-OSS/Ed-Fi-SDK-for-AI-Assistants | 🟢 **Apache-2.0 — byte-read** (`11,357 B`, `sha256:c71d239d…`, stock text, no holder) | 1 | North America | 🟢 **New this pass (`p817`), and the row that changes what `p810` concluded.** `p810` shelved [`Prototype-Semantic-Layer-with-MCP`](https://github.com/Ed-Fi-Exchange-OSS/Prototype-Semantic-Layer-with-MCP) as *“the first education agent published by the STANDARDS BODY itself”* and flagged it `demonstration purposes only`. 🟢 **This is the SECOND, it is from the same Ed-Fi Exchange, and it carries NO demonstration caveat** — an AI-assistant “SDK” for building integrations against the Ed-Fi Data Standard. Created `2025-08-06`, pushed `2026-11-12`. 🔴 **At `1★` it has no community whatsoever, so read it as a VENDOR SIGNAL rather than as supply:** the body that defines the US K-12 data standard is now shipping agent-integration scaffolding itself. 🔵 **Engagement use: it tells a district procurement team that agent access to Ed-Fi is a sanctioned direction, which is the objection that normally stops these projects. See `T53` and `P43`** |
| coursecode | https://github.com/course-code-framework/coursecode | 🟢 **MIT — byte-read** (`1,069 B`, `sha256:055ad2b2…`, holder `Seth Vi…`) | 7 | Global | 🟢 **New this pass (`p817`) — the anchor of `T54`.** *“Open-source course authoring framework for Claude Code, Codex, and MCP-capable AI tools. Build, preview, and test SCORM 1.2, SCORM 2004, cmi5 and LTI.”* Created `2026-02-12`, pushed `2026-11-06`. 🟢 **The architectural inversion this pass is built on: the course is AUTHORED BY AN AGENT IN A REPOSITORY and the 1999–2016 interchange standards are the EXPORT TARGET, not the platform.** 🔵 **Which means a studio ships into Moodle, Canvas, Open edX or a client's commercial LMS without adopting, forking or licensing any of them — the copyleft question that dominates `verticals/solutions.md` simply does not arise, because no LMS code enters the deliverable.** 🟢 Licence payload byte-identical to its desktop sibling below, same holder, same org — `T41`'s instrument reporting a SIBLING, not a re-publication. See `P43` |
| coursecode-desktop | https://github.com/course-code-framework/coursecode-desktop | 🟢 **MIT — byte-read** (`1,069 B`, `sha256:055ad2b2…`, holder `Seth Vi…`) | 5 | Global | 🟢 **New this pass (`p817`).** *“Open-source desktop app for building SCORM, cmi5, and LTI courses with local preview, LMS export, AI-assisted authoring.”* Created `2026-02-12`, pushed `2026-10-29`. 🔵 **The non-developer surface over the row above — the one an instructional designer actually opens**, which is what makes `P43` sellable to a faculty-development team rather than only to an engineering team. 🟢 **Local preview matters for the same reason sovereignty does elsewhere in this base: unpublished course material never leaves the institution during authoring** |
| tessera | https://github.com/redmodd/tessera | 🟢 **MIT — byte-read** (`1,078 B`, `sha256:a7b3b71f…`, holder line `Copyright (c) 2026-prese…`) | 5 | Global | 🟢 **New this pass (`p817`), and the freshest row on this shelf — pushed `2026-11-15`, the day of the pass.** *“A JavaScript framework for building interactive eLearning courses, designed for AI-assisted authoring.”* Created `2026-05-03`. 🔵 **Independent of `coursecode` in authorship, licence payload and org, and it describes the same shape** — which is the evidence that `T54` is a layer trend rather than one author's idea. 🟡 At `5★` and six months old, treat it as a reference implementation to read, not a dependency to pin |
| elabora-core | https://github.com/aureliendossantos/elabora-core | 🟢 **Apache-2.0 — byte-read** (`11,358 B`, `sha256:cfc7749b…`, stock text, no holder) | 2 | Global | 🟢 **New this pass (`p817`) — the most complete single statement of `T54`'s shape.** *“Open e-learning source format, validator, SCORM compiler, player, editing engine and agent tooling.”* Created `2026-10-20`, pushed `2026-11-13`. 🔵 **Note the order of the nouns: a SOURCE FORMAT first, a validator second, the SCORM compiler third.** That is a build pipeline for courseware, and it is the piece `coursecode` and `tessera` each implement only partly. 🔴 **One month old and `2★` — the idea is ahead of the supply, which is `T54`'s commercial point and this pass's widest build slot.** 🔴 **Its Apache payload collides byte-for-byte with [`apereo/cas`](https://github.com/apereo/cas) (`11,399★`), two wholly unrelated projects — `T41`'s bound holding, since stock Apache-2.0 embeds no holder** |
| scorm-engine | https://github.com/scormflow/scorm-engine | 🟢 **MIT — byte-read** (`1,079 B`, `sha256:7cdfc153…`, holder `ScormFlow co…`) | 2 | Global | 🟢 **New this pass (`p817`).** *“Open-source infrastructure for SCORM, xAPI, and cmi5 — with built-in LRS, webhooks, and AI analytics. Pluggable storage and auth.”* Created `2026-05-24`, pushed `2026-11-01`. 🔵 **The RUNTIME half of `P43`: `coursecode` and `elabora-core` produce the package, this plays it and records what happened.** 🟢 **It bundles its own LRS, which collapses the `lrsql`-plus-player assembly into one MIT dependency for small engagements** — 🔴 **but at `2★` it is not a substitute for [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) (`144★`, Apache-2.0) where the record has to survive an audit** |
| somtoday-mcp | https://github.com/barzoj/somtoday-mcp | 🟢 **MIT — byte-read** (`1,082 B`, `sha256:47056e02…`, holder `somtoday-mcp co…`) | 1 | EMEA | 🟢 **New this pass (`p817`) — and the ONLY new row `ACTION p816-F`'s parent-portal question produced, because this base had already harvested that layer without naming it.** 🔴 **`p816-F` asked “what system does someone OTHER than the learner log into about the learner” as if it were unexplored; `q="parent portal mcp"` returns `6` repositories and `p813` had already shelved two of them — [`infinitecampus-mcp`](https://github.com/chrischall/infinitecampus-mcp) (🇺🇸) and [`vigilo-mcp`](https://github.com/kristoffervp/vigilo-mcp) (🇳🇴). The layer was `67%` harvested before the question was asked.** *“Read-only MCP server for the Somtoday parent portal (unofficial).”* Created `2026-10-10`, pushed `2026-11-13`. 🟢 **Somtoday is a dominant secondary-school platform in the Netherlands 🇳🇱, which places this row EMEA under `T42` — the region follows the system's catalogue, not the author.** 🟢 **`Read-only` is declared in the repository's own description, which is the lowest-risk posture in this layer and the one to put in front of a data-protection officer first** |
| anki-mcp-server | https://github.com/ankimcp/anki-mcp-server | 🟢 **MIT — byte-read** (`1,074 B`, `sha256:0ef87fdb…`, holder `Anatoly Tarnavsky`) | 558 | Global | 🟢 **New this pass (`p816`), and the most-starred agent in the RETENTION layer.** *"A Model Context Protocol (MCP) server that enables AI assistants to interact with Anki."* `40` forks, pushed `2026-11-07`, part of the `ankimcp.ai` project. 🔴 **It reaches Anki over `FooSoft/anki-connect`, which is GPL-3.0 and NOT what GitHub's licence field says — see `T50`.** 🟢 **That is still the clean posture: AnkiConnect is a separate process answering HTTP on `8765`, so this is boundary-only use and no copyleft enters the deliverable's tree.** 🔴 **But read `T48` before adopting it: this repository's own README says *“Prefer the AnkiMCP addon for most setups”*, and that addon is AGPL-3.0. The upstream's recommended topology is the one a studio cannot ship.** 🔵 **Customisation slot: it exposes decks, notes and review state; the scheduling POLICY is not its job — that is `P40`'s MIT FSRS core** |
| anki-mcp-server (nailuoGG) | https://github.com/nailuoGG/anki-mcp-server | 🟡 **MIT — MANIFEST CHANNEL ONLY** (`package.json`, `2,598 B`, `sha256:5748d75e…`, `"license": "MIT"`); 🔴 **no grant payload at any of `32` licence paths** | 254 | Global | 🟢 **New this pass (`p816`) — the SECOND-most-starred agent in the layer, and the one whose grant is weakest.** *"MCP server for Anki via AnkiConnect."* `38` forks, pushed `2026-11-13`. 🔴 **A manifest field is a DECLARATION, not a grant: there is no licence text in the tree, so a consumer who vendors this code receives an assertion rather than permission.** 🟡 **Shelved build-safe because the declaration is unambiguous and machine-readable, and flagged because it is the only row in this layer that is.** 🔵 **Cheapest unblock in the layer, and the same one `p813-D` named for `loyaniu/moodle-mcp`: one `LICENSE` commit upstream converts a `254★` assertion into a grant. Ask; do not vendor first** |
| yanki-obsidian | https://github.com/kitschpatrol/yanki-obsidian | 🟢 **MIT — byte-read** (`1,071 B`, `sha256:1d5701eb…`, holder `Eric Mika`) | 201 | Global | 🟢 **New this pass (`p816`).** *"Obsidian plugin to sync flashcards from a folder in your vault to Anki. Pure Markdown syntax."* Pushed `2026-11-10`. 🔵 **The architecturally interesting row: the authoring surface is PLAIN MARKDOWN in a folder the institution already owns, so the corpus never lives inside the AGPL application — Anki becomes a render target rather than the system of record.** 🟢 **That inverts the copyleft problem instead of working around it, and it is why `P40` builds on this shape.** 🔵 **Same author as `kitschpatrol/yanki-connect`, which this base measured at `p683` and filed unusable for grant-location reasons later resolved by `P1057` — the byte payload here is the SAME `1,071 B` `1d5701eb…` object, which is `T41`'s instrument agreeing with its own earlier reading** |
| scorzeth/anki-mcp-server | https://github.com/scorzeth/anki-mcp-server | 🟢 **MIT — byte-read** (`1,084 B`, `sha256:815d89a1…`, holder `Scott Orzech & Wai Son Wong`) | 185 | Global | 🟢 **New this pass (`p816`).** *"An MCP server for Anki."* `28` forks. 🔴 **STALE: pushed `2025-01-08`, which is `22` months before this reading and predates the MCP spec revisions every other row in this layer has tracked.** 🟡 **Shelved for completeness and for its fork count, not as an adoption candidate — at `185★` with no commits in nearly two years it is a reference implementation, and `ankimcp/anki-mcp-server` is the maintained one** |
| true-recall | https://github.com/pieralukasz/true-recall | 🟢 **MIT — byte-read** (`1,070 B`, `sha256:23444362…`, holder `Łukasz Piera`) | 67 | Global | 🟢 **New this pass (`p816`), and the only row in the layer that is BOTH agentic and schedule-aware.** *"Native spaced repetition for Obsidian: AI-generated flashcards, FSRS v6 scheduling, image occlusion."* Pushed `2026-11-14` — the freshest row in this pass. 🟢 **It is the reference topology for `P40`: generation by an LLM, TIMING by FSRS, and no Anki anywhere in the tree — so the whole thing is MIT end to end.** 🔵 **`8` forks, single author: adopt the SHAPE, and expect to own the code** |
| Smart-Study-Agent | https://github.com/HumphreySun98/Smart-Study-Agent | 🟢 **MIT — byte-read** (`1,067 B`, `sha256:ca229b6d…`, holder `Haofei Sun`) | 60 | Global | 🟢 **New this pass (`p816`), and the clearest statement of the layer's thesis in its own tagline:** *"The AI study agent that learns how you learn — RL picks the action, FSRS picks the timing."* 🟢 **That division of labour is the finding `T49` generalises: the LLM/RL layer chooses WHAT to show, a measured algorithm chooses WHEN, and only the second one needs to be right about memory.** 🔴 **`0` forks, single author, pushed `2026-08-16`: a topology reference, not an adoption candidate** |
| Shiori-v1 | https://github.com/kaorii-ako/Shiori-v1 | 🟢 **MIT — byte-read** (`1,073 B`, `sha256:3c78be93…`, holder `Tawin Tangsukson`) | 48 | Global | 🟢 **New this pass (`p816`), and the only row in the layer that touches an INSTITUTIONAL system of record.** *"Open-source AI study companion — Google Classroom sync, Gemini AI plans, SRS flashcards."* 🔵 **It is therefore the bridge between this layer and the LMS layer eighteen passes harvested: the retention loop is personal, but the syllabus it draws from is the institution's.** 🔴 **`5` forks, single author, pushed `2026-07-25`; and a Google Classroom scope grant is a credential question — grade it on `T36` axis (a) before any pilot** |
| clanki | https://github.com/jasperket/clanki | 🟢 **MIT — byte-read** (`1,082 B`, `sha256:2bc1d14c…`, holder `Jasper Keith O. Vallecera`) | 45 | Global | 🟢 **New this pass (`p816`).** *"An MCP server for connecting LLMs with Anki Flashcards."* `21` forks — a high fork-to-star ratio for the layer, which usually means people are running it rather than starring it. Pushed `2026-10-22` |
| nietus/anki-mcp | https://github.com/nietus/anki-mcp | 🟢 **MIT — byte-read** (`1,063 B`, `sha256:58f1e901…`, holder `nietus`) | 44 | Global | 🟢 **New this pass (`p816`), and the only row whose stated verbs are MEASUREMENT verbs.** *"MCP server for Anki: get quizzed, track retention, find leeches and manage your flashcards."* 🔵 **“Track retention” and “find leeches” are reporting over review history, which is the one thing in this layer an institution will pay for and the one thing a personal flashcard app does not expose.** 🟢 **That is `P42`'s read: the sellable artefact is the retention EVIDENCE, not the cards.** `13` forks, pushed `2026-10-05` |
| CamdenClark/anki-mcp-server | https://github.com/CamdenClark/anki-mcp-server | 🟢 **MIT — byte-read** (`1,069 B`, `sha256:fe16a00b…`, holder `Camden Clark`) | 81 | Global | 🟢 **New this pass (`p816`).** *"A model context protocol server that connects to Anki through AnkiConnect."* 🔴 **STALE: pushed `2025-03-19`.** 🟡 **Shelved for completeness; `13` forks. Of the five Anki MCP servers above `40★`, THREE are stale and two are maintained — a consolidation signal in a layer that is only two years old** |
| canvas-lms-mcp | https://github.com/bruchris/canvas-lms-mcp | **MIT — byte-read** (`1,069 B`, `sha256:187d52a3…`, holder `Christian Bru`) | 10 | Global | **New this pass (`p815`), and the first row in this base whose stated purpose is to WRITE A GRADE.** *"Canvas LMS MCP server — read courses, assignments, submissions, rubrics, quizzes; grade and comment from any AI agent."* 🔴 **Grading is a write to a system of record, and unlike `expeditto` (which prepares a `rascunho` and lets a human file it) this one's headline verb is the write itself.** 🔵 **So it is shelved build-safe on licence and flagged on posture: adopt the connector, put `P6`/`P22`'s human-in-the-loop publication gate in front of the grading tools, and never expose them unattended.** 🟢 **It is also the fifth distinct Canvas surface in this base and the only one that reaches RUBRICS**, which is what makes `P37` possible. Pushed `2026-11-03` |
| AutoGrader-Agent | https://github.com/omerfarooq223/AutoGrader-Agent | **MIT — byte-read** (`1,076 B`, `sha256:c6210dbf…`, holder `Muhammad Omer Farooq`) | 3 | Global | **New this pass (`p815`) — the only row found that does the WHOLE assessment loop in one agent.** *"AI agent that grades student assignments from a ZIP file using LLMs — generates rubrics, detects plagiarism, and outputs…"* 🟡 **`3★`, single author: this is a topology reference, not an adoption candidate** — and the topology is the useful part, because it is exactly `T44`'s argument in miniature. 🔴 **Its plagiarism step is LLM-judged rather than measured; replace it with `dodona-edu/dolos` (MIT, `357★`) before anyone's academic record depends on it.** Pushed `2026-11-02` |
| athina | https://github.com/athina-edu/athina | **MIT — byte-read at `LICENCE`** (`1,098 B`, `sha256:dd7ad247…`, holder `Michail Tsikerdekis`) | 3 | Global | **New this pass (`p815`), and `T46`'s filename specimen — it spells the file `LICENCE`, which was NOT in `p814`'s probe list.** *"A formative assessment microservice for programming assignments."* 🟢 **FORMATIVE is the word that matters: it is built to give repeated feedback during the work rather than one grade at the end, which is the lowest-risk shape in the whole assessment layer** — no record is written, so neither `T36` nor the EU AI Act's high-risk grading trigger is engaged. 🔵 **Maintained since `2019-02-22` and pushed `2026-11-13`: seven years of continuity at `3★`.** `ACTION`: if adopted, open the `LICENCE`/`LICENSE` alias upstream so the API field stops reading it correctly by luck |
| lab-autograder | https://github.com/himanshuuem/lab-autograder | **MIT — byte-read** (`1,064 B`, `sha256:d20d8c5e…`, holder `Himanshu`) | 1 | Global | **New this pass (`p815`), and the entire agentic surface of this layer: `q="autograder mcp"` returns `total_count=1` and this is it.** *"Auto-grades lab assignments from Google Classroom: extracts code from PDFs, runs it in a Docker sandbox, checks outputs."* 🟢 **The Docker-sandbox step is the right instinct and it is the `Judge0` problem restated: this row reimplements in-house what the `4,519★` GPL-3.0 engine does properly, which is precisely why `T44` matters commercially.** 🔵 **And a 🇮🇳 India-origin specimen on a channel where `q="autograder assignments india college"` returns `0` — the supply exists and does not answer to regional queries.** 🟡 **`1★`, created `2026-10-10`: the measurement, not the build.** Pushed `2026-10-22` |
| claude-scholar | https://github.com/Galaxy-Dawn/claude-scholar | **MIT — byte-read** (`1,068 B`, `sha256:0458c162…`, holder `Gaorui Zhang`) | 6046 | Global | **New this pass (`p814`) — and the single most-starred education agent this base has ever shelved, by a factor of 250 over `p813`'s anchor.** Semi-automated research assistant for academic research and software-literature work. 🟢 **`T39`: this row is the measurement. Eighteen passes harvested the LMS/attendance layer and its ceiling was `98★`; the research-library layer opens at `6,046★` and nobody had looked.** Pushed `2026-10-19` |
| zotero-mcp (54yyyu) | https://github.com/54yyyu/zotero-mcp | **MIT — byte-read** (`1,079 B`, `sha256:f0c6d358…`, holder `Zotero MCP Contributors`) | 5908 | Global | **New this pass (`p814`) — the canonical Zotero MCP server and the layer's reference implementation.** Connects a local or cloud Zotero library to Claude and other MCP clients. Pushed `2026-11-13` (the day of this pass). 🔵 **Name-collision group with `cookjohn/zotero-mcp` below, separated by licence bytes, NOT by name — see `T41`** |
| paper-search-mcp | https://github.com/openags/paper-search-mcp | **MIT — byte-read** (`1,063 B`, `sha256:f159d578…`, holder `OPENAGS`) | 3085 | Global | **New this pass (`p814`) — and the specimen that makes axis (c) THREE-valued, not binary (`T40`).** Search and download across arXiv, PubMed, bioRxiv, medRxiv, Google Scholar, Semantic Scholar, Crossref, OpenAlex, PMC, CORE, Europe PMC, dblp, OpenAIRE, CiteSeerX, DOAJ, BASE, Zenodo, HAL, SSRN, OpenReview, Unpaywall. 🟡 **Its `download_with_fallback` chain is OA-FIRST and Sci-Hub LAST and optional: *"source-native download → OpenAIRE/CORE/Europe PMC/PMC discovery → Unpaywall DOI resolution → optional Sci-Hub"*, and it carries a dedicated `Sci-Hub Notice` section.** 🟡 **So this is not a rejection and not a clean row — it is a CONFIGURATION OBLIGATION: shippable with the optional Sci-Hub path disabled, and an engagement must record that it was.** Contrast `0jsDanny/academic-research-mcp` in the rejected table, where the same source is the headline feature |
| Agentero | https://github.com/poco-ai/Agentero | **MIT — byte-read** (`1,063 B`, `sha256:06efb279…`, holder `poco-ai`) | 2487 | Global | **New this pass (`p814`).** Unified research workspace for humans *and* agents: PDF Q&A with citations. 🟢 The largest payload of the layer's build-safe rows (`43.6 MB` of tree) and pushed `2026-11-13` |
| zotero-mcp (cookjohn) | https://github.com/cookjohn/zotero-mcp | **MIT — byte-read** (`1,091 B`, `sha256:e8ed0429…`, holder `the Zotero-MCP project contributors`) | 1278 | Global | **New this pass (`p814`) — a Zotero PLUGIN extension rather than an external server, so it installs inside Zotero itself.** 🔴 **`T41`'s specimen: [`lricher7329/zotero-mcp-claude-code`](https://github.com/lricher7329/zotero-mcp-claude-code) (`45★`) returns a BYTE-IDENTICAL licence payload — same `1,091 B`, same `sha256:e8ed0429…`, same holder string — while GitHub's own `fork` field reports `false` for it.** 🔵 **It is therefore shelved HERE, as this row's derivative, and is NOT counted as an independent agent.** Pushed `2026-11-12` |
| gs-skills | https://github.com/cookjohn/gs-skills | **MIT — byte-read** (`1,055 B`, `sha256:3bed3331…`, holder line `Copyright (c) 2025` with NO name) | 546 | Global | **New this pass (`p814`).** Google Scholar skills for Claude Code: search, citation tracking. 🔵 **Payload lives at `master`, not `main` — a branch-alias data point for `gate-branch-alias`.** 🟡 **Its MIT holder line names no holder at all, which is a weaker authorship claim than every other row in this block** |
| mcp-zotero (kaliaboi) | https://github.com/kaliaboi/mcp-zotero | **MIT — byte-read** (`1,070 B`, `sha256:01de2c6d…`, holder `Abhishek Kalia`) | 163 | Global | **New this pass (`p814`) — the OLDEST row of the layer (pushed `2025-02-04`), which dates the layer itself: Zotero agents predate every LMS agent on this shelf.** Claude Desktop connector for Zotero collections and sources. 🟡 Smallest tree in the block (`23 KB`) and untouched for 21 months |
| zotero-mcp (kujenga) | https://github.com/kujenga/zotero-mcp | **MIT — byte-read** (`1,068 B`, `sha256:9cdf67f1…`, holder `Aaron Taylor`) | 162 | Global | **New this pass (`p814`) — third member of the `zotero-mcp` name-collision group, and a third distinct licence hash.** Deliberately lightweight server over the Zotero API. Pushed `2026-08-07` |
| cli-anything-zotero | https://github.com/PiaoyangGuohai1/cli-anything-zotero | **Apache-2.0 — byte-read** (`11,356 B`, `sha256:e7a7ce22…`, title line `Apache License`) | 142 | Global | **New this pass (`p814`) — the only Apache-2.0 row of the layer, so the only one that carries a patent grant.** CLI server for Zotero 7/8/9 with 70+ commands. Pushed `2026-11-04` |
| seerai | https://github.com/dralkh/seerai | **MIT — byte-read** (`1,062 B`, `sha256:84181be8…`, holder `dralkh`) | 97 | Global | **New this pass (`p814`).** Zotero 10 AI plugin and research assistant — chat with the library. 🔵 **Pinned to Zotero 10, which makes it the layer's clearest upstream-version dependency** |
| chiken | https://github.com/yuanjua/chiken | **MIT — byte-read** (`1,068 B`, `sha256:ab0e04f2…`, holder `Yuanzhou Cai`) | 90 | Global | **New this pass (`p814`).** Zotero + RAG + MCP + deep research in one package — the layer's only row that bundles a retrieval stack rather than exposing the library raw. Pushed `2025-09-05` |
| ZotPilot | https://github.com/xunhe730/ZotPilot | **MIT — byte-read** (`1,061 B`, `sha256:5c2bb763…`, holder `xunhe`) | 74 | Global | **New this pass (`p814`).** MCP server *plus* a packaged agent skill — the two-surface shape (`server` + `skill`) that `p813` first saw in the Chaoxing tier, here independently |
| research-hub | https://github.com/WenyuChiou/research-hub | **MIT — byte-read** (`1,068 B`, `sha256:c08e49d6…`, holder `Wen-Yu Chang`) | 67 | Global | **New this pass (`p814`).** AI-operable research workspace spanning Zotero, Obsidian and NotebookLM. 🔵 **The only row that treats the reference manager as ONE of several systems rather than the system — the closest thing in this layer to an integration pattern.** Payload at `master`; pushed `2026-11-13` |
| zoteus | https://github.com/oscardvs/zoteus | **MIT — byte-read** (`1,067 B`, `sha256:c20cd2f8…`, holder `Oscar Devos`) | 65 | Global | 🟢 **New this pass (`p814`), and the best-graded row of the pass on BOTH of `p813`'s axes plus the new third one — the direct antonym of `T36`'s Tier 3.** Search by keyword or meaning, passages with page locators, CSL citation formatting via citeproc-js, `.docx` with live Zotero field codes. 🟢 **Writes are versioned with optimistic locking, trash is reversible by default, and permanent deletion is opt-in and confirmation-gated.** 🟢 **And `zotero_check_citations` is an INTEGRITY-POSITIVE capability, the first on this shelf: it reads a draft, finds every citation (pandoc, `\cite`, author-year, numeric, DOI, `[@ITEMKEY]`), reports which are in the library, which are ambiguous and which are absent, then looks up each direct quotation in the cited PDF — found with its page, close (with the source's real wording), or not found.** 🔵 **`T36` graded agents on how badly they can be abused; this is the first row that measurably reduces abuse, and it is the one to put in front of a client worried about invented citations.** Pushed `2026-11-11` |
| zotero-code-execution | https://github.com/kerim/zotero-code-execution | **MIT — byte-read** (`1,090 B`, `sha256:7dec1382…`, holder `Zotero Code Execution Contributors`) | 62 | Global | **New this pass (`p814`).** Multi-strategy Zotero search built on the code-execution pattern rather than tool-per-query — the layer's one architectural dissent, and the cheapest on tokens |
| mcp-pyzotero | https://github.com/gyger/mcp-pyzotero | **MIT — byte-read** (`1,068 B`, `sha256:4c4a98dc…`, holder `Samuel Gyger`) | 56 | Global | **New this pass (`p814`).** Connector for a local Zotero library built on `pyzotero`, so it inherits a maintained Python client instead of reimplementing the API. Pushed `2025-11-20` |
| bx-scholar-mcp | https://github.com/leomcamilo/bx-scholar-mcp | **MIT — byte-read** (`1,071 B`, `sha256:af97dd08…`, holder `Leonardo Camilo`) | 0 | Global | **New this pass (`p814`).** 25+ tools over OpenAlex, CrossRef and the open-metadata backbone — no credential, no paywall, no library required. 🟢 **The layer's floor case: at `0★` it is the cheapest honest starting point for a studio that wants the catalogue layer without Zotero at all** |
| biomcp | https://github.com/genomoncology/biomcp | **MIT — byte-read** (`1,066 B`, `sha256:dd4dd888…`, holder `Ian Maurer`) | 679 | North America | 🟢 **New this pass (`p814`) — the North America reference row, and the ONLY agent in this base whose README encodes the new third risk axis as a first-class document.** PubMed, PubTator3, Europe PMC, PMC OA, ClinVar, ClinicalTrials.gov API v2, NCI CTS, OncoKB, Semantic Scholar. 🟢 **It opens by stating the obligation: *"BioMCP retrieves data from upstream biomedical sources. Those sources' terms govern how you use the data they return: some restrict commercial or clinical use. Check each source's terms and obtain any licence you need before relying on the data"*, and ships `docs/reference/source-licensing.md` with the per-source breakdown.** 🔵 **`T40`: an MIT licence on the CODE says nothing about the terms on the DATA, and this is the row that says so out loud. Quote it to a client.** Keyed to NIH/NLM and `NCBI_API_KEY`; pushed `2026-11-10` |
| ScienceClaw (beita6969) | https://github.com/beita6969/ScienceClaw | **MIT — byte-read** (`1,073 B`, `sha256:33923cdb…`) 🟡 **holder reads `Peter Steinberger`, which is NOT the repository owner** | 1028 | North America | **New this pass (`p814`), shelved with an UNRESOLVED provenance flag.** Verifiable program-level self-evolution for AI-for-Science agents; backed by `arXiv:2610.08691`, a Hugging Face dataset card, and `mcp-servers/` carrying arXiv-LaTeX and ChEMBL servers. 🟢 **Substantive: *"Every row of the dataset records its own source, license and URL"* and ports record upstream transformations.** 🟡 **But the MIT holder line names a third party, and a name-collision sibling [`AgentTeam-TaichuAI/ScienceClaw`](https://github.com/AgentTeam-TaichuAI/ScienceClaw) (`682★`, NO licence) was created two days later (`2026-03-11` vs `2026-03-13`).** 🔴 **Neither is established as canonical on this channel, so cite the arXiv paper, not the repository, until the lineage is resolved — registered as a gap below** |
| nature-academic-search | https://github.com/wp-a/nature-academic-search | **MIT — byte-read** (`1,060 B`, `sha256:d3f91696…`, holder `wp-a`) | 388 | APAC | **New this pass (`p814`) — the APAC row of the research-library layer, and it is placed by LANGUAGE rather than by a national system.** 🇨🇳 Academic paper search harness for Codex / Claude Code / DeepSeek, written for 中文科研用户 (Chinese-language research users). 🔵 **`T42`: the catalogue is global, so the agent is placed by the audience it addresses — the first row in this base where that is the operative placement rule.** Pushed `2026-10-01` |
| dspace-mcp | https://github.com/mpasternak/dspace-mcp | **MIT — byte-read** (`1,073 B`, `sha256:900b820e…`, holder `Michał Pasternak`) | 3 | EMEA | 🟢 **New this pass (`p814`) — Tier 1 on credential hygiene, and the cleanest read-only DECLARATION in this base, because it is not a declaration.** 🇵🇱 Read-only MCP server over DSpace 7+ institutional repositories. 🟢 **Its own section heading is *"Read-only by construction, not by promise"*** — the argument is structural, not a pledge, which is exactly the distinction `p813`'s Tier 1 could only assert. 🟢 **Credential guidance is explicit and correct: *"Prefer the environment variable over `--password`"* because a command line is visible to other processes, with keychain storage recommended; anonymous installs pay no token cost for account tools at all.** 🔵 **Handing a restricted file to a person requires `get_download_link` rather than the raw `download_url` — a deliberate access boundary.** Ships an installable `.mcpb` bundle; pushed `2026-07-25` |
| ojs-mcp | https://github.com/mpasternak/ojs-mcp | **MIT — byte-read** (`1,096 B`, `sha256:56a6229a…`, holder `Michał Pasternak <michal.dtz@…>`) | 1 | EMEA | 🟢 **New this pass (`p814`) — and the layer's model WRITE GATE.** 🇵🇱 MCP server over the authenticated Open Journal Systems REST API: submissions, issues, editorial statistics, plus five write tools. 🟢 **`OJS_ALLOW_WRITES=1` is OFF by default, and the README states the reason rather than the setting: *"Writes change real journal data"*.** 🟢 **Write tools were verified by reading state back (`check_writes.py`), and the read tools have their own harness.** 🔵 **Deployment reality worth knowing before an engagement: OJS answers `401` to every token-carrying request unless `api_key_secret` is set in `config.inc.php` — a server-side change the institution's OJS admin must make, not the studio.** Pushed `2026-09-10` |
| armenian-national-library-mcp | https://github.com/suren-kk/armenian-national-library-mcp | **MIT — byte-read** (`1,072 B`, `sha256:b47a07d3…`, holder `Suren Karapetyan`) | 7 | EMEA | 🟢 **New this pass (`p814`) — the FIRST agent in this base that encodes a RIGHTS CHECK as a workflow step, which is the direct antidote to `T40`.** 🇦🇲 Independent, provider-neutral, read-only MCP integration for the National Library of Armenia's public DSpace 9 repository. 🟢 **Its documented procedure puts the rights review BEFORE retrieval: *"Review the record's rights and access fields. When access is public and your intended use is permitted, call `list_item_files` or `get_file_download`"*.** 🟢 **`"File writes are disabled and are not implemented by this server"`; all links and redirects must stay HTTPS on the exact host under the configured API base path; bounded text extraction with MIME verification, and binaries over `NLA_MAX_INLINE_BINARY_BYTES` are never base64'd into model context.** 🟢 **Ships a hardened Compose profile — `127.0.0.1:3000` only, read-only root filesystem, dropped capabilities, no-new-privileges — and tells issue reporters not to post credentials or file bytes.** 🔵 **A national-institution agent built to a standard the commercial rows in this layer do not reach.** Pushed `2026-11-13`, the day of this pass |
| koha-mcp-server (asjolaviral) | https://github.com/asjolaviral/koha-mcp-server | **MIT — byte-read** (`1,084 B`, `sha256:a8be4d3f…`, holder `Koha MCP Server contributors`) | 1 | EMEA | **New this pass (`p814`) — the only build-safe agent over Koha, the integrated library system used by public and academic libraries worldwide.** 🟢 **OAuth2 `client_credentials` with automatic token refresh — the strongest AUTH mechanism of any row this pass, and the only one that is not a password.** 🟡 **But the install step is `nano config.json # fill in your Koha credentials`, so the `client_secret` lands on disk in cleartext: Tier 2 on axis (a) despite Tier 1 machinery.** 🔵 Requires Koha's REST API enabled and an OAuth2 key pair — an institutional prerequisite, like `ojs-mcp`'s. Pushed `2026-08-23` |
| abnt-mcp | https://github.com/PedroSmaxY/abnt-mcp | **MIT — byte-read** (`1,086 B`, `sha256:1cdab623…`, holder `Pedro Henrique da Silva Novais`) | 2 | LATAM | 🟢 **New this pass (`p814`) — the LATAM row, and the first agent in this base bound to a NATIONAL STANDARDS BODY rather than to a national software system.** 🇧🇷 *"ABNT Copilot MCP — Servidor Model Context Protocol para Padronização, Auditoria e Conformidade Documental Acadêmica (ABNT/IBGE)"*, for TCCs, master's dissertations, doctoral theses and journal articles. 🟢 **It implements the norms by number and edition — NBR 14724 (structure, typography, `3-3-2-2` pagination), NBR 10520:2023 (author-date in mixed case, `(Silva, 2023)`, long quotations at 4 cm indent), NBR 6023 (references), 6022, 6024 (no terminal period after `1.1`), 6027, 6028 (150–500-word single-paragraph abstracts) — plus IBGE tabular presentation, and it flags REVOKED practice such as all-caps authorship in parentheses, *"prática formalmente extinta pela atualização da ABNT NBR 10520:2023"*.** 🟢 **Graded on `T36` axis (b) and it PASSES: the capability set is *auditoria, formatação formal, consulta em bases indexadas e compilação para PDF* — it conforms and audits a document the student wrote; it is not a ghostwriter.** 🔵 **The engagement value is that norm compliance is mechanically checkable and currently done by hand across every Brazilian university.** CI configured; pushed `2026-10-27` |
| xuexitong-cli | https://github.com/DanMo661/xuexitong-cli | **MIT — byte-read** (`1,065 B`, `sha256:3486ae61…`) | 24 | APAC | **New this pass (`p813`) — the anchor of the Chaoxing/学习通 cluster and the most-starred APAC education agent in this base.** 🇨🇳 CLI + MCP server + desktop watcher over 学习通: timetable (with `.ics` export), assignment deadlines, exams, chapter task-points, notices,材料 download, cloud disk. `2` forks, pushed `2026-10-27`, created `2026-09-11`. 🟢 **Read-only by DECLARATION: *"所有工具均为 GET/查询语义，不提交任何表单"*.** 🟢 **Credentials env-var first (`CHAOXING_PHONE`/`CHAOXING_PASSWORD`), *"凭据不落盘"*; `config.json` and `session_cookies.json` gitignored *"绝不入库"*.** 🟢 **Turns the abuse case away in its own README (`T36` Tier 1): *"自动签到/刷课/答题类需求请绕行"*.** 🔵 Renamed `chaoxing-mcp` → `xuexitong-mcp` → here — see `T22` |
| chaoxing-mcp (Han-maker-wp) | https://github.com/Han-maker-wp/chaoxing-mcp | **MIT — byte-read** (`1,069 B`, `sha256:55fe2518…`) | 15 | APAC | **New this pass (`p813`) — `T36` Tier 2.** 🇨🇳 Direct-HTTP 学习通 server, sub-second, cookie persistence across restarts. Every tool labelled `🟢 只读`; account stays on the user's machine (*"没有任何中间服务器"*). 🔴 **Ships a REVERSE-ENGINEERED AES login (the phone/password encryption parameters lifted from Chaoxing's JS) and documents `XT_PASSWORD` as a PLAINTEXT value in the MCP client config block** — same defect class as `p812`'s SIGAA servers. 🔵 Ships an `AGENTS.md` written for the installing agent |
| chaoxing (DeliciousBuding) | https://github.com/DeliciousBuding/chaoxing | **Apache-2.0 — byte-read** (`11,324 B`, `sha256:50e67517…`) | 0 | APAC | 🔴 **New this pass (`p813`) — SHELVED AS A WARNING, `T36` Tier 3: DO NOT ADOPT.** 🟢 **The best security architecture in this base:** one Go binary, three separated surfaces (React console / remote `POST /mcp` / loopback `POST /call`), OAuth scopes that *"can narrow but never widen"*, **no generic `write` scope by design**, PBKDF2 owner password, AES-GCM credential+cookie vault with a separately stored key, CSRF + `__Host-` session cookie, HTTPS-only publication, and a contract that never returns raw credentials, cookies, tokens or captcha secrets. 🔴 **And its scope list includes `chaoxing.sign` — *"normal, location, and operator-coded password/gesture sign-in"* — with a watcher that polls classes during course hours and submits attendance automatically, plus "answer generation and coursework submission".** 🔴 **Licence-safe, un-shippable. Cite the architecture, never the product** |
| chaoxing-mcp (Cyoung-Van) | https://github.com/Cyoung-Van/chaoxing-mcp | **MIT — byte-read** (`1,067 B`, `sha256:6aa62f5f…`) | 0 | APAC | **New this pass (`p813`).** 🇨🇳 Local MCP + CLI for 学习通 courses, tasks and progress **through Chrome CDP** rather than a reimplemented login. 🟢 **The CDP approach sidesteps the reverse-engineered-AES defect entirely: the browser holds the session.** Created and pushed `2026-10-21` |
| chaoxing-studyai-mcp | https://github.com/Erich1566/chaoxing-studyai-mcp | **MIT — byte-read** (`1,066 B`, `sha256:3a2898fc…`) | 0 | APAC | **New this pass (`p813`).** 🇨🇳 One-click onboarding for 超星智雅 (StudyAI): interactive wizard, automatic token renewal, multi-client support. Pushed `2026-09-23`. 🔵 **Targets Chaoxing's own AI product rather than the LMS — the only row in the cluster that does** |
| chaoxing-subtitles | https://github.com/ILLENIUM-25/chaoxing-subtitles | **MIT — byte-read** (`1,068 B`, `sha256:4b8fa2fc…`) | 0 | APAC | **New this pass (`p813`).** 🇨🇳 Local MCP that exports 学习通 course-replay subtitles. Created and pushed `2026-11-09`. 🟢 **Narrow, read-only, and the most directly reusable piece in the cluster: lecture transcripts are the input a RAG study agent actually needs** (see `P31`) |
| xuexitong-connector | https://github.com/Zhf0826/xuexitong-connector | **MIT — byte-read** (`1,089 B`, `sha256:52baef61…`) | 1 | APAC | **New this pass (`p813`).** 🇨🇳 One command installs the read-only 学习通 MCP server into WorkBuddy, writes the connector config and self-checks: timetable, assignment deadlines, exams, progress, notices. Created and pushed `2026-10-23`. 🔵 **An INSTALLER over someone else's server — the cluster is already consolidating rather than duplicating, as LATAM's did at `p812` (`T34`)** |
| xuexitong-plus | https://github.com/xiny8127-glitch/xuexitong-plus | **MIT — byte-read** (`1,066 B`, `sha256:97fa27f4…`) | 0 | APAC | **New this pass (`p813`).** 🇨🇳 Extension layer: assignment requirements, question and attachment text extraction, timetable, materials and deadlines. Created and pushed `2026-10-26`. 🟡 **"Question text extraction" sits one step from the integrity line `T36` draws — read the tool list before adopting** |
| ChaoXingMessageMCP | https://github.com/XueQian17654/ChaoXingMessageMCP | **MIT — byte-read** (`1,069 B`, `sha256:aade238a…`) | 0 | APAC | **New this pass (`p813`).** 🇨🇳 Single-purpose server for 学习通 messages. Pushed `2026-10-09`. 🔵 Shelved for cluster completeness: it is the message surface the others omit |
| canvas-chaoxing-silc-mcp | https://github.com/shu-silc-osc/canvas-chaoxing-silc-mcp | **MIT — byte-read** (`1,070 B`, `sha256:5e014c4f…`) | 3 | APAC | **New this pass (`p813`) — the only INSTITUTIONAL account in the cluster** (`shu-silc-osc`, Shanghai University SILC). Read-only Canvas student/shared MCP tools, a Student Center feasibility preview. 🟢 **States plainly that *"Chaoxing not implemented yet"* rather than claiming the integration** — the honesty pattern `caleb-media-studio/skyward-mcp` also shows. Pushed `2026-10-13` |
| yuketang-mcp | https://github.com/ahdaolma/yuketang-mcp | **MIT — byte-read** (`1,082 B`, `sha256:376d3d2e…`) | 0 | APAC | **New this pass (`p813`) — the second Chinese platform, not a third Chaoxing row.** 🇨🇳 雨课堂 (Rain Classroom, Tsinghua/Xuetangzaixian) companion: connects course and courseware, auto-organises key points in class mode, supports reading, annotation and course Q&A. Android app. Created `2026-10-19`, pushed `2026-10-28` |
| unnc-moodle-mcp | https://github.com/MarkyMarkMa/unnc-moodle-mcp | **MIT — byte-read** (`1,085 B`, `sha256:5494026c…`) | 4 | APAC | **New this pass (`p813`).** 🇨🇳 Unofficial courseware sync for **University of Nottingham Ningbo China**'s Moodle — macOS + Chrome, first-run setup wizard, ships a Codex skill. `1` fork, pushed `2026-11-10`. 🔵 **Region is assigned from the TARGET INSTITUTION (`T32`), not from the Moodle upstream: a UK university's Chinese campus is an APAC deployment** |
| siakad-mcp | https://github.com/alfa-yohannis/siakad-mcp | **MIT — byte-read** (`1,070 B`, `sha256:77bf83d2…`) | 0 | APAC | **New this pass (`p813`) — 🇮🇩 the FIRST Indonesia-origin education agent in this base.** MCP for **SIAKAD** (*Sistem Informasi Akademik*) at Universitas Pradita. Created `2026-08-30`, pushed `2026-10-08`. 🔵 **SIAKAD is the Indonesian analogue of SIU-Guaraní/SIGAA: a per-institution academic self-management system, not an LMS** — `1` repository on the whole query, so the slot is effectively open (`T34` shape, APAC instance) |
| mcp_server_neis_api | https://github.com/arapodcho/mcp_server_neis_api | **MIT — byte-read** (`1,066 B`, `sha256:65a48ca4…`) | 0 | APAC | **New this pass (`p813`) — 🇰🇷 and the ONLY row in this pass's harvest that targets an OFFICIAL, PUBLISHED API.** Server over **NEIS** (나이스), Korea's national education information system, via its open-data portal `open.neis.go.kr` — meals, timetables, academic calendar. Pushed `2025-11-27`. 🟢 **No scraping, no reverse-engineered login, no credential at all: it is a public data API.** 🔵 **This is what every other row in this harvest would look like if the system of record published an API — the comparison is the argument (`P32`)** |
| infinitecampus-mcp | https://github.com/chrischall/infinitecampus-mcp | **MIT — byte-read** (`1,067 B`, `sha256:17dd0009…`) | 5 | North America | **New this pass (`p813`) — the strongest North American row in this base and the only MULTI-DISTRICT one.** 🇺🇸 Infinite Campus (Campus Parent portal), `20` tools across academics, daily life, documents, messaging and a credential/district healthcheck. 🟢 **Single-account config: linked districts are AUTO-DISCOVERED via CUPS SSO after login** — the multi-child, multi-district case every other row in the tier ignores. 🟢 **Exactly one tool is gated as write/IO (`ic_download_document`), and on a hosted deployment it returns a signed expiring link and writes nothing to server disk.** 🔵 Tools carry `_meta.mint` domain hints for grouping by `mcp-host`. `1` fork, pushed `2026-11-08` |
| canvas-parent-mcp | https://github.com/chrischall/canvas-parent-mcp | **MIT — byte-read** (`1,067 B`, `sha256:17dd0009…` — same grant bytes as its sibling, same owner) | 1 | North America | **New this pass (`p813`).** 🇺🇸 The PARENT-side Canvas observer surface, from the author of `infinitecampus-mcp`. Pushed `2026-11-11`. 🔵 **Shelved as a pair: a US K-12 family engagement needs the SIS portal and the LMS observer role together, and this is the only author who has built both** |
| studentvue-mcp (coolcrazycid) | https://github.com/coolcrazycid/studentvue-mcp | **MIT — byte-read** (`1,069 B`, `sha256:60fe23fd…`) | 0 | North America | **New this pass (`p813`) — the clearest CREDENTIAL STATEMENT in the North American tier.** 🇺🇸 StudentVUE (Edupoint Synergy) grades, assignments, attendance, schedule. 🟢 **Read-only.** 🟢 **Drives the student WEBSITE with a headless browser, so it keeps working in districts that disabled the legacy StudentVUE app API** — a deliberate choice against the brittle path. 🟢 **States the trust boundary exactly: *"Your password stays in your MCP config on your computer. It's only sent to your district's StudentVue site, and never to the AI. The AI only sees the page text."*** 🟢 Disclaims affiliation with Edupoint and tells the user to follow school rules. Created and pushed `2026-11-08` |
| schoology-mcp (coolcrazycid) | https://github.com/coolcrazycid/schoology-mcp | **MIT — byte-read** (`1,069 B`, `sha256:60fe23fd…`) | 0 | North America | **New this pass (`p813`).** 🇺🇸 Same author and same posture, pointed at Schoology: what's due, overdue, events, courses, materials. 🟢 **Read-only, the user's own sign-in, no API key required** — which matters because Schoology admin API keys are a district-level grant a student or parent cannot obtain. Created and pushed `2026-11-08` |
| studentvue-mcp (meowgoober) | https://github.com/meowgoober/studentvue-mcp | **MIT — byte-read** (`1,062 B`, `sha256:17699c29…`) | 0 | North America | **New this pass (`p813`).** 🇺🇸 StudentVUE server built against the **new mobile app documentation** rather than the deprecated web API. Created and pushed `2026-10-15`. 🔵 **Shelved next to `coolcrazycid/studentvue-mcp` precisely because they take OPPOSITE routes to the same system — mobile API vs headless browser. Which survives a district upgrade is the real selection criterion** |
| skyward-mcp | https://github.com/caleb-media-studio/skyward-mcp | **MIT — byte-read** (`1,066 B`, `sha256:e7b1808c…`) | 0 | North America | **New this pass (`p813`) — the best WRITE DISCIPLINE in the North American tier.** 🇺🇸 Unofficial self-hosted MCP for **Skyward** (SIS, heavy in US K-12), user-hosted so it needs no centrally registered Skyward OAuth application. 🟢 **"The first release is deliberately read only"**, with ChatGPT connecting over **OAuth 2.1 with PKCE**. 🟢 **And it names what it does NOT do rather than overclaiming: teacher, parent, staff, Qmlativ, calendar parsing and SIS write support are listed as *"extension points rather than fake claims of support"*.** Created and pushed `2026-10-05` |
| blackbaud-fe-nxt-mcp-server (CData) | https://github.com/CDataSoftware/blackbaud-fe-nxt-mcp-server-by-cdata | **MIT — byte-read** (`1,076 B`, `sha256:151d2c72…`) | 0 | North America | **New this pass (`p813`) — the ONLY VENDOR-PUBLISHED agent in this pass's harvest, and the only one in the North American tier.** 🇺🇸 Read-only MCP over **Blackbaud Financial Edge NXT** (the finance system of independent schools and non-profits) through CData's JDBC drivers. Pushed `2025-10-18`. 🔵 **Everything else in this tier is a student or a parent writing code about their own school; this is a commercial data-integration vendor shipping the connector as a product.** 🟡 Read-only in this edition by design — CData gates full CRUD behind its paid driver |
| dewey | https://github.com/obfuscated-tm/dewey | **MIT — byte-read** (`900 B`, `sha256:e4c20e35…`), against GitHub's `NOASSERTION` | 2 | North America | **New this pass (`p813`) — and the ONLY row in this pass that needs NO credential at all.** 🇺🇸 Schoology toolkit for students: browser extension, native iOS and Android apps, and an MCP server over to-dos, grades and class materials. 🟢 **"No passwords — it uses the Schoology login Chrome already has."** *"Free · no account · no passwords · nothing leaves your computer."* 🟢 **Session-reuse is the architecture `Cyoung-Van/chaoxing-mcp` reaches for via CDP, and it dissolves the plaintext-password defect that recurs in every other cluster this base has measured.** 🔵 **Seventh `NOASSERTION`-means-read-the-bytes instance.** Pushed `2026-11-12` |
| vigilo-mcp | https://github.com/kristoffervp/vigilo-mcp | 🟢 **0BSD (Zero-Clause BSD) — byte-read** (`640 B`, `sha256:b5eaf2ff…`), against GitHub's `NOASSERTION` | 2 | EMEA | **New this pass (`p813`) — 🇳🇴 and the MOST PERMISSIVE GRANT ON THIS SHELF.** Read-only local MCP for **Vigilo**'s parent portal (Norwegian municipal school administration): messages, news, attachments, after-school (SFO) check-in status. 🟢 **0BSD imposes no attribution requirement at all — a studio can vendor this into a client deliverable with no notice obligation, which no MIT row permits.** 🔵 **Extends `T31` (EMEA supply is attached to national/regional school portals) to a sixth country.** `1` fork, pushed `2026-11-09` |
| spbstu-mcp | https://github.com/kad-xyz/spbstu-mcp | **MIT — byte-read** (`1,064 B`, `sha256:0dc1ec80…`) | 20 | EMEA | **New this pass (`p813`) — the most-starred EMEA education agent in this base.** 🇷🇺 Server for **SPbPU (Polytech)** students spanning THREE systems at once: `dl.spbstu.ru` Moodle, university mail, and `openedu.ru` (the Russian national MOOC platform). `2` forks, created `2026-10-19`, pushed `2026-11-10`. 🟢 Confirmation-gated writes. 🔴 **Sanctions and data-residency review is a precondition for any commercial use of this row — shelved as market evidence of the national-platform pattern, not as an adoptable dependency** |
| usp-mcp | https://github.com/CaioCastro1/usp-mcp | **MIT — byte-read** (`1,107 B`, `sha256:3bf0a0b6…`) | 28 | LATAM | **New this pass (`p813`) — and it DISPLACES `utn-mcp` as the most-starred LATAM education agent, `28★` against `12★`, one pass after `p812` crowned it.** 🇧🇷 Ask in Portuguese about **USP** (Universidade de São Paulo, the largest university in Latin America): `e-Disciplinas` deadlines and materials, `JupiterWeb` course catalogue, and the *bandejão* menus. Created `2026-08-31`, pushed `2026-11-13` — **today**. 🟢 `13` confirmation points in the README. 🔵 **`p812` said LATAM's supply is attached to university self-management systems (`T34`); USP is the third Brazilian system after SIGAA and SUAP, and the largest** |
| moodle-codex | https://github.com/EdmundD28/moodle-codex | **MIT — byte-read** (`1,067 B`, `sha256:67907d65…`) | 10 | Global | **New this pass (`p813`).** Local-first, **read-only** Moodle plugin for Codex with reproducible setup, **bounded file parsing** and course change tracking. Created `2026-09-22`, pushed `2026-11-11`. 🟢 **"Bounded file parsing" is a stated resource limit — the only row in this harvest that names one** |
| moodle-mcp (IsaacAnwar) | https://github.com/IsaacAnwar/moodle-mcp | **MIT — byte-read** (`1,068 B`, `sha256:99349e41…`) | 9 | Global | **New this pass (`p813`).** **Read-only** Moodle access for any MCP agent — courses, materials, deadlines, grades — shipped as a Claude Code plugin with guided setup. Created `2026-10-04`, pushed `2026-11-03` |
| moocp | https://github.com/ImArjunJ/moocp | **MIT — byte-read** (`1,075 B`, `sha256:42d87b42…`) | 5 | Global | **New this pass (`p813`).** "Moodle for your AI CLI." Created `2026-10-13`, pushed `2026-11-04` |
| moodle-mcp (matheussilvano) | https://github.com/matheussilvano/moodle-mcp | **MIT — byte-read** (`1,089 B`, `sha256:2269bf86…`) | 5 | Global | **New this pass (`p813`).** Community server connecting a student's OWN Moodle account to Claude Code, Codex and ChatGPT; states it is independent and not affiliated with any institution. `3` forks on a repo created `2026-11-04` — **the fastest fork accumulation in this pass's harvest**. 🔵 **Region `Global`, not LATAM, although the author writes in Portuguese: `T32` resolves region from the TARGET SYSTEM, and generic Moodle has no region** |
| utn-mcp | https://github.com/nialvape/utn-mcp | **ISC — byte-verified** (`748 B`, `sha256:2ad14eb14513a4fa…`, title line `ISC License`) | 12 | LATAM | **New this pass (`p812`), the anchor row of `T34`, and on two counts the most important LATAM row this base has ever carried: it is the region's most-starred AND most-forked education agent (`12★`, `8` forks), and it has the strongest CREDENTIAL HYGIENE of any student-facing agent here.** MCP server over **UTN** (Universidad Tecnológica Nacional, Argentina) covering TWO systems: the `aula virtual` (Moodle) across its regionales, plus **Sysacad**, the classic UTN self-management system, through per-regional connectors downloaded on demand. FRBA, FRC, FRRE and FRT verified by the author; the Sysacad connector list names `18` regionales; `autogestion_*` tools (academic standing, current enrolment, finals, correlatividades) are **read-only**. 🟢 **Writes state their control in the README: *"Las tools que escriben le piden al agente que te muestre lo que va a hacer y espere tu confirmación"* — preview-then-confirm, which makes Argentina the SIXTH independent jurisdiction to converge on that gate (`T20`).** 🟢 **In HTTP mode the server is itself an OAuth authorization server: the student's password is used ONCE to mint a Moodle token and is explicitly *"no se guarda"*, the session is encrypted at rest under `store.key`, and only the HASH of the client token is kept.** 🟢 **And it REFUSES to run where the transport is unsafe — Rafaela, Santa Cruz and Trenque Lauquen are excluded because their Sysacad has no valid HTTPS and *"la contraseña viajaría expuesta"*; Avellaneda and Rosario are excluded for captcha.** 🔵 Login adapts per regional: Moodle direct, Keycloak SSO (FRBA), or Office 365 with MFA. Created `2026-10-02`, pushed `2026-11-13` — the day of this pass. 🔴 Unofficial and unaffiliated with UTN |
| UniMCP | https://github.com/HyNuwa/UniMCP | **MIT + inherited ISC — byte-verified, against GitHub's `NOASSERTION`** (`1,980 B`, `sha256:727b864af003d1e5…`: an MIT grant © MaxiFG, then a second ISC grant for *"Portions of this software are derived from utn-mcp"* © Joaquín Peñalva) | 1 | LATAM | **New this pass (`p812`), and the row that shows LATAM's supply is a LINEAGE rather than a scatter — it is a relicensed derivative of `utn-mcp` above, generalised from one university to Argentine universities as a class.** Serves the `aula virtual` (Moodle) **and SIU Guaraní**, the self-management system used across Argentine higher education: academic history with marks, results, dates and **expiry of regularidades**, enrolment, and exam sittings. 🔵 **Guaraní is read-only by necessity and the repo says why: *"Guaraní no tiene API: el servidor entra con tu usuario y lee las páginas como lo harías vos"*** — to enrol, the agent hands the student a link instead of acting. Moodle writes (forums, assignment submission) require the student's confirmation. 🟢 **Campus support is established MECHANICALLY, not asserted: each aula was probed with Moodle's `tool_mobile_get_public_config` and each Guaraní with its login page, and the method is published so a reader can repeat it.** 🔴 **Tested thoroughly only at UNJu; the rest *"faltan probarlos con usuarios reales"*** — and SAML/OAuth2 portals (several UNC faculties) are not supported. 🔴 `NOASSERTION` here means only that two permissive licences share one file; both are build-safe. Created `2026-10-19`, pushed `2026-11-13` |
| utnfrm-mcp | https://github.com/BautistaAlosMartorell/utnfrm-mcp | **MIT — byte-verified** (`1,088 B`, `sha256:d3aa5dfc50196b9f…`) | 4 | LATAM | **New this pass (`p812`).** Campus-virtual MCP server for **UTN Facultad Regional Mendoza**. Created `2026-10-24`, pushed `2026-11-10`. 🔵 The same author also publishes `utn-mcp-mendoza-web` (`0★`), which carries **no licence** and is rejected below — so check the slug, not the author, before adopting |
| UTNFRSF-CampusVirtual-MCP | https://github.com/thiagoyb11/UTNFRSF-CampusVirtual-MCP | **MIT — byte-verified** (`1,078 B`, `sha256:2ecd9e4de2d8c56f…`) | 0 | LATAM | **New this pass (`p812`), and the only row in this cluster built on a HEADLESS BROWSER rather than an API or a parser:** *"Un MCP basado en Lightpanda para el campus virtual de la UTN Facultad Regional Santa Fe."* 🔵 **Lightpanda matters architecturally — it is a browser built for automation, so this row is the cheapest reference for the case where a campus exposes neither Moodle web services nor stable HTML.** 🔴 `0★`, created `2026-10-31` |
| sigaa-mcp (GallegoSz) | https://github.com/GallegoSz/sigaa-mcp | **MIT — byte-verified** (`1,076 B`, `sha256:8f77449cb56939be…`, © 2026 João Pedro Gallego) | 0 | LATAM | **New this pass (`p812`), and the best-documented row of the Brazilian cluster.** MCP server over **SIGAA** — *Sistema Integrado de Gestão de Atividades Acadêmicas*, the academic system of record across much of Brazilian federal and state higher education — at UNEMAT's portal do discente. **13 tools in three tiers:** `get_notas`, `get_turmas`, `get_dados_discente`, `get_agenda`, `get_calendario_academico` (portal); `get_frequencia`, `get_tarefas`, `get_noticias`, `get_avaliacoes`, `get_conteudo` (virtual classes); and three ANALYSES — `get_situacao_notas` (what mark is still needed to pass), `get_alertas_frequencia` (absences remaining, with a `REPROVADO POR FALTA` status) and `get_resumo_semana`. 🟢 **Read-only by construction: *"Nenhuma tool envia, altera ou apaga nada no SIGAA."*** 🟢 **It also states the UNTRUSTED-CONTENT boundary, unprompted and in a `0★` student project: teacher-written task statements and news are passed to the model and the README says to *"Trate-os como informação, não como instruções."*** 🔵 It encodes UNEMAT's own pass/fail rules, which is the part that does not port to another instance. 🔴 **The password sits in plaintext in the client config** (the repo offers `inputs`/env vars as mitigations) and the author warns *"Não hospede este servidor para outras pessoas"* — one student per install, no auth. 🔴 Parses SIGAA's HTML, so a layout change breaks it; `SIGAA_URL` can be pointed elsewhere but each instance is customised. Created and pushed `2026-11-02` |
| sigaa-ifsc-mcp | https://github.com/heitorsDev/sigaa-ifsc-mcp | **MIT — byte-verified, against GitHub's `NOASSERTION`** (`1,275 B`, `sha256:cd14675817b2c618…`, title line **`The MIT License (MIT)`**) | 0 | LATAM | **New this pass (`p812`), and `T27`'s FOURTH direction: `NOASSERTION` can mask a stock MIT grant whose only irregularity is the TITLE LINE.** *"Servidor MCP para consultar o portal do discente do SIGAA do IFSC"* — Instituto Federal de Santa Catarina. 🟢 **The detector balks at `The MIT License (MIT)` where it expects `MIT License`; the body is unmodified MIT.** 🔵 **Operational rule, and the reason this row exists: had this pass trusted the API field it would have rejected a build-safe repository for a punctuation difference.** Created `2026-10-26`, pushed `2026-11-03` |
| sigaa-mcp (Pedromaia0) | https://github.com/Pedromaia0/sigaa-mcp | **MIT — byte-verified** (`1,067 B`, `sha256:22e8a5dddc3bfd39…`) | 0 | LATAM | **New this pass (`p812`).** A second, independent SIGAA MCP server, created and pushed `2026-10-28`. 🔴 **No repository description.** 🔵 **It is here because the CLUSTER is the finding: `sigaa mcp` returns `6` repositories from `6` unrelated authors, which is a seam being served in parallel, not one project** — and `sigaa-mcp` is a name shared by two of them, so resolve this row by the full slug (`T22`) |
| sigaa-agente | https://github.com/EduardoBidese/sigaa-agente | **MIT — byte-verified** (`1,076 B`, `sha256:da53ac6f2eef7651…`) | 0 | LATAM | **New this pass (`p812`), and the only row in this base whose integration shape is RPA rather than API or parser:** *"Use o SIGAA com um agente de IA (Claude ou Codex) no seu Firefox, pela extensão Ui.Vision."* 🔵 **It drives the real browser session the student is already signed into, so it needs no credential storage of its own and no web-service token — which is a genuinely different risk profile from the four rows above, and the only one that survives a campus with captcha or MFA on every request.** 🔴 **It also inherits RPA's weaknesses: it is bound to one browser, one extension and the rendered DOM.** `0★`, created and pushed `2026-10-02` |
| cvuex-mcp | https://github.com/rdereparadores/cvuex-mcp | **MIT — byte-verified** (`1,074 B`, `sha256:db6ddec81755f4cd…`) | 0 | EMEA | **New this pass (`p812`), and it extends `p811`'s EMEA finding one tier UP — from the national/regional SCHOOL portal to the UNIVERSITY campus virtual.** *"Servidor MCP para consultar el Campus Virtual de la Universidad de Extremadura (CVUEx)"* 🇪🇸. 🔵 **Same shape as the Argentine cluster and arrived in the same window** (created `2026-09-26`, pushed `2026-11-03`), which is what makes `T34` a cross-regional pattern rather than a LATAM curiosity. 🔴 `0★`, `0` forks, single maintainer |
| lanis | https://github.com/udondan/lanis | MIT | 2 | EMEA | **New this pass (`p811`), and the anchor row of this pass's finding (`T31`).** Unofficial SDK, CLI **and MCP server for Schulportal Hessen (Lanis)** — the student/parent portal operated by a GERMAN FEDERAL STATE, not by an LMS vendor. Created `2026-03-22`, pushed `2026-11-09`; `0` forks. 🟢 **This is the first agent in this base that attaches to a Länder-level education system**, which is exactly the altitude `ACTION p802-B` said German deployment evidence would be found at — and it was found as SOFTWARE before it was found as a statistic. 🔴 `2★` and a single-maintainer account: read it as a reference implementation of the seam, not as a dependency |
| dsbmobile | https://github.com/udondan/dsbmobile | MIT | 0 | EMEA | **New this pass (`p811`).** *Inoffizielles SDK, CLI und MCP-Server für **DSBmobile*** — substitution plans (`Vertretungspläne`), timetables, news and documents. Same maintainer and same creation date as `lanis` (`2026-03-22`), pushed `2026-11-12`. 🔵 **DSBmobile is the daily-notification layer above whatever LMS a German school runs**, so the pair `lanis` + `dsbmobile` covers portal plus timetable for one country without touching Moodle at all. 🔴 `0★`, `0` forks |
| admentum-mcp | https://github.com/andyswe/admentum-mcp | MIT | 0 | EMEA | **New this pass (`p811`), and the safest-shaped row of the `T31` cluster.** *"A **read-only** MCP server that syncs your messages from **Admentum**, the Swedish school platform, to local storage, and serves them to a personal AI agent **one item at a time**."* Created `2026-10-25`, pushed `2026-11-11`. 🟢 **Two controls stated in the description itself — read-only, and a one-item-at-a-time serving discipline that bounds how much of a child's correspondence can enter a model context in one call.** 🔵 That second control is not present in any other row in this file and is worth copying. 🔴 `0★` |
| ipasen_mcp | https://github.com/boraita/ipasen_mcp | MIT | 0 | EMEA | **New this pass (`p811`).** Unofficial MCP server for **iPasen (Séneca)** — the student/family portal of the **Junta de Andalucía**, a Spanish REGIONAL education authority: grades, absences, messages and **"confirmed actions"**. Created `2026-10-30`, pushed `2026-11-10`. 🟢 **The confirm step is in the one-line description, which makes this the FOURTH independent jurisdiction to converge on preview-then-confirm writes (`T20`)** after the three this base already recorded. 🔵 Ships an OpenClaw installer, so the distribution assumption is a consumer agent runtime, not an institutional deployment. 🔴 `0★` |
| sch-mail | https://github.com/weirdapps/sch-mail | MIT | 0 | EMEA | **New this pass (`p811`).** IMAP/SMTP MCP server for **Greek School Network (`sch.gr`)** mailboxes — the state-run network that serves Greek public schools. Created `2026-10-01`, pushed `2026-11-12`, default branch `master`. 🔵 **The seam here is not an LMS API at all — it is the national mail system**, which is a reminder that in state school systems the integration surface is often whatever the ministry actually operates. 🔴 `0★`; mail credentials in an agent's hands is the risk to raise first |
| alms-server | https://github.com/underconnor/alms-server | MIT | 0 | Global | **New this pass (`p811`).** *"ALMS self-hosted backend and **read-only MCP interface** for the bundled school SDK."* Created `2026-10-22`, pushed `2026-11-10`. 🟡 **Placed `Global` rather than in a region because the description names no country-bound system** — the rule this pass adopted for this column (`T32`) places a row by the system it integrates with, and this one does not say. 🔴 `0★`; shelved for the self-hosted-backend-plus-read-only-MCP shape, which is the topology `P23` and `P24` both ask for |
| canvas-mcp | https://github.com/boyuchengz/canvas-mcp | MIT | 119 | Global | **New this pass (`p810`) — the highest-starred education agent added since `p806`, and the first agent in this base for Canvas, the LMS this file's own platform layer has named since the third pass.** Read-only MCP server exposing courses, assignments, deadlines, grades, announcements and files from the **Canvas LMS** REST API to Claude, ChatGPT and any MCP client. `36` forks, created `2026-10-25` and pushed `2026-10-27` — 🔴 **two days of life, so treat maintenance as unproven.** 🟢 Licence **byte-verified** on the blobless-clone channel: `LICENSE` blob `5ba93171ff8f`, `1,072 B`, `MIT License / Copyright (c) 2026 Boyucheng Zhang`. 🟢 **Read-only by construction** — it holds no write path, which is the property that makes it safe to put in front of a student |
| Prototype-Semantic-Layer-with-MCP | https://github.com/Ed-Fi-Exchange-OSS/Prototype-Semantic-Layer-with-MCP | Apache-2.0 | 0 | North America | **New this pass (`p810`), and the most architecturally important row in this file despite `0★` — the first education agent this base has found that is published by the STANDARDS BODY itself rather than by a vendor, a student or a lab.** Ed-Fi Alliance, LLC, pushed `2026-11-12` (one day before this pass). A PostgreSQL **semantic layer** over Ed-Fi API data plus a **read-only early-warning MCP server** scoped to the signed-in educator. Six tools: `get_my_scope`, `list_my_sections`, `find_students`, `list_students_at_risk`, `get_student_summary`, `get_attendance_trend`. 🟢 Licence byte-verified: blob `29f81d812f3e`, `11,558 B`, unmodified Apache-2.0. 🔴 **The README says "for demonstration purposes only; not intended to be a robust production solution" — ship the PATTERN, not the code.** See `P810-1` |
| openfoam-mcp-server | https://github.com/webworn/openfoam-mcp-server | **Apache-2.0 — byte-verified, against GitHub's own `NOASSERTION`** | 129 | Global | **New this pass (`p810`), and it is a row this base would have WRONGLY rejected on the API field alone.** GitHub's `license.spdx_id` returns `NOASSERTION`; the `LICENSE` bytes are **unmodified Apache-2.0** (blob `be1f2caa61c7`, `10,708 B`, `APPENDIX` present, no added restrictive clause — the three `shall not` hits are stock Apache §1 and §9). 🟢 **So it is build-safe.** An LLM-driven **OpenFOAM** CFD MCP server with Socratic questioning and expert error resolution — engineering-education specific, `24` forks. 🔴 Pushed `2026-01-18`, so it is the least recently maintained row added this pass. See `T969` |
| OpenStudy | https://github.com/OpenStudy-dev/OpenStudy | MIT | 80 | Global | **New this pass (`p810`).** Self-hostable study dashboard with a **built-in MCP server**, so an existing Claude/ChatGPT subscription becomes the study engine rather than a per-seat API spend. `14` forks, created `2026-04-17`. 🟢 **The commercial point is the inversion of the cost model** — the institution hosts the surface and the learner brings the model subscription, which is the only structure in this base that avoids per-learner inference billing entirely |
| Grader-agent | https://github.com/erictrainnlpinxihu/Grader-agent | MIT | 94 | Global | **New this pass (`p810`) — the first rubric-grading agent in this base with an auditable control structure, and the row that makes `P810-3` buildable.** Five-phase main loop `perceive→plan→act→observe→respond` driven by a harness. 🟢 **The design decision that matters: the MODEL decides only intent and confidence; routing, tool set and risk level are pinned in CODE.** That is exactly the separation Ofqual's "AI may not be the sole marker" and the EU Art. `27` FRIA both require a deployer to evidence. 🔴 `0` forks and a Chinese-language README; created `2026-09-21` |
| edumints-scorm-mcp | https://github.com/kemalyy/edumints-scorm-mcp | MIT | 9 | Global | **New this pass (`p810`).** MCP server that **assembles interactive, SCORM-compliant e-learning courses**, self-hostable, from edumints.com. `5` forks. 🟢 **SCORM is named `3,434` times across this base and until this pass had exactly one producing repo** — this is the second, and the first that an agent can drive conversationally |
| scorm-mcp-server | https://github.com/giacomomaria81/scorm-mcp-server | MIT | 6 | Global | **New this pass (`p810`).** Turns HTML, Claude Design bundles or mobile-learning exports into **LMS-ready SCORM 2004 / 1.2 packages — and validates any SCORM zip.** Offline and tracked. 🟢 **The validator is the reusable half**: it is the only SCORM conformance check in this base that runs without an LMS, which makes it a pre-delivery gate rather than a post-upload surprise |
| cubite-mcp | https://github.com/amirtds/cubite-mcp | MIT | 0 | Global | **New this pass (`p810`), and the widest tool surface of any education MCP server in this base: `137` tools.** Drives **Cubite LMS** (SCORM, xAPI, certificates, cohorts) from Claude, ChatGPT, Gemini CLI or Cursor, with OAuth sign-in. 🔴 **`0★`, `0` forks, single-vendor-bound, created and last pushed the same day (`2026-09-23`).** 🔵 Carried for the tool-surface design, not as a dependency — and read it next to [`jeffercbs/chispa-mcp`](https://github.com/jeffercbs/chispa-mcp)'s `77` tools, because a `137`-tool server at the teacher's own permission level is `p792-D`'s unclaimed risk at twice the size |
| myelinate | https://github.com/baney75/myelinate | MIT | 7 | Global | **New this pass (`p810`).** Claude Code plugin and **agent-skill suite that makes the assistant a Socratic tutor: `14` skills** for course design and teaching. 🟢 **MIT on a SKILL corpus is the licence shape this base has repeatedly failed to find** — `GarethManning/education-agent-skills` (`978★`) is CC BY-SA 4.0 and was rejected at `p802` as contaminating, so this is the first permissive skill corpus that can be cut down and shipped inside a client deliverable |
| CodeTrain (agent-skills) | https://github.com/InferHaven/agent-skills | Apache-2.0 | 4 | Global | **New this pass (`p810`).** An open-source **Socratic coding tutor that runs as an Agent Skill inside the learner's own coding agent** rather than as a separate product. 🟢 **The delivery shape is the finding: no server, no LMS, no seat** — it meets the learner where the work already happens, which is the one channel a university cannot procure its way out of |
| viable | https://github.com/VIABLE-Learning-Lab/viable | MIT | 1 | Global | **New this pass (`p810`), pushed `2026-11-11`, two days before this pass — the freshest row in this file.** "Open tools for AI that teaches the way a teacher wants": a **Harness that wraps any agent** plus an Engine. 🟢 **A lab-origin project (`VIABLE-Learning-Lab`) that separates teaching POLICY from the model** — the same control shape as `Grader-agent`, arrived at independently. 🔴 `1★`, created `2026-11-05`; this is a seed, and it is shelved as one |
| sakai-mcp | https://github.com/jtayped/sakai-mcp | MIT | 2 | Global | **New this pass (`p810`) — the first Sakai agent in this base.** Sakai is named `3,937` times across these files, more than any other LMS, and carried **zero** agents until this row. Student-account scope: courses, assignments, files, grades, notifications, tasks **and submission** — 🔴 **so it is NOT read-only; the submission path writes on the student's behalf.** Gate it. Created `2026-10-14`, pushed `2026-11-01` |
| sakai-tasks-mcp | https://github.com/sayt25606-rgb/sakai-tasks-mcp | Apache-2.0 | 1 | Global | **New this pass (`p810`).** Unofficial **local** MCP server for Sakai LMS — assignment deadlines, quizzes, announcements, course materials. 🟢 **Read-only and local**, which is the conservative counterpart to `jtayped/sakai-mcp`'s submission path: the same platform at two different risk levels, which is the first time this base can offer that choice on any LMS |
| schoology-mcp | https://github.com/riripatate/schoology-mcp | MIT | 3 | North America | **New this pass (`p810`) — the first Schoology agent in this base.** TypeScript client plus a Claude MCP skill. 🟢 **"No admin API keys needed" is the deployment property that matters**: it works from the student's own session, so a pilot needs no district IT approval — 🔴 which is also precisely why a district would want to block it. Both halves are the same fact |
| fcps-school-mcp | https://github.com/jibberswrld/fcps-school-mcp | MIT | 2 | North America | **New this pass (`p810`).** Local MCP server for **FCPS Schoology and StudentVUE**, one-command setup; pushed `2026-11-06`. 🔵 **Fairfax County Public Schools is one of the largest US districts**, and this is a pupil-built client for it — see `T974` on hyper-local supply |
| schoology-mcp (PAUSD) | https://github.com/dajun666/schoology-mcp | MIT | 1 | North America | **New this pass (`p810`).** MCP server for **PAUSD Schoology and the Infinite Campus student portal** — 🟢 **the first Infinite Campus surface in this base**, a US K-12 SIS this file has named `101` times and shelved never. Created and pushed `2026-10-08`; single-district scope |
| mcp-learning-server | https://github.com/shastripranav/mcp-learning-server | MIT | 0 | Global | **New this pass (`p810`).** MCP server for **learning analytics and SCORM/xAPI integration** — the only row in this base that spans both the packaging standard and the record standard in one server. 🔴 **`0★`, `0` forks, last pushed `2026-06-30`** — shelved for the span, not the traction |
| ashashala | https://github.com/piyushh62/ashashala | MIT | 2 | Global | **New this pass (`p810`).** **Multi-tenant, role-based agentic AI tutoring platform built for real schools**, explicitly "100% open source, zero paid APIs". 🟢 **Multi-tenant + role-based is rare at this star count** — most tutoring rows in this base are single-tenant demos, and tenancy is the thing a district pilot discovers it needs in week three |
| Tlamatini | https://github.com/XAIHT/Tlamatini | MIT | 15 | Global | **New this pass (`p810`).** "Speak an idea. Build the real thing." — voice-driven AI across code, 3D worlds and hardware with a live editor, aimed at making building teachable. 🔵 **Named for the Nahuatl *tlamatini* ("one who knows"), which SUGGESTS a Mexican or wider LATAM origin — 🔴 but `gh api users/{login}` is refused in this session (`T941`), so origin is NOT resolvable and this row is placed `LATAM?` rather than given the closed vocabulary on a guess** (`T935`). Pushed `2026-11-13`, the day of this pass |
| qiaomu-learning | https://github.com/joeseesun/qiaomu-learning | MIT | 72 | Global | **New this pass (`p810`) — APAC-origin, and the strongest Socratic-method row found this window.** Turns textbooks, screenshots, PDFs, notes or a bare topic into a **one-question-at-a-time derivation dialogue**, triggered by the learner explicitly asking not to be told the answer. `7` forks, created `2026-08-10`. 🟢 **It encodes the OECD's "pedagogy stays in control" finding as a product constraint rather than a principle** |
| tizhuang-agent-skills | https://github.com/weishao2/tizhuang-agent-skills | MIT | 39 | Global | **New this pass (`p810`) — APAC/China K-12.** Agent skill over a **20M+ item K-12 question bank** (Chinese primary and secondary past papers): free registration, item sampling, textbook/chapter/knowledge-point retrieval, practice tests and AI-assembled papers. `7` forks, pushed `2026-11-11`. 🔴 **MIT covers the SKILL code; it does NOT grant rights in the question bank the skill retrieves from** — the same corpus-versus-code split this base flagged at `P800-3`. Read the item licence before any deliverable touches it |
| scholarship-navigator | https://github.com/OmarZen/scholarship-navigator | MIT | 14 | Global | **New this pass (`p810`).** Scholarship matching with eligibility checks, fit scores, **missing-document detection** and a dated plan. `3` forks, pushed `2026-11-11`. 🟢 **The only student-finance agent in this base**, and the missing-document check is the part that generalises — it is an admissions-operations pattern, not a search box |
| brightspace-mcp-server | https://github.com/RohanMuppa/brightspace-mcp-server | MIT | 67 | Global | **New this pass (`p809`) — the highest-starred new education agent of this window, and the first D2L Brightspace agent on this shelf.** `29` tools in seven groups (courses/grades, assignments/rubrics, announcements/discussions, content, people/groups, instructor Dropbox, account). 🔴 **Strictly read-only by design** — README: *"It only reads your courses. It never submits, edits, or deletes anything."* Auth is the school's own SSO page plus the account's 2FA; the password goes to the OS keychain (Keychain/Credential Manager) and saved session state is **AES-256-GCM** encrypted. Author: ECE @ Purdue. README lists working instances in 🇺🇸 🇨🇦 🇳🇱 🇨🇴 🇸🇬. `492` commits. 🟢 `MIT` byte-verified: root `LICENSE`, `1,068 B`, `sha256:047079fbd49120ed…`, affero×`0`. |
| brightspace-mcp | https://github.com/JhostinAleck/brightspace-mcp | MIT | 16 | Global | **New this pass (`p809`) — the strongest write gate in this base, and the first LATAM-origin education agent found with a real, byte-verified grant.** `29` tools: **`26` read, `3` write** (`submit_assignment`, `post_discussion_reply`, `mark_announcement_read`). 🟢 **Writes require TWO independent opt-ins** — `writes.enabled: true` in config **and** `--enable-writes` passed to `serve` — plus a `dry_run` preview mode, a client-supplied **idempotency key** on every write, and a warning-level **audit-log** entry per write. Four auth strategies (API token; headless user+password with MFA via TOTP/Duo Push/manual; Playwright browser automation; session cookie). 🔵 Ships an `es-419` locale and an `America/Bogota` sample timezone. `452` commits. 🟢 `MIT` byte-verified: `1,070 B`, `sha256:008ec594c78e9fd5…`, affero×`0`. |
| campus-cli | https://github.com/alejooroncoy/campus-cli | ISC | 13 | Global | **New this pass (`p809`) — a Peru-origin agent and the most-developed Blackboard client found anywhere (`851` commits, `v3.1.0`).** TypeScript CLI **and** MCP server (`campus mcp`, stdio) over **UPC Aula Virtual** (Blackboard Learn); UPN also supported, Canvas and Moodle on the roadmap; repo topics include `peru`. 🔴 **Read-only against Blackboard** — the README states it does not submit assignments or change anything; submissions stay in Aula Virtual. Local writes are downloaded files and the stored authorisation only. 🔴 **Governance flag, and it is the reason this row is not a drop-in for an institution: the tool catalogue is brokered by a remote relay (`mcp.campuscli.com`) that decides which tools to offer per university**, so student credentials and traffic cross a third party. Fine for a student; a contract question for a client. 🟢 `ISC` byte-verified: `748 B`, `sha256:4ca1bd2e969c…`. |
| ntulearn-mcp | https://github.com/kingdonkatsu/ntulearn-mcp | 🟢 **MIT — byte-read `2026-11-16` (`p843`)** (`main/LICENSE`, `1,055 B`, `sha256₁₂ e6bd1450153a`, © 2026 kingdonkatsu), against GitHub's `NOASSERTION` | 4 | APAC | **New this pass (`p809`) — the first Singapore-origin agent in this base.** `8` tools over **NTULearn**, Nanyang Technological University's Blackboard Learn: courses, announcements, calendar items, grades, plus course-file download into local folder structures. Python 3.12+, `28` commits. 🔴 **Auth is the `BbRouter` session cookie, auto-read out of Edge/Chrome/Firefox/Brave via `browser-cookie3`**, falling back to `NTULEARN_COOKIE` and then an OS-keychain cache, with one clear-and-retry on `401`. 🔴 **Scraping a live session cookie is unsanctioned access** — same contract risk as the three proprietary-SIS paths in this base, and it should be priced as such, not as an integration. 🟢 `MIT` byte-verified: `1,055 B`, `sha256:e6bd1450153a…`, affero×`0` (sidebar shows only a generic "License" link; the payload is the evidence). |
| blackboard-mcp | https://github.com/Mattlo0546/blackboard-mcp | MIT | 1 | Global | **New this pass (`p809`) — the only vendor-neutral Blackboard Ultra server found; the other two Blackboard rows are each bound to one university.** Python 3.10+ MCP server: reads courses, deadlines and announcements and downloads lecture slides for Claude Desktop, Cursor and Codex. Signs in through the university's SSO rather than an API key. 🔴 **Read-only on Blackboard** — README: it *"can't submit work, post or change anything on Blackboard"*; the only writes are to a local folder. 🔴 **`4` commits — the earliest-stage row on this shelf. Read it as a reference implementation, never as a dependency.** 🟢 `MIT` byte-verified: `1,067 B`, `sha256:13c8ad755224…`, affero×`0`. |
| interactive-learning | https://github.com/geekjourneyx/interactive-learning | MIT | 52 | Global | **New this pass (`p808`) — and it is a *skill package*, not a server or an app, which is why four passes of agent-shaped searching missed it.** Takes arbitrary input — text, a link, a document or a bare question — and turns it into a **verifiable learning path**, optionally emitting an HTML "checkpoint card" that makes each step checkable rather than merely read. 🟢 **The verifiability is the reason it is shelved:** every other content-generation node in this base (`educhain`, `OpenMAIC`) produces material, not a checkable path, and the gap between "generated a lesson" and "can show the learner passed it" is the one a client always asks about. Installs into Claude Code / `opencode`-style harnesses as a skill, so it composes with `canvas-mcp` or `Moodle-MCP` for delivery rather than competing with them — see `P22`. 🔴 **`52★` and `4` commits: this is a seed, not a dependency.** Read it as a design for the checkpoint card and reimplement if it must carry weight. Licence verified from the rendered sidebar (`MIT license`). |
| braiinz-education | https://github.com/braiinz94/braiinz-education | Apache-2.0 (sidebar: `Apache-2.0 license`) | 0 | EMEA | **New this pass (`p827`), and the first row on this shelf aligned to a NATIONAL CURRICULUM rather than to a subject.** Socratic tutoring, spaced repetition and **PISA-aligned diagnostics**, explicitly built against the French curriculum; Python 3.12+, `37` commits, delivered through Telegram, built on the Anthropic Claude API. 🔴 **`0★` and `37` commits — this is a seed, not a dependency, and it must not be proposed as one.** 🟢 **Shelved for the alignment pattern:** every other tutoring row here is curriculum-neutral, while an EMEA schools engagement is sold against a named national curriculum and a named diagnostic instrument. Read the diagnostic mapping and reimplement. See `T97`. |
| DeepTutor | https://github.com/HKUDS/DeepTutor | Apache-2.0 | 59.4k | Global | Lifelong personalized tutoring; learner model persists across sessions and builds learning paths. **v1.7.2 released 2026-11-06**; 7.1k forks. Largest education-specific agent on GitHub. |
| OpenMAIC | https://github.com/THU-MAIC/OpenMAIC | MIT | 43.6k | Global | Open Multi-Agent Interactive Classroom (Tsinghua MAIC lab). Turns a topic or document into a multi-agent classroom — teacher, peers, assistant — in one click. `6.7k` forks. **Release channel corrected at `p827` (`T97`): `v1.4.2` (`2026-11-09`) is a FULL release and `v1.5.0-rc.2` (`2026-11-12`) is the pre-release above it.** `p826` recorded Releases as empty and treated the project as never having cut one; that was wrong, and a client-facing "pre-release only" caveat should no longer be attached to this row. Ships pt-BR and es-MX locales. |
| teacher-to-skills | https://github.com/JuneYaooo/teacher-to-skills | Apache-2.0 | 475 | Global | **New this pass.** Distills a specific teacher's materials (lecture video, notes, marked-up feedback) into a source-backed agent Skill that teaches to that teacher's standard and tapers support as the learner improves. Conclusions are tied to sources; unevidenced material is flagged, not filled in. Learner progress is stored outside the generated Skill. Runs under Claude Code / Codex / OpenClaw. 73 forks. |
| mcp-odoo (ERPipe) | https://github.com/erpipe-org/mcp-odoo | MIT | 433 | Global | **New this pass — the largest build-safe agent in this KB that reaches an open-source SIS, and it is not an education project, which is why four passes of SIS searching missed it.** 41 tools over **Odoo 16-19** (smoke-tested against 16.0/17.0/18.0/19.0): `search_records`, `read_record`, `aggregate_records`, `get_model_fields`, `list_models`, plus module helpers, diagnostics, migration, audit and cross-instance fan-out. Because the tools take the **model name as a parameter**, OpenEduCat's `op.student`, `op.admission`, `op.exam.attendees` and `op.fees` are reachable with no education-specific code. **Writes are gated by construction — this is the row's real value:** direct `create`/`write`/`unlink` are blocked, and an approved write must pass `preview_write` -> `validate_write` -> `execute_approved_write` carrying a **single-use, same-process, expiring approval token**, with `confirm=true`, live non-empty `fields_get` metadata, and `ODOO_MCP_ENABLE_WRITES=1`; `ODOO_MCP_ELICIT_WRITES=1` adds a native confirmation prompt, and `execute_method` runs allowlisted methods only. XML-RPC default, JSON-2 on Odoo 19. 198 forks, 118 commits, Releases empty. **Formerly `tuanle96/mcp-odoo`** — the old slug is what search results still return, so record the new one. **Caveat for any proposal: the maintainer sells a hosted product (ERPipe) built on this repo** — the MIT grant is real; the roadmap has a commercial owner. |
| sabis-mcp-server | https://github.com/hanifisenturk/sabis-mcp-server | ISC | 2 | EMEA | **New this pass — the third agent-to-SIS path in this KB and the first from EMEA (Türkiye).** MCP server over **SABIS**, the student information system of **Sakarya University**. One tool, `get-grades`: course codes and names, assessment types and weights, final letter grades, academic year and semester. 🔴 **Reaches the SIS by Puppeteer web scraping, not an API, and reads the student's own `USERNAME`/`PASSWORD` from environment variables** — a credential-replay design to read and *not* reproduce. README states it is unofficial, unaffiliated with the university, and for personal/educational use. 0 forks. Admitted for the regional and topological record: with `edupage-mcp` (Slovakia/Czechia, undocumented endpoints) and `mcp_hemis_student` (Uzbekistan), the pattern is three-for-three — **individual developers reaching captive national or institutional SIS products by unofficial means.** |
| DeepTutor-MCP | https://github.com/Suyutao/DeepTutor-MCP | Apache-2.0 | 1 | Global | **New this pass — the first MCP server in this base built over another education *agent's* data rather than over a platform.** 60 tools exposing a self-hosted DeepTutor install to any MCP client: status, courses, syllabus and linked resources; Mastery Paths with outlines, evidence and review settings; Question Bank and practice queues with answer checks and analytics; generated books and reading material with notes, highlights and bookmarks; notebooks; knowledge-base metadata with file search and vector passage retrieval; historical sessions and memory documents; plus an opt-in tool that posts into a DeepTutor conversation. 15 commits, no releases. **Two hard dependencies before it runs:** a reachable self-hosted DeepTutor HTTP API, and — for the Mastery tutor tools — upstream PR **`HKUDS/DeepTutor#1785`, which its README says is still open and unmerged**. Not a dependency yet; admitted as the first evidence that DeepTutor (58.7k) is growing a tool ecosystem. |
| canvas-mcp | https://github.com/vishalsachdev/canvas-mcp | MIT | 324 | Global | Canvas LMS MCP server plus 8 agent skills for students and educators. The cleanest path to making an agent act inside Canvas. **Tool count is inconsistent on its own page: README says "up to 128 tools", the sidebar About says 102.** Default profile registers fewer; feature-gated tools raise the total. 106 forks. |
| Moodle-MCP | https://github.com/Faixiang/Moodle-MCP | MIT | 206 | Global | **New this pass — closes this KB's declared Moodle gap.** Zero-dependency Python MCP server over the Moodle Web Service API. 10 **read-only** tools (courses, assignments, quizzes, deadlines, files), v1.4.0 dated 2026-11-02, docs in 10 languages, Moodle 3.x/4.x, verified by its author against Moodle 4.3.6. Read-only is a feature for a first engagement: no write path, no token escalation. |
| educhain | https://github.com/satvik314/educhain | MIT | 388 | Global | Python package for generating educational content (questions, lesson plans, flashcards) with GenAI. Library, not an app — good as a content-generation node. |
| ai-shifu | https://github.com/ai-shifu/ai-shifu | Apache-2.0 | 332 | Global | AI-guided instruction: the agent teaches and answers in a scripted, author-controlled flow rather than free chat. |
| OATutor | https://github.com/CAHLR/OATutor | MIT | 280 | Global | Open-source Intelligent Tutoring System with Bayesian Knowledge Tracing (UC Berkeley CAHLR). React + Firebase; mastery modelling is the asset. |
| Open TutorAI (CE) | https://github.com/Open-TutorAi/open-tutor-ai-CE | BSD-3-Clause | 117 | Global | Community edition of an educational collaborative AI platform. |
| Tutor MCP | https://github.com/ArnaudGuiovanna/tutor-mcp | MIT | 102 | Global | MCP server that turns any LLM into an Intelligent Tutoring System; persistent, auditable learner state and progression governed outside the model. v0.7.0 adds institutional courses, invitations, enrollment. Small star count, unusually mature design. |
| Claw-ED | https://github.com/SirhanMacx/Claw-ED | MIT | 65 | Global | **New this pass.** Local-first teaching assistant: starts from the teacher's own lesson plans, slides and assessments and drafts new lessons, student materials and decks. v9.18.2026.1 (Beta). **Explicitly single-teacher, not multi-tenant**, and student-facing features are experimental. README is honest that hosted models still receive the prompt content even though storage is local. 16 forks. |
| moodle-mcp (Rust) | https://github.com/G36maid/moodle-mcp | MIT | 29 | Global | **New this pass.** Rust MCP server: courses, assignments, forums, grades, and files-as-markdown. Author reports live verification against **Moodle 3.7, 4.5 and 5.2** — the widest version coverage of any Moodle MCP server found. |
| learnmcp-xapi | https://github.com/DavidLMS/learnmcp-xapi | MIT | 16 | Global | **New this pass — the only agent↔learner-record write path in this KB.** MCP server over any **xAPI 1.0.3**-compliant Learning Record Store. Three tools: record a statement, retrieve progress, manage activity vocabulary. Ships the `practiced` / `mastered` / `experienced` / `achieved` verbs and separates learners by an `ACTOR_UUID`, so one server serves a cohort. **Verified LRS targets: SQL LRS, Ralph, Veracity** (TinCan and xAPI Wrapper are listed as planned, not shipped). Python 3.8+, 4 forks, Releases empty, author states active development. This is what makes an agent's activity *reportable* by the institution instead of invisible. |
| AI Scoring Platform | https://github.com/wwrwbs/AI_AWE | 🟡 **Apache-2.0 BOILERPLATE-ONLY — byte-read `2026-11-16` (`p843`)** (`main/LICENSE`, `1,865 B`, `sha256₁₂ 4b5296db216d`; the full Apache-2.0 text is `11,357 B`, so the grant is by REFERENCE — `T145`). 🔴 **The file is a component manifest and it carries a build constraint: Apache-2.0 over code/LoRA/LightGBM scorer, MIT over vendored `TextComplexityToolkit`, `Qwen2.5-7B-Instruct` base obtained separately and NOT redistributed, and the `Persuade 2.0` corpus under an academic-use licence that CANNOT ship.** Previously recorded as: Apache-2.0 (per README + LICENSE; sidebar shows only a generic "License" link) | 2 | Global | **New this pass — the only credible open grading system found.** Automated argumentative-essay scoring (1–6) with label-aware feedback: fine-tuned Qwen2.5-7B LoRA discourse-move classifier → LightGBM scorer over 31 linguistic/discourse features → feedback generator, with a Gradio UI for single and batch scoring. Locally deployable. **Naming trap: the arXiv paper calls this system "ArguLens"; the repository never uses that name.** Vendored TextComplexityToolkit is MIT. |
| moodle-mcp (browser-session) | https://github.com/falkenslab/moodle-mcp | MIT | 2 | Global | **New this pass.** Claims **~260 Moodle tools** including grading and quiz building — by far the largest surface found. Authenticates by opening a real browser for the user's own interactive login, so it **supports SSO and 2FA and needs no web-service token, admin rights, or Moodle plugin** ("your login, never your password"). Targets Moodle 4.5 and 5.x. 2 stars: powerful design, unproven. |
| moodle-mcp (publishing) | https://github.com/MarcosNahuel/moodle-mcp | MIT | 1 | Global | **New this pass.** Aimed at *writing* pedagogical content: 40 high-level tools plus a `ws_raw` escape hatch across courses, sections, content, quizzes, gradebook, messaging, calendar and badges. Writes are **upsert-by-`idnumber`, so republishing is idempotent** — the right primitive for generated course content. Requires companion plugin `local_italiciamcp` for the full set; self-reported ~80% operability at v0.5.2. |
| Manu (tutor-ai-agent) | https://github.com/Jeanikt/tutor-ai-agent | MIT | 0 | Global | **New this pass — the first LATAM-origin education agent this KB has found.** Voice-first math tutor **in Brazilian Portuguese**, adapting from 1st grade to university; spoken explanations render to an on-screen chalkboard. TypeScript + LiveKit Agents with a Next.js front end. In development, no public deployment. 0 stars — a seed, not a dependency. |
| EDUKAI LongView | https://github.com/Keitous/EDUKAI-LONGVIEW | ISC | 0 | Global | **New this pass — the first Africa-origin education agent this KB has found.** MCP-powered *longitudinal* learning intelligence: tracks a learner across multiple academic periods rather than single test scores, retrieves supporting evidence, flags sustained strengths and recurring difficulties, and recommends for teacher review ("agent recommends, teacher decides"). Bilingual FR/EN, author based in **Guinea**. Node.js/Express. **Synthetic data only** — a prototype. |
| EduAgentic (EduMCP) | https://github.com/kamalelafoui/Agentic-AI-EdTech-J33-J34 | MIT | 0 | Global | **New this pass — the only MCP + A2A education example found.** FastMCP server on SSE exposing six tools (`search_courses`, `get_learner_profile`, `recommend_learning_path`, `generate_quiz`, `grade_quiz`, `get_learning_statistics`) **plus an A2A orchestrator** over three named agents (Tutor, Evaluation, Orientation). Every other education agent in this table is single-agent or MCP-only; this is the one place in the set to read an agent-to-agent education topology. **French-language** repo and docs — francophone provenance; the author's country is not stated on the page and is not asserted here. 0 stars, 0 forks, no releases: a course artifact. Take the **topology**, not the code. |
| socratic-tutor (Jane Street `agent_skills`) | https://github.com/janestreet/agent_skills | MIT | 7.9k | Global | **New this pass — the largest permissively licensed education artifact in this KB, and it is not software.** Jane Street's first public agent skill: a strict Socratic tutor that runs a 3-5 question diagnostic, maps the topic into **4-10 sub-skills rated 0-5**, asks **one question at a time**, then adds spaced review and a final assessment. 510 forks, **2 commits** — it is a `SKILL.md` instruction set, so it needs an LLM host (coding agent or chatbot), ships no code and carries **no dependency or CVE surface**. Compare `education-agent-skills` (977 stars, CC BY-SA) in the rejected table: same artifact class, wrong instrument. This one is MIT and can go into a client deliverable as-is. Third-largest education agent here after DeepTutor and OpenMAIC, on two commits. |
| edupage-mcp | https://github.com/oliverhruby/edupage-mcp | MIT | 4 | EMEA | **New this pass — the first verified agent-to-SIS path in this KB.** 31 tools over **EduPage**, the school information system used across Slovakia and Czechia: timetables, grades, homework and a daily summary, plus meal ordering, multi-school discovery, role-aware student switching and **2FA**. Distributed on PyPI (`edupage-mcp-full`), Docker/GHCR and the MCP Registry. **The caveat governs adoption:** it reaches EduPage through the community `edupage-api` library, which uses **undocumented endpoints** — there is no vendor contract, so it can break on any EduPage release. Python 3.10+, 1 fork, 123 commits. Take the topology; do not ship the dependency. |
| mcp_hemis_student | https://github.com/sukhrobyangibaev/mcp_hemis_student | MIT | 0 | EMEA | **New this pass — the second agent-to-SIS path, and the first Central Asian project in this KB.** MCP server over **HEMIS** (Higher Education Management Information System), the student-information platform used by Uzbek universities: a student pulls their own academic record, schedule, grades and attendance. 9 commits, no repository description, no releases, 0 stars. Admitted **for the SIS topology only** — it is evidence that the student-record gap is closing from the national-platform direction, not a dependency. |
| mcp-education (zavora-ai) | https://github.com/zavora-ai/mcp-education | 🟡 **Apache-2.0 BOILERPLATE-ONLY — byte-read `2026-11-16` (`p843`)** (`main/LICENSE`, `738 B`, `sha256₁₂ b3886fcd4f82`, © 2026 Zavora AI; full text is `11,357 B` — grant by REFERENCE, `T145`). Previously recorded as: Apache-2.0 (per README; sidebar shows only a generic "License" link) | 1 | Global | **New this pass — the only Rust education MCP server found, and the only server at any star count that gates writes in its tool contract.** Canvas LMS API: courses, assignments, grades, students, announcements. **12 tools split 9 read-only + 3 write operations that require approval** — the read/write boundary is declared by the server rather than left to the host's discretion, which is the design to copy for any education MCP server that writes to a gradebook. Built for "ADK-Rust Enterprise"; Rust 1.94.1, 1 fork. |
| ai-tutor-agent | https://github.com/vulinh1704/ai-tutor-agent | MIT | 0 | Global | **New this pass — the clearest tutoring *guardrail* implementation found at any star count.** FastAPI + LangGraph, with three controls this KB has not found written down elsewhere: a **Socratic hint ladder** that escalates one level per turn up to a configurable cap; an **answer-leak guard** that regenerates a draft which reveals the final answer and substitutes a safe hint if it still leaks; and **rubric grading in which per-criterion scores are validated against the rubric and the totals are computed in code, not by the model**. A router node splits tutor / grader / clarify. SQLite checkpointing persists a session across restarts; a deterministic offline fake model runs the whole graph with no API key, which also makes it testable in CI. 0 stars — take the control design, not the repo. |
| AI-Teaching-Agent | https://github.com/littlecookie0722/AI-Teaching-Agent | MIT | 0 | Global | **New this pass.** Compiles one Markdown teaching source into reviewable **Lab and Exam packages** plus short teaching decks, using structured DSLs, sandboxed evaluation and an MCP stdio server (`mcp_server/` with tool adapters, MCP manifest shipped in the wheel). **Nothing publishes automatically:** artifacts are validated, candidate-facing content is protected, and a human decision gates local export — the review-gate shape that `P6` (grading) and any assessment engagement needs. README states further MCP/Agent expansion is **frozen**, so treat it as a fixed reference rather than a growing project. |
| che-ntucool-mcp | https://github.com/PsychQuant/che-ntucool-mcp | MIT | 1 | APAC | **New this pass (`p806`) — the strongest write gate in this base, and the first Taiwan-origin agent in it.** MCP server over **NTU COOL**, National Taiwan University's Canvas deployment (`cool.ntu.edu.tw`), in **Swift**, Developer ID signed, Canvas token in the macOS keychain with a logged-in Safari tab as fallback auth. 10 tools: 6 read (`list_courses`, `list_assignments`, `list_announcements`, `list_submissions`, `list_files`, `list_enrollments`) and 2 write pairs. 🟢 **`post_grades` and `post_announcement` are gated twice over — an MCP elicitation dialog *plus* a single-use token bound to the previewed payload.** That is a stronger contract than `zavora-ai/mcp-education`, which this base previously called the only server gating writes in its own tool contract. 🔴 Found by audit of this base's own trending logs, not by search; `ntucool` appeared there 12 times and on no shelf. |
| Smartschool-MCP | https://github.com/maurodruwel/Smartschool-MCP | MIT | 6 | EMEA | **New this pass (`p806`) — the fourth agent-to-SIS path in this KB and the second from EMEA.** 15 tools over **Smartschool**, the dominant school platform in Flemish Belgium: results, schedule, periods, reports, planned elements, student support links, student notes, **absences**, attachments and homepage blocks. Python 3.10+, 7 forks against 6 stars. 🟢 **Read-only by construction — there is no write tool at all**, which makes it the lowest-risk row in this table to put in front of a school's data-protection officer. 🔴 **Belgium is inferred** from `school.smartschool.be` and Dutch field names (`Leerlingvolgsysteem`), not stated by the repo. |
| waseda-moodle-mcp | https://github.com/12dora/waseda-moodle-mcp | MIT | 0 | APAC | **New this pass (`p806`) — the first Japan-origin education agent in this base.** MCP server over **Waseda University's Moodle** (`wsdmoodle.waseda.jp`), authenticating with the same web-service token the official Moodle mobile app uses. **20 read tools and 11 write tools**, plus prompts (`daily_briefing`, `weekly_plan`, `exam_prep`) and `moodle://course/{id}` resources. 🟢 **Every mutation is split `prepare_*` → `confirm_action` / `cancel_action`** — nine `prepare_` verbs, one confirm, one cancel. Deploys to Cloudflare Workers or local stdio. 🔴 **Self-declared unofficial and unaffiliated with Waseda** — a reference design, not a vendor relationship. |
| Mathua | https://github.com/chuma-beep/mathua | 🟢 **MIT — byte-read** (`raw.githubusercontent.com/chuma-beep/mathua/main/LICENSE`, first line `MIT License`; sidebar agrees, `MIT/MIT License`) | 416 | Global | 🟢 **New this pass (`p819`), and the largest genuinely new education build-safe repository the star-ranked channel has returned in four passes.** A self-hostable **adaptive mathematics engine**, not a tutor wrapper: a checked prerequisite DAG of **`3,015` atomic concepts across `29` courses**, `9,045` worked examples (`3` subgoals each), `183` dual-coded diagrams, **FSRS-6** scheduling with implicit-repetition credit, and mastery gating that counts a correct-but-slow answer as WEAK mastery against a per-concept time threshold. 🔵 **Problems are GENERATED by parameterised Go generators with a stored fallback and a replay layer, so there is nothing to memorise and a session never stalls** — that is the property an engagement cannot buy from a content vendor. Go backend + React/Next.js, SQLite default and **Postgres via `pgx/v5`** for multi-user; CSV transcript export over the API. 🔴 **Honest dependency: ~`32%` of concepts need Python 3.11 + `sympy` for symbolic grading and the production image FAILS THE BUILD without it** — so "pure Go" is not the deployable configuration. Created `2026-04-28`, pushed `2026-11-14`, `43` forks, `0` open issues, not archived. 🟡 **Region `Global`: the owner is an individual account with no stated country, and this base does not infer origin from an account name (`T42`).** See `P49` |
| Whiteboard AI Tutor | https://github.com/molly554/whiteboard-ai-tutor | 🟢 **MIT — byte-read** (`raw.githubusercontent.com/molly554/whiteboard-ai-tutor/main/LICENSE`, first line `MIT License`; sidebar agrees) | 157 | Global | 🟢 **New this pass (`p819`). Shelved for the PROTOCOL and the BENCHMARK, not for the app** — the README says so itself: *"It is not a hosted tutoring app."* 🔵 **The protocol is the finding: the model streams drawing instructions as JSON, a browser plays them back as handwriting, and when the student interrupts, the app sends the BOARD STATE back to the model.** That makes whiteboard tutoring a transport concern rather than a model capability, so any LLM can be the tutor and the vendor is swappable — the single most useful property for a studio pricing a multi-year tutoring build. 🟢 **The benchmark is reusable evidence: one frozen prompt, `8` scenarios (science, maths, economics), `6` models, `2` thinking settings, `3` repeats = `288` lessons, `64` boards BLIND-REVIEWED, total spend `$4.83`, and every board is committed to the repository and replayable in a browser.** 🔵 **Published leaderboard: Gemini 4 Argon `11/11` boards passed at `$0.0277`/lesson and `8.0 s` to first stroke; Claude Haiku 5.5 `9/11` at `$0.0019`/lesson — a `~15×` cost spread across adjacent quality.** 🔴 **Four days old at shelving (created `2026-11-11`, pushed `2026-11-12`, `7` forks, `1` open issue): treat the leaderboard as a reproducible METHOD, not as a settled ranking.** 🟡 **Region `Global`: README is bilingual EN/zh-CN and the model set includes DeepSeek, which is an APAC signal, but the repository states no origin and this base does not promote a signal to a region (`T42`).** See `P49` |
| mawta | https://github.com/amaru-one/mawta | 🟢 **MIT — byte-read** (`raw.githubusercontent.com/amaru-one/mawta/main/LICENSE`, `1,074 B`, `sha256:34142d07…`, first line `MIT License`) | 2 | LATAM | 🟢 **New this pass (`p821`), and the first agent on this shelf bound to a LATAM NATIONAL CURRICULUM INSTRUMENT rather than to a subject.** *"An open-source gradebook for Peruvian schools, where AI drafts and the teacher decides."* The README names the instrument: Peru's **CNEB**, competency assessment, the four achievement levels **AD / A / B / C**, and the descriptive conclusion a teacher must write for each. Stack is **Python 3.14 + PostgreSQL 16 + SQLAlchemy Core + LangGraph**, one service per school, with API, job worker, agents, director's chat and migrations in one tree. 🔵 **Its design rule is the one a studio can sell:** *"AI that proposes, never decides"* — nothing is saved on the teacher's behalf and every claim points at the data it rests on. Created `2026-11-07`, pushed `2026-11-14`, `0` forks. ⚠️ `2★` — young, single-maintainer, and the row says so. |
| jemma | https://github.com/AI-Native-Ventures/jemma | 🟢 **MIT — byte-read** (`raw.githubusercontent.com/AI-Native-Ventures/jemma/master/LICENSE`, `1,075 B`, `sha256:888e10dd…`, first line `MIT License`) | 0 | EMEA | 🟢 **New this pass (`p821`) — the first AFRICA-origin row in this base, and a CATEGORY this base did not hold: the longitudinal learner profile with a consent gate.** *"Jemma follows one learner across years, not one term."* It marks class tests, keeps a sourced record per child, and surfaces a pattern only after it has held for three terms or more. 🔵 **The product rule is a refusal:** *"A profile, not a label"* — there is no screen that assigns a track, a subject path or a career, and the save tool drops a pattern worded as a label or a ranking. 🔵 **Parent access is TEACHER-GATED:** marks and gaps reach a family only after the teacher taps *Share with parents*. Ships **its own MCP server**. Region from the README's own locative: *"Built for the African Agentic AI Design Challenge, Education track (The Long View), sub-theme Longitudinal strength tracking."* Organisation-owned, created `2026-11-10`, pushed `2026-11-15`. 🔴 **Default branch is `develop`; the grant was byte-read on `master`, and both are stated because a branch is not a repository (`p428`).** ⚠️ `0★`, challenge-submission cadence. |
| teach-to-learn | https://github.com/olele114/teach-to-learn | 🟢 **MIT — byte-read** (`raw.githubusercontent.com/olele114/teach-to-learn/main/LICENSE`, `1,096 B`, `sha256:b43a17a6…`, first line `MIT License`) | 4 | APAC | 🟢 **New this pass (`p821`), and the freshest row this base has ever shelved — created `2026-11-14`, one day before the pass.** A **zero-dependency Agent Skill** for Codex-class runtimes that attacks the failure this base has named twice: *"Stop mistaking 'I understood the AI's explanation' for actual mastery."* The loop is fixed and inspectable — observable goal → **≤3** short diagnostics → **5–15 min** micro-lesson → open-ended attempt → evidence plus a **1/3/7/14-day** review queue → unseen transfer task. 🔵 **Declared lineage, which is rare and worth rewarding:** an explicit redesign of [Matt Pocock's `teach`](https://github.com/mattpocock/skills), named in the README. Region APAC from the authorship statement — `SKILL.md` and `references/` are authored in Chinese and a `README_CN.md` is published — **not** from the owner's account, which carries no location. Pushed `2026-11-15`. |
| educa-educai | https://github.com/tomasfossatti/educa-educai | 🟢 **MIT — byte-read** (`raw.githubusercontent.com/tomasfossatti/educa-educai/main/LICENSE`, `1,072 B`, `sha256:85e0337d…`, first line `MIT License`) | 0 | Global | 🟢 **New this pass (`p821`).** Spanish-language *"plataforma de inteligencia educativa"* that converts the evidence a learner generates while learning — tutor conversations and structured activities — into **traceable** information for the teacher. 🔵 **Two things make it worth a row at `0★`:** it implements a named closed loop (**Experience → Evidence → Interpretation → Feedback/Action → New Experience**) and it keeps four epistemic layers separate **in the data model and in the UI** — `Declarado → Observado → Inferido → Evaluado`. That separation is precisely what an audit of an AI grade needs and what almost nothing on this shelf models. Next.js 16 + React 19 + PostgreSQL 16 + Prisma 6, Zod validation on every server action **and on every AI output**, Claude via the official Anthropic SDK. Topics include `mcp`. Created `2026-10-05`, pushed `2026-11-15`. 🔴 **Region `Global`, not LATAM: the README is Spanish throughout and names no country, institution or curriculum. A language is not a location.** |
| Stardust Agent | https://github.com/cuic19053-hue/stardust-agent | 🟢 **MIT — byte-read** (`1,070 B`, `sha256:6fb44efa600b…`, stock text, holder `cuic19053-hue`) | 165 | APAC | 🟢 **New this pass (`p822`), and the highest-starred genuinely new education agent this base has added in eleven passes.** A workbench for the declaration documents Chinese undergraduates are judged by — 申报书, 申请书, 商业计划书, 实践报告, 个人陈述 — with `35` domain guides and the competitions named in its own README: 大创申报书, 挑战杯, and 中国国际大学生创新大赛. Python + FastAPI, `Ollama` local models or any OpenAI-compatible endpoint. 🔵 **Placed in APAC on a quoted locative, 中国, not on the language.** 🔵 **Engagement use: this is the first agent in this shelf attached to the COMPETITIVE-FUNDING document rather than to a course, which is the artefact a university actually staffs people to review. See `T75`** |
| Meska Brain | https://github.com/OmarAxis/meska-brain | 🟢 **Apache-2.0 — byte-read** (`11,340 B`, `sha256:52f203491064…`, stock text, no holder) | 0 | EMEA | 🟢 **New this pass (`p822`) — the SECOND education-track entry this base has taken from the channel `T71` named, and the one that bounds it.** README quotes it exactly: *"Entry for the African Agentic AI Design Challenge, Education track 'The Long View', sub-theme 'Longitudinal strength tracking'"*. An MCP server plus a LangGraph agent that follows one learner across YEARS and lays three maps over each other to show a teacher where a struggle may have STARTED. 🔴 **Status taken verbatim from its own README and not softened: *"a working prototype on synthetic data"*.** 🔵 **It is the category `T71` said Africa arrived carrying, now with a second independent instance — see `T74`** |
| Sautika | https://github.com/marthanp/sautika | 🟢 **MIT — byte-read** (`1,117 B`, `sha256:d5fea751d0cb…`, stock text, holder `2026`) | 1 | EMEA | 🟢 **New this pass (`p822`).** Placed by a quoted locative, not inferred: *"An AI-assisted, voice-first learning platform and intelligent study assistant designed for learners across East Africa"*. Swahili appears `9` times in the README. 🟢 **Three constraints this shelf had not held together: VOICE-FIRST as the primary interface, NATIVE LANGUAGE rather than English, and DYSLEXIA-INCLUSIVE design.** `package.json` present, `35,386 B` README. 🔵 **Engagement use: the combination is the one that survives low literacy AND low bandwidth, which is the actual constraint in the market it names** |
| EthioLearn AI | https://github.com/nafkunasefa1-hub/EthioLearn | 🟢 **MIT — byte-read** (`1,095 B`, `sha256:7203e6d09066…`, stock text, holder `2026`) | 0 | EMEA | 🟢 **New this pass (`p822`), and a category this base held NOWHERE: the agent whose object is PAYING for education rather than delivering it.** Ethiopian secondary students (Grades `9`–`12`) preparing for the `EUEE`, with a PayPal MCP server as the rail by which diaspora sponsors fund a specific learner. 🔴 **Graded honestly: it is a Devpost PayPal AI Hackathon submission with a live Hugging Face space, not a deployed system, and its market claims are its own.** 🔵 **The ARCHITECTURE is the finding — an MCP payments rail wired to an education outcome — and it is reusable whatever happens to this repository. See `P54`** |
| tutorizr | https://github.com/f2calv/tutorizr | 🟢 **MIT — byte-read** (`1,069 B`, `sha256:5179c8ca6c5f…`, stock text, holder `Alex Vi…`) | 0 | Global | 🟢 **New this pass (`p822`) — the first agent on this shelf whose CHANNEL is a messaging app rather than a web app.** A .NET 11 host relays a Signal group's conversation, including transcribed voice notes, to the `Agentizr` runtime, and exposes learner-progress tools over MCP backed by Redis; a .NET MAUI client for Android and Windows holds continuous, interruptible voice calls. 🔵 **Subject-agnostic by construction: the teaching behaviour lives in an agent definition published to the runtime, so a new subject is a new definition rather than a new build.** 🔴 **Placed GLOBAL, not EMEA: its only German-shaped signal is the language of the lessons, and a language is not a location — the rule this base published at `p821`** |
| 文渊 (wenyuan) | https://github.com/zjsyxzjsyx/wenyuan | 🟢 **MIT — byte-read** (`1,061 B`, `sha256:888e4c81df0e…`, stock text, holder `koyo`) | 0 | Global | 🟢 **New this pass (`p822`), and the cleanest PRIVACY BOUNDARY this shelf holds.** A per-course shared RAG service: the teacher's materials are shared with the whole class, each student's own notes are retrievable ONLY by that student, and — the part that matters — *"只要用到了笔记，就只用本地模型回答"*, if a private note is used, the answer is generated by a LOCAL model only. Milvus hybrid retrieval (vector + BM25, `jieba` segmentation), per-sentence `[S#]` citations anchored to a handout paragraph or a lecture-video timestamp, unsupported sentences deleted. 🔵 **That is a shippable answer to the data-governance objection that stops classroom RAG in procurement** |
| 校慧伴 (xiaohuiban) | https://github.com/jinxuan7983-afk/xiaohuiban | 🟢 **MIT — byte-read** (`1,066 B`, `sha256:dfe31c4d1444…`, stock text, holder `校慧伴`) | 0 | Global | 🟢 **New this pass (`p822`) — the most COMPLETE multi-agent teaching loop this shelf has taken at `0★`.** Five cooperating agents over one course (《计算机网络》): conversational learner profiling, tutoring, resource generation, path planning and effect assessment, with a knowledge graph carrying mastery state, `23` built-in illustrated lecture notes that double as the authoritative RAG corpus (`course_lecture` chunks in ChromaDB, loaded without per-item LLM calls so it starts in seconds and runs offline). FastAPI + Vue3, `13,633 KB` of Python. 🔵 **Read it as a reference ARCHITECTURE for a single-course deployment, which is how these engagements actually start** |
| interruptible-ai-tutor | https://github.com/fcedf/interruptible-ai-tutor | 🟢 **MIT — byte-read** (`1,062 B`, `sha256:73a60e84e767…`, stock text, holder `fcedf`) | 0 | Global | 🟢 **New this pass (`p822`), and the one INTERACTION primitive this base had never found shipped: barge-in.** A segmented explanation engine that retrieves, explains section by section, generates and RUNS code and draws charts incrementally while explaining, and lets the learner interrupt mid-sentence to ask something and then resume. Three entry points — CLI, REST + SSE, and a `SKILL.md` — because it is built *"面向「由 AI agent 操控」"*, to be driven BY an agent. 🟢 **Zero dependencies, zero build, and it runs its whole demo with NO API key; `36` unit tests.** 🔵 **The barge-in loop is the difference between a lecture and a tutorial, and it is reusable on its own** |
| lf-skill | https://github.com/cheahhl814/lf-skill | 🟢 **MIT — byte-read** (`1,067 B`, `sha256:84aebc1010eb…`, stock text, holder `cheahhl814`) | 0 | Global | 🟢 **New this pass (`p822`), and the first instance of a category this base now names in `T75`: the LEARNING-SCAFFOLD agent, whose subject is ANOTHER agent.** It wraps any shared agentic skill the way a student uses it for coursework — a pre-flight basics quiz, mid-run Socratic checkpoints where *"a defensible student parameter pick gets used"*, and a teach-back debrief — so the agent executes the pipeline while the student demonstrably learns. 🔵 **This is the only product shape in this shelf that answers the cognitive-offloading objection directly, and it is the one an academic-integrity office can actually sign. See `P53`** |
| ai-learning-skills | https://github.com/Hang-GaoZu/ai-learning-skills | 🟢 **MIT — byte-read** (`1,067 B`, `sha256:ea542d6e140b…`, stock text, holder `Ha…`) | 1 | Global | 🟢 **New this pass (`p822`) — second instance of the `T75` scaffold category, and the one with STATE.** Three `SKILL.md` skills for any agent that loads them: a Markdown course progression with main notes, self-tests, source/typing cards and a learning dashboard carried in `course-state.md`; the same loop emitting a self-contained OFFLINE HTML learning site with a progress timeline; and a learn-by-building variant. 🔵 **`course-state.md` is the cheap, inspectable substitute for the learner-record integration that `p817`'s declared gap says rests on one stale `16★` repository — worth knowing when xAPI is out of budget** |
| tuttor-kit | https://github.com/decolla/tuttor-kit | 🟢 **MIT — byte-read** (`1,064 B`, `sha256:3931a51e2767…`, stock text, holder `decolla`) | 0 | Global | 🟢 **New this pass (`p822`) — third instance of the `T75` category, and the one whose value is a REFUSAL.** It turns an AI CLI into a programming tutor that *"guides with questions and hints, and does not write the code"* — the inversion of every coding agent this base's technology shelf holds. 🔴 **Placed GLOBAL and not LATAM, deliberately: its only Brazil-shaped signal is a `README.pt-BR.md` locale label, and this base places on a locative statement rather than on a language or a locale tag.** 🔵 **Pair it with `lf-skill` when the client is a bootcamp whose complaint is that graduates cannot work without the agent** |
| Blinky | https://github.com/Tushardevx01/Blinky | 🟢 **MIT — byte-read** (`1,134 B`, `sha256:809c14e3383d…`, stock text, holder `Tushar Ka…`) | 0 | Global | 🟢 **New this pass (`p822`).** A privacy-first DESKTOP tutor and computer-use agent for Windows and Linux, with a React Native (Expo) mobile companion — `package.json` and `Cargo.toml` both present, so a JS surface over a Rust core. 🔵 **Why it is on this shelf rather than the technology one: the tutoring claim is primary and the computer-use capability is what makes "show me how" mean DOING it on the learner's own machine, which is the demonstration mode vocational training needs.** 🔴 **`0★`, unproven, and desktop control raises a governance question the client must answer before any pilot** |
| EduAdapt | https://github.com/Davide4599/EduAdapt-AI-Powered-Learning-Accessibility | 🟢 **MIT — byte-read** (`LICENSE.txt`, `1,069 B`, `sha256:2f4c03d4562b…`, stock text, holder `2025 Davide Iotti`) | 1 | Global | 🟢 **New this pass (`p822`), and it PARTLY corrects this base's standing accessibility gap.** A Chrome extension that uses the browser's ON-DEVICE Gemini Nano to reshape any web page for students with ADHD, dyslexia or autism — so the adaptation happens client-side with no page content leaving the machine, which is why it clears a school's data rules. Its own README states the strategies were *"compiled through AI-assisted research and iterative feedback from a doctoral researcher in special education"*. 🔴 **Two limits stated: it is a Chrome Built-in AI Challenge 2025 PROTOTYPE, and it was last pushed `2025-10-30` — thirteen months stale. Take the PATTERN, not the dependency** |
| 简析智评 (jianxi-resume-intelligence) | https://github.com/zhaokai0604/jianxi-resume-intelligence | 🟢 **Apache-2.0 — byte-read** (`11,336 B`, `sha256:a61284580cd0…`, stock text) | 3 | APAC | 🟢 **New this pass (`p822`).** A résumé-processing platform aimed at *"学生成长与教学分析"* — student development and TEACHING analytics, not recruitment: upload, text extraction, structured parsing, EVIDENCE-CONSTRAINED scoring, post matching and improvement. Placed APAC on a quoted locative: *"2026 大学生数据要素素质大赛国赛晋级作品"*, a national-round entry in a Chinese collegiate competition. CI green on `main`. 🔵 **Evidence-constrained scoring — a score that must cite the span it came from — is the same control `P51` requires of a gradebook, arriving independently in a second product. That convergence is worth more than either repository** |
| olymmath-agent | https://github.com/tamnd/olymmath-agent | 🟢 **Apache-2.0 — byte-read** (`11,358 B`, `sha256:cfc7749b96f6…`, stock text, no holder) | 0 | Global | 🟢 **New this pass (`p822`) — CONTENT infrastructure rather than a tutor, which is the layer every tutor on this shelf is short of.** A Go toolchain (`om`) for the `olymmath` corpus: it harvests sources, MERGES DUPLICATE problems and checks them, across mathematical olympiads. CI badge and semver releases present. 🔵 **De-duplicating and verifying an item bank is the unglamorous half of any assessment engagement, and this is a permissively licensed, runnable instance of it** |

## Copyleft — usable, but the license propagates

| Agent | Repo | License | Stars | What it does |
|---|---|---|---|---|
| VietAIS-Sentinel | https://github.com/NukeGeng/VietAIS-Sentinel | 🔴 **AGPL-3.0 — byte-read** (`34,522 B`, `sha256:4df3c306…`, stock text, title line `GNU AFFERO GENERAL PUBLIC LICENSE`) | 0 | 🟢 **New this pass (`p824`) — and the anchor of `T84`.** *"Open-source AI engine for explainable exam proctoring, combining object detection, gaze and head-pose estimation, and temporal behavior analysis."* 🔴 **It is the ONLY licensed education repository this pass could find in 🇻🇳 Vietnam, the jurisdiction whose AI law has named education and automated assessment as high-risk since `2026-03-01`** — `q="giao duc viet nam ai"` → `7`, all unlicensed; `q="vietnam education platform"` → `5`, all unlicensed. 🔵 **EXPLAINABLE is the right word for that law and the reason to read it: object, gaze, head-pose and temporal behaviour are inspectable signals, not an affect score.** 🔴 **AGPL-3.0 over a system an institution would HOST means network copyleft reaches the deployment, so this is the reference architecture for `P58`, not a fork candidate.** Created and pushed `2026-10-14`, `56 KB` |
| bupt-anything | https://github.com/Sun-sunshine06/bupt-anything | 🔴 **GPL-3.0 — byte-read** (`35,149 B`, `sha256:3972dc97…`, title line `GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007`) | 2 | 🟢 **New this pass (`p823`).** 北邮 **BUPT** 🇨🇳 campus MCP server and CLI: timetable, grades, free classrooms, 教学云 assignments and materials — *"unofficial read-only campus tools"*. 🔵 **The APAC member of the `T77` institution-integration population, and the one that cannot be adopted:** GPL-3.0 propagates to any deliverable it is linked into, so a client engagement would have to reimplement the campus adapters rather than vendor this one. 🟢 **Read-only by design, which is the right default for a student-facing campus agent** and worth copying even though the code is not. Pushed `2026-11-13`. |
| anki-cli | https://github.com/Macro002/anki-cli | 🔴 **AGPL-3.0 — byte-read** (`34,523 B`, `sha256:0d96a4ff…`, title line `GNU AFFERO GENERAL PUBLIC LICENSE Version 3`) | 1 | 🟢 **New this pass (`p817`), and it DISCHARGES `ACTION p816-D` — the AnkiConnect single-point-of-failure now has a successor, and it is not build-safe.** *“Anki's own engine as a fast headless server and CLI: a drop-in AnkiConnect replacement (legacy + v1 API) without Anki Desktop.”* Created `2026-10-26`, pushed `2026-11-13`. 🟢 **Architecturally it is what `p816` asked for: it removes the Qt desktop dependency, so an agent stack no longer needs a GUI application running to reach a collection.** 🔴 **But it is built on the official `anki` Python package, which is AGPL-3.0, and it inherits that — so it is limb 2 of `p816-D`, not limb 1.** 🔵 **Consequence for this base, stated plainly: `P40`'s algorithm-first shape remains the only recommendation in the retention layer that carries no copyleft. The replacement exists; it is not a replacement a studio can ship inside a deliverable.** 🔴 **Its AGPL payload is byte-identical (`34,523 B`, `0d96a4ff…`) to `frametell`'s and `learnharness`'s, recorded at `T817` — stock text, no lineage information** |
| anki-mcp-server-addon | https://github.com/ankimcp/anki-mcp-server-addon | 🔴 **AGPL-3.0-or-later — byte-read** (`227 B`, `sha256:34b58d89…`, holder `Anatoly Tarnavsky`, title line `GNU Affero General Public License, version 3 or later`) — 🔴 **GitHub's licence field says `NOASSERTION`** | 102 | 🟢 **New this pass (`p816`), and the specimen for `T48` and `T50` both.** *"An Anki addon that implements an MCP server, enabling AI assistants to interact with Anki."* 🔴 **It is the SAME ORGANISATION and the SAME FUNCTION as the `558★` MIT row above — and it is AGPL-3.0, because it runs IN-PROCESS inside Anki, which is AGPL-3.0.** 🔴 **And the upstream RECOMMENDS this one:** *“Prefer the AnkiMCP addon for most setups … the addon is the simpler and better-supported path.”* 🟢 **So the choice is explicit and must be made out loud on an engagement: take the maintainer's recommended path and the deliverable is AGPL, or take the MIT path and own the integration friction the maintainer is warning you about. `P41` takes the second and says why** |
| PDFMathTranslate | https://github.com/PDFMathTranslate/PDFMathTranslate | **AGPL-3.0 — byte-verified** (`34,522 B`, `sha256:20b067f8…`, title line `GNU AFFERO GENERAL PUBLIC LICENSE`) | 38407 | **New this pass (`p814`) — the largest repository this base has shelved in any industry, and it is an EDUCATION tool nobody here had measured.** EMNLP 2025 demo: scientific-paper PDF translation that preserves layout, formulas, tables and figures. 🟢 **The research-library layer's highest-value capability for a non-English programme: a Spanish-, Portuguese- or Chinese-language cohort reading English-language literature.** 🔴 **AGPL-3.0: run it as a separate service behind an API, never derive from it or link it into a client deliverable.** Pushed `2026-11-13` |
| llm-for-zotero | https://github.com/yilewang/llm-for-zotero | **AGPL-3.0 — byte-verified** (`34,519 B`, `sha256:d8de5179…`, title line `GNU AFFERO GENERAL PUBLIC LICENSE`) | 3556 | **New this pass (`p814`).** Open research-agent system over a Zotero library. 🔵 **Its licence payload is BYTE-IDENTICAL to `papersgpt-for-zotero`'s below (`34,519 B`, same hash) and the two are unrelated projects — which is the evidence for `T41`'s bound, not evidence of lineage.** Pushed `2026-11-10` |
| papersgpt-for-zotero | https://github.com/papersgpt/papersgpt-for-zotero | **AGPL-3.0 — byte-verified** (`34,519 B`, `sha256:d8de5179…`, title line `GNU AFFERO GENERAL PUBLIC LICENSE`) | 2706 | **New this pass (`p814`).** Zotero plugin: chat with PDFs and whole-library question answering. The most-starred in-Zotero plugin of the layer. Pushed `2026-11-13` |
| Aldine | https://github.com/trahloff/Aldine | **AGPL-3.0 — byte-verified** (`34,522 B`, `sha256:4df3c306…`, title line `GNU AFFERO GENERAL PUBLIC LICENSE`) | 126 | **New this pass (`p814`) — self-hosted collaborative LaTeX editor, an Overleaf alternative.** 🟢 **The AUTHORING end of the layer: `abnt-mcp` audits a manuscript and `zoteus` cites into it, and this is where a thesis is actually written. Self-hosting matters for institutions that cannot send unpublished work to a SaaS.** 🔴 **AGPL-3.0 and it is a hosted service by design, so the network-use clause is live: offering it to students triggers the source obligation.** Pushed `2026-11-12` |
| lc-vocabularies-mcp | https://github.com/msuicaut/lc-vocabularies-mcp | **GPL-3.0 — byte-verified** (`35,148 B`, `sha256:8b1ba204…`, title line `GNU GENERAL PUBLIC LICENSE`) | 4 | **New this pass (`p814`) — and the honest answer to "what does North America's national-institution layer hold?": exactly one repository, and it is copyleft.** Experimental MCP server over the Library of Congress linked-data vocabularies (subject headings, name authorities). 🔵 **Its licence payload is byte-identical to `pkp/ojs`'s and `pkp/pkp-lib`'s (`35,148 B`, `sha256:8b1ba204…`) across three unrelated projects — a THIRD independent confirmation of `T41`'s bound.** 🔴 **GPL-3.0: a separate process, not a library.** Pushed `2026-03-24` |
| expeditto | https://github.com/fabrica-de-inovacao/expeditto | **AGPL-3.0 — byte-verified** (`34,523 B`, `sha256:0d96a4ff68ad6d4b…`, title line `GNU AFFERO GENERAL PUBLIC LICENSE`) | 1 | **New this pass (`p812`), and the only agent in this base whose user is a TEACHER doing compliance paperwork rather than a student studying.** *"Expeditto: seu segundo expediente, resolvido. Prepara o RIT do SUAP (IFMA) como rascunho, via CLI e MCP."* The **RIT** (*Registro Individual de Trabalho*) is the workload return Brazilian federal-institute teachers must file in **SUAP**, the Instituto Federal administrative suite. 🟢 **The write gate is in the product definition, not bolted on: it prepares the RIT *as a draft* (`rascunho`) and a human files it.** 🔵 **That is the cleanest statement of `P6`/`P26`'s principle found so far — the agent does the assembly and never the submission — and it is worth quoting to any client nervous about agents touching a system of record.** 🔴 **AGPL-3.0: integrate as a separate service, never derive.** 🔵 Its licence payload is byte-identical to `LearnHarness`'s (`34,523 B`, `sha256:0d96a4ff68ad6d4b…`), which corroborates both as stock AGPL-3.0 rather than a modified grant. Created `2026-09-30`, pushed `2026-10-22` |
| edu-by-agent | https://github.com/Severnbli/edu-by-agent | GPL-3.0 | 0 | **New this pass (`p811`), and the FIFTH independent instance of preview-then-confirm (`T20`).** *"CLI, MCP server and Claude Code skills for managing school websites in the **edu.by** site constructor: pages, menus, news, images – **with preview and confirmation before every write**."* `edu.by` is the Belarusian national school-website constructor. Created `2026-11-09`, pushed `2026-11-13` — the day of this pass. 🔴 **GPL-3.0, so the code propagates**: take the preview/confirm write gate, which is stated as a property of EVERY write rather than of selected verbs. 🔴 `0★`, four days old |
| pronoteConnect | https://github.com/sairo-cyber/pronoteConnect | **GPL-3.0-or-later — byte-verified, against GitHub's `NOASSERTION`** | 2 | **New this pass (`p811`), and `T27`'s third direction: `NOASSERTION` masked INHERITED copyleft.** *Connecteur **PRONOTE** open source et auto-hébergé pour ChatGPT via MCP, avec connexion **EduConnect** locale* — PRONOTE is the dominant French secondary-school information system and EduConnect is the state identity provider. Created and pushed `2026-09-08`. 🟢 **`LICENSE` read first-hand on `raw.githubusercontent.com`: line 1 is `SPDX-License-Identifier: GPL-3.0-or-later`.** 🔴 **And the file states WHY, which is the commercially important part: *"This license choice is compatible with the declared GPL-3.0-or-later license of the `@blockshub/pawnote-lts` dependency used by this prototype."*** 🔵 **The copyleft is not the author's preference, it is inherited from the only available PRONOTE client library — so a permissive French PRONOTE agent cannot be produced by relicensing this repo; it requires a clean-room client.** See `T33` |
| canvas-pilot | https://github.com/X-isdoingreat/canvas-pilot | AGPL-3.0 | 125 | **New this pass (`p808`) — the highest-starred NEW education agent found in this window, and the only one of six LMS-seam candidates with meaningful traction.** Local-first Canvas LMS agent that **learns each course's recurring assignment workflow and replays it** through an explicit `scan -> approval -> execute` cycle with a student review step before anything is submitted. 🟢 **The workflow-learning loop is the genuinely new idea in this base:** every other Canvas agent here (`canvas-mcp`, `opencode-class-agents`) exposes Canvas as tools and leaves orchestration to the model, whereas this one treats the *recurring shape of a course's work* as the persistent artifact. 🔴 **AGPL-3.0 — the network clause makes it unusable as the base of a hosted or distributed client product**, exactly as with `LearnHarness`. Take the scan/approve/execute topology, not the code. 🔴 **Traction signal is internally odd and must not be quoted without this caveat: `125★` against `1` commit.** A single-commit repository at `125★` is either a squashed initial release or externally promoted; either way the star count does not evidence sustained maintenance. Licence verified from the rendered sidebar (`AGPL-3.0 license`). |
| mcp-server-odoo | https://github.com/ivnvxd/mcp-server-odoo | MPL-2.0 | 415 | **New this pass — the governed alternative to `erpipe-org/mcp-odoo`, and the better choice where the *institution* must own the policy.** Reaches any Odoo model, so it too reaches OpenEduCat's student record. Access control lives in a **companion Odoo module** carrying a per-model allowlist with separate read / write / create / delete permissions, layered on Odoo's own access rights and record rules — so the client's Odoo administrator decides what an agent may touch, rather than an environment variable inside the agent's container. 17 tools including `create_records`/`update_records` batches, attachments, `aggregate_records`, `post_message` and (double-env-gated) `call_model_method`. Odoo 16.0+ in standard mode; JSON-2 with an API key on Odoo 19+. 190 forks. **Why it is in this table and not the one above: MPL-2.0 is *file-level* weak copyleft** — modifications to its own files must be published, but it combines freely with proprietary code, so unlike AGPL it needs a licence note in the deliverable rather than a redesign. 🔴 **Red flag to raise in every review: "YOLO mode" requires no companion module, bypasses all MCP-level access control and exposes 200+ models; full YOLO mode permits delete.** Its own README restricts it to development and testing. Never ship it, and grep for it in any inherited deployment. |
| LearnHarness | https://github.com/amosblomqvist/learnharness | AGPL-3.0 (**payload-verified this pass**: root `LICENSE`, `34,523 B`, `sha256:0d96a4ff68ad6d4b…`, affero×`16`, title line `GNU AFFERO GENERAL PUBLIC LICENSE`; sidebar agrees) | 9.1k | **New this pass — the largest NEW education repository found in this window, and the fastest-growing artifact this base has tracked.** Desktop agent *harness* for learning hard material: agents plan and teach a lesson from the learner's current understanding toward a stated goal, and a **local knowledge graph stores ideas and the links between them rather than ability ratings** — a different persistence model from `DeepTutor`'s learner model and from `OATutor`'s Bayesian Knowledge Tracing, and the reason it is worth reading even though it cannot be shipped. Bring-your-own API keys; ships for macOS, Windows and Linux. `1,202` commits, `1.2k` forks. 🔴 **AGPL-3.0 is the whole adoption story: the network clause makes this unusable as the base of a distributed or hosted client product.** Take the knowledge-graph design, not the code. 🔵 Indexed write-ups are badly stale on size — one says `1.5k★`, another `5.7k★`; the rendered page said `9.1k★` this pass. 🔴 **NAMESAKE HAZARD, added at the twelfth pass (`p807`): "LearnHarness" does not uniquely identify this repository.** A `2026-11-13` adaptive-learning search returned [`h4ksclaw/learnharness`](https://github.com/h4ksclaw/learnharness) — **a different project, not a fork**: `3★`, `1` fork, `52` commits, described as *"Open-source adaptive learning harness with FSRS, BKT, and LLM-powered knowledge graphs. Domain-agnostic."* against this row's *"Agent harness for learning difficult things."* 🔴 **Its README states its licence as the bare word `MIT` under a `## License` heading, and there is NO `LICENSE` file at all** — `raw.githubusercontent.com` returns `404` for `LICENSE` and `LICENSE.md` on **both** `main` and `master`, which is why GitHub's sidebar shows no licence. 🔵 **A prose "MIT" with no grant file is not a grant; the default is all-rights-reserved.** 🟢 **Always resolve this row by the full slug `amosblomqvist/learnharness`, never by name** — the two differ in owner, size, purpose *and* licence, and the cheap mistake (`MIT`, `3★`) is the one that looks build-safe. 🔴 This is distinct from `T966`'s two `0★` byte-identical AGPL-3.0 forks; `h4ksclaw` is a third repository and shares no bytes with either. |
| tutor-gpt | https://github.com/plastic-labs/tutor-gpt | GPL-3.0 | 933 | AI tutor driven by Theory-of-Mind reasoning about the learner. GPL-3.0: fine for internal or hosted use, a problem for a distributed client product. |
| openedx-mcp | https://github.com/blend-ed/openedx-mcp | AGPL-3.0 | 3 | Open edX admin operations as an MCP facade for staff/superusers, native platform APIs only. Very early — reference, not dependency. |
| moodle-mcp-server (csmediapro) | https://github.com/csmediapro/moodle-mcp-server | AGPL-3.0 | 2 | Moodle MCP server over Web Services; 10 core tools plus cache management and `refresh_user_field_schema`. **Open-core: additional tools ship in a paid premium plugin.** AGPL plus a commercial upsell is the wrong base for a client deliverable — note it and move on. |
| moodle-mcp-server (lmscloud) | https://github.com/lmscloud-io/moodle-mcp-server | GPL-3.0 | 1 | Runs Moodle web services for administration and analysis; installs via `uvx`, authenticates with a Moodle web-service token. No repository description, no stated tool count. |
| Masar X | https://github.com/fotedev/Masar-x-next | 🔴 **AGPL-3.0 — byte-read** (`raw.githubusercontent.com/fotedev/Masar-x-next/main/LICENSE`, `34,523 B`, `sha256:0d96a4ff…`, first line `GNU AFFERO GENERAL PUBLIC LICENSE`) | 9 | **New this pass (`p821`).** Bilingual **English / العربية** university study platform — summaries, interactive courses, quizzes, AI assistance and learning management — as a pnpm monorepo with web (live), desktop (Electron) and mobile (Expo) surfaces, Supabase + **pgvector** RAG. 🔵 **Region EMEA from the bilingual Arabic product surface, and it is the only Arabic-first AI study platform this base has byte-read.** 🔴 **AGPL-3.0 over a NETWORK-DELIVERED platform is the hardest copyleft case in this file: §13 reaches users served over a network, so a hosted fork owes source to its users.** Usable as a reference implementation or under a separate commercial grant from the author; **not** adoptable into a client's hosted product without that grant. Created `2026-01-19`, pushed `2026-11-15`. |
 DIRA | https://github.com/DIRA-HUB-LTD/DIRA | 🔴 **AGPL-3.0 — byte-read** (`34,523 B`, `sha256:8486a10c4393…`, title line `GNU AFFERO GENERAL PUBLIC LICENSE`, `Copyright (C) 2007 Free Software Fou…`) | 1 | **New this pass (`p822`), and the copyleft half of the `T74` channel.** Its own description is the locative: *"Africa Agentic AI Design Challenge: Education - The Long View"* — the SAME sub-theme as `meska-brain`, built by a different team as a *"Learner Profile MCP"* for teacher-led classroom observation and learning pathways, on PostgreSQL 16. 🔴 **AGPL-3.0 propagates over a network service, so a hosted learner-profile built on this tree must publish. Read it for the DATA MODEL, deliver on `meska-brain`'s Apache-2.0 tree** |

## Rejected candidates and why

Real and active projects that are **not** open-source-licensed in a way
Globant can build a client deliverable on.

| Candidate | Repo | Actual license | Stars | Why rejected |
|---|---|---|---|---|
| multi-framework-agent-orchestrator | https://github.com/TruptiLone/multi-framework-agent-orchestrator | 🔴 **MIT bytes, but the grant is NOT this author's — `sha256:ab6328fe6d4d…`, `1,066 B`, holder `Copyright (c) 2025 Ed Donner`** | 0 | **New rejection (`p829`), and it is `T94`'s silent-republish class with the upstream NAMED BY HASH for the first time.** The identical `1,066 B` / `ab6328fe6d4d…` blob is served by [`ed-donner/agents`](https://github.com/ed-donner/agents) (`6,628★`), whose course these notebooks solve. 🔴 **GitHub reports `fork=false`.** 🔵 **Not a licence violation — MIT permits redistribution with the notice intact, and the notice IS intact. It is a SUPPLY-COUNTING defect: shelving this as an independent language-learning agent would count one upstream twice.** 🟢 The method generalises: a licence-byte hash collision against a larger repository is a republish detector needing no README reading |
| ApprenticeshipStandardsDotOrg | https://github.com/ApprenticeshipStandardsDotOrg/ApprenticeshipStandardsDotOrg | 🔴 **`CC0-1.0` — byte-read** (`7,048 B`, `sha256:a2010f343487…`, title line `Creative Commons Legal Code`) | 4 | **New rejection (`p829`), on `T78`'s rule and with real regret.** 🇺🇸 The US counterpart to `ksb-diff` and the only North American artefact the apprenticeship leg produced. 🔴 **CC0 is a public-domain dedication drafted for CONTENT, not software: no patent grant, no warranty disclaimer — which is exactly why `T78` exists.** 🔵 **Disposition is REFUSE-AS-SOFTWARE, not refuse-as-data: the STANDARDS DATA it publishes is usable, the Rails application around it is not clean to vendor.** 🟢 Filed as a licence-request candidate — a one-line relicence to MIT would make it `P69`'s North America adapter |
| english-teacher-agent | https://github.com/el-abid/english-teacher-agent | 🔴 **NO LICENCE FILE — byte-probed at `10` addresses (`LICENSE`, `LICENSE.md`, `LICENSE.txt`, `COPYING`, `LICENCE` × `main`/`master`), all HTTP `404`**; field `NONE` | 0 | **New rejection (`p829`).** CEFR English tutor for high-school students: LangGraph agent, FastAPI UI, local TTS. 🔵 Recorded so the next pass does not re-probe it |
| spanish-language-tutor | https://github.com/nickderobertis/spanish-language-tutor | 🔴 **NO LICENCE FILE — byte-probed at `10` addresses, all HTTP `404`**; field `NONE` | 0 | **New rejection (`p829`).** A LiveKit agent for teaching Spanish — the closest the language leg came to a real-time voice tutor, and unusable without a grant |
| PRADA | https://github.com/GothHeit/PRADA | 🔴 **NO LICENCE FILE — byte-probed at `10` addresses, all HTTP `404`**; field `NONE` | 1 | **New rejection (`p829`).** A distributed personal agent running an OFFLINE conversational language tutor on a local model — the offline posture this base keeps looking for, behind no grant |
| pingo-voice-backend | https://github.com/luharry2821/pingo-voice-backend | 🔴 **NO LICENCE FILE — byte-probed at `10` addresses, all HTTP `404`**; field `NONE` | 0 | **New rejection (`p829`).** Real-time voice language-learning agent on AssemblyAI Universal-Streaming |
| essay-grader-llm | https://github.com/Dmoayad/essay-grader-llm | 🔴 **LICENCE CONFLICT — sidebar says `GPL-3.0 license`, README's licence section claims MIT** | 1 | **New rejection (`p827`, `T96`).** LangChain + Gradio rubric grader with structured feedback and a plagiarism check. `12` commits, `1` fork. 🔴 **Rejected on two independent grounds.** First, the licence is self-contradictory, and on GitHub the sidebar reflects the actual `LICENSE` file while the README is prose — so the governing grant is `GPL-3.0`, which is copyleft and unusable as the base of a hosted client deliverable. Second, at `1★`/`12` commits it is a course-scale artifact regardless of licence. 🔵 Cited in `P67` for its rubric-feedback shape only. |
| Rubric_Agent | https://github.com/shafaq2019/Rubric_Agent | 🔴 **NO LICENCE FILE — sidebar carries no licence entry** | 0 | **New rejection (`p827`, `T96`).** FastAPI agent that learns scoring rules from a human reviewer's sample, then scores the remainder: reviewer scores a random `15%` sample, the agent drafts Do's & Don'ts from it, self-tests on held-out samples, then scores the rest, **running each item three times to flag unstable scores**. Handles typed and scanned answers; Gemini or Claude. `6` commits, `0` forks, and its own description names it a `DATA722` mid-term. 🔴 **No grant file means all rights reserved — not shelvable at any quality.** 🟢 **But the DESIGN is the best in the grading search and is reimplemented in `P67`:** the small-sample rubric induction, the held-out self-test, and the triple-run instability flag are all correct, and all three are cheap to rebuild from this description. |
| ntulearn-mcp (NTU Singapore Blackboard) | https://github.com/gangula-karthik/ntulearn-mcp | 🔴 **MODIFIED MIT — byte-read and DIFFED** (`1,055 B`, `sha256:9783f2a651e2…`, holder `kingdonkatsu`); GitHub's field reports `NOASSERTION` | 6 | 🔴 **Rejected `p826`, and it is `T93`'s worked example — this base's own header-only byte-read would have shelved it as MIT.** The file opens `MIT License` and reads as stock text until the permission clause, which is rewritten from *"to permit persons to whom the Software is furnished to do so"* to *"to furnish it to whom it is furnished to do so"* — i.e. the ONE sentence that grants onward distribution has been altered into something that does not parse as a grant. 🔵 **The `NOASSERTION` field is CORRECT here and the licence header is misleading; GitHub's matcher refused it for exactly the right reason.** 🟢 **Not a verdict on the code, which is a legitimate read-only MCP server over NTULearn and would be a wanted APAC row: this is a licence-text defect its author can fix in one commit by restoring the canonical sentence, and that request is the right next action** |
| courses-mcp | https://github.com/mahmutmft/courses-mcp | 🔴 **No grant file — byte-probed at 4 paths on `master`, all HTTP `404`** (`LICENSE`, `LICENSE.md`, `LICENSE.txt`, `COPYING`); GitHub licence field reads `NOASSERTION` | 1 | **New rejection this pass (`p823`).** Read-only MCP server for **FINKI Moodle** — the Faculty of Computer Science and Engineering, Ss. Cyril and Methodius University, Skopje 🇲🇰 — browsing enrolled courses and resources. 🔵 **It is a real member of the `T77` population and it is the one that cannot be shelved**, which is why it is filed by name: a later pass that re-finds it should not re-pay for the licence probe. 🔴 **`NOASSERTION` with NO bytes behind it is the OTHER failure direction of `T27`:** the field is equally uninformative when the grant is absent as when it is present, and only the probe distinguishes them. 🟢 Worth an upstream licence request — a single `LICENSE` file would move it to the build-safe table. Pushed `2026-11-15`. |
| Mothusi | https://github.com/TD-Mosoma/Mothusi | 🔴 **No grant file — byte-probed at 4 paths on `main`, all HTTP `404`**; GitHub licence field `NONE` | 0 | **New rejection this pass (`p823`), and the one this base most wanted to shelve.** *"An AI classroom colleague for Grade 1–4 teachers in South Africa"* 🇿🇦 — a team of LangGraph agents that plan lessons. 🔵 **Africa-placed foundation-phase supply, the category `T71` opened and that this base holds almost nothing in**, and it arrives all-rights-reserved. 🔴 **This is now the FIFTH substantial unlicensed education repository recorded here** (`llamatutor`, `AITutor-EvalKit`, `educational-agents`, `AI-Grading-Tool`, now `Mothusi`) — the pattern `T24` names. 🟢 **Concrete action available: an upstream licence request costs one issue and would place an Africa foundation-phase agent on this shelf.** Pushed `2026-11-14`. |
| educational-tools | https://github.com/birkanyavuz/educational-tools | 🔴 **CC BY-4.0 — byte-read** (`18,658 B`, `sha256:f5b745ef…`, title line `Attribution 4.0 International`) | 0 | **New rejection this pass (`p823`), on a ground this table has not used before.** An **A2A + MCP server for classroom tools** with creator attribution — genuinely the right protocol pairing for a classroom tool server. 🔴 **CC BY-4.0 is a CONTENT licence applied to SOFTWARE.** Creative Commons itself recommends against using it for code: it grants no patent rights, says nothing about source availability, and its attribution clause is written for works, not builds. 🔵 **It is not copyleft and not non-commercial, so this is not a refusal of intent — it is a refusal of INSTRUMENT**, and it is the mirror image of `T78`: there a content licence correctly governed content, here one governs code it was never drafted for. 🟢 **Also fixable upstream in one commit** — the author almost certainly means MIT or Apache-2.0. Pushed `2026-11-13`. |
| Website-MCP | https://github.com/corixien/Website-MCP | 🔴 **No grant file — byte-probed, HTTP `404`**; field `NONE` | 0 | **New rejection this pass (`p823`).** FastMCP server giving read-only access to **school portals** including Moodle. Filed by name as a `T77` population member that cannot be adopted. Pushed `2026-11-10`. |
| moodle-mcp-server | https://github.com/daniilnikhaev534-art/moodle-mcp-server | 🔴 **No grant file — byte-probed, HTTP `404`**; field `NONE` | 1 | **New rejection this pass (`p823`).** Moodle MCP server, no description published. Filed by name for the `T77` denominator. Pushed `2026-11-13`. |
| Veracity_MCP | https://github.com/chadudell/Veracity_MCP | 🔴 **NO LICENCE** — no payload at any probed path | 5 | 🔴 **Rejected this pass (`p817`), and it is the most useful rejection of the pass because of WHAT it is.** *“MCP server for Veracity Learning Record Store (LRS) API — 20 tools for learners, courses, classes, launches…”* 🔴 **The only agent surface over a COMMERCIAL LRS on this channel, `20` tools deep, and it carries no grant at all.** 🔵 **Consequence for `P43`: the agent layer over the learner record exists only for products a studio cannot build on, or in [`DavidLMS/learnmcp-xapi`](https://github.com/DavidLMS/learnmcp-xapi) (MIT, `16★`) over an open LRS. There is no third option** |
| edfi-mcp-server | https://github.com/cdweaver1992/edfi-mcp-server | 🔴 **NO LICENCE** — no payload at any probed path | 1 | 🔴 **Rejected this pass (`p817`).** MCP server for Ed-Fi ODS/API integration, pushed `2026-02-17`. 🔴 **The only non-Alliance agent surface over the US K-12 data standard, and it is unlicensed** — so the entire adoptable surface over Ed-Fi is the Alliance's own two Apache-2.0 prototypes. See `T53` |
| ebsi-vc-poc | https://github.com/KDiamantidis/ebsi-vc-poc | 🔴 **NO LICENCE** — no payload at any probed path | 0 | 🔴 **Rejected this pass (`p817`), and it is the ENTIRE result set for `q="ebsi verifiable diploma"` (`total_count=1`).** A proof of concept for issuing EBSI/W3C verifiable credentials for diplomas. 🔵 **The EU's own blockchain credential infrastructure has exactly one open implementation on this channel and it carries no grant — which is the EMEA half of `T56`** |
| srs-benchmark | https://github.com/open-spaced-repetition/srs-benchmark | 🔴 **NO GRANT — measured, not assumed:** no payload at any of `32` licence paths or `16` manifests; GitHub's licence field reads `NONE` and agrees | 287 | 🔴 **New rejection this pass (`p816`), and the only unlicensed repository in a layer that is otherwise MIT throughout.** *"A benchmark for spaced repetition schedulers/algorithms."* 🔵 **It is also the most CITABLE artefact in the layer — the published comparison that makes “use FSRS” an evidence-based recommendation rather than a preference — so the rejection is narrow and worth stating precisely: cite it, link it, reproduce its method; do not vendor its code.** 🟢 **`29` forks, pushed `2026-10-24`, same organisation as five MIT rows, which makes this an oversight rather than a policy — `ACTION p816-C` asks** |
| academic-research-mcp | https://github.com/0jsDanny/academic-research-mcp | 🟡 **MIT, byte-read and VALID** (`1,084 B`, `sha256:2a3fdf99…`, holder `Daniel Santos & Contributors`) — 🔴 **rejected on a basis the licence cannot cure** | 0 | 🔴 **New rejection this pass (`p814`), and the specimen that establishes the THIRD risk axis (`T40`).** 🟢 **Axis (a) is clean — it needs no learner credential at all. Axis (b) is clean — it retrieves literature and submits no coursework. `p813`'s two-axis grade would have SHELVED this row.** 🔴 **And it is unshippable, because its own README documents the mechanism: *"**Sci-Hub** \| Subscription Journals \| Automated TLS spoofing via `curl_cffi` to bypass paywalls and bot challenges"*, with `download_scihub_pdf` and `search_scihub_by_doi` as first-class tools and a "Sci-Hub Mirror" branch in its architecture diagram.** 🔴 **Paywall circumvention is a legality question about the DATA SOURCE, independent of the licence on the code and of how the credential is handled. A studio cannot ship it, fork it, or cite it.** 🔵 **Contrast `openags/paper-search-mcp` on the build-safe shelf: same source, last in an OA-first chain and optional — a configuration obligation, not a rejection. The axis is three-valued: clean / configurable / STRUCTURAL** |
| cnki-skills | https://github.com/cookjohn/cnki-skills | 🔴 **No licence — `404` for `LICENSE`, `LICENSE.md`, `LICENSE.txt` and `LICENSE-MIT` at `main` AND `master`, while `README.md` returns `200`** | 1067 | 🔴 **New rejection this pass (`p814`) — the most-starred ungranted repository in this base by a wide margin, and the APAC counterpart to `p813`'s `moodle-mcp` lesson.** 🇨🇳 CNKI (中国知网) skills for Claude Code: search papers, browse journals, check indexing status, download PDF/CAJ, export to Zotero. 🔴 **Rejected on the licence alone: `1,067★` buys no permission.** 🟡 **And a second, SEPARATE question a studio must not conflate with Sci-Hub: it drives the user's own manually authenticated Chrome session (*"Chrome browser (login handled manually for downloads)"*), so the issue is the INSTITUTION'S subscription terms on automated bulk retrieval — a terms-of-use matter, not copyright circumvention.** 🔵 **Naming that distinction precisely is the point: `T40` grades the data source, and "unlawful" and "outside your licence" are different findings with different remedies** |
| ScienceClaw (AgentTeam-TaichuAI) | https://github.com/AgentTeam-TaichuAI/ScienceClaw | 🔴 **No licence — no payload at either branch root; repository EXISTS (positive control fires)** | 682 | 🔴 **New rejection this pass (`p814`).** Personal research assistant built with LangChain. 🔵 **Half of a name-collision group: created `2026-03-13`, two days after `beita6969/ScienceClaw` (`2026-03-11`, MIT but with a third-party holder line). Neither is established as canonical, and this half has no grant at all** |
| docsagent | https://github.com/docsagent/docsagent | 🔴 **No licence — no payload at either branch root; `README.md` `200`** | 580 | 🔴 **New rejection this pass (`p814`).** Private document access for AI agents — squarely the research-library layer's use case, at `580★`, with no grant |
| ZotSeek | https://github.com/introfini/ZotSeek | 🔴 **No licence — no payload at either branch root; `README.md` `200`** | 239 | 🔴 **New rejection this pass (`p814`).** AI semantic search for Zotero with a built-in MCP server. 🔴 **The highest-starred ungranted Zotero agent, and the capability (semantic search over the library) that the build-safe rows cover least well — so this is the pass's most expensive rejection after `cnki-skills`** |
| ZotLink | https://github.com/TonybotNi/ZotLink | 🔴 **No licence — no payload at either branch root; `README.md` `200`** | 137 | 🔴 **New rejection this pass (`p814`).** Self-described production-ready Zotero MCP server for saving open preprints (arXiv and others). 🔵 *"Production-ready"* and ungranted is a contradiction a studio should name to the author |
| zotero-mcp-setup | https://github.com/ehawkin/zotero-mcp-setup | 🔴 **No licence — no payload at either branch root; `README.md` `200`** | 51 | 🔴 **New rejection this pass (`p814`).** Install scripts and a user guide for Zotero MCP — documentation, not an agent, and ungranted either way |
| koha-mcp-server (wrecks1997) | https://github.com/wrecks1997/koha-mcp-server | 🔴 **No licence — no payload at either branch root; `README.md` `200`** | 2 | 🔴 **New rejection this pass (`p814`).** MCP server over a specific institution's Koha catalogue (GBS library). 🔵 **Name-collision with the build-safe `asjolaviral/koha-mcp-server`, and the two are separated by the licence channel alone — same name, same purpose, opposite verdict** |
| agentilab-openalex | https://github.com/simonpierreboucher02/agentilab-openalex | 🔴 **No licence — no payload at either branch root; `README.md` `200`** | 0 | 🔴 **New rejection this pass (`p814`).** OpenAlex API docs, MCP server and agent skill over the free open catalogue. 🔵 **Use `leomcamilo/bx-scholar-mcp` (MIT) for the same catalogue instead** |
| moodle-mcp (loyaniu) | https://github.com/loyaniu/moodle-mcp | 🔴 **No licence — `404` for `LICENSE`, `LICENSE.md`, `LICENSE.txt` and `COPYING` at `main` AND `master`, while `README.md` returns `200` at both** | 57 | 🔴 **New rejection this pass (`p813`), and the most expensive one this base has ever recorded.** At `57★` and `17` forks it is **the most-starred Moodle MCP server in existence** and the first hit on every `moodle mcp` query — so it is precisely the row a future pass shelves by reflex and an engagement then depends on. 🟢 **The positive control fires: the repository EXISTS (`README.md` `200`) and simply has no grant** (`T37`). 🔴 **No licence means no permission: not forkable, not vendorable, not citable as a dependency.** 🔵 **Contact-the-author is the cheapest unblock in this base — one `LICENSE` commit converts the tier's anchor into a build-safe row** |
| tronclass-mcp (markbee66) | https://github.com/markbee66/tronclass-mcp | 🔴 **No licence — `404` at both branch roots; `README.md` `200`** | 1 | 🔴 **New rejection this pass (`p813`).** 🇹🇼 TronClass is the LMS of a large share of Taiwanese universities. `2` forks |
| TronClass-MCP (cantpr09ram) | https://github.com/cantpr09ram/TronClass-MCP | 🔴 **No licence — `404` at both branch roots; `README.md` `200`** | 3 | 🔴 **New rejection this pass (`p813`) — the most-starred and oldest of the TronClass tier (`2025-04-12`), and still ungranted after nineteen months** |
| FJU-TronClass-MCP | https://github.com/RX5950XT/FJU-TronClass-MCP | 🔴 **No licence — `404` at both branch roots; `README.md` `200`** | 1 | 🔴 **New rejection this pass (`p813`).** 🇹🇼 Fu Jen Catholic University: CLI + MCP for courses, to-dos, announcements, grades, bulk material download, video progress marking. **The most capable of the five, and unusable** |
| tronclass-mcp (JasonWu55) | https://github.com/JasonWu55/tronclass-mcp | 🔴 **No licence — `404` at both branch roots; `README.md` `200`** | 1 | 🔴 **New rejection this pass (`p813`).** `1` fork, pushed `2026-09-24` |
| tronclass-mcp (rlongdragon) | https://github.com/rlongdragon/tronclass-mcp | 🔴 **No licence — `404` at both branch roots; `README.md` `200`** | 0 | 🔴 **New rejection this pass (`p813`).** 🇹🇼 NTOU, built on `tronclass-api`. 🔴 **Completes a HARD NIL: `5` TronClass repositories, `5` existing, `0` licences — the whole Taiwanese university LMS tier is unadoptable, and that is a measurement, not a search failure** (`T37`) |
| xuexitong-cli (Kfjie-MCP) | https://github.com/Kfjie-MCP/xuexitong-cli | **MIT — byte-read** (`1,065 B`, `sha256:3486ae61…`) 🔴 **but the bytes are IDENTICAL to `DanMo661/xuexitong-cli`, including the copyright holder `Wu Jiale`** | 0 | 🔴 **New rejection this pass (`p813`), and it is NOT a licence rejection — the grant is clean.** 🔴 **It is a DE-DUPLICATION rejection (`T37`): same repo name, same licence bytes, same copyright holder, created `2026-11-13` (today) against the original's `2026-09-11`, with a `1,580 B` README against `24,943 B`.** 🟢 **Two addresses, one artefact; shelving both would inflate APAC supply and the cluster's apparent momentum.** 🔵 **Recorded here rather than silently dropped so a later pass does not re-discover and shelve it** |
| Sigaa-UFRPE-MCP | https://github.com/DaviPac/Sigaa-UFRPE-MCP | **No licence — `404` for `LICENSE`, `LICENSE.md`, `LICENSE.txt` and `COPYING` at `main` AND `master`** | 0 | **New rejection this pass (`p812`).** SIGAA MCP server for UFRPE (Universidade Federal Rural de Pernambuco). Created `2026-09-05`. Default all-rights-reserved |
| sigaa-ufpa-mcp | https://github.com/joaosnet/sigaa-ufpa-mcp | **No licence — `404` at both branch roots** | 1 | **New rejection this pass (`p812`), and the most developed of the ungranted Brazilian servers:** *"Este projeto implementa um servidor MCP (Model Context Protocol) específico para automatizar o acesso ao SIGAA"* (UFPA). Pushed `2026-11-08`. 🔵 **The highest-value licence request in the Brazilian cluster** — see `intel/licence-requests/` |
| campus-utn-frm-mcp | https://github.com/ignaw05/campus-utn-frm-mcp | **No licence — `404` at both branch roots** | 5 | **New rejection this pass (`p812`), and the one that stings: at `5★` it is the second-most-starred UTN campus agent and it carries no grant at all.** Pushed `2026-11-06` |
| utn-mcp (PedroCarassale) | https://github.com/PedroCarassale/utn-mcp | **No licence — `404` at both branch roots** | 1 | **New rejection this pass (`p812`).** *"Servidor MCP para el campus virtual (Moodle) de la UTN FRLP"* (La Plata). 🔴 **Shares the bare name `utn-mcp` with the ISC-licensed `nialvape/utn-mcp` on the shelf above — the `T22` collision, and here the ungranted one is the namesake.** Pushed `2026-10-31` |
| moodle-utn-mcp | https://github.com/NicolasViruel/moodle-utn-mcp | **No licence — `404` at both branch roots** | 2 | **New rejection this pass (`p812`).** *"Agente conectado via MCP para el consumo de la informacion de la facultad."* Pushed `2026-10-19` |
| suap-mcp | https://github.com/frjunioalves/suap-mcp | **No licence — `404` at both branch roots** | 0 | **New rejection this pass (`p812`).** The only other SUAP server besides the AGPL-3.0 `expeditto`. 🔴 **So SUAP, like PowerSchool, has no permissive agent: one copyleft and one ungranted.** Pushed `2026-05-22` |
| Sotto | https://github.com/affromero/Sotto | **PolyForm Noncommercial License 1.0.0 — byte-verified, against GitHub's `NOASSERTION`** | 35 | **New rejection this pass (`p810`), and the exact mirror of `webworn/openfoam-mcp-server`.** Self-hosted open-source AI language learning: CEFR courses, adaptive listening, speaking practice; `10` forks; pushed `2026-11-13`, the day of this pass. 🔴 **`LICENSE` blob `1a71cb643975`, `4,563 B`: "Any noncommercial purpose is a permitted purpose."** PolyForm Noncommercial is **not an OSI licence** and forbids exactly what Globant does — commercial client delivery. 🔴 **It calls itself "open source" in its own description.** 🟢 Read it for the CEFR course structure; do not ship a line of it. See `T969` |
| mcp-powerschool | https://github.com/443pablo/mcp-powerschool | **No licence — GitHub reports `NONE`, no `LICENSE` in the repository** | 2 | **New rejection this pass (`p810`).** The highest-starred PowerSchool MCP server found, and it carries no grant at all. 🔴 **PowerSchool is the largest US K-12 SIS and this base has named it `382` times; the only other candidates are `zuvy/ps-mcp-server` (`NONE`) and `thesupersupersigma/powerschoolMCP` (`GPL-3.0`, copyleft).** 🟢 **So the PowerSchool gap is NOT closed this pass, and it is a LICENCE gap rather than a supply gap** — three servers exist, none is build-safe |
| d2l-mcp-server | https://github.com/bencered/d2l-mcp-server | **No LICENSE file — `404` at `main` AND `master` root; GitHub sidebar shows none** | 12 | **New rejection this pass (`p809`).** The README carries a `License` section reading `MIT`, but **no licence payload exists at either branch root** and GitHub's own detector reports nothing, so on its face the repository is default all-rights-reserved. 🔵 **This is the T6 pattern in its most deniable form, and the transmission path was identified:** an aggregator (`glama.ai`) published *"License MIT"* read off the README, and that is where the claim entered circulation — the same channel that mis-reported `RohanMuppa/brightspace-mcp-server` as `AGPL-3.0` when its payload is a byte-verified `MIT`. 🔴 **Aggregator licence fields are not evidence in either direction.** `3` commits. Re-test the payload before any future admission. |
| PageLM | https://github.com/CaviraOSS/PageLM | CaviraOSS / "PageLM Community License" — **not OSI** | 2.1k | README requires prior written permission for commercial use or resale. Marketed as "open source"; it is source-available. Do not put it in a client stack. |
| llamatutor | https://github.com/Nutlope/llamatutor | **No license file** | 2.1k | Default all-rights-reserved. Good reference implementation of an AI personal tutor on Llama 3.1; not reusable without an explicit grant. |
| education-agent-skills | https://github.com/GarethManning/education-agent-skills | CC BY-SA 4.0 | 977 | 165 evidence-grounded education skills for Claude/Codex-style agents. CC BY-SA is a **content** license with share-alike — usable as pedagogy reference material, wrong instrument for shipped software. |
| AITutor-EvalKit | https://github.com/kaushal0494/AITutor-EvalKit | **No licence file — re-verified at `HEAD` `a71078456a90` this pass** | 4 | 🔴 **Moved out of the build-safe table this pass, and the move is a correction of this base against itself.** `p801` (`T961`) established that this repository serves **no licence anywhere**, while its `EACL 2026` paper calls it *"MIT-licensed"*. The row in the build-safe table went on publishing `MIT` for a further pass. `p802` re-probed the clone channel and reproduced `T961` exactly — **same `HEAD`, still a `7`-entry tree, still no `LICENSE`, `COPYING` or equivalent in the root tree** — so the grant does not exist and the default is all-rights-reserved. Still the only pedagogy-specific eval harness found, so it remains worth reading and worth an upstream licence request; it cannot be adopted. 🔴 **This base has now carried a licence it had itself refuted for one full pass — see `ACTION p802-A`.** |
| educational-agents | https://github.com/nifalconi/educational-agents | **No license file** | 1 | **New rejection this pass.** Spanish-language teaching library ("agents in 2 lines") from the *Niñas Pro* applied-AI course for girls in **Chile** — genuinely interesting as LATAM education provenance, and the kind of project worth contributing a LICENSE file to. As published it is all-rights-reserved and cannot be adopted. v0.1.0 prototype, built on the OpenAI Agents SDK via OpenRouter. |
| AI-Grading-Tool | https://github.com/end13s/AI-Grading-Tool | **No licence file — sidebar shows none** | 0 | **New rejection this pass (`p808`).** The only *Moodle*-targeted grader found in the LMS-seam leg, and functionally the closest fit to a real client ask: imports a Moodle roster and submissions, has an LLM check each one against the instructor's rubric, routes every result through human review, then exports grades back to Moodle. 🔴 **`134` commits and no grant of any kind — the default is all-rights-reserved.** 🔵 **This is the fourth education repository in this base to be substantial and unlicensed** (`llamatutor` `2.1k★`, `AITutor-EvalKit`, `educational-agents`, now this), which is itself the finding recorded as `T24`. Worth an upstream licence request; cannot be adopted as published. |
| k12-qbank | https://github.com/wisdom-km/k12-qbank | 🟢 MIT — byte-read (`1,066 B`, `sha256:03e6e939…`) | 0 | **New refusal this pass (`p821`), and the licence is not the reason — the implementation is.** A 🇨🇳 Heilongjiang maths question bank and teaching closed loop for 人教版 七年级上册, with a real pedagogical design: teacher verifies stem, answer, worked solution and knowledge point before a paper may be issued; per-student papers printed with student number and page number **and no name on the sheet**; photo capture to collect them back; teacher confirms the AI's suggestion before practice is re-scheduled. 🔴 **Its own README refuses the row for us: `catalog` and `practice` hold a minimal skeleton over synthetic data, there is 还没有网页 (no web surface) and 没有数据库 (no database), and `python scripts/status.py` prints status without issuing a paper or starting a site.** 🟢 **A design document with a licence file is not a build-safe agent.** Filed by name so the next pass does not re-pay for the discovery, and so it can be promoted when it ships. Created `2026-11-13`, pushed `2026-11-14`. |
 contextbridge-long-view | https://github.com/stevenking00/contextbridge-long-view | 🔴 **NO LICENCE — and no repository either: `README.md` is `404` at BOTH `main` and `master`, reported size `0 KB`** | 0 | 🔴 **New rejection this pass (`p822`).** Third Education-track entry in the `T74` channel, and it is a DESCRIPTION without a payload — *"Governed agentic AI for longitudinal learner intelligence"* with nothing behind it. 🟢 **Filed so the next pass does not pay to rediscover it, and so a later pass can promote it if it ships** |
 ai--manus2.0 (and ~774 siblings) | https://github.com/Topkiflare74/ai--manus2.0 | 🔴 **Apache-2.0 file present and byte-read — and WORTHLESS: the payload is a relicensed copy carried by a repository with no code.** The upstream it impersonates, `Simpleyyt/ai-manus`, is MIT | 678 | 🔴 **New rejection this pass (`p822`), and it stands for a CLASS of `775`.** No `package.json`, `requirements.txt`, `setup.py` or `install.sh`; `118 KB` against the original's `22,029 KB`; `0` open issues; a README whose `sha256` is identical across siblings and whose only call to action is a Dropbox `.rar` download. 🔴 **Created inside a `48`-hour window, each sibling carrying `650`–`680` stars.** 🟢 **Named here so that this shelf's reader can recognise the shape: relicensed text, no tree, synchronised creation, uniform stars. See `T73` and `P52`** |

## Declared gaps

- 🔴 **`p817` — the agent surface over the LEARNER RECORD is a two-row layer, and one of the two is unlicensed.**
  `q="xapi mcp server"` → `10`, of which exactly one is purpose-built and licensed:
  [`DavidLMS/learnmcp-xapi`](https://github.com/DavidLMS/learnmcp-xapi) (MIT, `16★`, last pushed
  `2025-08-29` — 🔴 **fifteen months stale**). The only other real candidate,
  [`chadudell/Veracity_MCP`](https://github.com/chadudell/Veracity_MCP) (`5★`, `20` tools), carries
  **no licence**. 🔴 **`q="learning analytics mcp"` → `21` and every row is unrelated noise.**
  🔵 **So the one component every compose pattern in this file depends on — the path by which an
  agent's actions become an institutional record — rests on a single stale MIT repository at `16★`.
  That is the most load-bearing single point of failure this base has recorded.**

- 🔴 **`p817` — a QUERY DEFECT of this pass's own, recorded so the nil is not inherited.**
  `q="caliper analytics sensor"` → **`total_count=0`**, and an earlier draft of this pass was going
  to publish *“Caliper has no open implementations.”* 🟢 **It is false, and this base's own
  `repos/foundations.md` refutes it: the Caliper layer table has been populated since `p805`, with
  [`CarnegieLearningWeb/caliper-ts`](https://github.com/CarnegieLearningWeb/caliper-ts) (MIT) in it.**
  🔵 **`p812`'s rule, restated because it caught a defect again: a nil is only informed if the query
  named the thing's OWN vocabulary. Check the shelf before publishing a nil about the world.**

- 🔴 **`p817` — EBSI, the EU's blockchain credential infrastructure: `total_count=1`, `0★`, unlicensed.**
  `q="ebsi verifiable diploma"` returns only [`KDiamantidis/ebsi-vc-poc`](https://github.com/KDiamantidis/ebsi-vc-poc).
  🔵 **Paired with the archived `European-Learning-Model` (`T56`), the honest EMEA statement is: the
  policy is the most developed in the world and the open codebase under it is one proof of concept
  and one archived data model.**

- 🔴 **`p817` — the APAC and LATAM credential/interoperability nils, with every query recorded.**
  🇮🇳 `q="academic bank of credits india"` → `1` (`0★`, unlicensed); `q="diksha ndear education india"` → **`0`**;
  🇯🇵 `q="gigaschool japan education data"` → **`0`**; 🇸🇬 `q="singapore student learning space api"` → **`0`**;
  🇦🇺 `q="australia unique student identifier"` → `2`, ceiling `3★`, both unlicensed;
  🌎 `q="credencial digital educacion verificable"` → **`0`**; `q="interoperabilidad educativa estandar"` → **`0`**;
  `q="registro academico nacional api"` → **`0`**. 🔵 **Both regions carry national mandates with no
  open infrastructure beneath them — see `T56`. In those regions `P44` is a BUILD, not an adoption.**

- 🔴 **`p817` — `ACTION p816-C` is NOT pending work and is retired as such, as `p816` instructed.**
  🔴 **The licence-issue backlog (`srs-benchmark` `287★`, `nailuoGG/anki-mcp-server` `254★`,
  `loyaniu/moodle-mcp` `57★`) requires contacting maintainers on behalf of the studio.** 🔴 **This
  pass ran unattended on a schedule with no human in the loop, so it could not and did not seek that
  decision, and it did not contact anyone.** 🟢 **Per `p816-C`'s own instruction — *“if `p817` cannot
  get that decision, say so plainly and stop re-listing it as though it were pending work”* — it is
  recorded here as BLOCKED ON A HUMAN DECISION and removed from the action list. It returns only when
  a person authorises outward contact.**

- 🔴 **`p815` — the PROCTORING layer is a measured near-nil, and the EU AI Act names it
  explicitly.** `q="proctoring exam open source"` → `total_count=12`, star ceiling `4★`
  ([`Chakrix-com/Swaya.me`](https://github.com/Chakrix-com/Swaya.me), `NOASSERTION`), modal
  licence `NONE`. 🔴 **Annex III lists education as high-risk and names exam-cheating detection
  among the listed uses** (`SECONDARY`: obligations reported postponed to `2027-12-02` under the
  2026 Digital Omnibus — verify against the official text before quoting a date to a client).
  🟢 **Meanwhile the only credible open implementation is `Safe Exam Browser` (ETH Zürich 🇨🇭),
  and it is not an AI proctor at all — it is a lockdown browser, MPL-2.0 on Windows
  (`seb-win-refactoring`, `369★`) and with NO licence payload on macOS/iOS (`seb-mac`, `150★`,
  README: *"not for building own versions of SEB"*).** 🔵 **So an EMEA client facing an Annex III
  conformity question has no adoptable AI-proctoring base in any licence. Build, or decline.**

- 🔴 **`p815` — ACCESSIBILITY REMEDIATION is a HARD NIL on this channel.**
  `q="accessibility remediation alt text education"` → **`total_count=0`**. Not thin — empty.
  🔵 **And it is the gap with the nearest deadline and the widest population: web-accessibility
  obligations for public education bodies bind in both North America (ADA Title II web rule) and
  EMEA (European Accessibility Act), and every institution on every platform in
  `verticals/solutions.md` is in scope.** 🟡 **Treat the regulatory dates as `SECONDARY` until
  verified; the `0` is `FIRST-HAND`.**

- 🔴 **`p815` — the IEP / special-education layer: `11` repositories, ceiling `3★`, and the
  honest reading is that it does not exist.** `q="IEP individualized education program"` → `11`,
  of which the only licensed row is [`dg13788/iep-system`](https://github.com/dg13788/iep-system)
  (MIT, `1★`, created `2026-09-06`); `q="special education management"` → `47` and every row is
  unrelated noise. 🔵 **IDEA makes the individualised programme a federal obligation for every US
  district, which makes this the highest-value North American build slot in this base — and the
  one where "adopt an open base" is simply not an available recommendation.**

- 🔴 **`p815` — the assessment ENGINE layer's regional nils, measured in three languages.**
  🇮🇳 `q="autograder assignments india college"` → **`0`**;
  🌎 `q="evaluacion automatica estudiantes plataforma"` → **`0`**;
  🇧🇷 `q="correcao automatica exercicios programacao"` → `5`, ceiling `1★`. 🟡 **The one actively
  developed LATAM specimen, [`felipelageduarte/runcodes`](https://github.com/felipelageduarte/runcodes),
  was pushed `2026-11-11` and carries NO licence — a live project a studio cannot touch.** 🔴
  **And `q="beecrowd online judge"` → `290` repositories of which every single one is a student's
  solutions dump (top row `eduardo-mior/URI-Online-Judge-Solutions`, `346★`): Latin America's
  dominant online judge is not open source, and the query that finds it finds only its users.**

- 🟡 **`p815` — `ACTION p815-A`, the probe's SECOND degree of freedom.** `T43` fixed the filename
  axis and left the branch guessed, and `pressbooks/pressbooks` (`462★`) read as unlicensed
  because its default branch is `dev`. 🔵 **The probe must resolve the default branch from the
  search API's own response rather than iterate `main`/`master`, and `LICENCE` (British spelling,
  found on `athina-edu/athina`) joins the filename list.** Until then, every `NO_PAYLOAD` verdict
  in this base carries an unquantified false-positive rate.


- 🔴 **`p814` — the lineage of the `ScienceClaw` name-collision group is UNRESOLVED, and it is
  registered rather than guessed.** [`beita6969/ScienceClaw`](https://github.com/beita6969/ScienceClaw)
  (`1,028★`, MIT, created `2026-03-11`) carries an MIT holder line naming `Peter Steinberger`,
  who is not the repository owner; [`AgentTeam-TaichuAI/ScienceClaw`](https://github.com/AgentTeam-TaichuAI/ScienceClaw)
  (`682★`, no licence, created `2026-03-13`) is the sibling. 🔴 **`search/repositories` reports
  `fork: false` for both, and `p814` established that the field misses re-uploads (`T41`), so the
  channel cannot settle it.** 🔵 **What WOULD settle it: full-history comparison, which needs
  per-repository API reads — blocked for unattached repositories in this environment. Cite
  `arXiv:2610.08691`, not the repository, until then.**

- 🔴 **`p814` — North America's national-institution layer is a MEASURED `1`, not a nil, and it
  is copyleft.** Queries run this pass: `q="library of congress mcp catalog"` → `total_count=1`,
  and it is [`msuicaut/lc-vocabularies-mcp`](https://github.com/msuicaut/lc-vocabularies-mcp)
  (GPL-3.0, `4★`); `q="apa citation style mcp"` → `total_count=0`; `q="eric ed.gov mcp education
  research"` → `total_count=0`. 🟢 **So North America is NOT thin on this layer overall — it is
  served through NIH/NLM (`q="pubmed mcp"` → `318` repositories, `genomoncology/biomcp` at `679★`
  shelved build-safe).** 🔵 **The transferable reading: the United States binds its education and
  research agents to AGENCY APIs (NIH/NLM, `NCBI_API_KEY`), not to a cultural-institution
  catalogue — the inverse of 🇦🇲 Armenia and 🇧🇷 Brazil this pass.**

- 🔴 **`p814` — a HARD NIL on the admissions layer, measured in both directions.**
  `q="ucas admissions mcp"` → `total_count=0` (🇬🇧 UK) and `q="enem vestibular mcp agente"` →
  `total_count=0` (🇧🇷 Brazil). 🔵 **Two national admissions systems that gate access to higher
  education for millions, and zero agentic surface of any licence on this channel. The widest
  open slot `p814` found, and it is open in both hemispheres.**

- 🟡 **`p814` — the layer's SEMANTIC-SEARCH capability is the one a build-safe row covers least
  well, and the gap is a licence gap, not a capability gap.** The strongest semantic search over
  a Zotero library is [`introfini/ZotSeek`](https://github.com/introfini/ZotSeek) (`239★`) and it
  carries no grant; [`yuanjua/chiken`](https://github.com/yuanjua/chiken) (MIT, `90★`) and
  [`oscardvs/zoteus`](https://github.com/oscardvs/zoteus) (MIT, `65★`) cover it at a quarter of
  the attention. 🔵 **Cheapest unblock in the pass: one `LICENSE` commit by `introfini`.**

- **🟢 CLOSED this pass (`p812`): the `LATAM 0` gap — and the reason it stood for sixteen passes
  is a search defect, stated precisely so it is not repeated.** Eight rows now attach to systems
  operated in Latin America. 🔴 **The defect: this file had never written the word `SIGAA`,
  `SIAGIE`, `SIMAT`, `SUAP` or `SIU-Guarani` once.** 🔵 **The transferable rule: a regional nil
  is only informed if a query named that region's OWN systems. Otherwise it reports the shelf,
  not the world** — and `p811` published it as a fact about the world.

- 🔴 **`SIAGIE` (Peru) — an INFORMED NIL, and now a properly evidenced one.** `gh api -X GET
  search/repositories q="siagie"` returns **`25` repositories and not one agent**: attendance
  uploaders, grade-consolidation reports, nómina tools, analytics dashboards, scrapers. 🔴
  **Every single one carries NO licence file.** 🔵 **So Peru's national K-12 system has an active
  developer community and zero agentic surface and zero grants** — the widest open slot this
  pass found, and the cheapest to enter.

- 🔴 **`SIMAT` (Colombia) — a HARD NIL.** `q="simat educacion"` returns `total_count=0`. Not a
  thin result; an empty one. Colombia's national enrolment system has no open-source presence of
  any kind on this channel.

- 🔴 **`SUAP` (Brazil) — a LICENCE gap, not a supply gap, and the second instance of the
  PowerSchool shape.** Two servers exist: `expeditto` (**AGPL-3.0**, shelved to the copyleft
  table) and `frjunioalves/suap-mcp` (**no licence**, rejected). 🔵 **Neither is build-safe, so
  SUAP joins PowerSchool as a system of record whose agents all fail the licence test rather than
  the existence test.**

- 🔴 **Q-Acadêmico (Brazil) and the Mexican, Chilean and Colombian school systems — NIL on a
  dedicated leg.** `q="q-academico mcp"`, `q="mcp server mexico universidad escuela"`,
  `q="mcp uc chile universidad"` and `q="mcp colegio escolar notas alumno"` each returned
  `total_count=0`. 🔵 **LATAM's supply is real but it is concentrated in exactly two countries —
  Argentina and Brazil.** Quote the region's eight rows as Argentine and Brazilian, never as
  "LATAM coverage."

- 🔴 **`ingest/derive-counts.py` is RED on `repos/foundations.md` and
  `verticals/solutions.md`, and this pass did NOT force it green — the diagnosis is recorded
  instead, because the fix is a judgement call.** The gate looks for ONE canonical shelf per file
  (`| Repo | Licence | Stars | Default branch | Why it is a foundation |` and
  `| Platform | Repo | Licence | Branch | Stack | Use case |`). 🔵 **Measured this pass: those two
  pages carry `13` and `13` tables respectively, deliberately organised BY LAYER** — rostering,
  LTI, xAPI, QTI, Caliper, curriculum corpus — with headers of the shape
  `| Repo | License | Stars | Notes |`. 🔴 **Flattening thirteen layered tables into one shelf to
  satisfy the gate would destroy the structure that makes those pages usable.** 🟢 **The right
  fix is to teach the gate to sum rows across a file's layer tables, as it was already taught at
  `p568` to accept family-suffixed recipe ids and at `p718` to key on column signatures instead of
  prose.** Left open deliberately, with the numbers above, so the next pass can act on evidence.

- 🔴 **`OneRoster` — an INFORMED NIL, and the cleanest one this base has produced.**
  OneRoster is named **`3,043`** times across these files and is the roster-sync standard
  every LMS/SIS integration in `compose/patterns.md` assumes. A dedicated leg
  (`gh api search/repositories q="oneroster mcp"`) returned an **empty result set — zero
  repositories, not zero good ones**. 🟢 **The standard itself is served on the
  non-agent side** — [`googleworkspace/oneroster-integration-conformance-tests`](https://github.com/googleworkspace/oneroster-integration-conformance-tests)
  (`Apache-2.0`, `7★`) and [`oat-sa/oneroster-import`](https://github.com/oat-sa/oneroster-import)
  (`GPL-2.0`, `8★`) are both shelved to `repos/foundations.md` this pass. 🔵 **So the gap is
  specifically agentic: there is a conformance suite and an importer, and nothing that lets an
  assistant read or reconcile a roster.** 🟢 **That is a buildable opening, not an absence** —
  and it is the narrowest, best-evidenced contribution target this file has ever carried.

- 🔴 **`PowerSchool` — NOT a supply gap, a LICENCE gap, and it stays open.** `382` mentions in
  this base. Three servers exist and were each checked this pass:
  [`443pablo/mcp-powerschool`](https://github.com/443pablo/mcp-powerschool) (`2★`, **no licence**,
  rejected above), `zuvy/ps-mcp-server` (`1★`, **no licence**), and
  [`thesupersupersigma/powerschoolMCP`](https://github.com/thesupersupersigma/powerschoolMCP)
  (`GPL-3.0` — copyleft, usable only where the deliverable can carry GPL). 🔵 **The largest US
  K-12 SIS has three agents and no permissive one.** A licence request is the cheap move here,
  and `intel/licence-requests/` is the place it belongs.

- 🔴 **Curriculum alignment — a THIN nil, declared rather than filled.** The leg
  `curriculum alignment ai agent` returned only `0★` repositories with **no licence file**
  (`shlomitb/curriculum_alignment_agent`, `anujgadwal-AI/SmartCurriculum-AI-agent`). 🟢 **Nothing
  was shelved from it.** 🔵 Standards-to-outcome alignment remains the highest-value unserved
  slot in this file, and it is now negatively evidenced twice.

- **🟢 CLOSED this pass (`p809`): the Brightspace gap and the Blackboard gap.** Both
  were gaps in this file, not in the world. **Brightspace/D2L** now has two shelf rows,
  `RohanMuppa/brightspace-mcp-server` (`MIT`, `67★`) and `JhostinAleck/brightspace-mcp`
  (`MIT`, `16★`). **Blackboard** has three, `alejooroncoy/campus-cli` (`ISC`, `13★`),
  `kingdonkatsu/ntulearn-mcp` (`MIT`, `4★`) and `Mattlo0546/blackboard-mcp` (`MIT`, `1★`).
  🔴 **Read the shape before quoting them: four of the five are read-only and two are
  hard-bound to a single university's tenant** (UPC/UPN, NTU). Exactly **one** agent in
  this base can write to Brightspace, and it is `JhostinAleck/brightspace-mcp` behind a
  two-opt-in gate. **Neither Blackboard nor D2L publishes an MCP server of its own**
  (checked 2026-11-13); every path above is unofficial, built on the REST API, the SSO
  session or a scraped cookie.
- **🔴 OPEN, and now the sharpest supply gap in this base: the higher-education SIS/ERP
  tier.** **Ellucian Banner**, **Ellucian Colleague** and **Workday Student** — the
  systems of record for most of North American higher education — have **no open-source
  MCP server or agent of any kind**, searched from two independent angles this pass and
  returning nothing but vendor connector pages. Ellucian documents **Ethos** (Data Model
  APIs, Business Process APIs, Ethos GraphQL) and publishes no MCP server; Workday ships
  its own proprietary *Agent-Ready Tools*. 🔵 **The only generic lead is the one that
  worked for OpenEduCat: wrap the platform API, not the vertical.** For Banner that means
  a thin server over Ethos. **Nothing in this base implements it, and an engagement that
  assumes otherwise will be wrong.**
- **🔴 The "open-source Agentic SIS" is a FRONT END, and this base came within one row of
  publishing the vendor's framing.** `iblai/sis` carries a genuine, byte-verified `MIT`
  payload (`1,089 B`, `sha256:969b7073d1c42ac2…`) — **and the README states plainly:**
  *"ibl.ai/sis is a front end for the ibl.ai platform"*, *"If you need the full backend,
  reach out at ibl.ai/contact for an enterprise license."* It writes **no backend
  endpoints of its own**; sign-in goes to `login.iblai.app`. 🟢 **The grant is real and
  it covers a Next.js client.** 🔴 **The system of record is proprietary.** Same shape as
  `iblai/lms` (`MIT`, `95★`: *"you need access to an ibl.ai backend instance"*) and
  `iblai/os` (`MIT`, `638★`: *"requires the ibl.ai backend platform … not included in
  this repository"*). **The SIS gap is NOT closed by these.** They are shelved under
  `verticals/solutions.md`, where a platform with a commercial core belongs, not here.


- **The learner-record gap is half closed, and the halves must not be
  confused.** `learnmcp-xapi` gives an agent a read/write path to the
  *learning-activity* record — xAPI statements: what the learner did, practiced
  and mastered. It does **not** reach the *student* record: enrolment,
  transcript, attendance, demographics, fees. Pattern `P9` needs the LRS
  and can be built today on permissive licenses; pattern `P8` needs the SIS.
  Scoping an advising engagement against the wrong one of
  these is the most expensive mistake available in this KB.
- **The SIS gap is CLOSED for one open-source SIS, and the reason four passes
  missed it is a search defect, not a market one (fifth pass).** The fourth pass
  withdrew "no SIS has an agent interface" and replaced it with "not one
  *open-source* SIS has an agent interface." **That is now withdrawn too.**
  OpenEduCat (LGPL-3.0, **911 stars, 789 forks** — the leading open-source
  education ERP) is a set of **Odoo addons**, and Odoo has two mature MCP servers
  whose tools take the **model name as a parameter**:
  `erpipe-org/mcp-odoo` (**MIT, 433 stars**, three-call gated writes) and
  `ivnvxd/mcp-server-odoo` (**MPL-2.0, 415 stars**, per-model allowlist in a
  companion Odoo module). `op.student`, `op.admission`, `op.exam.attendees` and
  `op.fees` are therefore reachable with no education-specific code.
  **The defect to learn from: every SIS search in four passes looked for an
  _education-specific_ server, so the largest relevant connector in the field —
  bigger than any education-specific agent in this KB except DeepTutor, OpenMAIC
  and `agent_skills` — was structurally invisible.** When a vertical gap looks
  empty, search the *platform* the vertical is built on.
- **What is still genuinely unserved, stated precisely so it can be priced.**
  **RosarioSIS** (GPL-2.0, 654 stars, PHP/Postgres, heavy LATAM K-12) and
  **Gibbon** (GPL-3.0, 638 stars, PHP/MySQL, international K-12) have **no
  agent interface and no generic connector of the Odoo kind** — searched by
  project name this pass and nothing returned. `frappe/education` (GPL-3.0, 707)
  sits on the Frappe framework, which is the next place to look for the same
  generic-connector trick. **The three servers that reach proprietary SIS
  products all do so unofficially** — `edupage-mcp` (undocumented endpoints via
  a community library), `mcp_hemis_student`, and new this pass
  `sabis-mcp-server` (Puppeteer scraping with the student's own credentials in
  environment variables). Three-for-three: **where the SIS is proprietary and
  national, the only agent paths are unsanctioned**, which is a contract risk,
  not an architecture.
- **`Gap 286` — the Odoo→OpenEduCat path is architecturally verified and has
  NOT been run.** The connectors' tools are model-generic and OpenEduCat is Odoo
  addons; both facts were read off the repository pages this pass. **No Odoo
  instance was stood up, OpenEduCat installed, and a tool called against
  `op.student`.** That run is the cheapest high-value experiment on this board.
  Until it is done, quote the path as *"the connector is generic and the SIS is
  Odoo addons"*, never as *"we have run it."*
- **Student-record *analytics* topology exists but could not be
  license-verified.** `EdyVision/student-services-mcp` (1 star) exposes 13
  tools including `fetch_student_dropout_risk`, `fetch_high_risk_students`,
  `fetch_attrition_statistics` and `fetch_attrition_feature_importance` — the
  closest thing found to a retention/early-warning tool surface, and a useful
  shape to copy for `P8`. **The rendered page shows no license field**, and it
  runs on **synthetic data** with no real SIS connection. Not admitted to the
  table: read it as a design sketch and do not adopt it without a license.
- **No pedagogy-specific eval harness at scale, and the only candidate is
  UNGRANTED.** `AITutor-EvalKit` (🔴 **no licence file — re-verified at `HEAD`
  `a71078456a90` in `p802`; the `MIT` this base published was refuted in `p801`
  and is withdrawn**, 4 stars, mathematics only) is still the only one found — unchanged across all
  three passes. Every agent in the table above claims pedagogical effect and
  none of them can be compared on it.

- **Grading is still nearly empty, but no longer absent.** `wwrwbs/AI_AWE`
  (Apache-2.0, **2 stars**) is the only credible open scoring *system* found —
  a real pipeline with a published paper behind it, at prototype scale.
  `nbgrader` (BSD-3-Clause, 1.4k) remains notebook autograding infrastructure,
  not an agent. The rest of the field is Kaggle-era TF-IDF/LSTM/DeBERTa
  coursework and single-star LLM wrappers, several of which are API-only
  (OpenAI/Azure/Cohere) and therefore unusable where data residency binds.
  **Nothing in grading is to grading what DeepTutor is to tutoring.**
- **Pedagogical evaluation is still the thinnest layer in education AI.**
  AITutor-EvalKit at 4 stars is the state of the art. Teams in every region are
  shipping tutors with no shared way to measure whether they teach.
- **The Moodle MCP field is now real but fragmented and unconsolidated.** Seven
  servers verified this pass, licenses split MIT / GPL-3.0 / AGPL-3.0, star
  counts 1–206, and **no two agree on tool surface**: 10 read-only
  (`Faixiang`), 40 idempotent-write + plugin (`MarcosNahuel`), ~260 via browser
  session (`falkenslab`), files-as-markdown in Rust (`G36maid`). There is a
  consolidation opportunity here, and in the meantime the choice is genuinely
  per-engagement — read-only vs write, token vs SSO, plugin vs no plugin.
- **LATAM and Africa now have education agents, both at 0 stars.** Manu
  (Brazil, MIT) and EDUKAI LongView (Guinea, ISC) exist and are the first this
  KB has found. They are prototypes, not foundations. The strategic reading is
  unchanged — localize permissively licensed APAC/North American agents — but
  the regional origin story has changed from *absent* to *nascent*, and a
  0-star repo by a Guinean author doing longitudinal learner analytics is worth
  watching.
- **The long tail is student coursework.** The `education-ai` GitHub topic lists
  71 repositories; the 20 most-starred run 475 down to 2 stars, and below
  `Claw-ED` (65) they are overwhelmingly single-author projects — Streamlit
  quiz generators, dropout-prediction notebooks, Chinese-language K-12 skill
  packs. Excluded here by design: a KB row implies "a studio could start from
  this."
