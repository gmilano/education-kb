"""Offline tests for `ACTION KF`'s dated-evidence gate.

No network, no clone, no clock dependence. Run with:
    python3 -I test_dated_write.py

The suite is built around the distinction the gate exists to make — a WRITE to a
dated path versus a MENTION of one — because a gate that cannot tell them apart
would flag every honest instrument in this repository, and `T262` taught that a
control which only ever runs against offenders cannot show it catches anything.
"""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from dated_write import offenders  # noqa: E402

FIXTURES = HERE / "fixtures"


def rows_for(name: str):
    return [row for row in offenders(FIXTURES, exclude_self=False) if row[0] == name]


class PositiveControls(unittest.TestCase):
    """The gate must CATCH, not merely pass."""

    def test_shell_redirection_to_a_dated_path_is_caught(self):
        rows = rows_for("offender_shell.sh")
        self.assertEqual(len(rows), 1, rows)
        self.assertEqual(rows[0][1], "verdict.2026-10-11.tsv")
        self.assertEqual(rows[0][2], "hardcoded")

    def test_variable_bound_to_a_dated_literal_then_written_is_caught(self):
        names = {row[1] for row in rows_for("offender_python.py")}
        self.assertIn("score.2026-10-11.tsv", names)

    def test_open_for_write_on_a_bound_dated_path_is_caught(self):
        names = {row[1] for row in rows_for("offender_python.py")}
        self.assertIn("phantom-claims.2026-10-11.tsv", names)

    def test_every_positive_control_is_classified_hardcoded(self):
        rows = rows_for("offender_shell.sh") + rows_for("offender_python.py")
        self.assertTrue(rows)
        self.assertEqual({row[2] for row in rows}, {"hardcoded"})


class NegativeControls(unittest.TestCase):
    """The gate must stay SILENT on correct behaviour."""

    def test_a_clock_derived_dated_write_is_out_of_scope_entirely(self):
        # `result.$STAMP.tsv` carries no literal date, so by construction it
        # cannot be an offender and the gate never sees the path at all. This
        # is the rule's boundary, asserted rather than assumed.
        self.assertEqual(rows_for("clean_clock.sh"), [])

    def test_a_literal_date_in_a_script_that_also_calls_the_clock_is_clock(self):
        rows = rows_for("mixed_clock_and_literal.py")
        self.assertEqual(len(rows), 1, rows)
        self.assertEqual(rows[0][1], "census-items.2026-10-05.tsv")
        self.assertEqual(rows[0][2], "clock")

    def test_a_fabricated_mention_only_file_is_silent(self):
        # Three mentions, one READ, and one write to an UNDATED path.
        self.assertEqual(rows_for("clean_mention.py"), [])

    def test_a_write_to_an_undated_path_is_out_of_scope(self):
        names = {row[1] for row in offenders(FIXTURES, exclude_self=False)}
        self.assertNotIn("summary.tsv", names)


class RuleShape(unittest.TestCase):
    """Properties of the rule itself, so it can be argued with."""

    def test_only_py_and_sh_are_examined(self):
        (FIXTURES / "decoy.txt").write_text("> result.2026-10-11.tsv\n", encoding="utf-8")
        try:
            self.assertEqual(rows_for("decoy.txt"), [])
        finally:
            (FIXTURES / "decoy.txt").unlink()

    def test_a_directory_with_no_scripts_yields_nothing(self):
        empty = HERE / "fixtures" / "_empty"
        empty.mkdir(exist_ok=True)
        try:
            self.assertEqual(offenders(empty), [])
        finally:
            empty.rmdir()

    def test_classification_is_one_of_two_values(self):
        self.assertTrue({row[2] for row in offenders(FIXTURES, exclude_self=False)} <= {"hardcoded", "clock"})

    def test_rows_are_stable_across_two_runs(self):
        self.assertEqual(offenders(FIXTURES, exclude_self=False), offenders(FIXTURES, exclude_self=False))

    def test_this_gates_own_positive_controls_are_excluded_from_a_repo_sweep(self):
        # Without this, every figure the gate publishes about the repository
        # would include the deliberate offenders written to test it.
        self.assertEqual(offenders(FIXTURES), [])
        self.assertNotEqual(offenders(FIXTURES, exclude_self=False), [])


if __name__ == "__main__":
    unittest.main(verbosity=2)
