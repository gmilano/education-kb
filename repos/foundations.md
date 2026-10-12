---
industry: education
region: Global
updated: 2026-10-12
---

## Pass 148 — 2026-10-12 — the foundational Rust row gets a bidirectional pin, and the `NOT_SHIPPED` rule fails as a general rule

🟢 **The clone and `npm pack` channels are both open** (`T65`), so this page's figures are
re-measured from the payload rather than carried.

### 🟢 `zavora-ai/mcp-student-records` — promoted to the strongest pin on the shelf

🟢 **`ACTION EO` and `ACTION EP` both discharge with silent falsifiers.** This row is the
first on this shelf whose declared tool manifest and whose actual router are proved **equal
as sets**, by an instrument that reads its language.

| property | value | how it is known |
|---|---|---|
| repo | [`zavora-ai/mcp-student-records`](https://github.com/zavora-ai/mcp-student-records) **v1.2.0** | clone, this pass |
| licence | 🟢 **Apache-2.0** | full body at `LICENSE`; `Cargo.toml` declares it |
| language | Rust, edition 2024, `rust-version = 1.94.1` | `Cargo.toml` |
| SDK | `rmcp` **3.1.2** + `adk-mcp-sdk` **0.2.0** | `Cargo.toml` |
| 🟢 **router surface** | 🟢 **46** | `#[tool(` sites inside `#[tool_router] impl StudentServer`, `src/server.rs`, brace-tracked |
| 🟢 **declared surface** | 🟢 **46** | `mcp-server.toml`, 46 `[[tools]]` |
| 🟢 **set identity** | 🟢 **PROVED** | symmetric difference empty both ways; **0** duplicates either side; order identical |
| approval-gated writes | **23 of 46** | `requires_approval = true` |
| risk classes | `read_only` / `internal_write` / `ExternalWrite` | typed per tool in the manifest |
| compliance posture | 🟢 **FERPA-gated communications + a FERPA access log** | `get_access_log` tool; package description |
| 🔴 **what the repo itself asserts** | 🔴 **the COUNT only** | `tests/manifest_test.rs`: `len() == 46`, `domain`, `requires_approval` on 11 named writes. 🔴 **No set comparison** |

🔵 **`P144-G` closes at 4 of 4.** The three earlier bidirectional pins were a SHA-256
lockfile (`malkreide/global-education-mcp`, 10), a classification manifest
(`oliverhruby/edupage-mcp`, 31) and a golden name array
(`divyarthjain/vtop-bhopal-mcp`, 17). 🆕 **The fourth is a typed TOML manifest with a risk
class per tool, and it is the only one of the four where the pin is a governance artefact
rather than a test fixture.** 🔴 **It is also the only one of the four the repository does
not verify itself.**

🟢 **For a studio, this is the row to start a records layer on**, and the caveat is one
sentence: the manifest is a contract the code happens to satisfy today, and nothing in CI
stops it drifting. [`p148-rust-surface`](../compose/code/p148-rust-surface/README.md) is the
check to vendor into a build — **14 tests**, offline, no network.

### 🔴 `ACTION EV` — the manifest allowlist cannot replace the name list, and the reason is worse than coverage

`ACTION EC` (p147) found the `NOT_SHIPPED` rule already written in `librus-mcp`'s own
`pyproject.toml`, and `T39` was vindicated. 🔴 **`ACTION EV` asked whether that generalises.
It does not.**

| verdict | n of 16 | meaning |
|---|---|---|
| 🟢 `ALLOWLIST` | **5** | a manifest include allowlist exists and was read |
| 🔴 `MANIFEST_NO_ALLOWLIST` | **7** | a manifest exists and declares no allowlist |
| 🔴 `NO_MANIFEST` | **3** | no package manifest of any kind |
| 🔴 `NO_ALLOWLIST_CONCEPT` | **1** | 🔴 **the manifest CANNOT express one** — `go.mod`; the module is the unit |

🔴 **5 of 16. The falsifier fires by eleven rows.** 🔵 **And `NO_ALLOWLIST_CONCEPT` is the
row that makes this structural rather than incidental**: `Agso-o/sigaa-calendar` is Go, and
no amount of author diligence would give it an include allowlist, because the format has no
such key. 🟢 **That is `T39` one level up — a property-based exclusion is sound only where
the property exists** — and it means the name list stays as a fallback, as the action's
consequence clause specified.

| row | allowlist | items | source |
|---|---|---|---|
| `krzysztofbury/librus-mcp` | 🟢 yes | **1** | `pyproject.toml [tool.hatch.build.targets.wheel] packages` |
| `malkreide/global-education-mcp` | 🟢 yes | **1** | same key |
| `yourssu/soongpt-plugin` | 🟢 yes | **1** | same key |
| `divyarthjain/vtop-bhopal-mcp` | 🟢 yes | **4** | `package.json files` |
| `nirholas/ai-tutor-mcp` | 🟢 yes | **4** | `package.json files` |

### 🆕 🔴 `T68` — and one manifest declares TWO allowlists that disagree

🔴 **This is the sharpest thing `ACTION EV` found, and it corrects p147's prose.**
`librus-mcp`'s `pyproject.toml` carries **two** hatchling include allowlists, for two
different build targets, and they do not admit the same directories:

| target | key | items | 🔴 `.tool(` sites inside it |
|---|---|---|---|
| **wheel** | `packages` | **1** — `src/librus_mcp` | 🟢 **35** |
| **sdist** | `only-include` | **16** — incl. `tests_native`, `scripts/qualify_native.py` | 🔴 **39** |

🔴 **p147 named the 16-item `only-include` as the rule and published 35, which is the wheel
figure.** 🟢 **The number 35 is correct** — it is what the installable package contains, it
matches `MCP_CONTRACT.md`'s prose to the token, and it is the figure a studio consuming the
package would observe. 🔴 **The rule cited for it yields 39**, because the sdist allowlist
admits `scripts/qualify_native.py` (**2** sites) and `tests_native` (**2** sites).

🔵 **So "read the manifest's include allowlist" is underdetermined.** A pass has to say
*which build target*, and the right answer depends on which artefact the question is about.
🟢 **For a tool surface, the wheel is the right target**, and this page states that
explicitly from now on.

🟢 **p147's other librus figures reproduce exactly.** Whole tree **60**, and the
decomposition is **35** (`src/librus_mcp`) + **21** (`legacy_reference`) + **2** (`scripts`)
+ **2** (`tests_native`) = **60**. 🔵 p147 reported *"23 in `legacy_reference` + 2 in
`scripts`"*, attributing `tests_native`'s two to `legacy_reference`; the total is identical
and no published figure changes.

Instrument [`p148-manifest-allowlist`](../compose/code/p148-manifest-allowlist/README.md),
**12 tests** — one of which is the two-allowlist shape itself.

### 🔵 The npm tier, re-measured — unchanged

🟢 **8 of 8 tarballs fetched.** `ACTION EQ` ran the language-extended licence matcher over
all eight: **0 rows change class**. The tier's licence picture stands as p145 published it —
**4 `README_ONLY`, 3 `PKG_ONLY`, 1 `NONE`** (`@n35da/brightspace-mcp`, still the only npm
row on this shelf with no grant on any channel, and still the only one of the eight that
ships source).
## Pass 147 — 2026-10-12 — the npm tier gains two regions, and a foundational row was never read

🟢 **The clone and `npm pack` channels are both open** (`T65`), so this page's npm block is
re-measured from the payload rather than carried.

### 🆕 🟢 Two npm rows are region-placeable after all — `T59` NARROWED

🔴 **`T59` called this shelf's 8 npm rows "structurally unplaceable on the region axis."**
🟢 **That is a property of the INSTRUMENT lane, not of the evidence.**

| row | region | host | where | strength |
|---|---|---|---|---|
| 🟢 `eth-moodle-mcp@1.3.3` | 🟢 **EMEA** | `moodle-app2.let.ethz.ch` — ETH Zürich | `README.md:76`, the `MOODLE_URL` **default** | 🟢 **strong** |
| 🟡 `mcp-canvas-lms@1.0.5` | 🟡 **APAC** | `canvas.ust.hk` — HKUST | `README.md:37`, an **`e.g.`** | 🟡 **a lead** |
| `@imazhar101/mcp-canvas-server` | 🔴 `UNPLACED` | — | — | — |
| `@ink-waffle/moodle-mcp` | 🔴 `UNPLACED` | — | — | — |
| `@n35da/brightspace-mcp` | 🔴 `UNPLACED` | — | 🔴 only `d2l.myschool.edu`, a placeholder | — |
| `@owen-x-tech/canvas-mcp` | 🔴 `UNPLACED` | — | — | — |
| `canvas-mcp-server` | 🔴 `UNPLACED` | — | — | — |
| `moodle-mcp-server-aql` | 🔴 `UNPLACED` | — | 🔴 only `moodle.example.edu`, a placeholder | — |

🟢 **`eth-moodle-mcp` is strong because two independent Swiss-specific signals agree**: the
shipped `MOODLE_URL` default is ETH Zürich's production Moodle, and the token-minting
instruction names **nethz** (ETH's account system) and **AAI** (SWITCHaai, the Swiss
academic federation). Instrument [`p147-npm-region`](../compose/code/p147-npm-region/README.md), **15 tests**.

### 🟢 `@imazhar101/mcp-canvas-server` — 227 confirmed by a third method

🔴 **This page has carried a disagreement: 227 descriptors on one instrument, 18 dynamic
sites on another.** 🟢 **Resolving the 18 one level gives exactly 227.**

**18 tool modules, 18 spread sites in the `tools/list` handler, 1:1** at
`dist/servers/canvas/src/index.js:263-280`. Largest: `user-tools` **39**, `page-tools`
**21**, `file-tools` **20**, `submission-tools` **20**, `module-tools` **18**. Smallest:
`lti-launch-definition-tools` **1**, `grading-standard-tools` **3**, `admin-tools` **4**.

🟢 **So `T42` is confirmed by a third method**: `surface_bound` counts descriptors,
`surface_gate*` counts registration sites, and the two are the same surface at two levels.
🔵 **The largest tool surface this KB quotes is correct.** Instrument
[`p147-tooldef-sum`](../compose/code/p147-tooldef-sum/README.md), **11 tests**.

### 🆕 🟢 A foundational row this page should have had — Apache-2.0, Rust, 46 tools

| [`zavora-ai/mcp-student-records`](https://github.com/zavora-ai/mcp-student-records) | v1.2.0 |
|---|---|
| licence | 🟢 **Apache-2.0** — buildable on, no copyleft |
| surface | 🟢 **46 tools**, declared in `mcp-server.toml` and pinned by test |
| write governance | 🟢 **23 of 46 `requires_approval = true`**; typed `risk_class` per tool |
| compliance | 🟢 **FERPA-gated communications + FERPA access log** |
| domain | 🟢 self-declared `domain = "education"` in the manifest |

🔴 **Both `os.walk` surface gates on this shelf read it as zero files**, because it is Rust
and `lang_of` has no `.rs` (`T64`). 🔵 **It is a complete SIS surface — students, courses,
enrollments, grades, rubrics, attendance, guardians, transcripts, analytics — under a
permissive licence, and the shelf could not see it.**

### 🔴 `moodle-mcp-server-aql`'s AGPL-3.0 — a packaging defect, not a missing grant

🔴 **`ACTION EF` REFUTED exactly as its falsifier specified.** The declared repository
[`csmediapro/moodle-mcp-server`](https://github.com/csmediapro/moodle-mcp-server) is alive
and carries the **complete 661-line AGPL-3.0 body** at its monorepo root.

🔴 **The tarball carries no licence file at all.** Cause, named precisely:
`packages/server/package.json` ships an explicit **`files` allowlist of 16 globs**, none of
them `LICENSE`, and there is **no `LICENSE` inside `packages/server/`**. 🔵 **npm's
automatic licence inclusion looks in the package directory and does not reach up a
monorepo.** 🟢 **The grant exists and it is AGPL-3.0** — the obligation is real, the file
just never shipped. 🔵 **Restate as a packaging warning, not a licence gap.**

## Pass 146 — 2026-10-12 — the platform layer's licence map, and a shelf-wide instrument defect

🔴 **No foundational repo was cloned this pass** (`P146-A`). 🟢 **But the licence axis of the
major platform layer was read for the first time, on a channel no previous pass had
tried** — and it changes which platform a studio should reach for.

### 🆕 🟢 The platform layer, read on the licence axis — one permissive row out of seven

| repo | licence | ★ | what it is | build bar |
|---|---|---|---|---|
| 🟢 [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | 🟢 **ECL-2.0** | 1.2k | Learning, teaching, research and collaboration platform. 🟢 **ECL-2.0 is Apache-2.0 with a narrowed §3 patent grant — OSI-approved, copyleft: no** | 🟢 **PASSES** |
| [`openedx/edx-platform`](https://github.com/openedx/edx-platform) | 🔴 **AGPL-3.0** | 8.2k | The Open edX LMS and Studio. MOOC-grade, Python/Django | 🔴 **network copyleft** |
| [`instructure/canvas-lms`](https://github.com/instructure/canvas-lms) | 🔴 **AGPL-3.0** | 6.9k | Instructure's open LMS, alongside its commercial SaaS | 🔴 **network copyleft** |
| [`moodle/moodle`](https://github.com/moodle/moodle) | 🔴 GPL-3.0 | 6.2k | The most-deployed LMS worldwide; deepest plugin ecosystem | 🔴 copyleft |
| [`chamilo/chamilo-lms`](https://github.com/chamilo/chamilo-lms) | 🔴 GPL-3.0 | 1.0k | LMS focused on ease of use and accessibility | 🔴 copyleft |
| [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | 🔴 LGPL-3.0 | 886 | 🟢 **LMS + SIS + fees + parent app on ONE database**, on the Odoo framework | 🔴 weak copyleft |
| [`ILIAS-eLearning/ILIAS`](https://github.com/ILIAS-eLearning/ILIAS) | 🔴 GPL-3.0 | 505 | Official ILIAS release and development branches | 🔴 copyleft |

🔵 **Why this is a foundations finding and not a verticals one.** A foundational repo is
one you build **on**. 🔴 **Six of these seven cannot be built on in the fork-and-modify
sense without a reciprocal obligation**, and the two largest carry AGPL's network clause,
which triggers on precisely the hosted multi-tenant shape these platforms are deployed in.
🟢 **Sakai is the only row where fork-and-modify is also on the table** — and it is the
fourth-largest, which is why no previous pass noticed.

🟢 **The API-boundary pattern remains the default on every copyleft row** and is unaffected:
a separate agent service speaking REST/LTI to the platform incurs no obligation on the
agent's own code. 🔵 **The licence map changes which platform you pick when the client
needs core changes, not whether the shelf's patterns work.**

### 🆕 🔴 The instrument layer under this page has a shelf-wide defect

🔴 **`T42` is a property of this shelf, not an incident.** `p146-exclusion-reach` reads every
traversing instrument in `compose/code/`:

| | count |
|---|---|
| instruments that traverse a tree | **35** |
| …carrying an **empty-walk guard** | 🔴 **0** |
| …excluding `dist`/`build` with no re-admission while emitting a verdict | 🔴 **5** |
| …that **cannot read anything but a git clone** | 🔴 **16** |

🆕 🔴 **`T59`**: 16 of 35 instruments traverse by `git ls-tree`/`ls-files`, so a clone is a
**precondition**, not a convenience — and 🔴 **the entire region-placement lane is in that
set** (`americas`, `cctld_urlctx`, `origin_scale`, `repo_origin`, `tenancy`). 🔵 **A
published npm package is not a git tree, so the 8 npm rows on this shelf are structurally
unplaceable on the region axis this KB exists to serve.** 🔴 **No pass had said so.**
`ACTION EK` asks whether a non-git channel can place any of them.

🟢 **`p146-empty-walk-guard` is the four-line fix**, with the distinction it exists to
preserve pinned by test: *zero files walked* withholds a verdict; *files walked, none
matched* is a finding and keeps its verdict.

### 🔴 What this page did NOT do this pass

- 🔴 **No star count, commit count, HEAD date or licence file was read for any existing
  shelf row** — all of those need a clone.
- 🔴 **The seven platform licences above are page readings, not `LICENSE`-file reads.** A
  licence badge is a declaration; `T21`/`P145-I` is this KB's own evidence that a
  declaration and a shipped grant diverge. 🔵 **They are published as declarations.**
- 🔴 **OpenEduCat's Odoo dependency chain was not read** — upstream is LGPL-3.0 with a
  proprietary Enterprise edition, and the obligation interaction is unknown.

# Education — foundational repos

**Pass 145, 2026-10-12.** 🔴 **The npm rows on this page were never read.** The instrument
this KB measures tool surfaces with excludes `dist` and `build` unconditionally, and **7 of
the 8 npm packages cited here ship their entire payload under exactly those two names**.
🟢 **All eight are now measured**, and 🔴 **none of the eight ships a licence file.**

### 🔴 `ACTION DZ` / `P145-A` — seven rows on this page returned a verdict over zero files

🔵 **p144 discharged `ACTION DP` by cloning three npm packages and comparing bundle against
source.** That comparison was sound. 🔴 **What nobody checked is whether the instrument
could read the bundle at all** — and on seven of eight rows it could not, because
`SKIP_DIRS` removed the only tree the package ships.

| package | all code under | files | p143 read | p145 reads |
|---|---|---|---|---|
| `@imazhar101/mcp-canvas-server` | 🔴 `dist/` | 69 | 🔴 `NOT_AN_MCP_SERVER` | **18 dynamic sites** (227 descriptors) |
| `moodle-mcp-server-aql` | 🔴 `dist/` | 68 | 🔴 `NOT_AN_MCP_SERVER` | 🔴 **`MUTATED` — plugin-extensible** |
| `@ink-waffle/moodle-mcp` | 🔴 `dist/` | 18 | 🔴 `NOT_AN_MCP_SERVER` | 🟢 **16 literal** |
| `mcp-canvas-lms` | 🔴 `dist/` | 16 | 🔴 `NOT_AN_MCP_SERVER` | 🟢 **3 literal** |
| `eth-moodle-mcp` | 🔴 `build/` | 13 | 🔴 `NOT_AN_MCP_SERVER` | 🟢 **18 literal** |
| `canvas-mcp-server` | 🔴 `build/` | 6 | 🔴 `NOT_AN_MCP_SERVER` | 🟢 **54 literal** |
| `@owen-x-tech/canvas-mcp` | 🔴 `build/` | 4 | 🔴 `NOT_AN_MCP_SERVER` | 🟢 **62 literal** |
| 🟢 `@n35da/brightspace-mcp` | 🟢 `lib/` + `server.mjs` | 17 | 🟢 **17 dynamic** | 🟢 **17 dynamic** (unchanged) |

🟢 **Four of the new readings reproduce counts this page already held by other means** — 16,
3, 18 and 54 match `p143-tier-size`'s hand counts exactly, and **62** matches the live
surface `p139` established for `@owen-x-tech/canvas-mcp`. 🔵 **Agreement across two
unrelated instruments on five rows is what makes the seven corrections trustworthy.**

### 🔴 The rule this page should have been applying, and now is

> **A tree is excluded only when it does not bear the property being measured.**

`dist/` is a regenerated artefact in a git checkout and **the shipped source itself** in a
published tarball. 🔵 **Same name, opposite correctness** — so the test is the package's own
declared entry point (`main`, `bin`, `module`, `exports`), not the name. Instrument:
[`p145-surface-payload-repair`](../compose/code/p145-surface-payload-repair/README.md),
**14 tests**.

🟢 **This also forecloses `T37` by construction**: a committed `dist/` beside its own source
stays excluded, so the double count that defeated `P144-A`'s first draft cannot recur.

### 🔴 `ACTION DX` — not one npm row on this page ships a licence file

| package | grant | licence |
|---|---|---|
| `@imazhar101/mcp-canvas-server` | 🔴 README only | MIT |
| `@ink-waffle/moodle-mcp` | 🔴 `package.json` only | MIT |
| `@n35da/brightspace-mcp` | 🔴 **NONE** | — |
| `@owen-x-tech/canvas-mcp` | 🔴 `package.json` only | MIT |
| `canvas-mcp-server` | 🔴 `package.json` only | MIT |
| `eth-moodle-mcp` | 🔴 `package.json` only | MIT |
| `mcp-canvas-lms` | 🔴 `package.json` only | MIT |
| `moodle-mcp-server-aql` | 🔴 `package.json` only | 🔴 **AGPL-3.0** |

🔴 **0 of 8.** 🔵 **Consistent with `T21`'s 33% npm licence-payload rate rather than in
conflict with it**: `npm pack` includes a `LICENSE` only if one exists in the tree, so a
0% file rate at HEAD and a 33% historical payload rate describe the same population at two
times. 🟢 **`P138`'s distinction holds and is the operative one here — a licence identifier
is not a licence**, and seven of these rows offer only an identifier.

🔴 **`@n35da/brightspace-mcp` is the sharpest row on the page**: the only npm package that
ships readable source, and the only one with no licence of any kind. 🔵 **The row a
developer can most easily learn from is the row they have least right to copy.**

### 🔴 The foundational row that is unbounded by design

`moodle-mcp-server-aql` builds `toolDefinitions = buildCoreToolDefinitions()` and then
**`.push()`es one descriptor per discovered plugin** (`dist/server/factory.js:131`, inside
the plugin loop). 🔴 **Its tool surface is a property of the deployment's plugin set**, not
of the published package — the first row on these shelves that is unbounded for an
architectural reason rather than an instrumental one.

🔴 **It is also the AGPL-3.0 declaration.** 🔵 **A plugin-extensible connector under
copyleft is a specific delivery hazard**: the extension points invite exactly the
modification the licence attaches obligations to. `ACTION EF` tests whether any licence
text exists behind the declaration.

### 🟢 What this page can now say about its own instruments

🔴 **`ACTION DV` asked for all four tiers under one instrument and that is not achievable
here.** `surface_bound.py` reads **JS and TS only**; of the 20 MCP servers across the four
tiers, **7 are Python and 1 is PHP**. 🔵 **Recorded as a structural property of the
population**, not as an environment blocker and not as a probe to re-register.

🔴 **And the two instruments measure different things.** `surface_bound` counts
**descriptors**; the gate instruments count **registration sites**. On
`@imazhar101/mcp-canvas-server` that is **227** against **18**, and 🟢 **neither number is
wrong** — which is why `T30`, built across both, is withdrawn outright rather than
reinstated.


**Pass 144, 2026-10-12.** 🔴 **The correction this page owed about its npm instruments is
discharged, and it resolves in the opposite direction.** p143 recorded that 7 of 8 npm packages
could not be read at all because they ship only compiled output, and withdrew the npm figures on
that basis. 🟢 **Three of them were cloned this pass and the compiled output turns out to be a
faithful measurement**: bundle and shipped source return **identical tool-name sets** on 3 of 3.
🔴 **But 5 of 8 have no reachable source at all**, and one of those *declares* a repository that
is dead.

### 🟢 `ACTION DP` — the npm foundation rows measure the same on bundle and on source

[`p144-npm-source-parity`](../compose/code/p144-npm-source-parity/README.md).

| package | repo | licence | bundle | shipped source | name sets |
|---|---|---|---|---|---|
| `canvas-mcp-server@2.2.3` | 🟢 [`DMontgomery40/mcp-canvas-lms`](https://github.com/DMontgomery40/mcp-canvas-lms) | 🟢 MIT | **54** | 🟢 **54** | 🟢 identical |
| `moodle-mcp-server-aql@0.1.7` | 🟢 [`csmediapro/moodle-mcp-server`](https://github.com/csmediapro/moodle-mcp-server) | 🔴 **AGPL-3.0** | **14** | 🟢 **14** | 🟢 identical |
| `mcp-canvas-lms@1.0.5` | 🟢 [`MisterCommand/mcp-canvas-lms`](https://github.com/MisterCommand/mcp-canvas-lms) | 🟢 MIT | **3** | 🟢 **3** | 🟢 identical |

🔵 **Set identity is the claim, not count identity** — `namesets.py` reports `bundle_only` and
`source_only`, both empty on all three rows. 🟢 **So `T30`'s npm figure is reinstated**, which is
what `ACTION DP` specified on this outcome.

🔴 **`moodle-mcp-server-aql` is AGPL-3.0 and that is a stop-ship for a studio build**, declared
in the npm metadata and confirmed in the repository. It is the only copyleft row on the npm tier.

### 🔴 The 5 rows this page cannot verify, stated per row rather than as a share

| package | source route | outcome |
|---|---|---|
| `@owen-x-tech/canvas-mcp@1.1.0` | `repository: owentaylor/canvas-mcp` | 🔴 **DECLARED AND DEAD** — `git ls-remote` prompts for credentials |
| `@imazhar101/mcp-canvas-server@2.1.3` | none | 🔴 no `repository`, `homepage` or `bugs`; **227 declared tools unverifiable** |
| `@ink-waffle/moodle-mcp@0.2.0` | none | 🔴 **18 `.map` files, zero `sourcesContent`** |
| `@n35da/brightspace-mcp@0.4.0` | none | 🔴 no pointer |
| `eth-moodle-mcp@1.3.3` | none | 🔴 no pointer |

🟢 **One correction to `P138-H` in the other direction**: `mcp-canvas-lms` was recorded as having
no `repository` field, which is true, and it is placeable anyway from `homepage`/`bugs`. 🔵 **A
missing `repository` field is not the same as an unsourceable package**, and three fields have to
be read before a row is declared dark.

🔴 **The sourcemap route is now closed and recorded as closed.** Three packages ship `.map`
files and not one carries `sourcesContent`, so a map yields original *path names* and no original
*bytes*. 🔵 **A future pass should not re-attempt it.**

### 🟢 `global-education-mcp` is no longer the only self-verifying row on this page

[`p144-surface-pin-census`](../compose/code/p144-surface-pin-census/README.md). `ACTION DQ` asked
for a second row carrying a committed tool-surface pin and found **two**, by two mechanisms
neither of which is a hash lockfile.

| row | licence | mechanism | pinned |
|---|---|---|---|
| 🟢 [`malkreide/global-education-mcp`](https://github.com/malkreide/global-education-mcp) | 🟢 MIT | `tools.lock.json`, SHA-256 per tool | **10** |
| 🆕 🟢 [`oliverhruby/edupage-mcp`](https://github.com/oliverhruby/edupage-mcp) | 🟢 MIT | classification manifest over live `list_tools()` | **31** |
| 🆕 🟢 [`divyarthjain/vtop-bhopal-mcp`](https://github.com/divyarthjain/vtop-bhopal-mcp) | 🟢 Apache-2.0 | `EXPECTED_TOOLS` golden name array | **17** |

🔴 **Three instances and three incompatible formats.** 🔵 **So a consumer cannot ask "does it
ship the lockfile?"** — the question is whether *any* committed artefact pins the surface, and
the answer has to be looked for in three places.

### 🆕 🔴 Two rows cited by this KB carry no licence at all

Found while verifying something else, which is why `ACTION DX` now counts all 44 connector rows
and all 8 packages rather than trusting an incidental pair.

| row | size | licence at HEAD |
|---|---|---|
| 🔴 [`Piyushtanwani/DAU-buddy`](https://github.com/Piyushtanwani/DAU-buddy) | **40 literal tools, 176 commits** | 🔴 **NONE** |
| 🔴 [`ruud0/aula-virtual-mcp`](https://github.com/ruud0/aula-virtual-mcp) | 4 commits | 🔴 **NONE** |

🔴 **`DAU-buddy` is the largest tool surface on the github-only tier and it is unusable** — no
licence means no grant, and no grant means a studio cannot copy a line of it. 🔵 **It remains
worth reading as a design reference**, which is a different permission from building on it.

### 🔵 Channel note — `curl -sI` cannot verify a GitHub URL in this environment

🔴 **`curl -sI https://github.com/<owner>/<repo>` returns `403` for every repository, live or
dead**, so it cannot distinguish them and must not be used as a URL check here. 🟢 **`git
ls-remote` and `git clone` both work**, and are what showed `owentaylor/canvas-mcp` to be dead
rather than merely unreachable. 🔵 **Every repository figure on this page was produced by
`git clone` over full history**; see
[`evidence/verified-repos.2026-10-12-p144.tsv`](../evidence/verified-repos.2026-10-12-p144.tsv).

**Pass 143, 2026-10-12.** 🟢 **`ACTION DO` discharged: the education-statistics row added last
pass is now VERIFIED rather than declared**, and it is the only row on this page whose tool
surface a consumer can check without running it. 🔴 **And a correction this page owes: the
licence-and-payload instruments it cites for npm rows cannot read 7 of the 8 npm packages at
all**, because they ship only compiled output.

### 🟢 `ACTION DO` — `global-education-mcp`'s lockfile verifies, independently recomputed

[`p143-lockfile-audit`](../compose/code/p143-lockfile-audit/README.md). p142 added this row on
the strength of a *declared* `tools.lock.json`. 🟢 **It is now a checked claim.**

| row | licence | verification |
|---|---|---|
| 🟢 [`malkreide/global-education-mcp`](https://github.com/malkreide/global-education-mcp) | 🟢 **MIT**, `LICENSE` present, declared in `pyproject.toml` | 🟢 **10 of 10 hashes recompute**, independently of the repository's own generator. 🟢 **10 of 10 agree with `server.py`** on `name`, `annotations` and `description`. 🟢 **10 of 10 `readOnlyHint: true`, zero write tools.** HEAD `26f7cd2`, **2026-10-04**, EMEA (`+0200` ×70) |

🔴 **One of the four hashed fields is NOT verified and the honest statement names it.**
`inputSchema` is generated by pydantic at import; checking it requires executing the
repository, which this audit does not do. 🔵 **So a consumer who cannot run the server has
verified three fields of four** — and that is still the strongest tool-surface guarantee
anywhere on these shelves.

**What a studio does with it.** 🟢 **`scripts/tool_signatures.py ci` is one CI step that
replaces four of this KB's own instruments** (`p139-tool-count-drift`,
`description-drift-audit`, `p141-agent-surface-gate`, `p142-github-only-tier`) for any
repository that adopts the pattern. 🔵 **It is the cheapest control on these shelves and it is
MIT**, so it can be lifted.

### 🔴 A correction this page owes about its own npm instruments

[`p143-tier-size`](../compose/code/p143-tier-size/README.md) measured what the 8 npm connector
packages actually ship:

| | |
|---|---|
| 🔴 npm packages shipping **only** compiled output (`dist/` or `build/`) | **7 of 8** |
| 🟢 npm packages shipping **source** | **1 of 8** — `@n35da/brightspace-mcp` (`.mjs`, `lib/`) |

🔴 **So a source-reading instrument sees nothing in 7 of 8 npm rows**, and any figure this KB
has published comparing npm rows to repository rows was comparing a **bundle** to a **source
tree**. 🔵 **`T21`'s licence-payload gradient is unaffected** — it reads published packages in
all three ecosystems, one artefact kind throughout, which is exactly why it has survived four
falsifiers. 🔴 **`T30`'s registration gradient is withdrawn**, and `T36` is the general rule.

**The practical consequence for a studio evaluating an npm education connector.** 🔴 **You
cannot audit what you cannot read.** 7 of 8 of these packages require fetching the repository
separately to review the code you are installing, and `@owen-x-tech/canvas-mcp` — whose README
claims 150+ tools against 62 measured — 🔴 **is the row whose repository is gone.** 🟢 **Prefer
the row that ships source or pins its surface**; on this page that is `@n35da/brightspace-mcp`
and `malkreide/global-education-mcp` respectively.

### 🔵 Channel note — the clone channel opened, and it changes what this page can verify

🟢 **`git clone` of public repositories now works from this environment**, with full history.
🔵 **Every verification on this page previously rested on single-file fetches**; licence files,
POM chains and payload measurements can now be read in tree. 🔴 **`api.github.com` repository
endpoints remain refused — on SCOPE, not a block** (`rate_limit` answers `200`), so star counts
are still unavailable and commit counts remain the size proxy. 🔴 **`codeload.github.com`
tarballs are `403` while `git clone` succeeds**, which is worth recording as a channel
asymmetry rather than rediscovering.

**Pass 142, 2026-10-12.** 🔴 **`ACTION DF` refuted: the licence a consumer gets from veraPDF
depends on which MODULE it resolves, not on the project.** 🟢 **And a foundational row is added
that this page has never had a category for — a permissively licensed, read-only connector over
UNESCO and OECD education statistics, which is a primary source for the figures `intel/market.md`
has had to take from vendor blogs.**

### 🔴 `ACTION DF` — veraPDF's grant is per-module, and 3 of 3 jars say nothing

[`p142-verapdf-module-grant`](../compose/code/p142-verapdf-module-grant/README.md). p140's
parent-chain walker, **executed unchanged**; only the coordinates are new.

| coordinate | own POM | effective licence | depth | jar licence text |
|---|---|---|---|---|
| `org.verapdf:core:1.30.3` | 🔴 NONE | **GPL-3.0 *or* MPL-2.0** *(from `verapdf-parent`)* | **4** | 🔴 `SILENT` — 460 entries |
| 🔴 **`org.verapdf:verapdf-xmp-core:1.30.3`** | 🟢 **BSD-3-Clause** | 🟢 **BSD-3-Clause** | 4 | 🔴 `SILENT` — 78 entries |
| `org.verapdf:validation-model:1.30.3` | 🔴 NONE | **GPL-3.0 *or* MPL-2.0** | 4 | 🔴 `SILENT` — 369 entries |
| 🔴 `org.verapdf:xmp-core:1.30.3` | — | — | — | 🔴 **404 — never published** |

**What a studio has to do differently.** veraPDF is the PDF/UA validator — the component you
reach for when course material has to meet an accessibility obligation. 🔴 **The election between
GPL-3.0 and MPL-2.0 applies to `core` and `validation-model` and does NOT arise for
`verapdf-xmp-core`, which is BSD-3-Clause.** A scanner reading the named umbrella coordinate
reports nothing and the umbrella has no jar at all.

🔵 **`org.verapdf:xmp-core` was never a coordinate.** p141 read it out of
`<modules><module>xmp-core</module></modules>`, and **a `<module>` entry is a source-tree path,
not an artifactId** — the directory `xmp-core/` builds `verapdf-xmp-core`. Any probe deriving
coordinates from a `<modules>` block inherits this error; it is pinned as a test.

### 🆕 🟢 The education-statistics layer — a foundational tier this page did not have

| repo | licence | what it is |
|---|---|---|
| 🟢 [`malkreide/global-education-mcp`](https://github.com/malkreide/global-education-mcp) | 🟢 **MIT**, `LICENSE` present, declared in `pyproject.toml` | 🟢 **UNESCO UIS (4 000+ indicators) and OECD *Education at a Glance*, over SDMX, with no API key.** 151 commits, HEAD **2026-10-04**, EMEA (`+0200` ×70). **10 tools, every name a literal, every one `readOnlyHint: true` — zero write tools.** Full MCP `ToolAnnotations` on 10 of 10, and 🟢 **a `tools.lock.json` that SHA-256-hashes each tool's annotations, description and schema** |
| 🟢 [`alcastaro/opendata-latam-mcp`](https://github.com/alcastaro/opendata-latam-mcp) | 🟢 **MIT** | 7 national CKAN open-data portals (AR, CL, DO, EC, MX, PA, UY), 15 628 datasets, cross-country parallel search. 🟢 **LATAM-placed on government hosts in 8 countries.** Not education-specific; the regional-evidence layer for engagements that need one |

🔵 **Why these belong on a *foundations* page rather than only on the agents shelf.** Every
regional figure this KB carries — market size, adoption rate, CAGR by region — currently comes
from market-research marketing pages, and `intel/market.md` says so each pass. 🟢 **UNESCO UIS and
OECD EAG are the primary sources those pages are re-quoting**, and there is now an MIT-licensed,
read-only, annotation-complete client for both.

🔴 **And it cannot run here.** `api.uis.unesco.org` and `sdmx.oecd.org` both answer `000` through
this environment's proxy. 🔵 **This is the most actionable entry the blocked-source ledger has
ever carried: two hostnames, one MIT dependency, and the figure channel this KB has been missing
for twenty passes.**

### 🟢 The practice worth copying off this page's newest row

`tools.lock.json` is a **tool-surface lockfile**: one SHA-256 per tool over its signature
(annotations + description + input schema), committed. 🔵 **This KB has built four instruments to
detect what that file prevents** — `p139-tool-count-drift`, `description-drift-audit`,
`p141-agent-surface-gate`, `p142-github-only-tier`. 🟢 **A row that pins its own surface by hash
makes all four unnecessary against it**, and the repository's own comment states the intent: the
logging wrapper preserves `__doc__` *"damit der `tools.lock.json`-Hash stabil bleibt"*. Adopted
as pattern `P21`.

**Pass 141, 2026-10-12.** 🔴 **`ACTION DC` applied p140's parent-chain walk to every Maven
coordinate this KB cites, and three further rows change verdict — so `T26` is not a property of
two artefacts but of Maven's inheritance model.** 🔴 **`ACTION DA` found the opposite failure
one layer below `openedx-core`'s distribution: not a disagreement between layers, but silence
in all of them below the wheel.**

### 🔴 `ACTION DC` — 5 of 9 coordinates on this shelf do not declare their own licence

[`p141-pom-chain-sweep`](../compose/code/p141-pom-chain-sweep/README.md). The walker is p140's,
re-used **unchanged** so that a changed verdict cannot be mistaken for a changed method; only
the population is new.

| coordinate | own POM | inherits from | inherited licence | depth |
|---|---|---|---|---|
| 🟢 `org.imsglobal:basiclti-util:1.2.0` | Apache-2.0 | — | — | 1 |
| 🆕 🔴 **`org.verapdf:verapdf-library:1.30.3`** | 🔴 **NONE** | `org.verapdf:verapdf-parent:1.30.1` | 🔴 **GPL-3.0 *or* MPL-2.0** | **3** |
| 🆕 🔴 `org.jasig.ssp:ssp:2.8.0` | 🔴 **NONE** | `org.jasig.parent:jasig-parent:39` | Apache-2.0 | **3** |
| 🆕 🔴 `org.sakaiproject:kernel:23.3` | 🔴 **NONE** | `org.sakaiproject:oss-parent:1` | ECL-2.0 | **3** |
| 🆕 🟢 `uk.ac.ox.ctl:spring-security-lti13:0.3.7` | Apache-2.0 | — | — | 1 |

Cumulative, p140 + p141: 🔴 **`INHERITS_FROM_PARENT` 5** (`net.oauth.core:oauth`,
`sakai-kernel-impl`, `verapdf-library`, `jasig.ssp:ssp`, `sakaiproject:kernel`) against 🟢
**`DECLARES_OWN` 4** (`sakai-kernel-api`, `lti-launch`, `basiclti-util`,
`spring-security-lti13`). 🔵 **56% inherit. An audit that reads one POM per coordinate is wrong
more often than right on this shelf.**

🟢 **`org.imsglobal:basiclti-util:1.2.0` is also now walked rather than carried.** p140's prose
table listed it as *"Apache-2.0 (own)"* on an earlier pass's authority while its committed TSV
held only four rows. 🟢 **The walk confirms it — `DECLARES_OWN`, depth 1** — so the cell is
now evidenced by the same instrument as its neighbours rather than inherited from prose.

### 🔴 The row that should change a delivery decision: veraPDF

`org.verapdf:verapdf-library` is the **PDF/UA accessibility validator** — in an education
engagement, the component reached for to prove course material meets an accessibility duty.

🔴 **Its own POM carries no `<licenses>` block at all. The grant is two levels up, and it is a
dual GPL-3.0 / MPL-2.0 offer** — at once the strongest reciprocal licence anywhere on these
shelves and, through MPL-2.0, the route out of it. 🟢 **MPL-2.0 is the obvious election for a
studio, and it cannot be elected by a team that does not know it is offered.** 🔴 A scanner
reading the named coordinate reports *"no licence"*, which invites the *"permissive by default"*
error p140 corrected on `net.oauth.core:oauth` — this time on a component whose licence
genuinely constrains redistribution.

🔵 **And there is no payload to inspect for a second opinion.** `verapdf-library` is
`<packaging>pom` with modules `core` and `xmp-core`; 🔴 **`verapdf-library-1.30.3.jar` is 404 on
Central**, because no jar is published under that name — consumers resolve `org.verapdf:core`.
`org.jasig.ssp:ssp:2.8.0` is the same class, `<packaging>war`. 🔵 **The coordinate a dependency
declaration names has no own grant and no bytes: the licence lives in a parent and the code
lives in siblings.** `org.sonatype.oss:oss-parent:7` is the shared grandparent of both chains
and declares nothing, so the walk must continue *past* a silent ancestor rather than stop there.

### 🟢 The cleanest Maven row on this shelf, and it places itself in EMEA

🆕 `uk.ac.ox.ctl:spring-security-lti13:0.3.7` — **Apache-2.0, declared in its own POM, depth 1**,
LTI 1.3 for Spring Security. 🔵 **Its `groupId` is the origin evidence**: `uk.ac.ox` is the
University of Oxford's reverse-DNS namespace and `.ac.uk` maps to 🟢 **EMEA** with no inference
required. A Maven `groupId` is a stronger origin signal than an npm author field — it is a
namespace the organisation had to control in order to publish — and this is the first row this
KB has placed that way.

🔴 **It still ships no licence text** — no `LICENSE` or `NOTICE` among the jar's 72 entries. So
`T21`'s gradient firms up on a sixth Maven row rather than softening:

| ecosystem | declares a licence, ships no text |
|---|---|
| PyPI | 🟢 **0%** — 0 of 10 *(after p140's `openedx-learning` correction)* |
| npm | 33% |
| 🔴 **Maven** | 🔴 **83% — 5 of 6** *(p140: 80%, 4 of 5)* |

🔴 **`edu.ksu.ome.lti:lti-launch` 1.4.7 remains the worst row on the shelf** — LGPL-3.0 declared
in its own POM, no text in the jar, and pattern `P13` still depends on it.

### 🔴 `ACTION DA` — `openedx-core` is clean at the distribution layer and SILENT below it

[`p141-package-grant-layer`](../compose/code/p141-package-grant-layer/README.md). p140 called
`openedx-core` **1.9.1** the cleanest licence payload this KB has measured. 🟢 **That stands.**
🔴 **One layer down there is nothing.**

| package | `.py` files | licence files | SPDX headers | copyright lines |
|---|---|---|---|---|
| `openedx_catalog` | 12 | 🔴 0 | 🔴 0 | 🔴 0 |
| `openedx_content` | **132** | 🔴 0 | 🔴 0 | 🔴 0 |
| `openedx_core` | 1 | 🔴 0 | 🔴 0 | 🔴 0 |
| `openedx_django_lib` | 7 | 🔴 0 | 🔴 0 | 🔴 0 |
| `openedx_learning` | 29 | 🔴 0 | 🔴 0 | 🔴 0 |
| `openedx_tagging` | 56 | 🔴 0 | 🔴 0 | 🔴 0 |
| **total** | **237** | 🔴 **0** | 🔴 **0** | 🔴 **0** |

🟢 Distribution layer, for contrast: `License-Expression: AGPL-3.0-only` (PEP 639) plus
`dist-info/licenses/LICENSE.txt`, **35 139 bytes**, Metadata-Version 2.4.

🔵 **p140's falsifier expected DISAGREEMENT between layers. The measured answer is SILENCE — and
for a studio that is the worse one.** Nobody vendors a wheel; they lift `openedx_tagging/` or
`openedx_content/` into their own tree. 🔴 **The moment a subtree leaves `dist-info/`'s company
it carries no grant, no holder and no notice** — while **AGPL-3.0-only** is the most reciprocal
obligation anywhere on these shelves. 🔵 **The licence is correct, current and complete in
exactly the one place the copy does not come from.** A `T21`-clean artefact can be `T18`-silent;
this is the clearest instance of it, and both findings are true of different layers.

🟢 **One thing this confirms rather than discovers:** `openedx_learning` survives as a **package
inside** the distribution even though the *distribution* `openedx-learning` was retired to a
shim. 🔵 **The name was demoted, not killed** — the 29 files under it are live code at 1.9.1,
not the 1 479-byte husk `openedx-learning` 0.33.1 publishes. A row keyed on the string alone
cannot distinguish those, which is exactly why `T27` reads the `Development Status` classifier.

### 🟡 One citation on this page, re-checked and confirmed

`uk.ac.ox.ctl:spring-lti13` is **404 on Maven Central**, as the row below already records. 🟢
The real artefact is `spring-security-lti13`; the shorter coordinate has never existed. 🔵
Recorded as a confirmation, not republished as a finding — and the kind of re-check `T24` exists
to force.

### 🔴 A method note: a `429` from Central is not a `404`

Maven Central answered **429** on two of six metadata fetches and on the `basiclti-util` jar,
clearing after 8–24 s of backoff. 🔴 **An earlier draft of this sweep recorded
`uk.ac.ox.ctl:spring-security-lti13` as "not on Central" off a single un-retried `429`** — which
would have deleted the cleanest row in the table above. Every fetch retries with backoff and a
failure is reported as a failure, never as an absence.


**Pass 140, 2026-10-12.** 🔴 **Two of p139's findings on this page are refuted, and both
refutations make the underlying defect worse rather than milder.** `ACTION CR` resolved the Maven
parent chains p139 recorded as "no signal"; `ACTION CS` established that the one PyPI hit was
never a defect at all — it is a **package rename this KB has been failing to follow for two
passes.**

### 🔴 `ACTION CR` — both "declares nothing" rows DO declare, two and three levels up

| coordinate | own POM | inherits from | inherited licence | depth |
|---|---|---|---|---|
| 🔴 `net.oauth.core:oauth` 20100527 | **NONE** | 🆕 `net.oauth:oauth-parent:20090531` | 🆕 **Apache-2.0** | 3 |
| 🔴 `org.sakaiproject.kernel:sakai-kernel-impl` 23.3 | **NONE** | 🆕 `org.sakaiproject:oss-parent:1` | 🆕 **ECL-2.0** | 4 |

Both p139 controls return unchanged — `sakai-kernel-api` 25.2 `DECLARES_OWN` (ECL-2.0),
`edu.ksu.ome.lti:lti-launch` 1.4.7 `DECLARES_OWN` (LGPL-3.0) — so the changed verdicts belong to
the rows, not to the method.
[`p140-pom-parent-chain`](../compose/code/p140-pom-parent-chain/README.md).

### 🔴 Two sentences on this page are now wrong, and here is the correction

p139 wrote, of `net.oauth.core:oauth`:

> *"carries no licence signal at all … No grant and no file is not 'permissive by default' — it
> is **unlicensed**, and sixteen years of use does not change that."*

🔴 **There is a grant: Apache-2.0, inherited from `net.oauth:oauth-parent`.** 🔵 **And the reason
nobody found it is the finding** — the parent sits under a **different `groupId`**, `net.oauth`
rather than `net.oauth.core`. The artefact is not unlicensed. Its grant is two files and one
namespace hop from where any reader would look.

p139 also described the two Sakai kernel artefacts as *"same release line, opposite licence
posture"*. 🔴 **Both are ECL-2.0.** `api` declares it directly; `impl` inherits it from
`org.sakaiproject:oss-parent:1`. 🔵 **The posture is identical — only the declaration DEPTH
differs**, and depth is precisely what a scanner reading one POM does not traverse.

### 🔴 The declared-but-absent rate on this shelf's Maven rows rises to 80%

| coordinate | declares | ships licence text in the jar |
|---|---|---|
| 🟢 `org.imsglobal:basiclti-util` 1.2.0 | Apache-2.0 (own) | 🟢 `META-INF/LICENSE` + `NOTICE` |
| 🔴 `edu.ksu.ome.lti:lti-launch` 1.4.7 | LGPL-3.0 (own) | 🔴 **NONE** |
| 🔴 `org.sakaiproject.kernel:sakai-kernel-api` 25.2 | ECL-2.0 (own) | 🔴 **NONE** |
| 🔴 `net.oauth.core:oauth` 20100527 | 🆕 Apache-2.0 (**inherited**) | 🔴 **NONE** |
| 🔴 `org.sakaiproject.kernel:sakai-kernel-impl` 23.3 | 🆕 ECL-2.0 (**inherited**) | 🔴 **NONE** |

🔴 **5 of 5 declare; 4 of 5 (80%) ship no text** — against p139's 40–67% and npm's 33%. 🔵 **So
`T21`'s gradient steepens rather than collapsing: PyPI 9%, npm 33%, Maven 80%.** The falsifier
fired and the trend it threatened got stronger, which is the only outcome that makes writing one
worthwhile. 🔴 **`edu.ksu.ome.lti:lti-launch` — the LGPL-3.0 Kansas State library pattern `P13`
depends on — remains the worst row**: the strongest obligation of the five and no text to satisfy
it.

## 🆕 🔴 `openedx-learning` is RETIRED. The row this page should carry is `openedx-core`

### `ACTION CS` — the empty 0.33.x wheels were never a packaging bug

p139 found `openedx-learning` **0.33.0** and **0.33.1** shipping **1 479-byte** wheels and
pre-registered `ACTION CS` to ask whether the breakage was known upstream. 🔴 **It is not
breakage.** The 0.33.1 `setup.py` says so in its own docstring:

> *"Builds a final shell release of openedx-learning which simply 'redirects' to openedx-core"*

with `packages=[]`, `install_requires=["openedx-core==0.34.1"]`,
`Development Status :: 7 - Inactive`, and a `long_description` reading
**"This package has been renamed to `openedx-core`!"**

🟢 **So `pip install openedx-learning` WORKS** — it resolves the shim and installs `openedx-core`.
p139's *"`pip install` resolves to the empty one"* is true of the bytes and wrong about the
outcome. 🆕 **This pass also measured the sdist, which p139 did not**: 11 paths, carrying
`setup.py` and `setup.cfg` and **zero package source**, with `top_level.txt` a single newline.
🔵 **A build recipe with nothing to build — which is exactly what a rename shim looks like.**

### 🆕 The row to carry forward

| field | value |
|---|---|
| package | 🆕 [`openedx-core`](https://pypi.org/project/openedx-core/) — [`openedx/openedx-core`](https://github.com/openedx/openedx-core) |
| latest | **1.9.1**, uploaded **2026-10-09** *(three days before this pass)* |
| version continuity | first release **0.34.1** — exactly what the shim pins |
| licence | 🔴 **AGPL-3.0-only**, as a **PEP 639 `License-Expression`** |
| 🟢 licence payload | `dist-info/licenses/LICENSE.txt`, **35 139 B**, `License-File: LICENSE.txt`, Metadata-Version **2.4** |
| wheel | 261 paths, 358 188 B |
| consolidates | `openedx_core`, `openedx_learning`, `openedx_tagging`, `openedx_catalog`, `openedx_content`, `openedx_django_lib` |
| steward | `David Ormsbee <dave@axim.org>` — **Axim Collaborative** |

🟢 **It is the cleanest licence payload this KB has measured.** Declared by SPDX expression,
shipped automatically under PEP 639 — 🔵 **which vindicates `T21`'s mechanism on the newest
artefact on the shelf: the grant is shipped by the build system, not by the maintainer's
diligence.** 🟢 **And it removes p139's only PyPI hit**: that row was a shim with no code, so this
shelf's PyPI declared-but-absent rate is **0 of 10**, not 1 of 11.

🔴 **The lesson is a freshness check, not a licence check.** Both signals — the `Inactive`
classifier and the rename in `long_description` — were sitting in the artefact p139 downloaded.
🔵 **New rule: before carrying a package row forward, read its latest release's
`Development Status` classifier and its `long_description`.** Entered as `T27`.

### 🔴 `ACTION CQ` — three `ROOT_ONLY` rows record ownership NOWHERE in source

`ACTION CQ` asked whether p139's foreign-source-header class extends beyond its three largest
rows. 🟡 **It does, weakly — 1 of 5, against p139's 2 of 3** (`Tim Branyen, contributors`, an
MIT-licensed vendored grunt task inside GPL-3.0 `adaptlearning/adapt_framework`). Across all eight
`ROOT_ONLY` rows: **3 of 8.**

🔴 **The stronger result is one the action did not ask for.** `overhangio/tutor` (157 source files
read), `openedx/XBlock` (99) and `openedx/codejail` (31) carry **no copyright header in any
source file** — 287 files, zero headers. So each row is scored for *where a holder is findable at
all*:

| row | does `LICENSE` name a holder? | where ownership actually lives |
|---|---|---|
| `Crosstalk-Solutions/project-nomad` | 🟢 yes — appendix **filled**: `Copyright 2024-2026 Crosstalk Solutions LLC` | + `package.json` |
| `adaptlearning/adapt_framework` | 🟡 only inside the GPL's **interactive-mode example** | — |
| `openedx/XBlock` | 🔴 no — left as `Copyright [yyyy] [name of copyright owner]` | `NOTICE.txt`, `pyproject.toml` |
| `openedx/codejail` | 🔴 no — **no copyright line at all** in the appendix | `NOTICE.txt`, `pyproject.toml` |
| `overhangio/tutor` | 🔴 no — left as `Copyright (C) <year>  <name of author>` | `pyproject.toml` **only** |

🔵 **For a delivery team asking "who holds this code?", the answer is increasingly not in the file
named `LICENSE`.** `adapt_framework` is a third form this KB has not recorded: its holder appears
in the licence file *only* as part of the GPL's illustrative `show c` snippet — a real
attribution in a place no scanner treats as one.
[`p140-rootonly-header-reach`](../compose/code/p140-rootonly-header-reach/README.md).

### 🔴 Open edX names its holder three ways across three layers

| layer | artefact | holder | contact |
|---|---|---|---|
| repo | `openedx/XBlock` | `edX` | 🔴 `oscm@edx.org` |
| repo | `openedx/codejail` | `edX` / 🆕 `Open edX Project` | 🆕 `oscm@openedx.org` |
| registry | `openedx-core` 1.9.1 | 🆕 `David Ormsbee` | 🆕 **`dave@axim.org`** |

🟢 **The holder NAME is defensible.** edX Inc. was *renamed* Axim Collaborative — same trustees,
same mission, same tax ID — after Harvard and MIT sold the edX brand to 2U, so `Copyright 2014,
edX` names the pre-rename identity of the current steward rather than a third party.

🔴 **The CONTACT domain is not.** `edx.org` is operated by **2U**, a different company from the
steward, and `openedx/XBlock`'s `pyproject.toml` still routes there while its sibling
`openedx/codejail` routes to `openedx.org`. 🔵 **Two repositories in one GitHub organisation, same
licence, different holder string and different contact domain — and a third domain on the live
PyPI artefact.** A client asked to send a notice gets three answers to one question.

🟡 **And one row inverts the expected reading.** `overhangio/tutor` declares
`authors = [{name = "Edly"}, {email = "hello@edly.io"}]`, which is **correct and current**: Edly,
the edtech arm of Pakistan-based Arbisoft, acquired Overhang.IO on **2023-03-27**, and Tutor's
founder Régis Behmo leads its technical direction there. 🔵 **Here the metadata is fresher than
the GitHub organisation name** — so a row's org name is not evidence of anything.

**Pass 139, 2026-10-12.** 🔴 **p138 measured the npm payload layer and found a third of the
connector shelf declaring a licence it does not ship. This pass asked the obvious next question —
is that open source, or is it npm? — and the answer is neither: it is the TOOLCHAIN.**
`ACTION CM` ran the same method against **PyPI** and **Maven Central**. Probe, tests and committed
TSVs: [`p139-pypi-maven-payload`](../compose/code/p139-pypi-maven-payload/README.md).

| registry | artefacts measured | 🔴 declare a licence, ship no licence file | rate | vs the 10% threshold |
|---|---|---|---|---|
| 🟢 **PyPI** | **11** (+1 absent from the registry) | 🟡 **1** — and it ships **nothing at all** | **9%** | 🟢 **REFUTED** |
| 🔴 **Maven Central** | **5** (+1 absent) | 🔴 **2 of the 3 that declare** | **40–67%** | 🔴 **NOT REFUTED** |
| *(npm, p138)* | *21* | *7* | *33%* | *not refuted* |

🔵 **The defect tracks each ecosystem's DEFAULT BUILD BEHAVIOUR, not its culture.**

- 🟢 **Python's backends ship the licence for you.** Under **PEP 639**, setuptools and hatch copy
  declared licence files into `<dist>.dist-info/licenses/`. **10 of 11** packages carried one in
  *both* wheel and sdist — every Open edX row included. A maintainer gets this right by doing nothing.
- 🔴 **Maven's jar plugin ships nothing for you.** A POM's `<licenses>` block lives in a *sibling
  file*; the jar on the classpath is untouched. `META-INF/LICENSE` requires deliberate
  configuration, and **2 of 3 declaring artefacts had not done it**.
- 🔴 **npm's `files` array names what to pack and silently omits what is absent** — p138's
  `canvas-mcp-server` *listed* `LICENSE` and shipped 8 paths containing none.

### 🔴 `P139-D1` — the Maven rows, and the library this KB tells clients to build on is in the defect class

| coordinate | version | POM declares | jar paths | licence in jar |
|---|---|---|---|---|
| 🟢 `org.imsglobal:basiclti-util` | 1.2.0 | Apache-2.0 | 70 | 🟢 `META-INF/LICENSE`, `META-INF/NOTICE` |
| 🔴 **`edu.ksu.ome.lti:lti-launch`** | **1.4.7** | 🔴 **LGPL-3.0** | 43 | 🔴 **NONE** |
| 🔴 `org.sakaiproject.kernel:sakai-kernel-api` | 25.2 | 🔴 **ECL-2.0** | **578** | 🔴 **NONE** |
| 🔴 `net.oauth.core:oauth` | 20100527 | 🔴 **nothing declared** | 32 | 🔴 **NONE** |
| 🔴 `org.sakaiproject.kernel:sakai-kernel-impl` | 23.3 | 🔴 **nothing declared** | **524** | 🔴 **NONE** |
| — `uk.ac.ox.ctl:spring-lti13` | — | — | — | not on Central (**404**) |

All five resolvable jars were **sha1-verified against the repository's own `.sha1`**; no mismatches.

🔴 **`edu.ksu.ome.lti:lti-launch` is the artefact built from
[`kstateome/lti-launch`](https://github.com/kstateome/lti-launch) — the LGPL-3.0 Kansas State
library p137 identified (`P137-A`) as the LTI→OAuth-subject mapping that pattern `P13` depends on.**
It declares the strongest obligation of the five and ships no text to satisfy it. 🔵 **The one
interoperability library this KB recommends building on reproduces p138's worst npm row, in Java.**

🔴 **`sakai-kernel-api` declares ECL-2.0 while `sakai-kernel-impl` declares nothing** — two
artefacts of one kernel, same release line, opposite licence posture, and the one with **578
paths** is the one making the claim with no text. ECL-2.0 is **education's own licence** (an
Apache-2.0 derivative with a university-oriented patent clause), and it is exactly the identifier a
client's scanner will not recognise.

🔴 **`net.oauth.core:oauth` (2010) carries no licence signal at all** and is still a transitive
dependency of LTI 1.1 integrations. No grant and no file is not "permissive by default" — it is
**unlicensed**, and sixteen years of use does not change that.

### 🔴 `P139-D2` — the PyPI hit is not a licence defect: `openedx-learning` ships NO CODE

The one PyPI row declaring a licence and shipping no licence file is **`openedx-learning` 0.33.1**
— *"Open edX Learning Core (and Tagging)"*. It declares `AGPL 3.0` by legacy field **and**
classifier. Its wheel holds **4 paths, all metadata**; `top_level.txt` is **1 byte**; `RECORD`
lists only the four `dist-info` entries.

| version | wheel | sdist |
|---|---|---|
| 0.31.0 | 268 554 B | 192 313 B |
| 0.32.0 | 257 553 B | 189 430 B |
| 🔴 **0.33.0** | 🔴 **1 479 B** | 🔴 **1 748 B** |
| 🔴 **0.33.1** *(latest)* | 🔴 **1 479 B** | 🔴 **1 742 B** |

🔴 **`pip install openedx-learning` resolves to 0.33.1 and installs no modules.** Across **79
releases**, the two most recent are the empty ones — this is the *current* state of a core library
of the dominant open-source higher-education platform, not an old artefact. The collapse from 257 KB
to 1.4 KB is the signature of a packaging regression, shipped twice.

🔵 **A licence probe found a release defect.** It is counted honestly in both places: as a licence
row it is the hit that makes PyPI 9% rather than 0%; as a *finding* it belongs to a different class.

🟡 **Two smaller carries.** `xblock-sdk` 0.15.2 ships **two vendored Jasmine 1.3.1 `MIT.LICENSE`
files** under `sample_xblocks/*/static/js/lib/` beside its own AGPL-3.0 grant — `ACTION CJ`'s
foreign-holder class, in a payload. And `moodle-dl` declares `GPL-3.0` with `license_files`
**absent** from its metadata yet **ships** `LICENSE` in both distributions: 🔵 **a missing
`License-File` field does not imply a missing file**, the mirror image of npm's `files` naming one
it does not ship.

## 🔴 `ACTION CJ` — on the rows where the root licence file was "the whole story", it names nobody

p137 cleared **8** of the 20 largest rows as `ROOT_ONLY`: one licence file, nothing else
licence-shaped in the tree. `ACTION CJ` read the **source-file headers** of the three largest.
🔴 **Two of the three carry a holder their licence file does not name**, so p137's 50% is a **floor,
not an estimate**. Probe, 20 tests and TSV:
[`p139-source-header-holder`](../compose/code/p139-source-header-holder/README.md).

| row | tree paths | source files read | own holders | 🔴 foreign holders | verdict |
|---|---|---|---|---|---|
| 🔴 [`frappe/lms`](https://github.com/frappe/lms) | 1 606 | 1 411 | 2 | 🔴 **1 — `FOSS United`, 78 header lines** | `FOREIGN_HEADER_IN_SOURCE` |
| 🔴 [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | 1 345 | 450 | 1 | 🟢 0 | `OWN_HEADERS_ONLY` — 🔴 *but its pointer dangles* |
| 🔴 [`academico-sis/academico`](https://github.com/academico-sis/academico) | 692 | 660 | 🔴 **0** | 🔴 **3** | `FOREIGN_HEADER_IN_SOURCE` |

🔴 **`frappe/lms`'s `license.txt` names no holder of `frappe/lms`.** All **three** of its
`Copyright` lines are the AGPL's own apparatus: the FSF's copyright on the licence text (line 4),
the §0 definitions (line 65), and 🔴 **the "how to apply" template with the placeholder never
filled in** — `Copyright (C) <year>  <name of author>` (line 633). Ownership exists **only** in the
source headers, and there it is **two distinct legal entities**: `Frappe` / `Frappe Technologies
Pvt. Ltd.` (165 lines) and 🔴 **`FOSS United`** (78 lines), a separate Indian non-profit. 🔵 **A
verdict read from the root — "AGPL-3.0, Frappe" — is wrong in both halves on 78 files.**

🔴 **`openeducat/openeducat_erp`'s root `LICENSE` delegates copyright twice, and both pointers
dangle.** It opens *"For copyright information, please see the COPYRIGHT file."* — and
`git ls-tree -r HEAD` over all **1 345** paths finds **no `COPYRIGHT` file anywhere**. It then
delegates again, to "the relevant source files", which carry only `OpenEduCat Inc` (190 lines).
🔵 **The grant is sound and legible (LGPL-3.0, stated in its first lines); the chain that would say
whom you owe terminates nowhere.** It is the only one of the three honest enough to say it is not
trying.

🔴 **`academico-sis/academico` has zero headers of its own** and three foreign ones, all in built
Filament bundles under `public/` — `Pusher` (`echo.js`), `Chen Fengyuan` (`cropperjs`), `Chen,
Yi-Cyuan` (`js-sha256`) — 🔵 **the paths a client redistributes, and where no licence file would
ever be looked for.**

### 🟢 A channel p138 recorded as closed is open, and HEAD dates are measurable again

🟢 **`git clone --depth 1` against `github.com` works here.** p138 published **UNMEASURED** for
star counts *and* HEAD dates on the strength of `api.github.com`, `codeload` and `github.com` HEAD
all answering **403**. 🔵 **Git smart-HTTP is a different lane from the REST API, and it answers** —
which is how every row on this page was verified this pass, and how the `ACTION CN` lineage work was
done at all.

| row | HEAD commit | HEAD date |
|---|---|---|
| `frappe/lms` | `0f760e6` | **2026-10-11** |
| `openeducat/openeducat_erp` | `1c95cef` | **2026-09-07** |
| `academico-sis/academico` | `d0cd78c` | **2026-10-07** |

🔴 **Star counts stay `UNMEASURED`** — git carries no star count, so that half of p138's gap stands.


**Pass 139 — second probe lane (`ACTION CH`), 2026-10-12.** 🟢 **p138 measured a fifth layer — the published package — and found a
third of the connector tier shipping an SPDX identifier with no licence text. It then registered a
falsifier against itself, and this pass fires it: `ACTION CH` read every shipped text file in all
21 payloads, and 0 of the 9 licence-file-less packages carry their own grant in a source header.**
🔴 **p138's count stands.** 🔴 **A sixth layer is now measured, and it is the one a partial copy
depends on: per-file notice, practised by 1 of 21 rows.** On the other 20, a single file lifted out
of the tree names no holder and no grant. 🔵 **And the repository layer was measured in the same
pass as the payload layer for the first time** — through this KB's already-documented raw-file lane,
not a new one — re-verifying two of this KB's published licence figures byte-exact. Instrument and 24 tests:
[`p139-source-header-grant`](../compose/code/p139-source-header-grant/README.md).

**Pass 138, 2026-10-12.** 🔴 **p137 measured that a licence cell describes a repository root rather
than a whole tree. This pass measured a fifth layer, and it is the only one a client actually
receives: the published package.** `ACTION CD` downloaded **21** education-LMS connector tarballs
(Canvas, Moodle, Brightspace, EduBase), **sha1-verified every one against the registry's own
`shasum`** — 21 of 21 matched — and enumerated every shipped path.

| the layer | what it tells you | measured |
|---|---|---|
| root licence file | what you may do | 🟢 right about the **family** 92% of the time (`p444`) |
| tree enumeration | 🔴 **whom you owe** | 🔴 incomplete for **50%** of the largest rows (`p137`) |
| 🆕 **published payload** | 🔴 **what the client is actually handed** | 🔴 **9 of 21 packages ship NO licence file; 7 of those declare an SPDX id** |

🔵 **`npm install` unpacks a tarball; it does not clone a repository.** A grant that lives only at
HEAD is never conveyed to the person who installs the package — so a licence cell sourced from a
repository can be correct about the repository and wrong about the delivery.

🔴 **The row that matters most is the copyleft one.** `moodle-mcp-server-aql` **0.1.7**
(2026-10-01) declares **AGPL-3.0** across **141 shipped paths** and ships no licence text, while
[`csmediapro/moodle-mcp-server`](https://github.com/csmediapro/moodle-mcp-server) carries a
canonical **34 523-byte** `LICENSE`. 🔵 The strongest obligation on this shelf, conveyed without the
document that states it.

🔴 **And the mechanism is now known rather than guessed**: `canvas-mcp-server` **2.2.3**'s packed
manifest reads `files: ["build/**/*", "README.md", "LICENSE", "package.json"]` — it **names**
`LICENSE` — and its 8 shipped paths contain none. npm omits a `files` entry that does not exist in
the tree, silently. 🔵 **New rule for this page: a manifest that lists a licence is not evidence
that one shipped.**

🟢 **Direction of the error, which decides the remedy.** All nine defective rows are the repository
being *better* than the distribution — **not one package shipped a licence its repository lacked**.
The ask to an upstream is a one-line `files` change, not a relicensing conversation.

Instrument, method, committed 21-row TSV and 7 passing tests:
[`p138-npm-payload-licence`](../compose/code/p138-npm-payload-licence/README.md).

🔴 **This probe reads licence FILES only**, so the `pipwerks` case — a grant in a source-file header
— stays invisible to it. **7 of 21 is a floor, not a count.** `ACTION CH` was registered to close
that hole at the repository layer and **did not run this pass**; it is re-registered.

🔴 **Scope, stated:** npm only, four platform families, one registry search each. PyPI, Maven and
crates were not probed, and `moodler-mcp` — a Python connector on this KB's shelf — **is not on PyPI
at all (404)**, so for part of the shelf there is no payload layer to measure and no registry to
arbitrate a disputed address.

**Pass 137, 2026-10-11.** 🔴 **Every licence cell on this page describes a repository ROOT, and for
half of the largest rows the root is not the whole obligation.** `ACTION BY` enumerated the file
trees of the **20 largest rows on this page** — **224 591 paths** — and found **316** licence-shaped
files outside the root, **242** of them real grants. 🔴 **Ten of the twenty (50%) carry at least one
grant whose copyright holder is not the repository's own.** The refutation threshold was **5%**.
Instrument, tests and per-row results: `compose/code/p137-foreign-holder-tree`.

🔵 **Read this next to [`p444-root-vs-tree-family`](../compose/code/p444-root-vs-tree-family/README.md),
which measured the other half of the same question and looks like it says the opposite.** p444: the
licence **family** read from the root file is the tree's family **92%** of the time. p137: the
**ownership** is incomplete in **50%** of the largest rows. 🟢 **Both are true, and together they
are the rule: a root licence cell predicts what you may DO; it does not predict whom you OWE.**

### 🆕 `ACTION BY` — what the trees carry, per row

| row | tree paths | non-root licence files | real grants | 🔴 foreign holders | verdict |
|---|---|---|---|---|---|
| [`moodle/moodle`](https://github.com/moodle/moodle) | **67 589** | 96 | 87 | 🔴 **66** | `FOREIGN_HOLDER_IN_TREE` |
| [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | 18 127 | 76 | 58 | 🔴 **13** | `FOREIGN_HOLDER_IN_TREE` |
| [`chamilo/chamilo-lms`](https://github.com/chamilo/chamilo-lms) | 13 231 | 28 | 22 | 🔴 **17** | `FOREIGN_HOLDER_IN_TREE` |
| [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) | 25 823 | 17 | 13 | 🔴 **10** | `FOREIGN_HOLDER_IN_TREE` |
| [`classroomio/classroomio`](https://github.com/classroomio/classroomio) | 5 137 | 14 | 10 | 🔴 **10** | `FOREIGN_HOLDER_IN_TREE` |
| [`openedx/openedx-platform`](https://github.com/openedx/openedx-platform) | 9 273 | 18 | 11 | 🔴 **9** | `FOREIGN_HOLDER_IN_TREE` |
| [`instructure/canvas-lms`](https://github.com/instructure/canvas-lms) | 22 662 | 23 | 22 | 🔴 **4** | `FOREIGN_HOLDER_IN_TREE` |
| [`bigbluebutton/bigbluebutton`](https://github.com/bigbluebutton/bigbluebutton) | 4 826 | 2 | 2 | 2 | `FOREIGN_HOLDER_IN_TREE` |
| [`ILIAS-eLearning/ILIAS`](https://github.com/ILIAS-eLearning/ILIAS) | 17 073 | 6 | 1 | 1 | `FOREIGN_HOLDER_IN_TREE` |
| [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | 5 749 | 8 | 8 | 1 | `FOREIGN_HOLDER_IN_TREE` |
| [`oppia/oppia`](https://github.com/oppia/oppia) | 7 405 | 13 | 8 | 🟢 **0** | `OWN_HOLDER_ONLY` |
| [`learnhouse/learnhouse`](https://github.com/learnhouse/learnhouse) | 2 489 | 1 | 1 | 🟢 **0** | `OWN_HOLDER_ONLY` |
| [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | 1 345 | 14 | 🟡 **0 readable** | 0 | 🟡 unreadable class |
| [`Crosstalk-Solutions/project-nomad`](https://github.com/Crosstalk-Solutions/project-nomad) | 664 | 🟢 0 | 0 | 0 | `ROOT_ONLY` |
| [`frappe/lms`](https://github.com/frappe/lms) | 1 606 | 🟢 0 | 0 | 0 | `ROOT_ONLY` |
| [`overhangio/tutor`](https://github.com/overhangio/tutor) | 249 | 🟢 0 | 0 | 0 | `ROOT_ONLY` |
| [`adaptlearning/adapt_framework`](https://github.com/adaptlearning/adapt_framework) | 118 | 🟢 0 | 0 | 0 | `ROOT_ONLY` |
| [`openedx/codejail`](https://github.com/openedx/codejail) | 43 | 🟢 0 | 0 | 0 | `ROOT_ONLY` |
| [`openedx/XBlock`](https://github.com/openedx/XBlock) | 193 | 🟢 0 | 0 | 0 | `ROOT_ONLY` |
| [`academico-sis/academico`](https://github.com/academico-sis/academico) | 692 | 🟢 0 | 0 | 0 | `ROOT_ONLY` |

### 🔴 The two findings inside the 50% that change a delivery decision

🔴 **`instructure/canvas-lms` is AGPL-3.0 at the root and ships an MIT LTI Advantage implementation
four levels down.** `gems/lti-advantage/LICENSE.txt` is **MIT, held by a named individual (Nathan
Mills)**. 🟢 **The LTI Advantage code inside the dominant North-American LMS is the permissive part
of it** — which is a different sentence from anything this page has published about Canvas, and the
one a studio needs before it decides to reimplement rather than extract. (The same tree also carries
`rick olson`'s `attachment_fu` and `Coolite Inc.`'s date library.)

🆕 **`classroomio/classroomio` (AGPL-3.0) vendors ten MIT-licensed agent-skills packs** —
`skills/*/LICENSE`, held by three outside individuals. 🔵 **This is a 2026-shaped obligation**: the
skills are exactly the part a client redistributes, and their grants are not the platform's.

🔵 **The rest of the 50% is front-end vendoring and the FSF's own text**: Fonticons, Twitter's
Bootstrap, Tiny Technologies' editor, Michael Bostock's d3, Ivan Sagalaev's highlight.js, Adobe's
cmaps, the PDFium Authors, Google's Liberation data, Mozilla; plus **The Trustees of Columbia
University** and the Apache Software Foundation inside Sakai, and a Debian maintainer's packaging
copyright inside Kolibri. The FSF appears as a holder **21 times** — a vendored licence body, not a
third-party grant, and counted because a notice obligation attaches to it too.

### 🔴 Three defects this probe produced before it produced a finding — stated, because the first two were wrong in the direction of a finding

1. 🔴 **An empty path list counted as one path**, so seven of twenty rows were first reported as
   carrying a non-root licence file they do not have. `printf '%s\n' "$empty" | grep -c ''` is 1.
2. 🔴 **Sakai's `content-copyright` i18n bundles matched on the WORD "copyright"** and produced seven
   false grants out of translated UI strings.
3. 🔴 **A four-filename licence sweep over 16 candidate rows called `kstateome/lti-launch`
   unlicensed. Tree enumeration found `License.txt` — LGPL-3.0, 7 651 B.** One of this pass's two
   absence verdicts was false, which is `p288-agpl-casefold` biting this KB a second time, and is
   why the committed instrument matches case-insensitively and ships a regression test for it.

🟡 **And one limit that keeps 50% a floor rather than an estimate:** this instrument reads licence
**files**. A grant inside a source header — the `pipwerks` case p136 corrected — is invisible to it.
🔴 **`Crosstalk-Solutions/project-nomad` defeats the method entirely**: `ROOT_ONLY` over 664 paths,
while composing Kiwix, Kolibri and Ollama **as container images**, so its real third-party
obligations are nowhere in its tree.

### 🆕 One row added to the interoperability layer, and it is university-owned

| repo | licence *(payload-read)* | ★ | last push | holder class | why it is foundational |
|---|---|---|---|---|---|
| [`kstateome/lti-launch`](https://github.com/kstateome/lti-launch) | 🟢 **LGPL-3.0** (`License.txt`, 7 651 B; `pom.xml` `<licenses>` agrees) | **UNMEASURED** | **2026-09-30** | 🟢 **US public university** (Kansas State University, Office of Mediated Education) | 🔴 **The only repository in this KB that maps a verified LTI launch onto a per-user OAuth grant** — `ltiSession.getEid()` → `OauthTokenService.getRefreshToken(userId)` → Canvas as that user. LTI **1.1** (OAuth 1.0a consumer model), Spring/Java, 34 paths. 🟢 **The first university-owned row in this page's standards tier**, and the pattern `P13` now copies. 🔴 LGPL + Java: port the pattern, not the file |

---

**Pass 135, 2026-10-11.** 🟢 **The assessment and course-content layer is added — the part of the
standards stack p134's interoperability section pointed at and did not reach.** p134 finished with
LTI, OneRoster, Ed-Fi and xAPI. Finishing the register (`ACTION BN`) found that **SCORM carries an
order of magnitude more code than any of them**, and that two of the six remaining standards have
almost no supply at all. Rows are below under *The assessment and content layer*.

🔴 **Every licence cell added this pass was established by hash, and the method matters more than
any single row.** `compose/code/p135-licence-sha-identity` discharges `ACTION BP` and **refutes its
premise**: not one payload in a 26-repo corpus is a whitespace variant of its canonical text. They
differ by **line wrap width** (SPDX wraps at ~105 columns, real `LICENSE` files at ~72), by
**typographic punctuation** (SPDX's GPL-3.0 uses curly quotes; shipped `COPYING` files use ASCII),
and by **the licence steward editing its own text** — two such edits are now known for GNU, the
`http`→`https` change and 🔴 **the FSF's move of `why-not-lgpl.html` from `/licenses/` to
`/philosophy/`, which was the entire remaining difference on five GPL-3.0 payloads.**
🟢 **Result: 21 of 26 resolved to a named SPDX identifier; the 5 that did not each have a named
cause, and 2 of them are correctly unmatched** because the text genuinely is not canonical.

🔴 **Two rows added this pass carry the defect this page exists to catch.**
[`pipwerks/scorm-api-wrapper`](https://github.com/pipwerks/scorm-api-wrapper) — **391★, 130 forks,
pushed 2026-09-18 — has no licence file under any of eight probed filenames**, and
[`adlnet/SCORM-to-xAPI-Wrapper`](https://github.com/adlnet/SCORM-to-xAPI-Wrapper) is published
**unlicensed and archived by the US Department of Defense body that authored both SCORM and xAPI.**
Neither can be used in a client deliverable. Both are measured absent, not inferred.
<!--corrected by p136: see "The pipwerks correction" below. The `pipwerks` half of this paragraph is
wrong about rights and right about files -- a grant IS declared, in `package.json` and the source
header. The `adlnet` half is not re-measured this pass and stands as written.-->

## 🔴 The `pipwerks` correction — `ACTION BR`, and the sentence this page got wrong

**Pass 136, 2026-10-11.** `ACTION BR` asked for the **dependency closure** of the unlicensed
`pipwerks/scorm-api-wrapper` across this KB's own rows, predicting refutation *"if no published row
depends on it."* 🔴 **The action was discharged and it answered a bigger question than it asked: the
premise of five pages of this KB is wrong.**

| what p135 published | what p136 measured |
|---|---|
| *"no licence file exists under 8 probed filenames"* | 🟢 **TRUE.** Re-confirmed; the repository's whole tree is `package.json`, `readme.md` and three source files |
| *"there is no grant, so there is no right to use it"* | 🔴 **FALSE.** `package.json` carries `"license": "MIT-style license: http://pipwerks.mit-license.org/"`, and `src/JavaScript/SCORM_API_wrapper.js` lines 11–12 carry *"Copyright (c) Philip Hutchison / MIT-style license: …"* |
| *"391★, 130 forks, pushed 2026-09-18"* — a live dependency | 🔴 **HEAD commit is 2018-09-06.** The manifest version is `1.1.20160322`. `pushed_at` moved in 2026; the code did not |
| *"the blast radius is unmeasured"* | 🟢 **Measured. One** published row on this KB's pages depends on it |

🟢 **The one dependant, and how it hides.** Seven manifest types were probed across the 324 repo
rows on this KB's non-log pages; **150 rows exposed at least one manifest**, and the only
`pipwerks` hit in any of them is **pipwerks' own `package.json`**. 🔴 **A manifest probe is the
wrong instrument**: [`numbas/Numbas`](https://github.com/numbas/Numbas) (Apache-2.0, Newcastle
University) **vendors the file** at `runtime/scripts/SCORM_API_wrapper.js` — version
**`v1.1.20121005`**, four years behind upstream's own manifest — with the copyright and MIT-style
header **intact**. GitHub code search finds **293 files** named `SCORM_API_wrapper.js` carrying that
header, including [`Lumieducation/Lumi`](https://github.com/Lumieducation/Lumi) and
[`sr258/scorm-h5p-wrapper`](https://github.com/sr258/scorm-h5p-wrapper), both in the H5P family this
KB tables on `verticals/solutions.md`.

🔵 **So the rule this page should carry is about the grant's LOCATION, not its existence.** A
filename probe measures files. A grant can live in a package manifest, a source header, or a URL —
and when it travels inside a **vendored file**, the header travels with it while the version does
not. 🔴 **The residual risk is real but different from the one this page published**: the terms are
declared, *unread* (the host is refused in this channel — DNS failure on `http`, 403 CONNECT on
`https`) and **not an SPDX identifier**, since *"MIT-style"* names no standard text.

**Pass 134, 2026-10-11.** 🟢 **This page gains the layer it was missing: the interoperability
standards an institution procures against.** `instructure/ims-lti` has sat at the bottom of this
page for many passes, described correctly as *"the integration path that avoids touching platform
source"* — and this KB never followed that sentence anywhere. Followed, it leads to **`Cvmcosta/ltijs`
(Apache-2.0, 373★, pushed 2026-10-06)**, which is larger and far more active than the row that
pointed at it, and to the first **vendor- and government-owned** repositories this KB has ever
tabled. See the new section *The interoperability layer* below, and `agents/top.md` → *Standards-native
agents*.

🟢 **`ACTION BG` is also discharged on this page** — the mirror detector p133 asked for was built and
run, one of its three proposed signals works, and `P133-A`'s inference about Canvas is narrowed. See
*The mirror rule, measured* below.

**Pass 132, 2026-10-11.** p131's rows carried forward unchanged (they were verified hours earlier
in the same date window); 🔴 **one new row changes this page's headline recommendation and refutes
this page's own flagship gap** — see `README.md` → Pass 132, `P132-C`. These are the systems a
client already runs, or would sensibly adopt, and that AI work gets attached to. Licence is the
first column that matters: it decides whether Globant can ship a derivative at all.

🔴 **Read this before trusting a licence cell.** GitHub's `license.spdx_id` reports **`NOASSERTION`
("Other")** whenever its matcher does not recognise a `LICENSE` file as a known template. That is
*not* a finding of "no grant", and p130 published it as one. Where this KB has **read the payload**,
the payload wins and the cell below says so.

## The platforms

| repo | licence | stars | last push | origin | why it is foundational |
|---|---|---|---|---|---|
| [`bigbluebutton/bigbluebutton`](https://github.com/bigbluebutton/bigbluebutton) | LGPL-3.0 | **9 241** | 2026-10-10 | North America (Blindside Networks, Canada) | The open virtual-classroom stack: WebRTC audio/video, whiteboard, breakouts, recordings. LGPL means linking is fine; modifying the library itself carries reciprocity. The place live-session AI (transcription, attention, summarisation) attaches. |
| [`openedx/openedx-platform`](https://github.com/openedx/openedx-platform) | AGPL-3.0 | **8 195** | 2026-10-10 | North America (Open edX / Axim) | The LMS + Studio behind MOOC-scale deployments. **Renamed:** this repo was `openedx/edx-platform`; the old URL still resolves and the README says "formerly known as edx-platform". Write the new name — earlier passes of this KB cite the old one. |
| [`moodle/moodle`](https://github.com/moodle/moodle) | GPL-3.0 | **7 473** | 2026-10-09 | APAC (Moodle HQ, Perth, Australia) | The most deployed LMS in the world, ~2 000 plugins. **Important for delivery:** this GitHub repo is a *public mirror* of `git.moodle.org` — pull requests do not go here, and it publishes no GitHub releases. Contribution goes through Moodle's own tracker and git server. 🟢 **Its mirror is live (pushed 2026-10-09), which is exactly why Canvas's frozen one was mistaken for a quiet project rather than a stopped job.** |
| [`instructure/canvas-lms`](https://github.com/instructure/canvas-lms) | AGPL-3.0 | **6 863** | 2026-04-30 **(mirror frozen — not inactivity)** | North America (Instructure, US) | The dominant LMS in North American higher ed and the one with the richest third-party API surface — which is why every MCP connector on the agent shelf targets Canvas first. 🔴 **Corrected by p133: this KB called it "the quietest of the major platforms" for four passes and that was a measurement error.** The repo's own topics include **`gerrit-mirror`**, and `instructure/analytics` carries the identical `pushed_at` **one second later** (14:52:10 / 14:52:11 on 2026-04-30) — a batch export, not a human push. 🟡 **The correct statement: the public GitHub mirror has been frozen since 2026-04-30, so GitHub is not a usable activity signal for Canvas, and anyone diffing this tree to track upstream has been reading a stale copy for five months.** Development is in Instructure's Gerrit; `updated_at` still moves daily. |
| [`oppia/oppia`](https://github.com/oppia/oppia) | **Apache-2.0** | **6 845** | 2026-10-11 | Global (Oppia Foundation) | An online learning platform built around structured, explorable lessons with built-in misconception handling. **The only major education platform under a permissive licence** — so the one a client can fork into a closed product without reciprocity. Underrated for exactly that reason. Android client: [`oppia/oppia-android`](https://github.com/oppia/oppia-android) (Apache-2.0, 418). |
| [`frappe/lms`](https://github.com/frappe/lms) | AGPL-3.0 | **3 299** | 2026-10-11 | APAC (Frappe, India) | Modern, actively developed LMS on the Frappe framework — so it sits next to Frappe/ERPNext finance and HR data without integration work. The strongest APAC-origin platform here. |
| [`learnhouse/learnhouse`](https://github.com/learnhouse/learnhouse) | AGPL-3.0 | 2 336 | 2026-10-11 | unplaced | Next-generation learning platform, Python/Next.js, AI features first-class rather than bolted on. Young, fast-moving. |
| [`classroomio/classroomio`](https://github.com/classroomio/classroomio) | AGPL-3.0 | 1 717 | 2026-10-11 | unplaced | Education platform aimed at companies running cohort training. Relevant to corporate-L&D engagements rather than academic ones. |
| [`sakaiproject/sakai`](https://github.com/sakaiproject/sakai) | **ECL-2.0** | 1 237 | 2026-10-09 | North America (Apereo Foundation) | Long-lived Java academic LMS. ECL-2.0 is Apache-2.0 with an educational-community patent tweak — **permissive**, and the licence most people misread as restrictive. Strong fit where a client already runs Java/Oracle estate. |
| [`overhangio/tutor`](https://github.com/overhangio/tutor) | AGPL-3.0 | 1 127 | 2026-10-08 | EMEA (Overhang.IO, France) | The Docker-based Open edX distribution — in practice *the* supported way to stand up and upgrade Open edX. A large first-party plugin ecosystem, all AGPL-3.0: `tutor-mfe` (micro-frontends), `tutor-cairn` (real-time analytics), `tutor-discovery`, `tutor-credentials`, `tutor-jupyter`, `openedx-scorm-xblock`. If the engagement is Open edX, it is a Tutor engagement. |
| [`learningequality/kolibri`](https://github.com/learningequality/kolibri) | **MIT** | 1 141 | 2026-10-10 | Global (Learning Equality) | Offline-first learning platform for low- and no-connectivity classrooms; content syncs by LAN or USB. **MIT-licensed**, which with its offline design makes it the single best base for rural LATAM, African and South Asian deployments. Content tooling: [`learningequality/studio`](https://github.com/learningequality/studio) (MIT, 192). |
| [`chamilo/chamilo-lms`](https://github.com/chamilo/chamilo-lms) | GPL-3.0 | 1 009 | 2026-10-10 | EMEA (Chamilo Association, Belgium) | LMS built around ease of use and accessibility, with real institutional adoption in Francophone Europe and Spanish-speaking LATAM. The most LATAM-relevant of the EMEA-origin platforms. |
| [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | 🟢 **LGPL-3.0** (payload-read) | 886 | 2026-10-09 | APAC (India) | Education *ERP* — admissions, students, faculty, timetabling, fees — built on Odoo. The natural target for the administrative automation nobody else serves. 🔴 **Licence corrected by p131.** GitHub's API reports `NOASSERTION` and p130 published that as "review terms before use". This KB had already **read `master/LICENSE` in full — 8 241 bytes, genuinely LGPL-3.0** — and used that read to *retract* an even earlier "no grant" row. p130 reinstated the retracted claim by trusting the API field over its own evidence. **LGPL on an LGPL Odoo base: linking is fine, modifying the module itself carries reciprocity.** |
| [`ILIAS-eLearning/ILIAS`](https://github.com/ILIAS-eLearning/ILIAS) | GPL-3.0 | 505 | 2026-10-10 | EMEA (Germany) | Mature German LMS with strong standards and accessibility compliance — relevant precisely because EMEA procurement weighs those heavily. |
| [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) | **NOASSERTION** | 447 | 2026-10-09 | EMEA (frentix, Switzerland) | Java LMS widely deployed in Swiss/German universities. Licence reads as "Other" to GitHub (it is Apache-2.0-based in its own documentation) — **verify before building**. |

## The offline / low-connectivity stack (added by p132 — and it refutes this page's own gap)

🔴 **This page has carried, for several passes, that "the offline slot is the cleanest unclaimed
opportunity in this KB". It is not unclaimed.** It is occupied by the second-largest repository
anywhere in this KB.

| repo | licence | stars | origin | why it is foundational |
|---|---|---|---|---|
| [`Crosstalk-Solutions/project-nomad`](https://github.com/Crosstalk-Solutions/project-nomad) | 🟢 **Apache-2.0** | **39 444** | unplaced | **Offline-first knowledge and education server**: Wikipedia, thousands of books, courses, maps and optional local AI, all on hardware the client owns with no internet required. Architecturally a **Docker orchestration layer over containerised tools** — **Kiwix** powers the Information Library, **Kolibri** powers the Education Platform, **Ollama** powers the AI Assistant (the installer provisions Ollama on the host; an external OpenAI-compatible endpoint is also supported). 🟢 **Permissive, so a client can ship a derivative.** 850 commits, updated the day of this pass. |
| [`karissafuller/project-nomad-macos`](https://github.com/karissafuller/project-nomad-macos) | 🟡 **UNREAD** | 20 | unplaced | macOS / Apple Silicon port, bundling Ollama, Open WebUI, Kiwix, Kolibri and FlatNotes. Useful as a single-machine pilot before committing to the Docker stack. Licence not measured this pass. |
| [`Tushar-cy/Offline-AI`](https://github.com/Tushar-cy/Offline-AI) | 🟡 **UNREAD** | 2 | **APAC (India)** | Offline LMS for Class 10 Maths and Science on the Indian curriculum: FastAPI + React + RAG over structured chapter data with a local Ollama model, gamified quizzes, LAN-only operation, and a claimed Kolibri integration. 🔴 **Duplicate pair** with [`Tushar-cy/Ai-edge-learning-hub`](https://github.com/Tushar-cy/Ai-edge-learning-hub) (same owner, byte-identical description). Small, but the only row that targets a *named national curriculum* offline. |

🔵 **Why eleven passes missed it, and why the probe was not at fault.** p131 ran `kolibri stars:>2`,
got 86 repos, correctly resolved 3 to the Learning Equality family and 0 with AI. **The probe was
valid; the conclusion was false.** NOMAD *composes* Kolibri as a container and never names it in
its description — the dependency appears only in the README architecture. **A dependency is not
always visible in the metadata of the thing that depends on it.**

🟢 **What this changes for an engagement.** The low-connectivity offer stops being *"build an
offline tutor"* and becomes *"deploy and extend an Apache-2.0 stack that already composes content,
library and local inference"* — faster, cheaper and far more defensible in a procurement
conversation. Kolibri (MIT) remains the right content layer; what changed is that the integration
around it already exists. See `compose/patterns.md` → P2.

## Administrative automation — the first optimiser (added by p132)

| repo | licence | stars | origin | what it gives you |
|---|---|---|---|---|
| [`saytooyum/AI-Based-Timetable-Generation-System`](https://github.com/saytooyum/AI-Based-Timetable-Generation-System) | **MIT** | 1 | **APAC (India)** | Conflict-free academic timetable generation under **India's NEP 2020**: electives, faculty availability, courses, rooms, balanced workloads, scenario simulation, manual overrides, exports, and a natural-language interface over MCP. 🟢 **The "most-cited driver, least-served tier" finally has a repo, and it is an optimiser rather than an LLM wrapper.** 🔴 One star — a reference design, not a dependency. |

## 🟢 The interoperability layer — how AI attaches without touching platform source *(new, p134)*

🔴 **Read this section before proposing a fork of anything above it.** Every platform in *The
platforms* is AGPL-3.0, GPL-3.0, LGPL-3.0 or ECL-2.0, and this KB spends a lot of words on which
reciprocity obligation bites when. 🟢 **The standards below make most of that moot:** a tool
launched over **LTI 1.3** runs as a separate application with its own licence, talking to the LMS
over HTTP. It never links platform code, so it inherits **no** copyleft obligation from Moodle,
Canvas or Open edX — and it is *invited in* by a client ID the institution issues and can revoke,
rather than holding a user's password.

| repo | licence | stars | last push | holder class | why it is foundational |
|---|---|---|---|---|---|
| [`Cvmcosta/ltijs`](https://github.com/Cvmcosta/ltijs) | 🟢 **Apache-2.0** (payload-read) | **373** | **2026-10-06** | named individual | 🟢 **The reference LTI 1.3 Advantage tool provider, and the headline addition to this page.** OIDC launch, Deep Linking, AGS grade passback, NRPS rosters. **1.8× the stars of `ims-lti` and pushed five days before this pass** — where `ims-lti` is Instructure's library for *their* platform, this is the platform-independent one. If an engagement puts AI inside an existing LMS, this is the integration dependency. |
| [`dmitry-viskov/pylti1.3`](https://github.com/dmitry-viskov/pylti1.3) | 🟢 **MIT** (payload-read) | 138 | 2024-08-18 | named individual | The Python LTI 1.3 Advantage library (Django/Flask). 🔴 **Dormant ~2 years**, and that is the most consequential staleness on this page: Python is where the agent frameworks live, so the LTI binding for an agent build is the least-maintained link in the chain. |
| [`Ed-Fi-Alliance-OSS/edfi-oneroster`](https://github.com/Ed-Fi-Alliance-OSS/edfi-oneroster) | 🟢 **Apache-2.0** (payload-read) | 6 | **2026-10-09** | 🟢 **standards body** | Serves a **OneRoster 1.2 API from an Ed-Fi ODS**. The bridge between the two US K-12 data standards, written by the body that owns one of them. 🟢 **Stars are the wrong measure here: this is the row that makes a US K-12 rostering story procurement-safe.** |
| [`googleworkspace/oneroster-integration-conformance-tests`](https://github.com/googleworkspace/oneroster-integration-conformance-tests) | 🟢 **Apache-2.0** (payload-read) | 7 | 2026-07-30 | 🟢 **platform vendor (Google)** | Conformance tests for a OneRoster integration. 🟢 **The only test suite in this KB that proves an integration correct rather than asserting it.** |
| [`trilogy-group/oneroster-ts`](https://github.com/trilogy-group/oneroster-ts) | 🟢 **0BSD** (payload-read, 711 B) | 10 | 2026-05-11 | named individual (noreply addr) | TypeScript OneRoster SDK. 🟢 **0BSD — the most permissive licence in this KB; it drops even attribution**, so a derivative carries no notice obligation at all. |
| [`AlexMeiling/wiseflow-api-integration-packages`](https://github.com/AlexMeiling/wiseflow-api-integration-packages) | 🟢 **MIT** (payload-read; holder **"UNIwise ApS"**) | 3 | 2026-06-11 | 🟢 **platform vendor (EMEA, Denmark)** | Integration packages for the **WISEflow** assessment platform — user creation, flow setup, assessor allocation, **grade passback**. 🟢 **A European assessment vendor publishing its own MIT integration path**: the cleanest EMEA counterparty in this KB, and the opposite of the unsanctioned-connector problem. |
| [`openfun/warren`](https://github.com/openfun/warren) | **MIT** | 17 | **2026-10-11** | 🟢 **national public operator (EMEA, France)** | Learning-analytics visualisation over **xAPI**. Same owner as [`openfun/richie`](https://github.com/openfun/richie) below — 🟢 **France Université Numérique now gives this KB two MIT rows, and this one was pushed on the day of this pass.** The dashboard layer over an LRS. |
| [`DavidLMS/learnmcp-xapi`](https://github.com/DavidLMS/learnmcp-xapi) | **MIT** | 15 | 2025-08-29 | named individual | 🟢 **The only repo found that bridges an AI agent to a sanctioned standard**: an MCP server that records and retrieves learning activity through an xAPI Learning Record Store. 🔴 **15 stars, last push ~14 months ago** — load-bearing and unmaintained, which is precisely why it is a build item rather than a dependency. Full tier in `agents/top.md`. |
| [`adlnet/MasterObjectModel`](https://github.com/adlnet/MasterObjectModel) | **Apache-2.0** | 12 | 2025-07-03 | 🟢 **government (US DoD ADL Initiative)** | xAPI profile for lifetime learner tracking, from the body that authored xAPI. The modelling reference for an LRS schema. |
| [`mn-mde-edfi/MDE-Ed-Fi-ODS-API-SDK`](https://github.com/mn-mde-edfi/MDE-Ed-Fi-ODS-API-SDK) | 🔴 **no licence field** | 0 | 2026-04-14 | 🟢 **government (Minnesota Dept of Education)** | C# SDK for a US state's Ed-Fi ODS API. 🔴 **The best-owned row on this page and unusable, because it carries no grant** — the recurring shape of this KB in one line. |

🔵 **The licence asymmetry is worth stating plainly, because it inverts this page's usual advice.**
*The platforms* are copyleft almost without exception and the one permissive major platform
(`oppia/oppia`, Apache-2.0) is the one nobody asks for. 🟢 **The interoperability layer is
permissive almost without exception** — Apache-2.0, MIT and 0BSD, with named vendor and government
holders. **So the licence-safest way to build on a copyleft platform is to not build on it at all,
and to attach over a standard instead.**

🔴 **And the honest limit of this section:** these are libraries, conformance tests and profiles.
They are the plumbing a security review passes. **None of them contains any AI**, and the one row
that joins them to an agent has 15 stars and has not been pushed in over a year.

## 🟢 The mirror rule, measured — `ACTION BG` discharged *(p134)*

p133 corrected a four-pass claim that `instructure/canvas-lms` was *"the quietest of the major
platforms"*, having found the topic `gerrit-mirror` and a sibling repo sharing its `pushed_at` one
second later. 🟢 **`ACTION BG` asked for that to become a detector before any further freshness
claim published. It was built and run over the 40 most-recently-updated `instructure` repositories,
and the result is mixed in a useful way.**

| proposed signal | verdict | measurement |
|---|---|---|
| **a topic containing *mirror*** | 🟢 **WORKS — and the defect is a lane, not a row** | **5 of 40** repos carry `gerrit-mirror`: `canvas-lms`, `dockerfiles`, `switchman`, `screencap`, `outrigger`. `ACTION BG`'s refutation condition (*"refuted if `canvas-lms` is the only mirror"*) is **not met** |
| **two repos in an org sharing `pushed_at` to the second** | 🔴 **DOES NOT GENERALISE — retire it** | across 40 repos, **no timestamp is shared by more than one repo.** p133's own evidence was two *adjacent* seconds (`:10` and `:11`), not a shared one; generalised into a detector it finds nothing |
| **a README naming an upstream elsewhere** | 🟡 **NOT TESTED** this pass | would need a payload read per repo; the topic field is cheaper and sufficient |

🔴 **And the measurement narrows `P133-A`'s inference.** p133 concluded 2026-04-30 was *"the date
their export to GitHub stopped running"*. 🟢 **It was not: sibling mirrors in the same org received
exports on 2026-09-30 (`switchman`) and 2026-10-08 (`dockerfiles`)** — three days before this pass.
**The Gerrit export job is running; `canvas-lms` specifically stopped receiving it.** Whether that
is a disabled export, a renamed upstream branch or a deliberate halt is not visible from here, and
this KB should not guess. 🟢 **p133's operative conclusion survives intact and is the one to quote:
`pushed_at` on `canvas-lms` is not an activity signal.** Its stronger causal story does not.

🟢 **The control that makes the rule usable:** [`instructure/ims-lti`](https://github.com/instructure/ims-lti)
carries **no** mirror topic and was pushed **2026-10-02**. **So within one org, some repos are
mirrors and some are GitHub-native, and the topic tells you which.** `pushed_at` is a valid
freshness signal for `ims-lti` and an invalid one for `canvas-lms` — which means freshness must be
checked per repo, never per organisation.

### 🔴 p136 runs the rule over the whole corpus — and 44% of its hits are not mirrors at all

`ACTION BU` asked for p135's successor signal (README **byte-identity**, which p135 called *"a
verdict"* against licence grouping's *"lead"*) to be applied corpus-wide. **1 389 READMEs fetched
over 1 528 published rows → 71 byte-identical clusters, 25 of them cross-owner** — twelve times
`ACTION BU`'s refutation threshold, so **not refuted**. 🔴 **But the word "verdict" does not
survive:**

| lineage verdict | clusters | what it means here |
|---|---|---|
| `ALIAS` — **identical ref set** | 🔴 **11** | **One repository under two slugs.** GitHub keeps answering a renamed owner or repo name, so the "two owners" are one |
| `DIVERGED_FORK` — shared commit shas | 5 | A real fork; count the connector once |
| `FORK_AT_TIP` — same HEAD, different ref sets | 4 | A fork that has not diverged yet |
| `ATTRIBUTION_STRIPPED_COPY` — identical root tree, **zero** shared commits | 1 | the ENEM cluster (`ACTION BW`, below) |
| `SQUASHED_COPY` — one side a single commit | 1 | `0awei0/kt`, and it **dropped the upstream MIT file** |
| `UNRESOLVED` — measurement not taken | 🔵 3 | **said, not guessed** |

🔴 **One of the eleven aliases lands on a conclusion this KB published.** `agents/trending.md`
reasoned about `theopenem/OneRoster.NET` versus `jdolny/OneRoster.NET` — *"both licences name
`theopenem` as copyright … so pin `theopenem`"* — when the two slugs have an **identical ref set**
(`3f4540f9706d9099`) and are **one repository**. The pin is harmless; the reasoning was about a
distinction that does not exist. 🟡 `KI-Campus/LRS` and `openHPI/openLRS` are the same case across
*both* a rename and a transfer.

🔴 **And 37 further clusters are this KB citing one repository under two spellings** — `Elgg/Elgg`
and `elgg/elgg`, `Schroedinger-Hat/certo` under **three**, eight `Opetushallitus/*` pairs. That is
`p443`'s case-collision class measured across the whole corpus for the first time.

🟢 **The rule, generalised for this page.** Freshness must be checked per repo (p134).
**Identity must be checked before freshness**: resolve the slug to a repository by **ref set**, then
ask about forks, then ask about dates. Instrument, six verdicts and 10 tests:
`compose/code/p136-lineage-verdict/`.

## 🟢 The assessment and content layer — added by p135

The standards an institution procures against do not stop at rostering and grade passback. Two more
carry real code: **SCORM**, which packages and tracks course content, and **QTI**, which carries
assessment items. This is where an AI engagement touching *content* or *assessment* attaches.

| system | repo | licence *(hash-verified)* | ★ | pushed | owner | why it is foundational |
|---|---|---|---|---|---|---|
| **Adapt Framework** | [`adaptlearning/adapt_framework`](https://github.com/adaptlearning/adapt_framework) | 🔴 **GPL-3.0** 🆕 *(p136: `UNMATCHED` → `RESOLVED` at ratio `0.997431`, holder **"2013 ADAPT LEARNING"**, 11 opcodes and not one an added clause)* | **630** | **2026-10-10** | Adapt community | The largest repo in the whole standards stack. Authoring toolkit producing responsive, accessible, multi-language courses that emit **both SCORM and xAPI**. 🔵 Copyleft: run it as a tool, do not link it |
| **OpenOlat** | [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) | 🟡 **Apache-2.0 + attribution** | **447** | 2026-10-09 | frentix GmbH / Univ. of Zurich | 🟢 **A full Java LMS this KB had never tabled**, with QTI, SCORM, curriculum management, assessment and lecture management built in. The permissive full-featured LMS this page's flagship gap says does not exist — see the verdict below |
| **scorm-again** | [`jcputney/scorm-again`](https://github.com/jcputney/scorm-again) | 🟢 **MIT** | **354** | 2026-10-09 | individual | The modern SCORM 1.2 / 2004 runtime. **Offline-first**, TypeScript, actively maintained. 🟢 **The permissive replacement for the unlicensed `pipwerks` wrapper** |
| **Numbas** | [`numbas/Numbas`](https://github.com/numbas/Numbas) | 🟢 **Apache-2.0** | 215 | 2026-10-09 | 🟢 **Newcastle University (UK)** | Browser-based e-assessment, strongest in mathematics, SCORM-packageable. **Institution-owned and permissive** — the cleanest base for assessment work before the 2027 clocks. 🆕 **p136: it vendors `pipwerks`' SCORM wrapper** (`runtime/scripts/SCORM_API_wrapper.js`, `v1.1.20121005`, header intact) — the only `pipwerks` dependant on this KB's pages, and a reminder that Apache-2.0 at the root says nothing about a vendored subtree |
| **QTI 3 item player** | [`amp-up-io/qti3-item-player`](https://github.com/amp-up-io/qti3-item-player) | 🟢 **MIT** | 30 | 2026-04-07 | amp-up.io | The reference renderer for QTI 3 assessment items, with a four-component sibling family from the same vendor |
| **Mentingo** | [`Selleo/mentingo`](https://github.com/Selleo/mentingo) | 🟢 **MIT** | 92 | **2026-10-10** | Selleo (PL) | 🟢 **An AI-native LMS under a permissive licence** — AI mentor, role-play, SCORM and xAPI, white-label, self-hosted. Small, but the only row where the AI is the platform's architecture rather than a bolt-on |
| **1EdTech validator** | [`1EdTech/digital-credentials-public-validator`](https://github.com/1EdTech/digital-credentials-public-validator) | 🟢 **Apache-2.0** | 17 | 2026-09-23 | 🟢 **1EdTech (the standards body)** | Conformance validation for **Open Badges and Comprehensive Learner Record**. The second conformance suite this KB has found, and the steward's own |

🔴 **Do not reach for these two, and the reason is the licence, not the code**

| repo | ★ | problem |
|---|---|---|
| [`pipwerks/scorm-api-wrapper`](https://github.com/pipwerks/scorm-api-wrapper) | **391** | 🆕 **p136: the reason changed.** The grant is **declared by reference** (`package.json` + source header, *"MIT-style license"* at a host refused in this channel) — so *"confers no rights whatsoever"* is withdrawn. Reach instead for `scorm-again` because **HEAD here is 2018-09-06** and *"MIT-style"* is not an SPDX id, not because there is no grant |
| [`cybercussion/SCOBot`](https://github.com/cybercussion/SCOBot) | 164 | **CC-BY-SA-4.0, and the file is only the 837-byte human-readable deed.** ShareAlike copyleft, no patent grant, and a content licence applied to code |

### 🔴 What this layer does NOT have

| standard | supply measured this pass |
|---|---|
| **Caliper Analytics** | 🔴 **One repository, 0★, no licence, last touched 2023.** The standard for carrying learning events to an analytics layer has no usable open-source client in any language |
| **Comprehensive Learner Record** | 🔴 **One real repository** — the 1EdTech validator above. The other two hits are an empty 2018 repo and a student project |
| **LTI Deep Linking**, probed alone | 🔴 **One repository, which declares in its own description that Deep Linking is not supported.** In practice it exists only inside `ltijs` |

## Supporting infrastructure

| repo | licence | stars | what it gives you |
|---|---|---|---|
| [`openedx/XBlock`](https://github.com/openedx/XBlock) | **Apache-2.0** | 470 | The component framework for custom learning activities inside Open edX. Permissively licensed even though the platform around it is AGPL — so a custom XBlock is the lowest-friction way to put an AI activity inside Open edX. |
| [`openedx/codejail`](https://github.com/openedx/codejail) | **Apache-2.0** | 476 | Sandboxed execution of untrusted code. Directly reusable wherever an agent runs learner-submitted or model-generated code — an auto-grader for programming courses, for instance. |
| [`jcputney/scorm-again`](https://github.com/jcputney/scorm-again) | **MIT** | 354 | Modern SCORM/AICC/xAPI runtime in TypeScript. The bridge between legacy courseware a client already owns and anything new. |
| [`openfun/richie`](https://github.com/openfun/richie) | **MIT** | 316 | Django/React CMS for building course catalogues and education portals in front of Open edX. From France Université Numérique, so it is proven at national scale in EMEA. |
| [`h5p/h5p-interactive-video`](https://github.com/h5p/h5p-interactive-video) | **MIT** | 263 | The H5P interactive-content family (Norway); the Moodle binding is [`h5p/moodle-mod_hvp`](https://github.com/h5p/moodle-mod_hvp) (GPL-3.0, 157). The standard way to ship interactive activities into an existing LMS. |
| [`academico-sis/academico`](https://github.com/academico-sis/academico) | **MIT** | 404 | Laravel/Filament school-management platform for small and mid-size institutions. MIT, so the most forkable administrative base here. |
| [`instructure/ims-lti`](https://github.com/instructure/ims-lti) | **MIT** | 203 | LTI tool-provider/consumer library. LTI is how an external AI tool gets launched from inside any compliant LMS — the integration path that avoids touching platform source, and therefore avoids AGPL reciprocity entirely. |

## The system-of-record tier (restored by p131)

p130's declared gaps said *"`openeducat_erp` (licence unclear) and `academico` (small) are the whole
field."* 🔴 **They are not.** This KB read a system-of-record tier in an earlier pass and p130's
rewrite dropped it. Restored here, because "there is no open-source SIS" and "every open-source SIS
is copyleft" are completely different briefings for a client.

| repo | licence | why it matters | the catch |
|---|---|---|---|
| [`frappe/education`](https://github.com/frappe/education) | **NOASSERTION** (API) — read terms | **662★**, pushed 2026-10-05, 454 forks. Full school management on Frappe: students, programmes, fees, assessment. Sits beside ERPNext finance/HR with no integration work. | Licence does not resolve to an OSI identifier via the API; GPL-3.0 in the Frappe family's own documentation. **Read `LICENSE` before committing** — this is exactly the row class p130 got wrong. |
| [`openeducat/openeducat_erp`](https://github.com/openeducat/openeducat_erp) | 🟢 **LGPL-3.0** (payload-read) | 886★. The Odoo-based ERP; the broadest functional coverage of the tier. | Odoo module, so you inherit the Odoo ecosystem *and* its constraints. |
| [`academico-sis/academico`](https://github.com/academico-sis/academico) | **MIT** | **404★**, pushed 2026-10-07. Laravel/Filament. **The only permissive SIS**, so the only forkable base for a closed client product. Carries the topic `student-information-system`. | Small, and aimed at small-to-mid institutions rather than a university of record. |
| **RosarioSIS** | GPL-2.0 | A genuine student information system with real deployments. | GPL-2.0 — the most restrictive option here. |
| **Gibbon** | GPL-3.0 | School platform with a long institutional track record. | GPL-3.0 reciprocity. |
| **openSIS** / **Fedena** | copyleft / mixed | Named in this KB's earlier reads of the tier; both long-lived. | Neither is permissive; verify the current edition's terms, since both have had commercial forks. |

🔵 **Provenance of the four rows without links.** RosarioSIS, Gibbon, openSIS and Fedena are
carried from **this KB's own earlier read of the tier** (`agents/trending.md:5160`, which recorded
`RosarioSIS mobile@899f6da` GPL-2.0, `Gibbon v31.0.00@683d2c4` GPL-3.0 and `OpenEduCat 19.0@1c95cef`
LGPL-3.0 at specific commits). 🔴 **They were NOT re-verified this pass and are deliberately listed
without links** — a row this pass did not measure does not get presented as one it did. Re-verify
before quoting them to a client; the three linked rows above were verified this pass and are in
`evidence/verified-repos.2026-10-11-p131.tsv`.

**The honest summary for a client:** there are **at least six** open-source systems of record. Exactly
**one** (`academico`, MIT) can become a closed derivative; one more (`openeducat_erp`, LGPL-3.0)
permits linking without reciprocity. The rest are GPL-family. 🔴 **So the gap is not supply — it is
that the system-of-record tier is almost entirely copyleft**, which is a licensing conversation at
the start of an engagement, not a missing-software conversation.

## How to choose, in one paragraph

If the client already runs a platform, the platform is chosen and the only question is the
attachment point: **LTI** (`ims-lti`) to stay outside the codebase and outside AGPL reciprocity, an
**XBlock** (Apache-2.0) inside Open edX, a **plugin** inside Moodle (GPL-3.0 reciprocity on the
plugin), or **MCP** against the platform API (see `agents/top.md`). If the client is greenfield and
wants to own a closed derivative, the shortlist is short because of licensing, not features:
**`oppia/oppia`** (Apache-2.0), **`sakaiproject/sakai`** (ECL-2.0), **`learningequality/kolibri`**
(MIT) and **`academico-sis/academico`** (MIT). Everything else on this page is copyleft, and the
AGPL rows commit a hosted-service client to reciprocal source release. 🟢 **And if the constraint
is connectivity rather than licensing, start from `Crosstalk-Solutions/project-nomad`
(Apache-2.0, 39 444★) instead of assembling the stack yourself** — it already composes Kolibri,
Kiwix and a local model, and it is permissive enough to fork.

## Declared gaps

- **No permissively licensed, full-featured LMS at the scale of Moodle or Canvas.** Oppia
  (Apache-2.0) and Sakai (ECL-2.0) are the permissive options and neither is a drop-in replacement
  for either. 🟢 **SURVIVES.**
- ~~**No open-source student information system of record.** `openeducat_erp` (licence unclear) and
  `academico` (small) are the whole field.~~ 🔴 **REFUTED by p131** — see the system-of-record tier
  above: at least six systems, read by an earlier pass and dropped by p130's rewrite. 🟢 **The
  surviving gap is that the tier is almost entirely copyleft, with `academico` (MIT) the lone
  permissive base — and that no AI *agent* targets any of them** (`agents/top.md`).
- **Canvas is the quietest major platform** (last push 2026-04-30, ~5 months) 🔴 **and it is now
  ~5.5 months quiet, unchanged on re-check this pass.** Worth raising explicitly before
  recommending it as an actively developed base — it is still the richest API surface in the
  sector, which is why every connector targets it.
- ~~**Three Kolibri-family repos, zero AI on any of them.** A valid re-probe this pass
  (`kolibri stars:>2` → 86 repos) resolves the family to three Learning Equality repos; the other
  83 are name collisions. **The offline slot is still the cleanest unclaimed opportunity in this
  KB** (`intel/trends.md` → T8).~~ 🔴 **REFUTED BY p132.** The family resolution was right —
  [`learningequality/kolibri`](https://github.com/learningequality/kolibri) (MIT, 1 141★),
  [`learningequality/studio`](https://github.com/learningequality/studio) (MIT, 192★),
  [`learningequality/kolibri-design-system`](https://github.com/learningequality/kolibri-design-system)
  (52★) — **and the conclusion drawn from it was wrong.**
  [`Crosstalk-Solutions/project-nomad`](https://github.com/Crosstalk-Solutions/project-nomad)
  (**Apache-2.0, 39 444★**) runs Kolibri as its education container beside Kiwix and Ollama, and
  does not contain the string `kolibri` in its description. 🟢 **The surviving gaps are narrower and
  real: (a) no AI project builds *inside* Kolibri itself** — NOMAD orchestrates it from outside and
  the Learning Equality repos carry no AI; **(b) nothing offline targets LATAM.** The one
  curriculum-specific offline row found is Indian (`Tushar-cy/Offline-AI`), and LATAM — where this
  KB argues offline is a first-class requirement rather than an edge case — has none.
  🟡 **Also note a new collision source: Aleph Alpha ships a 78B model called "Kolibri".**

### 🟡 p135's verdict on this page's flagship gap

- **"No permissively licensed, full-featured LMS at the scale of Moodle or Canvas."**
  🟡 **NARROWED, and honestly it is weaker than it was.**
  [`OpenOLAT/OpenOLAT`](https://github.com/OpenOLAT/OpenOLAT) is **447★**, pushed 2026-10-09, under
  **Apache-2.0** (with two attribution statements replacing the appendix — permissive in effect),
  and it ships QTI, SCORM, curriculum management, assessment and lecture management in one Java
  codebase. It is a real, maintained, permissive, full-featured LMS, and **this KB had never listed
  it.** 🔴 **The gap survives only in its "at the scale of Moodle or Canvas" clause** — OpenOlat is
  447★ against Moodle's order of magnitude more, and its deployment base is concentrated in
  German-speaking Europe. 🔵 **For an EMEA engagement that clause may not matter**, and this is now
  the first permissive answer this page can give to *"we want off Moodle's GPL."*
- 🆕 **The offline gap gains a permissive component it did not have.**
  [`jcputney/scorm-again`](https://github.com/jcputney/scorm-again) (MIT, 354★) lists `offline-first`
  among its own topics and implements the SCORM runtime client-side. 🟢 **That is the missing piece
  between `T8`'s offline requirement and standards-tracked course delivery** — a learner can
  complete tracked content with no connectivity and reconcile later. It still does not close *"no
  AI project builds inside Kolibri itself"*, and it still is not LATAM-originated.

### 🆕 Gaps this page opens after p135

- ~~**The sector's most-used SCORM library is unlicensed, and the blast radius is unmeasured.**~~
  🟢 **CLOSED AND CORRECTED by p136 (`ACTION BR`).** A grant is declared (manifest + source header);
  the blast radius on this KB's own pages is **one row**, `numbas/Numbas`, by **vendoring** rather
  than by manifest; and the sector-level reach is **293 files** carrying the header. 🔴 **What
  replaces it is narrower**: the declared body is unreadable in this channel and *"MIT-style"* is
  not an SPDX identifier, so the row's terms are *declared and unread* — and `pipwerks`' HEAD commit
  is **2018-09-06**, which makes it a stale dependency regardless of its licence.
- 🔴 **No permissive Python library exists for Open Badges.** Both Python rows are copyleft
  (LGPL-2.1 and LGPL-3.0). The permissive credential work is in **Rust** (`impierce`, Apache-2.0)
  and **Java** (`1EdTech`, Apache-2.0), which is a language mismatch for most AI engagements.

### 🆕 Gaps this page opens after p136

- 🔴 **This page's dependency picture is manifest-shaped, and the sector's is not.** `ACTION BR`
  measured 150 of 324 rows exposing at least one of seven manifest types; the one dependency that
  mattered was **vendored**, invisible to all seven. Until a tree-level probe runs (the instruments
  exist — `compose/code/p275-tree-enumeration`, `p441-tree-licence-enumeration`), **every "no
  dependants" statement on this page is a statement about manifests**.
- 🔴 **A root licence says nothing about a vendored subtree, and this page tables root licences.**
  `numbas/Numbas` is Apache-2.0 at the root and carries an MIT-style third-party header four levels
  down. Of the 24 rows in this page's platform and standards tables, **the number whose vendored
  subtrees have been read is zero.** 🔵 **This is `p969-root-only-licence-reach` one level deeper.**
  p93 measured that the grant ladder cannot see a **per-directory** licence (`bncc-dados`: code at
  the root, data one directory down). p136 measures that it cannot see a **third-party header inside
  a vendored file** either — same blind spot, and the vendored case is the common one in a sector
  whose code moves by copying.
- 🟡 **Three `UNRESOLVED` lineage clusters remain** (`education-ai-suite`, `OpenPronounce`,
  `agents-radar`). Each needs one clone per side; none is an education-supply row, which is why they
  were left — recorded so the 25-cluster figure is not read as 25 resolved.
