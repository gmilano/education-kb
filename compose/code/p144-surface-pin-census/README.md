# `p144-surface-pin-census` — `ACTION DQ`

> Find a second row with a tool-surface lockfile, or state that there is one.
> 🔴 *Refuted if zero further rows carry one.*

## Verdict: 🟢 **DISCHARGED, falsifier SILENT — three bidirectional pins, by three different mechanisms**

🟢 **`P21` is not a recipe derived from a single instance.** Two further rows pin their tool
surface in both directions, and neither does it the way `malkreide/global-education-mcp` does.

| row | artefact | mechanism | pinned |
|---|---|---|---|
| 🟢 `malkreide/global-education-mcp` | `tools.lock.json` | SHA-256 per tool at repo root | **10** |
| 🆕 🟢 `oliverhruby/edupage-mcp` | `tests/e2e/test_manifest.py` | classification manifest over live `list_tools()` | **31** (8 write + 4 auth/local + polled) |
| 🆕 🟢 `divyarthjain/vtop-bhopal-mcp` | `scripts/test-published.ts` | `EXPECTED_TOOLS` golden name array | **17** |

🔵 **Three instances and three formats is the finding.** The practice is real and spreading;
there is **no converged artefact**, so a studio cannot consume "the lockfile" as a standard —
it has to read whichever of the three a repository happens to use.

## 🟢 `edupage-mcp` pins harder than a hash file does

Its docstring states the contract outright: *"Adding a new tool (or deleting one) must update
this manifest — the test fails."* The test asserts

- **no unaccounted tools** — every live tool must be classified, and
- **no stale tools** — the manifest may not name a tool that no longer exists, and
- **disjointness** — a polled tool may not also be a write tool or auth/local tool.

🔵 **A hash lockfile pins identity; this pins identity AND write capability.** For an education
deployment the second is the one that matters, because it is a machine-checked statement of
which tools can change a student's record.

## 🆕 🟢 `vtop-bhopal-mcp` — a committed pin RESOLVES a `DYNAMIC_UNBOUNDED` verdict

🔴 **This shelf scores the row `DYNAMIC_UNBOUNDED` — 0 literal, 4 dynamic.** 🟢 **The
repository commits a 17-name golden array and checks both `missing` and `extra` against live
`tools/list`.** So the surface a static scan called unbounded is pinned to 17 by the
repository's own test.

🔵 **That is a new instrument class for this KB**: where static analysis fails on a dynamic
registration shape, a committed bidirectional pin bounds the surface anyway. The two are
complementary rather than competing, and the pin is the stronger evidence because it is
checked against a running server.

## 🟡 Three weaker artefacts, kept separate on purpose

| row | artefact | why it is not a pin |
|---|---|---|
| 🟡 `krzysztofbury/librus-mcp` | `MCP_CONTRACT.md` + `release_verification/measure_tools.py` | documented counts (27/31/35) enforced by a **UTF-8 KiB catalog budget** — a size gate, not a name set |
| 🟡 `Piyushtanwani/DAU-buddy` | `tests/test_prompt_tool_catalogue.py` | 🔵 **self-declared**: *"Only one direction is asserted"*; a `> 20` floor |
| 🟡 `felipedias-ie/blackboard-mcp` | `test/protocol.test.ts` | `assert tools.length >= 20` — a floor |

## 🔴 Two filename false positives, recorded so the next sweep does not re-find them

- 🔴 `MartinSA04/ntnu-mcp` — `tests/fixtures/catalog_page.json` is an **NTNU course catalogue**
  (`courseCode`, `TFE4130`), not a tool catalogue.
- 🔵 `alejooroncoy/campus-cli` — `site/public/.well-known/ai-catalog.json` is a **genuine
  artefact at a different layer**: an AIR-spec *service discovery* manifest with a `did:web`
  identifier advertising one MCP server. 🆕 **It pins no tool surface, and it is the first
  `.well-known` AI-discovery file on this shelf.**

## Run

See `result.2026-10-12-p144.tsv`. The census is a read over the 44-row connector population
plus the 8 npm packages; the search terms were `tools.lock*`, `*.lock.json`, `*.snap`,
`*catalog*.json`, `published_schema*`, and any test or fixture file matching `tools/list`,
`list_tools()` or `ListToolsRequest`.
