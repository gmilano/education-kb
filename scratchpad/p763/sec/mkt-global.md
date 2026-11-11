#### 🆕 p763 — the measuring layer is permissive, the layer that holds the record is copyleft, and the best-known open LRS has been stale for `18` months

**Register: the education data warehouse and the statutory return.**

🟢 **UNESCO's framing makes this register the global one.** The UIS operational guide states that EMIS play the largest role in generating SDG 4 monitoring data from administrative sources, and national EMIS data reaches UIS through annual statistical surveys consolidated nationally. 🔴 **SDG 4 indicator coverage stands at `60%` across `205` countries** (UIS 2025), attributed partly to gaps in collection, quality and reporting — which is this register's problem statement, stated by the custodian of the indicators.

🔴 **The governing licence structure, byte-read on `47` payloads this pass, and it is p757's law again.** Everything that *defines, measures, moves or validates* the data is permissive. Everything that *holds the student record* is copyleft.

| Layer | Representative, byte-read `2026-11-11` | Grant |
|---|---|---|
| Standard / schema / warehouse | [`CEDStandards/CEDS-IDS`](https://github.com/CEDStandards/CEDS-IDS) `51★` · [`CEDStandards/CEDS-Data-Warehouse`](https://github.com/CEDStandards/CEDS-Data-Warehouse) `35★` · [`Ed-Fi-Alliance-OSS/Ed-Fi-Data-Standard`](https://github.com/Ed-Fi-Alliance-OSS/Ed-Fi-Data-Standard) `47★` | 🟢 **Apache-2.0** `5/5` and `9/9` |
| Telemetry spec and store | [`adlnet/xAPI-Spec`](https://github.com/adlnet/xAPI-Spec) `955★` · [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) `144★` · [`adlnet/ADL_LRS`](https://github.com/adlnet/ADL_LRS) `335★` | 🟢 **Apache-2.0** |
| Conformance | [`adlnet/lrs-conformance-test-suite`](https://github.com/adlnet/lrs-conformance-test-suite) `78★` `1,046 B` / `c0fc02a86ae2` | 🟢 **MIT** |
| Record linkage | [`moj-analytical-services/splink`](https://github.com/moj-analytical-services/splink) `2,572★` | 🟢 **MIT** |
| **The national record system** | [`OpenEMIS/core`](https://github.com/OpenEMIS/core) `24★`, `15,518 B` / `b6f03c6715ee` | 🔴 **GPL-2.0** |
| **The best-known open LRS** | [`LearningLocker/learninglocker`](https://github.com/LearningLocker/learninglocker) `586★`, `35,141 B` / `589ed823e9a8` | 🔴 **GPL-3.0**, last pushed **`2024-05-30`** |

🔴 **Liveness is the hidden risk on this register, and it is measurable.** Of adlnet's top `20` xAPI repositories, **`11` are archived**. [`adlnet/xAPI-Spec`](https://github.com/adlnet/xAPI-Spec) (`955★`, the largest repository on register) was last pushed `2025-07-03`. **`adlnet/tla` — the Total Learning Architecture — is archived and Unlicense.** The best-known open LRS is `18` months stale. 🟢 **The live permissive alternatives exist and are named**: `yetanalytics/lrsql` (Apache-2.0, pushed `2026-11-08`) and `adlnet/ADL_LRS` (Apache-2.0) (`T611`).

🟢 **OpenEMIS is the register's government-owned EMIS and it is real**: a March 2026 concept note extends it to early-childhood tracking against SDG 4.2. 🔴 **Its only agent-layer clients are not open source** — see `T607`.

🔵 **Market figures carried and labelled, not re-derived:** AI-in-education at **`$10.6B` (2026) → `$42.48B` (2030)** at a `41.5%` CAGR, against an alternative `$9.58B` base — market-research and vendor material, and the spread is the finding. North America holds roughly `38%` of revenue. `86%` of education organisations report using generative AI (Microsoft 2025, via Faculty Focus). 🔴 **Only `45%` of the most-used tools have published research meeting an ESSA evidence tier** — which is a procurement argument for this register, because the evidence has to come out of the warehouse. The OECD *Digital Education Outlook 2026* holds that AI helps learning only where pedagogy stays in control.
