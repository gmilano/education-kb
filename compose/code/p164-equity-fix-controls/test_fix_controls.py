"""
ACTION IL regression net — P163-A step 1 (the nine-script corpus as cases)
and step 3 (Mn/Mc count as letters), with the controls as the guard.

Run: python3 -I test_fix_controls.py
"""
import sys
import unittest

sys.path.insert(0, ".")
import fixed_gate as F            # noqa: E402
import script_equity as base      # noqa: E402
import corpus                     # noqa: E402

BY_TAG = {r[0]: r[3] for r in corpus.CORPUS}
FIX = dict(marks_count=True, codepoint_denominator=True)


class Fidelity(unittest.TestCase):
    """The patched pipeline must be upstream's pipeline when unpatched."""

    def test_upstream_variant_matches_p163_replication(self):
        for tag, text in BY_TAG.items():
            with self.subTest(tag=tag):
                self.assertEqual(F.gibberish_check_patched(text),
                                 base.gibberish_check(text))


class ControlsSurviveTheFix(unittest.TestCase):
    """ACTION IL's falsifier, as executable assertions."""

    def test_symbol_spam_still_rejected_at_zero(self):
        rejected, reason, ratio, _ = F.gibberish_check_patched(
            BY_TAG["CTRL-symbols"], **FIX)
        self.assertTrue(rejected)
        self.assertEqual(reason, "letter-ratio")
        self.assertEqual(ratio, 0.0)

    def test_keyboard_mash_still_rejected(self):
        rejected, reason, _, _ = F.gibberish_check_patched(
            BY_TAG["CTRL-mash"], **FIX)
        self.assertTrue(rejected)
        # caught by entropy, NOT the ratio: the ratio is 1.000 either way,
        # so the ratio fix cannot reach this control by construction.
        self.assertEqual(reason, "entropy")

    def test_digits_and_punctuation_are_neither_letters_nor_marks(self):
        for ch in "0123456789!@#$%^&*()":
            with self.subTest(ch=ch):
                self.assertFalse(F.is_letter_or_mark(ord(ch)))


class EquityGain(unittest.TestCase):
    """p163's predictions, as assertions on the fixed gate."""

    def _ratio(self, tag, **kw):
        return F.gibberish_check_patched(BY_TAG[tag], **kw)[2]

    def test_vocalised_arabic_reaches_p163_predicted_099(self):
        self.assertAlmostEqual(self._ratio("ar-voc"), 0.552, places=3)
        self.assertGreater(self._ratio("ar-voc", **FIX), 0.98)

    def test_hindi_reaches_p163_predicted_098(self):
        self.assertAlmostEqual(self._ratio("hi"), 0.591, places=3)
        self.assertGreater(self._ratio("hi", **FIX), 0.98)

    def test_astral_han_denominator_moves_from_half_to_one(self):
        self.assertAlmostEqual(self._ratio("CTRL-extB"), 0.500, places=3)
        self.assertAlmostEqual(
            self._ratio("CTRL-extB", marks_count=False,
                        codepoint_denominator=True), 1.000, places=3)

    def test_no_valid_answer_changes_verdict(self):
        """The gain is MARGIN, not verdict: all ten were already accepted."""
        for tag in ("en", "de", "es", "zh", "ja", "ko", "ar", "ar-voc", "hi", "th"):
            with self.subTest(tag=tag):
                self.assertFalse(F.gibberish_check_patched(BY_TAG[tag])[0])
                self.assertFalse(F.gibberish_check_patched(BY_TAG[tag], **FIX)[0])

    def test_margin_spread_collapses(self):
        floor = base.MIN_LETTER_RATIO
        tags = ("en", "de", "es", "zh", "ja", "ko", "ar", "ar-voc", "hi", "th")
        up = [self._ratio(t) - floor for t in tags]
        fx = [self._ratio(t, **FIX) - floor for t in tags]
        self.assertGreater(max(up) / min(up), 5.0)    # upstream: 5.2x
        self.assertLess(max(fx) / min(fx), 1.2)       # fixed:    1.1x


if __name__ == "__main__":
    unittest.main(verbosity=2)
