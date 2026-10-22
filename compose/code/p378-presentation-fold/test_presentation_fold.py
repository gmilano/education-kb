#!/usr/bin/env python3
"""p378 -- controls for `ACTION p377-B`'s instrument.

Every control names a payload this pass read FIRST-HAND, or a p312 fixture already on these
shelves.  No fixture here was invented to make a suite pass: the two that matter most are the
negative controls, because an instrument that folds presentations is one bad regex away from
folding LICENCES.
"""
import os
import sys
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "..", "p312-template-identity"))

import presentation_fold as pf  # noqa: E402
import template_identity as ti  # noqa: E402

FIX = os.path.join(HERE, "..", "p312-template-identity", "fixtures")
EVID = os.path.join(HERE, "..", "..", "..", "evidence")


def fixture(name):
    with open(os.path.join(FIX, name), "rb") as fh:
        return fh.read().decode("utf-8", "replace")


def pinned(name):
    with open(os.path.join(EVID, name), "rb") as fh:
        return fh.read().decode("utf-8", "replace")


# The three MIT template digests p312 carries, by the fixture that produced each.
CANONICAL = "mit-mural-1066.LICENSE"            # 16d6b7b5799875f6, 8 payloads at p377
UNTITLED = "mit-lti-issuer-1076.LICENSE"        # 7768d3beb7949a85, p376-C's pin
PAREN = "mitparen-typed-japanese-1086.LICENSE"  # d936246a542832f3


class TheFindingItself(unittest.TestCase):
    """p377 published three MIT templates.  These controls assert there is ONE text."""

    def test_untitled_variant_is_the_canonical_text(self):
        # 🔴 This is p377's "THIRD distinct MIT template".  It is the same words.
        self.assertTrue(pf.same_text(fixture(UNTITLED), fixture(CANONICAL)))

    def test_paren_variant_is_the_canonical_text(self):
        # d936246a542832f3 differs by its title line alone: "The MIT License (MIT)".
        self.assertTrue(pf.same_text(fixture(PAREN), fixture(CANONICAL)))

    def test_p312_still_sees_three_distinct_templates(self):
        # 🔵 The disagreement IS the measurement.  If this control ever goes green the other
        # way, someone has edited p312's normalise() and every published digest has re-keyed.
        digests = {ti.template_digest(fixture(n)) for n in (CANONICAL, UNTITLED, PAREN)}
        self.assertEqual(len(digests), 3)

    def test_the_census_names_the_inflation(self):
        payloads = {n: fixture(n) for n in (CANONICAL, UNTITLED, PAREN)}
        c = pf.census(payloads, ti.template_digest)
        self.assertEqual(c["texts"], 1)
        self.assertEqual(c["template_digests"], 3)
        self.assertEqual(c["inflation"], 2)

    def test_every_mit_fixture_on_the_shelves_is_one_text(self):
        # All ten p312 MIT fixtures, not a chosen three.
        names = [n for n in sorted(os.listdir(FIX)) if n.startswith(("mit-", "mitparen-"))]
        self.assertEqual(len(names), 10, "fixture set changed: re-derive this control")
        self.assertEqual(len(pf.group({n: fixture(n) for n in names})), 1)


class NegativeControlsLicencesMustNotFold(unittest.TestCase):
    """🔴 The failure mode that would make this instrument worse than no instrument."""

    def test_mit_does_not_fold_onto_apache(self):
        self.assertFalse(pf.same_text(fixture(CANONICAL),
                                      fixture("apache-2.0-edfi-data-standard-10173.LICENSE")))

    def test_mit_does_not_fold_onto_gpl(self):
        self.assertFalse(pf.same_text(fixture(CANONICAL),
                                      fixture("gpl-2.0-memento-18097.LICENSE")))

    def test_mit_does_not_fold_onto_bsd_2_clause(self):
        # 🔵 The sharpest pair available: BSD-2-Clause shares whole sentences with MIT and
        # its title form IS in TITLES, so a title-stripping bug would show up here first.
        self.assertFalse(pf.same_text(fixture(CANONICAL),
                                      fixture("bsd-2-clause-github2pandas-1340.LICENSE")))

    def test_the_137_byte_cc0_paraphrase_does_not_fold_onto_real_cc0(self):
        # 🔴 Read first-hand at 12britz/awesome-free-models this pass: three lines that
        # PARAPHRASE CC0 and carry none of its operative sections.  Both payloads are pinned
        # in evidence/ so this control reads bytes, not a description of bytes.
        self.assertFalse(pf.same_text(
            pinned("cc0-paraphrase-137.2026-10-22-p378.LICENSE"),
            pinned("cc0-statement-of-purpose-5875.2026-10-22-p378.LICENSE")))

    def test_the_two_real_cc0_shapes_are_also_different_texts(self):
        # CC0's Statement of Purpose alone (5 875 B) vs the full Legal Code with the
        # Creative Commons preamble (7 048 B).  Same LICENCE, different DOCUMENTS -- so the
        # fold must keep them apart too, and this base must never read "one text" as "one
        # licence".  Both payloads pinned in evidence/ this pass; the control reads bytes.
        self.assertFalse(pf.same_text(
            pinned("cc0-statement-of-purpose-5875.2026-10-22-p378.LICENSE"),
            pinned("cc0-legal-code-7048.2026-10-22-p378.LICENSE")))

    def test_the_paraphrase_does_not_fold_onto_the_full_legal_code_either(self):
        # The 137-byte paraphrase against the OTHER real CC0 shape, so the paraphrase is
        # refused against both and not merely against the one it happened to be read beside.
        self.assertFalse(pf.same_text(
            pinned("cc0-paraphrase-137.2026-10-22-p378.LICENSE"),
            pinned("cc0-legal-code-7048.2026-10-22-p378.LICENSE")))


