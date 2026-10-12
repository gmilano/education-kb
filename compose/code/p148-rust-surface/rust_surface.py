"""p148-rust-surface -- `ACTION EO` and `ACTION EP`: a Rust reader, and set identity.

`T64` (p147) named three causes of an empty walk, and the third was a language outside
`surface_gate.lang_of`'s map. The row it hid is `zavora-ai/mcp-student-records` --
🟢 **Apache-2.0, 46 tools, a declared `mcp-server.toml` with a typed risk class per tool**
-- and p147 measured it with `grep`, which is exactly what this KB tells itself not to do.

Two actions, one instrument, because they read the same two artefacts:

| action | question | falsifier |
|---|---|---|
| `EO` | do the router and the manifest both read **46**? | refuted if they do not both read 46 |
| `EP` | are the 46 names equal as **SETS**, not as counts? | refuted if the name sets are not equal |

🔵 **`EO` is the weaker question and it is worth stating why.** Two counts agreeing at 46 is
compatible with 46 names on one side and 46 *different* names on the other. `P144-G` has
called this the bidirectional gap for four passes. `EP` is the question that closes it.

## Method -- a brace-tracked reader, not a line grep

`#[tool(...)]` is only a tool registration when it sits inside the `impl` block that
`#[tool_router]` annotates. A line-oriented count cannot know that, so this module:

1. finds `#[tool_router]` and the `impl ... {` that follows it;
2. tracks brace depth to find that block's extent, ignoring braces inside string
   literals, char literals, line comments and block comments;
3. inside the block only, pairs each `#[tool(` attribute with the `fn <name>` that
   follows it, taking an explicit `name = "..."` in the attribute when present and
   falling back to the function identifier when it is not;
4. reads `[[tools]]` `name = "..."` from `mcp-server.toml` with a minimal TOML
   table-array scan.

🟢 **The reader refuses rather than returning zero** (`T64`'s rule, and the generalisable
line from p147's register): a tree with no `.rs` file, no `#[tool_router]`, or no
`mcp-server.toml` yields `NO_RUST_SURFACE_READ` / `NO_MANIFEST_READ`, never `0`.

    python3 rust_surface.py <repo-dir>
    python3 test_rust_surface.py      # 14 tests, authored fixtures, offline
"""

import os
import re
import sys

RUST_EXT = ".rs"
TOOL_ATTR = "#[tool"
ROUTER_ATTR = "#[tool_router]"
FN_NAME = re.compile(r"\bfn\s+([A-Za-z_][A-Za-z0-9_]*)")
ATTR_NAME = re.compile(r"""\bname\s*=\s*["']([^"']+)["']""")
TOML_ARRAY = re.compile(r"^\s*\[\[\s*tools\s*\]\]\s*$")
TOML_NAME = re.compile(r"""^\s*name\s*=\s*["']([^"']+)["']""")


def strip_rust(src):
    """Blank out string/char literals and comments, preserving length and newlines.

    Brace depth is only meaningful over code, and a `}` inside a doc comment or a
    format string is not a block end. Length is preserved so offsets stay valid.
    """
    out = list(src)
    i, n = 0, len(src)
    while i < n:
        c = src[i]
        nxt = src[i + 1] if i + 1 < n else ""
        if c == "/" and nxt == "/":
            while i < n and src[i] != "\n":
                out[i] = " "
                i += 1
        elif c == "/" and nxt == "*":
            depth = 0
            while i < n:
                if src[i] == "/" and i + 1 < n and src[i + 1] == "*":
                    depth += 1
                    out[i] = out[i + 1] = " "
                    i += 2
                    continue
                if src[i] == "*" and i + 1 < n and src[i + 1] == "/":
                    depth -= 1
                    out[i] = out[i + 1] = " "
                    i += 2
                    if depth == 0:
                        break
                    continue
                if src[i] != "\n":
                    out[i] = " "
                i += 1
        elif c == '"':
            raw = src[max(0, i - 2):i] in ("r#", 'r"') or src[max(0, i - 1):i] == "r"
            out[i] = " "
            i += 1
            while i < n:
                if src[i] == "\\" and not raw:
                    out[i] = " "
                    if i + 1 < n and src[i + 1] != "\n":
                        out[i + 1] = " "
                    i += 2
                    continue
                if src[i] == '"':
                    out[i] = " "
                    i += 1
                    break
                if src[i] != "\n":
                    out[i] = " "
                i += 1
        elif c == "'":
            # a char literal is at most 'x' or '\n'; a lifetime ('a) has no closing quote
            m = re.match(r"'(\\.|[^'\\])'", src[i:])
            if m:
                for k in range(i, i + m.end()):
                    out[k] = " "
                i += m.end()
            else:
                i += 1
        else:
            i += 1
    return "".join(out)


