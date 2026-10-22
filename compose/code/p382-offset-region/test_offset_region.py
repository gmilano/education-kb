import os, sys, unittest
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import offset_region as orr

class P381sTwoSpecimens(unittest.TestCase):
    """The two rows p381 named, and the verdicts its prose already reached BY HAND."""

    def test_undergraduate_coding_tutor_is_ambiguous_not_north_america(self):
        """3 commits, all -0500. p381 published NOT PLACED; this names WHY."""
        v, why = orr.place_offsets(["-0500", "-0500", "-0500"])
        self.assertEqual(v, orr.AMBIGUOUS)
        self.assertIn("indistinguishable", why)

    def test_ml_from_scratch_book_code_is_north_america(self):
        """18 commits carrying BOTH -0400 and -0500 -> one US location crossing DST."""
        v, why = orr.place_offsets(["-0400", "-0500", "-0400"])
        self.assertEqual(v, orr.NORTH_AMERICA)
        self.assertIn("DST boundary", why)

class L1TheDSTDegeneracySpecimen(unittest.TestCase):
    """`intellectif/learning-kit` -- 275 c, -0500(228), months 05 08 09 10, zero in Nov-Mar.
    trending.md graded it 🟡 NOT RESOLVED. 🟢 The span test does better: it RULES OUT US
    Eastern, which NOT RESOLVED does not."""

    def test_it_is_ambiguous_and_us_eastern_is_ruled_out(self):
        v, why = orr.place_offsets(["-0500"], months=[5, 8, 9, 10])
        self.assertEqual(v, orr.AMBIGUOUS)
        self.assertIn("US Eastern is RULED OUT", why)

    def test_and_that_is_strictly_more_than_not_resolved(self):
        self.assertNotEqual(orr.place_offsets(["-0500"], months=[5, 8, 9, 10])[0],
                            orr.NOT_RESOLVED)

class TheSpanTestResolvesLATAMPositively(unittest.TestCase):
    def test_minus_0500_in_both_windows_is_latam(self):
        v, why = orr.place_offsets(["-0500"], months=[1, 7])
        self.assertEqual(v, orr.LATAM)
        self.assertIn("year-round", why)

    def test_minus_0500_in_winter_only_rules_out_us_central(self):
        v, why = orr.place_offsets(["-0500"], months=[12, 1])
        self.assertEqual(v, orr.AMBIGUOUS)
        self.assertIn("US Central is RULED OUT", why)

class NegativeControls(unittest.TestCase):
    def test_a_non_colliding_offset_is_not_adjudicated(self):
        v, _ = orr.place_offsets(["+0800"])
        self.assertEqual(v, orr.NOT_RESOLVED)

    def test_empty_census_is_not_resolved_not_a_region(self):
        v, why = orr.place_offsets([])
        self.assertEqual(v, orr.NOT_RESOLVED)
        self.assertIn("no offset", why)

    def test_march_and_november_straddle_and_rule_nothing_out(self):
        v, why = orr.place_offsets(["-0500"], months=[3, 11])
        self.assertEqual(v, orr.AMBIGUOUS)
        self.assertIn("straddle", why)

    def test_a_verdict_is_never_a_bare_region_without_a_reason(self):
        for args in ([["-0500"], {}], [["-0400", "-0500"], {}], [[], {}]):
            v, why = orr.place_offsets(args[0], **args[1])
            self.assertTrue(why and len(why) > 20, (v, why))

if __name__ == "__main__":
    unittest.main(verbosity=2)
