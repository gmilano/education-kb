#!/usr/bin/env python3
"""Tests for `surface_bound`. Run: python3 -I test_surface_bound.py

Every fixture here is either a verbatim excerpt from one of the eight npm payloads
probed this pass, or a shape an earlier draft of this probe got WRONG in a way that
would have changed the pass's published verdict. They are regression tests against
specific mistakes, not coverage decoration.
"""
import sys
import tempfile
import textwrap
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import surface_bound as sb  # noqa: E402


class Payload:
    """A throwaway directory holding one or more source files."""

    def __init__(self, **files):
        self._tmp = tempfile.TemporaryDirectory()
        self.path = Path(self._tmp.name)
        for name, body in files.items():
            (self.path / name.replace("__", ".")).write_text(textwrap.dedent(body))

    def __enter__(self):
        return self.path

    def __exit__(self, *exc):
        self._tmp.cleanup()


# --- masking ------------------------------------------------------------------

class TestMask(unittest.TestCase):
    def test_preserves_length_and_newlines(self):
        src = 'const a = "x{y}z"; // {brace}\n/* {more} */\nconst b = 1;\n'
        m = sb.mask(src)
        self.assertEqual(len(m), len(src))
        self.assertEqual(m.count("\n"), src.count("\n"))
        # braces inside a string or comment must never reach the brace analyser
        self.assertNotIn("{", m)
        self.assertNotIn("}", m)

    def test_handles_escaped_quote(self):
        src = r'const s = "a\"b{"; const t = 1;'
        m = sb.mask(src)
        self.assertNotIn("{", m)
        self.assertIn("const t", m)

    def test_template_literal_is_masked(self):
        src = "const q = `select {a} from t`; const u = 2;"
        m = sb.mask(src)
        self.assertNotIn("{", m)
        self.assertIn("const u", m)


# --- the server-name exclusion: the first draft's actual bug -------------------

class TestServerNameExclusion(unittest.TestCase):
    """Verbatim shape from @ink-waffle/moodle-mcp. The server's own name sits within
    the adjacency window of a later `inputSchema` and reads as a tool unless excluded.
    This is precisely why the first draft of this probe reported 17 tools where p139
    reported 16 -- p139's count was right and this probe's was wrong."""

    def test_server_name_is_not_a_tool(self):
        text = """
            const server = new McpServer({ name: 'moodle-mcp', version: '0.2.0' });
            server.registerTool('moodle_courses', { inputSchema: { type: 'object' } });
        """
        tools, excluded = sb.literal_tools([text], package_name="moodle-mcp")
        self.assertEqual(tools, {"moodle_courses"})
        self.assertIn("moodle-mcp", excluded)

    def test_namespaced_server_ctor_is_excluded(self):
        """A compiled build writes `new index_js_1.Server({…})`. A bare `new Server\\(`
        regex misses it and the server name leaks into the tool set."""
        text = """
            const server = new index_js_1.Server({ name: 'canvas-mcp', version: '1.0.0' });
            const tools = [{ name: 'list_users', inputSchema: { type: 'object' } }];
        """
        tools, excluded = sb.literal_tools([text], package_name="canvas-mcp")
        self.assertEqual(tools, {"list_users"})
        self.assertIn("canvas-mcp", excluded)

    def test_namespaced_server_instance_is_counted(self):
        masked = sb.mask(
            "const s = new index_js_1.Server({}); const h = new mcp_js_1.McpServer({});"
        )
        self.assertEqual(len(sb.SERVER_INSTANCE.findall(masked)), 2)


# --- dynamic registration: the shape p139's static count could not see ---------

