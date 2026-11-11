# 🆕 Trends new at `p763` (researched 2026-11-11) — `T604`–`T614`

**The register is the education data warehouse and the statutory return** — where learning telemetry lands, who is accountable for it, and the annual report that is the real deliverable. `ACTION p760-A`/`p761-G`/`p762-F` was pointed, as instructed, at the telemetry substrate these shelves already hold (`xAPI` `1,109` · `LTI` `1,633` · `OneRoster` `645` · `Ed-Fi` `533` · `Caliper` `402` · `LRS` `354`) and asked which institutional buyer's procurement is defined by it. **It returned the data office of the state or national education authority, at `SLDS` `0` · `institutional research` `0` · `P20W` `0` · `EDFacts` `0` · `accountability reporting` `0` · `record linkage` `0` · `data warehouse` `1`.** Third consecutive discharge of that rule, and the third consecutive buyer this base had never held.

**A note on form, stated once.** Plain declarative prose, the shelves' structural conventions, pass id, byte-read licence cells with length and sha256₁₂, region placement, `T` tokens, `INS` tokens for instrument findings (`ACTION p762-G`), `ACTION` tokens. 🔴 marks a refusal or a defect, 🟢 a usable finding, 🔵 a reading or reclassification.

**Instrument, measured:** `53` addresses resolved · **`47` licence payloads byte-read** with length and sha256₁₂ · `157` licence-path probes · `6` addresses returned no payload across `17` paths each (`102` probes) and **`3` of the `6` were refuted by a follow-up manifest probe**; the remaining `3` are published as absences and **none is published as a licence state** (`ACTION p761-C`) · `1` p762 control re-measured and reproduced exactly · **`default_branch` derived from the search channel for all `53` addresses, none guessed**.

---

### `T604` 🔴 The US statewide longitudinal data system has a `$28.5M` annual appropriation, has reached every state, and returns `0` repositories under its own name

