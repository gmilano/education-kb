#!/usr/bin/env python3
"""Controls for p445. Run: python3 test_divergence.py   (the NC_TOKEN set is offline)

This instrument's claim is that two classifiers disagree, so its dangerous failure is
a MANUFACTURED disagreement — a plumbing fault that looks like a classifier defect.
Both of this instrument's own first-run defects were exactly that, and both are
controlled here:

  * `"NC" in "UNCLASSIFIED"` is True, which put 11 rows in the NC-ERASED class whose
    shell verdict was `UNCLASSIFIED` — eight of them Finnish national-agency
    repositories. The class meant to say "forbids commercial use" was 73% noise.
  * `commercial_use_ok` signals through its EXIT STATUS, not stdout. Capturing stdout
    returned "" for all 412 rows, MIT included, which read as "commercial use not
    permitted" for the entire shelf. A column constant across every row is not a
    measurement — and this one was constant at the alarming value.
"""
import re
import unittest

import divergence as D


class TestNCToken(unittest.TestCase):
    """NC is a licence-name TOKEN, not a substring."""

    def test_unclassified_does_not_contain_an_NC_licence(self):
        # THE CONTROL THAT CHANGED THE PUBLISHED COUNT: 16 -> 5.
        self.assertFalse(D.NC_TOKEN.search("UNCLASSIFIED"))

    def test_other_words_containing_nc_are_not_nc(self):
        for s in ["UNCLASSIFIED", "NO-CESSION", "Unlicense", "INCOMPLETE",
                  "NONE", "franchise", "Encumbered"]:
            self.assertFalse(D.NC_TOKEN.search(s), s)

    def test_real_nc_families_are_detected(self):
        for s in ["CC-BY-NC-4.0", "CC-BY-NC-SA-4.0", "NC", "cc-by-nc",
                  "NonCommercial", "Non-Commercial", "PolyForm Noncommercial"]:
            self.assertTrue(D.NC_TOKEN.search(s), s)

    def test_commercially_usable_families_are_not_nc(self):
        for s in ["MIT", "Apache-2.0", "EUPL-1.2", "GPL-2.0", "AGPL-3.0",
                  "MPL-2.0", "CC-BY-4.0", "CC-BY-SA-4.0", "BSD-3-Clause", "ISC"]:
            self.assertFalse(D.NC_TOKEN.search(s), s)


class TestShellInvocation(unittest.TestCase):
    """The shell leg must answer, and must answer differently for different inputs."""

    MIT = ('MIT License\n\nCopyright (c) 2026 X\n\nPermission is hereby granted, '
           'free of charge, to any person obtaining a copy of this software and '
           'associated documentation files (the "Software"), to deal in the Software '
           'without restriction.\n')
    NC = ('Attribution-NonCommercial 4.0 International\n\nYou may not use the '
          'material for commercial purposes. NonCommercial means not primarily '
          'intended for or directed towards commercial advantage.\n')

    def test_commercial_flag_is_read_from_the_exit_status(self):
        # If this returns "" for MIT, the stdout-capture defect is back.
        fam, com = D.shell_classify(self.MIT)
        self.assertEqual(com, "YES")
        self.assertEqual(fam, "MIT")

    def test_the_flag_discriminates(self):
        # NEGATIVE CONTROL. Without this, a constant "YES" would pass the test above.
        fam, com = D.shell_classify(self.NC)
        self.assertEqual(com, "NO")

    def test_the_commercial_axis_is_independent_of_the_family_axis(self):
        # P250's design, and the reason the verdict gate uses the FLAG and not the
        # name: this fixture is too thin for the shell to name a family, and the
        # commercial restriction is still detected. 6 of the 11 live restricted rows
        # are exactly this shape (Elastic, PolyForm, and three UNCLASSIFIED).
        fam, com = D.shell_classify(self.NC)
        self.assertEqual((fam, com), ("UNCLASSIFIED", "NO"))

    def test_a_large_payload_is_not_truncated(self):
        # The payload goes on STDIN, not argv: several real ones exceed 35 kB and an
        # argv list has a hard limit. Silent truncation would look like a classifier
        # disagreement rather than a plumbing fault.
        big = self.MIT + ("\n# filler " + "x" * 90) * 500
        self.assertGreater(len(big), 45000)
        self.assertEqual(D.shell_classify(big)[0], "MIT")


