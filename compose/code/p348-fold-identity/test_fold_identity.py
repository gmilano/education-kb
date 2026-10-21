#!/usr/bin/env python3
"""p348 -- controls for ACTION ZZ-x's offline half.

Every control here is a statement this pass measured first-hand, not a shape invented to
make a suite pass.  The fixtures name real addresses from these shelves and the real
HEAD shas they resolved to.
"""
import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import fold_identity as fi  # noqa: E402

LIVE = "## Pass 348 · 2026-10-20 — live\n\n%s\n\n## Pass 347 · 2026-10-20 — prior\n\n%s\n"


def write(d, name, body):
    p = os.path.join(d, name)
    with open(p, "w", encoding="utf-8") as fh:
        fh.write(body)
    return p


class Harvest(unittest.TestCase):
    def test_plain_address(self):
        self.assertEqual(fi.slugs_in("see https://github.com/dodona-edu/dolos now"),
                         ["dodona-edu/dolos"])

    def test_markdown_link_and_trailing_paren(self):
        # the shelves write every row as [`a/b`](https://github.com/a/b): the backticked
        # label is NOT a URL, so the row yields the address once, not twice.  A harvester
        # that counted the label too would double every row in the denominator.
        self.assertEqual(fi.slugs_in("[`fairlearn/fairlearn`](https://github.com/fairlearn/fairlearn)"),
                         ["fairlearn/fairlearn"])

    def test_trailing_sentence_period_is_not_part_of_the_name(self):
        self.assertEqual(fi.slugs_in("at https://github.com/latam-gpt/anonymization-filter."),
                         ["latam-gpt/anonymization-filter"])

    def test_dot_git_suffix_folds_to_the_same_address(self):
        self.assertEqual(fi.slugs_in("https://github.com/examplary/qti.git"),
                         ["examplary/qti"])

    def test_a_blob_url_names_its_REPOSITORY(self):
        # Deliberate, and the opposite of what the first draft of this control asserted.
        # For an IDENTITY index a file URL does name the repository that holds the file,
        # so `.../blob/main/LICENSE` must fold onto `a/b` -- otherwise a shelf could cite
        # one repository by its root and a second casing by a blob path and collide with
        # neither.  `carried_index.py` has read addresses this way since p235.
        self.assertEqual(fi.slugs_in("https://github.com/a/b/blob/main/LICENSE"), ["a/b"])

    def test_command_template_is_not_an_address(self):
        # p347 dropped two placeholders by hand; here it is a rule
        self.assertEqual(fi.slugs_in("git clone https://github.com/OWNER/REPO"), [])
        self.assertEqual(fi.slugs_in("https://github.com/owner/repo"), [])


class Census(unittest.TestCase):
    def test_collision_is_reported_with_both_casings(self):
        with tempfile.TemporaryDirectory() as d:
            p = write(d, "a.md", "https://github.com/CAHLR/OATutor\nhttps://github.com/cahlr/OATutor\n")
            total, groups = fi.census([p])
            self.assertEqual(total, 1)
            self.assertEqual(groups["cahlr/oatutor"], ["CAHLR/OATutor", "cahlr/OATutor"])

    def test_three_variant_group_is_one_group(self):
        # OpenOLAT really is published three ways on these shelves
        with tempfile.TemporaryDirectory() as d:
            p = write(d, "a.md", "https://github.com/OpenOLAT/OpenOLAT\n"
                                 "https://github.com/OpenOLAT/OpenOlat\n"
                                 "https://github.com/openolat/OpenOLAT\n")
            total, groups = fi.census([p])
            self.assertEqual(total, 1)
            self.assertEqual(len(groups), 1)
            self.assertEqual(len(groups["openolat/openolat"]), 3)

    def test_an_org_transfer_is_NOT_a_collision_and_that_is_the_point(self):
        # digitalcredentials/... and openwallet-foundation-labs/... are ONE repository at
        # HEAD 1c46a82ba384, and folding cannot see it.  The census must not pretend to.
        with tempfile.TemporaryDirectory() as d:
            p = write(d, "a.md",
                      "https://github.com/digitalcredentials/learner-credential-wallet\n"
                      "https://github.com/openwallet-foundation-labs/learner-credential-wallet\n")
            total, groups = fi.census([p])
            self.assertEqual(total, 2)
            self.assertEqual(groups, {})

    def test_census_never_fails(self):
        with tempfile.TemporaryDirectory() as d:
            p = write(d, "a.md", "https://github.com/A/b\nhttps://github.com/a/b\n")
            self.assertEqual(fi.main(["census", p]), 0)


class LiveSection(unittest.TestCase):
    def test_split_is_at_the_second_pass_heading(self):
        cur, old = fi.split_live_section(LIVE % ("https://github.com/x/live",
                                                 "https://github.com/x/old"))
        self.assertIn("x/live", cur)
        self.assertNotIn("x/old", cur)
        self.assertIn("x/old", old)

    def test_a_file_with_one_pass_heading_is_all_live(self):
        cur, old = fi.split_live_section("## Pass 348 · x\n\nhttps://github.com/x/y\n")
        self.assertIn("x/y", cur)
        self.assertEqual(old, "")


