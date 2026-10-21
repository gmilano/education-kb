#!/usr/bin/env python3
"""Controls for `p352-census-currency`.

🔵 Every control is OFFLINE and runs from this directory (`p355-cwd-portability`'s class --
`python3 -I` strips the script's directory from `sys.path`, so the suite only resolves its
own module when invoked from here, which is why the Makefile recipe `cd`s in).
"""
import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import census_currency as cc  # noqa: E402

# The sentence form p351 actually published, at README.md:23, verbatim apart from the figures.
LIVE = ("🟢 **`ACTION ZZ-an` DISCHARGED — and its own prescription was insufficient.** "
        "**2 476** harvested shapes → **33** are not addresses → **2 443 addresses** "
        "(1.33 % inflation). 🔴 `ZZ-an` asked for a filter rejecting `topics/`")


class TheTripleParser(unittest.TestCase):
    def test_p351s_own_published_sentence_is_read_exactly(self):
        self.assertEqual(cc.published(LIVE), (2476, 33, 2443))

    def test_a_plain_space_is_the_measured_separator(self):
        # 0x32 0x20 0x34 0x34 0x33 at README.md:23 -- measured, not assumed.
        self.assertEqual(cc.to_int("2 443"), 2443)

    def test_the_thin_and_nobreak_spaces_are_accepted_too(self):
        # A later pass may paste one in; a cosmetic difference must not read as STALE.
        for sep in (" ", " ", " ", " ", ","):
            self.assertEqual(cc.to_int(f"2{sep}445"), 2445, sep)

    def test_an_ungrouped_figure_survives(self):
        self.assertEqual(cc.published(LIVE.replace("2 476", "2476")), (2476, 33, 2443))

    def test_a_single_digit_cell_survives(self):
        # The rejection count can legitimately fall to one digit.
        self.assertEqual(cc.published(LIVE.replace("**33** are not", "**7** are not")),
                         (2476, 7, 2443))

    def test_an_absent_sentence_is_None_and_not_zero(self):
        self.assertIsNone(cc.published("## Pass 352\n\nNo census this pass.\n"))

    def test_the_LIVE_occurrence_WINS_over_history(self):
        # 🔴 The load-bearing one. History below the live section holds previous passes'
        # figures, which were correct against THEIR trees. A gate that read the last match,
        # or demanded the whole file agree, would force the retro-editing this base's
        # `dated-by-measurement` convention forbids.
        doc = ("## Pass 352\n" + LIVE.replace("2 476", "2 478").replace("2 443", "2 445")
               + "\n\n## Pass 351\n" + LIVE + "\n")
        self.assertEqual(cc.published(doc), (2478, 33, 2445))

    def test_a_figure_without_the_bold_markers_is_not_read(self):
        # The anchor is the published SENTENCE, not any three numbers near the word harvested.
        self.assertIsNone(cc.published("2 478 harvested shapes, 33 are not addresses, "
                                       "2 445 addresses"))

    def test_the_anchor_tolerates_rewrapping(self):
        # These shelves are hard-wrapped prose: p278's first anchor MISSED because the phrase
        # it pinned wrapped. An anchor that breaks on rewrapping is the same brittleness
        # class as an anchor copied from the number under test.
        wrapped = ("**2 478** harvested\nshapes → **33** are\nnot addresses → "
                   "**2 445 addresses**")
        self.assertEqual(cc.published(wrapped.replace("harvested\nshapes", "harvested shapes")
                                      .replace("are\nnot", "are not")),
                         (2478, 33, 2445))