class TestDynamicRegistration(unittest.TestCase):
    def test_detected_and_collection_resolved(self):
        """Verbatim shape from @owen-x-tech/canvas-mcp build/index.js:1363. A probe
        counting name literals finds ONE registration here; the live server serves 62."""
        text = """
            const tools = [{ name: 'a', inputSchema: {} }];
            for (const tool of tools) {
                httpMcp.registerTool(tool.name, { description: tool.description });
            }
        """
        masked = sb.mask(text)
        hits = list(sb.DYNAMIC_REG.finditer(masked))
        self.assertEqual(len(hits), 1)
        self.assertEqual(sb.resolve_collection(masked, hits[0].start()), "tools")

    def test_literal_registration_is_not_dynamic(self):
        masked = sb.mask("server.registerTool('moodle_courses', { inputSchema: {} });")
        self.assertEqual(list(sb.DYNAMIC_REG.finditer(masked)), [])

    def test_forEach_collection_resolves(self):
        text = "TOOL_DEFS.forEach((t) => { server.registerTool(t.name, t.schema); });"
        masked = sb.mask(text)
        hits = list(sb.DYNAMIC_REG.finditer(masked))
        self.assertEqual(len(hits), 1)
        self.assertEqual(sb.resolve_collection(masked, hits[0].start()), "TOOL_DEFS")

    def test_runtime_collection_is_unbounded(self):
        """The one case where no static method answers the question and only
        execution does -- which is the case that would have vindicated `ACTION CP`."""
        with Payload(index__js="""
            const server = new McpServer({ name: 'srv' });
            const remote = await fetch(url).then(r => r.json());
            for (const tool of remote) {
                server.registerTool(tool.name, { inputSchema: tool.schema });
            }
        """) as p:
            r = sb.measure(p, package_name="srv")
        self.assertEqual(r["dynamic_sites"], 1)
        self.assertEqual(r["collection_class"]["remote"], "RUNTIME_OR_UNRESOLVED")
        self.assertEqual(r["verdict"], "UNBOUNDED")

    def test_static_collection_is_bounded_dynamic(self):
        with Payload(index__js="""
            const server = new McpServer({ name: 'srv' });
            const tools = [{ name: 'a', inputSchema: {} }, { name: 'b', inputSchema: {} }];
            for (const tool of tools) {
                server.registerTool(tool.name, { inputSchema: tool.inputSchema });
            }
        """) as p:
            r = sb.measure(p, package_name="srv")
        self.assertEqual(r["collection_class"]["tools"], "STATIC_IN_BUILD")
        self.assertEqual(r["verdict"], "BOUNDED_DYNAMIC")


# --- the installer-sibling correction ------------------------------------------

class TestGateClassification(unittest.TestCase):
    def test_else_with_exiting_sibling_is_not_a_gate(self):
        """@owen-x-tech/canvas-mcp wraps its ENTIRE server in
        `if (--setup) { … process.exit(0); } else { <server> }`. Scoring that as
        conditional would have published a false capability gate on all 62 of its
        tools -- a wrong finding, not merely a noisy one."""
        text = """
            if (process.argv.includes('--setup')) {
                writeConfig();
                process.exit(0);
            }
            else {
                server.registerTool('list_users', { inputSchema: {} });
            }
        """
        masked = sb.mask(text)
        off = sb.DIRECT.search(text).start()
        verdict, reason = sb.classify_gate(masked, off)
        self.assertEqual(verdict, "ungated", reason)

    def test_else_without_exiting_sibling_is_a_gate(self):
        text = """
            if (readOnly) {
                setup();
            }
            else {
                server.registerTool('delete_course', { inputSchema: {} });
            }
        """
        masked = sb.mask(text)
        off = sb.DIRECT.search(text).start()
        verdict, _ = sb.classify_gate(masked, off)
        self.assertEqual(verdict, "gated")

    def test_env_flag_if_is_a_gate(self):
        """The shape that WOULD make a static count an over-estimate: a write tool
        registered only when an environment flag is set."""
        text = """
            if (process.env.ENABLE_WRITES === '1') {
                server.registerTool('bulk_update_grades', { inputSchema: {} });
            }
        """
        masked = sb.mask(text)
        off = sb.DIRECT.search(text).start()
        verdict, _ = sb.classify_gate(masked, off)
        self.assertEqual(verdict, "gated")

    def test_iteration_is_not_scored_as_a_gate(self):
        """An iteration is dynamic registration and is counted on that axis. Scoring
        it as a gate as well would double-penalise one construct."""
        text = """
            for (const tool of tools) {
                server.registerTool('fixed_name', { inputSchema: {} });
            }
        """
        masked = sb.mask(text)
        off = sb.DIRECT.search(text).start()
        verdict, _ = sb.classify_gate(masked, off)
        self.assertEqual(verdict, "ungated")

    def test_brace_in_a_string_does_not_break_the_stack(self):
        """Without masking, the `{` inside the description string unbalances the brace
        stack and every later site is misclassified."""
        text = """
            const d = "a { b";
            server.registerTool('get_courses', { inputSchema: {} });
        """
        masked = sb.mask(text)
        off = sb.DIRECT.search(text).start()
        verdict, _ = sb.classify_gate(masked, off)
        self.assertEqual(verdict, "ungated")


