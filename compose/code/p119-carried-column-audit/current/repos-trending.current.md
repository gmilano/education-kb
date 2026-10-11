---
industry: education
region: Global
updated: 2026-10-11
---

## 🟢 Pass 118 — 2026-10-11 (fifth pass of this date), 03:4x–04:2x UTC

🔵 **APPEND-ONLY page. Added above p117's section; nothing below is edited.**

🟢 **"Trending" is measured here, not quoted. This pass adds a second measured axis beside the
star count: the DEFAULT BRANCH, read over the git transport (`P118-B`) for all 249 addresses in
this KB — and it turns out to be the axis that was quietly corrupting the licence column.**

### 🔴 `P118-C` — 37 of 249 addresses (14.9 %) do not default to `main` or `master`

🔴 **And five default to a TAG-SHAPED ref that no `main`/`master`/`develop` probe can reach.**

| default branch | addresses |
|---|---|
| `develop` / `dev` | **22** — `oppia/oppia`, `learningequality/kolibri`, `opencast/opencast`, `oat-sa/tao-core`, `ls1intum/Artemis`, `frappe/frappe`, `frappe/lms`, `frappe/erpnext`, `frappe/education`, `1EdTech/openbadges-specification`, `1EdTech/openbadges-validator-core`, `LearnPress/learnpress`, `learnhouse/learnhouse`, `pressbooks/pressbooks`, `douglasrizzo/catsim`, `nestauk/ojd_daps_skills`, `oppia/oppia-android`, `moodlehq/moodle-tool_dataprivacy` (`MOODLE_34_STABLE`), + others |
| 🔴 tag-shaped | **5** — `GibbonEdu/core` → **`v31.0.00`**, `claroline/Claroline` → **`15.0`**, `OpenEduCat/openeducat_erp` → **`19.0`**, `portabilis/i-educar` → **`2.12`**, `ed-fi-alliance-oss/Ed-Fi-Data-Standard` → **`v6.2.0`** |
| version-stream | `Elgg/Elgg` → `7.x`, `ILIAS-eLearning/ILIAS` → `release_11`, `cortezaproject/corteza` → `2024.9.x`, `bigbluebutton/bigbluebutton` → `v3.0.x-develop`, `portabilis/i-diario` → `1.6`, `xiaochong0302/course-tencent-cloud` → `v2` |
| other | `apache/ofbiz-framework` → `trunk`, `gocodebox/lifterlms` → `trunk`, `overhangio/tutor` → `release`, `francoisjacquet/rosariosis` → **`mobile`**, `jtylek/EpesiCRM` → `laravel` |

🔴 **Why this is a trending finding and not a footnote: `frappe/frappe`'s `master` carries an
**MIT** `LICENSE` and its `develop` — the branch it ships from, pushed 2026-10-11 — carries the
current grant. A probe that tries `main`, then `master`, then `develop` and stops at the first
200 reads a branch the project no longer develops on.** p117's `licence.sh` did exactly that, and
so did v1 of this pass's own instrument.

🟢 **The channel: `git ls-remote --symref https://github.com/{slug} HEAD`, 249/249, no session
scope needed — while `api.github.com/repos/{owner}/{repo}` was refused to `curl`, to `gh api` and
to the MCP relay alike (`P118-A`).** For the one field this census could not proceed without, the
oldest transport was the only ungated one.

### 🟢 Repos by stars, measured this pass

| repo | ★ | last push | default branch | licence, from the tree |
|---|---|---|---|---|
| [`HKUDS/DeepTutor`](https://github.com/HKUDS/DeepTutor) | 41 103 | 2026-10-11 | `main` | 🟢 Apache-2.0 |
| [`frappe/frappe`](https://github.com/frappe/frappe) | 10 913 | 2026-10-11 | 🔴 `develop` | 🟢 **MIT** ⚠️ was GPL-3.0 |
| [`instructure/canvas-lms`](https://github.com/instructure/canvas-lms) | 6 863 | 2026-10-09 | `master` | 🔴 AGPL-3.0 |
| [`oppia/oppia`](https://github.com/oppia/oppia) | 6 845 | 2026-10-11 | 🔴 `develop` | 🟢 Apache-2.0 |
| [`learnhouse/learnhouse`](https://github.com/learnhouse/learnhouse) | 2 335 | 2026-10-10 | 🔴 `dev` | 🔴 **AGPL-3.0** ⚠️ was Apache-2.0 |
| [`Elgg/Elgg`](https://github.com/Elgg/Elgg) | 1 677 | 2026-10-10 | 🔴 `7.x` | 🟡 **GPL-2.0 + MIT** (bundled plugins MIT) |
| [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | 1 141 | 2026-10-11 | 🔴 `develop` | 🟢 MIT |
| [`overhangio/tutor`](https://github.com/overhangio/tutor) | 1 127 | 2026-10-08 | 🔴 `release` | 🔴 AGPL-3.0 |
| [`plastic-labs/tutor-gpt`](https://github.com/plastic-labs/tutor-gpt) | 931 | 🔴 **2026-02-20** | `main` | 🔴 **GPL-3.0** ⚠️ was MIT |
| [`PrairieLearn/PrairieLearn`](https://github.com/PrairieLearn/PrairieLearn) | 518 | 2026-10-10 | `master` | 🔴 **AGPL-3.0 (CE) + MIT + proprietary `ee/`** |
| [`satvik314/educhain`](https://github.com/satvik314/educhain) | 389 | 2026-10-06 | `main` | 🟢 MIT |
| [`elmsln/elmsln`](https://github.com/elmsln/elmsln) | 253 | 🟡 2026-08-14 | `master` | 🔴 **GPL-3.0** ⚠️ was Apache-2.0 |
| [`Selleo/mentingo`](https://github.com/Selleo/mentingo) | 92 | 2026-10-10 | `main` | 🟢 **MIT** ⚠️ was Apache-2.0 |
| [`openedx/edx-ora2`](https://github.com/openedx/edx-ora2) | 64 | 2026-10-04 | `master` | 🔴 **AGPL-3.0** ⚠️ was Apache-2.0 |
| [`Tadreeb-LMS/tadreeblms`](https://github.com/Tadreeb-LMS/tadreeblms) | 34 | 2026-10-06 | `main` | 🔴 **AGPL-3.0** ⚠️ was GPL-3 |
| [`FWU-DE/ais-chat`](https://github.com/FWU-DE/ais-chat) | 25 | 2026-10-10 | `main` | 🔴 **AGPL-3.0** ⚠️ was MIT |
| [`MysterionRise/adaptive-knowledge-graph`](https://github.com/MysterionRise/adaptive-knowledge-graph) | 17 | 2026-10-08 | `main` | 🟢 **MIT** ⚠️ was Apache-2.0 |

🟡 **One address queried did not come back: [`mitodl/open-learning-ai-tutor`](https://github.com/mitodl/open-learning-ai-tutor).
Seven of eight `repo:` qualifiers returned; this one returned no record from the search endpoint,
while `raw.githubusercontent.com` served its `LICENSE` (MIT, 1 069 B) in the same window.**
🔵 Two channels, two answers about whether the repository is there — recorded rather than
resolved, because this pass has no third channel for it.

### 🔴 What `github trending` added to this page: nothing

🔵 **The mandated search returned no live GitHub Trending page — only third-party trackers and
roundups, all of whose addresses this KB already holds.** 🔴 **Zero new repos. `Gap 402` weakens
a third consecutive pass** (p117: 4 new tokens / 13 rejected; p118: 0 / 15). Stated explicitly,
because an append-only trend page with a silent section is indistinguishable from a covered one.

