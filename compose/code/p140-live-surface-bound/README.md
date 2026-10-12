---
industry: education
region: Global
updated: 2026-10-12
---

# `p140-live-surface-bound` — `ACTION CP`: the live tool list CAN differ from the build count, and the mechanism is a deployment flag

**Executes p139's pre-registered `ACTION CP`**, written as:

> Call `tools/list` on **one** running connector from the nine and diff it against this
> pass's static count. 🔴 *Refuted if the live list matches the build count exactly, which
> would make `p139-tool-count-drift`'s numbers behavioural rather than static — and would
> make step 5 of `P18` unnecessary.*

## 🔴 The action as written could not run, and the blocker is NEW

Installing and executing a third-party connector is **refused by this environment's
untrusted-code policy**. That is a *different* blocker from the network-policy
`403 at CONNECT` p139 diagnosed for government hosts — and this pass found that refusal
extends to **university** hosts too (`canvas.ust.hk`, `moodle-app2.let.ethz.ch`,
`safari.ethz.ch` all answer `403` at the proxy gateway). Both belong in the refusal ledger:

| channel | status this pass |
|---|---|
| 🟢 `registry.npmjs.org`, `pypi.org`, `files.pythonhosted.org`, `repo1.maven.org`, `github.com` (smart-HTTP), `raw.githubusercontent.com` | reachable |
| 🔴 `api.github.com` | `403` |
| 🔴 government hosts (p139) **and university hosts (new)** | `403` at `CONNECT` |
| 🔴 **executing an installed npm connector** | 🆕 **refused by sandbox policy, not by network** |

## Verdict: **`ACTION CP` NOT REFUTED — answered without execution, in two parts**

### Part 1 — on the npm shelf, static *is* live, and that is provable

A build whose every tool is registered under a **name literal in the shipped bytes**,
reached without a gate, on a **single server instance**, forces the live list to equal the
static count. Measured across the eight downloadable rows
([`result.2026-10-12-p140.tsv`](result.2026-10-12-p140.tsv)):

| package | literal tools | dynamic sites | server instances | gated | verdict |
|---|---|---|---|---|---|
| `@imazhar101/mcp-canvas-server` 2.1.3 | **227** | 0 | 1 | 0 | 🟢 `BOUNDED_STATIC` |
| `@owen-x-tech/canvas-mcp` 1.1.0 | **62** | 🔴 **1** | 🔴 **2** | 0 | 🔴 `MULTI_SURFACE` |
| `canvas-mcp-server` 2.2.3 | 54 | 0 | 1 | 0 | 🟢 `BOUNDED_STATIC` |
| `eth-moodle-mcp` 1.3.3 | 18 | 0 | 1 | 0 | 🟢 `BOUNDED_STATIC` |
| `@n35da/brightspace-mcp` 0.4.0 | 17 | 0 | 1 | 0 | 🟢 `BOUNDED_STATIC` |
| `@ink-waffle/moodle-mcp` 0.2.0 | 16 | 0 | 1 | 0 | 🟢 `BOUNDED_STATIC` |
| `moodle-mcp-server-aql` 0.1.7 | 14 | 0 | 1 | 0 | 🟢 `BOUNDED_STATIC` |
| `mcp-canvas-lms` 1.0.5 | 3 | 0 | 1 | 0 | 🟢 `BOUNDED_STATIC` |

🟢 **Every `literal tools` figure reproduces `p139-tool-count-drift` exactly** — 227, 62, 54,
18, 17, 16, 14, 3 — from an independently written extractor. That agreement is the strongest
thing in this file: p139's instrument is confirmed by reimplementation, not merely re-run.

🔴 **And it took a correction to get there.** This probe's first draft reported **17** tools
for `@ink-waffle/moodle-mcp` where p139 reported 16, **4** where p139 reported 3, and **64**
where p139 reported 62. p139 was right every time. The cause was the omission of its
`SERVER_CTOR` exclusion: `new McpServer({ name: 'moodle-mcp' })` sits within the adjacency
window of a later `inputSchema` and reads as a tool. 🔵 **The server's own name is not a tool,
and a probe that does not know this inflates every row by one.**

### Part 2 — 🔴 the refuting case exists, and it is a Go repo gated by a deployment flag

[`ArnaudGuiovanna/tutor-mcp`](https://github.com/ArnaudGuiovanna/tutor-mcp) (MIT, read for
`ACTION CT`) registers **56** tool names in non-test sources. 🔴 **Its own test suite asserts
a live `tools/list` of 46**:

```go
// tools/tools_register_test.go:221, in TestRegisterTools_LegacyRolloutAdvertisesOnlyBundle
if len(listed.Tools) != 46 {
    t.Fatalf("listed tools=%d, want 46", len(listed.Tools))
}
```

The mechanism is explicit in `RegisterTools`:

