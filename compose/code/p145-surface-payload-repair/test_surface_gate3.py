"""Tests for `p145-surface-payload-repair`.

Each test pins a defect that was real. The first two pin the defect this probe exists
for -- `SKIP_DIRS` excluding the only tree a package ships -- and the rest pin one
`ListToolsRequestSchema` shape each, all five of which occur on this shelf.
"""

import json
import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import surface_gate3 as g


def tree(spec):
    """Build a temp dir from {relpath: content} and return its path."""
    root = tempfile.mkdtemp()
    for rel, content in spec.items():
        p = os.path.join(root, rel)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, "w", encoding="utf-8") as fh:
            fh.write(content)
    return root


HANDLER = """
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { ListToolsRequestSchema } from "@modelcontextprotocol/sdk/types.js";
%s
"""


class PayloadExclusion(unittest.TestCase):
    """🔴 The defect: 7 of 8 npm rows ship only `dist/`, and `walk` dropped it."""

    def test_dist_admitted_when_it_is_all_the_package_ships(self):
        root = tree({
            "package.json": json.dumps({"name": "x", "main": "dist/index.js"}),
            "dist/index.js": HANDLER % "",
        })
        self.assertEqual(g.payload_trees(root), {"dist"})
        self.assertTrue(list(g.walk(root, admit={"dist"})))

    def test_unpatched_exclusion_would_walk_zero_files(self):
        """Pins the measured defect: the verdict came from an empty file set."""
        root = tree({
            "package.json": json.dumps({"name": "x", "main": "dist/index.js"}),
            "dist/index.js": HANDLER % "",
        })
        self.assertEqual(list(g.walk(root, admit=None)), [])
        sdk, hits = g.is_mcp_server(root, admit=None)
        self.assertFalse(sdk)
        self.assertEqual(hits, 0)          # "0 'mcp' tokens, no SDK import"
        sdk2, _ = g.is_mcp_server(root, admit={"dist"})
        self.assertTrue(sdk2)

    def test_dist_excluded_when_source_sits_beside_it(self):
        """🟢 Forecloses `T37`: a committed `dist/` must not be counted twice."""
        root = tree({
            "package.json": json.dumps({"name": "x", "main": "dist/index.js"}),
            "dist/index.js": HANDLER % "",
            "src/index.js": HANDLER % "",
        })
        self.assertEqual(g.payload_trees(root), set())

    def test_no_package_json_is_source_mode(self):
        root = tree({"src/app.py": "x = 1\n"})
        self.assertEqual(g.payload_trees(root), set())

    def test_bin_only_entry_still_admits(self):
        root = tree({
            "package.json": json.dumps({"name": "x", "bin": {"x": "build/cli.js"}}),
            "build/cli.js": HANDLER % "",
        })
        self.assertEqual(g.payload_trees(root), {"build"})


