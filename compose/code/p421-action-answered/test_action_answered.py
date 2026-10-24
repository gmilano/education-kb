"""Controls for `action_answered`.

The load-bearing one is `test_denominator_is_not_zero`.  `action-gap-crosscheck`
— the instrument this one re-notates — has a PASSING 16-control suite and
reports `0` citations over the live corpus, because it reads a notation the
register retired.  A gate whose denominator is zero is green for the same
reason a correct one is green, so the denominator is asserted here, not
printed.

The second group pins the THREE amendments p421 measured.  The first draft of
this instrument reported 268 findings; each amendment has its own control so a
successor cannot quietly undo one.
"""

import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from action_answered import (                     # noqa: E402
    cells_of, clause_of, closures, grade, platform_vocabulary, run, sections,
    shelf_graded_addresses, subjects_asked_about,
)

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                    os.pardir, os.pardir, os.pardir)

# The real specimen, copied byte-for-byte from `intel/open-gaps.md` at p420.
P420_E = ("| 🆕 `ACTION p420-E` | 🟡 **Resolve first-hand whether any Open edX "
          "component or Sakai is Apache-2.0**, against the majority AGPL-3.0 / "
          "ECL-2.0. 🔵 Two sources in this pass's vertical leg assert it; `p289` "
          "forbids writing either into a cell unread |")
P420_B = ("| 🆕 `ACTION p420-B` | 🟢 **Build `gate-grant-tree` to Amendment 10**, "
          "not to `ACTION p419-A`. Fixtures all measured today: `GradeU` (`main` "
          "granted / `teacher`+`admin` not) positive · `moodle/moodle` "
          "`MOODLE_15_STABLE` (`lang/en/docs/licence.html`) for **10.2** |")
P420_C = ("| 🆕 `ACTION p420-C` | 🟢 **Run `gate-slug-oracle` (`p293`) against the "
          "8 addresses of `Gap 420-C`** and record each as *absent* or *private*. "
          "🔵 One command against an instrument that already exists |")

VOCAB = {"open edx": "AGPL-3.0", "sakai": "ECL-2.0", "moodle": "GPL-3.0",
         "openeducat": "LGPL-3.0"}
GRADED = {"moodle/moodle": "GPL-3.0", "agents/top.md": "MIT"}


def block(*rows):
    return "## 🆕 `p420` · 2026-10-24 — h\n\n### 🟢 Actions\n\n" + "\n".join(rows) + "\n"


class Denominator(unittest.TestCase):
    """The control that `action-gap-crosscheck` did not have."""

    def test_denominator_is_not_zero(self):
        findings, denom = run(ROOT)
        self.assertGreater(denom["action_blocks"], 0,
                           "no action block parsed: the instrument is blind")
        self.assertGreater(denom["actions"], 0,
                           "no action parsed: the instrument is blind")
        self.assertGreater(denom["closed_gaps"], 0, "no closure parsed")
        self.assertGreater(denom["platforms"], 0, "platform vocabulary is empty")

    def test_a_blind_parse_is_distinguishable_from_a_clean_one(self):
        # The retired notation yields a zero denominator, which is the failure
        # mode this suite exists to make visible rather than green.
        retired = ("## 158. **Gap 50, CERRADO**\n\n"
                   "## las acciones que el pase 59 deja escritas\n\n"
                   "- resolver el gap 51\n")
        _, denom = grade(retired, "", [""])
        self.assertEqual(denom["action_blocks"], 0)
        self.assertEqual(denom["actions"], 0)


class RealSpecimen(unittest.TestCase):
    def test_p420_e_is_caught_on_both_halves(self):
        findings, _ = grade(block(P420_E), "", [""])
        got = {(f[2], f[3]) for f in findings} if findings else set()
        # With no verticals text the vocabulary is empty, so the arm cannot fire:
        # that is the point of the next control.
        self.assertEqual(got, set())

    def test_p420_e_fires_against_the_real_platform_vocabulary(self):
        findings, _ = grade(block(P420_E), "", [""])
        self.assertEqual(findings, [])
        f2, _ = grade(block(P420_E), _verticals(), [""])
        subjects = sorted(f[3] for f in f2)
        self.assertEqual(subjects, ["open edx", "sakai"])
        self.assertTrue(all(f[2] == "ANSWERED-BY-PLATFORM" for f in f2))
        self.assertTrue(all(f[1] == "p420-E" for f in f2))

    def test_the_whole_corpus_yields_exactly_the_specimen(self):
        """The RATCHET.  Two findings, both `ACTION p420-E`, zero false."""
        findings, _ = run(ROOT)
        self.assertEqual(len(findings), 2, [f[:4] for f in findings])
        self.assertEqual({f[1] for f in findings}, {"p420-E"})
        self.assertEqual(sorted(f[3] for f in findings), ["open edx", "sakai"])


