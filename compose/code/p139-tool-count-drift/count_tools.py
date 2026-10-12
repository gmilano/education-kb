"""p139-tool-count-drift — count the tools a shipped MCP build REGISTERS, and the tools
its own README DOCUMENTS.

Executes p138's `ACTION CK`. p138 measured this by hand for two repositories and found
`Jawadh-Salih/moodle-mcp-server` registering 19 tools and documenting 14, with two write
tools (`submit_journal`, `update_assignment`) in neither list. `ACTION CK` asks whether
that disagreement is the shelf's habit or those two repositories'.

Nothing here executes package code. Every payload is read as text.

## What counts as a registered tool

An MCP tool is a **name with an input schema**. That is the rule, and it is the rule
because the first draft of this probe used "a `name:` key in a file that mentions
`ListToolsRequestSchema`" and got two rows wrong in opposite directions:

* 🔴 `moodle-mcp-server-aql` came back with **0 tools over 34 source files**, because it
  uses a module-per-tool layout (`export const name = "list_courses"`) and its tool
  modules never mention the schema symbol — the handler that does is in another file.
* 🔴 `@imazhar101/mcp-canvas-server` came back with **3**, because its ~230 tools are
  defined in per-domain classes returning `getToolDefinitions()`, again in files with no
  schema symbol. The 3 it did find included `beta` and `prod`, which are
  `{ name: 'beta', suffix: '_BETA' }` environment entries and not tools at all.

Three idioms exist on this shelf and each gets a rule:

  direct   `server.registerTool("moodle_courses", {…})`, `server.tool("x", …)`
  adjacent `{ name: "get_courses", description: …, inputSchema: {…} }`
  module   a file exporting both `name = "list_courses"` and `inputSchema`

The adjacency window is what excludes `{ name: 'beta', suffix: '_BETA' }`: it carries no
`inputSchema`, so it is not a tool however tool-shaped the string looks.
"""

import json
import re
from pathlib import Path

JS_SUFFIXES = {".js", ".mjs", ".cjs"}
TS_SUFFIXES = {".ts", ".mts", ".cts"}

# A tool name on this shelf: lower snake_case, occasionally with a dot or dash.
_TOOL_NAME = r"[a-z][a-z0-9_.-]{2,63}"

# idiom 1 — a direct registration call names its tool in the first argument.
DIRECT = re.compile(r"(?:registerTool|\.tool)\(\s*[\"'](" + _TOOL_NAME + r")[\"']")

# idiom 2 — an object literal carrying a name and, within the window, an input schema.
NAME_LITERAL = re.compile(r"\bname\s*:\s*[\"'](" + _TOOL_NAME + r")[\"']")

# idiom 3 — a module that exports a tool's name and its schema as separate bindings.
MODULE_NAME = re.compile(r"\bname\s*=\s*[\"'](" + _TOOL_NAME + r")[\"']")

SCHEMA_MARKER = re.compile(r"inputSchema|input_schema")

SERVER_CTOR = re.compile(
    r"new\s+(?:Mcp)?Server\s*\(\s*\{[^{}]*?\bname\s*:\s*[\"']([^\"']+)[\"']",
    re.DOTALL,
)
LISTTOOLS = re.compile(r"ListToolsRequestSchema|registerTool|\.tool\(")

# How far after a `name:` key an `inputSchema` may sit and still belong to the same
# object. A tool's description is the only thing between them, and descriptions on this
# shelf run long -- `moodle-mcp-server-aql`'s are three concatenated string literals.
ADJACENCY_WINDOW = 900

# A README documents a tool by naming it. Backticked snake_case is the convention the
# whole shelf uses; a bare prose word is not counted, because "courses" in a sentence is
# not a claim that a `courses` tool exists.
README_BACKTICK = re.compile(r"`([a-z][a-z0-9_.-]{2,63})`")


def iter_source(pkg_dir):
    """Yield (relative_path, text) for every shipped source file, build first."""
    pkg_dir = Path(pkg_dir)
    files = [p for p in pkg_dir.rglob("*") if p.is_file()]
    js = [p for p in files if p.suffix.lower() in JS_SUFFIXES]
    chosen = js if js else [p for p in files if p.suffix.lower() in TS_SUFFIXES]
    for p in sorted(chosen):
        try:
            yield p.relative_to(pkg_dir).as_posix(), p.read_text(errors="replace")
        except OSError:
            continue


