## 🆕 2026-11-11 (p763) — **The education-data agent layer was built in the last nine months, is spread across five regions, and tops out at `13` stars — and every single artefact reads statistics that are already published. The standards body shipped Agent Skills for coding assistants yesterday. And the only OpenEMIS agents in existence are Business Source Licence 1.1, under a licence that names a different repository than the one it sits in.**

**Register: the education data warehouse and the statutory return — where telemetry lands, who answers for it, and the dated annual report that is the deliverable** · `10` agent rows filed of which `8` are usable in a proprietary deliverable, `4` refusals named, `1` byte-identical copy recorded · `53` addresses resolved · **`47` licence payloads byte-read** · `6` no-payload addresses of which **`3` were refuted by a manifest probe**, `3` published as absences · `1` p762 control reproduced exactly · `T604`–`T614`.

### The week's shelving finding: `ACTION p760-A` has discharged three times running, each time on a bigger buyer

Counted across these eight shelves with word boundaries, before this pass: `LTI` **`1,633`** · `xAPI` **`1,109`** · `OneRoster` **`645`** · `1EdTech` **`638`** · `SIS` **`635`** · `SCORM` **`598`** · `Ed-Fi` **`533`** · `Caliper` **`402`** · `LRS` **`354`** — against `SLDS` **`0`** · `institutional research` **`0`** · `P20W` **`0`** · `EDFacts` **`0`** · `accountability reporting` **`0`** · `unique student identifier` **`0`** · `record linkage` **`0`** · `data warehouse` **`1`**.

🔵 **This base has held every protocol for moving a student record and almost nothing about the warehouse it lands in or the return that is computed from it.** The return is a funding instrument: Brazil transmits to the FNDE on **`2026-12-11`** and federal money for roughly `40` million students follows it.

### 🟢 New this week, and it is the most on-register agent artefact that exists