class Amendment1_AddressChannel(unittest.TestCase):
    """A shelf path is not a repository, and p348's channel excludes it by shape."""

    def test_a_shelf_path_can_never_be_a_subject(self):
        cell = ("Resolve whether `agents/top.md` is Apache-2.0")
        self.assertEqual(subjects_asked_about(cell, {}, GRADED), [])

    def test_the_shelf_index_is_anchored_on_github_com(self):
        idx = shelf_graded_addresses(
            ["| a row | MIT | see `agents/top.md` and `lang/en/docs/licence.html` |"])
        self.assertEqual(idx, {})

    def test_a_real_github_address_does_enter_the_index(self):
        idx = shelf_graded_addresses(
            ["| [`moodle/moodle`](https://github.com/moodle/moodle) | GPL-3.0 |"])
        self.assertEqual(idx, {"moodle/moodle": "GPL-3.0"})


class Amendment2_RowSubject(unittest.TestCase):
    """A clause that cites a second action is referencing it, not delivering it."""

    def test_a_referenced_action_is_not_graded_on_this_clause(self):
        findings, denom = grade(block(P420_B), _verticals(), [""])
        self.assertEqual(denom["actions"], 1, "both ids in one row were counted")
        self.assertEqual(findings, [])

    def test_a_fixture_list_is_not_an_ask(self):
        findings, _ = grade(block(P420_B), _verticals(), [""])
        self.assertEqual(findings, [],
                         "a fixture naming moodle/moodle is not a licence question")


class Amendment3_OrderedTemplate(unittest.TestCase):
    """The subject must be the OBJECT of the ask, and the token must DIFFER."""

    def test_a_bound_refinement_does_not_fire(self):
        cell = "resolve whether openeducat is LGPL-3.0 only or or-later"
        self.assertEqual(subjects_asked_about(cell, VOCAB, {}), [],
                         "asking about a grade the base already carries is a refinement")

    def test_a_mismatching_token_does_fire(self):
        cell = "resolve whether Sakai is Apache-2.0"
        got = subjects_asked_about(cell, VOCAB, {})
        self.assertEqual([(g[0], g[2]) for g in got],
                         [("sakai", "ANSWERED-BY-PLATFORM")])

    def test_order_matters_licence_before_subject_does_not_fire(self):
        cell = "resolve whether Apache-2.0 appears, and separately read Sakai"
        self.assertEqual(subjects_asked_about(cell, VOCAB, {}), [])

    def test_a_copula_is_required(self):
        cell = "resolve whether Sakai — Apache-2.0 — needs a re-read"
        self.assertEqual(subjects_asked_about(cell, VOCAB, {}), [])

    def test_an_action_with_no_licence_question_does_not_fire(self):
        findings, _ = grade(block(P420_C), _verticals(), [""])
        self.assertEqual(findings, [])


class Notation(unittest.TestCase):
    def test_both_section_notations_parse(self):
        text = ("## 🆕 `p420` · 2026-10-24 — h\n\nbody\n\n"
                "## Pass 382 · 2026-10-22 — **old**\n\nbody\n")
        self.assertEqual([n for n, _ in sections(text)], [420, 382])

    def test_all_three_action_heading_phrasings_parse(self):
        for heading in ("### 🟢 Actions",
                        "### 🟢 Actions — ranked, cheapest first",
                        "### 🟢 The three registered actions, and their disposition"):
            text = f"## 🆕 `p1` · d — h\n\n{heading}\n\n| 🆕 `ACTION p1-A` | ask |\n"
            _, denom = grade(text, "", [""])
            self.assertEqual(denom["actions"], 1, heading)