class TheVerdict(unittest.TestCase):
    """The gate's own exit behaviour, over a throwaway root."""

    def _root(self, readme, shelf_text="see https://github.com/moodle/moodle\n"):
        root = tempfile.mkdtemp()
        for rel in cc.SHELF_FILES:
            p = os.path.join(root, rel)
            os.makedirs(os.path.dirname(p), exist_ok=True)
            with open(p, "w", encoding="utf-8") as fh:
                fh.write(shelf_text)
        with open(os.path.join(root, cc.ANCHOR_FILE), "w", encoding="utf-8") as fh:
            fh.write(readme)
        return root

    def test_one_address_one_shelf_derives_one_and_zero(self):
        root = self._root("x")
        self.assertEqual(cc.derive(root), (1, 0, 1))

    def test_an_agreeing_triple_is_GREEN(self):
        root = self._root("**1** harvested shapes → **0** are not addresses → "
                          "**1 addresses**")
        self.assertEqual(cc.main(["--root", root]), 0)

    def test_a_disagreeing_ADDRESS_cell_alone_is_RED(self):
        root = self._root("**1** harvested shapes → **0** are not addresses → "
                          "**2 addresses**")
        self.assertEqual(cc.main(["--root", root]), 1)

    def test_a_disagreeing_HARVESTED_cell_alone_is_RED(self):
        # Each cell is load-bearing on its own: a pass can get the total right and the
        # rejection count wrong, and that still means the census was run at the wrong time.
        root = self._root("**9** harvested shapes → **0** are not addresses → "
                          "**1 addresses**")
        self.assertEqual(cc.main(["--root", root]), 1)

    def test_a_disagreeing_REJECTED_cell_alone_is_RED(self):
        root = self._root("**1** harvested shapes → **9** are not addresses → "
                          "**1 addresses**")
        self.assertEqual(cc.main(["--root", root]), 1)

    def test_a_MISSING_anchor_is_RED_and_not_silently_green(self):
        # 🔴 A headline denominator that quietly stops being stated is how p349's went
        # unchecked for two passes. Absence must be loud.
        self.assertEqual(cc.main(["--root", self._root("## Pass 352\n\nnothing\n")]), 1)

    def test_a_rejected_shape_is_counted_on_the_REJECTED_side(self):
        # The derivation must be p351's classifier, not a bare slug count: `topics/education`
        # is a navigation namespace, not an address.
        root = self._root("**2** harvested shapes → **1** are not addresses → "
                          "**1 addresses**",
                          shelf_text=("https://github.com/moodle/moodle\n"
                                      "https://github.com/topics/education\n"))
        self.assertEqual(cc.main(["--root", root]), 0)

    def test_the_derivation_IGNORES_the_anchor_file(self):
        # 🔵 Load-bearing: if README.md counted, the gate would check a number against a file
        # that the act of stating the number changes, and could never be trusted.
        root = self._root("**1** harvested shapes → **0** are not addresses → "
                          "**1 addresses**\nhttps://github.com/kantord/LibreLingo\n")
        self.assertEqual(cc.derive(root)[0], 1)
        self.assertEqual(cc.main(["--root", root]), 0)

    def test_a_missing_shelf_file_RAISES_rather_than_under_counting(self):
        root = self._root("x")
        os.remove(os.path.join(root, "compose/patterns.md"))
        with self.assertRaises(FileNotFoundError):
            cc.derive(root)

    def test_the_anchor_LADDER_is_case_closed_in_stem_AND_extension(self):
        # 🔴 p283's audit graded this instrument SINGLE-SPELLING the moment it entered
        # HOOK_GATES, and it was right: a one-rung path ladder cannot prove an absence.
        # 🟢 Closed rather than excepted -- the gate was not taught to look away.
        stems, exts = set(), set()
        for rung in cc.ANCHOR_LADDER:
            stem, _, ext = rung.partition(".")
            stems.add(stem)
            if ext:
                exts.add(ext)
        self.assertLess(len({x.lower() for x in stems}), len(stems), "stem case must vary")
        self.assertLess(len({e.lower() for e in exts}), len(exts), "ext case must vary")

    def test_a_lowercase_write_up_is_FOUND_rather_than_reported_missing(self):
        root = self._root("x")
        os.rename(os.path.join(root, "README.md"), os.path.join(root, "readme.md"))
        self.assertTrue(cc.resolve_anchor(root).endswith("readme.md"))

    def test_the_FIRST_rung_wins_when_several_exist(self):
        root = self._root("**1** harvested shapes → **0** are not addresses → "
                          "**1 addresses**")
        with open(os.path.join(root, "readme.md"), "w", encoding="utf-8") as fh:
            fh.write("**9** harvested shapes → **9** are not addresses → **9 addresses**")
        self.assertEqual(cc.main(["--root", root]), 0)

    def test_no_rung_at_all_is_a_REAL_absence(self):
        root = self._root("x")
        os.remove(os.path.join(root, "README.md"))
        self.assertIsNone(cc.resolve_anchor(root))

    def test_a_missing_README_is_refused_with_2_not_1(self):
        # P541: a measurement over nothing is REFUSED, and the refusal is distinguishable
        # from a stale figure -- exit 2, never exit 1.
        root = self._root("x")
        os.remove(os.path.join(root, cc.ANCHOR_FILE))
        self.assertEqual(cc.main(["--root", root]), 2)

    def test_p351s_REAL_defect_reproduces_on_its_OWN_committed_tree(self):
        # 🔴 The regression this gate exists for, pinned as data rather than as a story:
        # p351 published the p350 tree's triple. 2 476/33/2 443 was TRUE of p350 and FALSE of
        # the tree p351 committed (2 478/33/2 445).
        self.assertEqual(cc.published(LIVE), (2476, 33, 2443))
        self.assertNotEqual(cc.published(LIVE), (2478, 33, 2445))


if __name__ == "__main__":
    unittest.main(verbosity=0)