class TitleStrippingIsClosedAndSafe(unittest.TestCase):
    def test_operative_first_line_survives_the_fold(self):
        # 🔴 The untitled payload opens on a COPYRIGHT line, not a title.  A wildcard
        # "strip the first line" would delete it and this control is why there is a list.
        text, title = pf.strip_title(fixture(UNTITLED))
        self.assertIsNone(title)
        self.assertIn("Copyright 2020 Center for 21st Century Universities", text)

    def test_a_title_form_not_in_the_list_is_left_alone(self):
        text, title = pf.strip_title("Mozilla Public License 2.0\n\nbody here\n")
        self.assertIsNone(title)
        self.assertIn("Mozilla Public License 2.0", text)

    def test_only_the_first_non_empty_line_is_eligible(self):
        # A later occurrence of a title string is body text and must not be removed.
        text, title = pf.strip_title("Copyright (c) x\n\nMIT License\n")
        self.assertIsNone(title)
        self.assertIn("MIT License", text)

    def test_leading_blank_lines_do_not_hide_a_title(self):
        text, title = pf.strip_title("\n\n  MIT License  \n\nbody\n")
        self.assertEqual(title, "MIT License")
        self.assertNotIn("MIT License", text)

    def test_title_match_is_case_insensitive_but_whole_line(self):
        self.assertEqual(pf.strip_title("mit license\nbody\n")[1], "MIT License")
        self.assertIsNone(pf.strip_title("MIT License and other terms\nbody\n")[1])


class FoldMechanics(unittest.TestCase):
    def test_rewrapping_alone_folds(self):
        wrapped = "MIT License\n\nPermission is hereby\ngranted to any person\n"
        flat = "MIT License\n\nPermission is hereby granted to any person\n"
        self.assertTrue(pf.same_text(wrapped, flat))

    def test_a_single_changed_word_does_not_fold(self):
        # 🔵 The fold must be blind to WRAPPING and nothing else.
        a = "MIT License\n\nPermission is hereby granted\n"
        b = "MIT License\n\nPermission is NOT granted\n"
        self.assertFalse(pf.same_text(a, b))

    def test_tabs_and_crlf_are_whitespace(self):
        self.assertTrue(pf.same_text("MIT License\r\n\r\na\tb\n", "MIT License\n\na b\n"))

    def test_empty_input_folds_to_empty_and_is_not_equal_to_a_grant(self):
        # P541's class: an empty input must not quietly equal something.
        self.assertEqual(pf.fold(""), "")
        self.assertFalse(pf.same_text("", fixture(CANONICAL)))

    def test_whitespace_only_input_is_not_a_grant(self):
        self.assertFalse(pf.same_text("   \n\t\n", fixture(CANONICAL)))

    def test_digest_is_stable_across_calls(self):
        t = fixture(CANONICAL)
        self.assertEqual(pf.presentation_digest(t), pf.presentation_digest(t))


class AgreementWithTheDrawThisPassMade(unittest.TestCase):
    def test_the_published_fold_digest_is_what_the_instrument_derives(self):
        # 🟢 evidence/mit-presentation-fold.2026-10-22-p378.tsv publishes
        # 584db484c03a8904 as the folded digest of the MIT text.  A figure published in
        # prose and never re-derived is the class p352 built a whole gate for.
        self.assertEqual(pf.presentation_digest(fixture(CANONICAL))[:16], "584db484c03a8904")
        self.assertEqual(pf.presentation_digest(fixture(UNTITLED))[:16], "584db484c03a8904")
        self.assertEqual(pf.presentation_digest(fixture(PAREN))[:16], "584db484c03a8904")

    def test_the_folded_text_length_published_is_right(self):
        self.assertEqual(len(pf.fold(fixture(UNTITLED))), 1043)


if __name__ == "__main__":
    unittest.main(verbosity=0)
