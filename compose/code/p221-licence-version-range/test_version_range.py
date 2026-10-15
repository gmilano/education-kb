"""Tests for p221's version-range instrument.

Every fixture is a VERBATIM reading taken 2026-10-15 from raw.githubusercontent.com,
with the byte size recorded in the test name's comment where it was measured.

Four are CONTROLS that must not fire:
  * a cell that already carries its bound must come back AGREE
  * an Apache-2.0 row must come back OUT-OF-SCOPE, not be coerced into a GNU verdict
  * the `AGPL-6 d` liveness-table artefact must not parse as a licence at all
  * a source that is bare on BOTH sides is the source's ambiguity, not a KB defect
"""

import unittest

from version_range import (audit_cell, combinable_with, parse_range, range_compare)

# --- verbatim file readings, 2026-10-15 -------------------------------------------
MOOVE = ("// it under the terms of the GNU General Public License as published by\n"
         "// the Free Software Foundation, either version 3 of the License, or\n"
         "// (at your option) any later version.\n"
         " * @license    http://www.gnu.org/copyleft/gpl.html GNU GPL v3 or later")
OAT_SA = ("* modify it under the terms of the GNU General Public License\n"
          "* as published by the Free Software Foundation; under version 2\n"
          "* of the License (non-upgradable).")
# Verbatim lines 6-9 of bbb-common-web/.../MeetingService.java, read 2026-10-15.
# The file is CRLF and the grant SENTENCE wraps: "any later" ends l.8, "version."
# opens l.9. The fixture keeps both, because the first version of this fixture
# stopped at l.8 and the instrument correctly read it as `unspecified`.
BBB = (" * This program is free software; you can redistribute it and/or modify it under the\r\n"
       " * terms of the GNU Lesser General Public License as published by the Free Software\r\n"
       " * Foundation; either version 3.0 of the License, or (at your option) any later\r\n"
       " * version.\r\n")
BBB_LINE_TRUNCATED = (
       " * Foundation; either version 3.0 of the License, or (at your option) any later\r\n")
TUTOR_HEADER = " * License: GPLv2 or later"
TUTOR_README = "License: GPLv3\nLicense URI: https://www.gnu.org/licenses/gpl-3.0.html"
LIFTERLMS = (" * License: GPLv3\n"
             " * License URI: https://www.gnu.org/licenses/gpl-3.0.html")
CELTIC = (" * @license  http://www.gnu.org/licenses/lgpl.html "
          "GNU Lesser General Public License, version 3")
TINCAN = ("# Licensed under the Apache License, Version 2.0 (the \"License\");\n"
          "#    you may not use this file except in compliance with the License.")


class TestParseRange(unittest.TestCase):

    def test_moodle_header_is_or_later(self):
        r = parse_range(MOOVE)
        self.assertEqual((r['family'], r['version'], r['bound']),
                         ('GPL', '3.0', 'or-later'))

    def test_non_upgradable_is_only(self):
        """oat-sa/lib-lti1p3-core: the word is `non-upgradable`, not `only`."""
        r = parse_range(OAT_SA)
        self.assertEqual((r['family'], r['version'], r['bound']),
                         ('GPL', '2.0', 'only'))

    def test_wrapped_grant_reads_as_or_later(self):
        """`ACTION QX`, folded into `RH` and landed: the sentence, not the line."""
        r = parse_range(BBB)
        self.assertEqual((r['family'], r['version'], r['bound']),
                         ('LGPL', '3.0', 'or-later'))

    def test_plugin_header_plus_suffix(self):
        self.assertEqual(parse_range(TUTOR_HEADER)['bound'], 'or-later')

    def test_pinned_version_without_bound_is_unspecified(self):
        """celtic LTI-PHP names version 3 and says nothing about later versions."""
        r = parse_range(CELTIC)
        self.assertEqual((r['family'], r['version'], r['bound']),
                         ('LGPL', '3.0', 'unspecified'))

    def test_bare_shelf_cell_is_unspecified(self):
        self.assertEqual(parse_range('GPL-3.0')['bound'], 'unspecified')

    def test_qualified_shelf_cell_reads_its_bound(self):
        self.assertEqual(parse_range('GPL-3.0-or-later')['bound'], 'or-later')
        self.assertEqual(parse_range('GPL-2.0-only')['bound'], 'only')

    def test_minor_version_is_normalised(self):
        self.assertEqual(parse_range('GPL-3')['version'], '3.0')

    def test_line_truncated_grant_is_honestly_unspecified(self):
        """The failure that produced `_normalise`, kept as a regression test.

        Cut the same grant at the line break and it is worse than underspecified:
        the words "Lesser General Public License" are on the PREVIOUS line, so a
        line-based reading of this file identifies neither the family nor the bound.
        The instrument must decline it rather than guess `or-later` from "any later".
        """
        r = parse_range(BBB_LINE_TRUNCATED)
        self.assertFalse(r['gnu'])
        self.assertIsNone(r['bound'])

    def test_crlf_does_not_break_the_read(self):
        self.assertEqual(parse_range(BBB)['family'], 'LGPL')

    # ---- CONTROL ----
    def test_control_daycount_artefact_is_not_a_licence(self):
        """`AGPL-6 d` is a liveness table's DAY COUNT. p221's census found one.

        It must not come back as AGPL version 6.
        """
        r = parse_range('AGPL-6 d / Apache-54 d spread')
        self.assertNotEqual(r['version'], '6.0')

    # ---- CONTROL ----
    def test_control_apache_is_out_of_scope(self):
        self.assertFalse(parse_range(TINCAN)['gnu'])


