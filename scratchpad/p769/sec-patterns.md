## 🆕 `p769` — `P352`–`P357` — **school-estate decarbonisation and energy reporting: the first register whose artefact is a published figure, which breaks `P350` and needs a restatement axis to fix**

Every repository named below was byte-read for its grant this pass over a **complete git tree** (`agents/top.md`, `repos/foundations.md`). Grants: `SEED-platform/seed` BSD-3, `py-seed` MIT+BSD-3, `NatLabRockies/EnergyPlus` BSD-3, `NatLabRockies/OpenStudio` BSD-3, `NatLabRockies/alfalfa` BSD-3, `LBNL-ETA/EnergyPlus-MCP` BSD-3, `ugr-sail/sinergym` MIT, `santoshphilip/eppy` MIT, `building-energy/epw` MIT, `jkbrzt/rrule` BSD-3, `getodk/collect` Apache-2.0, `traccar/traccar` Apache-2.0, `BBSR-GEG-Portal/*` MIT, `ABC-TransitionBasCarbone/bilan-carbone` MIT, `energiacte/cteepbd` MIT, `jmcaamanog/CE3X-MCP-Server` MIT, `centrefornetzero/epc-ppd-address-matching` MIT, `buds-lab/energystar-plus-plus` MIT, `CarlosBeltranVelamazan/NBEM` MIT, `zehengl/yyc-building-energy-benchmarking` MIT.

### `P352`
**Global — the restatement-safe reporting ledger. This replaces `P350` for any duty whose artefact is a published figure, and `P350` must not be used for one.**

🔴 **The defect being fixed:** `P350` keys a compliance record on `(period, event)`. An inspection either happened or did not, so that key is sound. **A reported figure is restatable** — a meter is found miscalibrated, a floor area is corrected after a survey, a scope boundary moves when a sports hall is reclassified — and `(period, event)` **silently overwrites a number that has already been published to a regulator**.

🟢 **Wire:** the primary key becomes `(site, period, version, basis)`, where `basis` names the method edition and the source of every input.
- **Store:** `SEED-platform/seed` (**BSD-3**, `121★`) as the system of record — it already models datasets by compliance cycle and per-jurisdiction programmes; write through `SEED-platform/py-seed` (**MIT and BSD-3**).
- **Never `UPDATE` a published row.** Insert `version = n+1`, retain `n`, and require a non-null `restatement_reason` on any version above `1`. A published figure is append-only for the same reason this base's shelves are.
- **Cadence:** `jkbrzt/rrule` (**BSD-3**) holds the due dates, one rule per jurisdiction — `FREQ=YEARLY` for a UK DEC above `1,000 m²`, `FREQ=YEARLY;BYMONTH=7;BYMONTHDAY=31` for Japan's 定期報告, `FREQ=YEARLY` for a US benchmarking report, and a **dated milestone list rather than a recurrence** for Brazil's `2027`/`2035`/`2040` ratchet.
- 🔴 **Brazil is the reason the cadence layer needs two shapes.** A ratchet is not a recurrence: `rrule` cannot express *"level `A` from `2027`, NZEB from `2035`"*. Model it as a target schedule evaluated against the period, not as a repeat (`T704`).
- **Evidence:** `getodk/collect` (**Apache-2.0**) for the meter photograph, the nameplate and the floor-area check; each submission carries the `version` it supports.

🟢 **Acceptance test that makes this real:** restate a prior period, then assert that the regulator-facing export for the original period still reproduces the originally published figure byte for byte. **If it does not, the ledger is `P350` with extra columns.**

### `P353`
**North America — the multi-jurisdiction benchmarking engine, with the scoring authority kept behind an interface.**

🟢 **Wire:** `py-seed` → `SEED-platform/seed` as the portfolio store → a per-jurisdiction rule table (`threshold_sqft`, `report_due`, `disclosure_required`, `performance_standard`) → `jkbrzt/rrule` for the due dates → `zehengl/yyc-building-energy-benchmarking` (**MIT**) as the worked reference for the public dashboard layer.

🔵 **Why the rule table is the deliverable and not an afterthought:** Washington's Clean Buildings Phase 1 begins **`1 June 2026`** at `50,000 sq ft` and is reported to cover K-12 explicitly, Phase 2 drops to `20,000 sq ft` in `2028`; California AB 802 adds public disclosure; NYC LL97 and Maryland BEPS are reported to cover schools. **A district spanning three jurisdictions has three thresholds, three deadlines and three disclosure rules against one building list.**

🔴 **And keep the score behind an interface.** ENERGY STAR is reported to be moving out of the EPA as of March 2026. `buds-lab/energystar-plus-plus` (**MIT**) is a worked reimplementation of the 1–100 score: wire it as a *fallback and a cross-check*, not as the primary. **If Portfolio Manager becomes unavailable or changes hands, a deliverable with no second scorer has no product.**

🟢 **The build-gate assertion that belongs in this pattern's CI, not in its report:** if the deliverable compiles EnergyPlus from source, set **`-DEIGEN_MPL2_ONLY`**. Eigen's own `COPYING.README` states that this makes the build **fail** if any LGPL-licensed Eigen header is included. **That turns a licensing opinion into a build error** (`T709`).

### `P354`
**EMEA — build the directive, configure the member state. The pattern exists because the national law does not.**

🔴 **The constraint this pattern is designed around:** the EPBD recast's transposition deadline was `29 May 2026` and **the Commission opened infringement proceedings against all `27` member states on `15 July 2026`.** National thresholds, penalties and competent authorities are still moving.

