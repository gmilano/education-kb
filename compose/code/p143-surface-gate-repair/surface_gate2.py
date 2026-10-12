"""p143-surface-gate-repair -- `ACTION DM`.

Repairs `p141-agent-surface-gate` for the two registration shapes it cannot see, then
re-runs all three tiers so `T30`'s three figures can be checked against an instrument
that is not blind to a third of its subjects.

## The defect, located rather than guessed

p141 scans **line by line**:

    for i, line in enumerate(lines):
        m = REG_PY.search(line)          # REG_PY = r"@(?:\\w+)\\.tool\\s*\\(([^)]*)\\)"

🔴 **Both failures follow from that one line of code.**

  1. **Multi-line decorator.** `@mcp.tool(` on its own line has no `)` on that line, so
     `([^)]*)\\)` cannot match and the site is never seen. `malkreide/global-education-mcp`
     declares **10 of 10** tools this way -- every decorator spans 10 lines -- and p141
     returns `NO_REGISTRATION_SITE_FOUND` on a repository that ships a lockfile
     SHA-256-pinning all ten.

  2. **REFLECTION / indirection decorator.** `oliverhruby/edupage-mcp` defines

         def _tool(fn):
             hints = TOOL_ANNOTATIONS.get(fn.__name__)
             if server is not None:
                 annotations = ToolAnnotations(**hints) if (hints and ToolAnnotations) else None
                 return server.tool(annotations=annotations)(fn)
             return fn

     and decorates 31 functions with a bare `@_tool`. There is no `.tool(` token at any
     decoration site, so p141 sees nothing. 🔵 **The name is `fn.__name__`, fixed at import
     by the source text** -- so this is the MOST static shape on the shelf, and the
     instrument scored it as the least.

## What this instrument does differently

Python is parsed with `ast`, not read as lines. 🔴 **A regex over a nested multi-line
decorator is the defect, so replacing it with a better regex would reproduce the defect.**

Classification is kept IDENTICAL to p141's categories so the tiers stay comparable:

  LITERAL  -- the tool's name is fixed by the source at import. Three sub-shapes, all
              counted the same because they are the same fact: `name="x"` in the
              decorator call; no `name=` at all (FastMCP derives it from `fn.__name__`);
              and an indirection decorator that forwards to `X.tool(...)(fn)`.
  DYNAMIC  -- a registration whose NAME is an expression, or a registration CALL made
              inside a loop or comprehension. The static count does not bound the live set.
  GATED    -- a registration lexically enclosed by an `if` whose test reads a deployment
              flag. `T28`'s property; reported separately because it is not dynamism.

🔵 **JS, Go and PHP handling is carried over from p141 UNCHANGED, deliberately.** Both
repaired shapes are Python, so leaving the other languages byte-identical means any
movement in the npm tier (which is JS/TS) is attributable to the subject set and not to
this rewrite. 🔴 **That is the control, and without it a moved figure could not be read.**

Run: python3 -I surface_gate2.py subject=path [subject=path ...]
"""

import ast
import os
import re
import sys

# ---------------------------------------------------------------- p141, carried over
COND = {
    "js": re.compile(r"^\s*(?:\}\s*)?(if|else if)\s*\((.*)$"),
    "php": re.compile(r"^\s*(?:\}\s*)?(if|elseif)\s*\((.*)$"),
}
FLAG_READ = re.compile(
    r"os\.getenv|os\.environ|process\.env|getenv\(|\$_ENV|\bconfig\.|\bsettings\.|"
    r"\benabled\b|\bfeature_flag\b|deps\.[A-Z]", re.IGNORECASE
)
REG_JS = re.compile(r"\.(?:registerTool|tool)\s*\(\s*([^,\n]*)")
REG_GO = re.compile(r"\bRegisterTool\s*\(|\bAddTool\s*\(")
REG_PHP = re.compile(r"function\s+list_tools\s*\(")
NAME_LITERAL_JS = re.compile(r"""^\s*['"]""")

SKIP_DIRS = {".git", "node_modules", "__pycache__", "dist", "build", ".venv", "venv",
             "vendor"}

