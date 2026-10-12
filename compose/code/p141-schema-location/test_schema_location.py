"""Tests for p141-schema-location.

The first test is the regression that matters: this probe's first draft counted a table
named `is`, out of a COMMENT in `db/postgres.go` that quotes `CREATE TABLE IF NOT EXISTS`
in prose. That inflated every Go-side figure by one. The exact line is pinned verbatim.
"""

import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from schema_location import strip_comments, survey, tables_in  # noqa: E402

# Verbatim from openedx-unrelated subject `ArnaudGuiovanna/tutor-mcp`, db/postgres.go:1710.
COMMENT_LINE = (
    "\t// Serialize migration across the fleet. CREATE TABLE IF NOT EXISTS is not\n"
    "\t// atomic with respect to concurrent writers on every engine.\n"
)


class TestCommentExclusion(unittest.TestCase):
    def test_ddl_quoted_in_a_go_comment_is_not_a_table(self):
        found = self._go(COMMENT_LINE)
        self.assertEqual(found, {}, "a comment quoting DDL must not register a table")

    def test_the_specific_false_positive_name(self):
        self.assertNotIn("is", self._go(COMMENT_LINE))

    def test_block_comment_quoting_ddl(self):
        found = self._go("/* CREATE TABLE ghosts (id TEXT); */\n")
        self.assertEqual(found, {})

    def test_sql_line_comment(self):
        with tempfile.TemporaryDirectory() as d:
            p = os.path.join(d, "x.sql")
            open(p, "w").write("-- CREATE TABLE ghosts (id TEXT);\n")
            self.assertEqual(tables_in([p], is_go=False), {})

    def _go(self, body):
        with tempfile.TemporaryDirectory() as d:
            p = os.path.join(d, "x.go")
            open(p, "w").write(body)
            return tables_in([p], is_go=True)


class TestRawStringsAreKept(unittest.TestCase):
    """The DDL lives inside Go backtick raw strings. Stripping those would zero the probe."""

    def test_table_inside_raw_string_counts(self):
        body = "const s = `\nCREATE TABLE pedagogical_decisions (\n id TEXT PRIMARY KEY\n);\n`\n"
        with tempfile.TemporaryDirectory() as d:
            p = os.path.join(d, "x.go")
            open(p, "w").write(body)
            self.assertIn("pedagogical_decisions", tables_in([p], is_go=True))

    def test_double_slash_inside_a_raw_string_is_not_a_comment(self):
        # A URL in a raw string must not blank the rest of the line.
        body = "const s = `-- see https://x/y\nCREATE TABLE keep_me (id TEXT);\n`\n"
        with tempfile.TemporaryDirectory() as d:
            p = os.path.join(d, "x.go")
            open(p, "w").write(body)
            self.assertIn("keep_me", tables_in([p], is_go=True))

    def test_strip_preserves_length(self):
        src = "a // bbbb\nc\n"
        self.assertEqual(len(strip_comments(src, True)), len(src))


class TestIfNotExistsAndCase(unittest.TestCase):
    def test_if_not_exists_form(self):
        self.assertIn("t1", self._go("const s = `CREATE TABLE IF NOT EXISTS t1 (id TEXT);`"))

    def test_lowercase_ddl(self):
        self.assertIn("t2", self._go("const s = `create table t2 (id text);`"))

    def _go(self, body):
        with tempfile.TemporaryDirectory() as d:
            p = os.path.join(d, "x.go")
            open(p, "w").write(body)
            return tables_in([p], is_go=True)


class TestSurveyShape(unittest.TestCase):
    def test_set_difference_and_empty_tree(self):
        with tempfile.TemporaryDirectory() as root:
            db = os.path.join(root, "db")
            os.makedirs(db)
            open(os.path.join(db, "schema.sql"), "w").write(
                "CREATE TABLE learners (id TEXT, email TEXT UNIQUE NOT NULL);\n"
                "CREATE TABLE shared (id TEXT);\n"
            )
            open(os.path.join(db, "contract.go"), "w").write(
                "const s = `CREATE TABLE pedagogical_decisions (id TEXT);\n"
                "CREATE TABLE shared (id TEXT);`\n"
            )
            # A _test.go file must be excluded from the Go population.
            open(os.path.join(db, "contract_test.go"), "w").write(
                "const s = `CREATE TABLE only_in_tests (id TEXT);`"
            )
            r = survey(root)
            self.assertEqual(r["only_sql"], ["learners"])
            self.assertEqual(r["only_go"], ["pedagogical_decisions"])
            self.assertEqual(r["both"], ["shared"])
            self.assertNotIn("only_in_tests", r["distinct"])

    def test_no_db_dir_is_not_a_crash(self):
        with tempfile.TemporaryDirectory() as root:
            r = survey(root)
            self.assertEqual(r["distinct"], [])


if __name__ == "__main__":
    unittest.main(verbosity=2)
