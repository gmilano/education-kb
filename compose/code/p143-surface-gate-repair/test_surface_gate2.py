"""Tests for p143-surface-gate-repair.

Each test pins a defect that was REAL -- every one of them was produced by this
instrument or by `p141-agent-surface-gate` on a subject in this KB's population, and
the test exists so the repair cannot be silently undone.

Run: python3 -I -m pytest test_surface_gate2.py -q
     (or: python3 -I test_surface_gate2.py  for a dependency-free run)
"""

import ast
import os
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import surface_gate2 as sg  # noqa: E402


def _sites(src, extra=""):
    """Parse `src` as a module and return scan_python's sites."""
    with tempfile.TemporaryDirectory() as d:
        p = os.path.join(d, "mod.py")
        open(p, "w", encoding="utf-8").write(src)
        indirect = sg.indirection_decorators(ast.parse(src + extra))
        return sg.scan_python(p, indirect)


# --------------------------------------------------------------- the p141 blind spots
def test_multiline_decorator_is_seen():
    """🔴 p141's `@(\\w+)\\.tool\\s*\\(([^)]*)\\)` is line-based, so a decorator whose
    `(` and `)` are on different lines never matched. `global-education-mcp` declares
    10 of 10 tools this way and p141 returned NO_REGISTRATION_SITE_FOUND."""
    src = (
        "@mcp.tool(\n"
        "    annotations={\n"
        '        "readOnlyHint": True,\n'
        '        "title": "x",\n'
        "    },\n"
        ")\n"
        "async def uis_list_countries(params):\n"
        '    """doc"""\n'
        "    return 1\n"
    )
    sites = _sites(src)
    assert len(sites) == 1, sites
    assert sites[0][1] == "LITERAL"
    assert sites[0][2] == "DECORATOR_CALL_NAME_FROM_FUNC"


def test_indirection_decorator_is_seen():
    """🔴 `edupage-mcp` decorates 31 functions with a bare `@_tool`, where `_tool`
    forwards to `server.tool(...)(fn)`. No `.tool(` token appears at any decoration
    site, so p141 saw nothing on its best-annotated row."""
    src = (
        "def _tool(fn):\n"
        "    return server.tool(annotations=None)(fn)\n"
        "\n"
        "@_tool\n"
        "def get_grades():\n"
        "    return 1\n"
        "\n"
        "@_tool\n"
        "def get_meals():\n"
        "    return 2\n"
    )
    sites = _sites(src)
    kinds = [s[1] for s in sites]
    shapes = [s[2] for s in sites]
    assert kinds.count("LITERAL") == 2, sites
    assert shapes.count("DECORATOR_INDIRECTION") == 2, sites


def test_indirection_body_is_not_counted_as_a_tool():
    """🔴 The forwarding call inside `_tool` is the MECHANISM. Counting it put this
    instrument at 32 on `edupage-mcp` against a hand count of 31."""
    src = (
        "def _tool(fn):\n"
        "    return server.tool(annotations=None)(fn)\n"
        "\n"
        "@_tool\n"
        "def only_one():\n"
        "    return 1\n"
    )
    sites = _sites(src)
    assert len(sites) == 1, sites
    assert sites[0][2] == "DECORATOR_INDIRECTION"


def test_call_applied_decorator_is_seen():
    """🔴 `librus-mcp` registers 35 tools as `server.tool(annotations=x)(fn)` -- a
    decorator spelled without the `@`. p141 missed all 35; this instrument's FIRST
    draft also missed all 35 and reported 23 sites from `legacy_reference/` instead."""
    src = (
        "def register(server):\n"
        "    server.tool(annotations=local_read)(get_send_history)\n"
        "    server.tool(annotations=local_write)(preview_message)\n"
    )
    sites = _sites(src)
    assert len(sites) == 2, sites
    assert all(s[1] == "LITERAL" for s in sites), sites
    assert all(s[2] == "CALL_APPLIED_NAME_FROM_FUNC" for s in sites), sites


# --------------------------------------------------------------- dynamism still detected
def test_name_expression_is_dynamic():
    """A repair must not make everything literal. `ahmedEid1/lumen` passes a computed
    name and genuinely is unbounded; it must stay DYNAMIC."""
    src = (
        "@mcp.tool(name=t['name'])\n"
        "def handler(params):\n"
        "    return 1\n"
    )
    sites = _sites(src)
    assert len(sites) == 1, sites
    assert sites[0][1] == "DYNAMIC", sites
    assert sites[0][2] == "DECORATOR_CALL_NAME_EXPR"


def test_registration_in_a_loop_is_dynamic():
    """p140's 61-tool blind spot: `for t in TOOLS: register(t.name, ...)`."""
    src = (
        "def register(server, TOOLS):\n"
        "    for t in TOOLS:\n"
        "        server.add_tool(t.name, t.fn)\n"
    )
    sites = _sites(src)
    assert len(sites) == 1, sites
    assert sites[0][1] == "DYNAMIC", sites


def test_call_applied_in_a_loop_is_dynamic():
    """The call-applied shape is static only OUTSIDE a loop. Inside one the iterated
    collection bounds it, not the source text."""
    src = (
        "def register(server, FNS):\n"
        "    for fn in FNS:\n"
        "        server.tool(annotations=None)(fn)\n"
    )
    sites = _sites(src)
    assert len(sites) == 1, sites
    assert sites[0][1] == "DYNAMIC", sites
    assert sites[0][2] == "CALL_APPLIED_IN_LOOP", sites


# --------------------------------------------------------------- population limits
def test_not_shipped_trees_are_excluded():
    """🔴 The defect that made the tier share move. `legacy_reference/` is dead code;
    21 of p141's 23 librus-mcp sites were in it."""
    assert "legacy_reference" in sg.NOT_SHIPPED
    assert "scripts" in sg.NOT_SHIPPED
    assert "examples" in sg.NOT_SHIPPED


def test_compiled_output_is_still_skipped():
    """🔵 `dist`/`build` stay skipped, and that is WHY the npm tier is unmeasurable
    with this instrument: 7 of 8 npm packages ship only compiled output. The figure
    `T30` quoted for npm came from `surface_bound.py`, which reads builds. The two
    are not commensurable and this test records that they are different questions."""
    assert "dist" in sg.SKIP_DIRS
    assert "build" in sg.SKIP_DIRS


def test_gating_still_detected():
    """`T28`'s property must survive the rewrite."""
    src = (
        "def register(server):\n"
        "    if os.getenv('ENABLE_INSTITUTIONAL'):\n"
        "        server.tool(annotations=None)(institutional_report)\n"
    )
    sites = _sites(src)
    assert len(sites) == 1, sites
    assert sites[0][1] == "GATED", sites


if __name__ == "__main__":
    fails = 0
    for name, fn in sorted(globals().items()):
        if name.startswith("test_") and callable(fn):
            try:
                fn()
                print("PASS %s" % name)
            except AssertionError as e:
                fails += 1
                print("FAIL %s: %s" % (name, e))
    print("\n%s" % ("ALL PASS" if not fails else "%d FAILED" % fails))
    sys.exit(1 if fails else 0)
