---
industry: education
region: Global
updated: 2026-10-12
---

# `p139-tool-count-drift` — `ACTION CK`: two thirds of the shelf disagrees with itself, and the gap is where the writes are

**Executes p138's pre-registered `ACTION CK`** (narrowed from `ACTION CI`), written as:

> Measure **tool-count drift** across the **nine npm rows whose payload is already
> downloaded**, counting registered tools in the shipped build and comparing to each
> package's own README. 🔴 *Refuted if fewer than a third disagree with themselves.*

## Verdict: **DISCHARGED, NOT REFUTED — 6 of 9 (66%) against a 33% threshold**

| package | build tools | documented | 🔴 undocumented | write tools | 🔴 **undocumented writes** | disagrees |
|---|---|---|---|---|---|---|
| 🔴 `@imazhar101/mcp-canvas-server` | **227** | 96 | 🔴 **131** | 105 | 🔴 **61** | **YES** |
| 🔴 `eth-moodle-mcp` | 18 | 3 | 🔴 **15** | 1 | 🔴 **1** | **YES** |
| 🔴 `moodle-mcp-server-aql` | 14 | 🔴 **0** | 🔴 **14** | 0 | 0 | **YES** |
| 🟡 `canvas-mcp-server` | 54 | 53 | 1 | 11 | 0 | **YES** |
| 🟡 `@owen-x-tech/canvas-mcp` | 62 | 61 | 1 | 24 | 0 | **YES** |
| 🔴 `@exhabition/brightspace-mcp` | **0** | 0 | 0 | 0 | 0 | **YES** *(see `P139-B4`)* |
| 🟢 `@n35da/brightspace-mcp` | 17 | 17 | 0 | 2 | 0 | no |
| 🟢 `@ink-waffle/moodle-mcp` | 16 | 16 | 0 | 0 | 0 | no |
| 🟢 `mcp-canvas-lms` | 3 | 3 | 0 | 0 | 0 | no |
| **total** | **411** | 249 | 🔴 **162** | 143 | 🔴 **62 (38% of undocumented)** | **6 of 9** |

🔵 **The count is not the finding. The axis is.** Of **162** undocumented tools,
🔴 **62 — 38% — mutate the LMS.** An undocumented read tool is a missing paragraph. An
undocumented `bulk_update_grades` is an ungoverned capability, and "grading or ranking
learners" is exactly what **Vietnam's Decision 33/2026/QĐ-TTg** and **EU AI Act Annex III**
name high-risk. A client reading the README cannot know the duty applies.

## `P139-B1` — `@imazhar101/mcp-canvas-server`: 61 undocumented write tools, including the identity surface

**227 registered tools; the README names 96.** The 131 it does not name include **61 writes**,
and they are not peripheral:

| class | undocumented write tools |
|---|---|
| 🔴 **grades** | `grade_submission`, `grade_submission_by_anonymous_id`, `bulk_update_grades`, `bulk_update_grades_for_course`, `bulk_update_assignment_dates` |
| 🔴 **identity and authentication** | `update_sso_settings`, `restore_authentication_provider`, `update_user_login`, `update_user`, `create_user` |
| destructive | `delete_assignment`, `delete_quiz`, `delete_module`, `delete_external_tool`, `delete_custom_data`, `delete_group_page`, … |
| content | `create_quiz`, `create_module`, `create_external_tool`, `update_course_front_page`, … |

🔴 **`update_sso_settings` and `restore_authentication_provider` change how a Canvas tenant
authenticates, and neither appears in the package's documentation.** This is the row p138
also flagged as carrying **no licence signal at all** and **no `repository` field** — so there
is no repository to read either. 🔵 **A client wiring this into an agent acquires 61 write
capabilities it was never told about, five of them over grades and five over identity.**

## `P139-B2` — `eth-moodle-mcp`: "Works with Any Moodle", and 10 tools hardwired to one course

