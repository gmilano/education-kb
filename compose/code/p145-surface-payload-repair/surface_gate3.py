"""p145-surface-payload-repair -- `ACTION DZ`, and the defect `ACTION DZ` was hiding.

Derived from `p143-surface-gate-repair/surface_gate2.py`. Every classification rule in
that file is carried over unchanged; this file changes exactly two things and records
both, because the second one was not registered and is the larger of the two.

## 1. `ACTION DZ` as registered -- the `setRequestHandler` shape

> 🟢 **`ACTION DZ`** -- give `surface_gate2.py` a pattern for
> `setRequestHandler(ListToolsRequestSchema, ...)`. `P144-A` shows it reads **0** on three
> real MCP servers in both artefact kinds, so every JS/TS row on this shelf measured by it
> is suspect. Add the shape, re-run the npm and github-only tiers, and compare.
> 🔴 *Refuted if no row's verdict changes* -- which would mean the blind spot never touched
> a published figure and the instrument can stay as it is.

`REG_JS` matches `.registerTool(` and `.tool(`. A server built on the low-level SDK
registers nothing of the kind: it answers one request handler,

    server.setRequestHandler(ListToolsRequestSchema, async () => ({ tools: [ ... ] }))

and the tool surface is the array inside. `JS_LIST_HANDLER` reads that array.

## 2. 🔴 The defect this probe found on the way -- `SKIP_DIRS` is not property-relative

🔴 **`ACTION DZ` could not have changed an npm verdict, because the npm tier was never
measured.** `surface_gate2.py` skips `dist` and `build` unconditionally, in BOTH of its
modes, and **7 of the 8 npm packages on this shelf ship their entire payload under exactly
those two names**. The instrument walked **zero files** on all seven, read `0 'mcp'
tokens`, and returned `NOT_AN_MCP_SERVER` -- a verdict drawn from an empty file set.

🔵 **This is `T39` exactly, one level up from where `P144-O` applied it.** `P144-O`
established that a population exclusion is sound only relative to the property being
measured, and fixed `NOT_SHIPPED`. 🔴 **`SKIP_DIRS` was never examined**, and it carries
the same defect in a worse place: `dist/` is a regenerated artefact in a git checkout and
it is **the shipped tree itself** in a published tarball. The same name, the same
exclusion, opposite correctness.

### The rule, stated so it can be tested rather than tuned

A tree named `dist`/`build` is admitted when, and only when, **excluding it would leave
the package with no declared entry point**:

  * read `package.json` for `main`, `bin`, `module`, `exports`;
  * if every declared entry resolves inside a `dist`/`build` tree, that tree IS the
    shipped source and is admitted (`artefact=PAYLOAD`);
  * otherwise it is a build artefact beside its own source and stays excluded
    (`artefact=SOURCE`).

🟢 **This also forecloses `T37`'s defect by construction.** `P144-A`'s first draft read a
committed `dist/` *and* its source and double-counted. Here the two are mutually exclusive
by rule, and the mode used is printed in a column rather than assumed.
"""

import ast
import json
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
# 🆕 `ACTION DZ`: the low-level SDK shape. A server that answers `tools/list` itself
# registers no tools by name; its surface is the array the handler returns.
LIST_HANDLER = re.compile(
    r"setRequestHandler\s*\(\s*(?:[A-Za-z_$][\w$]*\.)*ListToolsRequestSchema")
# A tool descriptor inside that array: `name:` carrying a schema in its object.
DESCRIPTOR = re.compile(r"""\bname\s*:\s*['"]([a-z][a-z0-9_.-]{2,63})['"]""")
SCHEMA_MARK = re.compile(r"inputSchema|input_schema")
# A spread in the returned array -- the surface is not static.
SPREAD = re.compile(r"\.\.\.\s*([A-Za-z_$][\w$.]*)")
# A spread of a CALL, e.g. `...ref.courseTools.getToolDefinitions()`. The spread array is
# assembled from function returns, and this instrument does not follow a call.
SPREAD_CALL = re.compile(r"\.\.\.\s*[A-Za-z_$][\w$.]*\s*\(")
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


