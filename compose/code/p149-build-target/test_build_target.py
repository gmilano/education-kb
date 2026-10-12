"""21 tests for `p149-build-target`. Authored fixtures, offline, no network."""

import json
import os
import shutil
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_target as bt  # noqa: E402


def write(root, rel, text):
    path = os.path.join(root, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)


class Base(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def root(self, name):
        p = os.path.join(self.tmp, name)
        os.makedirs(p, exist_ok=True)
        return p


class DeclaredTargetsTest(Base):
    def test_wheel_packages_is_one_target(self):
        r = self.root("a")
        write(r, "pyproject.toml",
              '[tool.hatch.build.targets.wheel]\npackages = ["src/pkg"]\n')
        got = bt.declared_targets(r)
        self.assertEqual(len(got), 1)
        self.assertEqual(got[0][2], "wheel")

    def test_sdist_include_is_found(self):
        # 🔴 The key p148's shape table omitted -- `soongpt-plugin`'s second target.
        r = self.root("b")
        write(r, "pyproject.toml",
              '[tool.hatch.build.targets.sdist]\ninclude = ["src/pkg", "skills"]\n')
        got = bt.declared_targets(r)
        self.assertEqual(len(got), 1)
        self.assertEqual(got[0][1], "include")
        self.assertEqual(got[0][2], "sdist")

    def test_sdist_only_include_is_found(self):
        r = self.root("c")
        write(r, "pyproject.toml",
              '[tool.hatch.build.targets.sdist]\nonly-include = ["src/pkg"]\n')
        self.assertEqual(bt.declared_targets(r)[0][1], "only-include")

    def test_wheel_and_sdist_in_one_file_are_TWO_targets(self):
        # 🟢 `T68`'s shape. p148's `measure()` returned the first and stopped.
        r = self.root("d")
        write(r, "pyproject.toml",
              '[tool.hatch.build.targets.wheel]\npackages = ["src/pkg"]\n\n'
              '[tool.hatch.build.targets.sdist]\ninclude = ["src/pkg", "tests"]\n')
        got = bt.declared_targets(r)
        self.assertEqual(len(got), 2)
        self.assertEqual({g[2] for g in got}, {"wheel", "sdist"})

    def test_npm_files_is_a_single_tarball_target(self):
        r = self.root("e")
        write(r, "package.json", json.dumps({"name": "x", "files": ["dist", "README.md"]}))
        got = bt.declared_targets(r)
        self.assertEqual(len(got), 1)
        self.assertEqual(got[0][2], "npm-tarball(single)")

    def test_an_empty_npm_files_array_is_not_a_target(self):
        r = self.root("f")
        write(r, "package.json", json.dumps({"name": "x", "files": []}))
        self.assertEqual(bt.declared_targets(r), [])

    def test_a_manifest_with_no_allowlist_declares_no_target(self):
        r = self.root("g")
        write(r, "pyproject.toml", '[project]\nname = "x"\n')
        self.assertEqual(bt.declared_targets(r), [])

    def test_no_manifest_declares_no_target(self):
        self.assertEqual(bt.declared_targets(self.root("h")), [])

    def test_setuptools_packages_is_one_target_for_both_artefacts(self):
        r = self.root("i")
        write(r, "pyproject.toml", '[tool.setuptools]\npackages = ["pkg"]\n')
        self.assertEqual(bt.declared_targets(r)[0][2], "wheel+sdist")

    def test_poetry_array_of_inline_tables_is_read(self):
        r = self.root("j")
        write(r, "pyproject.toml",
              '[tool.poetry]\npackages = [{include = "pkg"}]\n')
        got = bt.declared_targets(r)
        self.assertEqual(got[0][3], ["pkg"])

    def test_a_malformed_package_json_does_not_raise(self):
        r = self.root("k")
        write(r, "package.json", "{not json")
        self.assertEqual(bt.declared_targets(r), [])


class ScopeTest(Base):
    def test_a_directory_item_pulls_in_its_whole_tree(self):
        r = self.root("l")
        write(r, "src/pkg/a.py", "x = 1\n")
        write(r, "src/pkg/sub/b.py", "y = 2\n")
        self.assertEqual(bt.files_in_scope(r, ["src/pkg"]),
                         ["src/pkg/a.py", "src/pkg/sub/b.py"])

    def test_a_file_item_pulls_in_only_that_file(self):
        r = self.root("m")
        write(r, "README.md", "# x\n")
        write(r, "other.md", "# y\n")
        self.assertEqual(bt.files_in_scope(r, ["README.md"]), ["README.md"])

    def test_a_missing_item_contributes_nothing_and_does_not_raise(self):
        self.assertEqual(bt.files_in_scope(self.root("n"), ["nope"]), [])

    def test_pycache_is_excluded_from_scope(self):
        r = self.root("o")
        write(r, "src/pkg/a.py", "x = 1\n")
        write(r, "src/pkg/__pycache__/a.cpython-311.pyc", "junk")
        self.assertEqual(bt.files_in_scope(r, ["src/pkg"]), ["src/pkg/a.py"])


class SiteCountTest(Base):
    def test_a_decorator_site_is_counted_ONCE(self):
        # 🔴 The bug this module shipped and fixed: `@mcp.tool(` matched both patterns and
        # was counted twice, which read 43 where p148 published 39.
        r = self.root("p")
        write(r, "s.py", "@mcp.tool()\ndef a():\n    pass\n")
        self.assertEqual(bt.count_sites(r, ["s.py"]), 1)

    def test_a_server_tool_call_is_counted_once(self):
        r = self.root("q")
        write(r, "s.py", 'server.tool("a", handler)\n')
        self.assertEqual(bt.count_sites(r, ["s.py"]), 1)

    def test_three_mixed_forms_count_three(self):
        r = self.root("r")
        write(r, "s.py", "@mcp.tool()\ndef a():\n    pass\n\n"
                         'server.tool("b", h)\n@tool()\ndef c():\n    pass\n')
        self.assertEqual(bt.count_sites(r, ["s.py"]), 3)

    def test_a_file_type_with_no_pattern_contributes_nothing(self):
        r = self.root("s")
        write(r, "notes.md", "server.tool( in prose\n")
        self.assertEqual(bt.count_sites(r, ["notes.md"]), 0)

    def test_js_registerTool_is_counted(self):
        r = self.root("t")
        write(r, "i.js", "server.registerTool('a', h);\nserver.tool('b', h);\n")
        self.assertEqual(bt.count_sites(r, ["i.js"]), 2)


class MeasureTest(Base):
    def test_two_targets_that_differ_in_scope_report_different_counts(self):
        r = self.root("u")
        write(r, "pyproject.toml",
              '[tool.hatch.build.targets.wheel]\npackages = ["src/pkg"]\n\n'
              '[tool.hatch.build.targets.sdist]\nonly-include = ["src/pkg", "tests"]\n')
        write(r, "src/pkg/s.py", 'server.tool("a", h)\n')
        write(r, "tests/t.py", 'server.tool("b", h)\n')
        rows = bt.measure(r, "u")
        self.assertEqual(len(rows), 2)
        by_kind = {x["kind"]: x["tool_sites"] for x in rows}
        self.assertEqual(by_kind["wheel"], 1)
        self.assertEqual(by_kind["sdist"], 2)

    def test_a_subject_with_no_target_yields_one_NO_TARGET_row(self):
        rows = bt.measure(self.root("v"), "v")
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["kind"], "NO_TARGET")


if __name__ == "__main__":
    unittest.main(verbosity=2)