The README's own heading is **`## Works with Any Moodle`**, and its `## Available Tools`
table lists exactly **three**: `list_courses`, `get_course_materials`, `download_materials`.
The build registers **18**. The 15 it omits include:

- 🔴 **10 `ddca_*` tools** — `ddca_browse`, `ddca_get_lectures`, `ddca_get_exams`,
  `ddca_get_homeworks`, `ddca_get_labs`, `ddca_get_readings`, `ddca_get_navigation`,
  `ddca_get_announcements`, `ddca_list_files`, `ddca_download` — whose own descriptions say
  they scrape **"the DDCA course website"** (ETH Zürich's *Digital Design and Computer
  Architecture*). The package is substantially a single-course scraper presented as a generic
  Moodle client.
- 🔴 **`submit_assignment`** — a write tool, documented nowhere. 🔵 **The same shape p138 found
  in `Jawadh-Salih/moodle-mcp-server` (`submit_journal`, `update_assignment`), in a different
  repository, found by an instrument rather than by hand.** That is what generalises the class.
- `generate_flashcards`, `get_deadlines`, `get_quiz_info`, `get_announcements`.

## `P139-B3` — `moodle-mcp-server-aql`: documents none of its 14 tools, and asserts a licence it does not ship

🔴 **0 of 14.** Its 108-line README has sections for *Use With An MCP Client*, *Install
Globally*, *Install From Source*, *Configure*, *Run From Source*, *Plugin SDK* and *License* —
and **no tool list anywhere**, not even in prose: a search for its own tool names
(`list_courses`, `get_course`, `manage_cache`, …) across the README returns **zero hits**.

Two further defects in the same payload:

- 🔴 **The README's only documentation links escape the package.** It points at
  `../../docs/plugins/CREATING-PLUGINS.md` and `../../docs/plugins/CONTRACT.md`; the payload
  contains **0 paths under `docs/`**. Both links are dead for everyone who installs from npm.
- 🔴 **`## License` → `AGPL-3.0.`** — stated in prose, in a payload that p138 showed ships
  **no licence file across 141 paths**. 🔵 **This strengthens `P138-B`: the package asserts the
  strongest obligation on the shelf in its README and ships neither the text nor the tool list.**

## `P139-B4` — `@exhabition/brightspace-mcp` is not a server. It is an 82-line downloader.

The row p138 recorded as *"MIT, 3 paths, no licence file"* has an explanation, and it is bigger
than the licence:

