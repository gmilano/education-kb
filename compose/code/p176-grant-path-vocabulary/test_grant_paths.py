"""Offline suite for `P176-B`. No network, no clock, no repository reads.

Run: python3 test_grant_paths.py   (plain python3 — `-I` would strip this
                                    directory from sys.path, `T271`)
"""

from __future__ import annotations

import unittest

import grant_paths as G


class VocabularyShape(unittest.TestCase):
    def test_the_british_spellings_are_present(self):
        for path in ("LICENCE", "LICENCE.md", "LICENCE.txt"):
            self.assertIn(path, G.VOCABULARY)

    def test_copying_md_is_present(self):
        """`3` of this repository's `76` lists carried it. It is the second path
        `gap 133` named and the one nobody had probed."""
        self.assertIn("COPYING.md", G.VOCABULARY)

    def test_the_known_positive_path_is_in_the_vocabulary(self):
        """`uccser/cs-field-guide` carries `MIT` at exactly this path."""
        self.assertTrue(G.is_grant_path("LICENCE"))

    def test_american_spellings_come_first(self):
        """Order is part of the vocabulary: a probe that stops at the first hit
        should stop early on the overwhelmingly commonest shape."""
        self.assertEqual(G.VOCABULARY[:3], G.AMERICAN)

    def test_no_duplicates(self):
        self.assertEqual(len(G.VOCABULARY), len(set(G.VOCABULARY)))

    def test_vocabulary_is_versioned(self):
        self.assertTrue(G.VERSION)


class NoticeIsNotAGrant(unittest.TestCase):
    """The control that stops the vocabulary converting an absence into a
    licence."""

    def test_notice_is_probed(self):
        self.assertIn("NOTICE", G.VOCABULARY)

    def test_notice_does_not_support_a_verdict(self):
        self.assertFalse(G.is_grant_path("NOTICE"))

    def test_notice_is_probed_last(self):
        self.assertEqual(G.VOCABULARY[-1], "NOTICE")


class FabricatedNegatives(unittest.TestCase):
    """Paths written to be the most plausible false positives available."""

    def test_a_readme_is_not_a_grant_path(self):
        self.assertFalse(G.is_grant_path("README.md"))

    def test_a_licence_shaped_source_file_is_not_a_grant_path(self):
        """`T223`: `105` of `Moodle`'s apparent `193` grant documents were PHP
        source files."""
        for path in ("license.php", "LICENSE.php", "licenselib.php"):
            self.assertFalse(G.is_grant_path(path))

    def test_a_nested_path_is_not_the_root_vocabulary(self):
        """`T209`: `openSIS-Classic`'s `GPL-2.0` is at `docs/License.txt`. That
        is a real grant and NOT a root-vocabulary hit, and conflating the two is
        what made the root-only probe unsound."""
        self.assertFalse(G.is_grant_path("docs/License.txt"))
        self.assertFalse(G.is_grant_path("html/license.txt"))


class ClaimRendering(unittest.TestCase):
    def test_an_absence_claim_carries_its_paths_ref_and_version(self):
        text = G.absence_claim("JushBJJ/Mr.-Ranedeer-AI-Tutor", "main", 16, 0)
        self.assertIn("0 of 16", text)
        self.assertIn("main", text)
        self.assertIn(G.VERSION, text)
        self.assertIn("ON THIS REF", text)

    def test_an_absence_claim_refuses_to_render_over_a_hit(self):
        with self.assertRaises(ValueError):
            G.absence_claim("uccser/cs-field-guide", "master", 16, 1)

    def test_only_enumeration_earns_the_word_exhaustive(self):
        text = G.exhaustive_claim(
            "JushBJJ/Mr.-Ranedeer-AI-Tutor",
            ("main", "v2.6.2", "v2.6.3", "dev/v2.7", "Speedrun-Brother"),
            55,
        )
        self.assertIn("exhaustive by ENUMERATION", text)
        self.assertIn("5 branches", text)
        self.assertIn("55 file-paths", text)

    def test_an_absence_claim_never_says_exhaustive(self):
        self.assertNotIn(
            "exhaustive", G.absence_claim("a/b", "main", 16, 0).lower()
        )


class EnumerationBoundary(unittest.TestCase):
    def test_a_twelve_file_tree_should_be_enumerated(self):
        self.assertTrue(G.enumeration_beats_probing(12))

    def test_a_canvas_sized_tree_is_still_enumerable(self):
        self.assertTrue(G.enumeration_beats_probing(200))

    def test_a_moodle_sized_tree_is_not(self):
        self.assertFalse(G.enumeration_beats_probing(50_000))


if __name__ == "__main__":
    unittest.main(verbosity=2)
