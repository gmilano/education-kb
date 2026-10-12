"""Tests for p142-schema-location-tiers.

The first test is p141's regression, carried forward verbatim: a probe that generalises an
instrument must keep the instrument's own fixtures, or the generalisation silently reopens
the bug it inherited.
"""
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import schema_tiers as S  # noqa: E402


def names(text, lang):
    return [m.group(1) for m in S.CREATE_TABLE.finditer(S.strip_comments(text, lang))]


class P141Regression(unittest.TestCase):
    def test_a_go_comment_quoting_ddl_is_not_ddl(self):
        """🔴 p141's own defect, pinned verbatim. This line produced a table named `is`
        and inflated every Go-side figure by one."""
        line = ("// Serialize migration across the fleet. CREATE TABLE IF NOT EXISTS "
                "is not\n")
        self.assertEqual(names(line, "go"), [])

    def test_go_backtick_raw_strings_are_kept(self):
        src = "const m = `CREATE TABLE pedagogical_decisions (id TEXT PRIMARY KEY);`\n"
        self.assertEqual(names(src, "go"), ["pedagogical_decisions"])


class PerLanguageStripping(unittest.TestCase):
    def test_python_hash_comment_is_stripped(self):
        self.assertEqual(names("# CREATE TABLE learners (id TEXT)\n", "py"), [])

    def test_python_triple_quoted_ddl_is_kept(self):
        src = 'DDL = """\nCREATE TABLE learners (id TEXT);\n"""\n'
        self.assertEqual(names(src, "py"), ["learners"])

    def test_a_docstring_that_describes_a_table_is_not_ddl(self):
        """🔵 Triple quotes hold both DDL and docstrings. Prose ABOUT a table does not
        contain the keyword pair, so it cannot match; DDL inside a docstring does."""
        src = '"""Creates the table learners if it is absent, then returns it."""\n'
        self.assertEqual(names(src, "py"), [])

    def test_ts_line_comment_stripped_and_template_literal_kept(self):
        self.assertEqual(names("// CREATE TABLE x (a int)\n", "ts"), [])
        self.assertEqual(names("await db.exec(`CREATE TABLE x (a int)`)\n", "ts"), ["x"])

    def test_sql_dash_comment_is_stripped(self):
        self.assertEqual(names("-- CREATE TABLE y (a int)\n", "sql"), [])

    def test_block_comments_stripped_outside_python(self):
        self.assertEqual(names("/* CREATE TABLE z (a int) */\n", "ts"), [])

    def test_quoted_and_bracketed_identifiers(self):
        for src, want in ((' CREATE TABLE "learners" (a int)', "learners"),
                          (" CREATE TABLE `learners` (a int)", "learners"),
                          (" CREATE TABLE [learners] (a int)", "learners")):
            self.assertEqual(names(src, "sql"), [want], src)


class PopulationIsTheTreeNotADirectory(unittest.TestCase):
    def test_vendored_and_generated_trees_are_excluded(self):
        for p in ("node_modules/x/db.sql", "vendor/y/schema.go", "dist/app.js",
                  "__pycache__/a.py", ".venv/lib/x.py"):
            self.assertTrue(any(e in "/" + p for e in S.EXCLUDE), p)

    def test_test_files_are_excluded_as_p141_did(self):
        for p in ("db/postgres_test.go", "tests/test_x.py", "src/a.test.ts",
                  "src/__tests__/b.js"):
            self.assertTrue(S.is_test(p), p)

    def test_production_sources_are_not_excluded(self):
        for p in ("db/postgres.go", "src/models.py", "src/server.ts"):
            self.assertFalse(S.is_test(p), p)
            self.assertFalse(any(e in "/" + p for e in S.EXCLUDE), p)

    def test_an_orm_project_yields_no_create_table(self):
        """🔴 The `ACTION DD` finding, pinned. A SQLAlchemy model declares a table and
        contains no DDL, so a `CREATE TABLE` census returns zero on a real schema."""
        src = ('class Learner(Base):\n'
               '    __tablename__ = "learners"\n'
               '    id = Column(String, primary_key=True)\n')
        self.assertEqual(names(src, "py"), [])


if __name__ == "__main__":
    unittest.main(verbosity=2)
