"""Tests for p150-gpl-affero-discrimination. Authored fixtures, offline.

🔵 The fixtures reproduce the two licences at the only places that matter: the title
line, and section 13. The full bodies are not needed and are not used, which is why
these tests run with no network and no clone.
"""
import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gpl_affero as G  # noqa: E402

# GPL-3.0's shape: the title says GENERAL PUBLIC LICENSE and section 13 names Affero.
GPL3 = """                    GNU GENERAL PUBLIC LICENSE
                       Version 3, 29 June 2007

 Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>

                            Preamble

  The GNU General Public License is a free, copyleft license for
software and other kinds of works.

  13. Use with the GNU Affero General Public License.

  Notwithstanding any other provision of this License, you have
permission to link or combine any covered work with a work licensed
under version 3 of the GNU Affero General Public License into a single
combined work, and to convey the resulting work.  The terms of this
License will continue to apply to the part which is the covered work,
but the special requirements of the GNU Affero General Public License,
section 13, concerning interaction through a network will apply to the
combination as such.
"""

# AGPL-3.0's shape: the title says AFFERO and section 13 is Remote Network Interaction.
AGPL3 = """                    GNU AFFERO GENERAL PUBLIC LICENSE
                       Version 3, 19 November 2007

 Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>

                            Preamble

  The GNU Affero General Public License is a free, copyleft license for
software and other kinds of works.

  13. Remote Network Interaction; Use with the GNU General Public License.

  Notwithstanding any other provision of this License, if you modify the
Program, your modified version must prominently offer all users
interacting with it remotely through a computer network an opportunity
to receive the Corresponding Source of your version.
"""

MIT = """MIT License

Copyright (c) 2026 Someone

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction.
"""

LGPL3 = """                   GNU LESSER GENERAL PUBLIC LICENSE
                       Version 3, 29 June 2007

 Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
"""


class TheDefectReproduces(unittest.TestCase):
    """🔴 The published matcher must be shown wrong before it is replaced."""

    def test_naive_matcher_fires_on_plain_gpl3(self):
        self.assertEqual(G.naive_verdict(GPL3), "AGPL-3.0")

    def test_naive_matcher_also_fires_on_real_agpl3(self):
        # 🔵 It is not always wrong — which is why the defect survived.
        self.assertEqual(G.naive_verdict(AGPL3), "AGPL-3.0")

    def test_naive_matcher_cannot_distinguish_them(self):
        self.assertEqual(G.naive_verdict(GPL3), G.naive_verdict(AGPL3))

    def test_naive_matcher_is_silent_on_mit(self):
        self.assertIsNone(G.naive_verdict(MIT))


class TitleSurface(unittest.TestCase):
    def test_gpl3_title_is_gpl(self):
        self.assertEqual(G.title_licence(GPL3), "GPL")

    def test_agpl3_title_is_agpl(self):
        self.assertEqual(G.title_licence(AGPL3), "AGPL-3.0")

    def test_lgpl_is_not_read_as_gpl(self):
        self.assertEqual(G.title_licence(LGPL3), "LGPL")

    def test_mit_title(self):
        self.assertEqual(G.title_licence(MIT), "MIT")

    def test_title_window_ignores_blank_lines(self):
        padded = "\n\n\n" + GPL3
        self.assertEqual(G.title_licence(padded), "GPL")

    def test_affero_mention_below_the_window_cannot_reach_the_title(self):
        # The whole point: section 13 is outside the window.
        self.assertNotIn("Affero", G.title_window(GPL3))

    def test_unknown_licence_has_no_title_verdict(self):
        self.assertIsNone(G.title_licence("Do what you want.\n"))


class ClauseSurface(unittest.TestCase):
    def test_agpl_network_clause_present(self):
        self.assertEqual(G.clause_licence(AGPL3), "AGPL-3.0")

    def test_gpl_section13_is_the_affero_linking_permission(self):
        self.assertEqual(G.clause_licence(GPL3), "GPL")

    def test_mit_has_no_section_13(self):
        self.assertIsNone(G.clause_licence(MIT))

    def test_the_clause_is_anchored_not_substring(self):
        # Prose quoting the clause name mid-sentence must not satisfy it.
        prose = "see 13. Remote Network Interaction discussed in our FAQ"
        self.assertIsNone(G.clause_licence("Blah " + prose))