class ListHandlerShapes(unittest.TestCase):
    """🆕 `ACTION DZ` -- five shapes, each read off a real row on this shelf."""

    def test_inline_descriptors_are_literal(self):
        """`mcp-canvas-lms` shape."""
        src = HANDLER % """
        server.setRequestHandler(ListToolsRequestSchema, async () => ({
          tools: [
            { name: "list_courses", inputSchema: { type: "object" } },
            { name: "get_course",  inputSchema: { type: "object" } }
          ]
        }));
        """
        out = g.scan_js_list_handler(src)
        self.assertEqual([k for _, k, _ in out], ["LITERAL", "LITERAL"])
        self.assertEqual({s for _, _, s in out}, {"JS_LIST_HANDLER"})

    def test_identifier_resolving_to_literal_array_is_literal(self):
        """`canvas-mcp-server` shape -- `tools: TOOLS`, `const TOOLS = [...]`."""
        src = HANDLER % """
        const TOOLS = [
          { name: "a_tool", inputSchema: { type: "object" } },
          { name: "b_tool", inputSchema: { type: "object" } }
        ];
        server.setRequestHandler(ListToolsRequestSchema, async () => ({ tools: TOOLS }));
        """
        out = g.scan_js_list_handler(src)
        self.assertEqual([k for _, k, _ in out], ["LITERAL", "LITERAL"])
        self.assertEqual({s for _, _, s in out}, {"JS_LIST_HANDLER_REF"})

    def test_shorthand_return_resolves(self):
        """`@owen-x-tech/canvas-mcp` shape -- `return { tools }`."""
        src = HANDLER % """
        const tools = [ { name: "list_users", inputSchema: { type: "object" } } ];
        server.setRequestHandler(ListToolsRequestSchema, async () => { return { tools }; });
        """
        out = g.scan_js_list_handler(src)
        self.assertEqual([k for _, k, _ in out], ["LITERAL"])

    def test_pushed_array_is_dynamic(self):
        """🔴 `moodle-mcp-server-aql` shape -- a plugin loop `.push()`es tools in."""
        src = HANDLER % """
        const toolDefinitions = buildCoreToolDefinitions();
        toolDefinitions.push({ name: "plugin_tool", inputSchema: { type: "object" } });
        server.setRequestHandler(ListToolsRequestSchema, async () => {
          return { tools: toolDefinitions };
        });
        """
        out = g.scan_js_list_handler(src)
        self.assertEqual([k for _, k, _ in out], ["DYNAMIC"])
        self.assertEqual([s for _, _, s in out], ["JS_LIST_HANDLER_MUTATED"])

    def test_spread_of_calls_is_dynamic_and_counted(self):
        """🔴 `@imazhar101/mcp-canvas-server` shape -- 18 spread method calls."""
        src = HANDLER % """
        server.setRequestHandler(ListToolsRequestSchema, async () => {
          const tools = [
            ...ref.courseTools.getToolDefinitions(),
            ...ref.userTools.getToolDefinitions()
          ];
          return { tools: injectEnvParam(tools, envNames) };
        });
        """
        out = g.scan_js_list_handler(src)
        self.assertEqual([k for _, k, _ in out], ["DYNAMIC", "DYNAMIC"])
        self.assertEqual({s for _, _, s in out}, {"JS_LIST_HANDLER_SPREAD_CALL"})

    def test_call_wrapped_return_is_dynamic(self):
        """🔴 A surface that is a FUNCTION of the array is not bounded by the array."""
        src = HANDLER % """
        const tools = [ { name: "a_tool", inputSchema: { type: "object" } } ];
        server.setRequestHandler(ListToolsRequestSchema, async () => ({
          tools: injectEnvParam(tools, envNames)
        }));
        """
        out = g.scan_js_list_handler(src)
        self.assertEqual([s for _, _, s in out], ["JS_LIST_HANDLER_WRAPPED"])

    def test_unresolvable_identifier_is_dynamic(self):
        src = HANDLER % """
        server.setRequestHandler(ListToolsRequestSchema, async () => ({ tools: mystery }));
        """
        out = g.scan_js_list_handler(src)
        self.assertEqual([s for _, _, s in out], ["JS_LIST_HANDLER_UNRESOLVED"])

    def test_registertool_path_is_untouched(self):
        """🟢 p143's `JS_LINE` logic must be preserved exactly."""
        root = tree({
            "package.json": json.dumps({"name": "x", "main": "index.js"}),
            "index.js": HANDLER % """
            server.registerTool("alpha_tool", {});
            server.registerTool("beta_tool", {});
            """,
        })
        lit, dyn, gated, _langs, shapes, _sites = g.scan(root)
        self.assertEqual((lit, dyn, gated), (2, 0, 0))
        self.assertEqual(shapes, {"JS_LINE": 2})

    def test_descriptor_without_schema_is_not_a_tool(self):
        """🔴 A bare `name:` is metadata, not a tool -- p140's server-name false positive."""
        src = HANDLER % """
        server.setRequestHandler(ListToolsRequestSchema, async () => ({
          tools: [ { name: "notatool", title: "no schema here" } ]
        }));
        """
        out = g.scan_js_list_handler(src)
        self.assertEqual([k for _, k, _ in out], ["DYNAMIC"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