# 🔴 Trees that are present in a repository but are NOT the server it ships.
#
# This set exists because of a false positive this instrument produced on its FIRST run,
# and the false positive is more instructive than the fix. `krzysztofbury/librus-mcp`
# returned 23 literal sites -- 21 of them in `legacy_reference/src/server.py` and 2 in
# `scripts/qualify_native.py`. 🔴 **Not one came from the server the package runs.**
#
# 🔴 **p141 read exactly the same 23 files and called them 23 DYNAMIC sites.** So p141's
# librus-mcp row and this instrument's first draft disagreed about the classification of
# a population that neither should have been measuring, and the tier share was identical
# either way. 🔵 **That is why a share-based falsifier could never have caught this.**
NOT_SHIPPED = {"legacy_reference", "legacy", "scripts", "examples", "example", "docs",
               "doc", "benchmarks", "bench", "samples", "fixtures", "tests_native"}


def gated_braced(lines, i, lang):
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


def lang_of(path):
    return {".py": "python", ".js": "js", ".mjs": "js", ".cjs": "js", ".ts": "js",
            ".go": "go", ".php": "php"}.get(os.path.splitext(path)[1])


def walk(root, shipped_only=False):
    """Source files under `root`.

    `shipped_only=True` additionally drops the NOT_SHIPPED trees. Both modes are run and
    both are reported, because the difference between them IS a finding rather than a
    configuration detail.
    """
    for base, dirs, files in os.walk(root):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS
                   and not (shipped_only and d in NOT_SHIPPED)]
        for f in files:
            p = os.path.join(base, f)
            if lang_of(p):
                yield p


def is_mcp_server(root):
    hits, sdk = 0, False
    for p in walk(root):
        try:
            t = open(p, encoding="utf-8", errors="replace").read()
        except OSError:
            continue
        if re.search(r"""(from|import|require)\s*\(?\s*['"]?@?modelcontextprotocol"""
                     r"""|\bFastMCP\s*\(|new\s+McpServer\s*\(|from\s+mcp\.server""", t):
            sdk = True
        if '"tools/list"' in t or "'tools/list'" in t:
            sdk = True
        hits += len(re.findall(r"\bmcp\b", t, re.IGNORECASE))
    return sdk, hits


def is_test(p):
    q = p.replace(os.sep, "/")
    return "/test" in q or os.path.basename(q).startswith("test_")


# ---------------------------------------------------------------- REPAIRED: Python by AST
TOOL_ATTRS = {"tool", "add_tool", "register_tool", "registerTool"}


def _is_tool_attr_call(node):
    """`X.tool(...)` / `X.add_tool(...)` as a Call."""
    return (isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute)
            and node.func.attr in TOOL_ATTRS)


def indirection_decorators(tree):
    """Names of functions that FORWARD to `X.tool(...)(fn)`.

    The `edupage-mcp` shape. A function taking one argument whose body returns the result
    of calling `X.tool(...)` on that argument IS a tool registration, and `@that_name`
    is a registration site whose tool name is the decorated function's own name.
    """
    found = set()
    for node in ast.walk(tree):
        if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            continue
        args = node.args.args
        if len(args) != 1:
            continue
        param = args[0].arg
        for sub in ast.walk(node):
            # return server.tool(...)(fn)
            if (isinstance(sub, ast.Call) and _is_tool_attr_call(sub.func)
                    and any(isinstance(a, ast.Name) and a.id == param for a in sub.args)):
                found.add(node.name)
    return found


def _enclosing_flag_gate(src_lines, node, parents):
    """Is `node` lexically inside an `if` whose test reads a deployment flag?"""
    cur = node
    while cur in parents:
        cur = parents[cur]
        if isinstance(cur, ast.If):
            try:
                test_src = ast.get_source_segment("\n".join(src_lines), cur.test) or ""
            except (ValueError, TypeError):
                test_src = ""
            if FLAG_READ.search(test_src):
                return True
    return False


def _enclosing_func(node, parents):
    cur = node
    while cur in parents:
        cur = parents[cur]
        if isinstance(cur, (ast.FunctionDef, ast.AsyncFunctionDef)):
            return cur.name
    return None


def _in_loop(node, parents):
    cur = node
    while cur in parents:
        cur = parents[cur]
        if isinstance(cur, (ast.For, ast.AsyncFor, ast.While, ast.ListComp,
                            ast.DictComp, ast.SetComp, ast.GeneratorExp)):
            return True
    return False


