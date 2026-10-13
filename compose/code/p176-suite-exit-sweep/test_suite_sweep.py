"""Offline suite for `P176-A`. Every fixture is RUN, not simulated, so the suite
tests the classifier against real exit codes and real output.

The suite must show the sweep CATCHES, not merely that it passes:
  - four POSITIVE controls frozen from real shapes in this repository;
  - one control run BOTH WAYS, which is the only way to demonstrate `T271`;
  - one FABRICATED negative that prints every cue and must stay `ok`;
  - one KNOWN LIMIT asserted as a limit, so fixing it changes this file.

Run: python3 test_suite_sweep.py   (plain python3 - see `T271`; `-I` would strip
                                    this directory from sys.path and the import
                                    of `suite_sweep` below would fail, which is
                                    the very defect this instrument reports)
"""

from __future__ import annotations

import pathlib
import unittest

import suite_sweep as S

FIX = pathlib.Path(__file__).resolve().parent / "fixtures"


def verdict(name: str, isolate: bool = True) -> str:
    return S.run_one(FIX / name, timeout=20, isolate=isolate)[4]


def rc(name: str, isolate: bool = True) -> str:
    return S.run_one(FIX / name, timeout=20, isolate=isolate)[3]


class PositiveControls(unittest.TestCase):
    """Shapes frozen from real instruments. Each MUST be caught."""

    def test_shell_refusing_a_missing_argument_is_usage(self):
        self.assertEqual(verdict("wants_argument.sh"), "usage")

    def test_shell_unbound_variable_is_usage_not_crash(self):
        self.assertEqual(verdict("wants_argument_unbound.sh"), "usage")

    def test_prose_tally_below_its_denominator_is_assert(self):
        self.assertEqual(verdict("tally_failure.sh"), "assert")

    def test_tally_class_is_the_only_one_meaning_disagreement(self):
        self.assertIn(verdict("tally_failure.sh"), {"assert"})


class T271BothInvocations(unittest.TestCase):
    """`T271`: a sweep that runs one invocation measures its own argv."""

    def test_sibling_import_crashes_under_isolation(self):
        self.assertEqual(verdict("sibling_import.py", isolate=True), "crash")

    def test_same_script_is_ok_without_isolation(self):
        self.assertEqual(verdict("sibling_import.py", isolate=False), "ok")

    def test_the_two_invocations_disagree_which_is_the_whole_point(self):
        self.assertNotEqual(
            verdict("sibling_import.py", isolate=True),
            verdict("sibling_import.py", isolate=False),
        )


class FabricatedNegative(unittest.TestCase):
    """The control that matters: it prints every cue and exits 0."""

    def test_zero_exit_beats_every_cue(self):
        self.assertEqual(verdict("clean_exit.py"), "ok")

    def test_it_really_does_print_the_cues(self):
        text = (FIX / "clean_exit.py").read_text()
        for cue in ("usage", "FileNotFoundError", "AssertionError",
                    "Could not resolve host", "7/10"):
            self.assertIn(cue, text)


class KnownLimit(unittest.TestCase):
    """Asserted as a limit so that fixing it changes this file."""

    def test_spanish_usage_line_is_not_yet_recognised(self):
        self.assertEqual(verdict("spanish_usage.py"), "other")

    def test_and_it_really_is_a_usage_line(self):
        self.assertIn("uso:", (FIX / "spanish_usage.py").read_text())


class RuleShape(unittest.TestCase):
    def test_exit_code_is_recorded_verbatim(self):
        self.assertEqual(rc("spanish_usage.py"), "2")
        self.assertEqual(rc("tally_failure.sh"), "1")

    def test_timeout_classifies_as_timeout_not_other(self):
        self.assertEqual(S.classify(124, "", ""), "timeout")
        self.assertEqual(S.classify(-9, "", ""), "timeout")

    def test_usage_is_ordered_before_input(self):
        both = "usage: thing\nFileNotFoundError: no such file"
        self.assertEqual(S.classify(2, "", both), "usage")

    def test_test_scripts_are_labelled_by_prefix(self):
        self.assertEqual(
            S.run_one(FIX / "clean_exit.py", timeout=20)[2], "instrument"
        )

    def test_a_tally_at_or_above_its_denominator_is_not_assert(self):
        self.assertEqual(S.classify(1, "10/10 controls passed", ""), "other")


if __name__ == "__main__":
    unittest.main(verbosity=2)