[`Ed-Fi-Exchange-OSS/Ed-Fi-SDK-for-AI-Assistants`](https://github.com/Ed-Fi-Exchange-OSS/Ed-Fi-SDK-for-AI-Assistants) — **Apache-2.0**, `11,357 B` / `c71d239df917` from `main`, `1★`, **pushed `2026-11-10`**, copyright Ed-Fi Alliance, LLC. It ships a `skills/` folder of **Agent Skills** (agentskills.io) that give AI coding assistants — Claude Code and GitHub Copilot are the named examples — Ed-Fi-specific guidance when building API clients. **Not an MCP server and no LLM named.** It appeared during the Alliance Summit (`2026-11-09`–`11`, Nashville). 🟢 **A standards body is now publishing skills for coding assistants, which is the cheapest possible accelerator for a studio that would otherwise re-derive the data standard by hand.**

Also live this week on the same register: [`Ed-Fi-Alliance-OSS/Data-Management-Service`](https://github.com/Ed-Fi-Alliance-OSS/Data-Management-Service) (Apache-2.0, pushed **`2026-11-11`**), [`Ed-Fi-Alliance-OSS/edfi-oneroster`](https://github.com/Ed-Fi-Alliance-OSS/edfi-oneroster) (Apache-2.0, `2026-11-06`), [`Hug0x0/mcp-french-school-map`](https://github.com/Hug0x0/mcp-french-school-map) (MIT, `2026-11-06`), [`malkreide/swiss-statistics-mcp`](https://github.com/malkreide/swiss-statistics-mcp) (MIT, `2026-11-07`) and [`csmediapro/moodle-mcp-server`](https://github.com/csmediapro/moodle-mcp-server) (AGPL-3.0, `2026-11-07`).

### 🔵 The agent layer, placed by region — and the gap it leaves

| Region | Artefact | Grant, byte-read `2026-11-11` | Reads |
|---|---|---|---|
| EMEA | [`isakskogstad/Skolverket-MCP`](https://github.com/isakskogstad/Skolverket-MCP) `13★` | MIT · `1,093 B` / `7935973493aa` | Swedish National Agency for Education syllabus data |
| EMEA | [`malkreide/swiss-statistics-mcp`](https://github.com/malkreide/swiss-statistics-mcp) `2★` | MIT · `1,069 B` / `ac1fc40e61a6` | Swiss federal statistics |
| EMEA | [`Hug0x0/mcp-french-school-map`](https://github.com/Hug0x0/mcp-french-school-map) `0★` | MIT · `1,063 B` / `59557cd648d7` | French school directory |
| APAC | [`hkopenai/hk-education-mcp-server`](https://github.com/hkopenai/hk-education-mcp-server) `1★` | MIT · `1,070 B` / `473af2606a25` | Hong Kong open education data |
| APAC | [`andikadevs/pddikti`](https://github.com/andikadevs/pddikti) `2★` | 🔴 AGPL-3.0 · `34,523 B` / `0d96a4ff68ad` | Indonesia's higher-education national database |
| North America | [`lisaguthrie/wa-ed-mcp`](https://github.com/lisaguthrie/wa-ed-mcp) `1★` | 🔴 **no grant at `17` paths, no manifest declaration** | Washington State education data |
| North America | [`Ed-Fi-Exchange-OSS/Ed-Fi-SDK-for-AI-Assistants`](https://github.com/Ed-Fi-Exchange-OSS/Ed-Fi-SDK-for-AI-Assistants) `1★` | 🟢 Apache-2.0 · `11,357 B` / `c71d239df917` | — (developer-side skills) |
| Global | [`yifnli/uis-sdg4-mcp`](https://github.com/yifnli/uis-sdg4-mcp) `2★` | ⚠️ MIT by `pyproject.toml`, **no `LICENSE` file** | UNESCO UIS SDG 4 indicators |
| Global | [`malkreide/global-education-mcp`](https://github.com/malkreide/global-education-mcp) `1★` | MIT · `1,069 B` / `ac1fc40e61a6` 🔵 byte-identical to the Swiss row, same author | Global education indicators |
| LATAM | 🔴 **nothing** | — | `censo escolar inep microdados` → `total_count 12`, max `3★`; the Spanish-language probe → **`0`** |

🔴 **Every usable row reads data that has already been published. Not one writes to a student record, validates a return against a schema, or reconciles a correction window** — which is the work with the deadline and the budget (`T610`).

### 🔴 The week's worst landmine: a Business Source Licence that names the wrong artefact

[`tixuz/openemis-mcp`](https://github.com/tixuz/openemis-mcp) (`4★`) and [`tixuz/openemis-mcp-pro`](https://github.com/tixuz/openemis-mcp-pro) (`2★`) carry **byte-identical** `LICENSE.md` at **`647 B` / `4dead97d8aaf`**, both indexed `NOASSERTION`. It is **BSL 1.1** — not an open-source licence. Additional Use Grant: *"non-production evaluation and internal testing only."* The text: you *"may not offer the Licensed Work as a commercial hosted service or embed it in a commercial product without a separate commercial licence."* Change Date `2029-01-01`, Change License MIT. 🔴 **And in both files the `Licensed Work:` field reads `openemis-mcp-pro`**, so the free repository's coverage is undetermined on the face of its own instrument. These are the only agents for UNESCO's ministry EMIS that exist (`T607`).

### 🔴 And the most-starred early-warning model for schools forbids selling a service

[`dssg/student-early-warning`](https://github.com/dssg/student-early-warning) (`70★`, index `NOASSERTION`) byte-reads at **`2,069 B` / `11f9627267d7`** as a University of Chicago grant limited to *"academic research or other not-for-profit scholarly purposes"*, which *"excludes any service or part of selling a service that uses the Program."* The same clause sits on [`dssg/police-eis`](https://github.com/dssg/police-eis) (`1,979 B`) and on p762's [`workforce-data-initiative/skills-ml`](https://github.com/workforce-data-initiative/skills-ml) (`1,976 B`, **re-measured as a control and reproduced exactly**). 🟢 **The usable half of the finding**: the lab's generic pipeline, [`dssg/triage`](https://github.com/dssg/triage) (`202★`), is **verbatim MIT** at `1,176 B` / `e3f05dfc649c` — and is *also* indexed `NOASSERTION`, because one attribution line sits above the title. 🟢 **Take the pipeline, never the model** (`T606`).