🟢 **Wire:** `BBSR-GEG-Portal/webservice-fuer-energieausweise` + `druckapplication-fuer-energieausweise` (**MIT**, German federal institute) as the certificate service and renderer for a German engagement → `energiacte/cteepbd` (**MIT**) for the Spanish CTE calculation → `ABC-TransitionBasCarbone/bilan-carbone` (**MIT**, the method's owning body) for the French carbon balance → `jmcaamanog/CE3X-MCP-Server` (**MIT**) as the worked pattern for driving a certified national desktop tool from an agent → `centrefornetzero/epc-ppd-address-matching` (**MIT**) to join the estate list to the certificate register, which is the real first task.

🟢 **Hard-code only the EU-level dated obligations, which will not move:** solar on new public and non-residential buildings above `250 m²` by **`31 Dec 2026`**; national building renovation plans by **`31 Dec 2026`**; renovation-passport schemes due **`29 May 2026`**; **zero-emission standard for all new public buildings from `1 Jan 2028`**. 🔴 **Everything national — threshold, penalty, authority, assessor accreditation — is configuration.** A deliverable that hard-codes a member state's threshold today is hard-coding a draft.

🔴 **Refuse `ladybug-tools/honeybee-energy` (AGPL-3.0) in any hosted EMEA deliverable.** It is the stack a team will reach for by default because it is what the teaching material uses.

### `P355`
**APAC — Japan: the EEGS submission pipeline. The duty is the most precisely dated on the register and the local supply is zero, so this pattern is integration, not assembly.**

🟢 **Wire:** `NatLabRockies/OpenStudio` (**BSD-3**) for the model and its measure system → `santoshphilip/eppy` (**MIT**) to script the IDF → `building-energy/epw` (**MIT**) for weather normalisation → `traccar`-class time-series ingest for sub-metering → `jkbrzt/rrule` (**BSD-3**) encoding **two** statutory dates, not one: **エネルギー使用状況届出書 by the end of May** and **定期報告書 plus 中長期計画書 by the end of July** → an export shaped for **EEGS** electronic filing.

🔴 **The trigger is the pattern's distinguishing feature and it is not floor area.** 特定事業者 designation fires at **`1,500 kL` crude-oil equivalent per year**, aggregated across the operator's sites. 🟢 **So the data model must support an operator-level rollup that crosses the `1,500 kL` line, which no floor-area-triggered jurisdiction needs.** A school board below the threshold has no duty at all; one above it has an annual filing for the whole estate.

🟢 **MEXT (文部科学省) is the named competent ministry for schools** and publishes 学校のための省エネガイドブック (March 2025) — read it as the requirements document before designing the export. 🔴 **`0` open-source artefacts in Japanese were found across `7` query legs: there is no local component to adopt and no local convention to match.**

### `P356`
**LATAM — Brazil: the ENCE ratchet tracker. The only register duty on this base that is a multi-year target schedule rather than a repeat.**

🟢 **Wire:** a building inventory keyed by **federative level** (federal / state / district / municipal, because the deadline depends on it) → the ENCE target schedule as dated milestones: **federal public buildings at level `A` from `2027` and NZEB by `2035`** (`2040` for Rio Grande do Sul), **state and district level `A` reported `2032–2035`, NZEB `2037–2040`**, **municipalities above `50,000` inhabitants in a final phase to `2040`** → a current-class assessment per building → a **gap-to-target** report per milestone → `P352`'s ledger to hold the published class and its restatements.

🟢 **The commercial shape is better than any other region's, and it follows from the instrument.** A ratchet with named years means the client cannot do this once: every milestone is a re-assessment, procurement must require the labels, and a completed public building must **display the ENCE at its main entrance**, which makes the output visible and therefore politically owned.

🔴 **Two honest limits to state in any Brazilian proposal.** (1) **Resolução CGIEE nº 4/2025 does not name schools**; their inclusion follows from "public building" and should be confirmed against the resolution text before scoping. (2) **There is no permissive Brazilian code to build on** — `0` grant-carrying repositories across the Portuguese legs. The substrate is `P352` plus `P353`'s engine, localised; nothing is reusable from the local ecosystem.

### `P357`
**Global — the agentic layer, and the only honest way to wire it on a reporting duty.**

🟢 **Wire:** `LBNL-ETA/EnergyPlus-MCP` (**BSD-3**, `126★`) exposes the simulation engine as MCP tools → `NatLabRockies/alfalfa` (**BSD-3**) makes a running model interactive so the agent can act mid-simulation → `ugr-sail/sinergym` (**MIT**, `242★`) is the training and evaluation harness → `santoshphilip/eppy` (**MIT**) is the deterministic escape hatch for anything the agent should not be doing probabilistically → `P352`'s ledger receives every figure with its `basis`.

🔵 **The architecture both existing MCP servers chose, and it is the right one: the agent never performs the regulated calculation.** `EnergyPlus-MCP` wraps EnergyPlus; `CE3X-MCP-Server` wraps CE3X. **The certified engine stays certified, and the agent is responsible only for assembling inputs and drafting the narrative.**

🔴 **The boundary, stated as a rule:** an agent may propose a figure and must never be the figure's `basis`. The practitioner consensus read this pass is that automating a flawed input pipeline delivers **assured errors faster**, and that reasonable assurance brings scrutiny of the model itself — explainability and the basis for validation rules. 🟢 **So every agent-touched value in `P352` carries `basis = (engine, engine_version, input_provenance, human_signoff)`, and an export refuses to render a period where any value's `human_signoff` is null.** That refusal is the pattern's single most important line of code.

🔴 **Both MCP servers are six weeks old.** `EnergyPlus-MCP` was pushed `2026-11-04`, `CE3X-MCP-Server` `2026-10-29`. **Adopt them as an interface to pin and vendor, not as a stable dependency.**
