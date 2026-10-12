"""p141-agent-surface-gate — `ACTION CZ`: is flag-gated tool registration a property of agent servers?

p140 pre-registered:

> Apply `p140-live-surface-bound` to the **five other tutoring-agent rows p139 added**
> (`zijinz456/OpenTutor`, `ahmedEid1/lumen`, `mohaneesh-03/mcp-tutor`,
> `nirholas/ai-tutor-mcp`, `hesham0-0nasser/tutor-lms-mcp`) and count flag-gated
> registration. 🔴 *Refuted if none is gated -- which would make `T28` a property of
> `tutor-mcp`'s maturity rather than of agent servers, and would narrow the `P18` amendment
> back to a note.*

🔴 **REFUTED: none is gated. Zero of five.**

## 🔴 Why p140's probe could not simply be "applied"

`p140-live-surface-bound` masks TypeScript/JavaScript string and comment syntax and reads the
`@modelcontextprotocol/sdk` idioms. Of these five rows, **two are Python**, **one is PHP**,
**one is a JavaScript app with no MCP server in it at all**, and only one is the JS/TS shape
that probe understands. 🔵 **"Apply the probe" was an instruction written against an assumed
homogeneity that does not hold one tier up.** This probe therefore reimplements the question
-- *is the set of registered tools fixed by the build, or can a deployment change it?* -- per
language, and reports the language it used.

## The three shapes that matter

  `LITERAL`   a tool's name is a literal at the registration site, reached unconditionally.
              The live `tools/list` is forced to equal the static count.
  `DYNAMIC`   the name comes from an expression -- `for (const t of TOOLS)
              server.registerTool(t.name, ...)`, or `@mcp.tool(name=name)` inside a walk
              over a spec table. 🔴 A name-literal count returns a number unrelated to what
              is served.
  `GATED`     registration sits behind a conditional on configuration, an environment
              variable or injected dependencies -- `tutor-mcp`'s `if deps.Institution`,
              `REGULATION_GOAL=on`. The surface is a property of the DEPLOYMENT.

`GATED` is what `ACTION CZ` asked to count. `DYNAMIC` is what it found.

## 🔴 A correction this probe made to itself, before publishing

The first draft tested for a gate by scanning a **25-line lookback window** for a conditional
that reads config or environment. That reported `mohaneesh-03/mcp-tutor` as `GATED`, and it is
not. The window had caught `if CONFIG.auto_open_browser:` -- a line inside the body of an
*earlier* tool function, 64 lines above the registration it was blamed for.

🔵 **Proximity is not enclosure.** A conditional gates a registration only when the
registration is lexically INSIDE it. Gating is therefore decided by block structure:
indentation for Python, brace depth for JavaScript. A site at module top level -- indentation
zero, brace depth zero -- cannot be gated by anything, and all five of `mcp-tutor`'s
`@mcp.tool()` decorators are at indentation zero.

🔴 **The PHP row was also misread.** `hesham0-0nasser/tutor-lms-mcp` matched the SDK test on
the string `io.modelcontextprotocol/ui` -- inside a *comment*. It is nonetheless a real MCP
server: it implements the JSON-RPC methods `tools/list` and `tools/call` by hand over a
WordPress REST route, with the tool set returned by a static `TLMS_MCP_Tools::list_tools()`.
That idiom is added explicitly rather than left to report `NO_REGISTRATION_SITE_FOUND`.
"""

import os
import re
import sys

# Conditional keywords per language.
COND = {
    "python": re.compile(r"^(\s*)(if|elif)\b(.*)$"),
    "js": re.compile(r"^\s*(?:\}\s*)?(if|else if)\s*\((.*)$"),
    "php": re.compile(r"^\s*(?:\}\s*)?(if|elseif)\s*\((.*)$"),
    "go": re.compile(r"^(\s*)(if)\b(.*)$"),
}
# Reads that make a conditional a DEPLOYMENT flag rather than a dispatch branch.
FLAG_READ = re.compile(
    r"os\.getenv|os\.environ|process\.env|getenv\(|\$_ENV|\bconfig\.|\bsettings\.|"
    r"\benabled\b|\bfeature_flag\b|deps\.[A-Z]", re.IGNORECASE
)


def indent_of(line):
    return len(line) - len(line.lstrip())


def gated_python(lines, i):
    """True when line `i` is lexically INSIDE an `if`/`elif` whose test reads a flag.

    🔴 Not a proximity window: walk outward to strictly smaller indentation, which is what
    encloses a statement in Python. A site at indentation 0 cannot be gated.
    """
    target = indent_of(lines[i])
    if target == 0:
        return False
    level = target
    for j in range(i - 1, -1, -1):
        line = lines[j]
        if not line.strip():
            continue
        ind = indent_of(line)
        if ind < level:
            m = COND["python"].match(line)
            if m and FLAG_READ.search(m.group(3)):
                return True
            level = ind
            if level == 0:
                return False
    return False


def gated_braced(lines, i, lang):
    """True when line `i` sits inside a flag-reading `if (...) {` block.

    Brace depth from the file start; a site at depth 0, or whose enclosing blocks are all
    functions rather than flag conditionals, is not gated.
    """
    depth = 0
    stack = []
    for j, line in enumerate(lines):
        if j == i:
            return any(stack[:depth])
        m = COND[lang].match(line)
        opens = line.count("{") - line.count("}")
        if m and FLAG_READ.search(m.group(2)) and opens > 0:
            stack.append(True)
            depth += opens
            continue
        if opens > 0:
            stack.extend([False] * opens)
            depth += opens
        elif opens < 0:
            depth = max(0, depth + opens)
            stack = stack[:depth]
    return False