```js
const url = `https://github.com/Exhabition/brightspace-mcp-rs/releases/download/v${version}/${asset}`;
// … get(url) → up to 5 redirects → pipeline(response, createWriteStream(destination))
// … spawn(tar, ['-xzf', archive, '-C', root]) → chmodSync(binary, 0o700) → spawn(binary, …)
```

🔴 **The npm package contains no MCP server at all.** On first run it downloads a
platform-specific Rust binary from GitHub Releases, extracts it, makes it executable and
executes it. Its README documents **31 tool names** that exist only in that binary — which is
why it reports 0 build tools and 31 "phantom" names. 🔵 **The 0 is correct and the README is
not lying; the tools are simply not in the artefact npm serves.**

🔴 **No integrity check.** A search of the loader for `sha`, `hash`, `checksum`, `integrity`,
`createHash` or `digest` returns **nothing**. The version is pinned to the package version; the
*bytes* are not pinned to anything. A redirect chain of up to five hops ends in
`chmod 0o700` and `spawn`. 🔵 **For a client, this is a supply-chain fact that no licence audit
and no tool count would ever surface** — and it is a new repository address for this KB:
🆕 [`Exhabition/brightspace-mcp-rs`](https://github.com/Exhabition/brightspace-mcp-rs).

## What counts as a registered tool — and the two rows that forced the rule

**An MCP tool is a name with an input schema.** Three idioms on this shelf, one rule each:

| idiom | shape | rows |
|---|---|---|
| `direct` | `server.registerTool("moodle_courses", {…})` | `@ink-waffle`, `@n35da`, `eth-moodle-mcp` |
| `adjacent` | `{ name: "get_courses", description: …, inputSchema: {…} }` | `@imazhar101`, `canvas-mcp-server`, `@owen-x-tech`, `mcp-canvas-lms` |
| `module` | a file exporting both `name = "list_courses"` and `inputSchema` | `moodle-mcp-server-aql` |

🔴 **The first draft used "a `name:` key in a file mentioning `ListToolsRequestSchema`" and got
two rows wrong in opposite directions:**

1. 🔴 **`moodle-mcp-server-aql`: 0 tools over 34 source files.** It uses a module-per-tool
   layout and its tool modules never mention the schema symbol — the handler that does is in
   `dist/server/factory.js`. A 141-path package reporting zero tools is not a finding, it is a
   broken probe, and it was caught by disbelieving the number.
2. 🔴 **`@imazhar101/mcp-canvas-server`: 3 tools instead of 227.** Its tools are defined in
   per-domain classes returning `getToolDefinitions()`, again in files with no schema symbol —
   and **two of the three it did find were `beta` and `prod`**, which are
   `{ name: 'beta', suffix: '_BETA' }` environment entries. 🔵 **The under-count and the
   false-positives had the same cause: a file-level gate standing in for an object-level fact.**

The `inputSchema` adjacency window (900 characters) is what excludes those environment entries,
and the server-name exclusion is **load-bearing, not defensive**: `mcp-canvas-lms` ships
`name: "canvas-mcp-server"` inside the window of its own tool array's `inputSchema`, so
adjacency alone returns the server's identity as a tool. `test_count_tools.py` asserts exactly
that, at both layers.

## Files

| file | role |
|---|---|
| `count_tools.py` | the three rules, `is_write_tool`, README extraction. No I/O beyond reading text |
| `test_count_tools.py` | **12 tests**, every fixture verbatim from these nine payloads or from the two rows above. `python3 -I test_count_tools.py` |
| `run_drift.py` | the runner; emits the TSV and the write-axis summary |
| `result.2026-10-12-p139.tsv` | the table above, plus all 62 undocumented write tool names |

### Reproduce

```sh
curl -sS https://registry.npmjs.org/eth-moodle-mcp | python3 -I -c \
  'import json,sys; print(json.load(sys.stdin)["versions"]["1.3.3"]["dist"]["tarball"])'
# download, verify shasum (p138-npm-payload-licence does this), unpack, then:
python3 -I run_drift.py /path/to/unpacked/package
```

## 🔴 What this probe does NOT establish

- 🔴 **`phantom` is a weaker signal than `undocumented` and should not be quoted as a count.**
  It catches parameter names: `eth-moodle-mcp`'s single "phantom" is `since_days_ago`, an
  argument, not a tool. `undocumented` is derived from the build and is sound; `phantom` is
  derived from backticks in prose and is a lead.
- 🔴 **A tool a README names in a table but not in backticks counts as undocumented.** Spot
  checks found none on this shelf — `eth-moodle-mcp`'s table does backtick its three — but the
  extractor would miss it, which biases `undocumented` **upward**.
- 🔴 **Nine npm rows, one registry.** The three Moodle connectors p138 read in source are not
  here, and `moodler-mcp` has no payload layer at all.
- 🔴 **No tool was CALLED.** Registration is not behaviour: a registered tool may be a stub.
  `@imazhar101`'s 61 undocumented writes are 61 registered writes, which is what a client's
  agent would see in `tools/list` — not 61 verified mutations.
- 🔴 **`is_write_tool` reads verbs, not effects.** `get_cache_status` is classified read and
  `mark_module_item_read` write, on their names alone. The 62 is a name-level estimate.
- 🔴 **No region measured.** `eth-moodle-mcp` is ETH Zürich (**EMEA**) by its tool descriptions
  and `@imazhar101` has no repository field at all, so neither is booked as region evidence.
