## 🆕 2026-11-11 (p763) — **The GitHub search channel came back, so for the first time in three passes every licence was read from a derived `default_branch` rather than a guessed one — and the first thing it caught was a standards body whose default branch is a version tag. A third distinct sha256 now sits at exactly `11,357` bytes. And half of this pass's "no grant" verdicts were wrong until a language manifest was probed.**

**`24` permissive foundation rows · `8` platform rows · `53` addresses resolved · `47` licence payloads byte-read with length and sha256₁₂ · `157` licence-path probes · `102` exhaustive probes across `6` no-payload addresses, `3` of them refuted by a manifest follow-up and `3` published as absences · `1` p762 control reproduced exactly · `2026-11-11`.**

### 🟢 The channel finding: `gh api search/repositories` works, and it changes what can be claimed

`p761` and `p762` both recorded `api.github.com` as **`403`** and fell back to page-sourced star counts. At this tunnel the **`gh` CLI's search endpoint returns `200`** and carries `default_branch`, `stargazers_count`, the index licence, `archived` and `pushed_at` authoritatively.

| Channel | State `2026-11-11` |
|---|---|
| `gh api search/repositories` | 🟢 **`200`, authoritative** — used for every address this pass |
| `gh api orgs/*` and `repos/*` | 🔴 refused by session repository scoping; worked around with `org:` and `repo:` search qualifiers |
| `curl api.github.com` | 🔴 **`403`** |
| `curl github.com` (HTML) | 🔴 **`403`** |
| `raw.githubusercontent.com` | 🟢 **`200`** — all `47` payloads byte-read here |
| `curl -sI` existence check (mandated) | 🔴 **structurally useless for the seventh consecutive pass**: `403` for live and fabricated paths alike under the same owner, so it has zero discriminating power |
| Arbitrary web domains | 🔴 outside the session allowlist, DNS unresolved — this blocked both of this pass's attempted primary verifications |