# --- whole-payload verdicts ----------------------------------------------------

class TestVerdicts(unittest.TestCase):
    def test_single_server_all_literal_is_bounded_static(self):
        with Payload(index__js="""
            const server = new McpServer({ name: 'srv' });
            server.registerTool('get_courses', { inputSchema: {} });
            server.registerTool('get_grades', { inputSchema: {} });
            const t = new StdioServerTransport();
        """) as p:
            r = sb.measure(p, package_name="srv")
        self.assertEqual(r["literal_tools"], 2)
        self.assertEqual(r["server_instances"], 1)
        self.assertEqual(r["verdict"], "BOUNDED_STATIC")
        self.assertEqual(r["transports"], "StdioServerTransport")

    def test_two_server_instances_are_multi_surface(self):
        """Two server instances mean the live list is per-transport, so "the package's
        tool count" is not a well-formed quantity. Verbatim shape from
        @owen-x-tech/canvas-mcp."""
        with Payload(index__js="""
            const server = new index_js_1.Server({ name: 'srv' });
            server.registerTool('a', { inputSchema: {} });
            function createHttpServer() {
                const httpMcp = new mcp_js_1.McpServer({ name: 'srv' });
                httpMcp.registerTool('dashboard', { inputSchema: {} });
                return httpMcp;
            }
            const x = new StdioServerTransport();
            const y = new StreamableHTTPServerTransport();
        """) as p:
            r = sb.measure(p, package_name="srv")
        self.assertEqual(r["server_instances"], 2)
        self.assertEqual(r["verdict"], "MULTI_SURFACE")
        self.assertIn("StreamableHTTPServerTransport", r["transports"])

    def test_one_server_on_two_transports_is_not_multi_surface(self):
        """The distinction that carries the finding: two TRANSPORTS sharing ONE server
        instance expose the same tool list. @ink-waffle/moodle-mcp is this shape and
        must not be reported alongside @owen-x-tech/canvas-mcp."""
        with Payload(index__js="""
            const server = new McpServer({ name: 'srv' });
            server.registerTool('a', { inputSchema: {} });
            const x = new StdioServerTransport();
            const y = new StreamableHTTPServerTransport();
        """) as p:
            r = sb.measure(p, package_name="srv")
        self.assertEqual(r["server_instances"], 1)
        self.assertEqual(r["verdict"], "BOUNDED_STATIC")
        self.assertIn("StdioServerTransport", r["transports"])
        self.assertIn("StreamableHTTPServerTransport", r["transports"])

    def test_empty_payload_reports_zero_not_crash(self):
        with Payload(readme__txt="no code here") as p:
            r = sb.measure(p, package_name="x")
        self.assertEqual(r["literal_tools"], 0)
        self.assertEqual(r["dynamic_sites"], 0)
        self.assertEqual(r["server_instances"], 0)

    def test_typescript_only_payload_is_read(self):
        """A payload shipping no built JS falls back to its TypeScript sources, as
        p139's `iter_source` does -- otherwise such a row reads as zero tools."""
        with Payload(index__ts="""
            const server = new McpServer({ name: 'srv' });
            server.registerTool('get_courses', { inputSchema: {} });
        """) as p:
            r = sb.measure(p, package_name="srv")
        self.assertEqual(r["literal_tools"], 1)

    def test_built_js_wins_over_typescript_source(self):
        """When both ship, the BUILD is what runs. Counting both would double-count."""
        with Payload(
            index__js="const s = new McpServer({ name: 'srv' });\n"
                      "s.registerTool('from_build', { inputSchema: {} });\n",
            index__ts="const s = new McpServer({ name: 'srv' });\n"
                      "s.registerTool('from_source', { inputSchema: {} });\n",
        ) as p:
            r = sb.measure(p, package_name="srv")
        self.assertEqual(r["tool_names"], ["from_build"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