# 🔴 `dist` and `build` are NOT unconditionally skippable -- see the module docstring.
# They are generated artefacts beside their own source in a git checkout, and they are the
# shipped tree itself in a published tarball. Which one a given root is, is a question its
# own `package.json` answers.
BUILT_TREES = {"dist", "build", "lib", "out"}


def declared_entries(root):
    """Top-level trees the package declares as its entry surface, from `package.json`."""
    pj = os.path.join(root, "package.json")
    if not os.path.isfile(pj):
        return set()
    try:
        with open(pj, encoding="utf-8", errors="replace") as fh:
            meta = json.load(fh)
    except (OSError, ValueError):
        return set()
    paths = []
    for key in ("main", "module", "browser"):
        v = meta.get(key)
        if isinstance(v, str):
            paths.append(v)
    b = meta.get("bin")
    if isinstance(b, str):
        paths.append(b)
    elif isinstance(b, dict):
        paths.extend(v for v in b.values() if isinstance(v, str))

    def walk_exports(node):
        if isinstance(node, str):
            paths.append(node)
        elif isinstance(node, dict):
            for v in node.values():
                walk_exports(v)
        elif isinstance(node, list):
            for v in node:
                walk_exports(v)
    walk_exports(meta.get("exports"))

    trees = set()
    for q in paths:
        parts = q.lstrip("./").split("/")
        if len(parts) > 1 and parts[0] in BUILT_TREES:
            trees.add(parts[0])
    return trees


def payload_trees(root):
    """The `dist`/`build` trees to ADMIT for this root, by the property-relative rule.

    Admitted only when excluding them would leave the package with no declared entry
    point -- i.e. the package ships compiled output and nothing else. When source sits
    beside the built tree, the built tree stays excluded and `T37`'s double count cannot
    occur.
    """
    declared = declared_entries(root) & SKIP_DIRS
    if not declared:
        return set()
    # Is there any source file OUTSIDE the declared built trees?
    for base, dirs, files in os.walk(root):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for f in files:
            if lang_of(os.path.join(base, f)):
                return set()          # source exists beside the build -> SOURCE mode
    return declared                   # compiled output is all there is -> PAYLOAD mode


def walk(root, shipped_only=False, admit=None):
    """Source files under `root`.

    `shipped_only=True` additionally drops the NOT_SHIPPED trees. Both modes are run and
    both are reported, because the difference between them IS a finding rather than a
    configuration detail.

    `admit` is the set of otherwise-skipped built trees that this root's own
    `package.json` proves to be its shipped source.
    """
    skip = SKIP_DIRS - (admit or set())
    for base, dirs, files in os.walk(root):
        dirs[:] = [d for d in dirs if d not in skip
                   and not (shipped_only and d in NOT_SHIPPED)]
        for f in files:
            p = os.path.join(base, f)
            if lang_of(p):
                yield p


def is_mcp_server(root, admit=None):
    hits, sdk = 0, False
    for p in walk(root, admit=admit):
        try:
            with open(p, encoding="utf-8", errors="replace") as fh:
                t = fh.read()
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


def brace_body(text, start):
    """(body, end) for the first brace-balanced block at or after `start`."""
    i = text.find("{", start)
    if i == -1:
        return "", start
    depth = 0
    for j in range(i, len(text)):
        if text[j] == "{":
            depth += 1
        elif text[j] == "}":
            depth -= 1
            if depth == 0:
                return text[i:j + 1], j
    return text[i:], len(text)


def balanced(text, start, open_ch="[", close_ch="]"):
    """The bracket-balanced slice beginning at the first `open_ch` at or after `start`."""
    i = text.find(open_ch, start)
    if i == -1:
        return ""
    depth = 0
    for j in range(i, len(text)):
        if text[j] == open_ch:
            depth += 1
        elif text[j] == close_ch:
            depth -= 1
            if depth == 0:
                return text[i:j + 1]
    return text[i:]


def count_descriptors(block):
    """Distinct tool names in an array of descriptor objects carrying a schema."""
    names = set()
    for d in DESCRIPTOR.finditer(block):
        if SCHEMA_MARK.search(block[d.end(): d.end() + 900]) or \
                SCHEMA_MARK.search(block[max(0, d.start() - 900): d.start()]):
            names.add(d.group(1))
    return names


