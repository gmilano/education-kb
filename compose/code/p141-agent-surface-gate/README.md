---
industry: education
region: Global
updated: 2026-10-12
---

# `p141-agent-surface-gate` — `ACTION CZ`: 🔴 REFUTED. None of the five is gated — and the tier's real problem is the opposite one

## The action, as p140 wrote it

> Apply `p140-live-surface-bound` to the **five other tutoring-agent rows p139 added**
> (`zijinz456/OpenTutor`, `ahmedEid1/lumen`, `mohaneesh-03/mcp-tutor`,
> `nirholas/ai-tutor-mcp`, `hesham0-0nasser/tutor-lms-mcp`) and count flag-gated
> registration. 🔴 *Refuted if none is gated — which would make `T28` a property of
> `tutor-mcp`'s maturity rather than of agent servers, and would narrow the `P18` amendment
> back to a note.*

## Verdict: 🔴 **DISCHARGED and REFUTED. 0 of 5 — and 0 of the 4 that are MCP servers at all.**

🔵 **So `T28` is a property of `tutor-mcp`'s maturity, not of agent servers**, exactly as the
falsifier specified, and `T28` is rewritten on `intel/trends.md` to say so.
[`result.2026-10-12-p141.tsv`](result.2026-10-12-p141.tsv):

| row | language | MCP server? | literal sites | 🔴 dynamic | gated | static bounds live? | verdict |
|---|---|---|---|---|---|---|---|
| 🔴 `zijinz456/OpenTutor` | Python + TSX | 🔴 **NO** | — | — | — | n/a | 🔴 `NOT_AN_MCP_SERVER` |
| 🔴 `ahmedEid1/lumen` | Python | yes | 1 | 🔴 **9** | **0** | 🔴 **NO** | 🔴 `DYNAMIC_UNBOUNDED` |
| 🟢 `mohaneesh-03/mcp-tutor` | Python | yes | **5** | 0 | **0** | 🟢 YES | 🟢 `BOUNDED_STATIC` |
| 🔴 `nirholas/ai-tutor-mcp` | JavaScript | yes | 0 | 🔴 **1** | **0** | 🔴 **NO** | 🔴 `DYNAMIC_UNBOUNDED` |
| 🟢 `hesham0-0nasser/tutor-lms-mcp` | PHP | yes | **1** *(a static 31-entry array)* | 0 | **0** | 🟢 YES | 🟢 `BOUNDED_STATIC` |

## 🔴 The unasked-for finding is larger: p140's `BOUNDED_STATIC` result is TIER-SCOPED

p140 proved that on the npm connector shelf a static count forces the live `tools/list`, for
**7 of 8** rows — one dynamic registration in eight (12%). One tier up, the ratio inverts:

| tier | rows | 🔴 dynamic registration | share |
|---|---|---|---|
| npm connectors (p140) | 8 | 1 (`@owen-x-tech/canvas-mcp`) | 12% |
| 🔴 **agent servers (this probe)** | 4 | 🔴 **2** (`lumen`, `ai-tutor-mcp`) | 🔴 **50%** |

🔴 **`ahmedEid1/lumen` serves 10 tools and a name-literal count returns 1.** It walks
`TOOL_SPECS` — 10 `ToolSpec(` entries in `app/mcp/tools.py` — calling `_register_tool(mcp,
spec)`, where the decorator reads `@mcp.tool(name=name, description=description)` from
variables. 🔴 **`nirholas/ai-tutor-mcp` serves 2 and a literal count returns 0**: `for (const
tool of TOOLS) server.registerTool(tool.name, …)` — the *identical* idiom that made
`@owen-x-tech/canvas-mcp` a 61-tool blind spot in p140.

🔵 **So the 61-tool blind spot was never a one-off.** It is the ordinary way a table-driven
server registers, and it is the majority shape on this tier. p140's claim stands where it was
measured and must not be carried past it — the same rescoping-by-tier that `ACTION CV` applied
to `T18` two passes ago, now for the second time. That is `T30`.

## 🟢 The best thing on this shelf is in its smallest repository

`nirholas/ai-tutor-mcp` has **2 commits** and **Apache-2.0**. It also ships the exact remedy
p139 recorded as missing from `canvas-lms-mcp`, whose `dist/http.js` calls `main()` at module
top level with no entry-point guard and so `process.exit(1)`s the importing process:

