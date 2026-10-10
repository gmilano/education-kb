---
industry: education
region: Global
updated: 2026-10-10
---

# Education — AI agents shelf

**Pass 109, 2026-10-10.** ⏱️ **Nineteenth pass of this date** (107: 16:4x–17:xx UTC;
108: 17:4x–18:xx; this one 18:4x–19:xx).

🟢 **Instrument this pass: `compose/code/p109-freshness/` — `test_p109.sh` **32 passed /
0 failed** (fully offline: real git repositories served over `file://`, no mocks);
`freshness.sh` read **296 of 296** shelf addresses, `rc=0` on every one, **zero
unread**.** 🔵 **It adds the third axis in three passes, and the one `Gap 376` actually
asked for at pass 92: not *does it release* (p107), not *what do I pin* (p108), but
**is it alive**.** 🔴 **It also found that a figure p107 published — `head_sha40` — is
the wrong commit for 20 addresses, and `—` for 13 more (`P109-E`).**

### 🔴 🆕 p109 — why the two previous answers could not see this

| pass | axis | answers | cannot say |
|---|---|---|---|
| p107 | tag **count** | how much ref traffic | nothing reliable — it inverts at the top |
| p108 | release **identity** | *can I pin it* | whether the pin is from 2019 |
| 🟢 **p109** | commit **recency** | 🟢 **is it alive** | how good it is |

🔴 **A row can be flawless semver, Apache-2.0, pinnable — and five years dead. p108
would rank it clean and say nothing was wrong.** 🟢 **24 of the 168 rows p108 called
version-pinnable (14.3 %) have not been touched in over a year.**

### 🟢 🆕 p109 — agent-layer rows, now with a liveness column