def scan_python(path, indirect_global):
    """-> list of (lineno, kind, shape)"""
    try:
        text = open(path, encoding="utf-8", errors="replace").read()
        tree = ast.parse(text)
    except (OSError, SyntaxError):
        return []
    lines = text.splitlines()
    parents = {}
    for p in ast.walk(tree):
        for c in ast.iter_child_nodes(p):
            parents[c] = p
    indirect = indirection_decorators(tree) | indirect_global
    sites = []
    # inner `X.tool(...)` nodes already consumed as part of an `X.tool(...)(fn)` site,
    # so the same registration is not counted twice.
    consumed = {id(n.func) for n in ast.walk(tree)
                if isinstance(n, ast.Call) and _is_tool_attr_call(n.func)}

    for node in ast.walk(tree):
        if id(node) in consumed and not isinstance(
                node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            continue
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            for dec in node.decorator_list:
                kind = shape = None
                # @X.tool(...)  -- ANY arity, ANY number of lines
                if _is_tool_attr_call(dec):
                    namekw = next((k for k in dec.keywords if k.arg == "name"), None)
                    if namekw is None:
                        kind, shape = "LITERAL", "DECORATOR_CALL_NAME_FROM_FUNC"
                    elif isinstance(namekw.value, ast.Constant) and \
                            isinstance(namekw.value.value, str):
                        kind, shape = "LITERAL", "DECORATOR_CALL_NAME_LITERAL"
                    else:
                        kind, shape = "DYNAMIC", "DECORATOR_CALL_NAME_EXPR"
                # @X.tool  -- bare attribute decorator
                elif isinstance(dec, ast.Attribute) and dec.attr in TOOL_ATTRS:
                    kind, shape = "LITERAL", "DECORATOR_BARE_ATTR"
                # @_tool -- indirection decorator forwarding to X.tool(...)(fn)
                elif isinstance(dec, ast.Name) and dec.id in indirect:
                    kind, shape = "LITERAL", "DECORATOR_INDIRECTION"
                if kind is None:
                    continue
                if _enclosing_flag_gate(lines, node, parents):
                    kind = "GATED"
                sites.append((dec.lineno, kind, shape))

        # ---- X.tool(...)(fn) -- the decorator applied as an ordinary CALL.
        #
        # 🔴 The shape that BOTH p141 and this instrument's first draft missed, and the
        # dominant one in `krzysztofbury/librus-mcp` (37 sites). `server.tool(
        # annotations=local_read)(get_send_history)` registers exactly one tool whose name
        # is `get_send_history`, fixed by the source. It is as static as a decorator --
        # it IS a decorator, spelled without the `@`.
        elif (isinstance(node, ast.Call) and _is_tool_attr_call(node.func)):
            # 🔴 The forwarding call INSIDE an indirection decorator's own body is the
            # MECHANISM, not a tool. `edupage-mcp`'s `_tool` contains
            # `return server.tool(annotations=annotations)(fn)`; counting it put this
            # instrument at 32 against a hand count of 31, and the 32nd was the engine.
            # Excluding it is what makes 31 a corroboration rather than a near miss.
            if _enclosing_func(node, parents) in indirect:
                continue
            target = node.args[0] if node.args else None
            if isinstance(target, ast.Name):
                kind, shape = "LITERAL", "CALL_APPLIED_NAME_FROM_FUNC"
            elif isinstance(target, ast.Constant) and isinstance(target.value, str):
                kind, shape = "LITERAL", "CALL_APPLIED_NAME_LITERAL"
            else:
                kind, shape = "DYNAMIC", "CALL_APPLIED_TARGET_EXPR"
            if _in_loop(node, parents):
                kind, shape = "DYNAMIC", "CALL_APPLIED_IN_LOOP"
            if _enclosing_flag_gate(lines, node, parents):
                kind = "GATED"
            sites.append((node.lineno, kind, shape))

        # a bare registration CALL (not applied to anything) -- dynamic only in a loop
        elif _is_tool_attr_call(node):
            if any(node is d for f in ast.walk(tree)
                   if isinstance(f, (ast.FunctionDef, ast.AsyncFunctionDef))
                   for d in f.decorator_list):
                continue
            if _in_loop(node, parents):
                kind = "GATED" if _enclosing_flag_gate(lines, node, parents) else "DYNAMIC"
                sites.append((node.lineno, kind, "CALL_IN_LOOP"))
    return sites


def scan(root, shipped_only=False):
    lit = dyn = gated = 0
    langs, shapes, sites = set(), {}, []

    # indirection decorators may be defined in one module and used in another
    indirect_global = set()
    for p in walk(root, shipped_only):
        if lang_of(p) == "python" and not is_test(p):
            try:
                indirect_global |= indirection_decorators(
                    ast.parse(open(p, encoding="utf-8", errors="replace").read()))
            except (OSError, SyntaxError):
                pass

    for p in walk(root, shipped_only):
        lang = lang_of(p)
        if is_test(p):
            continue
        if lang == "python":
            found = scan_python(p, indirect_global)
            if found:
                langs.add("python")
            for lineno, kind, shape in found:
                shapes[shape] = shapes.get(shape, 0) + 1
                if kind == "GATED":
                    gated += 1
                elif kind == "LITERAL":
                    lit += 1
                else:
                    dyn += 1
                sites.append((os.path.relpath(p, root), lineno, kind, shape))
            continue

        # ---- JS / Go / PHP: p141 logic, unchanged
        try:
            lines = open(p, encoding="utf-8", errors="replace").read().splitlines()
        except OSError:
            continue
        for i, line in enumerate(lines):
            m = kind = None
            if lang == "js":
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
            g = gated_braced(lines, i, lang) if lang in ("js", "php") else False
            if g:
                gated += 1
                kind = "GATED"
            elif kind == "LITERAL":
                lit += 1
            else:
                dyn += 1
            shapes["%s_LINE" % lang.upper()] = shapes.get("%s_LINE" % lang.upper(), 0) + 1
            sites.append((os.path.relpath(p, root), i + 1, kind, "%s_LINE" % lang.upper()))
    return lit, dyn, gated, sorted(langs), shapes, sites


COLS = ["subject", "tier", "languages", "is_mcp_server", "literal_sites", "dynamic_sites",
        "gated_sites", "static_bounds_live", "verdict", "shapes",
        "all_tree_literal", "all_tree_dynamic", "not_shipped_delta"]


def _verdict(lit, dyn, gated):
    if gated:
        return "GATED"
    if dyn:
        return "DYNAMIC_UNBOUNDED"
    if lit:
        return "BOUNDED_STATIC"
    return "NO_REGISTRATION_SITE_FOUND"


def row(subject, root, tier):
    if not os.path.isdir(root):
        return dict(zip(COLS, [subject, tier, "-", "NO", 0, 0, 0, "n/a", "NO_CLONE",
                               "-", 0, 0, "-"]))
    sdk, mentions = is_mcp_server(root)
    if not sdk:
        langs = ",".join(sorted({lang_of(p) for p in walk(root)} - {None}))
        return dict(zip(COLS, [subject, tier, langs, "NO", 0, 0, 0, "n/a",
                               "NOT_AN_MCP_SERVER (%d 'mcp' tokens, no SDK import)"
                               % mentions, "-", 0, 0, "-"]))
    # shipped tree -- the server the package actually runs
    lit, dyn, gated, langs, shapes, _ = scan(root, shipped_only=True)
    # whole tree -- p141's inclusion policy, kept so the delta is visible
    alit, adyn, _ag, _al, _ash, _as = scan(root, shipped_only=False)
    delta = "SAME" if (alit, adyn) == (lit, dyn) \
        else "WHOLE_TREE_ADDS lit+%d dyn+%d" % (alit - lit, adyn - dyn)
    shapestr = ",".join("%s=%d" % kv for kv in sorted(shapes.items())) or "-"
    v = _verdict(lit, dyn, gated)
    return dict(zip(COLS, [subject, tier, ",".join(langs), "YES", lit, dyn, gated,
                           "YES" if v == "BOUNDED_STATIC" else "NO", v,
                           shapestr, alit, adyn, delta]))


def main(argv):
    rows = []
    for spec in argv:
        parts = spec.split("=")
        rows.append(row(parts[0], parts[1], parts[2] if len(parts) > 2 else "-"))
    print("\t".join(COLS))
    for r in rows:
        print("\t".join(str(r[c]) for c in COLS))

    print("", file=sys.stderr)
    tiers = {}
    for r in rows:
        tiers.setdefault(r["tier"], []).append(r)
    for tier, rs in sorted(tiers.items()):
        servers = [r for r in rs if r["is_mcp_server"] == "YES"]
        dynamic = [r for r in servers if r["verdict"] == "DYNAMIC_UNBOUNDED"]
        nrs = [r for r in servers if r["verdict"] == "NO_REGISTRATION_SITE_FOUND"]
        gatedr = [r for r in servers if r["gated_sites"]]
        share = (100.0 * len(dynamic) / len(servers)) if servers else 0.0
        print("# tier %-14s servers=%-2d dynamic=%-2d (%.0f%%)  gated=%d  "
              "no_site=%d" % (tier, len(servers), len(dynamic), share, len(gatedr),
                              len(nrs)), file=sys.stderr)
        if nrs:
            print("#   still invisible: %s" % ", ".join(r["subject"] for r in nrs),
                  file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
