"""Tests for p146-empty-walk-guard.

Two of these are regression pins on `T42` rather than tests of this module: they
reproduce the defect in `p141/surface_gate.py` and `p143/surface_gate2.py` on a fixture
authored here, so the claim "a second instrument carries P145-A's defect" is checked
rather than asserted. The fixtures are written by this test; no external payload is
fetched or executed.
"""
import importlib.util
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
SHELF = HERE.parent

sys.path.insert(0, str(HERE))
from walk_guard import (NO_PAYLOAD_WALKED, WALKED, guard_verdict,  # noqa: E402
                        walked_or_refuse)


def load(rel, name):
    """Import a shelf instrument by path, without needing it to be a package."""
    spec = importlib.util.spec_from_file_location(name, SHELF / rel)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def make_dist_only_server(root):
    """A tree whose ONLY code is under `dist/` — the shape P145-A found on 7 of 8.

    The payload is a real MCP server by every signal the gates look for: an SDK import,
    a server construction and three registered tools.
    """
    d = Path(root) / "dist"
    d.mkdir(parents=True, exist_ok=True)
    (d / "index.js").write_text(
        "const { McpServer } = require('@modelcontextprotocol/sdk/server/mcp.js');\n"
        "const server = new McpServer({ name: 'fixture-mcp', version: '1.0.0' });\n"
        "server.registerTool('list_courses', { inputSchema: {} }, async () => ({}));\n"
        "server.registerTool('get_course', { inputSchema: {} }, async () => ({}));\n"
        "server.registerTool('submit_grade', { inputSchema: {} }, async () => ({}));\n",
        encoding="utf-8")
    (Path(root) / "package.json").write_text(
        '{"name":"fixture-mcp","version":"1.0.0","main":"dist/index.js"}\n',
        encoding="utf-8")
    return root


def make_root_server(root):
    """The same server, with its code at the root — nothing is excluded."""
    Path(root).mkdir(parents=True, exist_ok=True)
    (Path(root) / "index.js").write_text(
        "const { McpServer } = require('@modelcontextprotocol/sdk/server/mcp.js');\n"
        "const server = new McpServer({ name: 'fixture-mcp', version: '1.0.0' });\n"
        "server.registerTool('list_courses', { inputSchema: {} }, async () => ({}));\n",
        encoding="utf-8")
    (Path(root) / "package.json").write_text(
        '{"name":"fixture-mcp","version":"1.0.0","main":"index.js"}\n', encoding="utf-8")
    return root


def make_empty_of_code(root):
    """A tree with files, none of them code the instrument reads."""
    Path(root).mkdir(parents=True, exist_ok=True)
    (Path(root) / "README.md").write_text("# not a server\n", encoding="utf-8")
    return root


class TestGuard(unittest.TestCase):
    def test_nonempty_walk_passes(self):
        self.assertEqual(walked_or_refuse(["a.js", "b.js"])[0], WALKED)

    def test_empty_walk_refuses(self):
        status, detail = walked_or_refuse([], root="/x", excluded={"dist", "build"})
        self.assertEqual(status, NO_PAYLOAD_WALKED)
        self.assertIn("0 files walked", detail)
        self.assertIn("dist", detail)
        self.assertIn("T42", detail)

    def test_detail_counts_files(self):
        self.assertIn("3 file(s)", walked_or_refuse(iter(["a", "b", "c"]))[1])

    def test_generator_is_not_consumed_twice(self):
        self.assertEqual(walked_or_refuse(iter(["a.js"]))[0], WALKED)

    def test_guard_verdict_passes_a_real_verdict_through(self):
        self.assertEqual(guard_verdict("BOUNDED_STATIC", ["a.js"])[0], "BOUNDED_STATIC")

    def test_guard_verdict_replaces_a_verdict_over_nothing(self):
        self.assertEqual(guard_verdict("NOT_AN_MCP_SERVER", [])[0], NO_PAYLOAD_WALKED)

    def test_guard_does_not_fire_when_input_was_seen_but_matched_nothing(self):
        """The distinction the module exists to preserve.

        A walk that read a README and found no server is a FINDING. Only a walk that read
        nothing is an instrument failure.
        """
        self.assertEqual(guard_verdict("NOT_AN_MCP_SERVER", ["README.md"])[0],
                         "NOT_AN_MCP_SERVER")


class TestT42RegressionOnShelfInstruments(unittest.TestCase):
    """🔴 Pins the defect in the two instruments `p146-exclusion-reach` calls AT_RISK."""

    @classmethod
    def setUpClass(cls):
        import tempfile
        cls.tmp = tempfile.TemporaryDirectory()
        base = Path(cls.tmp.name)
        cls.dist_only = make_dist_only_server(base / "dist_only")
        cls.at_root = make_root_server(base / "at_root")
        cls.no_code = make_empty_of_code(base / "no_code")

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def test_p141_surface_gate_walks_zero_files_on_a_dist_only_payload(self):
        """🆕 `P146-B`: p141's gate carries `P145-A`'s defect, in an inline literal set."""
        g = load("p141-agent-surface-gate/surface_gate.py", "sg141")
        self.assertEqual(list(g.walk(str(self.dist_only))), [],
                         "p141 walk must yield nothing on a dist-only payload")
        sdk, hits = g.is_mcp_server(str(self.dist_only))
        self.assertFalse(sdk)
        self.assertEqual(hits, 0)

    def test_p141_negative_control_same_server_at_root_is_detected(self):
        """🟢 The control: identical payload, not under `dist/`, reads as a server."""
        g = load("p141-agent-surface-gate/surface_gate.py", "sg141b")
        self.assertTrue(list(g.walk(str(self.at_root))))
        sdk, hits = g.is_mcp_server(str(self.at_root))
        self.assertTrue(sdk, "the same bytes at the root must read as an SDK server")
        self.assertGreater(hits, 0)

    def test_p143_surface_gate2_walks_zero_files_on_a_dist_only_payload(self):
        """🔴 `P145-A`'s own finding, pinned here as a regression."""
        g = load("p143-surface-gate-repair/surface_gate2.py", "sg143")
        self.assertEqual(list(g.walk(str(self.dist_only))), [])

    def test_p145_surface_gate3_readmits_a_declared_built_tree(self):
        """🟢 p145's repair works: `package.json` declares `dist/`, so it is walked."""
        g = load("p145-surface-payload-repair/surface_gate3.py", "sg145")
        admit = g.payload_trees(str(self.dist_only))
        self.assertIn("dist", admit)
        self.assertTrue(list(g.walk(str(self.dist_only), admit=admit)))

    def test_guard_converts_both_false_verdicts_into_a_refusal(self):
        """What the guard buys, stated as the two instruments' own output."""
        for rel, name in (("p141-agent-surface-gate/surface_gate.py", "sgA"),
                          ("p143-surface-gate-repair/surface_gate2.py", "sgB")):
            g = load(rel, name)
            walked = list(g.walk(str(self.dist_only)))
            status, _ = walked_or_refuse(walked, self.dist_only, {"dist", "build"})
            self.assertEqual(status, NO_PAYLOAD_WALKED, rel)


if __name__ == "__main__":
    unittest.main(verbosity=2)