class Attribution(unittest.TestCase):
    """T103 — by SENTENCE (here, by ROW then CELL), never by line number."""

    def test_a_table_match_is_attributed_to_its_row(self):
        blk = "| `ACTION p1-A` | first ask |\n| `ACTION p1-B` | second ask |\n"
        pos = blk.index("p1-B")
        self.assertEqual(clause_of(blk, pos), "| `ACTION p1-B` | second ask |")

    def test_a_row_splits_into_cells(self):
        self.assertEqual(cells_of("| a | b | c |"), ["a", "b", "c"])

    def test_prose_is_attributed_to_its_sentence(self):
        blk = "First sentence here. ACTION p1-A asks something. Third one."
        pos = blk.index("ACTION")
        self.assertIn("asks something", clause_of(blk, pos))
        self.assertNotIn("Third one", clause_of(blk, pos))


class StaleArm(unittest.TestCase):
    """The ported arm: an action citing a gap the register already closed."""

    def test_a_citation_of_an_earlier_closure_is_stale(self):
        text = ("## 🆕 `p10` · d — h\n\n### 🟢 Closed this pass\n\n"
                "| 🟢 `Gap 5-A` | closed |\n\n"
                "## 🆕 `p20` · d — h\n\n### 🟢 Actions\n\n"
                "| 🆕 `ACTION p20-A` | re-open `Gap 5-A` |\n")
        findings, _ = grade(text, "", [""])
        self.assertEqual([(f[1], f[2], f[3]) for f in findings],
                         [("p20-A", "STALE", "Gap 5-A")])

    def test_a_forward_reference_is_not_stale(self):
        text = ("## 🆕 `p20` · d — h\n\n### 🟢 Actions\n\n"
                "| 🆕 `ACTION p20-A` | close `Gap 5-A` |\n\n"
                "## 🆕 `p30` · d — h\n\n### 🟢 Closed this pass\n\n"
                "| 🟢 `Gap 5-A` | closed |\n")
        findings, _ = grade(text, "", [""])
        self.assertEqual(findings, [])

    def test_closures_are_attributed_by_row_not_by_block(self):
        text = ("## 🆕 `p10` · d — h\n\n### 🟢 Closed this pass\n\n"
                "| 🟢 `Gap 5-A` | closed |\n| 🟢 `Gap 6-B` | closed |\n")
        self.assertEqual(closures(text), {"5-A": 10, "6-B": 10})

    def test_the_live_register_cites_no_closed_gap_in_an_action(self):
        """A measurement, not a tautology: the denominators above are non-zero."""
        findings, _ = run(ROOT)
        self.assertEqual([f for f in findings if f[2] == "STALE"], [])


class Vocabulary(unittest.TestCase):
    def test_the_platform_vocabulary_is_closed_and_shelf_derived(self):
        vocab = platform_vocabulary(_verticals())
        self.assertIn("sakai", vocab)
        self.assertIn("open edx", vocab)
        self.assertEqual(vocab["sakai"], "ECL-2.0")

    def test_a_prose_sentence_first_cell_never_enters_the_vocabulary(self):
        shelf = "| **North American higher-ed integration reality** | MIT |\n"
        self.assertEqual(platform_vocabulary(shelf), {})

    def test_the_prose_first_cell_hole_is_open(self):
        """🟡 p421's known hole, asserted so it cannot be forgotten.

        A ONE-WORD prose first cell enters the vocabulary when its row carries a
        licence token.  It is latent on the live shelf (next control), and the
        obvious closure was refuted in-pass: co-occurrence with a `github.com/`
        slug drops `sakai`, the specimen's own subject, because this shelf grades
        Sakai with no address on its row.
        """
        self.assertEqual(platform_vocabulary("| **Inside** | MIT |\n"),
                         {"inside": "MIT"})

    def test_the_hole_is_latent_on_the_live_shelf(self):
        vocab = platform_vocabulary(_verticals())
        self.assertEqual(len(vocab), 14)
        for prose in ("inside", "outside"):
            self.assertNotIn(prose, vocab)

    def test_a_row_with_no_licence_token_never_enters(self):
        self.assertEqual(platform_vocabulary("| **Moodle** | an LMS |\n"), {})


def _verticals():
    with open(os.path.join(ROOT, "verticals", "solutions.md"), encoding="utf-8") as fh:
        return fh.read()


if __name__ == "__main__":
    unittest.main(verbosity=2)