class TestRangeCompare(unittest.TestCase):

    def test_bare_cell_against_or_later_file_is_underspecified(self):
        """The 4 Moodle rows read this pass, and the pass's headline."""
        self.assertEqual(range_compare('GPL-3.0', MOOVE), 'RANGE-UNDERSPECIFIED')

    def test_bare_cell_against_only_file_is_underspecified(self):
        """The shelf cell for oat-sa is a bare `GPL-2.0`; the file says v2 ONLY."""
        self.assertEqual(range_compare('GPL-2.0', OAT_SA), 'RANGE-UNDERSPECIFIED')

    def test_tutor_three_channels_differ_in_VERSION_not_just_bound(self):
        """themeum/tutor, read 2026-10-15 - and the expectation this test corrected.

        `tutor.php` says `GPLv2 or later`; `readme.txt` says `GPLv3`. That is not two
        bounds on one grant, it is TWO DIFFERENT GRANTS, and the instrument must say
        so rather than filing it as a range problem. The shelf publishes `GPL-3.0`,
        which matches one of the three channels and hides the other two.
        """
        self.assertEqual(range_compare(TUTOR_README, TUTOR_HEADER), 'GRANT-CONFLICT')
        self.assertEqual(parse_range(TUTOR_HEADER)['version'], '2.0')
        self.assertEqual(parse_range(TUTOR_README)['version'], '3.0')

    def test_lesser_vs_plain_is_a_grant_conflict(self):
        self.assertEqual(range_compare('GPL-3.0', BBB), 'GRANT-CONFLICT')

    def test_version_mismatch_is_a_grant_conflict(self):
        self.assertEqual(range_compare('GPL-3.0', OAT_SA), 'GRANT-CONFLICT')

    def test_pure_bound_disagreement_is_a_range_conflict(self):
        """Same family, same version, opposite bounds - the state's real case."""
        self.assertEqual(range_compare('GPL-3.0-only', MOOVE), 'RANGE-CONFLICT')

    # ---- CONTROL ----
    def test_control_already_qualified_cell_agrees(self):
        self.assertEqual(range_compare('GPL-3.0-or-later', MOOVE), 'AGREE')

    # ---- CONTROL ----
    def test_control_bare_on_both_sides_is_the_sources_problem(self):
        """gocodebox/lifterlms is bare in the FILE too - not a KB defect."""
        self.assertEqual(range_compare('GPL-3.0', LIFTERLMS), 'BOTH-UNSPECIFIED')

    # ---- CONTROL ----
    def test_control_apache_row_is_out_of_scope(self):
        self.assertEqual(range_compare('Apache-2.0', TINCAN), 'OUT-OF-SCOPE')


class TestCombinability(unittest.TestCase):

    def test_gpl2_only_cannot_enter_a_gpl3_host(self):
        """The finding that pays for this instrument: oat-sa into a Moodle tree."""
        self.assertFalse(combinable_with('only', '2.0', '3.0'))

    def test_or_later_can(self):
        self.assertTrue(combinable_with('or-later', '2.0', '3.0'))

    def test_unspecified_is_unknown_not_yes(self):
        self.assertIsNone(combinable_with('unspecified', '2.0', '3.0'))


class TestAudit(unittest.TestCase):

    def test_oat_sa_audit_carries_the_incompatibility(self):
        a = audit_cell('GPL-2.0', OAT_SA, 'oat-sa/lib-lti1p3-core')
        self.assertEqual(a['state'], 'RANGE-UNDERSPECIFIED')
        self.assertFalse(a['combinable_with_gpl3'])
        self.assertIn('unusable', a['next'])

    def test_moove_audit_is_republishable(self):
        a = audit_cell('GPL-3.0', MOOVE, 'willianmano/moodle-theme_moove')
        self.assertEqual(a['state'], 'RANGE-UNDERSPECIFIED')
        self.assertTrue(a['combinable_with_gpl3'])


if __name__ == '__main__':
    unittest.main()