def adjacent_tools(text, window=ADJACENCY_WINDOW):
    """Names whose object also carries an input schema, within `window` characters."""
    out = set()
    for m in NAME_LITERAL.finditer(text):
        tail = text[m.end():m.end() + window]
        if SCHEMA_MARKER.search(tail):
            out.add(m.group(1))
    return out


def module_tools(text):
    """A module exporting both a tool name and an input schema declares one tool."""
    if not SCHEMA_MARKER.search(text):
        return set()
    return set(MODULE_NAME.findall(text))


def server_names(texts):
    """Identities the package gives its own server — never tools."""
    out = set()
    for text in texts:
        out.update(SERVER_CTOR.findall(text))
    return out


def build_tools(pkg_dir, package_name=None):
    """The set of tool names the shipped build registers, and how each was found."""
    by_path = dict(iter_source(pkg_dir))
    texts = list(by_path.values())

    excluded = server_names(texts)
    if package_name:
        excluded.add(package_name)
        excluded.add(package_name.split("/")[-1])

    direct, adjacent, module = set(), set(), set()
    for text in texts:
        direct.update(DIRECT.findall(text))
        adjacent.update(adjacent_tools(text))
        module.update(module_tools(text))

    tools = (direct | adjacent | module) - excluded
    idioms = [n for n, s in (("direct", direct), ("adjacent", adjacent),
                             ("module", module)) if s - excluded]
    return {
        "tools": tools,
        "direct": direct - excluded,
        "adjacent": adjacent - excluded,
        "module": module - excluded,
        "excluded_server_names": excluded,
        "source_files": len(by_path),
        "idiom": "+".join(idioms) if idioms else "none",
        "serves_tools": any(LISTTOOLS.search(t) for t in texts),
    }


def readme_tools(pkg_dir):
    """Backticked tool-shaped tokens in the package's own README."""
    pkg_dir = Path(pkg_dir)
    for name in ("README.md", "readme.md", "README.MD", "Readme.md"):
        p = pkg_dir / name
        if p.is_file():
            return set(README_BACKTICK.findall(p.read_text(errors="replace"))), name
    return set(), None


def manifest_name(pkg_dir):
    p = Path(pkg_dir) / "package.json"
    if not p.is_file():
        return None
    try:
        return json.loads(p.read_text(errors="replace")).get("name")
    except (OSError, ValueError):
        return None


# A tool that MUTATES the LMS. The axis matters more than the count: an undocumented
# read tool is a missing paragraph, an undocumented `bulk_update_grades` is an
# ungoverned capability — and "grading or ranking learners" is named high-risk by
# Vietnam's Decision 33/2026/QĐ-TTg and by EU AI Act Annex III.
WRITE_VERB = re.compile(
    r"^(create|update|delete|submit|post|put|remove|add|set|enroll|grade|bulk|upload|"
    r"send|mark|assign|reset|clear|duplicate|import|move|edit|hide|publish|unpublish|"
    r"archive|restore|accept|decline|reorder|activate|deactivate)_"
    r"|_(create|update|delete|submit|upload)(_|$)"
)


def is_write_tool(name):
    return bool(WRITE_VERB.search(name))


def drift(pkg_dir):
    """Compare what the build registers with what the README names.

    `undocumented` is the finding that matters to a client: a tool the server will
    answer that its documentation never mentions. `phantom` is the opposite — a
    snake_case token the README presents as a tool that the build does not register.
    """
    name = manifest_name(pkg_dir)
    b = build_tools(pkg_dir, name)
    rm, rm_file = readme_tools(pkg_dir)

    documented = b["tools"] & rm
    undocumented = b["tools"] - rm
    # Only snake_case README tokens are candidate phantoms: `npm`, `dist` and `node`
    # are backticked in every README on the shelf and are not tool claims.
    phantom = {t for t in rm - b["tools"] if "_" in t}

    return {
        "package": name,
        "readme": rm_file,
        "write_tools": sorted(t for t in b["tools"] if is_write_tool(t)),
        "undocumented_writes": sorted(t for t in undocumented if is_write_tool(t)),
        "source_files": b["source_files"],
        "idiom": b["idiom"],
        "serves_tools": b["serves_tools"],
        "build_tools": sorted(b["tools"]),
        "documented": sorted(documented),
        "undocumented": sorted(undocumented),
        "phantom": sorted(phantom),
        "disagrees": bool(undocumented or phantom),
    }