REG_PY = re.compile(r"@(?:\w+)\.tool\s*\(([^)]*)\)")
REG_JS = re.compile(r"\.(?:registerTool|tool)\s*\(\s*([^,\n]*)")
REG_GO = re.compile(r"\bRegisterTool\s*\(|\bAddTool\s*\(")
# A hand-rolled JSON-RPC server with no SDK: the tool set is whatever a static
# `list_tools()` returns. Bounded by the build unless that array is built at runtime.
REG_PHP = re.compile(r"function\s+list_tools\s*\(")

NAME_LITERAL_PY = re.compile(r"""name\s*=\s*['"]""")
NAME_LITERAL_JS = re.compile(r"""^\s*['"]""")


def lang_of(path):
    return {".py": "python", ".js": "js", ".mjs": "js", ".cjs": "js", ".ts": "js",
            ".go": "go", ".php": "php"}.get(os.path.splitext(path)[1])


def walk(root):
    for base, dirs, files in os.walk(root):
        dirs[:] = [d for d in dirs
                   if d not in {".git", "node_modules", "__pycache__", "dist", "build",
                                ".venv", "venv", "vendor"}]
        for f in files:
            p = os.path.join(base, f)
            if lang_of(p):
                yield p


def is_mcp_server(root):
    """Does this tree contain an MCP server at all, or only the word in its name?

    A repository can be named `*-mcp` and contain no MCP surface. Counting its tools would
    be a category error, so the question is asked first and answered in the output.
    """
    hits = 0
    sdk = False
    for p in walk(root):
        try:
            t = open(p, encoding="utf-8", errors="replace").read()
        except OSError:
            continue
        # An import or construction, not a mention: `io.modelcontextprotocol/ui`
        # inside a comment is not an SDK, and the first draft read one as a server.
        if re.search(r"""(from|import|require)\s*\(?\s*['"]?@?modelcontextprotocol"""
                     r"""|\bFastMCP\s*\(|new\s+McpServer\s*\(|from\s+mcp\.server""", t):
            sdk = True
        # Hand-rolled JSON-RPC: the MCP methods themselves, served without an SDK.
        if '"tools/list"' in t or "'tools/list'" in t:
            sdk = True
        hits += len(re.findall(r"\bmcp\b", t, re.IGNORECASE))
    return sdk, hits


def scan(root):
    lit = dyn = gated = 0
    langs = set()
    sites = []
    for p in walk(root):
        lang = lang_of(p)
        if "/test" in p.replace(os.sep, "/") or os.path.basename(p).startswith("test_"):
            continue
        try:
            lines = open(p, encoding="utf-8", errors="replace").read().splitlines()
        except OSError:
            continue
        for i, line in enumerate(lines):
            m = kind = None
            if lang == "python":
                m = REG_PY.search(line)
                if m:
                    arg = m.group(1).strip()
                    kind = "LITERAL" if (arg == "" or NAME_LITERAL_PY.search(arg)) \
                        else "DYNAMIC"
            elif lang == "js":
                m = REG_JS.search(line)
                if m:
                    kind = "LITERAL" if NAME_LITERAL_JS.search(m.group(1)) else "DYNAMIC"
            elif lang == "go":
                m = REG_GO.search(line)
                kind = "LITERAL" if m else None
            elif lang == "php":
                m = REG_PHP.search(line)
                kind = "LITERAL" if m else None
            if not m:
                continue
            langs.add(lang)
            if lang == "python":
                g = gated_python(lines, i)
            elif lang in ("js", "php"):
                g = gated_braced(lines, i, lang)
            else:
                g = False
            if g:
                gated += 1
                kind = "GATED"
            elif kind == "LITERAL":
                lit += 1
            else:
                dyn += 1
            sites.append((os.path.relpath(p, root), i + 1, kind))
    return lit, dyn, gated, sorted(langs), sites


COLS = ["subject", "languages", "is_mcp_server", "literal_sites", "dynamic_sites",
        "gated_sites", "static_bounds_live", "verdict"]


def row(subject, root):
    sdk, mentions = is_mcp_server(root)
    if not sdk:
        return dict(zip(COLS, [subject, ",".join(sorted({lang_of(p) for p in walk(root)} - {None})),
                               "NO", 0, 0, 0, "n/a",
                               "NOT_AN_MCP_SERVER (%d 'mcp' tokens, no SDK import)" % mentions]))
    lit, dyn, gated, langs, _ = scan(root)
    if gated:
        verdict = "GATED"
    elif dyn:
        verdict = "DYNAMIC_UNBOUNDED"
    elif lit:
        verdict = "BOUNDED_STATIC"
    else:
        verdict = "NO_REGISTRATION_SITE_FOUND"
    return dict(zip(COLS, [subject, ",".join(langs), "YES", lit, dyn, gated,
                           "YES" if verdict == "BOUNDED_STATIC" else "NO", verdict]))


def main(argv):
    rows = [row(*spec.split("=", 1)) for spec in argv]
    print("\t".join(COLS))
    for r in rows:
        print("\t".join(str(r[c]) for c in COLS))
    servers = [r for r in rows if r["is_mcp_server"] == "YES"]
    print("\n# %d of %d subjects are MCP servers" % (len(servers), len(rows)), file=sys.stderr)
    print("# GATED: %d of %d servers" % (sum(1 for r in servers if r["gated_sites"]),
                                         len(servers)), file=sys.stderr)
    print("# DYNAMIC (static count does NOT bound live): %d of %d servers"
          % (sum(1 for r in servers if r["verdict"] == "DYNAMIC_UNBOUNDED"), len(servers)),
          file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
