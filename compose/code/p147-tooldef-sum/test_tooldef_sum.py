"""Tests for p147-tooldef-sum. Authored fixtures only; no module is imported or executed."""
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tooldef_sum as T  # noqa: E402


def arr(src):
    return T._scan_array(src, src.index("["))[0]


class TestScanArray(unittest.TestCase):
    def test_counts_objects_at_depth_one(self):
        self.assertEqual(arr("[{a:1},{b:2},{c:3}]"), 3)

    def test_empty_array_is_zero(self):
        self.assertEqual(arr("[]"), 0)

    def test_nested_object_does_not_add_a_descriptor(self):
        self.assertEqual(arr("[{a:{b:{c:1}}}]"), 1)

    def test_nested_array_of_enums_is_not_a_descriptor(self):
        self.assertEqual(arr("[{enum:['a','b']},{enum:['c']}]"), 2)

    def test_brace_inside_a_string_opens_no_level(self):
        self.assertEqual(arr("""[{d:"a { brace"},{d:'another }'}]"""), 2)

    def test_brace_inside_a_line_comment_opens_no_level(self):
        self.assertEqual(arr("[{a:1}, // a { comment\n{b:2}]"), 2)

    def test_brace_inside_a_block_comment_opens_no_level(self):
        self.assertEqual(arr("[{a:1}, /* a { comment */ {b:2}]"), 2)

    def test_escaped_quote_does_not_end_the_string(self):
        self.assertEqual(arr('[{d:"a \\" {"},{d:"b"}]'), 2)


class TestNameCountIsWrong(unittest.TestCase):
    def test_a_name_property_is_not_a_descriptor(self):
        """🔴 The defect a `grep -c 'name:'` has: `name` is also a Canvas parameter."""
        src = """getToolDefinitions() { return [
            { name: 'create_course', inputSchema: { properties: { name: { type: 'string' } } } }
        ]; }"""
        import tempfile
        with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False) as fh:
            fh.write(src)
            path = fh.name
        try:
            self.assertEqual(T.module_count(path), 1)
            self.assertEqual(src.count("name:"), 2)
        finally:
            os.unlink(path)


class TestHandlerSites(unittest.TestCase):
    def test_spread_calls_are_found_with_line_numbers(self):
        import tempfile
        src = "x\n...ref.aTools.getToolDefinitions(),\n...ref.bTools.getToolDefinitions(),\n"
        with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False) as fh:
            fh.write(src)
            path = fh.name
        try:
            sites = T.handler_sites(path)
            self.assertEqual([s[0] for s in sites], [2, 3])
        finally:
            os.unlink(path)

    def test_a_bare_call_without_a_spread_is_not_a_site(self):
        import tempfile
        with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False) as fh:
            fh.write("const t = ref.aTools.getToolDefinitions();\n")
            path = fh.name
        try:
            self.assertEqual(T.handler_sites(path), [])
        finally:
            os.unlink(path)


if __name__ == "__main__":
    unittest.main(verbosity=2)