def resolve_array(ident, text, payload):
    """Classify what `ident` holds. Returns (kind, names, shape).

    🔵 One level of resolution, and the limit is stated rather than hidden: an identifier
    assigned from a function call is NOT followed into that function.
    """
    for body in [text] + [t for t in payload if t is not text]:
        m = re.search(r"\b(?:const|let|var)\s+%s\s*=\s*" % re.escape(ident), body)
        if not m:
            continue
        tail = body[m.end(): m.end() + 200]
        # 🔴 `.push()` anywhere on this identifier means the list is assembled, not declared.
        mutated = re.search(r"\b%s\s*\.\s*push\s*\(" % re.escape(ident), body)
        if tail.lstrip().startswith("["):
            block = balanced(body, m.end())
            names = count_descriptors(block)
            call_spreads = SPREAD_CALL.findall(block)
            if mutated:
                return "DYNAMIC", names, "JS_LIST_HANDLER_MUTATED"
            if call_spreads:
                return "DYNAMIC", names, "JS_LIST_HANDLER_SPREAD_CALL"
            if names:
                return "LITERAL", names, "JS_LIST_HANDLER_REF"
            return "DYNAMIC", names, "JS_LIST_HANDLER_REF_EMPTY"
        if re.match(r"\s*[A-Za-z_$][\w$.]*\s*\(", tail):
            return "DYNAMIC", set(), ("JS_LIST_HANDLER_MUTATED" if mutated
                                      else "JS_LIST_HANDLER_FROM_CALL")
    return "DYNAMIC", set(), "JS_LIST_HANDLER_UNRESOLVED"


RETURN_IDENT = re.compile(r"\btools\s*:\s*([A-Za-z_$][\w$]*)\s*(\()?")
RETURN_SHORT = re.compile(r"\{\s*tools\s*\}")
# An array built inside the handler body itself -- `_imazhar101`'s shape.
INLINE_ARRAY = re.compile(r"\b(?:const|let|var)\s+([A-Za-z_$][\w$]*)\s*=\s*\[")


def scan_js_list_handler(text, payload=()):
    """🆕 `ACTION DZ` -- the tool surface of a `ListToolsRequestSchema` handler.

    `REG_JS` matches `.registerTool(`/`.tool(` and is blind to the low-level SDK shape,
    where the whole surface is the array one handler returns. Five shapes occur on this
    shelf and each is classified rather than lumped:

      `JS_LIST_HANDLER`             descriptors written inline in the handler body
      `JS_LIST_HANDLER_REF`         handler returns an identifier that IS a literal array
      `JS_LIST_HANDLER_SPREAD_CALL` the array spreads method calls -- not resolvable here
      `JS_LIST_HANDLER_MUTATED`     the array is `.push()`ed into; runtime-extensible
      `JS_LIST_HANDLER_FROM_CALL`   the identifier is a function's return value
      `JS_LIST_HANDLER_UNRESOLVED`  no declaration found in the payload

    🔵 Only the first two bound the live list. The other four are reported as DYNAMIC
    because this instrument does not follow a call, and saying so is the point.
    """
    out = []
    for m in LIST_HANDLER.finditer(text):
        body, _ = brace_body(text, m.end())
        if not body:
            continue
        lineno = text.count("\n", 0, m.start()) + 1
        inline = count_descriptors(body)
        if inline:
            for _ in sorted(inline):
                out.append((lineno, "LITERAL", "JS_LIST_HANDLER"))
            continue

        # 🔵 The array may be assembled INSIDE the handler, which is a statement about
        # the surface in its own right -- `_imazhar101` spreads 18 method calls here.
        mia = INLINE_ARRAY.search(body)
        if mia:
            block = balanced(body, mia.end() - 1)
            names = count_descriptors(block)
            spread_calls = SPREAD_CALL.findall(block)
            if spread_calls:
                for _ in spread_calls:
                    out.append((lineno, "DYNAMIC", "JS_LIST_HANDLER_SPREAD_CALL"))
                continue
            if names:
                for _ in sorted(names):
                    out.append((lineno, "LITERAL", "JS_LIST_HANDLER_INLINE_ARRAY"))
                continue

        ident, wrapped = None, False
        mi = RETURN_IDENT.search(body)
        if mi:
            ident, wrapped = mi.group(1), bool(mi.group(2))
        elif RETURN_SHORT.search(body):
            ident = "tools"
        if wrapped:
            # 🔴 `return { tools: f(tools, …) }` -- the published surface is a FUNCTION of
            # the array, so the array alone does not bound it.
            out.append((lineno, "DYNAMIC", "JS_LIST_HANDLER_WRAPPED"))
            continue
        if not ident:
            out.append((lineno, "DYNAMIC", "JS_LIST_HANDLER_UNRESOLVED"))
            continue
        kind, names, shape = resolve_array(ident, text, payload)
        if kind == "LITERAL":
            for _ in sorted(names):
                out.append((lineno, "LITERAL", shape))
        else:
            out.append((lineno, "DYNAMIC", shape))
    return out


