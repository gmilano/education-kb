## `2026-11-15` (thirty-third pass, `p828`) — **`6` foundation rows and `1` vertical platform, and the Brazilian cluster's upstream is found UNMAINTAINED**

🟢 **Foundations `142` → `148`; verticals `131` → `132`. Every licence byte-read on
`raw.githubusercontent.com`, `2026-11-15`.**

### Filed

| Repo | Licence | Why it is a foundation and not an agent |
|---|---|---|
| `labsai/EDDI` | Apache-2.0, `394★`, `132` forks | 🇩🇪 Config-driven agent engine: JSON becomes a running multi-agent service, 19+ providers, MCP/A2A, RAG, persistent state. 🟢 **The orchestration layer `P68` mounts the LMS adapters on, so no one has to write one** |
| `BrightspaceUI/core` | Apache-2.0, `81★` | 🇨🇦 **D2L's own** accessible web components — the supported route to a studio-built surface INSIDE the LMS rather than beside it |
| `GeovaneSchmitz/sigaa-api` | MIT, `61★`, `22` forks | 🇧🇷 **The upstream of the entire Brazilian SIGAA cluster.** 🔴 **Last push `2024-04-10` — ~`19` months stale** |
| `suap-ava-suite/djangoapp-integrador_ava` | MIT | 🇧🇷 SGA↔Moodle middleware: **SUAP** natively, generic profile for **SIGAA** and **Q-Acadêmico**. 🔴 Declared development-use-only at IFRN — a specification, not a deployable |
| `cyanheads/oecd-mcp-server` | Apache-2.0 | 1,500+ OECD statistical datasets over SDMX — a **first-hand** route to education indicators this base has had to cite second-hand |
| `SidneyBissoli/uis-mcp-server` | MIT | **Provenance-first** UNESCO UIS statistics: every figure carries its source, which is what makes a statistic usable in a client deliverable |

### The vertical, and why one row matters

🟢 **`Selleo/mentingo` (MIT, `109★`, `30` forks) is the only PERMISSIVELY-licensed LMS on this
shelf.** 🔴 Moodle, Open edX, Canvas, Chamilo and Frappe LMS are all GPL or AGPL, so a derived
platform is copyleft. 🟢 **An MIT, AI-native LMS can be forked and shipped commercially — a
strategic option rather than another row.**

### The risk worth naming

🔴 **The Brazilian tier's lineage traces to one unmaintained MIT library.**
`heitorsDev/sigaa-ifsc-mcp` states it ported its navigation and extraction from
`GeovaneSchmitz/sigaa-api`, which has not been pushed since `2024-04-10`. 🟢 **Adopting the tier
means inheriting it; maintaining it is a small, cheap, nameable deliverable that would make a
studio the de facto steward of the layer.**
