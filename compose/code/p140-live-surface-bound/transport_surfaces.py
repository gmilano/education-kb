"""p140 — for a MULTI_SURFACE payload, what does EACH server instance serve?

`surface_bound.py` reports that a payload constructs more than one MCP server, which
makes "the package's tool count" ill-formed: `tools/list` answers per transport. This
script resolves the surfaces separately for the one such row on this shelf,
`@owen-x-tech/canvas-mcp` 1.1.0, and it is written to be re-pointed at the next one.

Two surfaces exist in that build:

  stdio  `new index_js_1.Server(...)` + `setRequestHandler(ListToolsRequestSchema,
         async () => ({ tools }))` -- so the surface IS the `tools` array, verbatim.
  http   `createHttpServer()` -> `new mcp_js_1.McpServer(...)`, which registers
         `course_dashboard` by literal and then every other member of the SAME `tools`
         array through `for (const tool of tools) httpMcp.registerTool(tool.name, …)`,
         skipping the one already registered.

🔵 **The two surfaces therefore agree at 62, and they agree for a reason that is a
property of this build rather than of the shape.** A name-literal count of the HTTP path
alone returns 1. That gap -- 1 counted, 62 served -- is the measurement risk this probe
exists to name.

Nothing here executes package code. The payload is read as text.
"""

import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import surface_bound as sb  # noqa: E402

NAMED_IN_ARRAY = re.compile(r"\bname\s*:\s*[\"']([a-z][a-z0-9_.-]{2,63})[\"']")
LITERAL_ON = re.compile(
    r"\b(?P<recv>[A-Za-z_$][\w$]*)\.registerTool\(\s*[\"'](?P<tool>[a-z][a-z0-9_.-]{2,63})[\"']"
)
DYNAMIC_ON = re.compile(
    r"\b(?P<recv>[A-Za-z_$][\w$]*)\.registerTool\(\s*(?![\"'])(?P<expr>[A-Za-z_$][\w$.]*)"
)
SKIP_GUARD = re.compile(
    r"if\s*\(\s*[\w$.]+\s*===?\s*[\"']([a-z][a-z0-9_.-]{2,63})[\"']\s*\)\s*continue"
)


def bracket_span(text, start):
    """Span of the array literal opening at or after `start`."""
    i = text.index("[", start)
    depth = 0
    for j in range(i, len(text)):
        if text[j] == "[":
            depth += 1
        elif text[j] == "]":
            depth -= 1
            if depth == 0:
                return i, j + 1
    return i, len(text)


def array_members(text, array_name):
    """Tool names declared in a literal array, by name."""
    m = re.search(r"\b(?:const|let|var)\s+" + re.escape(array_name) + r"\s*=\s*\[", text)
    if not m:
        return []
    lo, hi = bracket_span(text, m.start())
    return NAMED_IN_ARRAY.findall(text[lo:hi])


def surfaces(path):
    text = Path(path).read_text(encoding="utf-8", errors="replace")
    masked = sb.mask(text)

    # Which receiver object is the stdio server, and which the secondary one?
    receivers = {}
    for m in LITERAL_ON.finditer(text):
        receivers.setdefault(m.group("recv"), {"literal": [], "dynamic": []})
        receivers[m.group("recv")]["literal"].append(m.group("tool"))
    for m in DYNAMIC_ON.finditer(masked):
        recv = m.group("recv")
        receivers.setdefault(recv, {"literal": [], "dynamic": []})
        coll = sb.resolve_collection(masked, m.start())
        receivers[recv]["dynamic"].append(coll or "<unresolved>")

    # The stdio handler returns an array wholesale: `return { tools }`.
    wholesale = re.search(
        r"ListToolsRequestSchema\s*,\s*async[^{]*\{\s*return\s*\{\s*([A-Za-z_$][\w$]*)\s*\}",
        masked,
    )

    out = {}
    if wholesale:
        arr = wholesale.group(1)
        members = array_members(text, arr)
        out["stdio (ListTools returns `%s` wholesale)" % arr] = {
            "served": len(members),
            "name_literals_on_this_path": len(members),
            "how": "array literal returned unchanged",
        }

    for recv, got in sorted(receivers.items()):
        served, how = len(got["literal"]), []
        if got["literal"]:
            how.append("%d by literal" % len(got["literal"]))
        for coll in got["dynamic"]:
            members = array_members(text, coll) if coll else []
            # A `continue` guard skips a tool already registered by literal.
            skipped = set(SKIP_GUARD.findall(text)) & set(got["literal"])
            added = len([n for n in members if n not in skipped])
            served += added
            how.append("%d via `for … of %s`%s" % (
                added, coll, " (minus %d already registered)" % len(skipped) if skipped else ""))
        out["instance `%s`" % recv] = {
            "served": served,
            "name_literals_on_this_path": len(got["literal"]),
            "how": " + ".join(how) or "nothing",
        }
    return out


def main(argv):
    for path in argv:
        print("#", path)
        s = surfaces(path)
        print(json.dumps(s, indent=2))
        served = {v["served"] for v in s.values()}
        print("# surfaces agree" if len(served) == 1 else "# SURFACES DIVERGE: %s" % sorted(served))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
