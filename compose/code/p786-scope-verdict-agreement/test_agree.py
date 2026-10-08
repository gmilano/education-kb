#!/usr/bin/env python3
"""Suite for p786.  Offline: every case is a recorded verdict pair, no network.

The two mandatory cases are the two REAL failures measured in pass 62.  They must come out
with OPPOSITE classes -- if both landed in one bucket this would be a disagreement counter,
not a gate that tells you which direction the error runs.
"""
import os
import subprocess
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from agree import classify, comparable  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))


class TestComparable(unittest.TestCase):
    def test_coarse_prefix_is_not_a_disagreement(self):
        # p441 says BSD, p784 says BSD-3-Clause.  p637's CONTRATO class.
        self.assertTrue(comparable("BSD", "BSD-3-Clause"))
        self.assertTrue(comparable("LGPL?", "LGPL-3.0"))

    def test_different_families_are_a_disagreement(self):
        self.assertFalse(comparable("MIT", "Apache-2.0"))
        self.assertFalse(comparable("CC-BY", "Apache-2.0"))

    def test_gpl_is_not_a_prefix_of_lgpl(self):
        # The trap P753/P773 names: every GNU text names its relatives.
        self.assertFalse(comparable("GPL-3.0", "LGPL-3.0"))


class TestMandatoryRealCases(unittest.TestCase):
    """The two pass-62 failures, and they must not collapse into one class."""

    def test_openbadges_specification_is_a_false_ABSENCE(self):
        # p784: UNGRANTED (0 of 16 root names).
        # p441: found 342 paths, reported CC-BY;CC0-1.0.
        # Truth: ob_v3p0/license.md, 200, 12 324 B, IMS Global SPEC-LICENSE.
        cls, note = classify("UNGRANTED", [], "BUNDLED-GRANT-ONLY", ["CC-BY", "CC0-1.0"])
        self.assertEqual(cls, "DISAGREE-ABSENCE")
        self.assertIn("ROOTED", note)

    def test_openbadgeslib_prose_partition_is_flagged_not_passed(self):
        # p784: SINGLE LGPL-3.0.  p441: OWN-GRANT-AT-ROOT, LGPL?.  They AGREE.
        # Truth: LGPL-3.0 library + BSD-2-Clause CLI, in wiki/ only.
        cls, note = classify("SINGLE", ["LGPL-3.0"], "OWN-GRANT-AT-ROOT", ["LGPL?"])
        self.assertEqual(cls, "NEEDS-PROSE-READ")
        self.assertIn("P786", note)

    def test_the_two_real_cases_land_in_DIFFERENT_classes(self):
        a, _ = classify("UNGRANTED", [], "BUNDLED-GRANT-ONLY", ["CC-BY"])
        b, _ = classify("SINGLE", ["LGPL-3.0"], "OWN-GRANT-AT-ROOT", ["LGPL?"])
        self.assertNotEqual(a, b)


class TestClassify(unittest.TestCase):
    def test_unanimous_permissive_is_still_not_a_pass(self):
        # digitalcredentials/vc: both read BSD.  Agreement is not sufficient (P786).
        cls, _ = classify("SINGLE", ["BSD-3-Clause"], "OWN-GRANT-AT-ROOT", ["BSD"])
        self.assertEqual(cls, "NEEDS-PROSE-READ")

    def test_absence_sustained_by_BOTH_channels(self):
        cls, note = classify("UNGRANTED", [], "ABSENCE-ENUMERATED", [])
        self.assertEqual(cls, "ABSENCE-ENUMERATED")
        self.assertIn("complete tree", note)

    def test_false_PRESENCE_is_reported_even_when_p784_found_something(self):
        # The dangerous direction: p441 adds a family p784 never saw.
        cls, note = classify("SINGLE", ["Apache-2.0"], "BUNDLED-GRANT-ONLY", ["CC-BY"])
        self.assertEqual(cls, "DISAGREE-PRESENCE")
        self.assertIn("documentation", note)

    def test_declared_partition_is_distinguished_from_a_prose_one(self):
        cls, _ = classify("PARTITIONED", ["MIT", "CC-BY-NC-SA-4.0"],
                          "OWN-GRANT-AT-ROOT", ["MIT"])
        self.assertEqual(cls, "PARTITIONED-DECLARED")

    def test_unreachable_propagates(self):
        cls, _ = classify("UNREACHABLE", [], "UNREACHABLE", [])
        self.assertEqual(cls, "UNREACHABLE")

    def test_coarse_vs_fine_does_not_raise_a_false_disagreement(self):
        cls, _ = classify("SINGLE", ["Apache-2.0"], "OWN-GRANT-AT-ROOT", ["Apache-2.0"])
        self.assertEqual(cls, "NEEDS-PROSE-READ")


class TestRefusesEmptyInput(unittest.TestCase):
    """Gap 245 / P541: an instrument that reports success over nothing is the defect."""

    def test_no_arguments_exits_nonzero(self):
        r = subprocess.run([sys.executable, os.path.join(HERE, "agree.py")],
                           capture_output=True, text=True)
        self.assertNotEqual(r.returncode, 0)
        self.assertIn("refusing", r.stderr)

    def test_empty_slugs_file_exits_nonzero(self):
        path = os.path.join(HERE, ".test-empty.tmp")
        open(path, "w").close()
        try:
            r = subprocess.run([sys.executable, os.path.join(HERE, "agree.py"), path],
                               capture_output=True, text=True)
            self.assertNotEqual(r.returncode, 0)
            self.assertIn("no slugs", r.stderr)
        finally:
            os.remove(path)

    def test_missing_file_exits_nonzero(self):
        r = subprocess.run([sys.executable, os.path.join(HERE, "agree.py"),
                            os.path.join(HERE, "no-such-file-zzz")],
                           capture_output=True, text=True)
        self.assertNotEqual(r.returncode, 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