```js
// Connect stdio ONLY when this file is the process entry point. Importing the
// module (tests, embedding) must not grab the transport. realpath both sides:
// npm bin shims are symlinks, so argv[1] may differ from import.meta.url.
function isProcessEntryPoint() {
  if (!process.argv[1]) return false;
  try { return import.meta.url === pathToFileURL(realpathSync(process.argv[1])).href; }
  catch { return false; }
}
```

🟢 **It also declares its own ungatedness** — *"Registration is env-free, so this is safe to
import from tests"* — and `buildServer()` returns a fully-registered server with no transport,
which is precisely the seam p139 found unreachable in the larger package. 🔵 **Two commits, and
it solved the problem the 19-version package has not.** Commit count is not maturity.

## 🔴 Two rows were misclassified on arrival, and both corrections matter

🔴 **`zijinz456/OpenTutor` is not an MCP server.** 425 Python + 184 TSX files, and the token
`mcp` occurs **once** in the entire tree — no SDK import, no `tools/list`. Its only `Server(`
is `ThreadingHTTPServer` in `scripts/mock_openai_server.py`, a test double. 🟢 It is a real,
MIT, active tutoring *application* (191 commits, HEAD 2026-10-08, 🟢 **APAC** — `+1100`); it
simply has no tool surface to bound, and p139 shelved it beside connectors it does not
resemble.

🔴 **`hesham0-0nasser/tutor-lms-mcp` is a WordPress plugin**, not a standalone server. Six PHP
files, `MCP_PLUGIN_DIR`, and a hand-rolled JSON-RPC router serving `tools/list` and
`tools/call` over a `register_rest_route`, with OAuth. Its surface is static and now measured:
🔴 **31 tools, of which 17 of 33 distinct names are `tutor_create_*` / `tutor_update_*` /
`tutor_delete_*`** — course create, update and delete among them. 🔴 **And it still ships no
licence file at `HEAD`** (7 commits, HEAD 2026-05-26, 🟢 EMEA — `+0300`). 🔵 **A WordPress
plugin with no licence is a sharper defect than it looks**: the platform's own distribution
terms assume GPL-compatibility, so there is no "permissive by omission" reading available.
Unusable, and the reason is now specific.

## 🔴 Two corrections this probe made to itself, and one lane whose verdict is WITHHELD

**1. Proximity is not enclosure.** The first draft tested for a gate with a **25-line lookback
window** and reported `mcp-tutor` as `GATED`. It is not: the window had caught `if
CONFIG.auto_open_browser:` inside the body of an *earlier* tool function, 64 lines above. Gating
is now decided by block structure — indentation for Python, brace depth for JS and PHP — and a
site at top level cannot be gated by anything. All five of `mcp-tutor`'s `@mcp.tool()`
decorators are at indentation zero.

**2. A protocol name in a comment is not an SDK.** `tutor-lms-mcp` matched the server test on
`io.modelcontextprotocol/ui` inside a comment. The test now requires an import or a
construction — or the hand-rolled `"tools/list"` method, which is what this row actually has.

**3. 🔴 The Go lane FAILS ITS CONTROL, so no Go verdict is published.** Run against
`tutor-mcp` — which p140 established *is* gated — this probe returns `BOUNDED_STATIC`,
0 gated sites. Two causes, both real:

* `tutor-mcp` registers through a **project-local helper**, `addTool(server, &mcp.Tool{Name:
  "get_next_activity"})`, not a recognisable SDK call.
* 🔵 **Its gate is two indirections above the name.** `tools/tools.go` calls
  `registerGetNextActivity(server, deps)` and friends, and the `deps.Institution` conditional
  sits at *that* call site — not around the `addTool` that carries the literal.

🔴 **No lexical-enclosure test at the registration site can see call-site gating**, so this is
a structural limit of both this probe and p140's, not a bug to patch. It is pinned as a test
(`TestKnownLimit`) rather than left as a comment. 🔵 **The only reason the `0 of 5` verdict
survives it** is that all four servers register at module top level with no intermediate
`register*` helpers — checked by hand, row by row, after the control failed. Had any of them
used `tutor-mcp`'s shape, this action would have been reported as unanswerable.

## Reproduce

```sh
python3 -I surface_gate.py "owner/repo=/path/to/clone" ...
python3 -I test_surface_gate.py    # 10 tests, incl. the proximity regression and the Go limit
```