def router_block(code):
    """Return (start, end) offsets of the impl block annotated `#[tool_router]`."""
    at = code.find(ROUTER_ATTR)
    if at < 0:
        return None
    brace = code.find("{", at)
    if brace < 0:
        return None
    depth, i, n = 0, brace, len(code)
    while i < n:
        if code[i] == "{":
            depth += 1
        elif code[i] == "}":
            depth -= 1
            if depth == 0:
                return (brace, i)
        i += 1
    return None


def router_tools(src):
    """Tool names registered inside the `#[tool_router]` impl block, in source order."""
    code = strip_rust(src)
    span = router_block(code)
    if span is None:
        return None
    start, end = span
    names, i = [], start
    while True:
        at = code.find(TOOL_ATTR, i)
        if at < 0 or at > end:
            break
        # `#[tool(` and `#[tool]` register; `#[tool_router]` does not
        tail = code[at + len(TOOL_ATTR):at + len(TOOL_ATTR) + 1]
        if tail not in ("(", "]"):
            i = at + len(TOOL_ATTR)
            continue
        close = code.find("]", at)
        attr_src = src[at:close + 1] if close > at else ""
        explicit = ATTR_NAME.search(attr_src)
        fn = FN_NAME.search(code, close if close > at else at, end)
        if explicit:
            names.append(explicit.group(1))
        elif fn:
            names.append(fn.group(1))
        i = (close if close > at else at) + 1
    return names


def manifest_tools(path):
    """`[[tools]]` names from an `mcp-server.toml`, in file order."""
    if not os.path.exists(path):
        return None
    names, in_tool = [], False
    with open(path, encoding="utf-8", errors="replace") as fh:
        for line in fh:
            if TOML_ARRAY.match(line):
                in_tool = True
                continue
            if line.lstrip().startswith("[") and not TOML_ARRAY.match(line):
                in_tool = False
                continue
            if in_tool:
                m = TOML_NAME.match(line)
                if m:
                    names.append(m.group(1))
                    in_tool = False
    return names


def rust_files(root):
    found = []
    for dirpath, dirs, files in os.walk(root):
        dirs[:] = [d for d in dirs if d not in {".git", "target", "node_modules"}]
        for f in files:
            if f.endswith(RUST_EXT):
                found.append(os.path.join(dirpath, f))
    return sorted(found)


def measure(root):
    """Measure one repository. Returns a dict; refuses rather than returning zero."""
    res = {"root": root, "rs_files": 0, "router_file": None,
           "router": None, "manifest": None, "verdict": None}
    rs = rust_files(root)
    res["rs_files"] = len(rs)
    if not rs:
        res["verdict"] = "NO_RUST_SURFACE_READ (no .rs file walked)"
        return res
    for path in rs:
        with open(path, encoding="utf-8", errors="replace") as fh:
            src = fh.read()
        got = router_tools(src)
        if got is not None:
            res["router"], res["router_file"] = got, os.path.relpath(path, root)
            break
    if res["router"] is None:
        res["verdict"] = "NO_RUST_SURFACE_READ (no #[tool_router] in %d .rs files)" % len(rs)
        return res
    res["manifest"] = manifest_tools(os.path.join(root, "mcp-server.toml"))
    if res["manifest"] is None:
        res["verdict"] = "NO_MANIFEST_READ (no mcp-server.toml)"
        return res
    r, m = res["router"], res["manifest"]
    rs_set, m_set = set(r), set(m)
    res["count_equal"] = len(r) == len(m)
    res["set_equal"] = rs_set == m_set
    res["router_only"] = sorted(rs_set - m_set)
    res["manifest_only"] = sorted(m_set - rs_set)
    res["router_dupes"] = sorted({x for x in r if r.count(x) > 1})
    res["manifest_dupes"] = sorted({x for x in m if m.count(x) > 1})
    res["order_equal"] = r == m
    res["verdict"] = ("SET_IDENTICAL" if res["set_equal"]
                      else "SET_DIVERGENT")
    return res


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2
    res = measure(argv[1])
    print("root            %s" % res["root"])
    print("rs files        %d" % res["rs_files"])
    if res["router"] is None or res["manifest"] is None:
        print("verdict         %s" % res["verdict"])
        return 1
    print("router file     %s" % res["router_file"])
    print("router tools    %d" % len(res["router"]))
    print("manifest tools  %d" % len(res["manifest"]))
    print("ACTION EO       counts %s" % ("AGREE" if res["count_equal"] else "DISAGREE"))
    print("ACTION EP       %s" % res["verdict"])
    print("router_only     %s" % (res["router_only"] or "-"))
    print("manifest_only   %s" % (res["manifest_only"] or "-"))
    print("router dupes    %s" % (res["router_dupes"] or "-"))
    print("manifest dupes  %s" % (res["manifest_dupes"] or "-"))
    print("order identical %s" % res["order_equal"])
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
