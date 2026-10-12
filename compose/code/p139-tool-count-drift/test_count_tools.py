#!/usr/bin/env python3
"""Tests for `count_tools`. Run: python3 -I test_count_tools.py

Every fixture is a verbatim excerpt from one of the nine npm payloads probed this pass,
or from the two rows the first draft of the probe got wrong.
"""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import count_tools as ct  # noqa: E402

# --- verbatim fixtures ----------------------------------------------------------

# @ink-waffle/moodle-mcp, dist/ — idiom 1
DIRECT_SRC = """
    server.registerTool("moodle_connect", {
    server.registerTool("moodle_status", {
    server.registerTool("moodle_disconnect", {
    server.registerTool("moodle_courses", {
"""

# @imazhar101/mcp-canvas-server, dist/servers/canvas/src/tools/assignment-tools.js — idiom 2
ADJACENT_SRC = """
export class AssignmentTools {
    getToolDefinitions() {
        return [
            {
                name: 'list_assignments',
                description: 'List assignments for a course',
                inputSchema: {
                    type: 'object',
                    properties: { course_id: { type: 'string' } },
                },
            },
        ];
    }
}
"""

# @imazhar101/mcp-canvas-server — the environment entries the first draft counted as tools
ENV_ENTRIES_SRC = """
    const envs = [
        { name: 'beta', suffix: '_BETA' },
        { name: 'prod', suffix: '_PROD' },
    ];
"""

# moodle-mcp-server-aql, dist/tools/list-courses.js — idiom 3
MODULE_SRC = """
import { z } from "zod";
export const name = "list_courses";
export const description = "List LMS courses available to the configured API token. " +
    "Returns course ID, full name, short name, category, category path, and visibility.";
export const inputSchema = z.object({ categoryId: z.number().optional() });
"""

# mcp-canvas-lms, dist/index.js — the server's own identity, two lines from a tool
SERVER_CTOR_SRC = """
const server = new Server({ name: "canvas-mcp-server", version: "1.0.5" }, {});
server.setRequestHandler(ListToolsRequestSchema, async () => ({
  tools: [
    { name: "get_courses", description: "List courses", inputSchema: { type: "object" } },
  ],
}));
"""


class TestDirectIdiom(unittest.TestCase):
    def test_register_tool_calls_are_counted(self):
        got = ct.DIRECT.findall(DIRECT_SRC)
        self.assertEqual(sorted(got), [
            "moodle_connect", "moodle_courses", "moodle_disconnect", "moodle_status"])

    def test_direct_needs_no_schema_marker(self):
        # A registerTool call is self-evidently a registration; adjacency is not required.
        self.assertEqual(ct.adjacent_tools(DIRECT_SRC), set())


class TestAdjacentIdiom(unittest.TestCase):
    def test_name_with_input_schema_is_a_tool(self):
        self.assertEqual(ct.adjacent_tools(ADJACENT_SRC), {"list_assignments"})

    def test_env_entries_are_not_tools(self):
        """The regression that rewrote this instrument.

        `{ name: 'beta', suffix: '_BETA' }` was published as a tool of
        @imazhar101/mcp-canvas-server by the first draft. It carries no inputSchema.
        """
        self.assertEqual(ct.adjacent_tools(ENV_ENTRIES_SRC), set())

    def test_window_is_bounded(self):
        far = "{ name: 'x_tool', " + ("pad," * 500) + " inputSchema: {} }"
        self.assertEqual(ct.adjacent_tools(far), set())
        near = "{ name: 'x_tool', description: 'd', inputSchema: {} }"
        self.assertEqual(ct.adjacent_tools(near), {"x_tool"})


class TestModuleIdiom(unittest.TestCase):
    def test_module_exporting_name_and_schema_is_a_tool(self):
        """moodle-mcp-server-aql: 0 tools over 34 files on the first draft."""
        self.assertEqual(ct.module_tools(MODULE_SRC), {"list_courses"})

    def test_module_without_schema_is_not_a_tool(self):
        self.assertEqual(ct.module_tools('export const name = "not_a_tool";'), set())

    def test_colon_form_is_not_double_counted_as_module(self):
        self.assertEqual(ct.module_tools(ADJACENT_SRC), set())


class TestServerNameExclusion(unittest.TestCase):
    def test_server_identity_is_not_a_tool(self):
        names = ct.server_names([SERVER_CTOR_SRC])
        self.assertIn("canvas-mcp-server", names)

    def test_adjacency_alone_cannot_tell_them_apart(self):
        """Why the exclusion is load-bearing rather than belt-and-braces.

        `name: "canvas-mcp-server"` sits within the adjacency window of the tool array's
        `inputSchema`, so the adjacency rule returns the SERVER's identity too. Only the
        constructor-derived exclusion in `build_tools` removes it.
        """
        self.assertEqual(ct.adjacent_tools(SERVER_CTOR_SRC),
                         {"get_courses", "canvas-mcp-server"})

    def test_build_tools_excludes_the_server_name(self):
        import tempfile
        with tempfile.TemporaryDirectory() as d:
            (Path(d) / "index.js").write_text(SERVER_CTOR_SRC)
            (Path(d) / "package.json").write_text('{"name": "mcp-canvas-lms"}')
            b = ct.build_tools(d, ct.manifest_name(d))
            self.assertEqual(b["tools"], {"get_courses"})
            self.assertIn("canvas-mcp-server", b["excluded_server_names"])
            self.assertTrue(b["serves_tools"])


class TestReadmeExtraction(unittest.TestCase):
    def test_backticked_snake_case_is_a_claim(self):
        import tempfile
        with tempfile.TemporaryDirectory() as d:
            (Path(d) / "README.md").write_text(
                "## Tools\n- `get_courses` — list\n- `submit_journal` — write\n"
                "Install with `npm` and run `node dist/index.js`.\n")
            got, fname = ct.readme_tools(d)
            self.assertEqual(fname, "README.md")
            self.assertIn("get_courses", got)
            self.assertIn("submit_journal", got)
            # `npm` and `node` are backticked in every README and are not tools; they
            # survive extraction but are filtered from `phantom` by the underscore rule.
            self.assertIn("npm", got)
            self.assertNotIn("npm", {t for t in got if "_" in t})


if __name__ == "__main__":
    unittest.main(verbosity=2)
