## 🆕 `p769` — **Eight trends for school-estate decarbonisation and energy reporting. The governing one is that the duty and the tooling have swapped places: the regulator now ships more usable open source than the community does, and on this register the thing missing is not the engine but the submission.**

### 🟢 `T-a` — The regulator is now an upstream, and that is new

🟢 **The German federal institute BBSR publishes the statutory energy-certificate web service and print application under MIT, with its own name filled into the copyright line.** The US DOE funds BSD-3-Clause EnergyPlus, OpenStudio, SEED and alfalfa. LBNL ships the register's only MCP server under a modified BSD. 🔵 **Across `p765`–`p768` the pattern was the opposite: the duty was defined by a paid standards body and the open-source layer was community-built and copyleft.** Here the regulator is the most permissive publisher in the vertical, and a studio's first search should be the regulator's GitHub organisation, not a topic query.

### 🟢 `T-b` — Agents arrived on this register in the last six months, and they arrived as tool servers

🟢 **`LBNL-ETA/EnergyPlus-MCP` (`126★`, pushed `2026-11-04`) and `jmcaamanog/CE3X-MCP-Server` (pushed `2026-10-29`) are both MCP servers over a *regulator-sanctioned calculation tool*.** 🔵 **Neither tries to replace the calculation; both wrap it so a model can drive it.** That is the correct architecture for a compliance deliverable — the certified engine stays certified, and the agent is responsible only for the inputs and the narrative. **It also means the agent layer on this register is six weeks old**, and a studio adopting it is adopting an alpha-stage interface over a stable engine.

### 🔴 `T-c` — Automation of a reporting duty produces assured errors faster

🔴 **The consistent warning across the practitioner sources read this pass is that automating a flawed input pipeline delivers *assured* errors, not fewer errors**, and that reasonable assurance brings scrutiny of the AI models themselves — explainability and the basis for validation rules. 🟢 **The engineering consequence is specific: on a reporting duty the agent's output must carry its provenance to the figure, because the audit question is not "what is the number?" but "where did this number come from and who signed it?"** `P352` makes the `(period, version, basis)` triple the primary key for exactly this reason.

### 🔴 `T-d` — The EMEA duty is in force and untransposed, which is a worse state than either

🔴 **The EPBD recast's transposition deadline was `29 May 2026`; on `15 July 2026` the Commission opened infringement proceedings against all `27` member states.** An earlier March 2026 action covered `19` member states over draft National Building Renovation Plans. 🔵 **A directive in force with no national transposition means the obligation is certain and its national detail is not** — thresholds, penalties and the competent authority are all still moving. 🟢 **The posture that survives: build the EU-level dated obligations, keep national parameters as configuration.**

### 🔵 `T-e` — The scoring authority is a dependency, and in North America it is a wobbling one

🔴 **ENERGY STAR is reported to be moving out of the EPA as of March 2026, with at least `$33M` appropriated for FY2026.** Portfolio Manager is the instrument that dozens of city and state ordinances name *by product*. 🔵 **A deliverable that treats the 1–100 score as a primitive is coupled to a federal programme's organisational chart.** 🟢 `buds-lab/energystar-plus-plus` (MIT) matters here beyond its `9★`: it is a worked reimplementation of the score, which is what makes the score an interface rather than a dependency.

### 🟢 `T-f` — A reporting duty is restatable and an inspection duty is not; this breaks the shared data model

🟢 **The structural result of this pass.** Four previous registers produced inspection duties, whose records are immutable once signed. This register produces *published figures*, which get restated — a meter is found miscalibrated, a floor area is corrected, a scope boundary moves. 🔴 **`P350`'s `(period, event)` model silently overwrites the published number.** 🟢 **`P352` replaces it with `(period, version, basis)`, retains the superseded figure and records the restatement reason.** `p768-F` predicted this failure mode by name before the register was built.

### 🟢 `T-g` — Corporate sustainability reporting is contracting while building-law reporting ratchets

🔴 The CSRD **Omnibus** raised thresholds to **`>1,000` employees and `>€450M` turnover from FY2027**; one vendor-adjacent source puts the reduction at roughly **`85%` of previously covered companies** (single-source, not endorsed). 🔵 Meanwhile Brazil's ratchet runs `2027 → 2035 → 2040`, the EU's zero-emission public building rule starts `1 Jan 2028`, and Washington's K-12 phase starts `1 June 2026`. 🟢 **The two curves diverge, and the school estate sits on the rising one: its duty comes from building law, not corporate reporting law.** **For a studio choosing where to invest, the public estate is the more durable buyer** (`T714`).

### 🔴 `T-h` — Open-source supply in a buyer's own language tracks grant *quality*, not result *volume*

🔴 **`ACTION p768-E`'s predictor, tested as recorded and FALSIFIED as stated.** The prediction written before any query ran was that German and French would be the two richest legs because the certificate register is published by a public body in both, and that Japanese would be medium for the same reason.

| Leg | Predicted | Measured | Outcome |
|---|---|---|---|
| **French** | RICH | `24`/`21`/`15`/`13`/`80`/`2`/`2`, with MIT grants from the method's own owner | 🟢 **Held** |
| **German** | RICH | `11`/`1`/`1`/`0`/`1`/`0`/`0` — near-nil by count, **but the only federal-institute MIT grants on the register** | 🔴 **Failed on volume, held on quality** |
| **Japanese** | MEDIUM | 🔴 **`0` across all `7` legs**, though the data owner is a ministry | 🔴 **Failed outright** |
| **Spanish `huella de carbono`** | MEDIUM | `450` results, almost entirely coursework, `0` usable grants | 🔴 **Failed in the opposite direction** |

🟢 **The refinement that survives the falsification: a public-body data owner predicts the PRESENCE of a permissive grant, not the SIZE of the result set — and volume and usability are anti-correlated.** The German leg returned `15` repositories total and the register's two best rows; the Spanish leg returned `450` and nothing. 🔴 **Japan falsifies even the refined form, and the exception is itself informative: Japan's ministries publish the duty, the guidance and the filing portal, and publish no code at all.** Whether a public body publishes *software* is a cultural fact about that institution, not a consequence of its owning the data (`T717`, `ACTION p769-A`).
