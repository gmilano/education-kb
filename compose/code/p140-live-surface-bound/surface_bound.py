"""p140-live-surface-bound — is a shipped MCP build's STATIC tool count a BOUND on what
a live `tools/list` returns?

## Why this probe exists, and why it is not the probe that was pre-registered

p139 pre-registered `ACTION CP`: run one of the nine connectors and diff `tools/list`
against the static count, on the stated ground that *"registration is not behaviour"*.

That action cannot run here. Installing and executing a third-party connector is refused
by this environment's untrusted-code policy -- a DIFFERENT blocker from the network-policy
`403 at CONNECT` that p139 diagnosed for government hosts. Both are now in the refusal
ledger; neither is a probe to re-register unchanged.

So this probe asks the same question from the other side. The one-directional logic:

  * If a build registers every tool under a **name that is a literal in the shipped
    bytes**, reached without a gate, on a **single server instance**, then the live tool
    list is forced to equal the static count. No execution is needed to know it.
  * If any registration takes its name from an **expression**, the static count stops
    being a bound unless the iterated collection is itself static in the build -- and if
    that collection is fetched at runtime, no static method can bound the live list at all.

🔴 **The second case is the one p139 could not see, and this shelf contains it.**
`@owen-x-tech/canvas-mcp` registers 1 tool by literal on its HTTP server and the other 61
through `for (const tool of tools) httpMcp.registerTool(tool.name, ...)`. A probe counting
name literals finds **1** where the live server serves **62**.

## Method

1. **Mask** the source: every character inside a string literal, template literal, line
   comment or block comment becomes a space, preserving length and newlines, so offsets
   into the masked copy and the original agree exactly. Brace and conditional analysis
   runs on the masked copy; names are read from the original.

2. **Literal registrations** reuse p139's three idioms unchanged -- direct call, adjacent
   object literal carrying an `inputSchema`, module exporting `name` and schema separately
   -- including its `SERVER_CTOR` exclusion, so the denominator is the population p139
   counted. *Omitting that exclusion is what made this probe's first draft report 17 tools
   for `@ink-waffle/moodle-mcp` where p139 reported 16: the server's own name
   (`new McpServer({ name: 'moodle-mcp' })`) sits within the adjacency window of an
   `inputSchema` and reads as a tool. p139's counts reproduce exactly once it is applied.*

3. **Dynamic registrations**: a `registerTool(` or `.tool(` call whose first argument is
   not a string literal. For each, resolve the iterated collection by walking back to an
   enclosing `for (… of X)` / `X.forEach(` / `X.map(` and recording `X`; then classify `X`
   as `STATIC_IN_BUILD` if a literal array by that name is declared in the same payload,
   else `RUNTIME_OR_UNRESOLVED`.

4. **Server instances and transports**: count `new …Server(` constructions (namespace
   tolerant -- a compiled build writes `new index_js_1.Server({`, which a bare
   `new Server\(` regex misses) and the distinct transport classes constructed. Two server
   instances can carry two different tool surfaces under one version.

5. **Lexical gating**, with the correction that matters: a registration inside an `else`
   whose sibling `if` branch terminates the process (`process.exit`) is NOT gated -- that
   is an installer path, not a capability flag. `@owen-x-tech/canvas-mcp` wraps its entire
   server in exactly that shape, and scoring it `CONDITIONAL` would have been wrong.

## Verdicts

  `BOUNDED_STATIC`  every registration is literal, ungated, one server instance.
                    Static count == live `tools/list`, provable without running it.
  `BOUNDED_DYNAMIC` dynamic registration present, but every iterated collection is
                    static in the build, so the live count is still computable.
  `UNBOUNDED`       a collection is not resolvable in the build. Only execution answers it.
  `MULTI_SURFACE`   more than one server instance; the live list is per-transport and
                    "the package's tool count" is not a well-formed quantity.

## Limits, stated rather than hidden

Lexical analysis does not prove reachability: a registration not lexically gated can still
sit in a function nobody calls, so `BOUNDED_*` bounds the live list from ABOVE and does not
prove equality. The strong results here are the negative ones. Call-graph analysis would
close it, and is not attempted.
"""

import json
import re
import sys
from pathlib import Path

JS_SUFFIXES = {".js", ".mjs", ".cjs"}
TS_SUFFIXES = {".ts", ".mts", ".cts"}

_TOOL_NAME = r"[a-z][a-z0-9_.-]{2,63}"

# --- p139's three idioms, carried over unchanged -------------------------------------
DIRECT = re.compile(r"(?:registerTool|\.tool)\(\s*[\"'](" + _TOOL_NAME + r")[\"']")
NAME_LITERAL = re.compile(r"\bname\s*:\s*[\"'](" + _TOOL_NAME + r")[\"']")
MODULE_NAME = re.compile(r"\bname\s*=\s*[\"'](" + _TOOL_NAME + r")[\"']")
SCHEMA_MARKER = re.compile(r"inputSchema|input_schema")
ADJACENCY_WINDOW = 900
SERVER_CTOR = re.compile(
    r"new\s+(?:[A-Za-z_$][\w$]*\.)*(?:Mcp)?Server\s*\(\s*\{[^{}]*?\bname\s*:\s*[\"']([^\"']+)[\"']",
    re.DOTALL,
)