def scan(root, shipped_only=False, admit=None):
    lit = dyn = gated = 0
    langs, shapes, sites = set(), {}, []

    # The whole JS payload, so a handler's identifier can be resolved across modules.
    js_payload = []
    for q in walk(root, shipped_only, admit):
        if lang_of(q) == "js" and not is_test(q):
            try:
                js_payload.append(open(q, encoding="utf-8", errors="replace").read())
            except OSError:
                pass

    # indirection decorators may be defined in one module and used in another
    indirect_global = set()
    for p in walk(root, shipped_only, admit):
        if lang_of(p) == "python" and not is_test(p):
            try:
                indirect_global |= indirection_decorators(
                    ast.parse(open(p, encoding="utf-8", errors="replace").read()))
            except (OSError, SyntaxError):
                pass

    for p in walk(root, shipped_only, admit):
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
            raw = open(p, encoding="utf-8", errors="replace").read()
        except OSError:
            continue
        lines = raw.splitlines()

        # 🆕 `ACTION DZ`: the low-level SDK shape, which `REG_JS` cannot see at all.
        if lang == "js":
            for lineno, kind, shape in scan_js_list_handler(raw, js_payload):
                langs.add("js")
                shapes[shape] = shapes.get(shape, 0) + 1
                if kind == "LITERAL":
                    lit += 1
                else:
                    dyn += 1
                sites.append((os.path.relpath(p, root), lineno, kind, shape))
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


COLS = ["subject", "tier", "artefact", "admitted", "languages", "is_mcp_server",
        "literal_sites", "dynamic_sites", "gated_sites", "static_bounds_live", "verdict",
        "shapes", "all_tree_literal", "all_tree_dynamic", "not_shipped_delta"]


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
        return dict(zip(COLS, [subject, tier, "-", "-", "-", "NO", 0, 0, 0, "n/a",
                               "NO_CLONE", "-", 0, 0, "-"]))
    # 🔴 The property-relative exclusion decision, made per root and PRINTED.
    admit = payload_trees(root)
    mode = "PAYLOAD" if admit else "SOURCE"
    admitted = ",".join(sorted(admit)) or "-"

    sdk, mentions = is_mcp_server(root, admit)
    if not sdk:
        langs = ",".join(sorted({lang_of(p) for p in walk(root, admit=admit)} - {None}))
        return dict(zip(COLS, [subject, tier, mode, admitted, langs, "NO", 0, 0, 0, "n/a",
                               "NOT_AN_MCP_SERVER (%d 'mcp' tokens, no SDK import)"
                               % mentions, "-", 0, 0, "-"]))
    # shipped tree -- the server the package actually runs
    lit, dyn, gated, langs, shapes, _ = scan(root, shipped_only=True, admit=admit)
    # whole tree -- p141's inclusion policy, kept so the delta is visible
    alit, adyn, _ag, _al, _ash, _as = scan(root, shipped_only=False, admit=admit)
    delta = "SAME" if (alit, adyn) == (lit, dyn) \
        else "WHOLE_TREE_ADDS lit+%d dyn+%d" % (alit - lit, adyn - dyn)
    shapestr = ",".join("%s=%d" % kv for kv in sorted(shapes.items())) or "-"
    v = _verdict(lit, dyn, gated)
    return dict(zip(COLS, [subject, tier, mode, admitted, ",".join(langs), "YES",
                           lit, dyn, gated,
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
