#!/usr/bin/env python3
"""Validate the replication against OpenOLAT's OWN JUnit oracle cases.

Every assertion below is transcribed from the upstream test files at
HEAD e4be14f0:

  src/test/java/org/olat/core/commons/services/ai/essay/GibberishPreFilterTest.java
  src/test/java/org/olat/core/commons/services/ai/essay/AiGradingTierTest.java

If the replication disagrees with upstream's own expectations, the equity
measurement built on it is worthless -- so this runs first.

Run:  python3 -I test_script_equity.py
"""

import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from script_equity import classify, gibberish_check  # noqa: E402


class GibberishOracle(unittest.TestCase):
    """The six upstream GibberishPreFilterTest cases, verbatim inputs."""

    def test_null_returns_empty(self):
        self.assertFalse(gibberish_check(None)[0])

    def test_blank_returns_empty(self):
        self.assertFalse(gibberish_check("   ")[0])

    def test_too_short_text_passes_regardless(self):
        self.assertFalse(gibberish_check("aaa bbb ccc")[0])

    def test_natural_english_prose_passes(self):
        prose = (
            "The mitochondria is the powerhouse of the cell. "
            "It generates most of the cell's supply of adenosine triphosphate (ATP), "
            "used as a source of chemical energy."
        )
        self.assertFalse(gibberish_check(prose)[0])

    def test_natural_german_prose_passes(self):
        prose = (
            "Der Klimawandel ist eine der grössten Herausforderungen unserer Zeit. "
            "Wissenschaftler fordern sofortige Massnahmen zur Reduktion von Treibhausgasen."
        )
        self.assertFalse(gibberish_check(prose)[0])

    def test_keyboard_mash_is_rejected(self):
        self.assertTrue(gibberish_check("a" * 49)[0])

    def test_symbol_spam_is_rejected_by_letter_ratio(self):
        symbols = "1234567890!@#$%^&*()1234567890!@#$%^&*()"
        rejected, reason, _ratio, _entropy = gibberish_check(symbols)
        self.assertTrue(rejected)
        self.assertEqual("letter-ratio", reason)


class GradingTierOracle(unittest.TestCase):
    """The upstream AiGradingTierTest cases."""

    @staticmethod
    def words(n):
        return " ".join("word%d" % i for i in range(n))

    def test_null_returns_short(self):
        self.assertEqual("SHORT", classify(None)[0])

    def test_blank_returns_short(self):
        self.assertEqual("SHORT", classify("   ")[0])

    def test_single_word_is_short(self):
        self.assertEqual("SHORT", classify("hello")[0])

    def test_at_short_threshold_is_short(self):
        self.assertEqual("SHORT", classify(self.words(150))[0])

    def test_just_above_short_threshold_is_medium(self):
        self.assertEqual("MEDIUM", classify(self.words(151))[0])

    def test_at_medium_threshold_is_medium(self):
        self.assertEqual("MEDIUM", classify(self.words(400))[0])

    def test_just_above_medium_threshold_is_long(self):
        self.assertEqual("LONG", classify(self.words(401))[0])

    def test_heavily_cjk_text_uses_char_count(self):
        self.assertEqual("SHORT", classify("好" * 150)[0])

    def test_mixed_cjk_below_threshold(self):
        self.assertEqual("SHORT", classify("字" * 300)[0])


class ReplicationInternals(unittest.TestCase):
    """Guards on the two fidelity details the equity finding turns on."""

    def test_utf16_length_is_code_units_not_code_points(self):
        from script_equity import utf16_units
        # U+20000, a CJK Extension B ideograph: ONE code point, TWO UTF-16 units.
        self.assertEqual(2, len(utf16_units("\U00020000")))

    def test_devanagari_vowel_sign_is_not_a_java_letter(self):
        from script_equity import is_java_letter
        self.assertTrue(is_java_letter(0x092A))   # प  DEVANAGARI LETTER PA, Lo
        self.assertFalse(is_java_letter(0x093E))  # ा  VOWEL SIGN AA, Mc
        self.assertFalse(is_java_letter(0x094D))  # ्  VIRAMA, Mn

    def test_thai_vowel_sign_is_not_a_java_letter(self):
        from script_equity import is_java_letter
        self.assertTrue(is_java_letter(0x0E01))   # ก  THAI CHARACTER KO KAI, Lo
        self.assertFalse(is_java_letter(0x0E34))  # ิ  THAI VOWEL SIGN SARA I, Mn

    def test_arabic_harakat_is_not_a_java_letter(self):
        from script_equity import is_java_letter
        self.assertTrue(is_java_letter(0x0628))   # ب  ARABIC LETTER BEH, Lo
        self.assertFalse(is_java_letter(0x064E))  # َ   ARABIC FATHA, Mn

    def test_cjk_ranges_omit_extension_a_and_compatibility(self):
        from script_equity import _is_cjk
        self.assertTrue(_is_cjk(0x4E00))    # in CJK Unified
        self.assertFalse(_is_cjk(0x3400))   # CJK Extension A  -- NOT listed
        self.assertFalse(_is_cjk(0xF900))   # CJK Compatibility -- NOT listed
        self.assertFalse(_is_cjk(0x20000))  # CJK Extension B  -- NOT listed
        self.assertFalse(_is_cjk(0x1100))   # Hangul Jamo      -- NOT listed


if __name__ == "__main__":
    unittest.main(verbosity=2)
