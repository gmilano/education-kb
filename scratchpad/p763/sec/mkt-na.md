#### 🆕 p763 — the federal programme that funds this register is flat at `$28.5M`, has reached every state, and has **`0`** repositories carrying its name

**Register: the education data warehouse and the statutory return** — where learning telemetry lands, who is accountable for it, and the report that is the actual deliverable.

🟢 **The demand side is appropriated and named.** The Statewide Longitudinal Data Systems grant programme is funded at **`$28.5` million** in FY26 with the Workforce Data Quality Initiative at **`$6` million**, both unchanged from the prior year (Data Quality Campaign — **search-sourced; `dataqualitycampaign.org` is outside this session's allowed network domains and could not be primary-verified**). Across eight rounds of SLDS funding, **`50` states, `5` territories and the District of Columbia** have received at least one grant (NCES). IES's special-education SLDS-use competition (**`84.324S`**) took letters of intent by `2026-09-03` and applications by **`2026-10-01`**, with awards to **`$1,200,000`** — a research competition requiring SLDS data, not a warehouse build.

🔴 **And the supply side carries the programme's name zero times.** `statewide longitudinal data system` on the repository-search channel returns **`total_count 0`** (`T604`). The reference implementation is real, permissive and findable only under a different name: [`CEDStandards/CEDS-IDS`](https://github.com/CEDStandards/CEDS-IDS) — the Common Education Data Standards **Integrated Data Store** — `51★`, Apache-2.0 byte-read at `11,357 B` / `c71d239df917` from `master`.

| North America, measured `2026-11-11` | Value |
|---|---|
| SLDS programme, FY26 | **`$28.5M`** flat · WDQI `$6M` flat (search-sourced) |
| States reached, 8 rounds | `50` states + `5` territories + DC |
| `statewide longitudinal data system` repositories | **`0`** |
| CEDS estate | `5` repositories, **`5 / 5` Apache-2.0**, all byte-read |
| Ed-Fi adoption | **more than a quarter of US states**; a third-party list names `14` and is **not** verified against an Ed-Fi source |
| Ed-Fi OneRoster early adoption | **`9` agencies, `4.5M+` students**; SEA commitments for SY26-27 |
| Utah SLDS | **`$2.2M`** projected funding loss on its four-year project; system sits in the Utah Data Research Center |

🟢 **The vendor-side event ran as this pass was written.** The Ed-Fi Alliance Summit was held **`2026-11-09` to `2026-11-11`** in Nashville. Its Spring 2026 release carried Data Standard `v6.1`, ODS/API `v7.3.2`, the Ed-Fi OneRoster Service and MetaEd `v4.7`, with a move to .NET 10 ahead of .NET 8 end-of-support in November 2026, and the roadmap flags a **PII flag for AI discovery** in the `6.x` line. 🔴 **No Summit outcome is indexed yet and none is published here** — the event closed the day this pass ran.

🔴 **The architectural constraint comes from the standard's own authors.** Ed-Fi's May 2026 white paper *"The Ed-Fi Data Standard in the Age of AI"* recommends that **AI and analytics systems should not interact directly with the Ed-Fi API** (search-sourced; `docs.ed-fi.org` is outside this session's allowed domains). Every pattern this pass filed reads a warehouse replica instead (`T609`).

🔴 **The region's own refusal, named.** [`dssg/student-early-warning`](https://github.com/dssg/student-early-warning) (`70★`) is the most-starred open early-warning model for US schools and its licence byte-reads at `2,069 B` / `11f9627267d7` as a University of Chicago research grant that **"excludes any service or part of selling a service that uses the Program"** (`T606`).
