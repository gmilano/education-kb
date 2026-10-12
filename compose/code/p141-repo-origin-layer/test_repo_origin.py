"""Tests for p141-repo-origin-layer.

The load-bearing tests are the REFUSALS. This KB has gone nine passes without a LATAM-owned
row and has said so; an instrument that books one by accident off `-0600` would convert an
honest gap into false coverage. p140 already caught itself booking North America three times
off placeholder hostnames. These tests make the same class of error impossible here.
"""

import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from repo_origin import AMBIGUOUS, OFFSET_REGION, book  # noqa: E402


class TestAmbiguousOffsetsAreRefused(unittest.TestCase):
    def test_minus_0600_is_not_north_america(self):
        region, note, _ = book({"-0600": 13, "-0700": 2, "-0400": 1})
        self.assertEqual(region, "UNMAPPED")
        self.assertIn("AMBIGUOUS", note)
        self.assertIn("Mexico City", note)

    def test_every_americas_offset_is_refused(self):
        for off in ("-0300", "-0400", "-0500", "-0600", "-0700"):
            with self.subTest(off=off):
                self.assertEqual(book({off: 99})[0], "UNMAPPED")

    def test_no_americas_offset_leaks_into_the_bookable_table(self):
        for off in AMBIGUOUS:
            self.assertNotIn(off, OFFSET_REGION,
                             "%s must not be bookable" % off)

    def test_latam_is_never_booked_by_this_instrument(self):
        """No offset in the table maps to LATAM, because none is unambiguous.

        If a future pass adds one, this test must be the thing that is changed first, with
        the reasoning written down -- not quietly satisfied by a new table entry.
        """
        self.assertEqual([o for o, (r, _) in OFFSET_REGION.items() if r == "LATAM"], [])


class TestUtcIsNotEvidence(unittest.TestCase):
    def test_all_utc_is_unmapped(self):
        region, note, _ = book({"+0000": 382})
        self.assertEqual(region, "UNMAPPED")
        self.assertIn("container default", note)

    def test_utc_does_not_outvote_a_real_offset(self):
        region, _, ev = book({"+0000": 382, "+0200": 76})
        self.assertEqual(region, "EMEA")
        self.assertIn("+0200", ev)


class TestUnambiguousBookings(unittest.TestCase):
    def test_plus_0800_is_apac(self):
        self.assertEqual(book({"+0800": 20})[0], "APAC")

    def test_plus_0530_is_apac(self):
        self.assertEqual(book({"+0530": 5})[0], "APAC")

    def test_plus_1100_and_1000_agree_on_apac(self):
        region, _, _ = book({"+1100": 135, "+0000": 50, "+1000": 6})
        self.assertEqual(region, "APAC")

    def test_plus_0300_is_emea(self):
        self.assertEqual(book({"+0300": 7})[0], "EMEA")

    def test_evidence_string_carries_the_denominator(self):
        _, _, ev = book({"+0800": 20})
        self.assertIn("of 20 commits", ev)


class TestCrossRegionDisagreementIsRefused(unittest.TestCase):
    def test_two_unambiguous_offsets_in_different_regions(self):
        region, note, _ = book({"+0800": 10, "+0200": 9})
        self.assertEqual(region, "UNMAPPED")
        self.assertIn("disagree", note)

    def test_a_single_stray_commit_does_not_block_a_booking(self):
        # One commit from a conference laptop should not void 828 from home.
        region, _, _ = book({"+0200": 828, "+0800": 1})
        self.assertEqual(region, "EMEA")

    def test_empty_history(self):
        self.assertEqual(book({})[0], "UNMAPPED")


if __name__ == "__main__":
    unittest.main(verbosity=2)