# --- new in p140 --------------------------------------------------------------------
# A registration whose first argument is NOT a string literal.
DYNAMIC_REG = re.compile(r"(?:registerTool|\.tool)\(\s*(?![\"'])([A-Za-z_$][\w$.\[\]]*)")
# The collection an enclosing iteration walks.
FOR_OF = re.compile(r"\bfor\s*\(\s*(?:const|let|var)\s+[\w$]+\s+of\s+([A-Za-z_$][\w$.]*)")
ITER_CALL = re.compile(r"\b([A-Za-z_$][\w$.]*)\s*\.\s*(?:forEach|map|flatMap)\s*\(")
# A literal array declared in the build, e.g. `const tools = [`.
LITERAL_ARRAY = re.compile(r"\b(?:const|let|var)\s+([A-Za-z_$][\w$]*)\s*=\s*\[")

SERVER_INSTANCE = re.compile(r"new\s+(?:[A-Za-z_$][\w$]*\.)*(?:Mcp)?Server\s*\(")
TRANSPORT = re.compile(
    r"new\s+(?:[A-Za-z_$][\w$]*\.)*"
    r"(StdioServerTransport|StreamableHTTPServerTransport|SSEServerTransport)"
)

COND_BEFORE_BRACE = re.compile(
    r"(?:\bif\s*\([^;{}]*\)|\belse\b|\bswitch\s*\([^;{}]*\)|\bfor\s*\([^;{}]*\)"
    r"|\bwhile\s*\([^;{}]*\)|\bcatch\s*\([^)]*\))\s*$"
)
GUARD_INLINE = re.compile(r"(?:&&|\|\|)\s*$")
PROCESS_EXIT = re.compile(r"process\.exit\s*\(")
ITERATION_HEAD = re.compile(r"(?:\bfor\s*\([^;{}]*\bof\b[^;{}]*\)|\bwhile\s*\([^;{}]*\))\s*$")


def mask(text):
    """Blank strings and comments, preserving length and newlines."""
    out = list(text)
    i, n = 0, len(text)
    while i < n:
        c = text[i]
        if c in "\"'`":
            quote, j = c, i + 1
            while j < n:
                if text[j] == "\\":
                    j += 2
                    continue
                if text[j] == quote:
                    break
                j += 1
            for k in range(i, min(j + 1, n)):
                if out[k] != "\n":
                    out[k] = " "
            i = j + 1
            continue
        if c == "/" and i + 1 < n and text[i + 1] == "/":
            j = text.find("\n", i)
            j = n if j == -1 else j
            for k in range(i, j):
                out[k] = " "
            i = j
            continue
        if c == "/" and i + 1 < n and text[i + 1] == "*":
            j = text.find("*/", i + 2)
            j = n if j == -1 else j + 2
            for k in range(i, min(j, n)):
                if out[k] != "\n":
                    out[k] = " "
            i = j
            continue
        i += 1
    return "".join(out)


def brace_stack_at(masked, offset):
    """Offsets of the `{` still open at `offset`, outermost first."""
    stack = []
    for i, c in enumerate(masked[:offset]):
        if c == "{":
            stack.append(i)
        elif c == "}" and stack:
            stack.pop()
    return stack


def block_end(masked, open_brace):
    depth = 0
    for i in range(open_brace, len(masked)):
        if masked[i] == "{":
            depth += 1
        elif masked[i] == "}":
            depth -= 1
            if depth == 0:
                return i
    return len(masked)


def _sibling_if_exits(masked, else_brace):
    """True when the `if` branch preceding this `else` terminates the process.

    `if (--setup) { …; process.exit(0); } else { <the whole server> }` is an installer
    path, not a capability gate, and must not score as conditional.
    """
    head = masked[:else_brace]
    close = head.rstrip().rfind("}")
    if close == -1:
        return False
    depth = 0
    for i in range(close, -1, -1):
        if masked[i] == "}":
            depth += 1
        elif masked[i] == "{":
            depth -= 1
            if depth == 0:
                return bool(PROCESS_EXIT.search(masked[i:close]))
    return False


def classify_gate(masked, offset):
    """('gated'|'ungated', reason) for one registration site."""
    before = masked[max(0, offset - 200): offset].rstrip()
    if GUARD_INLINE.search(before):
        return "gated", "inline && / || guard"
    for brace in brace_stack_at(masked, offset):
        head = masked[max(0, brace - 240): brace].rstrip()
        m = COND_BEFORE_BRACE.search(head)
        if not m:
            continue
        kind = m.group(0).strip()
        if kind.startswith("else") and _sibling_if_exits(masked, brace):
            continue  # installer sibling: the other branch exits
        if ITERATION_HEAD.search(head):
            continue  # an iteration is counted as dynamic, not as a gate
        return "gated", "enclosing " + kind[:48]
    return "ungated", ""