| row | licence | `class` | pin | last commit | age | band |
|---|---|---|---|---|---|---|
| [`jeanlucio/moodle-local_aihub`](https://github.com/jeanlucio/moodle-local_aihub) | 🟡 GPL-3 (in-LMS) | `semver` | `v1.3.4` | 2026-10-10 | **0 d** | 🟢 fresh |
| [`UniTime/unitime`](https://github.com/UniTime/unitime) | 🟢 Apache-2.0 | `semver` | `v4.9.152` | 2026-10-09 | **1 d** | 🟢 fresh |
| [`CAHLR/pyBKT`](https://github.com/CAHLR/pyBKT) | 🟢 MIT | `semver` | `1.4.3` | 2026-10-08 | **1 d** | 🟢 fresh |
| [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) | 🟢 Apache-2.0 | `semver` | `v1.6.14` | 2026-10-08 | **2 d** | 🟢 fresh |
| [`CAHLR/OATutor`](https://github.com/CAHLR/OATutor) | 🟢 MIT | `semver` | `v1.7` | 2026-09-30 | **10 d** | 🟢 fresh |
| [`bncc-dev/bncc-pacotes`](https://github.com/bncc-dev/bncc-pacotes) | 🟢 MIT + CC BY 4.0 | 🔴 `none` | 🔴 SHA only | 2026-09-26 | **14 d** | 🟢 fresh |
| [`bncc-dev/bncc-dados`](https://github.com/bncc-dev/bncc-dados) | 🟢 MIT + CC BY 4.0 | `prefixed` | `dados-2026.07.1` | 2026-08-11 | **60 d** | 🟢 active |
| [`wanghaoyu0408/OpenRubrics`](https://github.com/wanghaoyu0408/OpenRubrics) | 🟢 MIT | 🔴 `none` | 🔴 SHA only | 2026-06-23 | 🟡 **109 d** | 🟡 slowing |
| [`Qwen-Applications/OpenRS`](https://github.com/Qwen-Applications/OpenRS) | 🟢 Apache-2.0 | 🔴 `none` | 🔴 SHA only | 2026-03-05 | 🔴 **219 d** | 🟡 slowing |
| [`planepig/rubricbench`](https://github.com/planepig/rubricbench) | 🟢 MIT | 🔴 `none` | 🔴 SHA only | 2026-03-03 | 🔴 **221 d** | 🟡 slowing |

### 🔴 🆕 p109 — `Gap 379`'s diagnosis changes shape for the third time, and this reading is the sharpest

🔵 **The `P96-A` / `P107-A` rubric↔curriculum bind has been described for twelve passes
as "four permissive layers, three publishers, no integration", and p107 added "and four
of the five have never cut a release".** 🟢 **Liveness splits the bind cleanly in two,
and the split falls on the publisher boundary:**

```
the RUBRIC half  (China + US academic)        the CURRICULUM half  (Brazil, bncc-dev)
  OpenRS        219 d   slowing                 bncc-pacotes    14 d   fresh
  rubricbench   221 d   slowing                 bncc-dados      60 d   active
  OpenRubrics   109 d   slowing                 bncc-benchmark  21 d   fresh
```

🔴 **Every rubric layer is 3.5–7 months cold. Every curriculum layer is current.**
🟢 **So the bind is not symmetrically stalled — the half that would supply judgement is
cooling while the half that would supply the standard is actively maintained.** 🔵 **For
an engagement that changes the plan: the BNCC side can be consumed as a live dependency,
and the rubric side has to be vendored at a SHA and owned. `Gap 379` stays open, and
`compose/patterns.md` prices it on liveness this pass rather than on releases.**

🟢 **A fourth `bncc-dev` repository, [`bncc-benchmark`](https://github.com/bncc-dev/bncc-benchmark)
(21 d, fresh), is recorded here because the bind has been described with five components
for twelve passes and there are six.**

### 🟡 🆕 p109 — `P106-A`'s memory tier is the cooling half of that pattern too

| `P106-A` component | licence | last commit | age | band |
|---|---|---|---|---|
| [`a2br/moodle-mcp`](https://github.com/a2br/moodle-mcp) | 🟢 MIT | 2026-09-25 | 16 d | 🟢 fresh |
| [`fwu-de/mem-mcp`](https://github.com/fwu-de/mem-mcp) | 🟢 Unlicense | 2026-06-09 | 🟡 **123 d** | 🟡 slowing |

🔵 **p106 called both TAKEABLE and that verdict is unchanged — a permissive licence does
not expire.** 🟡 **But the sidecar's memory tier is the staler of the two, so the pattern's
risk sits there rather than being spread evenly.**

### 🔴 🆕 `P109-A` — the mandated query set is EXHAUSTED, and this pass proves it is not a depth artefact

🟢 **All eight mandated searches ran: four global, one each for North America, EMEA, APAC
and LATAM.** 🔴 **Every one ran in **extended** mode — a deeper, fresher, several-times
costlier channel than the standard mode p104–p108 used.** 🔴 **About **45** candidate
tokens were extracted and **every single one is already held on a live page of this
KB**.**

🔵 **That is a materially stronger negative than any prior pass's, because it retires a
hypothesis rather than repeating an observation.** 🔴 **p104–p108 each recorded "zero new
items" and `P1023` read it as *the channel is saturated*. A reasonable competing
explanation was that standard-mode search was simply too shallow.** 🟢 **It is not: the
expensive channel returns the same zero. The query SET is exhausted, not the channel.**

🟢 **The axis-change remedy (`P933`: search by licence + stack, never by category — the
method that found `GegoK12` at pass 3) was also tested this pass, against three axes, and
all three came back already-held:**

| axis probed | representative candidates | verdict |
|---|---|---|
| agents / frameworks | `LLMs-from-scratch`, `generative-ai-for-beginners`, `nanochat`, `agents-radar`, `500-AI-Agents-Projects`, `awesome-ai-agents-2026` | 🔴 **6 / 6 held** |
| SIS / ERP by licence+stack | `GegoK12`, `frappe/education`, `ERPNext`, `RosarioSIS`, `Fedena` | 🔴 **5 / 5 held** |
| standards / integration | `LTI 1.3`, `ltijs`, `pylti`, `1EdTech/caliper-*`, `xAPI`, `pykt`, `EduKTM` | 🔴 **all held** |

🔵 **Recorded as a standing instruction, because five passes have now spent their search
budget re-confirming it: a future pass should NOT re-run the eight mandated queries
expecting novelty. The cheap, unexhausted channel in this environment is MEASUREMENT of
the shelf this KB already holds — which is what every pass since p106 that produced a new
finding actually did.**

---

# Education — AI agents shelf

**Pass 108, 2026-10-10.** ⏱️ **Eighteenth pass of this date** (106: 15:4x–16:xx UTC;
107: 16:4x–17:xx; this one 17:4x–18:xx).

🟢 **Instrument this pass: `compose/code/p108-release-identity/` — `test_p108.sh`
**38 passed / 0 failed** (offline; five trap fixtures + two real captures); `census.sh`
read **296 of 296** shelf addresses in 1 m 49 s, `rc=0` on every one, **zero unread**.**
🔵 **It reproduces all six of p107's hand-read pins exactly, then finds four systematic
faults that six spot-checks could not have surfaced.** 🔴 **`api.github.com` repo
endpoints remain 403 by session scoping, so ★ stays unread — and this pass declines to
"fix" that by attaching third-party repos with `add_repo` purely to harvest their
metadata (`P108-H`, below).**

### 🟢 🆕 p108 — the shelf's third axis: not *does it release*, but **what do I pin**

| `class` | n | share | what to pin |
|---|---|---|---|
| `semver` | 159 | 53.7 % | 🟢 `latest_stable` — a bare `vN.N.N` exists |
| `prefixed` | 9 | 3.0 % | 🟢 `latest_prefix` — a release under a project prefix |
| `stamp` | 15 | 5.1 % | 🔴 **no version anywhere** — a commit SHA, nothing else |
| `none` | 113 | 38.2 % | 🔴 no tags — a commit SHA, nothing else |
| **total** | **296** | | 🟢 **version-pinnable: 168 (56.8 %)** |

🔵 **Denominator is 296, not p107's 299: three addresses were case-duplicates of three
others (`P108-F`).**

### 🟢 Agent-layer rows, now with a release identity rather than a tag count

| row | licence | tags | `class` | pin |
|---|---|---|---|---|
| [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) | 🟢 Apache-2.0 | 🟢 **86** | `semver` | 🟢 **`v1.6.14`** |
| [`UniTime/unitime`](https://github.com/UniTime/unitime) | 🟢 Apache-2.0 | 🟢 **101** | `semver` | 🟢 **`v4.9.152`** |
| [`CAHLR/pyBKT`](https://github.com/CAHLR/pyBKT) | 🟢 MIT | 🟡 **4** | `semver` | 🟢 **`1.4.3`** |
| [`CAHLR/OATutor`](https://github.com/CAHLR/OATutor) | 🟢 MIT | 🟡 **4** | `semver` | 🟢 **`v1.7`** |
| [`jeanlucio/moodle-local_aihub`](https://github.com/jeanlucio/moodle-local_aihub) | 🟡 GPL-3 (in-LMS) | 🟢 **9** | `semver` | 🟢 **`v1.3.4`** |
| [`bncc-dev/bncc-dados`](https://github.com/bncc-dev/bncc-dados) | 🟢 MIT + CC BY 4.0 | 🟡 **3** | `prefixed` | 🟢 **`dados-2026.07.1`** |
| [`Qwen-Applications/OpenRS`](https://github.com/Qwen-Applications/OpenRS) | 🟢 Apache-2.0 | 🔴 **0** | `none` | 🔴 **SHA only** |
| [`wanghaoyu0408/OpenRubrics`](https://github.com/wanghaoyu0408/OpenRubrics) | 🟢 MIT | 🔴 **0** | `none` | 🔴 **SHA only** |
| [`planepig/rubricbench`](https://github.com/planepig/rubricbench) | 🟢 MIT | 🔴 **0** | `none` | 🔴 **SHA only** |
| [`bncc-dev/bncc-pacotes`](https://github.com/bncc-dev/bncc-pacotes) | 🟢 MIT + CC BY 4.0 | 🔴 **0** | `none` | 🔴 **SHA only** |

🔴 **Four of the five components of the `P96-A` / `P107-A` rubric↔curriculum bind are
`class=none`.** 🟢 **That is unchanged from p107's finding and is restated here because
p108 now expresses it in the units an engagement plan uses: the bind cannot be
version-pinned, only SHA-pinned, and `compose/patterns.md` prices it accordingly.**

### 🔵 🆕 `P108-H` — a boundary this pass declined to cross

🔴 **The ★ column has read `—` since pass 93 because `api.github.com` 403s for any repo
not attached to this session.** 🔵 **`add_repo` would lift that, repo by repo, and this
session demonstrably has the tool: it used it once this pass, for `gmilano/education-kb`,
which is this KB's own publishing target.** 🔴 **It was NOT used to attach
`moodle/moodle`, `openedx/edx-platform` or any other third-party repository, because
attaching somebody else's repository to harvest star counts is not what the mechanism is
for.** 🟢 **The ★ column therefore stays honestly unread rather than dishonestly filled,
and the release ladder and release identity carry the maintenance signal instead.**
🔵 **Recorded as a standing rule so later passes stop re-litigating it.**

---


# Education — AI agents shelf

**Pass 107, 2026-10-10.** ⏱️ **Seventeenth pass of this date** (105: 14:4x–15:xx UTC; 106:
15:4x–16:xx; this one 16:4x–17:xx).

🟢 **Instrument written and executed this pass: `compose/code/p107-git-lane-census/` —
`test_p107.sh` 20 passed / 0 failed (offline, real captured fixtures); `census.sh` read **299 of 299**
shelf addresses in 2 m 17 s, `rc=0` on every one.** 🔴 **`api.github.com` repo endpoints are STILL
403 — but the 403 was triaged this pass and is an authorization boundary, not an outage
(`P107-A`), so a `—` in a ★ column is permanently unread rather than temporarily unread.**
🟢 **A second axis replaces it below: the release ladder, read from the anonymous git lane.**

### 🔴 🆕 p107 — the shelf's second axis, measured for the first time in 107 passes: **38 % of it has never shipped a release**

🟢 **`P107-D`: a licence probe answers *may I use it*; a ref probe answers *can I pin it*.** 🔴 **This
KB has run the first for 107 passes and the second never**, and the two are independent — a row can
be flawlessly permissive and still have no version to depend on.

```
299 shelf addresses, every one read:
  0 tags      — UNRELEASED    114   38.1%
  1–4         — nascent        37   12.4%
  5–24        — shipping       45   15.1%
  25–99       — mature         40   13.4%
  100+        — industrial     63   21.1%
```

🔴 **114 rows of this shelf cannot be pinned to anything.** 🟡 **That is not a disqualification — it
is a cost that was previously invisible: vendoring at a SHA, carrying your own patches, and owning
the upgrade path.**

### 🔴 🆕 p107 — the two flagship patterns, scored on the new axis, and **both fail it**

| `P96-A` component (`Gap 379`, open 11 passes) | licence | tags | |
|---|---|---|---|
| [`Qwen-Applications/OpenRS`](https://github.com/Qwen-Applications/OpenRS) | 🟢 Apache-2.0 | 🔴 **0** | the rubric judge |
| [`wanghaoyu0408/OpenRubrics`](https://github.com/wanghaoyu0408/OpenRubrics) | 🟢 MIT | 🔴 **0** | the generator |
| [`planepig/rubricbench`](https://github.com/planepig/rubricbench) | 🟢 MIT | 🔴 **0** | the calibrator, 1 147 expert annotations |
| [`bncc-dev/bncc-pacotes`](https://github.com/bncc-dev/bncc-pacotes) | 🟢 MIT + CC BY 4.0 | 🔴 **0** | 1 721 BNCC objectives, 7 MCP tools |
| [`bncc-dev/bncc-dados`](https://github.com/bncc-dev/bncc-dados) | 🟢 MIT / CC BY 4.0 | 🟡 **3** | `dados-2026.07.1` — the only ladder |

🔴 **`Gap 379` has been stated for eleven passes as "four permissive layers, three publishers, no
integration". The diagnosis was incomplete: four of the five layers have never cut a release.**
🟢 **So the missing piece is not only the wiring — there is no version of any layer to wire
*against*.** 🔵 **Re-specified as `P107-A` in `compose/patterns.md`; `Gap 379` stays open, cost
revised upward.**

🔴 **`P106-A`, specified LAST pass, scores 3 of 5 unreleased** — including both rows the pattern
leans on: `a2br/moodle-mcp` (MIT, *"the measured precedent"*) and `fwu-de/mem-mcp` (Unlicense,
*"the memory tier"*), both **0 tags**. 🟡 **Its GPL-3 half ships (`moodle-local_aihub` `v1.3.4`,
`moodle` `v5.3.0-rc2`); the permissive sidecar half — the half that exists to be licensable — does
not.** 🟢 **p106's verdict that those rows are TAKEABLE stands and is unchanged. Takeable and
pinnable are simply different claims.**

### 🟢 🆕 p107 — the rows that DO ship, with the version to pin

| row | licence | tags | pin |
|---|---|---|---|
| [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) | 🟢 Apache-2.0 | 🟢 **86** | `v1.6.14` |
| [`UniTime/unitime`](https://github.com/UniTime/unitime) | 🟢 Apache-2.0 | 🟢 **101** | `v4.9.152` |
| [`jeanlucio/moodle-local_aihub`](https://github.com/jeanlucio/moodle-local_aihub) | 🟡 GPL-3 (in-LMS) | 🟢 **9** | `v1.3.4` |
| [`CAHLR/pyBKT`](https://github.com/CAHLR/pyBKT) | 🟢 MIT | 🟡 **4** | `1.4.3` |
| [`CAHLR/OATutor`](https://github.com/CAHLR/OATutor) | 🟢 MIT | 🟡 **4** | `v1.7` |

🔵 **`UniTime/unitime` also discharges `Gap 381` on the new axis** — the tested MCP gate this KB has
carried in `compose/code/` since pass 42 points at a repository with **101 releases and a pinnable
`v4.9.152`**. 🟢 **It is the best-engineered permissive asset on this shelf and it reached no shelf
page until pass 106.**

**Pass 106, 2026-10-10.** ⏱️ **Sixteenth pass of this date** (103: 12:4x–13:xx UTC; 104:
13:4x–14:xx; 105: 14:4x–15:xx; this one 15:4x–16:xx).

🟢 **Instrument written and executed this pass: `compose/code/p1040-ecl-corpus-census/` —
`test_p1040.sh` 82 passed / 0 failed; `census.sh` read 1 381 addresses in 2 m 22 s with empty
stderr.** 🔵 **`P1028` holds a fourth pass.** 🔴 **`api.github.com` = `http=403` for a fourteenth
consecutive pass, which is why every ★ below is `—`: unread, never zero.**

### 🟢 🆕 p106 — this page's own warnings, re-derived MECHANICALLY, and they agree **13 of 13**

🔵 **The whole-corpus census (`Gap 398`) gave the classifier a bucket it never had: `NON-GRANT`, for
a payload that resolves 200 and grants nothing.** 🟢 **It found 13 such rows. Every one of the 13 is
ALREADY characterised as unusable in this KB's prose** — `dssg/student-early-warning` as *"not
OSI-licensed"*, `skills-ml` as *"do NOT start from"*, `cloud-learning-ce` as all-rights-reserved
(`P1029`), the Elastic and PolyForm rows as commercial bars in `agents/trending.md`.

🟢 **So this is an AGREEMENT, not a correction, and it is the first time the restriction tier has
been derived by code rather than by hand:** 13 hand-written warnings accumulated over many passes,
13 rows found mechanically, the same 13. 🔵 **`p963`'s shelf-licence-agreement gate, satisfied for
the restricted tier.**

🔴 **The commercially load-bearing half:** `canyongbs/advisingapp` — a **student-advising platform** —
is Elastic-2.0; `sdv-dev/sdv` (synthetic data) is BUSL-1.1; `sodadata/soda-core` (data quality) is
Elastic-2.0. 🟡 **All three are infrastructure a studio reaches for by reflex, and none can be
embedded in a client deliverable.**

### 🟢 🆕 p106 — three agent-layer rows measured, and only one is takeable

| row | licence | bytes | verdict |
|---|---|---|---|
| 🆕 [`fwu-de/mem-mcp`](https://github.com/fwu-de/mem-mcp) | 🟢 **Unlicense** | 1 211 | 🟢 **TAKEABLE — public domain.** An MCP server from the German federal education-media institute; 🔵 **the single most permissive row in this KB's EMEA tier** |
| 🆕 [`frdel/agent-zero`](https://github.com/frdel/agent-zero) | 🟢 MIT | 1 150 | 🟡 **permissive but OFF-INDUSTRY** — a general Dockerised agent framework, no education surface. 🔵 **`P1023` predicted it; the probe settles it** |
| 🆕 [`Earth-OL-Player/Ai_learn_project`](https://github.com/Earth-OL-Player/Ai_learn_project) | 🔴 **PolyForm Noncommercial** | 181 | 🔴 **NOT takeable.** 🔵 **Declared in Chinese** (*「仅允许非商业用途」*) in a 181 B `LICENSE.md` — a row that three passes ago read `UNRECOGNISED` and sat beside real grants |

🔵 **All three came from pass 105's battery, which shelved them as "secondary-only, none probed".
They are probed now, and the pattern is `P1023`'s: a search surfaces permissive rows that are not
education, and education rows that are not permissive.**

### 🔴 🆕 p106 — the agent/MCP layer's licence composition, measured across the whole corpus

🔵 **1 381 addresses, every payload read (`P1005`), buckets named by PROPERTY (`P1037`):**

| bucket | rows |
|---|---|
| permissive | 🟢 **804** |
| copyleft | 199 |
| CC family | 51 |
| 🔴 **not a grant** | 🔴 **13** |
| 🟡 unread (`Gap 401`) | 🟡 **17** |
| **total with a payload** | **1 084** |

🟢 **804 + 199 + 51 + 13 + 17 = 1 084 — it reconciles.** 🔴 **Beside it: 233 rows resolve and serve
NO licence payload at eleven filenames with a clean 200 control**, 38 `ABSENT`, 25 without a
control, and 🔴 **1 `THROTTLED`** (`appliedrelevance/frappe_mcp_server`, `429` — reported as
**unmeasured**, never as absent; `Gap 388`).

🔵 **`T28` is unmoved and now has a second channel behind it (`T34`, `intel/trends.md`): Moodle's own
AI-subsystem plugin types — `moodle-aiprovider` and `moodle-aiplacement` — return **ZERO** packages
on `packagist.org` against 159 across 21 older types.** 🟢 **The LMS→agent seam is a Globant
deliverable, measured twice by two instruments on two channels.**

**Pass 104, 2026-10-10.** ⏱️ **Fourteenth pass of this date** (91: 2026-10-09 23:0x–00:00 UTC; 92:
00:4x–01:3x; 93: 01:4x–02:24; 94: 02:5x; 95: 03:4x; 96: 04:4x–05:xx; 97: 05:4x–06:xx; 98:
06:4x–07:xx; 99: 07:4x–08:xx; 100: 08:4x–09:xx; 101: 09:4x–10:xx; 102: 10:4x–11:xx; this one
12:4x–13:xx).

🔵 **Instrument state, measured TWICE inside this pass, and the two answers differ by AUTHORSHIP.**
🔴 A **pre-existing** instrument of this repository (`p383-region-heading-gate/check_headings.py`) was
**REFUSED** (`[Code from External]`). 🟢 An instrument **written in this pass**
(`p1026-archive-regression-census/`) **RAN**: `test_census.sh` **9 passed, 0 failed**, and
`census.sh . ./archive` returned `681 / 1 419 / 88`. 🔵 **`P1028`: `Gap 383` is not alternating
between passes as pass 102 read it — the restriction is on executing this KB's back catalogue, and a
measurement packaged fresh still runs.**

🔵 **Carried from pass 101, not re-measured here** (pass 102 and pass 103 both had the ladder
refused): 🟢 **the instrument RAN for the first time since pass 92 — and exactly half of it did.**
`test_ladder.sh` executed offline: **16 passed, 0 failed**. `./ladder.sh --reach` returned
`names=24 byte-floor=1B classifier=lib/license_family.sh`. 🔴 **Its NETWORK path was refused** —
`./ladder.sh <slug>` was denied backgrounded *and* in the foreground.
🔵 **So `Gap 376` was never "the instrument is unrunnable". It is "the instrument's network path is
denied; its classifier and its reach are VERIFIED."** Those are two facts and nine passes reported them
as one. 🟢 **The ten registered corrections in `lib/license_family.sh` are now known-good by
execution rather than by assertion** — including the `GPL-2.0` title-block pair (`oat-sa/tao-core`,
`portabilis/i-educar`) that `v3`'s fork got wrong and that reached a published client recommendation.

🟢 **`P1005` applied from the outset, in this pass as in the last**: every address below came from
`git ls-remote --symref` run inline, every licence from a `raw.githubusercontent.com` payload, every
tag count from `git ls-remote --tags`. 🔴 **`api.github.com` returns `http=403` for every repository not attached to
this session — measured this pass, with the proxy's own message.** 🔵 **That is WHY the ★ column is
unread, and this is the first pass to establish the CAUSE instead of restating the effect.**

🔵 **Marker convention.** A bare 🆕 is inherited from the pass that added the row; **rows added or
re-measured by this pass are marked 🆕 p103.** 🔴 **A `—` in the ★ column means not read this pass.
It never means zero** — and 🟢 **this pass measured the cause again: `api.github.com` is `403` for
every repository not attached to this session.**

### 🟢 🆕 p105 What pass 105 adds — the shelf's permissive count was **38, not 40**, and this pass's own instrument was wrong twice before it was right

🔵 **No agent joined this shelf. The headline is that two agents already on it were in the wrong
bucket, and the mechanism that put them there is still running.**

🔴 **`classify_payload` — the licence classifier that `p1029` ran over all 99 addresses in pass 104
— returns `UNRECOGNISED` for every Educational Community License payload in the Apereo lineage.**
🟢 **Cause, read from the text rather than inferred: the ECL-2.0 licence contains ZERO occurrences
of the string `Apache License`.** It names the *"Apache 2.0 license"* in lower case, so a pattern
keyed on the Apache title never fires.

🔵 **ECL-2.0 is the Apache-2.0 text with section 3's patent grant narrowed to education — it is
PERMISSIVE, and it is the only OSI-approved licence written for this industry.** 🔴 **So two rows
Globant can build on were outside the permissive count for two passes:**

| row | bytes | `sha256` (16) | was | 🟢 **is** |
|---|---|---|---|---|
| [`Apereo-LAI/lap-sakai-extractor`](https://github.com/Apereo-Learning-Analytics-Initiative/lap-sakai-extractor) | 11 087 | `a9ea5cca8da2c8d5` | 🔴 `UNRECOGNISED` | 🟢 **ECL-2.0 · permissive** |
| [`Apereo-LAI/OpenDashboard-legacy`](https://github.com/Apereo-Learning-Analytics-Initiative/OpenDashboard-legacy) | 9 919 | `fb10d1260ddc8dff` | 🔴 `UNRECOGNISED` | 🟢 **ECL-2.0 · permissive** |

🟢 **Permissive 38 → 40; copyleft 22; CC 5; one payload that is not a grant. 40 + 22 + 5 + 1 = 68,
and the granted total reconciles to the row.**

🟡 **Reading guidance for anyone picking an agent off this shelf:** 🔴 **an `UNRECOGNISED` licence
column is not a reason to skip a row.** It is three unlike situations under one label — a permissive
grant the tooling cannot see, a copyleft grant named elsewhere, and a genuine all-rights-reserved
file called `LICENSE` (`P1029`). 🟢 **Two of the three are buildable, and only reading the payload
tells you which you have.**

#### 🔴 Two bugs this pass found in its own code, before it found anything about education

🟢 **`test_p1035.sh`: 33 passed, 0 failed — and 9 of the 33 are regressions for this pass's own
errors.** 🔵 **Both are recorded because both were the kind that publishes wrong data quietly.**

| # | the bug | what it would have published |
|---|---|---|
| 1 | 🔴 **`place_string` placed any `universidad de …` string in EMEA.** `mietiainvestigacion-creator/api-eduadapt` names **Universidad de Córdoba** — Córdoba, **Spain** *and* Córdoba, **Colombia** | 🔴 **a LATAM row published as EMEA supply.** 🟢 Corrected: an institution name alone is `UNPLACED`; only a ccTLD, a country word or a nationally unique system name (`SIGAA`, `UNAM`) places a row, and every row carries the string that placed it (`P1035`) |
| 2 | 🟡 **`declared_name` split ECL into "titled" and "unversioned" families** because the 9 919 B payload carries *"Version 2.0, April 2007"* on a line BELOW its title | 🟡 **one grant reported as two licence families, on line-wrapping alone.** 🟢 Corrected: title and version are sought independently |

🔵 **`P1039`: write the test that could refute the finding and keep the refuted branch.** This pass
asserted ECL would **mislabel as Apache**, measured that it does not, and kept both branches — so
the day an ECL payload does carry the Apache title, the audit says so instead of staying silent.

#### 🔴 The agent battery saturated a fifth consecutive pass

🟢 **Four global queries ran, every hit `grep`-checked against the live corpus.** 🔴 **Not one
returned an education agent this shelf does not hold** — DeepTutor, ChatTutor, Instructional Agents,
OATutor, pyKT, Artemis (Iris / Athena / Hyperion), `frappe/lms` all already shelved. 🔵 **What the
query actually returns is general-purpose agent rankings from vendor-neutral blogs — OpenClaw,
OpenHands, CrewAI, LangGraph, goose, aider — with no education layer, and `P1023` has predicted this
five passes running.**

🟡 **Three addresses were new to the corpus and are deliberately NOT shelved here, because none was
probed:** `Earth-OL-Player/Ai_learn_project`, `frdel/agent-zero`, `DataTalksClub/llm-zoomcamp`.
🔴 **An unprobed address does not go on a shelf page** (`P1026`: a worklist is not a shelf).
🟢 **All three are pre-registered for probing next pass.**

### 🟢 🆕 p104 What pass 104 adds — `Gap 394` is probed to the last address, and the MCP layer it recovered is **53 % unusable**

🟢 **Instrument written and executed: `compose/code/p1029-lost-address-recovery/`.**
`test_probe.sh` **18 passed, 0 failed**; `probe.sh addresses.txt` →
`live=94 absent=5 with_grant=68 no_grant=23 no_control=3`.

🔵 **`Gap 394` carried 68 unprobed addresses. This pass probed 99** — the whole `LOST` list of 82
plus the 17 worklist-only addresses pass 103 never reached. 🟢 **Nothing in `Gap 394` is unprobed.**

🟢 **The four rows pass 103 had already measured were left in the input as blind calibration, and
4 of 4 agree to the byte and to the tag.** 🔵 **That is the only reason the other 95 rows are worth
reading.**

#### 🔴 `T28` — the education MCP layer is the LEAST licensed layer this KB has measured

🔵 **15 of the 99 addresses are MCP servers for an education system** (Moodle, Canvas, a district, a
national SIS). 🔴 **Eight of the fifteen cannot be used commercially at all.**

| MCP layer, 15 rows | n | |
|---|---|---|
| 🟢 **MIT** | **6** | `ahnopologetic/canvas-lms-mcp` (3 tags) · `jibberswrld/fcps-school-mcp` (4) · `sukhrobyangibaev/mcp_hemis_student` (1) · `ait0u5hi/canvas-scholar-mcp` (1) · `a2br/moodle-mcp` (0) · `jorickpepin/campus-mcp` (0) |
| 🔴 **no payload at 11 filenames, clean 200-control** | 🔴 **6** | `ink-waffle/moodle-mcp` · `ink-waffle/sisu-mcp` · `dddanielliu/nccu-moodle-mcp` · `git-pratap-shrey/uniai_mcp` · `poorvika12-hub/student_mcp` · `hocphi-info/hocphi-info-mcp` |
| 🔴 **ABSENT** | 🔴 **2** | `owentaylor/canvas-mcp` · `imazhar101/mcp-canvas-server` |
| 🟡 copyleft | 1 | `hefi002/tfg-mcp-moodle-server` (GPL-3.0) |

🔴 **Canvas is the sharpest case: four Canvas MCP servers, two MIT and two ABSENT.** 🔵 **Commercial
consequence: the LMS-to-agent bridge is the layer a Globant engagement must expect to OWN. It is
written by individuals, it is rarely licensed, and it disappears — 🟢 the two with release
engineering (`canvas-lms-mcp`, `fcps-school-mcp`) are the only ones worth forking rather than
rewriting.**

#### 🟢 The permissive rows this shelf gets back

🔵 **Every grant below is a `raw.githubusercontent.com` payload read at the measured ref, with bytes
and `sha256` (`P1005`). No row is here on the strength of a licence *name*.**

| agent / tool | grant · bytes | ref · tags | region | what it is |
|---|---|---|---|---|
| [`aiverify-foundation/moonshot-ui`](https://github.com/aiverify-foundation/moonshot-ui) | 🟢 **Apache-2.0** · `LICENSE.md` 11 347 B | `main` · 🟢 **23** | 🟢 **APAC** (AI Verify Foundation, Singapore) | 🟢 **Completes the eval harness.** `moonshot` + `moonshot-cicd` + `moonshot-ui` are **all three Apache-2.0 and all three released** |
| [`ahnopologetic/canvas-lms-mcp`](https://github.com/ahnopologetic/canvas-lms-mcp) | 🟢 **MIT** · 1 091 B | `main` · 🟢 3 | 🔵 unplaced (individual holder) | Canvas LMS as MCP tools — courses, assignments, submissions |
| [`jibberswrld/fcps-school-mcp`](https://github.com/jibberswrld/fcps-school-mcp) | 🟢 **MIT** · 1 073 B | `main` · 🟢 4 | 🟢 **North America** (Fairfax County Public Schools) | 🔵 **A K-12 DISTRICT's own MCP surface** — the only district-scoped one in the corpus |
| [`eai6/ai-tutor`](https://github.com/eai6/ai-tutor) | 🟢 **MIT** · 1 090 B | `main` · 🟢 8 | 🔵 unplaced | Tutoring agent with the most release history of the recovered tutors |
| [`sukhrobyangibaev/mcp_hemis_student`](https://github.com/sukhrobyangibaev/mcp_hemis_student) | 🟢 **MIT** · 1 074 B | `main` · 1 | 🟢 **APAC** (Uzbekistan — HEMIS, the national HE information system) | 🔵 **A national SIS exposed as MCP.** The pattern a ministry engagement starts from |
| [`marc-shade/docsingest`](https://github.com/marc-shade/docsingest) | 🟢 **MIT** · 1 079 B | `main` · 2 | 🔵 unplaced | Document-to-context ingestion for courseware corpora |
| [`ait0u5hi/canvas-scholar-mcp`](https://github.com/ait0u5hi/canvas-scholar-mcp) | 🟢 **MIT** · 1 065 B | `main` · 1 | 🔵 unplaced | Second surviving Canvas MCP |
| [`a2br/moodle-mcp`](https://github.com/a2br/moodle-mcp) | 🟢 **MIT** · 1 073 B | `main` · 0 | 🔵 unplaced | Moodle as MCP tools — 🔴 **no releases** |
| [`jorickpepin/campus-mcp`](https://github.com/jorickpepin/campus-mcp) | 🟢 **MIT** · 1 069 B | `main` · 0 | 🔵 unplaced | Campus-services MCP |
| [`sngdtechnologies/ai-moodle-security`](https://github.com/sngdtechnologies/ai-moodle-security) | 🟢 **BSD-2-Clause** · 1 299 B | `main` · 0 | 🔵 unplaced | 🔵 **The only BSD-2 row in the corpus** — AI-assisted Moodle hardening |
| [`hkuds/paper2slides`](https://github.com/hkuds/paper2slides) | 🟢 **MIT** · 1 062 B | `main` · 0 | 🟢 **APAC** (HKU Data Science Lab) | Paper → lecture slides |
| [`thu-maic/dsh-openmaic`](https://github.com/thu-maic/dsh-openmaic) | 🟢 **MIT** · 1 078 B | `main` · 0 | 🟢 **APAC** (Tsinghua) | Multi-agent instructional content |
| [`gemlab-hku/unlearn_and_relearn`](https://github.com/gemlab-hku/unlearn_and_relearn) | 🟢 **MIT** · 1 074 B | `main` · 0 | 🟢 **APAC** (HKU) | Knowledge-editing research code |
| [`aliipou/student-retention-prediction`](https://github.com/aliipou/student-retention-prediction) | 🟢 **MIT** · 1 098 B | `main` · 0 | 🔵 unplaced | 🔵 **A second permissive early-warning row** — `Gap 385` stays refuted |
| [`mizcausevic-dev/student-data-access-audit-stream`](https://github.com/mizcausevic-dev/student-data-access-audit-stream) | 🟢 **MIT** · 1 069 B | `main` · 0 | 🔵 unplaced | Student-record access audit trail — the FERPA/GDPR evidence layer |
| [`devissaputra/classroom_discourse_intelligence`](https://github.com/devissaputra/classroom_discourse_intelligence) | 🟢 **MIT** · 1 073 B | `main` · 0 | 🔵 unplaced | Classroom talk analytics |
| [`yptheangel/attention-monitor`](https://github.com/yptheangel/attention-monitor) | 🟡 **Apache-2.0** · 11 357 B | `master` · 0 | 🔵 unplaced | 🔴 **Attention monitoring — read `SB 1580` and `AB 1159` before proposing it** |
| [`magnusvron/llm-benchmark-quality-index`](https://github.com/magnusvron/llm-benchmark-quality-index) | 🟡 **MIT for CODE, separate terms for DATA** · 2 488 B | `main` · 0 | 🔵 unplaced | 🔴 **DUAL-licensed — see `P1030`** |

#### 🔴 The answer to pass 103's own next-action, and it is a no

🔵 **`intel/open-gaps.md` listed `aiverify-foundation/llm-evals-catalogue` as action item 4: "if the
catalogue is permissively licensed it supplies the recipe LIBRARY that `P103-A` currently has to
write."** 🔴 **Measured: `LIVE-NOGRANT` — no payload at 11 filenames, clean 200-control at 26 342 B,
and ZERO tags.** 🟢 **So `P103-A` keeps the whole rubric-writing cost; what it does NOT keep is the
UI, because `moonshot-ui` is Apache-2.0 with 23 tags.**

🟡 **And the provenance argument survives intact**: all three granted harness components come from
the foundation the Singapore regulator convened (AI Verify Foundation / IMDA), not from an education
vendor.

#### 🔴 `P1029` — a `LICENSE` that returns 200 is not a grant

🔴 **`yuanjiusheng/cloud-learning-ce` serves 4 117 B from a file named `LICENSE`, and the text is
all-rights-reserved Chinese copyright assertion** — *「版权所有 (c) 2021，猿究生 / 保留所有权利。」*
🔵 **It classifies `UNRECOGNISED` precisely because it matches no grant. Presence is not permission,
and a classifier that mapped filename → licence would have shelved a proprietary LMS.**

### 🔴 🆕 p103 What pass 103 adds — the shelf was missing rows it already owned, and `Gap 393` is now only half a gap

- 🔴 **`Gap 394` OPENED, and it is about this shelf rather than about the supply.** A census of
  `archive/2026-10-06-pre-reset/` against every live file finds **82 of 681 addresses (12.0 %) held
  nowhere outside the archive**, and **103 (15.1 %) on no page at all**. 🟢 **Instrument written and
  executed this pass**: `compose/code/p1026-archive-regression-census/` — `test_census.sh`
  **9 passed, 0 failed**; `census.sh . ./archive` → `archive_addresses=681 live_addresses=1419
  lost_total=88` (**82 `LOST`** + 6 declared `CONTROL`), stable on re-run after its own results were
  committed. 🔵 **`P1026`: the live corpus more than DOUBLED and still lost a sixth of the archive,
  which is why twelve passes of growth never showed it.**
- 🔴 **The 21-address difference between "82" and "103" sits in ONE file** —
  `compose/code/p725-readme-payload-sweep/shelf-repos.2026-10-08.txt`, an instrument's **input
  worklist**. 🔵 **A worklist is not a shelf: those 21 are held by the repository and offered by no
  page.** Among them `mitodl/open-learning-ai-tutor` (**MIT, 15 releases**),
  `project-sunbird/sunbird-devops` (**MIT, 702 tags**) and `ollama/ollama`.
- 🟢 **`Gap 393` is REFRAMED, not discharged — and the reframing changes what a studio sells.**
  Pass 102 left the whole BEA-2025 pedagogical-evaluation layer ungranted on both halves, and that
  is still true. 🟢 **But the HARNESS is permissive and released:**
  [`aiverify-foundation/moonshot`](https://github.com/aiverify-foundation/moonshot) is
  **Apache-2.0** (`LICENSE.md` **11 347 B**), `main` ·
  `03e9344dc9fc949ae05b1f38580611fce36528ab`, **26 tags**, top **`0.7.6`**. Its README names the
  extension points verbatim: **recipes** (custom *"input-target pairs"* datasets, prompt templates,
  an evaluation metric, **grading scales**), **cookbooks**, **connector endpoints**, **attack
  modules**, **context strategies**. 🔵 **A four-dimension rubric on a three-value scale IS a
  Moonshot recipe with a grading scale.** 🔴 **What stays unbuyable is comparability — the MRBench
  labels are the ungranted asset, so no MRBench number is reproducible.** 🟢 **`P103-A`.**
- 🟡 **And note WHERE that harness comes from: the AI Verify Foundation, the body Singapore's IMDA
  convened** — not an education vendor. 🔵 **`T27`.**
- 🔴 **`Gap 396` OPENED — the Open Badges MINTING tier is a dead address at 5 of 5 names.**
  `concentricsky/badgr-server`, `1EdTech/badgr-server`, `IMSGlobal/badgr-server`,
  `instructure/badgr-server` and `concentricsky/badgr-ui` **all return ABSENT**. 🔵 **`P1012`'s
  successor-org axis run properly rather than declared dead on one 404.** 🟢 **The VALIDATOR
  survives:** [`1EdTech/openbadges-validator-core`](https://github.com/1EdTech/openbadges-validator-core),
  **Apache-2.0, 28 tags**, `develop` · `0a66b52`. 🔵 **`T17` one step worse: the permissive grant is
  on the side that MEASURES, and the side that becomes the RECORD is no longer copyleft — it is
  gone.**
- 🔵 **`P1024` — a bundled-grant declaration can live INSIDE the `LICENSE`, and a byte count ABOVE
  pristine is the tell.** `openbadges-validator-core`'s payload is **13 185 B**, **1 828 B more**
  than pristine Apache-2.0 (11 357 B), and the surplus is a subcomponent block (*"The BasicLTI
  Utilities … includes a number of subcomponents with separate copyright notices and license
  terms"*): **OAuth** (© AOL LLC, Google, Netflix) and **Base64** (© the ASF), 🟢 **both
  Apache-2.0, so this one is clean.** 🔴 **`P1013` said read the `NOTICE`; the correction is that the
  `NOTICE`'s CONTENT need not be in a file called `NOTICE`.** 🟢 **Compare to pristine in both
  directions: below means text removed (Ed-Fi's 10 172 B is the omitted appendix), above means
  someone else's grant was added.**
- 🔵 **`P1025` — equal byte count is not identity.** Three Sunbird payloads are all **1 072 B** MIT
  and are not all the same file: `sunbird-devops` and `sunbird-lms-service` hash `7dde0671…`,
  `knowledge-platform` hashes `fd3adcd5…`, and the difference is **© 2018 against © 2019**.
  🔴 **`P386` deduplicates by size; a grant pinned by size is pinned to a coincidence.** 🟢 **Pin by
  `sha256`.**
- 🔴 **`P1020` has a FOURTH and FIFTH non-standard default branch, and `P1021` extends.**
  `bigbluebutton/bigbluebutton` defaults to **`v3.0.x-develop`** and `1EdTech/openbadges-validator-core`
  to **`develop`**; `ed-fi-alliance-oss/Ed-Fi-Data-Standard` defaults to **`v6.2.0`** — 🔵 **a
  TAG-SHAPED branch name, so a `ref` that looks like a version is not evidence that you pinned a
  tag.**
- 🔴 **The mandated battery ran in full — eight queries — and `P1023` holds a SECOND consecutive
  pass: all four regions returned less than this KB holds.** 🟢 **But the retired query has a second
  use (`P1027`): `Tennessee` came back from the North America query, is on NO live page, and sits in
  the archive with its instrument — `SB 1580`, which bars an AI tool from performing mental-health
  assessment or screening of a student.** 🔵 **A regional miss is now evidence about the FILE.**
- 🔴 **Two global queries are exhausted and should be retired, not re-run.** `top open source AI
  agents education {year} github MIT` returned only general frameworks (CrewAI, LangGraph,
  OpenHands, OpenCode). 🔵 **And `github trending education AI {year}` returns LEARNING MATERIAL, not
  education software** — `rasbt/LLMs-from-scratch`, `microsoft/generative-ai-for-beginners`,
  `karpathy/nanochat`. 🔵 **In a trending feed "education" means *teaching people about AI*, not *AI
  for teaching*. That is a channel property and it explains six passes of thin returns.**
- 🔴 **Zero non-GitHub primary-source reads, TWELFTH consecutive pass — and this pass carries the
  error string for four hosts at once.** `unesdoc.unesco.org`, `eur-lex.europa.eu`, `www.oecd.org`
  and `arxiv.org` all return `http=000` with `curl: (56) CONNECT tunnel failed, response 403`:
  🔵 **the gateway refuses the CONNECT tunnel per host, which is a cause, not an outage.**
  🟢 **Controls in the same sweep: `raw.githubusercontent.com` 200, `pypi.org` 200,
  `registry.npmjs.org` 200.**

### 🔴 🆕 p102 What pass 102 adds — `Gap 391` is CONFIRMED and WIDENED: the benchmark's DATA is ungranted too

- 🔴 **`Gap 391` holds at an un-drifted address, second consecutive pass.**
  [`kaushal0494/AITutor-EvalKit`](https://github.com/kaushal0494/AITutor-EvalKit) is still at
  `main` · `a71078456a90a7bb616f7c7e1de83f0bfbc44ab1` — **byte-identical pin to pass 101** — and
  `LICENSE`, `LICENSE.md` and `LICENSE.txt` all return **404**, with a clean `P872` 200-control
  (`README.md` = **14 451 B** at that same SHA). 🔵 **The absence is STABLE, not a timing artifact:
  two passes, one SHA, same answer.**
- 🔴 **`Gap 393` OPENED — and it is the bigger half. The BEA-2025 benchmark DATASET is ungranted.**
  [`kaushal0494/UnifyingAITutorEvaluation`](https://github.com/kaushal0494/UnifyingAITutorEvaluation)
  is the official shared-task data repository (**MRBench**, built from MathDial + Bridge; the dev set
  is **300 dialogues / 2 476 annotated tutor responses**, the test set **191 / 1 547**, labels
  `Yes` / `To some extent` / `No`). `main` · `bbef521ddb875f2cc8a5ee798f4066965a7cfd8a`,
  🔴 **no licence payload at `LICENSE`, `LICENSE.md`, `LICENSE.txt`, `COPYING` or `NOTICE`**, clean
  `P872` 200-control (`README.md` = **9 525 B**).
- 🔵 **`P1022`: when a benchmark's TOOLKIT is ungranted, probe its DATASET repository separately.
  They are two grants and they fail independently.** 🔴 **Here they failed the same way, so the whole
  BEA-2025 pedagogical-evaluation layer — the scorer and the thing it scores against — is unlicensed.**
  🟢 **That changes the purchase**: a studio cannot adopt this evaluation layer, and it cannot
  re-derive it either, because the labels are the asset. 🔵 **Same shape as `Gap 390`/`T21` one level
  worse: there the code was permissive and the corpus was not; here neither is granted.**
- 🟡 **`NaumanNaeem/BEA_2025` is UNRESOLVED, not a negative.** `main` ·
  `bcaa52dae63d4112edea4b0186c386f0fafd5b97`: no payload at 4 licence names **and no 200-control** —
  `README.md`, `readme.md`, `README`, `README.MD`, `requirements.txt` and `.gitignore` are all 404,
  so the probe never proved it reached the tree. 🔵 **Recorded as unread, never as zero.**
- 🔴 **The instrument was REFUSED this pass, and pass 101 RAN it.** `bash ./test_ladder.sh` was denied
  before starting (`[Code from External]`). 🔵 **So `Gap 383`'s state FLIPS between passes rather than
  trending** — pass 101's execution was not the start of a recovery, and this is the first pass to
  record the refusal *after* a success. 🟢 **No classifier was written** (`P237`); every address below
  came from `git ls-remote --symref` run inline and every grant from a `raw.githubusercontent.com`
  payload (`P1005`).
- 🔴 **`api.github.com` and the non-GitHub primary-source hosts were NOT measured this pass.** The
  multi-host probe that opens every pass was itself **denied as a batch**, so the ★ column and the
  primary-source ledger carry `—`, which is unread. 🔵 **A new fact about this environment: the
  channel-probe RITUAL is now gated, independently of the channels it probes.**

### 🟢 🆕 p101 What pass 101 adds, and the headline is a gap discharged by a repository that has existed since 2012

- 🟢 **`Gap 385` is DISCHARGED. A permissive open-source student early-warning system exists:
  [`Jasig/SSP`](https://github.com/Jasig/SSP)** — the Apereo **Student Success Plan** —
  **Apache-2.0**, `LICENSE` 11 359 B, `master` · `711244dc0d6d5c65fd261c9bec77dd48b4dbaaf6`,
  **57 tags** (top `ssp-2.9.0`), `pom.xml` `org.jasig.ssp:ssp:2.9-SNAPSHOT`.
  🔴 **Five passes of this shelf said this layer had no permissive row. It had one with 57 releases.**
- 🔵 **`P1012`: an incumbent consortium's code may still be addressed under its PREDECESSOR
  organisation's name.** Measured, not inferred: `apereo/SSP`, `apereo/OpenLRW`, `apereo/openlrs` and
  `apereo/opencast` **all return ABSENT**; `Jasig/SSP` exists. Apereo was formed from the **JA-SIG +
  Sakai Foundation** merger and *the repository never moved*. 🔴 **Searching the industry, the
  technique and the CURRENT org name all failed. The predecessor name is a fourth axis.**
- 🔴 **`P1013`: a root Apache-2.0 grant does not describe the SHIPPED artifact — read the `NOTICE`.**
  SSP's `NOTICE` declares its bundled grants, and they are not all permissive: **Ext JS under GPL-3.0**
  (with Sencha's FLOSS exception), **JasperReports, JFreeChart, Hibernate Commons Annotations and c3p0
  under LGPL**, **iText under MPL**. 🟢 **Apache-2.0 to take the DOMAIN MODEL; copyleft sits in the
  shipped UI and the reporting layer.** 🔵 **This is `Gap 370`'s shape one level out: `Gap 370` is about
  a per-DIRECTORY licence the root cannot see; this is a per-DEPENDENCY one — and unlike `Gap 370`, the
  `NOTICE` file makes it READABLE. That is a partial instrument, not just a gap.**
- 🔴 **And the honest maturity read, because the licence is the easy half.** `portlet-api` 2.0, Ext JS,
  `spring-security-oauth` 2.5.0 and a `2.9-SNAPSHOT` version put this on a **uPortal-era JVM stack**.
  🟢 **What is deliverable here is the early-alert / caseload / intervention DOMAIN MODEL and its
  57-release schema history — not the front end.** Costed as `P101-A` in `compose/patterns.md`.
- 🔴 **The MODERN ML early-warning tier is ungranted or non-commercial, and that is now MEASURED at
  6 of 6 — see the new tier below.** 🔵 **Same shape as `Gap 372`'s history: the permissive layer is the
  MODEL and the VALIDATION; the production implementation is not permissive.**
- 🔴 **The most-cited repository in this tier excludes Globant's own business model by name.**
  `dssg/student-early-warning` (University of Chicago DSSG) is **not OSI-licensed**: a bespoke
  terms-of-use grant whose permission covers *"academic research or other not-for-profit scholarly
  purposes"* and **"excludes any service or part of selling a service that uses the Program"**.
  🔵 **A services company is the excluded case, verbatim.** Commercial terms via the Polsky Center.
- 🔴 **`Gap 391` OPENED — the pedagogical-alignment judge exists as a TECHNIQUE and is UNGRANTED.**
  [`kaushal0494/AITutor-EvalKit`](https://github.com/kaushal0494/AITutor-EvalKit) (MBZUAI, EACL 2026
  system demo, arXiv:2512.03688) scores tutor replies on the four **BEA-2025** dimensions — Mistake
  Identification, Mistake Location, Providing Guidance, Actionability. 🔴 **The paper states MIT; the
  repository carries NO licence payload at 24 filenames**, `main` ·
  `a71078456a90a7bb616f7c7e1de83f0bfbc44ab1`, **with a `P872` 200-control** (`README.md` = `200` at that
  same SHA, so the probe reached the tree). 🔵 **`P1014`: a paper's licence claim is not a grant. Cite
  the payload or shelve the row as read-only.**
- 🟢 **`P1010` applied to carried rows, and it moved two addresses.**
  `pykt-team/pykt-toolkit` **DRIFTED** off this shelf's pinned `77c3e90` to
  `4751688e3a10156248d82c4ef80714c5b210dd68` and **kept its grant** (MIT, 1 066 B — byte-identical to the
  earlier reading), **5 tags, counted for the first time**. `douglasrizzo/catsim` is **BSD-3-Clause**,
  1 514 B, **38 tags**, and 🔴 **its default ref is `dev`, not `master` or `main`** —
  `7e6caae84a8e7779422ba9338cfe2e2335185b28`. 🔵 **This shelf had never recorded a non-standard default
  branch; a `main`-assuming probe would have 404'd every filename and published a false negative.**

### 🔴 What pass 100 adds, and the first line is a correction of this shelf by this shelf

- 🔴 **`Gap 372` is DISCHARGED — by two rows this shelf has carried since passes 93 and 94.**
  Pass 99 declared the open-response scoring tier *"release-blocked, 0 of 3 released"* and wrote
  *"what is missing is not a licence, it is a release."* 🟢 **`wwrwbs/AI_AWE` has a release
  (`v0.1.0`, adapter artifact `http=200`) and `EducationalTestingService/rsmtool` has 33 of them
  (`v12.0.0`).** 🔵 **Neither had ever had its tags counted, because `tags` only became a measured
  column at pass 98.** 🟢 **`P1010`: re-measure a tier's EXISTING rows before declaring the tier
  blocked on a newly measured property.** 🔴 **A THIRD instance landed in the same pass** —
  `OpenOLAT/OpenOLAT`, on the platform page **since pass 35**, measures **542 tags**, the most of any
  repository in this KB. 🔵 **Three carried rows, three empty tag columns, one false gap: `P1010` is a
  property of every row tabled before pass 98.**
- 🟢 **`P1011`: in a regulated activity, search the INCUMBENT's open-source output before the AI
  community's.** The most release-engineered permissive tool in educational assessment is published
  by **ETS**, the house that scores TOEFL and the GRE. 🔴 **`P975` still binds** — the same
  organisation ships `factor_analyzer` under GPL-2.0.
- 🔴 **`Gap 390` OPENED — the PERSUADE 2.0 term is stated THREE ways, and `AI_AWE`'s own per-asset
  table is the third:** *"academic-use, attribution"*, which keeps NonCommercial in substance and
  **drops ShareAlike**. 🔵 **The adapter weights are distributed and were trained on an `NC-SA`
  corpus that is not. The code is yours; the weights are not.**
- 🟢 **`Gap 389` SETTLED, and pass 99's direction was inverted.** The **author's** own two
  repositories both state **`CC-BY-NC-SA-4.0`** from the payload; the `CC BY 4.0` claim is the
  **funder's** page, describing a smaller release (14 000 essays vs over 25 000).
  🟢 **`P1007`: a corpus's licence is stated by its AUTHOR's repository, never by its funder's or
  distributor's page.** 🟢 **`P1009`: a README saying "this *was* the repository" is a REDIRECT —
  resolve to the named successor before pinning.**
- 🟢 **The newer state of the art has no code, so the hardening target is unchanged.** A 2026 ACL
  paper names **GAPS** (Do et al., 2025) the newer SOTA cross-prompt trait scorer; 🔴 **GAPS has no
  repository and its authors record the GEC component's official code as absent.** 🟢 **`ProTACT`
  (BSD-3) stays the row worth hardening.**
- 🟡 **`P1008`: a `pyproject.toml` carrying `license = { file = "LICENSE" }` is a POINTER, not a
  second oracle** — it cannot corroborate `P979`.

### 🟢 What pass 99 adds, in one line each

- 🔴 **`P1006`: the LMS connector layer splits on licence, and the split decides which LMS the studio
  can serve permissively.** **Canvas** has a released permissive connector
  (`vishalsachdev/canvas-mcp`, **MIT**, **26 tags, `v1.14.0`**). **Moodle has no repo that is both**:
  its released connector is **AGPL-3.0 at `v0.1.7`** and self-describes as the connector *behind* a
  commercial product; its **MIT** alternative has **0 tags**. 🔵 **And the sting is regional — Moodle
  is the platform this KB has aimed at LATAM and the public sector for eight passes of patterns.**
- 🔴 **`Gap 372` stops being an absence and becomes a SIZE.** Three permissive open-response scorers
  were read at pinned SHAs — **MIT**, **Apache-2.0**, **BSD-3-Clause** — and 🔴 **0 of 3 has a single
  release tag**, in a pass that read three education repos carrying **26, 135 and 194** tags.
  🔵 **What is missing is not a licence. It is a release.**
- 🟡 **`P998` has a second shape, and it is the COST of the fix `P960` got right.**
  `Open-TutorAi/open-tutor-ai-CE` carries **all three BSD clauses verbatim**, 🔴 **zero occurrences of
  `"BSD"`**, and **no title block** — it opens `All rights reserved.` 🔵 **A title-block classifier,
  which is exactly what `P960` corrected this instrument into, returns UNCLASSIFIED on it.**
- 🟢 **`Gap 388` discharged as a CONDITION**: a true 404 body is **exactly 14 B** (`404: Not Found`)
  against pass 98's **1 523 B** HTML throttle. 🔴 **Unwired**, because the file that needs the three
  lines cannot be executed.
- 🟢 **`P872` false-discards again**, on the row pass 98 promoted: `seb-server`'s `README.md` witness
  is **404 / 14 B** while its `LICENSE` is **200 / 16 725 B** at the same pinned SHA.
- 🔴 **A hypothesis was formed, tested and REFUTED in-pass** — "scoring code is permissive, graded
  corpora are not" — and what replaced it is narrower: the corpus licence is **not uniform**, and for
  the largest corpus **the distributor and the originator state it differently** (`Gap 389`).
- 🟢 **All five of pass 98's pre-registered leads were run**, India and the EU procedure among them;
  the EU answer moved a **dated deadline inside 8 weeks** onto this KB's own tooling. See
  `intel/trends.md` `T4` and `intel/market.md`.

### 🟢 What pass 98 adds, in one line each

- 🔴 **`Gap 381` DISCHARGED with one grep, and it found a missing SALE rather than a missing row.**
  **1 056** slugs live in `compose/code/`, **159** on the shelf, **956** in code and on no shelf
  page — of which 🟢 **only 4 are carried by a purpose-built directory** instead of a sweep results
  table, and one of those is a parse artefact. 🔴 **The other three are the `UniTime` shape**, and the
  worst is `SafeExamBrowser/seb-server`: **three tested artefacts here since pass 43**, and this
  shelf names proctoring only as a regulatory exposure it offers nothing to address.
- 🟢 **The exam layer now reads end to end**: `UniTime` (timetabling, Apache-2.0, p96) +
  `seb-server` (supervision, **MPL-2.0**, p98) + `moodle-grading-mcp` (draft-only grading, MIT, p98),
  **all three with a tested gate already committed here.**
- 🟢 **Two new tiers, both from `P955`'s technique-named queries**: skills taxonomy (3 permissive
  rows) and credentialing (1 Apache + 1 MIT against 4 copyleft).
- 🔵 **`P1001`**: the permissive/copyleft seam found in scoring (`Gap 372`) **repeats exactly in
  credentialing** — permissive to validate and publish, copyleft to mint, 4 of 5. 🔵 **Stated as a
  falsifiable rule: the permissive side MEASURES, the copyleft side becomes the RECORD.**
- 🔴 **`P999`**: `skills-ml` carries the **same University of Chicago non-commercial template** that
  `Gap 385` hit on `dssg/student-early-warning` one pass ago. **The two highest-ROI institutional use
  cases in this industry share one licensing office.**
- 🟢 **The 6 shelf rows pass 97 counted as having no history trace are NAMED and 6 of 6 re-verify
  byte for byte** — which inverts `Gap 384`: a shelf row absent from the history is not unwitnessed,
  because the shelf row *is* the evidence record (`P996`).
- 🔴 **`Gap 387` OPENED: the 2026-10-06 reset dropped a verified row** and left a `compose/code/`
  cross-reference pointing at a page that no longer carries it.

### 🟢 What pass 97 adds, in one line each

- 🔴 **`Gap 384` — this shelf has been losing verified layers, and the loss is finally measured.**
  **1 259** slugs sit in the append-only history, **146** on the shelf pages, **1 119** in the
  history and on **no** shelf page — of which **528** carry a permissive grant and no rejection
  marker. 🔵 **1 119 is NOT the defect** (the history records rejected candidates by design)
  🔴 **but nothing distinguishes "measured and declined" from "measured and forgotten"**, and both
  known instances — `UniTime/unitime` (p96, in `compose/code/` since pass 42) and the **entire
  pronunciation layer** (this pass, verified since **pass 14**) — are the forgotten kind, **found by
  accident rather than by a sweep.**
- 🟢 **So the speech-and-pronunciation tier is PROMOTED, not discovered**, with two genuinely new
  rows and three corrections. 🟢 **`compose/code/p311-duplicate-alta-gate/` is what stopped this
  pass from republishing eight-pass-old rows as finds — the gate did its job.**
- 🟢 **`MontrealCorpusTools/Montreal-Forced-Aligner` (MIT, `v3.4.3`, 116 tags) is the mature anchor
  the layer never had** — **116 releases** where every other member has 2 or 0.
- 🔴 **`P994` — the corpus is ungranted while all seven tools around it are permissive.**
  `speechocean762`, the reference corpus of pronunciation scoring, serves **no licence payload**;
  so does `Phonos`, which this KB had counted *inside* a permissive layer. 🔵 **Priced as a line
  item: the pipeline ships, the calibration data does not.**
- 🔴 **`Gap 385` — there is no permissive open-source student early-warning system.** Six
  candidates, **five with no licence payload at all**, and the sixth non-OSI.
- 🔴 **`P990` — a file named `LICENSE` is not necessarily a grant.** The University of Chicago
  payload opens *"BY DOWNLOADING … YOU AGREE TO THE FOLLOWING TERMS OF USE"* with a **BSD-shaped
  permission sentence**, and excludes *"any service or part of selling a service"*. 🟢 **`lib` gets
  it right — and had no software fixture for that branch until this pass committed one.**
- 🟢 **`P989` — two slugs at the same HEAD SHA are one repository.** `CHINOBv/OpenPronounce` ≡
  `Halleck45/OpenPronounce` at **`74bc17ea406e6f`**. 🔵 **A fork test that needs no token and works
  through the only channel six passes of 403 left open.**
- 🟡 **`P991` — the title block can be DISPLACED.** `kaldi`'s Apache title hides at byte **2 531**
  behind an ownership notice, 4 of 4 clause headings present. 🟢 **`lib`'s 4 000 B window holds,
  with 1 469 B of margin — the bound is now measured, not assumed.**
- 🟡 **`P992` — `apache.org` serves 11 358 B, a repo serves 11 357 B**, and the byte is a leading
  newline. 🔴 **Diffing against the authority would call every pristine copy modified.**
- 🟢 **A second new tier, shelved with a hard guardrail: AI-text detection** — GLTR (Apache-2.0) and
  `Open-Detector` (MIT). 🔴 **For analysis and teaching only, never for a verdict that sanctions a
  student** — the field's own 2026 literature calls the task unsolved, and Annex III binds such a
  system from 2 Dec 2027.
- 🔴 **`github trending education AI {year}` returned its SEVENTH consecutive zero.** 🟢 **The
  retirement pass 96 called for stands**, and `P955` — name the TECHNIQUE — produced rows from three
  of four technique queries.

#### Pass 96 — carried below, unchanged

**Pass 96, 2026-10-10.** ⏱️ **Sixth pass of this date** (91: 2026-10-09 23:0x–00:00 UTC; 92: 00:4x–01:3x;
93: 01:4x–02:24; 94: 02:5x; 95: 03:4x; this one 04:4x–05:xx).

🔴 **The sandbox refuses to execute repository code for a FOURTH consecutive pass** — `grant-ladder-v4`'s
`ladder.sh` and its offline `test_ladder.sh` were both denied before starting (`[Code from External]`).
🟢 **So pass 96 wrote no classifier either** (`P237`). 🟢 **But the corrective duty `Gap 376` declared was
discharged in the one axis the open channel permits, and it produced the number four passes have been
missing: 122 of 127 published rows are provably un-drifted, 5 moved, and all 5 were re-read and kept their
grant.** `compose/code/p987-census-sha-currency/`.

🔵 **Marker convention, because six passes ran on one date.** A bare 🆕 is inherited from the pass that
added the row and was **not** re-flagged; **rows added by this pass are marked 🆕 p96.** **A `—` in the ★
column means not read this pass. It never means zero** — `api.github.com` returned **HTTP 403 for a fifth
consecutive pass**, so no star count on this page moved.

### 🟢 What pass 96 adds, in one line each

- 🟢 **`Gap 376` BOUNDED, not discharged.** 127 published `(slug, ref, sha7)` triples were asked one cheap
  question — *is the pinned SHA still the tip of the pinned ref?* — and **122 answered yes, 0 were
  unreachable, 0 refs had vanished.** 🔵 **A row still at its pinned SHA cannot have drifted, whatever else
  about it is unverified.** 🔴 **This is not 127 rows re-verified**, and must never be cited as if it were.
- 🔴 **`P987` — a 7-character SHA is a display format, not an address.**
  `raw.githubusercontent.com/.../ff82521694719bc1e282d046631bf0232c9d673e/README.md` → **200**;
  `.../ff82521/README.md` → **404**; *same object*. 🔴 **An unresolved abbreviation 404s all 24 filenames,
  which this shelf publishes as `no licence payload`.** 🟢 **`P872` caught it** — the control 404'd too, so
  the sweep was discarded. 🟢 **And the blast radius is measured: all 10 published negatives return a 200
  control at their published SHA. 0 of 10 are artefacts.**
- 🟢 **A new permissive tier, found by naming the TECHNIQUE (`P955`, fourth consecutive pass): rubric-based
  evaluation.** `OpenRS` (Apache-2.0), `OpenRubrics` (MIT), `rubricbench` (MIT), `awesome-rubric-rewards`
  (CC0). 🔵 **The instructional-alignment gap is restated as a WIRING gap, not an availability gap** — the
  same shape as `Gap 369`. Costed as `P96-A`.
- 🟢 **`UniTime/unitime` (Apache-2.0, pristine 11 357 B, `v4.9.152`) is a verified permissive platform this
  KB's own `compose/code/unitime-mcp-gate/` has used since pass 42 and no shelf page ever listed.**
  🔴 **Its `NOTICE` is 22 526 B** — Apache §4(d) makes that a shipping obligation.
- 🔴 **`Gap 377` is half wrong as written, and pass 96 refutes its own predecessor.** The Maven reader
  **already exists and is already wired** (`p289` → `p283::PARSERS`, by `P294`) — one import, not new code
  (`P237`). And **`build.gradle` is not a licence oracle**: Artemis declares none in 52 855 B.
- 🟢 **`P988` — in a `pom.xml` the `<url>` is the identifier and the `<name>` is prose.** 4 of 4 JVM
  platforms carry a canonical URL; **3 of 4 spell the name right** — `OpenOLAT` ships
  *"Apache 2.0 Open Source **L6icense**"*.
- 🆕 **`P984` — when a repo serves two licence files of very different sizes, the SMALL one has the facts.**
  Chamilo's unread 1 614 B `license.txt` yields **GPL-3.0-or-later** (this shelf publishes bare `GPL-3.0`),
  **12 holders in 5 countries with `BeezNest Latino SAC, Peru` FIRST** (`P800`), and a **third** licence
  location.
- 🟢 **`Gap 375`'s remainder discharged as UNMEASURABLE, with the mechanism** — and `P985` splits
  "no version" into three facts that price differently. 🔴 **The permissive-SIS candidate
  `academico-sis/academico` has 404 ★ and ZERO tags.**
- 🔴 **The binding high-risk regime for automated assessment is now APAC's, not EMEA's** — the EU deferred
  Annex III to **2 Dec 2027** while **Vietnam's Decision 33/2026/QD-TTg took effect 15 Aug 2026** and names
  automated assessment outright. New `T15` in `intel/trends.md`.
- 🔴 **`github trending education AI {year}` returned its SIXTH consecutive zero. Retire the query** — the
  ambiguity is in the phrase, not the index.

#### Pass 95 — carried below, unchanged

**Pass 95, 2026-10-10.** ⏱️ **Fifth pass of this date** (91: 2026-10-09 23:0x–00:00 UTC; 92: 00:4x–01:3x;
93: 01:4x–02:24; 94: 02:5x; this one 03:4x).

🔴 **The sandbox refuses to execute repository code for a THIRD consecutive pass** —
`grant-ladder-v4/ladder.sh --reach` denied before it started. 🟢 **So pass 95 wrote no classifier either**
(`P237`), ran the oracle map by hand and printed payloads instead of matching on them (`P970`).
**14 slugs resolved: 6 licence payload reads, 2 negative controls, 12 version reads, 4 release ladders, 2
registry-metadata reads.** Pass 92's 133-row census is **not** superseded (`P966`); every row not marked
🆕 p95 is carried at an earlier SHA and was **not** re-read this pass. **A `—` in the ★ column means not
read this pass. It never means zero** — and this pass it means **the GitHub API returned HTTP 403 for every
slug tried**, as it did for pass 94.

### 🟢 What pass 95 adds, in one line each

- 🔴 **`P980` — two unrelated projects, one name, incompatible grants.** A search summary said
  *"Otter-Autograder is GPL-3.0-or-later"*; the payload said BSD-3-Clause. **Both are true**:
  `otter-grader` 7.0.0 is [`ucbds-infra/otter-grader`](https://github.com/ucbds-infra/otter-grader)
  (**BSD-3**) and `Otter-Autograder` 0.15.9 is
  [`OtterDen-Lab/Autograder`](https://github.com/OtterDen-Lab/Autograder) (**GPL-3.0**) — different orgs,
  different code, same problem domain. 🟢 **A tool is identified by its REPOSITORY; a distribution name is
  a hint, never an identity.**
- 🟢 **A permissive production autograder, new to this shelf** —
  [`ucbds-infra/otter-grader`](https://github.com/ucbds-infra/otter-grader) (**BSD-3-Clause**, UC Berkeley,
  `v7.0.0`, Canvas + Gradescope). 🔵 **It does not close `Gap 372`** — it grades code against tests, not
  open responses. 🟢 **It closes a hole nobody had named**: the automated-feedback layer's only
  classroom-proven row was AGPL-3.0.
- 🔴 **`Gap 372` now has three MEASURED negatives instead of a shrug.** `GradeAid` is **CC BY-SA 4.0** (a
  content licence, carrying a ShareAlike term, applied to software); `RATASv1` and `emorynlp/llm-grading`
  have **no licence payload at all**. 🔴 **`P981`: "we publicly release our code" in a paper is not a
  grant** — and ungranted means all rights reserved.
- 🟢 **`eribean/girth_mcmc` discharged** — the lead pass 94 named and did not run. **MIT**, `0.6.0`, at
  **`LICENSE.txt`** while `LICENSE` is **404**. **Sixth row in the psychometric tier.**
- 🟢 **`P978` — the default branch reports the DEVELOPMENT version**, measured on four platforms rather
  than one. Sakai's root pom says `27-SNAPSHOT`; its newest tag is `25.2`. **Publish both, or publish a
  release nobody can install.**
- 🟢 **`P979` — the Maven `pom.xml` is a second licence oracle**, and Sakai's independently confirmed
  ECL-2.0 from a file read for an unrelated reason.
- 🟢 **Japan and Quebec both DISCHARGED**, each after two passes of returning nothing, and **neither by a
  new kind of query — by the method the previous pass had already written down.** See `intel/market.md`.
- 🟢 **Pakistan is a new jurisdiction and the FIRST higher-education mandate on this shelf** — an HEC
  notification making a 3-credit AI course compulsory in every UG and PG degree from session 2026.
- 🔴 **`Gap 376` — this KB's instrument has now been unrunnable longer than it was runnable.** The census
  denominator decays by ~12 hand-read rows per pass against a 133-row claim. **The first duty of the next
  pass that can execute code is corrective, not additive.**

#### Pass 94 — carried below, unchanged

**Pass 94, 2026-10-10.** ⏱️ **Fourth pass of this date** (91: 2026-10-09 23:0x–00:00 UTC; 92: 00:4x–01:3x;
93: 01:4x–02:24; this one 02:5x).

🔴 **The sandbox still will not execute repository code** — `grant-ladder-v4/ladder.sh` is refused before it
starts, for the second pass running. 🟢 **So pass 94 wrote no classifier either** (`P237`), ran the oracle
map by hand and **printed payload title blocks instead of matching on them** (`P970`). **12 slugs resolved:
9 licence payload reads at pinned SHAs, 1 negative control, 2 version-file reads.** Pass 92's 133-row census
is **not** superseded (`P966`); every row not marked 🆕 p94 is carried at an earlier SHA and was **not**
re-read this pass. **A `—` in the ★ column means not read this pass. It never means zero.**

### 🟢 What pass 94 adds, in one line each

- 🟢 **The scoring-*validation* layer, and it is permissive** — `rsmtool` (Apache-2.0, 2 916 commits) and
  `skll` (BSD-3) from **Educational Testing Service**, plus `NodeGrade` (MIT, LTI 1.1/1.3) for short
  answers. 🔵 **`Gap 372` is narrowed to the scorer**: the *evidence* a regulator asks for is open; the
  model is not. New tier below, costed as `P94-A`.
- 🔴 **One publisher, three grants** — ETS ships Apache-2.0, BSD-3 **and GPL-2.0** (`factor_analyzer`).
  `P975`: licence is a property of the repository, never of the publisher.
- 🟢 **`P974`: the clause probe, not the byte count, is the test for pass 93's `P971`.** `rsmtool` returns
  4 of 4 Apache clause headings; `AI_AWE` returns 0 of 4 — and an honest abridged copy (10 227 B) sits
  between them on size alone.
- 🟢 **`P972`/`P973`: platform versions are readable from the payload**, and the market leader is **5.3
  stable / 6.0dev alpha** while every blog read this pass said 5.2 — with `version.php` **not at the
  root**. `repos/foundations.md`, `verticals/solutions.md`, evidence in
  `compose/code/p972-platform-version-ladder/`.
- 🟢 **`Gap 370`'s failing path is resolved by hand**: `dados/LICENSE.md`, 676 B, HTTP 200 — and it carries
  a sovereignty clause no root licence could ([`repos/trending.md`](../repos/trending.md)).

#### Pass 93 — carried below, unchanged

**Pass 93, 2026-10-10.** ⏱️ **Third pass of this date** (91: 23:0x–00:00 UTC; 92: 00:4x–01:3x; this one
later the same day).

🔴 **This pass could not run the shelf's own instrument, and that is the first thing to say.**
`compose/code/grant-ladder-v4/ladder.sh` is committed and correct, but **this session's sandbox declines to
execute repository code.** 🔴 **The move that would have produced a clean-looking page — write a fresh
classifier — is the one `P237` forbids, and it is exactly what cost pass 91 two platform licences and one
client recommendation.** 🟢 **So pass 93 wrote no classifier.** It ran v4's oracle map by hand
(`git ls-remote --symref` → existence, ref, SHA; `raw.githubusercontent.com/<slug>/<SHA>/<name>` → payload)
and **printed each payload's title block instead of matching on it** — `P970`, stated in
`repos/foundations.md`.

**Consequence, stated plainly so no reader over-reads this page: 13 slugs were resolved this pass — 11
with a licence payload read at a pinned SHA, 1 negative, 1 invented control. Every other row on this page
is carried at its pass-92 SHA and was NOT re-read.** 🟢 Each new
row carries bytes, filename, ref and SHA so v4 can re-derive it mechanically next pass and contradict this
one on the record. **A `—` in the ★ column means not read this pass. It never means zero.**

🔵 **Marker convention, because three passes ran on one date.** A bare 🆕 is inherited from the pass that
added the row and was **not** re-flagged; **rows added by this pass are marked 🆕 p93.** Nothing on this
page silently changes its own provenance.

**Two-sided control.** 🟡 `moodle/moodle` → `COPYING.txt` **35 147 B** at `main` · `f205347` —
byte-identical to pass 92 **and at the same SHA**, so a re-read of the same object, **not** an independent
eleventh measurement; said rather than counted. 🟢 Invented slug → `ABSENT`. 🟢 And a free third-party
control: `OS4ED/openSIS-Classic` → 404 on `LICENSE`, `LICENSE.txt` **and** `LICENSE.md`, independently
reproducing a no-grant negative this KB already carried, with a different instrument.

### 🟢 What pass 93 adds, in one line each

- 🟢 **The psychometric layer** — BKT, IRT, CAT and spaced-repetition scheduling, **five permissive
  libraries whose seams their own READMEs name**. In `repos/foundations.md` Tier 2c; wired in `P93-A`.
- 🟢 **A national curriculum as verified open data** — Brazil's BNCC, MIT code + CC BY 4.0 data, with an
  MCP server. **The counter-example to the "frameworks are ungranted" shape** this shelf has carried for
  two passes. `repos/foundations.md` Tier 1b.
- 🟢 **A measured number for grounding**, which this KB has argued for 90 passes without one:
  **31.9 % → 0.2 %** hallucination. `intel/trends.md` `T11`.
- 🔴 **A blind spot in this KB's own licence reach**, proved on a real row and confirmed by a second,
  independent oracle. `P969` / `Gap 370`.

## The shelf

### Platform-grade AI (production, named deployments)

| agent | grant (payload · bytes · ref · SHA) | ★ | region | why it matters |
|---|---|---|---|---|
| [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) | **Apache-2.0** · 11 408 B · `main` · `6cf793b` | 41k | **APAC** (HKU Data Science lab) | The reference agent-native tutoring workspace. Real agent loop with `web_search`/`rag`/`exec`/`consult_subagent` tools, MCP servers, **multi-engine RAG** (LlamaIndex, PageIndex, GraphRAG, LightRAG) and a **three-layer file-backed memory** (L1 traces → L2 summaries → L3 synthesis). An `ask_user` tool lets a turn pause for clarification — the pedagogically correct primitive. |
| [`ls1intum/Artemis`](https://github.com/ls1intum/Artemis) | **MIT** · 1 091 B · `develop` · `760e2e1` | 816 | **EMEA** (TU München, AET group) | A production university platform, MIT, with three named LLM subsystems: **Iris** (virtual tutor giving hints and leading questions), **Athena** (feedback suggestion for text, modelling and programming exercises) and **Hyperion** (AI-assisted exercise authoring on Spring AI). All optional and config-gated. The best starting point in this industry for a closable deliverable. |
| [`Open-TutorAi/open-tutor-ai-CE`](https://github.com/Open-TutorAi/open-tutor-ai-CE) | **BSD** · 1 531 B · `main` · `196c547` | ~107 | 🔵 unplaced | Permissive, peer-reviewed (arXiv 2602.07176), Ollama and OpenAI-compatible, **local RAG over course materials**. The BSD grant makes it the cleanest base for a closed client deliverable. |
| [`Selleo/mentingo`](https://github.com/Selleo/mentingo) | **MIT** · 1 062 B · `main` · `2bca285` | 91 | **EMEA** (Selleo, Poland) | AI-native LMS; vendor documents an AI Mentor with Teacher / Mentor / Roleplay modes. 🟡 Open-core boundary still unverified (`Gap 362`) — stays out of every costed pattern. |
| [`satvik314/educhain`](https://github.com/satvik314/educhain) | **MIT** · 1 092 B · `main` · `38adb1e` | — | **APAC** (India) | Content and assessment generation from arbitrary sources; the long-standing generator row on this shelf. |

### Composable agents and protocol surface

| agent | grant (payload · bytes · ref · SHA) | ★ | region | why it matters |
|---|---|---|---|---|
| [`ankimcp/anki-mcp-server`](https://github.com/ankimcp/anki-mcp-server) | **MIT** · 1 074 B · `main` · `ed6774d` | 511 | 🔵 unplaced | Exposes Anki to any MCP client. **Spaced repetition becomes a tool call** — the cheapest way to give an agent durable retention mechanics instead of reimplementing them. |
| [`ArnaudGuiovanna/tutor-mcp`](https://github.com/ArnaudGuiovanna/tutor-mcp) | **MIT** · 1 073 B · `main` · `3708287` | 44 | 🔵 unplaced | Go MCP server that turns any LLM into an intelligent tutoring system. Model-agnostic by construction. |
| 🆕 [`kemalyy/edumints-scorm-mcp`](https://github.com/kemalyy/edumints-scorm-mcp) | **MIT** · 1 069 B · `main` · `bd14b95` | 8 | 🔵 unplaced | 🟢 **Self-hostable MCP server that assembles SCORM-compliant courses.** The interop spec becomes a tool call. |
| 🆕 [`giacomomaria81/scorm-mcp-server`](https://github.com/giacomomaria81/scorm-mcp-server) | **MIT** · 1 070 B · `main` · `fd5f110` | 6 | 🔵 unplaced | 🟢 Converts HTML exports **into** SCORM packages and **validates** SCORM zips. The second of its shape — see the note below. |
| 🆕 p93 [`bncc-dev/bncc-pacotes`](https://github.com/bncc-dev/bncc-pacotes) | 🟢 **split grant at the root** · `LICENSE` 1 299 B (index) · `main` · `ac9feb8` → **MIT** code (`packages/*/src/`, `python/bncc/*.py`, `mcp-worker/src/`, `scripts/`, tests) + **CC BY 4.0** data | 9 | 🟢 **LATAM** (Brazil — the licence payload is in Portuguese and its attribution clause names **MEC/CNE**) | 🟢 **A national curriculum behind an MCP server.** `@bncc/mcp` 0.2.0 exposes **7 tools** (`bncc_lookup`, `bncc_buscar`, `bncc_listar`, `bncc_decodificar`, `bncc_estatisticas`, `bncc_estrutura`, `bncc_progressao_ei`) over **1 721 verified BNCC learning objectives**, **with the dataset embedded so queries run locally** — no network call per lookup, which is the property that matters in a school. 🔵 **Curriculum alignment stops being a prompt-engineering problem and becomes a tool call against data with per-record provenance.** 🟡 Pre-1.0 (npm `@bncc/dados` 0.3.1, PyPI `bncc` 0.2.0). |
| 🆕 p93 [`dfdb76/bncc-mcp`](https://github.com/dfdb76/bncc-mcp) | **MIT** · `LICENSE` 1 218 B · `main` · `f94ca6a` | — | 🟡 **LATAM** (Brazil by subject matter — the payload's copyright line is a username, so the region is **not** `P800`-grade here and is labelled accordingly) | A **second, independent** MCP server over the BNCC skills, by a different author. 🔵 **n=2, so this is a shape rather than one project** — the same test pass 92 applied to MCP × SCORM. |
| [`towardsai/ai-tutor-app`](https://github.com/towardsai/ai-tutor-app) | **Apache-2.0** · 11 386 B · `main` · `1b7fbe0` | 31 | 🔵 unplaced | Agentic RAG tutor built on LangGraph — a readable reference for the orchestration layer rather than a product. |
| [`MysterionRise/adaptive-knowledge-graph`](https://github.com/MysterionRise/adaptive-knowledge-graph) | **MIT** · 1 094 B · `main` · `f88f69f` | 17 | 🔵 unplaced | Knowledge graph + local LLM + **Bayesian skill tracking**. One of very few rows carrying an explicit learner model rather than relying on prompt context. |
| 🆕 p99 [`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp) | 🟢 **MIT** · `LICENSE` 1 071 B · `main` · `b054b913603a206c677565bcbec128652cb9d398` | — | 🟢 **North America** (© 2025 **Vishal Sachdev**, University of Illinois — and Canvas's install base is overwhelmingly US higher ed) | 🟢 **The only RELEASED permissive LMS agent connector this KB has verified: 26 tags, `v1.14.0`, README 44 176 B.** MCP server over the Canvas LMS API — courses, assignments, submissions, feedback — so an agent reaches the gradebook through a maintained tool surface instead of bespoke REST glue. 🔵 **This is the row that makes a Canvas engagement permissive end to end.** |
| 🆕 p99 [`peancor/moodle-mcp-server`](https://github.com/peancor/moodle-mcp-server) | 🟢 **MIT** · `LICENSE` 1 064 B · `main` · `666f12222ed6cffc9051455eb4799bb2ac8608ce` | — | 🔵 unplaced (the payload's copyright line is a username — **not** `P800`-grade, labelled accordingly) | MCP server exposing Moodle courses, students, assignments and quizzes to an LLM, **including grades and feedback**, over Moodle Web Services. 🔴 **0 tags** — the permissive half of `P1006`'s split, and the unreleased half. 🟡 Use it as a fork base, not as a dependency. |
| 🆕 p99 [`Li-Evan/Bloom`](https://github.com/Li-Evan/Bloom) | 🟢 **MIT** · `LICENSE` 1 069 B · `main` · `b3918981bb34ef5d3090dc81cc5b184555ae3bd6` | — | 🔵 unplaced (© 2026 **Li Zhengping**; no institutional holder in the payload) | Self-hosted adaptive tutor — **FastAPI + React 19, Python 3.11+** — that reads how a learner actually learns and targets the next lesson from it, built explicitly on the **2-sigma** premise that 1-on-1 tutoring moves a median learner to the top few per cent. 🟡 **0 tags**, so treat it as a current reference implementation of the learner-model loop rather than a dependency. |
| 🆕 p99 [`shibing624/judger`](https://github.com/shibing624/judger) | 🟢 **Apache-2.0** · `LICENSE` 11 357 B *(pristine)* · `master` · `7c0817c02efa4a844937869d107ccb5afb14a972` | — | 🟡 **APAC** (by subject matter — it scores **Chinese** and English essays; the payload carries no holder line, so this is not `P800`-grade) | Java essay scorer with **self-trainable** scoring models and WEKA feature handling, zh + en. 🔴 **0 tags and a 177-byte README** — the most permissive grant in the scorer tier attached to the least documented repo in it. |
| 🆕 p99 [`doheejin/ProTACT`](https://github.com/doheejin/ProTACT) | 🟢 **BSD-3-Clause** · `LICENSE` 1 496 B · `main` · `403814318fe854dd6dc1959dbd005b9ab330e0c9` | — | 🟡 **APAC** (© 2023 **Heejin Do**, POSTECH) | Reference implementation of **ProTACT** — prompt- and trait-relation-aware **cross-prompt** essay *trait* scoring (ACL Findings 2023). 🔵 **Cross-prompt is the property a studio actually needs**: a scorer that transfers to a prompt it was not trained on. 🔴 **0 tags — research artefact, not a release.** |
| 🆕 p99 [`KamalEzzo/automated-essay-grading-system`](https://github.com/KamalEzzo/automated-essay-grading-system) | 🟢 **MIT** · `LICENSE` 1 363 B · `main` · `f47ac3a2bdb146e72e163f072904d504d69f603c` | — | 🔵 unplaced (© 2026 **Kamal Muhammad Kamal Abdul-Fattah**) | Fine-tuned **Gemma 2 9B-IT + LoRA** short-answer grader with a **4-criterion rubric** (clarity, terminology, coverage, accuracy) on a **0–5** scale, plus an ablation study and commercial-model benchmarks. 🔴 **Scoped to accounting / business education only, 0 tags** — valuable as a rubric-conditioning recipe, not as a general scorer. |

| 🆕 p103 [`mitodl/open-learning-ai-tutor`](https://github.com/mitodl/open-learning-ai-tutor) | 🟢 **MIT** · `LICENSE` 1 069 B · `main` · `d0ee63babac945ab533df1c1caa9c4f45605f0eb` | — | 🟡 **North America** by org (`mitodl` = MIT Open Learning); 🔴 the payload's holder line is an individual (© 2024 **Romain Puech**), so **not `P800`-grade on the holder** | 🟢 **A tutor library with 15 releases, top `v0.0.24`** — from the same institution whose 2-sigma premise every row in this tier cites. 🔴 **README is 214 B: this ships releases and almost no documentation**, so budget reading the code. 🔵 **Recovered by `Gap 394`'s census: it sat in an instrument's input worklist and on no page of this KB for the whole post-reset history.** |

🆕 🟢 **New shape, n=2 not n=1: MCP × SCORM.** Two independent MIT servers now put *content packaging* behind
the Model Context Protocol — one authoring packages, one validating them. 🔵 **This matters more than either
repo's star count.** Every education engagement eventually has to get content into a platform the client
already runs; until this pass that was always build-it-yourself glue. Both are tiny and both are MIT, so they
are cheap to fork and audit. See `P91-C`.

### 🟢 🆕 p103 The pedagogical-evaluation harness tier — permissive and RELEASED, which the rubric it must carry is not

🔵 **`Gap 393` (pass 102) left the BEA-2025 layer ungranted on both halves: the scorer
(`AITutor-EvalKit`) and the labels (`UnifyingAITutorEvaluation` / MRBench).** 🟢 **That holds. What
pass 103 adds is that the HARNESS those two were the only route to is a separate, permissive,
released purchase.**

| agent | grant (payload · bytes · ref · SHA) | ★ | region | why it matters |
|---|---|---|---|---|
| 🆕 p103 [`aiverify-foundation/moonshot`](https://github.com/aiverify-foundation/moonshot) | 🟢 **Apache-2.0** · `LICENSE.md` 11 347 B · `main` · `03e9344dc9fc949ae05b1f38580611fce36528ab` | — | 🟢 **APAC** (**AI Verify Foundation** — the body convened by Singapore's IMDA) | 🟢 **Benchmarking + red-teaming for any LLM-based system, 26 tags, top `0.7.6`.** Its named extension points are exactly the shape of a pedagogical rubric: **recipes** (custom *"input-target pairs"* datasets + prompt templates + an evaluation metric + **grading scales**), **cookbooks**, **connector endpoints**, **attack modules**, **context strategies**. 🔵 **A four-dimension rubric on a three-value scale is a recipe with a grading scale — so the rubric is a re-implementation and the harness is a purchase.** 🟡 Self-declared **beta**. |
| 🆕 p103 [`aiverify-foundation/moonshot-cicd`](https://github.com/aiverify-foundation/moonshot-cicd) | 🟢 **Apache-2.0** · `LICENSE` 11 357 B *(pristine)* · `main` · `996365ba61586c52040f632f8a9d7ff5c5573129` | — | 🟢 **APAC** | 🟢 **The pipeline limb: evaluation as a CI gate instead of a notebook, 6 tags.** 🔵 **This is the half that makes a pedagogical gate auditable** — a regulator asks when the check ran, not whether someone ran it. 🟡 Tags are `uat`-prefixed (top `uat0.2`): pre-GA, so pin the SHA. |

🔴 **What this tier does NOT buy: comparability.** 🔵 **The MRBench labels are the ungranted asset
(`Gap 393`), so a studio can run a defensible rubric on the client's own dialogues and cannot quote
an MRBench score as reproducible.** 🟢 **Cost the re-annotation; never the benchmark number.**

🟡 **And the provenance is the finding as much as the licence is.** 🔵 **The harness that makes
regulated pedagogical evaluation shippable comes from a REGULATOR-convened body in APAC, not from an
education vendor and not from EMEA — where the institutional output of the same period ships
releases with no grant at all (`Gap 395`).** 🟢 **`T27`.**

### 🔴 🆕 p99 `P1006` — the LMS connector tier, and the licence split that decides which LMS the studio can serve

🔵 **Six passes of patterns on this shelf assume an agent can reach the platform the client already
runs.** 🟢 **This pass measured the three repos that actually do that, and they do not agree on
licence.**

| slug | grant (payload · bytes · ref · full SHA) | tags / latest | verdict for the studio |
|---|---|---|---|
| [`vishalsachdev/canvas-mcp`](https://github.com/vishalsachdev/canvas-mcp) | 🟢 **MIT** · 1 071 B · `main` · `b054b913603a206c677565bcbec128652cb9d398` | 🟢 **26 / `v1.14.0`** | 🟢 **Use it.** Permissive *and* released. |
| [`csmediapro/moodle-mcp-server`](https://github.com/csmediapro/moodle-mcp-server) | 🔴 **AGPL-3.0** · 34 523 B · `main` · `5a194a53cc399155bdc5e49737709f43f9a16406` | 🟡 **7 / `v0.1.7`** | 🔴 **Declined.** Network copyleft on a server the client reaches over a network. |
| [`peancor/moodle-mcp-server`](https://github.com/peancor/moodle-mcp-server) | 🟢 **MIT** · 1 064 B · `main` · `666f12222ed6cffc9051455eb4799bb2ac8608ce` | 🔴 **0** | 🟡 **Fork base only.** Permissive, unreleased. |

🔴 **So the asymmetry is the finding, not any single row: Canvas has a connector that is permissive
AND released; Moodle has one of each and neither is both.**

🔵 **And this is region-bearing rather than a licence curiosity.** Moodle is the platform this KB has
pointed at **LATAM** and the public sector across eight passes of patterns — because it is what
ministries and public universities actually run — and it is precisely the platform whose agent
connector forces a choice between **AGPL-3.0** and **untagged**. 🟢 **A Canvas engagement
(overwhelmingly North America higher ed) inherits a permissive, released connector at `v1.14.0`;**
🔴 **a Moodle engagement inherits a fork.**

🔴 **`P975` on top of it:** the third-party directory that surfaced the AGPL server first described it
only as *"open-source"*. 🟢 **The payload says AGPL-3.0 at 34 523 B.** 🔴 **And the error ran in the
expensive direction** — the same direction as `P997`'s Apache-for-MPL slip two passes ago: a
permissive-sounding label over the one family that can reach a client's own code.

🟢 **What to do with the Moodle half, concretely:** `peancor/moodle-mcp-server` is **1 064 B of MIT
over Moodle Web Services** and small enough to audit in an afternoon. 🔵 **Fork it, pin it, and treat
the AGPL server as a specification to read rather than code to link** — which is lawful and is the
same manoeuvre `sebserver-mcp-gate` already documents for MPL (`§1.10(a)`, per-file copyleft).

### 🟢 🆕 p100 `Gap 372` — **DISCHARGED**, and the gap was in this shelf's back catalogue, not in the supply

🔵 **Pass 99 measured `0 of 3` tagged across the three scorer rows it had just added and concluded:
*"What is missing is not a licence. It is a release."*** 🔴 **Two rows already on this shelf refute
that, and neither had ever had its tags counted — `tags` only became a measured column at pass 98.**

| row (pass that tabled it) | what that pass recorded | 🟢 what pass 100 measured |
|---|---|---|
| 🆕 p93 [`wwrwbs/AI_AWE`](https://github.com/wwrwbs/AI_AWE) (**ArguLens**) | *"a 2★ research repo … shelve it as a reference for the architecture, never as a dependency"* | 🟢 **1 tag — `v0.1.0` · `bfb34af069e31adabfcd2e7a51acb1605cb4d2a7`**; `main` · `41ae3bd4dd9e891bf46dd4834644ca143dbd36df`; **adapter weights published as a release artifact, `http=200`** |
| 🆕 p94 [`EducationalTestingService/rsmtool`](https://github.com/EducationalTestingService/rsmtool) | *"2 916 commits"*, Apache-2.0, 11 358 B | 🟢 **33 tags · `v12.0.0`**; `main` · `a844f71614712f81177b5731dbb17b3e018dcc85`; conda `anaconda.org/ets`; **GitLab + Azure CI**; `requires-python >= 3.10` |

🟢 **`P1010` — when a pass declares a tier blocked on a property, re-measure the tier's EXISTING rows
on that property before declaring the gap.** 🔵 **A gap asserted on a column never populated for
carried rows is a gap in the measurement.** 🔴 **This one survived a full pass and was written into
three files.** 🟢 **The discharge cost one `git ls-remote --tags` per slug.**

#### 🟢 What `AI_AWE` actually is, now that its README has been read as well as its LICENSE

🔵 Pass 93 read the **1 865 B** `LICENSE` and the name/claim divergence. 🟢 **This pass read the
README (5 931 B), and it describes a runnable system rather than a library:** discourse-move
classifier (Qwen2.5-7B-Instruct + LoRA, *claim / data / counterclaim / rebuttal*) **+** LightGBM
scorer over **31 linguistic features** **+** feedback generator; **Gradio UI** with single-essay and
batch modes and downloadable per-essay breakdowns (`result.json`, `sentence_labels.csv`,
`summary.csv`); selectable **vLLM** or **4-bit HuggingFace** backends; and a test suite that
**skips its service tests when no backend is reachable, so it runs offline.**

🟢 **So the purchase changes shape for the third time, and is small for the first time:** not *"find a
scorer"* (p95), not *"harden one of three paper artefacts to a release"* (p99), but 🟢 **"stand up an
Apache-2.0 system that already runs, and retrain its adapter on a corpus you may use commercially."**
🟢 **The repository ships the seam for exactly that:**
`qwen_move_classifier/data/prepare_persuade.py --in /path/to/licensed/persuade_export.json`.
🔵 **Costed as `P100-A` in `compose/patterns.md`.**

🟡 **Pass 93's `P971` flag STANDS and nothing above softens it**: this row's `LICENSE` is the Apache
**header notice**, **1 865 B**, **0 of 4 clause headings** — Apache-2.0 **by reference**. 🔴 **A
procurement that requires the licence text in the bundle must add it by hand.** 🟢 Contrast
`rsmtool`'s **11 358 B**, the full canonical length.

🔴 **And its own responsible-use section is the line to quote to a client, not to bury**: PERSUADE 2.0
is *US middle-school argumentative essays*, the tool is *"intended for research and assistive use,
not for high-stakes automated decisions without human oversight"*, and 🔵 **under Annex III that
sentence is not a disclaimer — it is the deployment condition.**

#### 🔴 🆕 p100 `Gap 390` — the corpus term is stated THREE ways, and the third drops ShareAlike

🟢 `AI_AWE`'s README carries a **per-asset licensing table**, which is better due-diligence
engineering than most commercial packs:

| asset, as the repo itself declares it | licence it states | shipped in the repo? |
|---|---|---|
| source code / adapter config / scorer | 🟡 **Apache-2.0** (by reference, `P971`) | 🟢 yes |
| `adapter_model.safetensors` | release artifact | 🟢 **yes — `v0.1.0`, `http=200`** |
| TextComplexityToolkit (TAALED / QuanSyn) | 🟢 **MIT** | 🟢 vendored, LICENSE kept |
| Qwen2.5-7B-Instruct base | 🟢 **Apache-2.0** | 🔴 no — fetch from HF |
| **PERSUADE 2.0 corpus** | 🔴 **"academic-use, attribution"** | 🔴 no — run `prepare_persuade.py` |
| spaCy `en_core_web_sm` | 🟢 MIT/CC | 🔴 no |

🔴 **"Academic-use, attribution" is neither reading already on the table**: it keeps NonCommercial in
substance and **silently drops ShareAlike**. 🔵 **`Gap 390`, narrow and checkable: the adapter is
DISTRIBUTED and was fine-tuned on an `NC-SA` corpus that is NOT — is the published adapter a
derivative work of the corpus?** 🟢 **The KB does not need the answer to sell around it**, because
the retraining seam exists. 🔴 **But it must never ship the released adapter to a commercial client
while the question is open.**

#### 🟢 🆕 p100 `Gap 389` SETTLED — and pass 99 had the conflict's direction backwards

| slug | ref · full SHA | payload | licence stated in it |
|---|---|---|---|
| [`scrosseye/persuade_corpus_2.0`](https://github.com/scrosseye/persuade_corpus_2.0) | `main` · `67d182ac88ea4a4dda736de859cfdb0bc360ee9b` | `README.md` **2 159 B**, line 29 | 🔴 **CC-BY-NC-SA-4.0** |
| [`scrosseye/PERSUADE_corpus`](https://github.com/scrosseye/PERSUADE_corpus) | `main` · `de78d7a5d22c333d24d489b95dd744a5aa490e5f` | `README.md` **3 557 B**, line 51 | 🔴 **CC-BY-NC-SA-4.0** |

🟢 **`scrosseye` is Scott Crossley, the corpus's own first author.** 🔵 **The `CC BY 4.0` claim is
the Learning Agency Lab's — the FUNDER's page — and it describes 14 000 essays where the author's
repositories describe over 25 000.** 🟢 **Not two readings of one release: a page describing a
different, smaller one.** 🔴 **The operative term is `NC-SA`**, and nothing permissive should assume
`BY`. 🔴 **Neither repo has a licence FILE** (`LICENSE`, `.md`, `.txt` → three `404`s): `P969`'s
shape, a data licence living in prose.

🟢 **Both pages are in the refused set and the gap closed anyway**, via the route pass 99
pre-registered as *"the cheap route"*. 🔵 **`P1007`: a corpus's licence is stated by its AUTHOR's
repository, never by its funder's or distributor's page.** 🔵 **`P1009`: a README saying "this *was*
the repository" is a REDIRECT — resolve to the named successor before pinning, or be right about the
licence by luck and wrong about the release.**

#### 🟢 The hardening target is unchanged, and now for a measured reason

🟢 [`doheejin/ProTACT`](https://github.com/doheejin/ProTACT) re-read at a full address —
**BSD-3-Clause**, `LICENSE` **1 496 B** (*"Copyright (c) 2023, Heejin Do"*), `main` ·
`403814318fe854dd6dc1959dbd005b9ab330e0c9`, 🔴 **0 tags.**
🟢 **A 2026 ACL paper names GAPS (Do et al., 2025) the newer SOTA cross-prompt trait scorer.**
🔴 **GAPS has no repository, and its own authors record the GEC component's official code as absent,
substituting a third-party `GEC-T5`.** 🔵 **The newest *published* trait scorer is less deliverable
than the 2023 one, so `ProTACT` stays the row worth hardening** — its cross-prompt property is what a
client's unseen assignment needs on day one.
🟡 Snippet-only, no primary read: ProTACT ≈ **0.592** mean QWK (prompt 7 weakest, 0.446); ArguLens
reports **82.6 %** / **0.727** macro-F1 and **0.813** mean QWK — 🔴 **which its authors call a
component-level diagnostic, not an end-to-end result.**

🔴 **One clean negative:** [`Chunngai/aes-papers`](https://github.com/Chunngai/aes-papers) — `master` ·
`87c9a818784314c7181b62a5fe359bfd7eb70116`, **five root licence filenames probed, five `404`. No
grant → reading list, never a dependency.**

### 🔴 🆕 p99 `Gap 372` — the scorer tier was never missing. It is UNRELEASED, and that is a different purchase

🔵 **Four passes carried `Gap 372` as "no permissive production-grade corrector for open response".**
🟢 **Three permissive ones were read this pass, at pinned full SHAs, and the tier rows are above.**

| slug | grant | tags | what it is, and what it is not |
|---|---|---|---|
| `KamalEzzo/automated-essay-grading-system` | 🟢 **MIT** | 🔴 **0** | Gemma 2 9B-IT + LoRA, 4-criterion rubric, 0–5 — 🔴 **accounting only** |
| `shibing624/judger` | 🟢 **Apache-2.0** | 🔴 **0** | Java/WEKA, zh + en, self-trainable — 🔴 **177-byte README** |
| `doheejin/ProTACT` | 🟢 **BSD-3-Clause** | 🔴 **0** | **cross-prompt** trait scoring, ACL Findings 2023 — 🔴 **paper artefact** |

🟢 **The control is in this same pass, same industry, same instrument:** `canvas-mcp` **26 tags /
`v1.14.0`**, `HKUDS/DeepTutor` **135 tags**, `SafeExamBrowser/seb-server` **194 tags**.
🔵 **So the tier is not licence-blocked. It is release-blocked** — and that changes what the studio
sells: 🟢 **not "find a scorer" but "harden one of three permissive scorers to a release", with
`ProTACT`'s cross-prompt property as the one worth hardening** because transfer to an unseen prompt
is the property a client's new assignment needs on day one.

🔴 **And the half a regulator asks for is still the half that exists** (`P94`'s scoring-validation
tier): the permissive supply is strongest at **validating** a score and weakest at **producing** one.

🔴 **The corpus, not the code, is now the open term.** The graded corpora this pass located do **not**
share a licence — one **CC-BY-NC-SA-4.0** read from its payload
([`anaistack/cefr-asag-corpus`](https://github.com/anaistack/cefr-asag-corpus), `LICENSE.txt`
**20 863 B**, `main` · `7f3b75afe516bf6e309cbacfc1de0263ff04bb72`), one reported **CC BY**
(ASAP 2.0), and one 🔴 **stated differently by its distributor and its originator** (PERSUADE 2.0 —
`Gap 389`). 🔵 **Price the corpus licence as a procurement term, and never inherit it from a
distributor's listing.**

### 🆕 The checker tier — and the gap this shelf declared for five passes is now **half closed**

🔴 **What the shelf said, in three files:** *"a targeted search for AI accessibility/alignment checkers in
education returned nothing usable"*, and *"the only accessibility checker found is `ucfopen/UDOIT` — GPL-3.0,
and not AI-driven."* 🟢 **The accessibility half of that is now FALSE.** Permissive, AI-driven WCAG checkers
exist, were found on the first targeted query, and verified from the payload:

| checker | grant (payload · bytes · ref · SHA) | region | scope |
|---|---|---|---|
| 🆕 [`tomaszboloz/WCAG-Accessibility-Skills`](https://github.com/tomaszboloz/WCAG-Accessibility-Skills) | **MIT** · 1 070 B · `main` · `1b095c2` | 🔵 unplaced | 🟢 **The best row in this tier.** WCAG 2.1/2.2 audit CLI **and** agent skill, with CI regression gates — and an **explicit manual-review boundary**: it states it cannot declare legal conformance from an automated pass. 🔵 **That refusal is the feature.** A checker that overclaims is a liability in a Section 508 dispute. |
| 🆕 [`Community-Access/accessibility-agents`](https://github.com/Community-Access/accessibility-agents) | **MIT** · 1 069 B · `main` · `decf6ba` | 🔵 unplaced | Eleven WCAG 2.2 AA review agents for Claude Code and Copilot. Aimed at stopping AI coding tools **generating** inaccessible output — the preventive position rather than the audit one. |
| 🆕 [`9mtm/WCAG-Checker`](https://github.com/9mtm/WCAG-Checker) | **MIT** · 4 219 B · `main` · `d34decd` | 🟡 **EMEA** (publisher is an Austrian/German GmbH per the payload's copyright line) | Websites **and PDF files** — PDF matters, because course handouts are where institutional accessibility exposure actually lives. |
| 🆕 [`nsip/curriculum-mapper`](https://github.com/nsip/curriculum-mapper) | **Apache-2.0** · 11 357 B · `master` · `2b405d5` | 🟢 **APAC** (NSIP — National Schools Interoperability Program, Australia) | ML mapping **between curricula**. 🔴 **Archived and read-only**, and keyword-based rather than semantic. Read it as a spec for the problem, not a dependency. |
| 🆕 [`learning-commons-org/evaluators`](https://github.com/learning-commons-org/evaluators) | 🟡 **four-way split grant** · `LICENSE.md` 1 615 B · `main` · `59d2396` | 🔵 unplaced | LLM-as-a-judge scoring of generated text **against research-backed educational rubrics**, with expert-annotated corpora. 🔴 **Read the licence note below before costing it.** |
| [`learning-commons-org/knowledge-graph`](https://github.com/learning-commons-org/knowledge-graph) | 🔴 **`MULTI-GRANT-FRAMEWORK`** · `LICENSE.md` 5 789 B · `main` · `65701e9` | 🔵 unplaced | A data layer for educational AI, tagged to academic standards. 🆕 🔴 **Its `LICENSE.md` grants NOTHING — it is a licensing *framework* document** (`P965`). It names *"Code … MIT"* and *"Open … CC BY 4.0 … CC0"*, and then the clause that governs: **"Gated — Not covered by an open license. Access requires Data Provider approval"**, and **"Gated content isn't yours to redistribute by default."** 🔴 **A classifier reading it returned `CC0-1.0` — the most permissive family the document merely mentions — for a payload whose operative term is the opposite.** Resolve the grant **per dataset and per download** in the catalogue before costing anything. |

🔴 **The licence structure in this tier is the finding, not the repo list.** `learning-commons-org/evaluators`
ships **one** `LICENSE.md` granting **four different things**: code **MIT**, prompts and settings
**CC-BY-4.0**, and the Annotated CLEAR Corpus and Annotated PERSUADE 2.0 Corpus **CC-BY-NC-SA-4.0**.
🔴 **The non-commercial clause sits on the corpora — which are the part that makes it an evidence-backed
evaluator rather than a prompt.** 🔵 **So the question in the checker tier is not "is it permissive" but
"is the permissive part the valuable part".** Here it is not. The code and prompts are usable in a paid
deliverable; the annotated corpora are not, and a studio must bring or buy its own.

🔴 **Four checker candidates have NO grant at all** (24 filenames each) and one of them is published as MIT:

| row | what is claimed | what the payload says |
|---|---|---|
| [`qed42/ai-accessibility-checker`](https://github.com/qed42/ai-accessibility-checker) | 🔴 a search summary states plainly *"It is MIT-licensed"* | 🔴 **No licence payload in 24 filenames** · `main` · `5716afc`. The most capable-looking row in the tier — Python CLI **plus** GitHub Action, WCAG 2.0–2.2 A/AA/AAA — and **unusable**. |
| [`albertomf1979/wcag-accessibility-agent`](https://github.com/albertomf1979/wcag-accessibility-agent) | WCAG 2.1 agent with CLI and PDF/DOCX export | 🔴 **No licence payload in 24 filenames** · `main` · `472c6bb` |
| [`Zion-support/curriculum-alignment-checker`](https://github.com/Zion-support/curriculum-alignment-checker) | checks materials against standards, flags gaps | 🔴 **No licence payload in 24 filenames** · `main` · `c148b67`. Self-describes as batch-generated app-network content. |
| [`lovejzzz/CourseMapper`](https://github.com/lovejzzz/CourseMapper) | course mapping with browser-local AI | 🔴 **No licence payload in 24 filenames** · `main` · `63d8172`. Its own README logs source-attribution and answer-quality failures. |

🔵 **What is still genuinely missing, stated narrowly.** 🟢 The **accessibility** checker gap is closed —
permissive, AI-driven, and three independent rows. 🔴 **The instructional-alignment checker gap stands.**
Nothing found audits whether content actually meets a learning outcome under a permissive grant with usable
evidence: `nsip/curriculum-mapper` is archived and keyword-based, `evaluators`' corpora are NC, and the two
alignment-named repos carry no grant. **That is the build, and it is now a sharper specification than
"checkers barely exist".**

### 🟢 🆕 p96 The rubric tier — the instructional-alignment gap is a **wiring** gap, not an availability gap

🔴 **What this shelf has said for five passes:** *"Nothing found audits whether content actually meets a
learning outcome under a permissive grant with usable evidence. That is the build."* 🟢 **That sentence is
still true of education repositories and FALSE of the technique**, and the correction arrived on the first
query that named **rubrics** instead of education — `P955` holding for a **fourth consecutive pass**, now
on a gap that has survived five.

| repo | grant (payload · bytes · ref · SHA-40 prefix) | role | region |
|---|---|---|---|
| 🆕 p96 [`Qwen-Applications/OpenRS`](https://github.com/Qwen-Applications/OpenRS) | 🟢 **Apache-2.0** · 10 770 B · `master` · `4c7f22b5707536` | 🟢 **The judge.** *Open Rubric System* — LLM-as-a-Judge that replaces a reward model with **adaptive, query-type-specific rubrics**: 50+ rubric sets, criteria **weighted critical / core / important / highlight**, bi-directional A/B-swap debiasing, and **interpretable verdicts**. 🔵 **Weighted tiered criteria plus a written verdict is structurally what an Annex III explanation is.** | 🟡 **APAC** (Qwen application org — publisher country not established from the repo, so not `P800`-grade) |
| 🆕 p96 [`wanghaoyu0408/OpenRubrics`](https://github.com/wanghaoyu0408/OpenRubrics) | 🟢 **MIT** · 1 067 B · `main` · `1a40c14cb7827ae` | 🟢 **The generator.** Reference implementation of the OpenRubric family — **synthetic rubric generation at scale** for reward modelling and alignment (**ACL 2026 long paper**). 🔵 *Given an instruction, produce the rubric.* | 🔵 unplaced |
| 🆕 p96 [`planepig/rubricbench`](https://github.com/planepig/rubricbench) | 🟢 **MIT** · 1 067 B · `main` · `07daecc72ac159` | 🟢 **The validator, and the piece this KB has needed most.** **1 147 pairwise comparisons** with **expert-annotated atomic rubrics derived strictly from the instruction**, spanning Chat, Instruction-Following, STEM, Coding and Safety — and it scores **the intermediate reasoning as well as the final verdict**. 🔵 **This is how you answer "does our rubric judge agree with a human marker", which is the question an appeal turns on.** | 🔵 unplaced |
| 🆕 p96 [`chrisliu298/awesome-rubric-rewards`](https://github.com/chrisliu298/awesome-rubric-rewards) | 🟡 **CC0-1.0** · 7 048 B · `main` · `4897f496d7868e` | The curated index of rubrics, checklists, criteria sets and scoring guides used to score, rank, verify, filter or train generative models. 🟡 **A list, not a dependency** — entry point only. | 🔵 unplaced |

🟢 **`P974`'s positive class gets a second instance, and this time the missing section is named.**
`OpenRS`'s `LICENSE` is **10 770 B** against pristine Apache-2.0's **11 357 B** — a 587-byte shortfall that
on size alone looks like a modified grant. **The clause probe returns 4 of 4** —
`Grant of Copyright License`, `Grant of Patent License`, `Redistribution`, `Disclaimer of Warranty` — with
**`APPENDIX` ABSENT**. 🔵 **An honest abridgement that dropped only the "how to apply this licence"
boilerplate.** 🟢 **Byte count is the smell; the clause probe is the test.**

#### 🔵 Why this reframes the gap instead of closing it

🔴 **Not one of these four repos knows what a learning outcome is.** They bind a rubric to an *instruction*.
**The education-specific step — binding a rubric to a published curriculum standard, with per-record
provenance — is what nothing found in five passes does.**

🟢 **And this shelf already holds every other piece, permissively, from three unrelated publishers:**

| piece | row already on this shelf | grant |
|---|---|---|
| the **standards data**, with provenance | [`bncc-dev/bncc-pacotes`](https://github.com/bncc-dev/bncc-pacotes) — **1 721 verified BNCC objectives** behind **7 MCP tools**, dataset embedded so lookups run locally | 🟢 **MIT** code + **CC BY 4.0** data |
| the **education rubrics + judge code** | [`learning-commons-org/evaluators`](https://github.com/learning-commons-org/evaluators) — LLM-as-a-judge against research-backed educational rubrics | 🟢 **MIT** code · 🟢 CC-BY-4.0 prompts · 🔴 **corpora CC-BY-NC-SA-4.0** |
| the **rubric judge and its validator** | 🆕 `OpenRS` + `rubricbench` | 🟢 Apache-2.0 / MIT |
| the **psychometric defence** | `catsim` (BSD-3), `pyBKT` / `py-irt` / `girth` / `girth_mcmc` (MIT) | 🟢 permissive |

🔵 **Four permissive layers of one system, never wired together.** 🟢 **`Gap 379` is that wiring, stated
narrowly enough to be built:** *take a curriculum objective from an MCP standards server, generate a rubric
for it with `OpenRubrics`, judge candidate content against it with `OpenRS`, and calibrate the judge against
human markers with `rubricbench`.* **Costed as `P96-A` in `compose/patterns.md`.**

🔴 **And the honest caveat on `evaluators`, unchanged and re-confirmed at a new SHA this pass:** its
annotated CLEAR and PERSUADE 2.0 corpora are **non-commercial**, and they are the part that makes it
evidence-backed rather than a prompt. **A paid deliverable can use the code and the prompts; it must bring
or buy its own annotated corpus.** 🟢 **`rubricbench`'s 1 147 expert-annotated comparisons are MIT** — 🔵
**which is the first permissive annotated comparison set this shelf has found, even though it is not
education-domain.**

### 🆕 The AI-literacy tier — because literacy is now a statutory duty, not a nice-to-have

🟢 **Four jurisdictions now *mandate* AI instruction rather than regulate AI systems** (see `intel/trends.md`
`T7`): China's MoE (≥8 h/year from age six), Singapore's MoE (March 2026), India's CBSE (Classes 3–8 from
2026-27) and the EU AI Act's **Article 4 staff AI-literacy duty — which is already in force and was NOT
deferred to December 2027 with the high-risk obligations.** Someone has to write, localise and assess that
curriculum. These are the permissive starting points, all verified from the payload this pass:

| curriculum repo | grant (payload · bytes · ref · SHA) | ★ | note |
|---|---|---|---|
| 🆕 [`microsoft/ai-agents-for-beginners`](https://github.com/microsoft/ai-agents-for-beginners) | **MIT** · 1 141 B · `main` · `ff2ba66` | ~67k (search-reported) | Twelve lessons on building AI agents. The largest permissive AI curriculum found; vendor-backed and translated. |
| 🆕 [`rohitg00/ai-engineering-from-scratch`](https://github.com/rohitg00/ai-engineering-from-scratch) | **MIT** · 1 070 B · `main` · `b6a7a17` | — | 🟢 **Reached #1 on GitHub Trending on 24 May 2026** (Trendshift). Build-it-yourself AI engineering. |
| 🆕 [`pguso/agents-from-scratch`](https://github.com/pguso/agents-from-scratch) | **MIT** · 1 091 B · `main` · `da3f9df` | ~796 (search-reported) | Agents from first principles **against a local LLM** — the right shape where student data cannot leave the building. |
| 🆕 [`cccareers/open-source-curriculum`](https://github.com/cccareers/open-source-curriculum) | 🔴 **CC-BY-NC-SA-4.0** · `LICENSE.md` 1 891 B · `main` · `dd01b98` | — | 🔴 **Non-commercial.** Usable as reference, **not** in a paid deliverable. 🔵 Pass 91’s instrument misfired on this row (it recorded `Unlicense/PD`, and its committed TSV still does); re-derived correctly this pass — see `compose/code/grant-ladder-v4/README.md` (`P954`, `P966`). |
| [`lukeslp/awesome-accessibility`](https://github.com/lukeslp/awesome-accessibility) | **CC0-1.0** · 6 464 B · `main` · `d146ae6` | — | A list, not software, and public-domain dedicated — so quotable without attribution obligations. 🆕 🔵 **This row is also the payload that proved the shared classifier's CC0 branch was unreachable for canonical CC0 text** (`P962`) — pass 91's own results file recorded it as `OTHER/unclassified` while the shelf published `CC0-1.0`, found by hand. |
| 🆕 [`ai-builders-foundation/ai-builders-curriculum`](https://github.com/ai-builders-foundation/ai-builders-curriculum) | **MIT** · 1 079 B · `main` · `fe2da3d` | — | 🟢 **Vendor-neutral, 501(c)(3)-backed**, full-stack AI application curriculum with hackathon starter kits. The cleanest governance story in this tier — a foundation rather than a vendor, which matters for a public-sector procurement. 🔴 Adult/developer audience, like every other row here. |
| 🆕 [`fborrasumh/tutoria`](https://github.com/fborrasumh/tutoria) | **MIT** · 1 120 B · `main` · `65b2903` | — | 🟢 **EMEA** (Universidad Miguel Hernández de Elche, Spain — from the payload's copyright line). **Evidence-based tutor where the teacher VALIDATES the lesson before the student sees it**, then hints → diagnosis → check → review. 🔵 **The teacher-in-the-loop gate is the compliance-relevant primitive**: under the EU AI Act's Annex III, assessing learning outcomes is high-risk and needs human oversight, and this is that oversight expressed as a product step rather than a policy document. |

🔵 **Why this tier belongs on an *agents* shelf.** A mandated curriculum is the one education deliverable with
a legal deadline attached and no incumbent product, and the content layer is where a studio adds most value per
hour. 🔴 **The licence split matters sharply here**: curriculum is content, and content is where NC clauses
cluster. Three of the eight rows above are CC, and one of those forbids commercial use.

### 🔴 The framework every mandate points at is **ungranted** — and primary school is still empty

🔴 **`Gap 367` (no permissive AI curriculum for primary) STANDS, unchanged from pass 92.** Not re-queried
this pass; carried verbatim rather than re-asserted on no new evidence. A K-5-specific query returned
**no GitHub repository at all**; every permissive curriculum repo on this shelf is written for adult
developers. 🟢 The named non-GitHub alternative stands too: **MIT Day of AI** (`dayofai.org`,
**CC-licensed** — K-2 *"AI Foundations for Early Childhood"*, grades 3-5 *"How We Teach Machines"*) plus
Code.org's AI modules, both organised around the **AI4K12 Five Big Ideas** (Perception · Representation
and Reasoning · Learning · Natural Interaction · Societal Impact).

🔴 **And the finding that matters for a deliverable, also carried:** AI4K12 is the framework the K-12
guidance and India's CBSE curriculum align to, jointly sponsored by **AAAI and CSTA** — and its
repository, [`touretzkyds/ai4k12`](https://github.com/touretzkyds/ai4k12), carries **no licence payload in
24 filenames** (`master` · `727b8bb`).

### 🟢 🆕 p93 But the *shape* of that gap is now refuted — by Brazil, and with better engineering than the framework it refutes

🔴 **What this shelf generalised from `ai4k12` and `learning-commons-org/knowledge-graph` was a rule:**
*reference frameworks and curriculum standards are authored by bodies that do not grant them, so a
studio can cite the structure but never ship it.* 🟢 **That rule is now false in at least one
jurisdiction, and the counter-example is not a near-miss — it is strictly better built than the artefact
it contradicts.**

**Brazil's *Base Nacional Comum Curricular* is published as verified open data at `bncc.dev`** (run by
Profy), licences read from the payload at pinned SHAs and tabled in `repos/foundations.md` **Tier 1b**:

| property | `touretzkyds/ai4k12` (AAAI/CSTA) | 🟢 `bncc-dev/bncc-dados` |
|---|---|---|
| grant | 🔴 **no payload in 24 filenames** | 🟢 **MIT** code · **CC BY 4.0** data (🟡 and see `P969` — the data grant is *not* at the root) |
| machine-readable | 🔴 no | 🟢 **JSON, SQLite, CSV — 1 721 learning objectives** |
| provenance | 🔴 none per item | 🟢 **per record**: `fonte` → spreadsheet row + official PDF page |
| verifiable against the official text | 🔴 not offered | 🟢 **1 576 of 1 580** BNCC-2018 texts match the MEC/CNE PDF **character for character**; the 4 mismatches are documented in `DECISOES.md`; **141 of 141** for the Computing supplement |
| reproducible | 🔴 — | 🟢 **CI re-runs the extraction pipeline on every change and rejects divergence** |
| agent-reachable | 🔴 — | 🟢 **MCP server, 7 tools, dataset embedded** (`bncc-dev/bncc-pacotes`, and an independent second one in `dfdb76/bncc-mcp`) |

🔵 **So the correct statement of the gap is narrower and more useful than the one this shelf carried:**
**it is not that curriculum standards are ungranted — it is that the *anglophone AI-curriculum* frameworks
are, while a national curriculum base in LATAM is available as audited open data.** 🔴 **And the method
that found it is the one this KB has now recorded five times: the query was in Portuguese.** `P870`.

🟡 **What it does not fix.** BNCC is **Brazil's** curriculum, not an AI-literacy framework — it does not
discharge `Gap 367`, which is about **K-5 AI instruction material**. 🔵 It refutes the generalisation, not
the gap. And the four other mandates (China MoE, Singapore MoE, India CBSE, EU Art. 4) still have no
comparable artefact — **recorded as `Gap 371`: does a BNCC-shaped open-data publication exist for any
other national curriculum?** The question is now worth asking precisely because one exists.

### 🆕 p93 Automated essay scoring — the regulated activity, and the thinnest supply on this shelf

🔵 **`T9` says the regulated activity is assessment.** A targeted search for permissive automated essay
scoring returned **one** candidate with a usable grant, and it is a research artefact, not a dependency:

| repo | grant (payload · bytes · ref · SHA) | ★ | region | read |
|---|---|---|---|---|
| 🆕 p93 [`wwrwbs/AI_AWE`](https://github.com/wwrwbs/AI_AWE) | 🟡 **Apache-2.0 *by reference*** · `LICENSE` **1 865 B** · `main` · `41ae3bd` | 2 | 🔵 unplaced | Qwen2.5-7B + LoRA discourse-move classifier plus a **LightGBM** scorer, over the **PERSUADE 2.0** corpus. 🔴 **Read the licence note below before costing it.** |

🔴 🆕 **`P971` — a LICENSE file can be the Apache *header notice* rather than the Apache *licence*.**
Canonical Apache-2.0 is **11 357 B** (measured on this shelf a dozen times). This payload is **1 865 B, 29
non-empty lines**, and it opens with the canonical title block — *"Apache License / Version 2.0, January
2004"* followed by *"Licensed under the Apache License, Version 2.0 … You may obtain a copy of the License
at http://www.apache.org/licenses/LICENSE-2.0"*. 🔴 **A grep of the payload for the clause headings
returns nothing: no "Grant of Patent License", no "Grant of Copyright License", no "Redistribution", no
"trademark", no "APPENDIX".**
🔵 **The grant is real — incorporation by reference works — but the terms are not in the repository.**
Practical consequences, both concrete: **(a)** a classifier matching the title block returns `Apache-2.0`
and is not wrong, so this defect is invisible to every instrument on this shelf; **(b)** the single
biggest reason to prefer Apache-2.0 over MIT is **§3, the express patent grant**, and **a deliverable that
vendors this repository ships none of that text** — if a procurement requires the licence text in the
bundle, you add it yourself.
🟡 **Independent of the licence, this is a 2★ research repo.** Its README does **not** use the name
*"ArguLens"* that its paper publishes it under, and the paper's headline **QWK 0.813** does not appear in
the README — a claim-versus-payload divergence of exactly the shape `compose/code/description-drift-audit/`
was built for. 🔵 **Shelve it as a reference for the architecture (classifier + gradient-boosted scorer,
not one end-to-end LLM), never as a dependency.**

🔴 **And the honest negative that goes with it.** The other AES repositories the same search surfaced are
**CC0-1.0 competition notebooks** (`kjgpta/Data-Augmentation-for-Automated-Essay-Scoring-using-Transformer-Models`,
`kjgpta/SHL-Automated-Essay-Scoring`) or carry no stated grant — **not resolved from the payload this pass
and therefore not tabled.** 🔵 **There is no production-grade permissive AES library in this industry.**
`Gap 372`. For the activity the EU AI Act names high-risk by name, that is the most consequential supply
gap on this shelf.

### 🟢 🆕 p94 The scoring-**validation** tier — `Gap 372` narrowed to the scorer, and the half that a regulator asks for is permissive

🔴 **What this shelf concluded one pass ago:** *"there is no production-grade permissive AES library in this
industry."* 🟢 **True of the scorer. False of the deliverable.** Under Annex III the obligation attached to
assessing learning outcomes is **evidence of validity and fairness, with an explanation owed to the person
assessed** — and that layer is Apache/BSD, has 2 916 commits, and is published by the house that runs TOEFL
and the GRE.

| repo | grant (payload · bytes · file · ref · SHA) | ★ | region | what it is |
|---|---|---|---|---|
| 🆕 p94 [`EducationalTestingService/rsmtool`](https://github.com/EducationalTestingService/rsmtool) | 🟢 **Apache-2.0** · **11 358 B** · `LICENSE` · `main` · `a844f71` | 71 | 🟢 **North America** (Educational Testing Service) | 🟢 **2 916 commits.** Config-driven pipeline that builds and **evaluates** automated scoring models and emits a customisable HTML statistical report; scikit-learn + SHAP in the stack, `fairness` among its own topics, Python ≥ 3.8. 🔴 **Its README states it is *"not a scoring engine itself"*** — which is exactly why it is the row that matters. |
| 🆕 p94 [`EducationalTestingService/skll`](https://github.com/EducationalTestingService/skll) | 🟢 **BSD-3-Clause** · 1 555 B · `LICENSE.txt` · `main` · `b350eb0` | — | 🟢 **North America** — `P800`-grade: *"Copyright (c) 2012–2022 Educational Testing Service"* | Runs scikit-learn experiments from configuration instead of code. `rsmtool` pins it at `skll==5.0.1`, so the pair is one dependency decision, not two. |
| 🆕 p94 [`HASKI-RAK/NodeGrade`](https://github.com/HASKI-RAK/NodeGrade) | 🟢 **MIT** · 1 062 B · `LICENSE` · `main` · `8e144ac` | 3 | 🟡 **EMEA** (Germany — by the ECSEE '25 citation and its authors; the payload's holder line reads only *"HASKI"*, so this is **not** `P800`-grade) | 🟢 **Short-answer grading built as a node graph, with LTI 1.1/1.3 and 421 commits.** NestJS + Prisma + Postgres, React/Vite PWA on litegraph.js, Python sentence-embedding worker, providers pluggable (**local**, OpenAI, OpenRouter, OpenAI-compatible), facilitator-run workshop mode. 🔵 **The only open-response grader on this shelf that already speaks the protocol an LMS speaks** — and 3★, which is why it is tabled with its commit count rather than its popularity. |

🔴 **Where the production AES code actually lives, measured this pass:**

| repo | payload | read |
|---|---|---|
| 🆕 p94 [`openedx/ease`](https://github.com/openedx/ease) | 🔴 **AGPL-3.0** · 35 136 B · `LICENSE.txt` · `master` · `056da0a` | edX's *Enhanced AI Scoring Engine* — the first place anyone looks, and network copyleft. |
| 🆕 p94 [`openedx/edx-ora2`](https://github.com/openedx/edx-ora2) | 🔴 **AGPL-3.0** · 35 135 B · `LICENSE` · `master` · `1b7ae59` | Open Response Assessment: peer, self and staff assessment inside Open edX. Same grant. |

🔵 **So the engagement shape is a boundary, not a fork.** Score behind the AGPL service boundary (or buy the
score), **validate with Apache/BSD**, and keep the evidence pack as the client's own artefact. 🔴 **What is
still genuinely missing is one thing, precisely stated:** a permissive, production-grade **scorer** for
open-response work. That is the whole of `Gap 372` now.

#### 🔴 `P975` — one publisher, three grants, measured in a single sitting

| slug | payload | family |
|---|---|---|
| `EducationalTestingService/rsmtool` | 11 358 B · Apache title block · **4 of 4** clause headings | 🟢 Apache-2.0 |
| `EducationalTestingService/skll` | 1 555 B · *"New BSD License"* | 🟢 BSD-3-Clause |
| 🆕 p94 `EducationalTestingService/factor_analyzer` | 18 092 B · *"GNU GENERAL PUBLIC LICENSE / Version 2, June 1991"* · `main` · `de933d2` | 🔴 **GPL-2.0** |

🔴 **`factor_analyzer` is dependency-shaped** — exploratory and confirmatory factor analysis, the kind of
library a scoring pipeline imports without reading — **and it is GPL-2.0-only from the organisation whose
other two repositories are permissive.** 🔵 **A sophisticated publisher is not a licence guarantee.**
🟢 Negative control: `EducationalTestingService/rsmexplain`, named by a search summary, **does not resolve**
(`git ls-remote` exit 128).

#### 🟢 `P974` — the clause probe is the test; the byte count is only a smell

Pass 93's `P971` caught an Apache **header notice** masquerading as the Apache **licence** by its size
(1 865 B against 11 357 B). 🔴 **Size alone misjudges an honest abridged copy** — this shelf carries
`SimonsTang/feifei-companion` at 10 227 B, which is real. 🟢 **Probing for the four clause headings settles
it**: *Grant of Patent License* · *Grant of Copyright License* · *Redistribution* · *APPENDIX*.

| payload | bytes | clause headings present | reading |
|---|---|---|---|
| `rsmtool` `LICENSE` | 11 358 | 🟢 **4 of 4** | the licence |
| `wwrwbs/AI_AWE` `LICENSE` | 1 865 | 🔴 **0 of 4** | the notice, grant by reference only (`P971`) |

🔵 **And the clause that decides it is one of the four:** §3's express patent grant is the single strongest
reason to prefer Apache-2.0 over MIT, so a payload missing the heading is missing the reason.

#### 🟢 Two rows upgraded from the payload

- [`CAHLR/OATutor`](https://github.com/CAHLR/OATutor) — **MIT** · 1 105 B · `main` · `939eb0e`; holder line
  *"Zachary A. Pardos (@zpardos) - CAHL research lab"* → 🟢 **region placed: North America** (`P800`),
  previously unplaced on this shelf. 🔵 **A `Gap 369` candidate in its own right**: Bayesian Knowledge
  Tracing **and** LTI in one MIT repository — a mastery estimate that can already reach an LMS.
- 🆕 p94 [`Ebimsv/AITutorAgent`](https://github.com/Ebimsv/AITutorAgent) — **MIT** · 1 072 B · `main` ·
  `09fdd67`; holder *"Ebrahim Mousavi"* → 🔵 unplaced. LangGraph tutoring loop (structured tutorials, Q&A,
  knowledge checks). 🟡 **Reference, not dependency**: no learner model, no LTI.

### 🟢 🆕 p95 The permissive autograder tier — and the registry collision that nearly cost it

🟢 **The automated-feedback layer had exactly one row with real classroom use, and it was AGPL-3.0**
(`mumuki/mumuki-laboratory`, LATAM). **There is now a BSD-3 option**, which moves the deliverable from
*integrate across a service boundary* to *fork and own*.

| repo | grant (payload · bytes · file · ref · SHA) | version | ★ | region | what it is |
|---|---|---|---|---|---|
| 🆕 [`ucbds-infra/otter-grader`](https://github.com/ucbds-infra/otter-grader) | 🟢 **BSD-3-Clause** · 1 560 B · `LICENSE` · `master` · `190c1a4` | **7.0.0** | — | 🟢 **North America** (UC Berkeley Data Science Education Program) | 🟢 **Production autograder for Python scripts and Jupyter notebooks at course scale.** Parallel Docker grading, an Otter-managed grading VM, a student-side client for public checks, and **native Canvas and Gradescope support**. Zenodo DOI; CI and coverage live. |

🟢 **Three-layer licence agreement, which this shelf rarely gets to record.** The `LICENSE` payload says
BSD-3-Clause, `pyproject.toml` says `license = "BSD-3-Clause"`, and the PyPI classifier says
`License :: OSI Approved :: BSD License`. 🔵 **Payload, manifest and registry concur** — the opposite of
`P975` and `P342`, where they do not. 🟢 **And the default branch agrees with the tag ladder** (`7.0.0` =
`v7.0.0`), which under `P978` makes it the one platform-grade row on this shelf whose published version is
also the shippable one.

#### 🔴 `P980` — two unrelated projects, one name, incompatible grants

| what you cite | PyPI | repository | grant (payload · bytes · ref · SHA) |
|---|---|---|---|
| `otter-grader` | `otter-grader` **7.0.0** | [`ucbds-infra/otter-grader`](https://github.com/ucbds-infra/otter-grader) | 🟢 **BSD-3-Clause** · 1 560 B · `master` · `190c1a4` |
| `Otter-Autograder` | `Otter-Autograder` **0.15.9** | [`OtterDen-Lab/Autograder`](https://github.com/OtterDen-Lab/Autograder) | 🔴 **GPL-3.0** · 35 149 B · `main` · `2d9555f` |

🔴 **Different organisations, different repositories, different licences, seven major versions apart — and
both are autograders for programming coursework.** 🟢 **Resolving "the Otter autograder" by name picks
between them at random; resolving it by repository cannot.** This KB already holds
`p253-registry-first-identity` and `p791-registry-id-provenance`; **`P980` is the case where the registry
is itself the ambiguity**, and the only disambiguator is the `project_urls` → repository link.

🟡 **A second defect in the same reads, worth knowing before trusting any registry licence field.**
`Otter-Autograder`'s PyPI `license` field holds **the entire 35 kB GPL-3.0 text pasted into the metadata
field**, with `license_expression` set to `None`. 🔵 A consumer reading `info.license` for an SPDX id gets a
licence *document*; one reading its first 20 characters gets `"GNU GENERAL PUBLIC LI"`. **Prefer the
`classifiers` array — it was correct for both packages.**

#### 🔴 `Gap 372`'s three measured negatives — the open-response scorers that are not grants

| candidate | what the paper or index claims | what the payload says |
|---|---|---|
| [`edgresearch/code-automaticgrading-2022`](https://github.com/edgresearch/code-automaticgrading-2022) (**GradeAid**) | a published ASAG framework with released code | 🔴 **CC BY-SA 4.0** · 20 130 B · `LICENSE` · `master` · `309bb7e`. **A content licence, carrying a ShareAlike obligation, applied to software** — no patent or linking language, and Creative Commons itself advises against CC for code. **Unusable for a studio deliverable.** |
| [`datalab912/RATASv1`](https://github.com/datalab912/RATASv1) (rubric-based grading) | *"the authors publicly release all code on GitHub"* | 🔴 **No licence payload in 8 candidate filenames** · `main` · `04dd983` |
| [`emorynlp/llm-grading`](https://github.com/emorynlp/llm-grading) | *"an open-source auto-grading toolkit"* | 🔴 **No licence payload in 8 candidate filenames** · `master` · `b37150e` |

🔴 **`P981`: "we publicly release our code" in a paper is not a grant.** Two of these three are reachable,
populated and ungranted — which under copyright default is **all rights reserved**. 🔵 **The academic
sentence and the legal position point in opposite directions, and this industry's scoring supply is
largely academic**, so the defect is systematic rather than incidental.

### 🟢 🆕 p98 The skills-taxonomy tier — the layer a corporate-L&D engagement needs, with a non-commercial trap in the middle of it

🔵 **Found by naming the TECHNIQUE, not the industry** (`P955`, fifth consecutive pass that this
method is what paid): `open source skills taxonomy extraction ESCO O*NET`. 🔵 **It exists because
`Gap 386` established that every market figure on `intel/market.md` was institutional** — so the
buyer this tier serves had no supply tier at all.

| repo | grant (payload · bytes · ref · SHA-14) | release ladder | ★ | region | what it is |
|---|---|---|---|---|---|
| 🆕 p98 [`nestauk/ojd_daps_skills`](https://github.com/nestauk/ojd_daps_skills) | 🟢 **MIT** · `LICENSE` **1 095 B** · `dev` · `e73c2b5045793d` | 🟢 **8 tags**, `v3.0.0` | — | 🟢 **EMEA** — holder *"Copyright (c) 2024, Nesta"* (UK), read off the grant (`P800`) | 🟢 **The anchor.** Extracts skill phrases from free text and maps them onto **ESCO**, **Lightcast Open Skills** or a custom taxonomy. 🔵 **The taxonomy is a parameter** — which is exactly what a studio serving several clients and jurisdictions needs. |
| 🆕 p98 [`KonstantinosPetrakis/esco-skill-extractor`](https://github.com/KonstantinosPetrakis/esco-skill-extractor) | 🟢 **MIT, read from the BODY** · `LICENSE` **1 068 B** · `master` · `cf2877d462f99a` | 🔴 **0 tags** → `UNRELEASED` (`P985`) | — | 🔵 unplaced — the holder is a person, so `P800` yields no institution | ESCO skills **and** ISCO occupations from job descriptions or CVs, by sentence embedding + cosine similarity. Ships on PyPI and as a Docker image. |
| 🆕 p98 [`dkavargy/ESCOPlus2.0`](https://github.com/dkavargy/ESCOPlus2.0) | 🟢 **MIT** · `LICENSE` **1 086 B** · `main` · `88338a7cc196c8` | 🔴 **0 tags** | — | 🟡 **EMEA, weakly** — holder *"Copyright (c) 2026 Dimitrios Christos Kavargyris"*; the sibling slug a search named sits under `Datalab-AUTH`, Aristotle University of Thessaloniki | Extends and maintains the ESCO taxonomy itself from live job-ad data. 🔵 **The maintenance end, not the extraction end** — ESCO ages, and this is the only row here that addresses that. |

🔴 **And the first result anyone reaches is the one you cannot use.**
[`workforce-data-initiative/skills-ml`](https://github.com/workforce-data-initiative/skills-ml) — the
Open Skills Project's flagship — is **`NONCOMMERCIAL-NOT-OSI`**: `LICENSE.md`, **1 976 B**, `master` ·
`feffead90815ccd`, *"Copyright ©2018. The University of Chicago"*, granting use *"for educational and
not-for-profit research purposes"* and stating that those purposes **"exclude any service or part of
selling a service that uses the Program"**, with commercial licensing routed to the Polsky Center.

🔴 **That is the same University of Chicago template, phrase for phrase, that `Gap 385` hit one pass
ago on `dssg/student-early-warning`.** 🔵 **`P999`: the two highest-ROI institutional use cases in
this industry — student risk and skills inference — both have their canonical open-source
implementation under one university's non-commercial terms.** 🟢 **The fingerprint `"BY DOWNLOADING"`
+ `"excludes any service or part of selling a service"` has now caught 2 of 2 and is worth carrying
as a search key.** 🔴 **It is a search key and never a verdict — `P975` governs, and licence is a
property of the repository, never of the publisher.**

🟡 **Costing term, stated because two of three permissive rows have ZERO tags:** this tier is a
**build commitment**, not a product integration (`P985`). The one row with a release ladder is
Nesta's.

### 🟢 🆕 p98 The credentialing tier — permissive to VALIDATE and PUBLISH, copyleft to MINT (4 of 5)

🔵 **`repos/foundations.md` already carried the spec end** (`1EdTech/openbadges-validator-core`,
Apache-2.0; the specification itself ungranted). **This pass measured the product end, and it lands
on a seam this KB has already met once.**

| repo | grant (payload · bytes · ref · SHA-14) | release ladder | what it does |
|---|---|---|---|
| 🆕 p98 [`CredentialEngine/Open-Badge-Publisher`](https://github.com/CredentialEngine/Open-Badge-Publisher) | 🟢 **Apache-2.0** · **11 357 B pristine**, 🟢 4 of 4 clause headings (`P974`) · `main` · `278b9d7dc084a6` | 🔴 **0 tags** | 🟢 **The only permissive row in the layer**, and it **publishes** badge descriptions to the Credential Registry. 🔴 **No `NOTICE`** — so no holder, so no region from the payload. |
| 🆕 p98 [`nfh-trust-labs/opencred`](https://github.com/nfh-trust-labs/opencred) | 🟢 **MIT** · **1 071 B**, *"Copyright (c) 2026 NFH Trust Labs"* · `main` · `0fd0a9c65356db` | 🟢 **30 tags**, `v1.9.1` | Local-first **W3C Verifiable Credentials** issuer/verifier; issuer private keys never leave the host. 🔵 **The permissive issuing option is the GENERIC VC one, not the Open Badges one.** |
| 🔴 p98 `19otherrsh-dot/Opencred` | 🔴 **AGPL-3.0** · 34 523 B · `main` · `d14619e186ed08` | — | Open Badges 3.0, `did:web` issuers, status-list revocation, Docker/Helm. 🔴 **Same project NAME as the row above, different repository, opposite licence** (`P1000`). |
| 🔴 p98 `Schroedinger-Hat/certo` | 🔴 **AGPL-3.0** · 33 820 B · `main` · `6fd0a11fe2ff61` | — | Open Badges 3.0 on Strapi/Nuxt, bulk CSV issuance, public verification page. |
| 🔴 p98 `LongsightGroup/credtrail-app` | 🔴 **AGPL-3.0** · 34 523 B · `main` · `948a8ca43f3f33` | — | Open Badges 3.0, Ed25519 signing, `did:web`. |
| 🔴 p98 `CoopCodeCommun/pyopenbadges` | 🔴 **LGPL-3.0** · 26 526 B · `main` · `e38e1894fd9bce` | — | Python library to create and validate OB3 credentials. |

🔵 **`P1001` — the seam, second independent confirmation.** `Gap 372` found open-response **scoring**
AGPL while its **validation** layer is Apache/BSD. Credentialing repeats it exactly: **validate and
publish is permissive; mint is copyleft, 4 of 5.** 🔵 **Falsifiable generalisation for a later pass to
break: in education open source the permissive grant sits on the side that MEASURES, and copyleft on
the side that becomes the RECORD.** 🔴 **If it holds it is an engagement-shape rule — build the
measuring side, draw the boundary at the record** — which is the same conclusion `P94-A` reached for
scoring, arrived at independently.

### 🟢 🆕 p98 The exam layer, completed — `Gap 381`'s discharge is an AGENT row, not just a repo row

🔴 **This shelf mentioned proctoring exactly once, in `intel/trends.md`, as the place the EU AI Act's
emotion-recognition prohibition bites — and offered nothing to build the remedy with**, while this
repository has carried **three tested artefacts** for the dominant open-source exam-supervision
platform since **pass 43**.

| repo | grant (payload · bytes · ref · SHA-14) | release ladder | what already exists HERE |
|---|---|---|---|
| 🆕 p98 [`SafeExamBrowser/seb-server`](https://github.com/SafeExamBrowser/seb-server) | 🟡 **MPL-2.0** · `LICENSE` **16 725 B** · `master` · `7f45689f797337` | 🟢 **194 tags**, `v3.0-latest` | 🟢 **`sebserver-mcp-gate`** (MCP allowlist, `P85`'s second instance), 🟢 **`seb-proctoring-validator`** (closes upstream gap 90 in `ProctoringSettingsValidator.java`), 🟢 **`proctoring-reach-audit`** (which provider methods talk to the remote). 🔵 **FIRST MPL-2.0 row on any live page here** — per-file copyleft (§1.10(a)), so a proprietary integration layer is lawful and only modified MPL files reciprocate. |
| 🆕 p98 [`toshieji/moodle-grading-mcp`](https://github.com/toshieji/moodle-grading-mcp) | 🟢 **MIT** · `LICENSE` **1 120 B** · `main` · `5695878b4735ed` | 🔴 **0 tags** → `UNRELEASED` | 🟢 **`grading-draft-gate`, 37/37 offline with negative controls.** 🔵 **`Gap 372`'s seam in one repo: it writes the grade at `workflowstate=readyforreview` and never releases it** — the human stays the author of record, which is precisely what the Annex III high-risk framing asks for. |
| 🆕 p98 [`juneyaooo/lineage-skill`](https://github.com/juneyaooo/lineage-skill) | 🟢 **Apache-2.0** · `LICENSE` **11 358 B** · `main` · `7e2cbc5dc31713` | 🔴 **0 tags** | Carried by `aiact-50-2-marking`. 🔵 **11 358 B in a REPOSITORY refines `P992`** — that byte count is not unique to `apache.org`. |

🔴 **Two of the three `seb-server` READMEs said Apache-2.0 until this commit** — and
`proctoring-reach-audit` was written at **pass 46**, two passes *after* pass 44 recorded the MPL
correction in `sebserver-mcp-gate/README.md`. 🔵 **`P997`: a correction written as prose in one file
does not propagate.** 🔴 **And this one ran in the expensive direction** — Apache-2.0 is *more*
permissive than MPL-2.0, so the error would have had a studio promise a client freedoms the grant
does not give. 🟢 **Corrected in this commit, in both files.**

### 🟢 🆕 p97 The speech and pronunciation tier — **promoted after 83 passes in the history and none on this shelf**

🔴 **This layer was verified in `agents/trending.md` and `repos/trending.md` at pass 14 and never
reached a shelf page.** That is `Gap 384`, and it is bookkeeping rather than discovery — stated
plainly so nobody reads this tier as new intelligence. 🟢 **Two rows ARE new (🆕 p97); the rest are
promotions, and three are corrections.**

| agent | grant (payload · bytes · ref · SHA-14) | release ladder | ★ | region | why it matters |
|---|---|---|---|---|---|
| 🆕 p97 [`MontrealCorpusTools/Montreal-Forced-Aligner`](https://github.com/MontrealCorpusTools/Montreal-Forced-Aligner) | 🟢 **MIT** · `LICENSE` **1 066 B** · `main` · `93411fc0df3bc7` | 🟢 **116 tags · `v3.4.3`** | — | 🔵 unplaced (McGill, Montreal) | 🟢 **The production-grade anchor of this tier.** Kaldi-backed phoneme-level forced alignment — the step underneath every pronunciation score, speaking rate and pause measurement. 🔵 **116 releases where every other member of this tier has 2 or 0.** 🔵 A **titleless MIT** payload, opening directly at `Copyright (c) 2016`. |
| 🆕 p97 [`lingjzhu/charsiu`](https://github.com/lingjzhu/charsiu) | 🟢 **MIT** · `LICENSE` **1 061 B** · `main` · `13a69f2a22ca0c` | 🔴 **0 tags** | — | 🔵 unplaced | **Text-INDEPENDENT** alignment on Wav2Vec2 — it does not need a reference transcript, which is what free-form learner speech actually is. 🔵 **Complements MFA rather than replacing it.** |
| 🔵 promoted [`Halleck45/OpenPronounce`](https://github.com/Halleck45/OpenPronounce) | 🟢 **MIT** · 1 113 B · `main` · `74bc17ea406e6f` | 🟡 2 tags · `v0.3.0` | — | **EMEA** (holder `Jean-François Lépine`) | Phoneme-level scoring against expected text; returns 0–100, phoneme/word error rate, DTW acoustic distance and prosody. **Runs local, no API key.** The sellable piece of the tier. |
| 🔵 promoted [`YuanGongND/gopt`](https://github.com/YuanGongND/gopt) | 🟢 **BSD-3-Clause** · 1 517 B · `master` · `bed909daf8eca0` | 🔴 0 tags | — | 🔵 unplaced (MIT CSAIL) | The ICASSP-2022 transformer baseline — **the published number a bid gets scored against.** |
| 🆕 p97 [`doheejin/HiPAMA`](https://github.com/doheejin/HiPAMA) | 🟢 **BSD-3-Clause** · 1 526 B · `main` · `89e3f650e224e2` | 🔴 0 tags | — | **APAC** (Korea) | Hierarchical multi-aspect assessment. 🟢 **`P995`: its grant's FIRST copyright line is `Copyright (c) 2022, Yuan Gong`** — gopt's author — **so the derivation is provable from the payload, not just asserted in the paper.** |
| 🔵 promoted [`Fuann/open-apa`](https://github.com/Fuann/open-apa) | 🟢 **BSD-3-Clause** · 1 528 B · `master` · `2c92c0de1eca58` | 🔴 0 tags | — | **APAC** (Taiwan) | Benchmark and evaluation toolkit — **it scores the scorer.** This is what converts a pronunciation demo into an acceptance test. |
| 🔵 promoted [`kaldi-asr/kaldi`](https://github.com/kaldi-asr/kaldi) | 🟡 **Apache-2.0** · `COPYING` **17 264 B** · `master` · `e02e35f0254bb0` | 🔴 0 tags | — | 🔵 unplaced | The ASR substrate under MFA and the GOP tools. 🔴 **`P991`: not a pristine payload — the Apache title sits at byte 2 531 behind a joint-ownership notice**, 4 of 4 clause headings present. |

#### 🔴 The three negatives in this tier, measured — and one of them is a correction to this KB

| slug | verdict |
|---|---|
| 🔴 **CORRECTION** [`CyanXLab/Phonos`](https://github.com/CyanXLab/Phonos) | 🔴 **NO LICENCE PAYLOAD** / 24 names @ 1 B · `main` · `8a13a3b7611a3d`. **This KB counted Phonos inside a permissive layer of three.** It has no grant, and a layer count including it overstates what is buildable. |
| 🔴 [`jimbozhang/speechocean762`](https://github.com/jimbozhang/speechocean762) | 🔴 **NO LICENCE PAYLOAD** · `main` · `613968e3b0b789`. **`P994`: the reference corpus of this task is ungranted while all seven tools above are permissive.** |
| 🔴 [`tzyll/goparrot`](https://github.com/tzyll/goparrot) · [`JazminVidal/gop-pykaldi`](https://github.com/JazminVidal/gop-pykaldi) | 🔴 **NO LICENCE PAYLOAD** (both) · `0c1825fb641873` / `c34952ebbfc492`. `P981` again — a paper's *"we release our code"* is not a grant. |

🔵 **`P994`, priced the way a bid has to price it:** the engine is MIT, the aligner is MIT, the
benchmark is BSD-3 — **so the pipeline ships.** 🔴 **The data that calibrates it is not licensed**,
so a deliverable either licenses a corpus or collects and labels its own. **That is a line item in
the estimate, not a footnote in an appendix.** 🟢 **It is also the one place in this tier where
LATAM and APAC engagements are structurally better off than the shelf suggests** — L1-specific
pronunciation data has to be collected locally anyway, so the corpus gap is a scope item that was
always going to exist, not a blocker introduced by the licence.

### 🟢 🆕 p97 The AI-text-detection tier — shelved **for analysis only**, and the guardrail outranks the rows

| agent | grant (payload · bytes · ref · SHA-14) | ★ | region | why it matters |
|---|---|---|---|---|
| 🆕 p97 [`HendrikStrobelt/detecting-fake-text`](https://github.com/HendrikStrobelt/detecting-fake-text) | 🟢 **Apache-2.0** · `LICENSE` **11 357 B** *(pristine, `P992`)* · `master` · `fdf7de9396d121` | — | **North America** (MIT-IBM Watson AI Lab) | **GLTR.** Shows per-token predictability **instead of returning a verdict** — 🟢 **the pedagogically and legally correct primitive**, and the only institution-grade row here. 🔴 0 tags. |
| 🆕 p97 [`Imalwayshere/Open-Detector`](https://github.com/Imalwayshere/Open-Detector) | 🟢 **MIT** · `LICENSE` **1 066 B** · `main` · `62cc0b4655b5f3` | — | 🔵 unplaced | BERT stylometric detection trained on academic text. 🔴 **Its 99.57 % accuracy is the author's own unreplicated claim**, and the README concedes stylometry only. 🔴 0 tags. |

🔴 **Read the guardrail before either row.** The 2026 literature on this task is titled
*"LLM-Generated Text Detection Remains an Unsolved Problem"* (arXiv **2608.11256**), and a second
paper this pass read asks outright *"Why AI Detection Fails for Academic Integrity"* (arXiv
**2608.11256** / **2605.27921**). 🔴 **So this tier is shelved for ANALYSIS AND TEACHING ONLY and
never as the basis of a verdict that sanctions a student.**

🔵 **That is the regulatory position, not an abundance of caution.** An automated system bearing on
a student's academic standing is an Annex III high-risk system under the EU AI Act, whose
obligations bind from **2 Dec 2027** — and a tool whose own research field calls the task unsolved
cannot carry a high-risk conformity assessment. 🔴 **Any compose pattern that wires these rows into
a sanctioning path is out of scope and stays out of `compose/patterns.md`.** 🟢 **What they are good
for is the inverse**: a teacher-facing view that makes *predictability* visible so a class can
discuss it — which is an AI-literacy deliverable, and AI literacy is a statutory duty in EMEA
already (2 Feb 2025) and a graduation requirement in parts of North America.

### 🟢 🆕 p101 The student early-warning tier — `Gap 385` discharged on the licence, REFRAMED as a legacy-stack and corpus problem

🔵 **Read the two halves of this tier separately, because they fail for opposite reasons.** The
**institutional** half is permissive and old; the **machine-learning** half is modern and unusable.

**The institutional half — permissive, release-engineered, legacy stack.**

| repo | grant (payload · bytes · ref · SHA-40) | tags | ★ | region | note |
|---|---|---|---|---|---|
| 🆕 p101 [`Jasig/SSP`](https://github.com/Jasig/SSP) | 🟢 **Apache-2.0** · `LICENSE` 11 359 B · `master` · `711244dc0d6d5c65fd261c9bec77dd48b4dbaaf6` | 🟢 **57** (`ssp-2.9.0`) | — | 🟢 **North America** (`P800`-grade — `NOTICE`: *"Copyright 2012, JA-SIG, Inc."* and *"originally granted to JA-SIG by **Sinclair Community College**"*, Ohio, USA) | **Apereo Student Success Plan.** Early-alert, caseload management, intervention tracking and student-success plans for higher ed. 🔴 **`NOTICE` declares bundled Ext JS under GPL-3.0 and JasperReports / JFreeChart / c3p0 / Hibernate Commons under LGPL** (`P1013`). 🟢 **Take the domain model and the schema; leave the portlet UI.** |

**The machine-learning half — 6 of 6 probed, 6 of 6 unusable as a dependency.**

| repo | grant (payload · bytes · ref · SHA-40) | tags | what it is | verdict |
|---|---|---|---|---|
| 🆕 p101 [`dssg/student-early-warning`](https://github.com/dssg/student-early-warning) | 🔴 **Bespoke academic terms-of-use, NOT OSI** · `LICENSE` 2 069 B · `master` · `b68f23c76d5277d96ec70768c728234660428e92` | 0 | U Chicago DSSG; high-school on-time graduation, survival analysis, ranks by urgency | 🔴 **EXCLUDED for a services business** — grant covers not-for-profit scholarly use and *"excludes any service or part of selling a service"*. Commercial terms via Polsky Center. |
| 🆕 p101 [`Gnanakamalesh-M/student-dropout-early-warning`](https://github.com/Gnanakamalesh-M/student-dropout-early-warning) | 🔴 **NO LICENCE PAYLOAD** / 24 names @ 1 B · `main` · `6685be37a1686fdde63b55d561537417de6565db` | 0 | 🟢 the best-engineered of the six — OULAD, 30-day withdrawal at fixed checkpoints, **calibrated XGBoost + SHAP**, FastAPI + React | 🔴 **Ungranted.** 🔵 Read the **method** (calibration + SHAP is an Annex III-shaped explanation); do not take the code. |
| 🆕 p101 [`alessandroryo/student-dropout-prediction`](https://github.com/alessandroryo/student-dropout-prediction) | 🟢 **MIT** · `LICENSE` 1 073 B · `main` · `78d256a2f1543064ede59729501724443c338c2b` | 0 | demographic / academic / socio-economic features, preprocessing + training + deploy scripts | 🟡 **The only permissive row — and a single-author portfolio project with 0 tags.** Permissive is necessary, not sufficient. |
| 🆕 p101 [`himasriniva/student-dropout-early-warning`](https://github.com/himasriniva/student-dropout-early-warning) | 🔴 **NO LICENCE PAYLOAD** / 24 · `main` · `f48e88b43bc5751569c696e5c6d4277fd56fdacc` | 0 | scikit-learn on the UCI 4 424-student set, three timeline checkpoints | 🔴 Ungranted. |
| 🆕 p101 [`miansaimnadeem/Student-dropout-prediction`](https://github.com/miansaimnadeem/Student-dropout-prediction) | 🔴 **NO LICENCE PAYLOAD** / 24 · `main` · `ec805a6ecb52662c7a7f81cec09c575985b208b2` | 0 | LightGBM, FastAPI + Streamlit, Dropout/Enrolled/Graduate + risk bands | 🔴 Ungranted. |
| 🆕 p101 [`ShahCoding1/student-dropout-risk-system`](https://github.com/ShahCoding1/student-dropout-risk-system) | 🔴 **NO LICENCE PAYLOAD** / 24 · `main` · `7c5f75229ed1cb55a860fe1e18312a53c44642d2` | 0 | scikit-learn, FastAPI + React dashboard, risk banding | 🔴 Ungranted. |

🔴 **The standing statement for this tier, now evidence-backed rather than asserted:** *the permissive
supply for student early warning is the **institutional domain model** (`Jasig/SSP`, Apache-2.0, 57
releases, legacy stack) and the **psychometrics** (`CAHLR/pyBKT`, `douglasrizzo/catsim`); the modern ML
implementations are **ungranted (4 of 6)**, **non-commercial (1 of 6)** or a **portfolio project
(1 of 6)**.* 🔵 **Model the risk with the permissive psychometrics, carry the SSP schema, and treat every
ML repo in this tier as a paper you may read.**

🔴 **And the event pipe underneath it is copyleft or consortium-licensed — new this pass.**
[`LearningLocker/learninglocker`](https://github.com/LearningLocker/learninglocker), the de-facto xAPI
Learning Record Store, is **GPL-3.0** (`LICENSE` 35 141 B, `master` ·
`5fec948a823e372e740df521aa3684c8df1dcba7`, **221 tags**), and
[`IMSGlobal/caliper-spec`](https://github.com/IMSGlobal/caliper-spec) carries an **IMS Global
*Specification Document License*** (`LICENSE.md` 12 402 B, `master` ·
`1849e118b47acb24a6d97f976fe72fc2f5182570`, 4 tags) — 🔵 **a consortium spec licence, not an OSI
grant.** 🟢 **So the stack is permissive at the MODEL and the MATHS, and copyleft/consortium at the
EVENT PIPE** — which is exactly `T17`: the permissive grant sits on the side that MEASURES, and
copyleft sits on the side that becomes the RECORD.

### 🔴 🆕 p97 `Gap 385` — there is no permissive open-source student early-warning system 🟢 **— SUPERSEDED by `🆕 p101` above; kept as the record of a gap that was a search failure, not a supply failure**

🔵 **The institutional use case with the clearest ROI in this industry — dropout and retention risk
— has nothing on this shelf to start from, and that is now measured rather than assumed.**

| candidate | verdict |
|---|---|
| [`dssg/student-early-warning`](https://github.com/dssg/student-early-warning) — Data Science for Social Good, **University of Chicago** | 🔴 **`NONCOMMERCIAL-NOT-OSI`** · `LICENSE` **2 069 B** · `master` · `b68f23c76d5277`. Commercial use **PROHIBITED** (`P990`). The most credible candidate, and it is the one Globant cannot build a deliverable on. |
| `miansaimnadeem/Student-dropout-prediction` | 🔴 **NO LICENCE PAYLOAD** / 24 names · `ec805a6` |
| `maherdhami/student-dropout-risk-prediction` | 🔴 **NO LICENCE PAYLOAD** · `b107c1f` |
| `mrbansal0001/Early_dropout_risk_prediction` | 🔴 **NO LICENCE PAYLOAD** · `d9d64b9` |
| `omerErkam/student-dropout-prediction-ml` | 🔴 **NO LICENCE PAYLOAD** · `914d4c4` |
| `Syrah111/...`, `manahil2731/...`, `EmaanRana012/...` | 🟡 **same shape, not resolved** — coursework repos over one UCI dataset, named here so the denominator is honest |

🟢 **Five of six resolved; five negatives; the sixth non-OSI.** 🔵 **So the correct engagement shape
is "build the risk model, adopt the mathematics"** — the permissive psychometric tier (`pyBKT`,
`py-irt`, `eribean/girth`, `douglasrizzo/catsim`, `pykt-team/pykt-toolkit`) measures **mastery**,
which is an input to risk and not a substitute for it. 🔴 **Do not quote an open-source
early-warning system to a client. There isn't one.**

### The agent *skill* as the unit of delivery

Carried from pass 90 and re-verified at the same SHAs. ~1 in 4 rows on `topics/ai-tutor` (🆕 p94 **665 repos** — 664 at pass 90, 664 at pass 93, so
flat for three passes; the churn is inside the existing population, not new entrants) is a **skill for an agent harness** rather than an application — markdown-plus-scripts
with no UI, no hosting and no database, and overwhelmingly MIT.

| skill | grant (payload · bytes · ref · SHA) | ★ | region | scope |
|---|---|---|---|---|
| [`Miaotofu01/Study-Mate`](https://github.com/Miaotofu01/Study-Mate) | **MIT** · 1 064 B · `main` · `2cd8393` | 772 | 🔵 unplaced | Self-study agent: plans learning paths, explains concepts, guides projects |
| [`ZeKaiNie/universal-examprep-skill`](https://github.com/ZeKaiNie/universal-examprep-skill) | **MIT** · 1 065 B · `main` · `b9e84f5` | 303 | 🔵 unplaced | Slide-based teaching with page citations, **cross-session memory** |
| [`karanb192/algo-sensei`](https://github.com/karanb192/algo-sensei) | **MIT** · 1 081 B · `main` · `25ea970` | 286 | 🔵 unplaced | DSA mentor with progressive hints and mock interviews |
| [`Li-Evan/Bloom`](https://github.com/Li-Evan/Bloom) | **MIT** · 1 069 B · `main` · `b391898` | 285 | 🔵 unplaced | Adaptive tutor built on **Bloom's 2-sigma** research; self-hostable *and* a skill |
| [`SenmuuuuW/universal-diagnostic-tutor-skill`](https://github.com/SenmuuuuW/universal-diagnostic-tutor-skill) | **MIT** · 1 102 B · `main` · `075c189` | 242 | 🔵 unplaced | **Diagnosis-first** tutoring for STEM/CS — assesses before teaching |
| [`KeWang0622/kaogong-skill`](https://github.com/KeWang0622/kaogong-skill) | **MIT** · 1 083 B · `main` · `c85ca76` | 166 | **APAC** (China, civil-service exams) | Jurisdiction-specific exam coaching |
| [`zijinz456/OpenTutor`](https://github.com/zijinz456/OpenTutor) | **MIT** · 1 068 B · `main` · `f0142f2` | 137 | 🔵 unplaced | **Local-first**; notes, quizzes, flashcards from uploaded material |
| 🆕 [`PrepLabsAI/InterviewMentor`](https://github.com/PrepLabsAI/InterviewMentor) | **MIT** · 1 071 B · `main` · `609d311` | 112 | 🔵 unplaced | AI mock interviews for technical hiring — the corporate-reskilling adjacency |
| 🆕 [`SimonsTang/feifei-companion`](https://github.com/SimonsTang/feifei-companion) | 🟡 **Apache-2.0 variant** · 10 227 B · `main` · `c9c6295` | 106 | **APAC** (China) | K-12 AI education companion. 🟡 **10 227 B is not canonical Apache-2.0 (11 357 B)** — an abridged copy; read it before relying on the patent clause. |
| [`flysheep-ai/education-skills`](https://github.com/flysheep-ai/education-skills) | **MIT** · 1 068 B · `main` · `b4c9352` | 107 | 🔵 unplaced | A *collection* of teaching/study skills — the bundle pattern |
| 🆕 [`codeXsidd/Studivexa`](https://github.com/codeXsidd/Studivexa) | **MIT** · 1 068 B · `main` · `6ac2799` | 72 | 🔵 unplaced | Student productivity workspace |

### LATAM

Placed rows, not a gap. 🟢 **Every one was found by querying in Portuguese or Spanish** — confirmed again this
pass as the single highest-yield move for this region.

| row | grant (payload · bytes · ref · SHA) | ★ | region | note |
|---|---|---|---|---|
| [`belentani7/aprende-brasil`](https://github.com/belentani7/aprende-brasil) | **MIT** · 1 085 B · `main` · `bbeea5a` | — | **LATAM** (Brazil, pt-BR) | Interactive pt-BR platform, **205 modules**, AI tutor "Nilo" with optional OpenAI-compatible LLM and an **offline local fallback**; React + FastAPI + SQLite. MIT end to end. |
| 🆕 [`mumuki/mumuki-laboratory`](https://github.com/mumuki/mumuki-laboratory) | 🔴 **AGPL-3.0** · 34 523 B · `master` · `fce1ede` | 199 | **LATAM** (Argentina) | 🟢 **Student programming practice with automated feedback** — a real, long-running Argentine autograding platform used in schools and universities. 🔴 AGPL: network copyleft, so integrate, do not absorb. **The strongest LATAM row in the assessment tier.** |
| [`programadores-obreros/Agente-editor-inet`](https://github.com/programadores-obreros/Agente-editor-inet) | 🔴 **GPL-3.0** · 35 149 B · `main` · `0fa7298` | — | **LATAM** (Argentina, INET) | Teaching agent for Arduino/ESP32 in Argentine technical schools; runs **offline, double-click**. Pedagogically excellent, 🔴 copyleft. |
| 🆕 [`LabSirius/TutorIA`](https://github.com/LabSirius/TutorIA) | **MIT** · 1 069 B · `main` · `032b5aa` | — | **LATAM** (Colombia) | 🟢 **The strongest new LATAM row this pass, and the only one that is permissive end to end.** Autonomous virtual tutor agent for **rural higher education in Risaralda**, from Universidad Tecnológica de Pereira. 🟢 **It integrates with Open edX** — so it attaches to the platform tier this shelf already carries instead of replacing it. 🔵 **Region evidence is the payload's own copyright line** (`Grupo Sirius`), not an inference from the README (`P800`). 🟡 Depends on a hosted model API, which is the constraint to raise first with a public institution. |
| 🆕 p93 [`douglasrizzo/catsim`](https://github.com/douglasrizzo/catsim) | **BSD-3-Clause** · `LICENSE` 1 514 B · `dev` · `7e6caae` | 153 | 🟡 **LATAM** (Brazil) | 🟢 **The only computerized-adaptive-testing engine on this shelf, and the strongest LATAM row in the *psychometrics* tier** — item selection, ability estimation, stopping rules and a simulator, BSD-licensed, 877 commits. 🟡 **Region evidence is weaker than `P800`**: the payload's copyright line is a personal name, and Brazil comes from the project's own documentation host (`douglasrizzo.com.br`) linked throughout the README — labelled, not upgraded. 🟡 Default branch is `dev`. Tabled in `repos/foundations.md` **Tier 2c**. |
| 🆕 p93 [`bncc-dev/bncc-dados`](https://github.com/bncc-dev/bncc-dados) | 🟡 **MIT at root / CC BY 4.0 for the data** · `LICENSE` 1 073 B · `main` · `daabd7d` | 20 | 🟢 **LATAM** (Brazil) | 🟢 **Brazil's national curriculum base as audited open data — 1 721 learning objectives, per-record provenance, 1 576/1 580 character-exact against the official MEC/CNE PDF.** 🔵 **The counter-example to this shelf's "frameworks are ungranted" rule**, and the anchor of `P93-B`. 🔴 **Read `P969` before costing it: the CC BY 4.0 data grant is NOT at the repo root.** |

### 🔴 🆕 p102 `Gap 393` — the pedagogical-evaluation layer, measured as a pair

🔵 **`Gap 391` was filed against a scorer. `Gap 393` is filed against the scorer AND its benchmark**,
because a judge you cannot license is useless and a judge whose *labels* you cannot license is useless
in the same way. Both read this pass, at full addresses, with 200-controls.

| slug | role in the layer | grant (24-name probe) | ref · SHA | `P872` 200-control |
|---|---|---|---|---|
| [`kaushal0494/AITutor-EvalKit`](https://github.com/kaushal0494/AITutor-EvalKit) | the **scorer** — four BEA-2025 dimensions (Mistake Identification, Mistake Location, Providing Guidance, Actionability) | 🔴 **NONE** (paper states MIT; `P1014`) | `main` · `a71078456a90a7bb616f7c7e1de83f0bfbc44ab1` | 🟢 `README.md` **14 451 B** |
| [`kaushal0494/UnifyingAITutorEvaluation`](https://github.com/kaushal0494/UnifyingAITutorEvaluation) | the **benchmark** — MRBench; dev **300 dialogues / 2 476 responses**, test **191 / 1 547** | 🔴 **NONE** | `main` · `bbef521ddb875f2cc8a5ee798f4066965a7cfd8a` | 🟢 `README.md` **9 525 B** |
| [`NaumanNaeem/BEA_2025`](https://github.com/NaumanNaeem/BEA_2025) | a participant system (Track 1) | 🟡 **UNRESOLVED** | `main` · `bcaa52dae63d4112edea4b0186c386f0fafd5b97` | 🔴 **none obtained — 6 paths 404** |

🔴 **So the shared task that drew over 50 teams, and that this industry now quotes as the standard for
"is this tutor pedagogically sound", rests on two repositories with no grant between them.**
🟢 **What is takeable is the RUBRIC, which is published in the paper and is not copyrightable as a
method**: the four dimensions and the three-way label scale can be re-implemented against a studio's
own annotated set. 🔴 **What is not takeable is the comparability** — scores against MRBench are the
only numbers anyone recognises, and MRBench is the ungranted half. 🔵 **Cost the re-annotation, or
cost the engagement without a published benchmark number. There is no third option, and pretending
otherwise is how `P1014` reaches a client deck.**

## Negatives and licence flags — read before you quote a blog

Each re-read from the payload this pass. 🟢 Four rows advanced their HEAD since pass 90 and **kept their
grant** — `LAION-AI/Desktop_BUD-E` → `13ba697`, `ahmedEid1/lumen` → `07635d3`, `artcc/freelingo` → `ce978cf`,
`yh2072/edgameclaw` → `4d92b73`. Activity without licence drift is the normal case; it is worth measuring
because this shelf pins SHAs.

| row | what is widely claimed | what the payload says |
|---|---|---|
| [`frappe/lms`](https://github.com/frappe/lms) | 🔴 a widely-cited LMS comparison lists it as **MIT** | 🔴 **AGPL-3.0**, `license.txt` (lowercase), 33 893 B, `develop` · `933fc60`. 🆕 **And this row is why v3 exists**: v2 never probed `license.txt` and recorded it as *no grant*. Now resolved automatically. |
| [`plastic-labs/tutor-gpt`](https://github.com/plastic-labs/tutor-gpt) | listed in roundups as a permissive open tutor | 🔴 **GPL-3.0**, 35 149 B, `main` · `5c2f924` |
| [`microsoft/autogen`](https://github.com/microsoft/autogen) | "MIT" | 🟡 **Split grant, now detected mechanically** by `ladder.sh --all`: `LICENSE` = **CC-BY-4.0** (18 650 B), `LICENSE-CODE` = **MIT** (1 141 B). 🔴 **A first-match read returns CC-BY — the wrong answer for anyone shipping the code.** Cite the file. |
| [`24kchengYe/human-skill-tree`](https://github.com/24kchengYe/human-skill-tree) | 567★, prominent on `topics/ai-tutor` | 🔴 **AGPL-3.0** (1 134 B — a short-form AGPL grant, unusual) |
| [`artcc/freelingo`](https://github.com/artcc/freelingo) | self-hosted language tutor, 164★ | 🔴 **AGPL-3.0**. Self-hosting does not imply a permissive grant. |
| [`ahmedEid1/lumen`](https://github.com/ahmedEid1/lumen) | learner-owned AI education platform, 88★ | 🔴 **GPL-3.0** |
| [`yh2072/edgameclaw`](https://github.com/yh2072/edgameclaw) | material → game-based course, 71★ | 🔴 **AGPL-3.0** |
| [`A-R007/Multi-Agent-Study-Assistant`](https://github.com/A-R007/Multi-Agent-Study-Assistant) | 62★, six specialised agents | 🔴 **No licence payload in 24 filenames** (was 12 — the negative is now twice as strong) |
| [`LAION-AI/Desktop_BUD-E`](https://github.com/LAION-AI/Desktop_BUD-E) | LAION educational voice assistant, 43★ | 🔴 **No licence payload in 24 filenames** |
| 🆕 [`mahseema/aibooks`](https://github.com/mahseema/aibooks) | 91★ curated AI/ML book list on `topics/ai-tutor` | 🔴 **No licence payload in 24 filenames** · `master` · `0d71402` |
| 🆕 p101 [`kaushal0494/AITutor-EvalKit`](https://github.com/kaushal0494/AITutor-EvalKit) | the paper (arXiv:2512.03688) states the toolkit is **MIT**-licensed | 🔴 **No licence payload in 24 filenames** · `main` · `a71078456a90a7bb616f7c7e1de83f0bfbc44ab1` · **`P872` 200-control passed** (`README.md`=`200` at the same SHA). `P1014`: a paper's claim is not a grant. |
| 🆕 p101 [`dssg/student-early-warning`](https://github.com/dssg/student-early-warning) | cited in roundups as the serious open-source early-warning system | 🔴 **Not OSI at all** — bespoke U Chicago terms of use, 2 069 B, which **excludes selling a service** that uses it. 🔵 The excluded case is a services company. |
| 🆕 p101 [`LearningLocker/learninglocker`](https://github.com/LearningLocker/learninglocker) | the standard open xAPI Learning Record Store | 🔴 **GPL-3.0**, 35 141 B, `master` · `5fec948a823e372e740df521aa3684c8df1dcba7`, 221 tags. The learner-event record is copyleft. |
| 🆕 p101 [`IMSGlobal/caliper-spec`](https://github.com/IMSGlobal/caliper-spec) | "open standard" for learning analytics events | 🔴 **IMS Global *Specification Document License***, 12 402 B — a consortium spec grant, **not** an OSI licence. |

🟢 **The standing rate, re-measured with the corrected instrument: 5 of the 92 established slugs carry no
licence payload — ~1 in 18, not pass 90's ~1 in 15.** 🔵 **The change is an instrument correction, not a
change in the world**: `frappe/lms` was never ungranted, it was unreachable by a 12-name probe. Pass 87's
much worse 1-in-3 figure was measured on *fresh* `ai-tutor` rows rather than established ones and is not
withdrawn — the sampling difference remains the explanation.

## What this shelf still does not have

- 🟢 🆕 **p101: `Gap 385` is DISCHARGED — and it was a SEARCH failure, not a supply failure.**
  `Jasig/SSP` (Apache-2.0, 57 tags) has existed since 2012 under Apereo's **predecessor** org name, so
  every `apereo/*` probe this KB could have run would have returned ABSENT (`P1012`). 🔴 **What is
  genuinely missing is narrower and now stated precisely: a permissive, MODERN, release-engineered ML
  early-warning implementation.** 4 of 6 candidates are ungranted, 1 is non-commercial by its own terms,
  1 is a portfolio project — all six measured this pass. 🔵 **Tracked as `Gap 392`.**
- 🔴 🆕 **p101: `Gap 391` — the pedagogical-alignment judge is UNGRANTED.** `AITutor-EvalKit` scores
  the four BEA-2025 tutor dimensions and is the closest thing found to the instructional-alignment
  checker the first bullet on this list has asked for since pass 96 — 🔴 **and it carries no licence
  payload at 24 names with a passing 200-control.** 🔵 **The technique is published; the grant is not.**

- 🔴 **An instructional-alignment checker.** Narrowed, not closed — see the checker tier above. The
  accessibility half is done; outcome alignment has no permissive row with usable evidence.
- 🔵 **Region placement.** 20 rows above are honestly **unplaced** — the publisher's country could not be
  established from the repo this pass. Recorded rather than guessed.
- 🟢 **Learner models — `Gap 335` DISCHARGED after eight passes untouched.** The complaint stands for
  the *agents* on this shelf: only `adaptive-knowledge-graph` (Bayesian) and `Bloom` (2-sigma) carry an
  explicit learner model, and everything else relies on the context window, which is not a mastery
  estimate. 🟢 **But the missing layer exists and is MIT:**
  [`pykt-team/pykt-toolkit`](https://github.com/pykt-team/pykt-toolkit) (**MIT**, 1 066 B, `77c3e90`,
  ~430★) — the reference deep-knowledge-tracing benchmark library, 7 datasets and a model zoo (DKT,
  DKVMN, SAKT, SAINT, AKT, GKT, LPKT). Shelved in `repos/foundations.md` **Tier 2b**.
  🔵 **It was found on the first query that named the TECHNIQUE instead of the industry** — `P955`
  holding for a second consecutive pass, now on a gap that had survived eight.
  🔴 **What remains open is composition, not availability:** nothing on this shelf wires a tracing
  model to an agent's turn, so `pykt-toolkit` → agent is a build, not an integration. See `Gap 369`.
  🟢 🆕 **p93 widens the available layer from one library to four techniques, and reverses the
  recommendation inside it.** `repos/foundations.md` **Tier 2c** now carries `CAHLR/pyBKT` (MIT, 282★,
  Bayesian Knowledge Tracing), `nd-ball/py-irt` (MIT, 173★, Bayesian IRT), `eribean/girth` (MIT, 126★,
  IRT estimation), `douglasrizzo/catsim` (**BSD-3-Clause**, 153★, the only **adaptive-testing engine** on
  this shelf) and `open-spaced-repetition/py-fsrs` (MIT, 506★, review scheduling).
  🔵 **And the ordering matters more than the count: for a deliverable, prefer the classical
  psychometrics over the deep model.** `catsim` has 877 commits and a BSD grant where `pykt-toolkit` is a
  research benchmark — but the deciding reason is regulatory, not maturity. Under Annex III, assessing
  learning outcomes is high-risk and owes an explanation; **an item-difficulty parameter and a per-skill
  mastery probability are explanations, and a trained network's activation is not.**
  🟢 **`Gap 369` is narrowed by `P93-A` in `compose/patterns.md`, which specifies the wiring — but no
  repository found this pass ships it, so it stays open.**

- 🟡 🆕 **p94: `Gap 372` is narrowed, not closed.** The missing thing is a permissive production-grade
  **scorer** for open-response work. 🟢 **The validation layer that a regulator actually asks for exists and
  is permissive** — `EducationalTestingService/rsmtool` (Apache-2.0, 2 916 commits) with
  `EducationalTestingService/skll` (BSD-3), plus `HASKI-RAK/NodeGrade` (MIT, LTI 1.1/1.3) for short answers.
  🔴 **And the production scoring code is copyleft**: `openedx/ease` and `openedx/edx-ora2` are both
  AGPL-3.0, read from the payload this pass. **Score behind a service boundary, validate with Apache/BSD.**
  See the scoring-validation tier above and `P94-A`.
- 🔴 🆕 **p95: `Gap 372` is unchanged in direction and three measurements stronger.** The three
  open-response candidates the literature names were probed and **all three fail**: `GradeAid` is
  **CC BY-SA 4.0**, `RATASv1` and `emorynlp/llm-grading` carry **no licence payload**. 🟢 **So the standing
  statement is now evidence-backed rather than asserted:** *the permissive supply for regulated
  open-response scoring is the **validation** layer (`rsmtool` Apache-2.0, `skll` BSD-3); the production
  scoring code is **copyleft** (`openedx/ease`, `openedx/edx-ora2`, AGPL-3.0); the research scoring code is
  **ungranted or CC-licensed**.* **Score behind a service boundary, validate with Apache/BSD.**
  🔵 **What pass 95 did add at this layer is adjacent, not the gap**: `ucbds-infra/otter-grader` (BSD-3)
  grades **code against tests**, which is a different assessment type from a constructed response.
- 🟢 🆕 **p100: `Gap 372` is DISCHARGED, and the three bullets above it are superseded in their
  conclusion but kept as the record of how a measurement error propagated.** Everything p94 and p95
  measured about *licences* was correct; the inference *"therefore no permissive scorer is
  deliverable"* was not. 🟢 **`wwrwbs/AI_AWE` has a release (`v0.1.0`, adapter artifact `http=200`)
  and `EducationalTestingService/rsmtool` has 33 (`v12.0.0`)** — and both were on this shelf, with
  their tags uncounted, while five consecutive passes described their tier as supply-starved.
  🔵 **`P1010`: re-measure a tier's existing rows before declaring the tier blocked on a newly
  measured property.** 🔴 **What remains is NOT a supply gap but a corpus gap — `Gap 390`:** the
  distributed adapter was trained on `CC-BY-NC-SA-4.0` material (`Gap 389`, settled this pass from
  the author's own payload), so **the code ships and the weights do not.** 🟢 **The retraining seam
  is in the repository and is costed as `P100-A`.**
- 🔴 🆕 **p95: `Gap 376` — this shelf's instrument has been unrunnable for three consecutive passes**, and
  that is the only item here getting worse rather than narrower. `grant-ladder-v4` carries ten registered
  corrections in a shared classifier and **has not executed since pass 92**; passes 93, 94 and 95 each
  hand-read ~12 rows against a published 133-row census. 🔴 **The decay is in the denominator, not the
  method.** 🟢 **The first duty of the next pass that can execute code is to re-derive the full census and
  disagree with these pages on the record** — every other item on this list is additive; this one is
  corrective.
- 🔴 🆕 **p93: this shelf cannot see a per-directory licence** (`P969` / `Gap 370`). A dataset repository
  can present MIT at the root while the data it exists to publish is CC BY 4.0 one directory down, and
  **both the 24-name ladder and GitHub's own sidebar return the root answer.** Proved on
  `bncc-dev/bncc-dados`; mechanism in `repos/foundations.md`.

- 🟡 🆕 **p96: the instructional-alignment checker is RESTATED, not closed — and the restatement is the
  progress.** 🟢 The *technique* is permissive and published in 2026: `Qwen-Applications/OpenRS`
  (Apache-2.0) judges against weighted tiered rubrics, `wanghaoyu0408/OpenRubrics` (MIT) generates them,
  `planepig/rubricbench` (MIT) calibrates the judge against **1 147 expert-annotated** human comparisons.
  🔴 **What no repository does is bind a rubric to a published curriculum standard.** 🟢 **This shelf holds
  the other end of that bind** — `bncc-dev/bncc-pacotes`, MIT code + CC BY 4.0 data, **1 721 verified BNCC
  objectives behind 7 MCP tools** — **and nothing wires them.** 🔵 **So this is now the same shape as
  `Gap 369`: four permissive layers, three publishers, no integration.** Tracked as **`Gap 379`**; specified
  and costed as `P96-A` in `compose/patterns.md`.
- 🟡 🆕 **p96: `Gap 376` is BOUNDED and still owed.** 🔴 **The instrument has now been unrunnable for four
  consecutive passes** — `grant-ladder-v4/ladder.sh` *and* its offline `test_ladder.sh` were both denied
  before starting. 🟢 **But the decay is no longer a mood: 127 published `(slug, ref, sha7)` triples were
  probed and 122 are still at the tip of their pinned ref — 0 unreachable, 0 vanished refs — and all 5
  drifted rows were re-read and kept their grant.** 🔵 **"The coverage is decaying" is now "5 rows of 127
  needed re-reading, and they were read."** 🔴 **This is NOT 127 rows re-verified**: a current SHA says
  nothing about whether the 24-name reach or the classifier behind that row was sound, and that is precisely
  what only `grant-ladder-v4` can settle. **The corrective duty stands; its size is now known.**
  Evidence: `compose/code/p987-census-sha-currency/`.
- 🔴 🆕 **p96: `Gap 380` — this shelf addresses payloads by abbreviated SHA, and the abbreviation does not
  always resolve** (`P987`). Measured on one commit both ways: the **full 40 characters return 200 and the
  7-character form returns 404**, inconsistently per commit. 🔴 **An unresolved abbreviation 404s all 24
  filenames and reads exactly like `no licence payload`.** 🟢 **`P872` caught the one case that occurred,
  and all 10 published negatives were re-probed at their published SHAs: 10 of 10 return a 200 control, so
  none is an artefact.** 🔵 **Publish the abbreviation for a human; address the payload with the full 40.**
- 🔴 🆕 **p96: `Gap 381` — a tested integration in `compose/code/` is not checked against the shelf.**
  `UniTime/unitime` is **Apache-2.0** with a pristine 11 357 B payload and 101 release tags, this KB has
  carried a tested MCP gate for it since **pass 42**, and it appears on **no shelf page**. 🔵 **Nothing
  reconciles the two inventories**, so a verified asset can sit in the evidence directory for fifty passes
  without ever being offered to a client.

*Prior pass content is preserved in git history at commit `306eb06` and earlier; it is not duplicated here.*