class TestVerdictLogic(unittest.TestCase):
    def setUp(self):
        self._r, self._s = D.E.read_blob, D.shell_classify
        self._f = D.family_of

    def tearDown(self):
        D.E.read_blob, D.shell_classify, D.family_of = self._r, self._s, self._f

    def _row(self, body, py, sh, com):
        D.E.read_blob = lambda slug, path, timeout=25: body
        D.family_of = lambda t: py
        D.shell_classify = lambda t: (sh, com)
        return D.one(("o/r", "LICENSE"))

    def test_nc_erased_requires_the_python_family_to_be_commercially_usable(self):
        r = self._row("x" * 100, "CC-BY", "CC-BY-NC-4.0", "NO")
        self.assertEqual(r[6], "NC-ERASED")

    def test_an_nc_family_on_BOTH_sides_is_not_erased(self):
        # POSITIVE CONTROL for the gate: if the python side also carried the NC, there
        # would be nothing erased and the row must not be reported.
        r = self._row("x" * 100, "CC-BY-NC-4.0", "CC-BY-NC-4.0", "NO")
        self.assertNotEqual(r[6], "NC-ERASED")

    def test_agreement_tolerates_a_version_suffix(self):
        for py, sh in [("GPL", "GPL-2.0"), ("EUPL", "EUPL-1.2"),
                       ("CC-BY", "CC-BY-4.0"), ("MIT", "MIT")]:
            self.assertEqual(self._row("x" * 100, py, sh, "YES")[6], "AGREE",
                             (py, sh))

    def test_a_real_family_disagreement_is_vocabulary_not_agreement(self):
        for py, sh in [("MPL-2.0", "GPL-3.0"), ("LGPL", "GPL-2.0"),
                       ("AGPL-3.0", "CC-BY-SA-4.0")]:
            self.assertEqual(self._row("x" * 100, py, sh, "YES")[6], "VOCABULARY",
                             (py, sh))

    def test_one_sided_unknowns_are_their_own_classes(self):
        self.assertEqual(self._row("x" * 100, "UNKNOWN", "Elastic", "NO")[6],
                         "PYTHON-UNKNOWN")
        self.assertEqual(self._row("x" * 100, "MIT", "", "YES")[6], "SHELL-UNKNOWN")

    def test_unreadable_payload_is_not_a_disagreement(self):
        D.E.read_blob = lambda slug, path, timeout=25: ""
        self.assertEqual(D.one(("o/r", "LICENSE"))[6], "UNREADABLE")

    def test_every_row_has_seven_columns(self):
        for args in [("x" * 100, "MIT", "MIT", "YES"),
                     ("x" * 100, "UNKNOWN", "Elastic", "NO")]:
            self.assertEqual(len(self._row(*args)), 7, args)


class TestPublishedResultIntegrity(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        import os
        here = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(here, "result.2026-10-07.tsv")) as f:
            cls.rows = [l.rstrip("\n").split("\t") for l in f][1:]

    def test_denominator_is_the_licensed_side(self):
        self.assertEqual(len(self.rows), 412)

    def test_no_short_rows(self):
        self.assertTrue(all(len(r) == 7 for r in self.rows))

    def test_the_commercial_column_is_not_constant(self):
        # The exact defect: a column constant across 412 rows is not a measurement.
        self.assertEqual({r[5] for r in self.rows}, {"YES", "NO"})

    def test_no_unclassified_row_is_in_the_nc_class(self):
        for r in self.rows:
            if r[6] == "NC-ERASED":
                self.assertNotIn("UNCLASSIFIED", r[4], r[0])

    def test_the_nc_erased_class_is_nonempty_and_small(self):
        # Written as a PROPERTY (P399): the claim is that this class EXISTS and is a
        # handful, not that it is exactly five forever.
        nc = [r for r in self.rows if r[6] == "NC-ERASED"]
        self.assertTrue(nc)
        self.assertLess(len(nc), 40)

    def test_the_specimen_is_in_it(self):
        self.assertIn("facebookresearch/seamless_communication",
                      [r[0] for r in self.rows if r[6] == "NC-ERASED"])

    def test_both_classifiers_have_rows_the_other_misses(self):
        # THE HEADLINE, as a property: neither classifier is a superset of the other.
        py_blind = [r for r in self.rows
                    if r[6] in ("NC-ERASED", "PYTHON-UNKNOWN")]
        sh_blind = [r for r in self.rows
                    if r[6] == "VOCABULARY" and "UNCLASSIFIED" in r[4]]
        self.assertTrue(py_blind, "python-blind class is empty")
        self.assertTrue(sh_blind, "shell-blind class is empty")


if __name__ == "__main__":
    unittest.main(verbosity=2)