def iter_source(pkg_dir):
    """(path, text) for each shipped source file, preferring the built JS."""
    files = [p for p in Path(pkg_dir).rglob("*") if p.is_file()]
    js = [p for p in files if p.suffix.lower() in JS_SUFFIXES]
    chosen = js if js else [p for p in files if p.suffix.lower() in TS_SUFFIXES]
    for p in sorted(chosen):
        try:
            yield p, p.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue


def literal_tools(texts, package_name=None):
    """p139's build-tool set, with its server-name exclusion applied."""
    excluded = set()
    for t in texts:
        excluded.update(SERVER_CTOR.findall(t))
    if package_name:
        excluded.add(package_name)
        excluded.add(package_name.split("/")[-1])
    found = set()
    for text in texts:
        found.update(DIRECT.findall(text))
        for m in NAME_LITERAL.finditer(text):
            if SCHEMA_MARKER.search(text[m.end(): m.end() + ADJACENCY_WINDOW]):
                found.add(m.group(1))
        if SCHEMA_MARKER.search(text):
            found.update(MODULE_NAME.findall(text))
    return found - excluded, excluded


def resolve_collection(masked, offset):
    """The collection an enclosing iteration walks, or None."""
    for brace in reversed(brace_stack_at(masked, offset)):
        head = masked[max(0, brace - 240): brace].rstrip()
        m = FOR_OF.search(head)
        if m:
            return m.group(1)
    window = masked[max(0, offset - 600): offset]
    m = None
    for m in ITER_CALL.finditer(window):
        pass
    return m.group(1) if m else None


def measure(pkg_dir, package_name=None):
    by_path = dict(iter_source(pkg_dir))
    texts = list(by_path.values())
    lit, excluded = literal_tools(texts, package_name)

    arrays = set()
    for t in texts:
        arrays.update(LITERAL_ARRAY.findall(t))

    dynamic, collections, gated, gate_reasons = 0, {}, 0, {}
    servers = transports = 0
    transport_kinds = set()

    for path, text in by_path.items():
        masked = mask(text)
        servers += len(SERVER_INSTANCE.findall(masked))
        for m in TRANSPORT.finditer(masked):
            transport_kinds.add(m.group(1))
            transports += 1
        for m in DYNAMIC_REG.finditer(masked):
            dynamic += 1
            coll = resolve_collection(masked, m.start())
            key = coll or "<unresolved>"
            collections[key] = collections.get(key, 0) + 1
        for name in DIRECT.finditer(text):
            verdict, reason = classify_gate(masked, name.start())
            if verdict == "gated":
                gated += 1
                gate_reasons[reason] = gate_reasons.get(reason, 0) + 1

    resolved = {
        c: ("STATIC_IN_BUILD" if c.split(".")[0] in arrays else "RUNTIME_OR_UNRESOLVED")
        for c in collections if c != "<unresolved>"
    }
    unbounded = (
        "<unresolved>" in collections
        or any(v == "RUNTIME_OR_UNRESOLVED" for v in resolved.values())
    )

    if servers > 1:
        verdict = "MULTI_SURFACE"
    elif dynamic and unbounded:
        verdict = "UNBOUNDED"
    elif dynamic:
        verdict = "BOUNDED_DYNAMIC"
    elif gated:
        verdict = "GATED"
    else:
        verdict = "BOUNDED_STATIC"

    return {
        "literal_tools": len(lit),
        "dynamic_sites": dynamic,
        "collections": collections,
        "collection_class": resolved,
        "server_instances": servers,
        "transports": ",".join(sorted(transport_kinds)) or "-",
        "gated_sites": gated,
        "gate_reasons": gate_reasons,
        "excluded_server_names": sorted(excluded),
        "source_files": len(by_path),
        "verdict": verdict,
        "tool_names": sorted(lit),
    }


COLS = ["package", "literal_tools", "dynamic_sites", "server_instances",
        "transports", "gated_sites", "verdict"]


def main(argv):
    rows = []
    for d in argv:
        name = Path(d).name
        r = measure(d, package_name=name)
        r["package"] = name
        rows.append(r)
    print("\t".join(COLS))
    for r in rows:
        print("\t".join(str(r[c]) for c in COLS))
    print("\n# detail", file=sys.stderr)
    for r in rows:
        print(r["package"], json.dumps({
            "collections": r["collections"],
            "collection_class": r["collection_class"],
            "gate_reasons": r["gate_reasons"],
            "excluded_server_names": r["excluded_server_names"],
        }), file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