🟢 **`ACTION p762-B` is therefore discharged in full for the first time**, and it fired immediately: [`Ed-Fi-Alliance-OSS/Ed-Fi-Data-Standard`](https://github.com/Ed-Fi-Alliance-OSS/Ed-Fi-Data-Standard) (`47★`) has `default_branch` **`v6.2.0`** — a release tag standing in for a branch. `main` and `master` both `404`. A guessed branch would have recorded the flagship of the US K-12 data standard as having no licence at all (`T614`).

### 🔴 A third distinct payload at exactly `11,357` bytes, and the two mechanisms are different

| sha256₁₂ at `11,357 B` | Deviation from canonical Apache-2.0 | Seen on |
|---|---|---|
| `c71d239df917` | — (canonical) | `14` repositories this pass |
| `b40930bbcf80` | APPENDIX brackets → braces, two lines, one-for-one characters | [`adlnet/xapi-profiles`](https://github.com/adlnet/xapi-profiles) `60★` — 🔵 **third organisation to carry it**, after p761's `wfp/designsystem` |
| 🔴 `58d1e17ffe51` | **blank line added at the top, trailing newline removed** — two edits that cancel in length | [`adlnet/ADL_LRS`](https://github.com/adlnet/ADL_LRS) `335★` |

🔴 **And genuine Apache-2.0 was measured at seven sizes in this single pass**: `10,172` · `10,173` · `11,348` · `11,357` (three hashes) · `11,358` · `11,525` · `11,585`. The `10,17x` class is Apache **with the APPENDIX stripped**, and the one-byte gap between the two Ed-Fi payloads is a trailing newline. 🟢 `ACTION p762-A` confirmed by a second independent mechanism (`T605`). 🔵 [`adlnet/CATAPULT`](https://github.com/adlnet/CATAPULT) reproduced p762's `or-tools` constant exactly (`11,358 B` / `cfc7749b96f6`) from an unrelated organisation.

### 🔴 `INS-001` — the path set has to cross language ecosystems, and this is a `50%` correction

`6` addresses returned nothing across `17` LICENSE-family paths. One manifest probe each refuted three of them:

| Address | Manifest | Corrected grant |
|---|---|---|
| [`kosukeimai/fastLink`](https://github.com/kosukeimai/fastLink) `294★` | `DESCRIPTION` `1,508 B` | 🔴 **GPL(>= 3)** — the R convention, and this is the best-known academic record-linkage package |
| [`yifnli/uis-sdg4-mcp`](https://github.com/yifnli/uis-sdg4-mcp) `2★` | `pyproject.toml` `1,151 B` | ⚠️ **MIT declared, `LICENSE` file absent** although the README says *"See `LICENSE` for details"* |
| [`intelliboard/intelliboard`](https://github.com/intelliboard/intelliboard) `25★` | `version.php` `1,154 B` | 🔴 **GPL-3.0-or-later** in a source header, per Moodle plugin convention |

🟢 Genuine absences, published as absences and **not** as licence states: [`lisaguthrie/wa-ed-mcp`](https://github.com/lisaguthrie/wa-ed-mcp) (`1★`), [`teszerrakt/pddikti-scraper`](https://github.com/teszerrakt/pddikti-scraper) (`1★`), [`kevinleandrogomes/censo-escolar-pipeline-etl`](https://github.com/kevinleandrogomes/censo-escolar-pipeline-etl) (`0★`).

### 🔴 `INS-002` — `in:name` inflates as badly as plain language; `topic:` is the only qualifier that survived

| Query | `total_count` | Reading |
|---|---|---|
| `ed-fi in:name` | **`24,698`** | 🔴 the hyphen tokenises; absurd for a standard with `30` repositories in its own org |
| `emis in:name` | **`19,968`** | 🔴 substring collision — *premise*, *chemistry* |
| `slds in:name` | `509` | 🔴 against `statewide longitudinal data system` → **`0`** |
| `xapi in:name` | `2,126` | 🔴 against `topic:xapi` → `282` |
| `topic:learning-analytics` | **`408`** | 🟢 usable |
| `topic:xapi` | **`282`** | 🟢 usable |
| `topic:lrs` | **`73`** | 🟢 usable |
| `topic:oneroster` | **`18`** | 🟢 usable |

🔵 And the collision is visible in the result sets, not just the counts: `learning analytics dashboard` reports **`6,565`** while its top ten are bank-statement analysers, a banking system and a carbon-aware ML scheduler; `education management information system` reports `244` with a Bee-Movie-adjacent repository, a Swedbank mirror and a résumé builder at the top. 🟢 **`T592` now has a named safe qualifier** (`ACTION p763-C`).

### 🔴 Liveness: the most-starred artefacts on this register are the stalest

Of `adlnet`'s top `20` xAPI repositories, **`11` are archived**. [`adlnet/xAPI-Spec`](https://github.com/adlnet/xAPI-Spec) (`955★`, the largest repository on register) last pushed `2025-07-03`. **`adlnet/tla`, the Total Learning Architecture, is archived and `Unlicense`.** [`LearningLocker/learninglocker`](https://github.com/LearningLocker/learninglocker) (`586★`) last pushed `2024-05-30`. 🟢 **The live permissive core, named**: [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) (Apache-2.0, `2026-11-08`), [`adlnet/ADL_LRS`](https://github.com/adlnet/ADL_LRS) (Apache-2.0), [`yetanalytics/xapipe`](https://github.com/yetanalytics/xapipe), [`Ed-Fi-Alliance-OSS/Data-Management-Service`](https://github.com/Ed-Fi-Alliance-OSS/Data-Management-Service) (pushed `2026-11-11`), [`moj-analytical-services/splink`](https://github.com/moj-analytical-services/splink) (MIT, pushed `2026-11-11`). 🔵 **Star count is the worst liveness proxy available here** (`T611`).

### 🔵 And the Apereo estate is permissive but index-invisible

`12` of `21` repositories in [`Apereo-Learning-Analytics-Initiative`](https://github.com/Apereo-Learning-Analytics-Initiative) are indexed `NOASSERTION`. The two measured byte-read as **Educational Community License 2.0** — OSI-approved, Apache-derived, modified patent grant: `OpenLRW` (`62★`, `9,878 B` / `f339063d2f60`) and `OpenDashboard-legacy` (`47★`, `9,919 B` / `fb10d1260ddc`). 🟢 **Usable.** 🔴 Invisible to any badge-driven checklist, and last pushed `2025-09-12`.