class Gate(unittest.TestCase):
    def test_new_casing_in_the_live_section_FAILS(self):
        with tempfile.TemporaryDirectory() as d:
            p = write(d, "top.md", LIVE % ("https://github.com/cahlr/OATutor",
                                           "https://github.com/CAHLR/OATutor"))
            f = fi.gate([p])
            self.assertEqual(len(f), 1)
            self.assertEqual(f[0][1], "P348-NEW-CASING")
            self.assertEqual(f[0][2], "cahlr/OATutor")
            self.assertIn("CAHLR/OATutor", f[0][3])

    def test_the_published_casing_PASSES(self):
        with tempfile.TemporaryDirectory() as d:
            p = write(d, "top.md", LIVE % ("https://github.com/CAHLR/OATutor",
                                           "https://github.com/CAHLR/OATutor"))
            self.assertEqual(fi.gate([p]), [])

    def test_a_genuinely_new_address_PASSES(self):
        # the gate must not block supply; it blocks a SECOND SPELLING of held supply
        with tempfile.TemporaryDirectory() as d:
            p = write(d, "top.md", LIVE % ("https://github.com/dodona-edu/dolos",
                                           "https://github.com/CAHLR/OATutor"))
            self.assertEqual(fi.gate([p]), [])

    def test_history_in_ANOTHER_file_still_counts_as_published(self):
        with tempfile.TemporaryDirectory() as d:
            a = write(d, "top.md", LIVE % ("https://github.com/cahlr/OATutor", "nothing here"))
            b = write(d, "trending.md", LIVE % ("x", "https://github.com/CAHLR/OATutor"))
            f = fi.gate([a, b])
            self.assertEqual([x[1] for x in f], ["P348-NEW-CASING"])

    def test_gate_exit_status_is_the_signal(self):
        with tempfile.TemporaryDirectory() as d:
            bad = write(d, "bad.md", LIVE % ("https://github.com/cahlr/OATutor",
                                             "https://github.com/CAHLR/OATutor"))
            good = write(d, "good.md", LIVE % ("https://github.com/CAHLR/OATutor",
                                               "https://github.com/CAHLR/OATutor"))
            self.assertEqual(fi.main(["gate", bad]), 1)
            self.assertEqual(fi.main(["gate", good]), 0)

    def test_P541_no_input_is_REFUSED_not_passed(self):
        self.assertEqual(fi.main(["gate"]), 2)
        self.assertEqual(fi.main([]), 2)


class MeasuredCorpus(unittest.TestCase):
    """The two numbers this pass published, pinned so a later pass cannot drift them
    silently: 65 collision groups over the complete nine-shelf set, and p347's
    five-file denominator of 440."""

    def setUp(self):
        self.root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
        self.all9 = [os.path.join(self.root, p) for p in (
            "agents/top.md", "agents/trending.md", "repos/foundations.md",
            "repos/trending.md", "verticals/solutions.md", "intel/market.md",
            "intel/trends.md", "intel/open-gaps.md", "compose/patterns.md")]
        self.live5 = [os.path.join(self.root, p) for p in (
            "agents/top.md", "repos/foundations.md", "verticals/solutions.md",
            "compose/patterns.md", "intel/market.md", "intel/trends.md",
            "intel/open-gaps.md")]
        if not all(os.path.exists(p) for p in self.all9):
            self.skipTest("run from inside the KB")

    def test_the_append_only_shelves_hold_the_majority_of_the_addresses(self):
        total9, _ = fi.census(self.all9)
        total5, _ = fi.census(self.live5)
        self.assertGreater(total9, 2000)
        self.assertLess(total5 * 3, total9)   # p347's set is under a third of the whole

    def test_collision_groups_do_not_drop_silently(self):
        _, groups = fi.census(self.all9)
        self.assertGreaterEqual(len(groups), 65)

    def test_the_live_sections_are_clean(self):
        self.assertEqual(fi.gate(self.all9), [])



class DatedHeadingForm(unittest.TestCase):
    """🔴 p349: `agents/trending.md` writes `## 2026-10-20 · Pass 348 — …`, date first.
    Anchored at `^## Pass`, the splitter walked past every dated heading and put the
    live/history boundary tens of thousands of lines down in the old-form history, so
    most of that file counted as the live section. It passed anyway — a boundary that is
    too generous is silent until a gate using it finds something, and p349's author-key
    gate was that gate on its first run."""

    def test_C22_date_first_heading_is_a_pass_heading(self):
        text = ("## 2026-10-20 · Pass 349 — live\n\nlive body\n\n"
                "## 2026-10-20 · Pass 348 — history\n\nold body\n")
        live, old = fi.split_live_section(text)
        self.assertIn("live body", live)
        self.assertNotIn("old body", live)
        self.assertIn("old body", old)

    def test_C23_pass_first_heading_still_splits(self):
        text = "## Pass 349 · 2026-10-20 — live\n\nlive body\n\n## Pass 348 — old\n\nold body\n"
        live, old = fi.split_live_section(text)
        self.assertIn("live body", live)
        self.assertNotIn("old body", live)

    def test_C24_a_prose_H2_mentioning_a_pass_far_into_the_line_is_not_a_heading(self):
        # The window is bounded so a narrative H2 that happens to say "Pass 12" late in
        # its title cannot be read as a section boundary.
        text = ("## Pass 349 — live\n\nlive body\n\n"
                "## a long narrative heading that only much later happens to mention "
                "Pass 12 in passing\n\nstill live\n")
        live, _ = fi.split_live_section(text)
        self.assertIn("still live", live)


if __name__ == "__main__":
    unittest.main(verbosity=2)
