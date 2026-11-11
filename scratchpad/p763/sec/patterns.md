## 🆕 `P311`–`P317` — added at p763 (2026-11-11)

**Register: the education data warehouse and the statutory return** — the warehouse telemetry lands in, the office accountable for it, and the dated annual report that is the actual deliverable. Every component named below was byte-read for its licence on `2026-11-11`, **every licence was read from the branch the search channel reported as `default_branch`, and the branch is named** (`ACTION p762-B`).

🔴 **The governing design constraint comes from the standard's own authors**: Ed-Fi's May 2026 white paper recommends that AI and analytics systems **not** interact directly with the Ed-Fi API (`T609`). Every pattern below therefore reads a warehouse replica and lands data into it through a published connector. 🔴 **The second constraint: there is no open-source statutory-return system in any region at any licence**, so each of these is a composition, not a fork.

---

### `P311` — The statutory-return rehearsal harness

**The problem.** The return is annual, dated and has no retry: Brazil transmits to the FNDE on **`2026-12-11`**, the UK School Workforce Census is due **`2026-12-04`**, India's UDISE+ 2026-27 entry closed **`2026-09-30`**. A school system discovers its data defects when the window is closing.

**Wire it.** [`CEDStandards/CEDS-Data-Warehouse`](https://github.com/CEDStandards/CEDS-Data-Warehouse) (Apache-2.0, `master`, `11,357 B`/`c71d239df917`) for the dimensional schema → [`CEDStandards/CEDS-Elements`](https://github.com/CEDStandards/CEDS-Elements) (Apache-2.0, `master`) to express every statutory field as a named element → [`duckdb/duckdb`](https://github.com/duckdb/duckdb) (MIT, `main`, `1,072 B`/`075c33400ffc`) as the local rehearsal engine, so last year's homologated return is replayed on a laptop with no production access → [`yetanalytics/datasim`](https://github.com/yetanalytics/datasim) (Apache-2.0, `master`) to synthesise telemetry at volume where real student data may not be touched → [`dagster-io/dagster`](https://github.com/dagster-io/dagster) (Apache-2.0, `master`, `11,348 B`/`e25b0c5be442`) to schedule the rehearsal against the published deadline rather than against a cron guess.

**Deliverable.** A dated dry-run report naming every field that would fail validation, produced weeks before the window. 🟢 **Sell it against the calendar, not against the technology** — the buyer already knows the date.

---

### `P312` — Read-only agent over the warehouse replica, never over the transactional API

**The problem.** The naive build points an agent at the Ed-Fi ODS/API. The Alliance's own guidance says not to (`T609`), and the PII flag arriving in the `6.x` line exists because of it.

**Wire it.** [`Ed-Fi-Alliance-OSS/Ed-Fi-Kafka-Connect`](https://github.com/Ed-Fi-Alliance-OSS/Ed-Fi-Kafka-Connect) (Apache-2.0, `main`) **or** [`Ed-Fi-Alliance-OSS/Ed-Fi-API-Publisher`](https://github.com/Ed-Fi-Alliance-OSS/Ed-Fi-API-Publisher) (Apache-2.0, `main`) to land records out of the ODS → [`CEDStandards/CEDS-IDS`](https://github.com/CEDStandards/CEDS-IDS) (Apache-2.0, `master`) as the integrated store the agent is allowed to read → [`CEDStandards/CEDS-Ontology`](https://github.com/CEDStandards/CEDS-Ontology) (Apache-2.0, `main`) as the semantic layer, so the agent resolves *"chronically absent"* to a defined element rather than guessing a column → [`apache/superset`](https://github.com/apache/superset) (Apache-2.0, `master`, `11,585 B`/`ff254eb676d6`) for the human surface.

**For the build itself:** install [`Ed-Fi-Exchange-OSS/Ed-Fi-SDK-for-AI-Assistants`](https://github.com/Ed-Fi-Exchange-OSS/Ed-Fi-SDK-for-AI-Assistants) (Apache-2.0, `main`, pushed `2026-11-10`) — Agent Skills that give Claude Code or GitHub Copilot Ed-Fi-specific guidance while writing the client. 🟢 **The standards body publishes skills for coding assistants; a studio that ignores them is re-deriving the data standard by hand.**

---

### `P313` — Student identity resolution without a national identifier

**The problem.** The P20W join — school to college to workforce — is the entire purpose of the SLDS programme, and these shelves held `record linkage` and `unique student identifier` at **`0`**. Names change, dates of birth are mistyped, and there is no national student number in most jurisdictions.

**Wire it.** [`moj-analytical-services/splink`](https://github.com/moj-analytical-services/splink) (**MIT**, `master`, `1,076 B`/`b985d2c0fca6`, `2,572★`, UK Ministry of Justice, pushed `2026-11-11`) as the linkage engine → [`nhsengland/NHSE_probabilistic_linkage`](https://github.com/nhsengland/NHSE_probabilistic_linkage) (**MIT**, `main`, `1,068 B`/`bc445c79fdfe`) as the worked public-sector reference for parameter choice and clerical review → land the resolved identity into `CEDS-IDS`.

🔴 **Do not reach for [`kosukeimai/fastLink`](https://github.com/kosukeimai/fastLink)** (`294★`): it is the better-known academic package and it is **GPL(>= 3)**, declared in `DESCRIPTION` with no `LICENSE` file at `17` paths. 🟢 **Both permissive components are government-authored, which is the procurement argument as much as the licence is.**

---

### `P314` — A telemetry landing zone that is permissive end to end

**The problem.** The default answer is Learning Locker, which is **GPL-3.0** and was last pushed `2024-05-30` (`T611`).

**Wire it.** [`yetanalytics/lrsql`](https://github.com/yetanalytics/lrsql) (Apache-2.0, `main`, `11,357 B`/`c71d239df917`, pushed `2026-11-08`) as the store → [`yetanalytics/xapipe`](https://github.com/yetanalytics/xapipe) (Apache-2.0, `main`) to forward statements into the warehouse rather than query the LRS in anger → [`adlnet/lrs-conformance-test-suite`](https://github.com/adlnet/lrs-conformance-test-suite) (**MIT**, `master`, `1,046 B`/`c0fc02a86ae2`) as the **acceptance gate written into the statement of work** → [`adlnet/CATAPULT`](https://github.com/adlnet/CATAPULT) (Apache-2.0, `main`) where cmi5 course packaging is in scope.

🟢 **The conformance suite is the commercially useful part**: it converts "the LRS works" into a passing test run a client can re-execute. 🔴 Treat [`adlnet/xAPI-Spec`](https://github.com/adlnet/xAPI-Spec) as the normative reference it is, not as a live dependency — `955★` and last pushed `2025-07-03`.

---

### `P315` — One rostering endpoint instead of two integrations

**The problem.** A district runs Ed-Fi for state reporting and OneRoster for application provisioning, and pays to maintain both seams.

**Wire it.** [`Ed-Fi-Alliance-OSS/edfi-oneroster`](https://github.com/Ed-Fi-Alliance-OSS/edfi-oneroster) (Apache-2.0, `main`, pushed `2026-11-06`) to serve OneRoster 1.2 natively from the Ed-Fi store — shipped in ODS/API `7.3.2`, with early adoption reported at **`9` agencies and `4.5M+` students** → [`googleworkspace/oneroster-integration-conformance-tests`](https://github.com/googleworkspace/oneroster-integration-conformance-tests) (Apache-2.0, `main`) as the conformance gate.

🔴 **Avoid [`oat-sa/oneroster-import`](https://github.com/oat-sa/oneroster-import)** (**GPL-2.0**, `18,026 B`/`39db8f9acf03`) inside a proprietary deliverable. 🟢 **The sell is the retirement of an integration, which is an operating-cost line the buyer can already see.**

---

### `P316` — A ministry-statistics agent that respects the data licence as well as the code licence

**The problem.** Nine agent artefacts on this register wrap published statistics (`T610`) and the pattern is clearly replicable per country — but the code licence is not the only licence in play.

**Wire it.** Follow [`isakskogstad/Skolverket-MCP`](https://github.com/isakskogstad/Skolverket-MCP) (**MIT**, `master`, `1,093 B`/`7935973493aa`, `13★`): wrap the national statistics API as an MCP server, keep the code permissive, and ship the indicator semantics with it.

🔴 **And carry the data terms separately.** [`yifnli/uis-sdg4-mcp`](https://github.com/yifnli/uis-sdg4-mcp) shows the trap precisely: the code is MIT by `pyproject.toml` declaration — with **no `LICENSE` file at `17` paths despite a README that points to one** — while the README also states that data obtained through it is *"subject to UIS data terms of use"*. 🟢 **A statistics agent inherits two grants, and only one of them is in the repository.** Record both in the engagement's licence register.

🔵 **Deliberately bounded**: this pattern serves analysts reading published aggregates. It is **not** a path into the student record, and it must not be sold as one.

---

### `P317` — The component licence gate this pass's own instrument requires

**The problem.** Three of this pass's six "no grant" verdicts were wrong, and the index reported `NOASSERTION` across a usable MIT grant, a research-only grant and a Business Source Licence in the same batch.

**Run it, in this order, before shelving any component.**
1. **Resolve `default_branch` from the search channel — never guess.** It fired this pass on `Ed-Fi-Data-Standard`, whose default branch is the tag `v6.2.0` (`T614`).
2. **Probe the `LICENSE` family** across `LICENSE`/`LICENCE` × `{,.md,.txt,.TXT,.rst}`, `COPYING`, `NOTICE`, `LICENSE-APACHE`, `LICENSE-MIT`, in both cases.
3. 🔴 **Then probe the language manifest** — `DESCRIPTION` (R), `pyproject.toml`, `package.json`, `Cargo.toml`, `composer.json`, and plugin source headers such as Moodle's `version.php`. **This step corrected `50%` of this pass's no-grant verdicts** (`INS-001`).
4. **Read the payload bytes and record length with sha256₁₂** — and 🔴 **never key identity on the length**: three distinct payloads sat at exactly `11,357 B` this pass (`T605`, `ACTION p762-A`).
5. **Read the whole payload, not the title line.** A file titled `MIT License` can carry a Commons Clause (p761) and a file titled `Business Source License 1.1` can name a different repository as its licensed work (`T607`).
6. 🔴 **Never record `NOASSERTION` or "no licence file" as a licence state** (`ACTION p761-C`).

🟢 **Deliverable: a per-engagement licence register whose every row cites a byte count, a hash and the branch it was read from.** On this register that is not bureaucracy — three of the components a studio would reach for first forbid selling a service.
