#!/usr/bin/env python3
"""Tests for `rootonly_reach`. Run: python3 -I test_rootonly_reach.py

The first group pins a LATENT DEFECT IN p139's CLASSIFIER and its fix. p139's results
are not affected -- its three rows contain no nameless notice, and an audit of its
committed detail table finds zero year-shaped holders -- but the defect fired on the
first new row this pass read, so it is pinned here in both directions: the inherited
behaviour is asserted as-is, and the guard is asserted to suppress it.
"""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import rootonly_reach as rr  # noqa: E402

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "p139-source-header-holder"))
import header_holder as hh  # noqa: E402


class TestNamelessHolderDefect(unittest.TestCase):
    """`adaptlearning/adapt_framework` ships `"attribution": "Copyright © 2024"` in
    `src/course/en/components.json`. Unguarded, p139's extractor publishes `2024` as a
    FOREIGN COPYRIGHT HOLDER of the repository."""

    def test_p139_extractor_returns_the_year_as_a_holder(self):
        """The inherited behaviour, asserted so the fix cannot drift away from it."""
        self.assertEqual(hh.extract_holder("Copyright © 2024"), "2024")

    def test_guard_suppresses_the_nameless_notice(self):
        self.assertIsNone(rr.extract_holder("Copyright © 2024"))

    def test_guard_suppresses_the_verbatim_json_line(self):
        line = '          "attribution": "Copyright © 2024"'
        self.assertEqual(hh.extract_holder(line), "2024")
        self.assertIsNone(rr.extract_holder(line))

    def test_guard_suppresses_other_nameless_forms(self):
        for line in ("Copyright (c) 2024", "Copyright 2013-2015", "Copyright © 2020, 2021",
                     "copyright (C) 1999"):
            with self.subTest(line=line):
                self.assertIsNone(rr.extract_holder(line))

    def test_real_holders_still_survive_the_guard(self):
        """The guard must not cost a single real holder. Each of these is verbatim from
        a row read this pass or by p139."""
        cases = {
            "Copyright (c) 2016 Tim Branyen, contributors": "Tim Branyen, contributors",
            "Copyright 2014, edX": "edX",
            "Copyright 2013-2015, edX": "edX",
            "Copyright (C) 2013  ADAPT LEARNING": "ADAPT LEARNING",
            "Copyright 2024-2026 Crosstalk Solutions LLC": "Crosstalk Solutions LLC",
            "Copyright (c) 2026 Arnaud Guiovanna": "Arnaud Guiovanna",
        }
        for line, want in cases.items():
            with self.subTest(line=line):
                self.assertEqual(rr.extract_holder(line), want)

    def test_holder_whose_name_begins_with_a_digit_survives(self):
        """`1EdTech` is the current name of IMS Global and is a real holder. A guard
        testing 'starts with a digit' rather than 'is ONLY digits' would drop it."""
        self.assertEqual(rr.extract_holder("Copyright (c) 2023 1EdTech Consortium"),
                         "1EdTech Consortium")

    def test_steward_only_notice_is_not_a_holder_of_the_row(self):
        """The FSF's copyright on the GPL text is licence apparatus, not ownership."""
        holder = rr.extract_holder("Copyright (C) 2007 Free Software Foundation, Inc.")
        self.assertIsNotNone(holder)
        self.assertTrue(hh.is_steward(holder))


class TestTemplateDetection(unittest.TestCase):
    """An unfilled appendix is a distinct state from a missing one: the project put the
    placeholder in and never replaced it. Three of the five rows are in this state."""

    def test_apache_appendix_template(self):
        self.assertTrue(rr.TEMPLATE_HOLDER.search(
            "   Copyright [yyyy] [name of copyright owner]"))

    def test_gpl_how_to_apply_template(self):
        self.assertTrue(rr.TEMPLATE_HOLDER.search(
            "    Copyright (C) <year>  <name of author>"))

    def test_gpl_brace_template(self):
        self.assertTrue(rr.TEMPLATE_HOLDER.search(
            "    Copyright (C) {year}  {name of author}"))

    def test_a_filled_appendix_is_not_a_template(self):
        self.assertIsNone(rr.TEMPLATE_HOLDER.search(
            "   Copyright 2024-2026 Crosstalk Solutions LLC"))

    def test_a_filled_gpl_example_is_not_a_template(self):
        """`adapt_framework` fills the GPL's interactive-mode example rather than the
        appendix: `adapt_framework  Copyright (C) 2013  ADAPT LEARNING`."""
        self.assertIsNone(rr.TEMPLATE_HOLDER.search(
            "    adapt_framework  Copyright (C) 2013  ADAPT LEARNING"))


class TestNamelessPattern(unittest.TestCase):
    def test_year_shapes_match(self):
        for s in ("2024", "2013-2015", "2020, 2021", "1999", "2024.", " 2024 ",
                  "2013–2015"):
            with self.subTest(s=s):
                self.assertTrue(rr.NAMELESS.match(s.strip()))

    def test_names_do_not_match(self):
        for s in ("edX", "1EdTech Consortium", "Crosstalk Solutions LLC",
                  "Tim Branyen, contributors", "ADAPT LEARNING", "3M Company"):
            with self.subTest(s=s):
                self.assertFalse(rr.NAMELESS.match(s.strip()))


if __name__ == "__main__":
    unittest.main(verbosity=2)
