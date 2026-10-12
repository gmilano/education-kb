"""Tests for p141-agent-surface-gate.

The first class is the regression that forced this probe to be rewritten: a 25-line lookback
window reported `mohaneesh-03/mcp-tutor` as GATED off `if CONFIG.auto_open_browser:` sitting
in the body of an earlier tool function, 64 lines above the registration it was blamed for.
Proximity is not enclosure.
"""

import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from surface_gate import gated_braced, gated_python  # noqa: E402


class TestProximityIsNotEnclosure(unittest.TestCase):
    def test_flag_conditional_in_an_earlier_function_body_does_not_gate(self):
        lines = [
            "@mcp.tool()",
            "async def open_dashboard() -> str:",
            "    if CONFIG.auto_open_browser:",
            "        webbrowser.open(url)",
            "    return 'ok'",
            "",
            "@mcp.tool()",                 # index 6 — indentation 0
            "async def log_prose(t): ...",
        ]
        self.assertFalse(gated_python(lines, 6))

    def test_module_top_level_can_never_be_gated(self):
        lines = ["if settings.enabled:", "    pass", "@mcp.tool()"]
        self.assertFalse(gated_python(lines, 2))


class TestRealPythonEnclosure(unittest.TestCase):
    def test_registration_inside_a_flag_conditional_is_gated(self):
        lines = [
            "def build(mcp):",
            "    if os.getenv('INSTITUTION_TIER'):",
            "        @mcp.tool(name='publish_formation')",
            "        def publish(): ...",
        ]
        self.assertTrue(gated_python(lines, 2))

    def test_a_dispatch_branch_is_not_a_gate(self):
        """`if name == "list_courses":` selects which wrapper to declare; it does not gate."""
        lines = [
            "def _register(mcp, spec):",
            "    if name == 'list_courses':",
            "        @mcp.tool(name=name)",
            "        async def _list(): ...",
        ]
        self.assertFalse(gated_python(lines, 2))

    def test_nested_non_flag_blocks_do_not_gate(self):
        lines = [
            "def build(mcp):",
            "    for spec in TOOL_SPECS:",
            "        @mcp.tool(name=spec.name)",
            "        def _t(): ...",
        ]
        self.assertFalse(gated_python(lines, 2))

    def test_blank_lines_do_not_break_the_outward_walk(self):
        lines = [
            "def build(mcp):",
            "    if settings.institution_tier:",
            "",
            "        @mcp.tool(name='x')",
            "        def x(): ...",
        ]
        self.assertTrue(gated_python(lines, 3))


class TestBracedEnclosure(unittest.TestCase):
    def test_js_registration_inside_env_conditional(self):
        lines = [
            "function build(server) {",
            "  if (process.env.ENABLE_ADMIN) {",
            "    server.registerTool('admin_tool', {}, fn);",
            "  }",
            "}",
        ]
        self.assertTrue(gated_braced(lines, 2, "js"))

    def test_js_plain_function_body_is_not_gated(self):
        lines = [
            "function build(server) {",
            "  for (const tool of TOOLS) {",
            "    server.registerTool(tool.name, {}, fn);",
            "  }",
            "}",
        ]
        self.assertFalse(gated_braced(lines, 2, "js"))

    def test_php_static_return_is_not_gated(self):
        lines = [
            "class Tools {",
            "  public static function list_tools(): array {",
            "    return [ self::schema('tutor_list_courses', '', [], []) ];",
            "  }",
            "}",
        ]
        self.assertFalse(gated_braced(lines, 1, "php"))


class TestKnownLimit(unittest.TestCase):
    """🔴 The documented blind spot, pinned so it cannot be forgotten.

    `tutor-mcp` gates at the CALL SITE of a `register*` helper in `tools/tools.go`, two
    indirections above the `addTool(server, &mcp.Tool{Name: "..."})` that carries the name.
    No lexical-enclosure test at the registration site can see that, so the Go lane fails
    its control and its verdict is withheld rather than published.
    """

    def test_call_site_gating_is_invisible_to_an_enclosure_test(self):
        lines = [
            "func RegisterTools(server *mcp.Server, deps *Deps) {",
            "\tif deps != nil && deps.Institution {",
            "\t\tregisterDraftFormation(server, deps)",   # the gate is HERE
            "\t}",
            "}",
            "func registerDraftFormation(server *mcp.Server, deps *Deps) {",
            "\taddTool(server, &mcp.Tool{Name: \"draft_formation\"})",  # index 6, ungated
        ]
        self.assertFalse(gated_python(lines, 6),
                         "an enclosure test at the name site cannot see call-site gating")


if __name__ == "__main__":
    unittest.main(verbosity=2)