class BothSurfacesAgree(unittest.TestCase):
    def test_gpl3_agrees(self):
        verdict, _s, status = G.agree(GPL3)
        self.assertEqual((verdict, status), ("GPL", "AGREE"))

    def test_agpl3_agrees(self):
        verdict, _s, status = G.agree(AGPL3)
        self.assertEqual((verdict, status), ("AGPL-3.0", "AGREE"))

    def test_mit_is_title_only(self):
        verdict, _s, status = G.agree(MIT)
        self.assertEqual((verdict, status), ("MIT", "TITLE_ONLY"))

    def test_lgpl_title_with_gpl_clause_still_agrees(self):
        verdict, _s, status = G.agree(LGPL3 + "\n  13. Use with the GNU Affero\n")
        self.assertEqual((verdict, status), ("LGPL", "AGREE"))

    def test_a_frankenstein_file_is_reported_not_guessed(self):
        # AGPL title, GPL section 13: a hand-edited file. Must DISAGREE, not pick one.
        frank = AGPL3.replace("13. Remote Network Interaction; Use with the GNU General"
                              " Public License.",
                              "13. Use with the GNU Affero General Public License.")
        verdict, _s, status = G.agree(frank)
        self.assertEqual(status, "DISAGREE")
        self.assertEqual(verdict, "AGPL-3.0")

    def test_empty_input_is_undetermined_not_a_crash(self):
        # 🔵 p146's empty-walk guard, applied to this instrument.
        verdict, _s, status = G.agree("")
        self.assertEqual((verdict, status), (None, "UNDETERMINED"))


class CensusOverTrees(unittest.TestCase):
    def _tree(self, body, name="LICENSE"):
        d = tempfile.mkdtemp()
        with open(os.path.join(d, name), "w", encoding="utf-8") as fh:
            fh.write(body)
        return d

    def test_gpl3_tree_is_marked_overstated(self):
        r = G.census(self._tree(GPL3), "fixture")
        self.assertEqual((r["naive"], r["fixed"], r["delta"]),
                         ("AGPL-3.0", "GPL-3.0", "OVERSTATED"))

    def test_agpl3_tree_is_not_marked_overstated(self):
        r = G.census(self._tree(AGPL3), "fixture")
        self.assertEqual((r["naive"], r["fixed"], r["delta"]),
                         ("AGPL-3.0", "AGPL-3.0", "-"))

    def test_copying_filename_is_read(self):
        r = G.census(self._tree(GPL3, "COPYING"), "fixture")
        self.assertEqual(r["fixed"], "GPL-3.0")

    def test_tree_with_no_licence_file(self):
        r = G.census(tempfile.mkdtemp(), "fixture")
        self.assertEqual(r["status"], "NO_LICENCE_FILE")

    def test_absent_tree_is_no_clone(self):
        r = G.census("/nonexistent/path/xyz", "fixture")
        self.assertEqual(r["status"], "NO_CLONE")



class VersionSurface(unittest.TestCase):
    """🔵 `qxbao/qldt-hanu-mcp` is GPL-2.0 and was published as bare `LGPL`."""

    # 🔵 Realistic spacing: in the real file the title block is lines 1-4 and the
    # "Lesser" mention is at line 18, well past any title window.
    GPL2 = """                    GNU GENERAL PUBLIC LICENSE
                       Version 2, June 1991

 Copyright (C) 1989, 1991 Free Software Foundation, Inc.,
 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA

 Everyone is permitted to copy and distribute verbatim copies
 of this license document, but changing it is not allowed.

                            Preamble

  The licenses for most software are designed to take away your
freedom to share and change it.  By contrast, the GNU General Public
License is intended to guarantee your freedom to share and change free
software--to make sure the software is free for all its users.  This
License applies to most of the Free Software Foundation's software and
to any other program whose authors commit to using it.  (Some other
Free Software Foundation software is covered by the GNU Lesser General
Public License instead.)  You can apply it to your programs, too.
"""

    def test_gpl2_title_version(self):
        self.assertEqual(G.title_version(self.GPL2), "2.0")

    def test_gpl3_title_version(self):
        self.assertEqual(G.title_version(GPL3), "3.0")

    def test_gpl2_spdx_carries_the_version(self):
        self.assertEqual(G.spdx(self.GPL2), "GPL-2.0")

    def test_gpl3_spdx_carries_the_version(self):
        self.assertEqual(G.spdx(GPL3), "GPL-3.0")

    def test_gpl2_is_not_read_as_lgpl(self):
        # The defect that produced the published `LGPL` value: a body substring. The
        # sibling IS named in the body (line-wrapped, as in the real file), and the
        # title surface is unmoved by it.
        flat = " ".join(self.GPL2.split())
        self.assertIn("GNU Lesser General Public License", flat)
        self.assertEqual(G.spdx(self.GPL2), "GPL-2.0")

    def test_agpl_spdx_is_unversioned_by_construction(self):
        self.assertEqual(G.spdx(AGPL3), "AGPL-3.0")

    def test_mit_has_no_version(self):
        self.assertEqual(G.spdx(MIT), "MIT")

    def test_gpl2_has_no_section_13(self):
        self.assertIsNone(G.clause_licence(self.GPL2))

    def test_unknown_body_has_no_spdx(self):
        self.assertIsNone(G.spdx("do as you wish"))


if __name__ == "__main__":
    unittest.main(verbosity=2)