```go
if deps != nil && deps.Institution {
    registerFormationTools(server, deps)        // draft_formation, publish_formation, …
    registerProgressTools(server, deps)         // get_learner_progress
    registerLearnerFormationTools(server, deps) // get_cohort_insights, list_trainer_cohorts, …
    registerBadgeTools(server, deps)
}
```

and the repository states the principle `ACTION CP` was probing, in its own comment:

> `// [1] GoalDecomposer — gated by REGULATION_GOAL=on. When off, neither tool is`
> `// registered, so the surface is invisible to the LLM and the system prompt has no`
> `// instruction to call them.`

🔵 **Three gates — `deps.Institution`, `REGULATION_GOAL`, `deps.OAuthGranularScopes` — mean
there is no such quantity as "this package's tool count".** There is a count per deployment
configuration. 🔴 **So step 5 of `P18` is NOT unnecessary**, and p139's stated fear is
answered: the enumeration is needed, and the reason is not drift. It is that *no payload read
can tell you which flags a client's deployment sets.*

## `P140-A1` — the multi-surface row, and why a name-literal count of it returns 1

`@owen-x-tech/canvas-mcp` 1.1.0 builds **two** MCP servers in one file, selected by `--http`
([`transport.2026-10-12-p140.json`](transport.2026-10-12-p140.json)):

| surface | tools served | name literals on that path | how |
|---|---|---|---|
| stdio (default) | **62** | 62 | `ListTools` returns the `tools` array unchanged |
| HTTP (`--http`) | **62** | 🔴 **1** | 1 by literal + 61 via `for (const tool of tools)` |

🟢 **The two surfaces agree at 62** — but for a reason that belongs to this build rather than
to the shape: the loop re-registers the same static array, skipping the one already added.
🔴 **A probe counting name literals on the HTTP path alone would report 1 where the server
serves 62.** That 61-tool gap is the measurement risk, and it is invisible to every
instrument this KB has used until now.

🔵 **`@ink-waffle/moodle-mcp` is the control that makes the distinction real**: it constructs
**two transports** (`Stdio` + `StreamableHTTP`) on **one** server instance, so both expose the
same 16 tools. *Two transports is not two surfaces; two server instances is.* The test
`test_one_server_on_two_transports_is_not_multi_surface` pins it.

## Method

See the module docstring in [`surface_bound.py`](surface_bound.py). In outline: mask strings
and comments while preserving byte offsets, find registrations by p139's three idioms *with*
its `SERVER_CTOR` exclusion, flag registrations whose name is an expression rather than a
literal, resolve the iterated collection and classify it `STATIC_IN_BUILD` or
`RUNTIME_OR_UNRESOLVED`, count server instances with a namespace-tolerant pattern (a compiled
build writes `new index_js_1.Server({`), and classify lexical gates.

🔴 **One correction is load-bearing.** `@owen-x-tech/canvas-mcp` wraps its entire server in
`if (process.argv.includes('--setup')) { …; process.exit(0); } else { <server> }`. That `else`
is an **installer sibling**, not a capability gate, and an earlier draft scored all 62 of its
tools `CONDITIONAL` on the strength of it. A registration inside an `else` whose sibling
branch terminates the process is reached on every serving run.

## Limits, stated rather than hidden

- Lexical analysis does not prove reachability: a registration not lexically gated can still
  sit in a function nobody calls. 🔵 **`BOUNDED_STATIC` bounds the live list from ABOVE and
  does not prove equality.** The negative verdicts are the strong ones.
- Part 2's live figure is an assertion in the subject's **own test suite**, not a
  measurement this pass took. It is strong evidence — a CI-enforced number — and it is
  still second-hand. 🔴 **No `tools/list` was called by this pass.**
- The ninth row of p139's nine, `@exhabition/brightspace-mcp`, is absent here: it ships no
  server, so there is no registration to bound.

## Reproduce

```sh
# payloads are read as text; nothing here executes package code
for p in @ink-waffle/moodle-mcp@0.2.0 eth-moodle-mcp@1.3.3 \
         @imazhar101/mcp-canvas-server@2.1.3 @n35da/brightspace-mcp@0.4.0 \
         mcp-canvas-lms@1.0.5 canvas-mcp-server@2.2.3 \
         @owen-x-tech/canvas-mcp@1.1.0 moodle-mcp-server-aql@0.1.7; do
  name=${p%@*}; ver=${p##*@}; base=${name##*/}
  curl -sSL -o "${base}-${ver}.tgz" \
    "https://registry.npmjs.org/${name}/-/${base}-${ver}.tgz"
  mkdir -p "payload/${base}-${ver}" && tar -xzf "${base}-${ver}.tgz" -C "payload/${base}-${ver}"
done

python3 -I surface_bound.py payload/*/
python3 -I transport_surfaces.py payload/*owen-x-tech*/package/build/index.js
python3 -I test_surface_bound.py   # 22 tests
```