The query `statewide longitudinal data system` returns **`total_count 0`** on the repository-search channel. The SLDS grant programme is funded at **`$28.5` million** for FY26 with the Workforce Data Quality Initiative at `$6` million, both flat (Data Quality Campaign; **search-sourced — the host is outside this session's allowed network domains**), and across eight rounds **`50` states, `5` territories and DC** have held at least one grant (NCES). 🟢 **The reference implementation exists, is Apache-2.0 and is actively maintained**: [`CEDStandards/CEDS-IDS`](https://github.com/CEDStandards/CEDS-IDS), `51★`, `11,357 B` / `c71d239df917` from `master`, where IDS is *Integrated Data Store*. 🔵 **The finding is a vocabulary gap, not a supply gap, and it is the most expensive one this base has measured**: the buyer's procurement phrase and the artefact's name share no words.

### `T605` 🔴 A third distinct sha256 at exactly `11,357` bytes, by a mechanism unlike the first

`p761` measured two Apache-2.0 payloads of identical length and different hash, differing by a bracket-for-brace swap. This pass reproduces that variant **in a third organisation** ([`adlnet/xapi-profiles`](https://github.com/adlnet/xapi-profiles), `60★`, `b40930bbcf80`) and adds a third payload at the same length: [`adlnet/ADL_LRS`](https://github.com/adlnet/ADL_LRS) (`335★`, **`58d1e17ffe51`**), which differs by **one blank line added at the top and the trailing newline removed** — two whitespace edits that cancel in length. Genuine Apache-2.0 was measured at **seven sizes** this pass (`10,172` · `10,173` · `11,348` · `11,357`×3 · `11,358` · `11,525` · `11,585`); the `10,17x` class is Apache with the APPENDIX stripped. 🟢 **`ACTION p762-A` is confirmed by a second independent mechanism: a byte count cannot identify a licence, and now cannot distinguish three.**

### `T606` 🔴 One university lab ships its pipeline under MIT and its education model under a grant that forbids selling a service — and the index reports `NOASSERTION` for both

Four payloads, all indexed `NOASSERTION`, all from the University of Chicago's Data Science for Social Good lineage:

| Repo | Stars | Payload | Grant |
|---|---|---|---|
| [`dssg/triage`](https://github.com/dssg/triage) | `202★` | `1,176 B` · `e3f05dfc649c` | 🟢 **Verbatim MIT**, with one attribution line above the title |
| [`dssg/student-early-warning`](https://github.com/dssg/student-early-warning) | `70★` | `2,069 B` · `11f9627267d7` | 🔴 Research-only; *"excludes any service or part of selling a service"* |
| [`dssg/police-eis`](https://github.com/dssg/police-eis) | `57★` | `1,979 B` · `4a1de093c141` | 🔴 Same clause |
| [`workforce-data-initiative/skills-ml`](https://github.com/workforce-data-initiative/skills-ml) | `178★` | `1,976 B` · `2cc582006b14` | 🔴 Same clause — **p762's finding, re-measured as a control and reproduced exactly** |

🟢 **The usable rule: take the generic pipeline, never the domain model.** `triage` is the pipeline under the early-warning work and it is MIT. 🔵 **A mechanism, measured for this case only**: the single prepended attribution line is the sole difference between `triage`'s payload and verbatim MIT, and it is enough for the index to decline to name it. 🔴 **This does not explain `p761-E`'s `getodk` case** — byte-identical payloads with different index verdicts — and no claim is made that it does. 🔴 **Third consecutive register whose key component forbids consulting delivery.**

### `T607` 🔴 The only OpenEMIS agents are Business Source Licence 1.1, and the licence names a different repository than the one it sits in

[`tixuz/openemis-mcp`](https://github.com/tixuz/openemis-mcp) (`4★`) and [`tixuz/openemis-mcp-pro`](https://github.com/tixuz/openemis-mcp-pro) (`2★`) both carry `LICENSE.md` at **`647 B` / `4dead97d8aaf` — byte-identical**, both indexed `NOASSERTION`. It is **BSL 1.1**, which is not an open-source licence: Additional Use Grant *"non-production evaluation and internal testing only"*, with the text stating you *"may not offer the Licensed Work as a commercial hosted service or embed it in a commercial product without a separate commercial licence"*; Change Date `2029-01-01`, Change License MIT. 🔴 **The `Licensed Work:` field reads `openemis-mcp-pro` in both files**, so on the face of its own instrument the free repository's coverage is undetermined. 🔵 **A new failure class for these shelves: the licence is legible, correctly scoped to a product, and names the wrong artefact.**

### `T608` 🟢 `p757`'s law holds on the warehouse register without a counter-example

Permissive, byte-read: `5 / 5` CEDS repositories (Apache-2.0), `9 / 9` Ed-Fi repositories read (Apache-2.0), `adlnet` (Apache-2.0 and MIT), `yetanalytics` (Apache-2.0), `splink` (MIT, UK Ministry of Justice), `NHSE_probabilistic_linkage` (MIT), Superset, DuckDB, Dagster, and Apereo's **ECL-2.0**. Copyleft, byte-read: `OpenEMIS/core` **GPL-2.0** — UNESCO's own ministry EMIS — `learninglocker` **GPL-3.0**, `pddikti` and `moodle-mcp-server` **AGPL-3.0**, `oneroster-import` **GPL-2.0**, `fastLink` **GPL(>=3)**, `intelliboard` **GPL-3.0+**. 🟢 **Everything that defines, measures, moves or validates the data is permissive. Everything that holds the student record is copyleft. Fourth consecutive register, no counter-example.**

### `T609` 🔴 The standard's own authors say not to point an AI system at the API

Ed-Fi's May 2026 white paper *"The Ed-Fi Data Standard in the Age of AI"* argues a data standard matters **more** in the AI era, and recommends that **AI and analytics systems should not interact directly with the Ed-Fi API** (search-sourced; `docs.ed-fi.org` is outside this session's allowed network domains and the recommendation could not be primary-verified). The `6.x` roadmap adds a **PII flag for AI discovery**, and the Alliance is aligning the Ed-Fi Data Standard, Ed-Fi OneRoster and CEDS. 🟢 **Consequence, and it governs every pattern filed this pass: read a warehouse replica, land data with `Ed-Fi-Kafka-Connect` or `Ed-Fi-API-Publisher`, and keep the agent off the transactional store** (`P312`).

### `T610` 🔵 The agent layer on this register is reader-side, nine months old, globally distributed, and absent from the work that is paid for

Nine agent artefacts, none above `13★`, all first pushed within the last nine months, placed across five regions: Sweden (`Skolverket-MCP`, MIT, `13★`), Switzerland, France, Hong Kong, Indonesia, Washington State, UNESCO UIS, one global, and the Ed-Fi Alliance's own [`Ed-Fi-SDK-for-AI-Assistants`](https://github.com/Ed-Fi-Exchange-OSS/Ed-Fi-SDK-for-AI-Assistants) (Apache-2.0, pushed `2026-11-10`), which ships **Agent Skills** for Claude Code and GitHub Copilot rather than an MCP server. 🔴 **Every one reads already-published statistics. Not one produces, validates or reconciles a statutory return** — the annual, dated, funding-bearing deliverable. 🟢 **That is the gap with a budget attached.**

### `T611` 🔴 The xAPI estate is largely archived and its flagship is stale

Of `adlnet`'s top `20` xAPI repositories, **`11` are archived**. [`adlnet/xAPI-Spec`](https://github.com/adlnet/xAPI-Spec) (`955★`, the largest repository on this register) was last pushed `2025-07-03`. **`adlnet/tla` — the Total Learning Architecture — is archived and `Unlicense`.** [`LearningLocker/learninglocker`](https://github.com/LearningLocker/learninglocker) (`586★`) was last pushed `2024-05-30`. 🟢 **The live permissive core is narrow and nameable**: `yetanalytics/lrsql` (Apache-2.0, `2026-11-08`), `adlnet/ADL_LRS` (Apache-2.0), `yetanalytics/xapipe`, `adlnet/CATAPULT`. 🔵 **Star count is the worst possible liveness proxy on this register** — the most-starred artefacts are the stalest.

### `T612` 🔴 Secondary sources do not respect this base's region vocabulary, and the APAC leg proved it

The APAC regional leg returned the **UAE's `25` generative-AI school prohibitions (February 2026)** and the **UK's January 2026 school AI safety standards** inside an APAC result set. Both are EMEA under this base's closed five-value vocabulary. 🟢 **Neither was filed in APAC.** 🔵 **The rule this implies: a region field may never be populated from the region framing of the source that supplied the fact.** A pipeline that trusts it silently mis-buckets, and `region` is precisely the field whose variants break the filter.

### `T613` 🔴 LATAM has this register's best-documented demand and a supply side of `12` repositories, and the Spanish-language probe returns zero

Brazil's Censo Escolar 2026 (Educacenso, **Portaria Inep nº 217/2026**) has a reference date of `2026-05-27`, closed stage-1 collection on `2026-07-31`, extended checking to `2026-09-11`, takes corrections to `2026-10-23` (secondary-sourced), and **transmits final homologated data to the FNDE on `2026-12-11`**, from which federal funding for roughly `40` million students is computed; stage 2 runs `2027-02-01` to `2027-03-12`. Against that: `censo escolar inep microdados` → **`total_count 12`**, **maximum `3★`**, mostly undergraduate analyses, and the only pipeline-named repository has `0★` and no grant at `17` paths or in any manifest. And `educacion datos abiertos ministerio escuelas` → **`total_count 0`**. 🟢 **The sharpest funded-demand-to-nil-supply gap measured in any region this pass.**

### `T614` 🔴 `default_branch` is not always a branch, and a version tag broke the guess

[`Ed-Fi-Alliance-OSS/Ed-Fi-Data-Standard`](https://github.com/Ed-Fi-Alliance-OSS/Ed-Fi-Data-Standard) (`47★`) has `default_branch` **`v6.2.0`** — a version tag serving as the default branch. `main` and `master` both fail. 🟢 **`ACTION p762-B` is discharged in full for the first time**: the search channel returned an authoritative `default_branch` for all `53` addresses this pass, so none was guessed, and the one address that would have defeated a guess is the standards body's flagship repository. 🔵 See `INS-002` for what the same channel does **not** support.
