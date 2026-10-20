"""Offline controls for `p341-bespoke-instrument-census`.

No network, no clock.  Every fixture is a payload read first-hand — the two in
this directory at `p341` over `raw.githubusercontent.com`, the rest pinned by
`pass257`, `p312` and `lib/` in earlier passes and REFERENCED here rather than
copied.  🔵 Copying them would create a second source of truth for a byte count
three suites already assert, which is the defect `p308` named.
"""

import os
import sys
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
CODE = os.path.dirname(HERE)
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(CODE, "pass257-restriction-scan"))
sys.path.insert(0, os.path.join(CODE, "p312-template-identity"))

import bespoke_census as bc          # noqa: E402
import restriction_scan as p257      # noqa: E402
import template_identity as p312     # noqa: E402

FIX = os.path.join(HERE, "fixtures")
P257FIX = os.path.join(CODE, "pass257-restriction-scan", "fixtures-p257")
P312FIX = os.path.join(CODE, "p312-template-identity", "fixtures")
LIBFIX = os.path.join(CODE, "lib")


def read(path):
    with open(path, "rb") as fh:
        return fh.read().decode("utf-8", "replace")


ASTHETECH = os.path.join(FIX, "bespoke-asthetech-6489.LICENSE")
GRASPFUL = os.path.join(FIX, "bespoke-rider-graspful-1439.LICENSE")
MIT = os.path.join(P257FIX, "mit-1091.txt")
MIT_UNTITLED = os.path.join(P257FIX, "mit-untitled-1057.txt")
APACHE = os.path.join(P257FIX, "apache-2.0-11356.txt")
GPL3 = os.path.join(P257FIX, "gpl-3.0-35146.txt")
USC = os.path.join(P257FIX, "usc-academic-1812.txt")
RAPKUMER = os.path.join(P257FIX, "rapkumer-id-3140.txt")
GAOKAO = os.path.join(P257FIX, "opengaokao-zh-15992.txt")
UCHICAGO = os.path.join(
    LIBFIX, "fixtures-p990",
    "noncommercial-uchicago-student-early-warning.LICENSE")

ALL_FIXTURES = [ASTHETECH, GRASPFUL, MIT, MIT_UNTITLED, APACHE, GPL3, USC,
                RAPKUMER, GAOKAO, UCHICAGO]


class TestFixturesArePinnedByteExact(unittest.TestCase):
    """The two payloads this pass added are pinned at the bytes it measured."""

    def test_asthetech_is_6489_bytes(self):
        self.assertEqual(os.path.getsize(ASTHETECH), 6489)

    def test_graspful_is_1439_bytes(self):
        self.assertEqual(os.path.getsize(GRASPFUL), 1439)

    def test_every_referenced_fixture_exists(self):
        for p in ALL_FIXTURES:
            self.assertTrue(os.path.exists(p), p)


class TestNoWindowDrift(unittest.TestCase):
    """The SPDX limb reads the title over `pass257`'s window, not a copy of it."""

    def test_title_lines_is_not_a_second_constant(self):
        self.assertEqual(bc.TITLE_LINES, p257.TITLE_LINES)

    def test_anchor_vocabulary_is_pass257s_object(self):
        # Not `==` against a transcription: the SAME tuple object.
        self.assertIs(
            bc.titled_family.__globals__["p257"].TITLE_ANCHORS,
            p257.TITLE_ANCHORS)


class TestSpdxTitledStock(unittest.TestCase):
    """A verbatim stock text, titled, is stock — including copyleft."""

    def test_mit_is_spdx_titled_and_stock(self):
        t = read(MIT)
        self.assertEqual(bc.title_form(t), bc.SPDX_TITLED)
        self.assertEqual(bc.titled_family(t), "MIT")
        self.assertTrue(bc.is_stock(t))
        self.assertFalse(bc.needs_a_human(t))

    def test_apache_is_spdx_titled_and_stock(self):
        t = read(APACHE)
        self.assertEqual(bc.title_form(t), bc.SPDX_TITLED)
        self.assertTrue(bc.is_stock(t))

    def test_verbatim_gpl3_is_stock_despite_noncommercially(self):
        """`P171`/pass-15's trap, inherited rather than re-fought.

        GPL-3.0 §6 contains `noncommercially`.  `pass257.BENIGN_FAMILY_HITS`
        already absorbs it, so this census must grade a verbatim GPL-3.0 payload
        STOCK and must NOT send it to a human.
        """
        t = read(GPL3)
        self.assertEqual(bc.title_form(t), bc.SPDX_TITLED)
        self.assertTrue(bc.is_stock(t))
        self.assertFalse(bc.needs_a_human(t))
        g = bc.grade(t)
        self.assertEqual(g["effective_hits"], ())
        self.assertIn("noncommercial", g["benign_hits"])


class TestTheUntitledClassIsNotTheBespokeClass(unittest.TestCase):
    """`p314`'s class, kept separate — the control that makes the census mean something."""

    def test_untitled_verbatim_mit_is_untitled_not_bespoke(self):
        t = read(MIT_UNTITLED)
        self.assertEqual(bc.title_form(t), bc.UNTITLED)
        self.assertNotEqual(bc.title_form(t), bc.BESPOKE_TITLED)

    def test_untitled_verbatim_mit_is_not_sent_to_a_human(self):
        """A real MIT grant with no title line is a dependency to TAKE.

        🔵 It is not `stock` under this census's conjunction — the title makes
        no claim — but flagging it for a human would be the other defect
        `pass257` named: a usable grant declined for no reason.
        """
        t = read(MIT_UNTITLED)
        self.assertFalse(bc.is_stock(t))
        self.assertFalse(bc.needs_a_human(t))

    def test_its_family_is_found_on_the_body_channel(self):
        g = bc.grade(read(MIT_UNTITLED))
        self.assertEqual(g["scan_family"], "MIT")
        self.assertIsNone(g["titled_family"])
        self.assertEqual(g["family_channel"], "BODY")


class TestBespokeTitled(unittest.TestCase):
    """The class T29 asked for a census of."""

    def test_asthetech_is_bespoke_titled_and_restricted(self):
        t = read(ASTHETECH)
        self.assertEqual(bc.title_form(t), bc.BESPOKE_TITLED)
        self.assertIsNone(bc.titled_family(t))
        self.assertEqual(bc.grade(t)["scan_verdict"],
                         p257.VERDICT_RESTRICTED)
        self.assertTrue(bc.needs_a_human(t))
        self.assertFalse(bc.is_stock(t))

    def test_asthetech_forbids_the_thing_a_consultancy_sells(self):
        g = bc.grade(read(ASTHETECH))
        self.assertIn("saas", g["effective_hits"])
        self.assertIn("non-commercial", g["effective_hits"])

    def test_bespoke_instruments_in_three_languages(self):
        for p, fam in ((RAPKUMER, None), (GAOKAO, None)):
            t = read(p)
            self.assertEqual(bc.title_form(t), bc.BESPOKE_TITLED, p)
            self.assertEqual(bc.titled_family(t), fam, p)
            self.assertTrue(bc.needs_a_human(t), p)


class TestTheRiderIsTheExpensiveRow(unittest.TestCase):
    """`graspful`: a bespoke title over a body that recites MIT word for word."""

    def test_graspful_body_reads_mit_on_the_body_channel(self):
        g = bc.grade(read(GRASPFUL))
        self.assertEqual(g["scan_family"], "MIT")
        self.assertEqual(g["family_channel"], "BODY")

    def test_but_its_title_is_bespoke(self):
        self.assertEqual(bc.title_form(read(GRASPFUL)), bc.BESPOKE_TITLED)
        self.assertIsNone(bc.titled_family(read(GRASPFUL)))

    def test_and_it_is_neither_stock_nor_clearable(self):
        t = read(GRASPFUL)
        self.assertFalse(bc.is_stock(t))
        self.assertTrue(bc.needs_a_human(t))
        self.assertEqual(bc.grade(t)["scan_verdict"], p257.VERDICT_FAMILY_PLUS)

    def test_a_bare_family_read_would_have_published_it_as_mit(self):
        """The live defect this census exists to catch, asserted not argued.

        `lib/license_family.sh` — the classifier `probe_repo` uses to fill the
        family column of every shelf row — returns `MIT` for this payload, and
        `probe_repo` returned exactly that at `p341`.  A family column alone
        cannot carry this row; the title form can.
        """
        t = read(GRASPFUL)
        self.assertEqual(p257.family_of(t), "MIT")
        self.assertFalse(p257.is_usable_permissive(t))
        self.assertTrue(bc.needs_a_human(t))


class TestTheTitleShapeRepair(unittest.TestCase):
    """Regression controls for the false positive measured at `p341`."""

    def test_usc_academic_is_untitled_not_bespoke_titled(self):
        """Bare `agreement` over a 4-line window typed this BESPOKE-TITLED.

        Its second line reads "… without a written agreement is hereby
        granted".  That is body prose, not a title.
        """
        t = read(USC)
        self.assertEqual(bc.title_form(t), bc.UNTITLED)

    def test_usc_academic_is_still_sent_to_a_human(self):
        """The repair must not lose the row — only its REASON changes."""
        self.assertTrue(bc.needs_a_human(read(USC)))

    def test_bare_agreement_is_not_an_instrument_word(self):
        self.assertNotIn("agreement", bc._INSTRUMENT_WORDS)

    def test_uchicago_prose_preamble_is_not_a_title(self):
        t = read(UCHICAGO)
        self.assertEqual(bc.title_form(t), bc.UNTITLED)
        self.assertTrue(bc.needs_a_human(t))

    def test_no_pinned_title_sits_near_the_threshold(self):
        """A constant with a fixture ON it is a constant that will move."""
        titled = []
        for p in (MIT, APACHE, GPL3, ASTHETECH, GRASPFUL, RAPKUMER, GAOKAO):
            lines = bc.title_lines(read(p))
            self.assertTrue(lines, p)
            titled.append(len(bc._DECORATION.sub("", lines[0]).encode("utf-8")))
        self.assertLessEqual(max(titled), bc.TITLE_MAX_BYTES - 15)

    def test_markdown_heading_decoration_does_not_hide_a_title(self):
        self.assertEqual(bc.title_form("# MIT License\n\nblah"), bc.SPDX_TITLED)
        self.assertEqual(
            bc.title_form("## Acme Community License\n\nblah"),
            bc.BESPOKE_TITLED)


class TestP312IsNotABespokeDetector(unittest.TestCase):
    """Measured, because reading `UNKNOWN-TEMPLATE` as "bespoke" is the trap.

    🔴 `p312.identify` returns `UNKNOWN-TEMPLATE` for any payload outside its
    fixture-derived registry.  If that answer were taken as "bespoke", verbatim
    stock texts would be reported bespoke — which is `p310`'s byte-band error in
    a new costume.  These controls pin the DIVERGENCE so no later pass wires
    `p312` into this census by mistake.
    """

    # 🔴 The first draft of this class asked `p312` about `p312`'s OWN fixtures
    # and asserted some would be unknown to it.  They are all known, necessarily:
    # `_register_from_fixtures` DERIVES the registry from exactly those files.
    # The control was measuring the tautology instead of the divergence, and it
    # failed on the first run — which is the only reason it is right now.
    # The population has to be stock payloads p312 does NOT own.
    EXTERNAL_STOCK = (("apache-2.0-11356", APACHE), ("gpl-3.0-35146", GPL3))

    def test_verbatim_stock_texts_are_unknown_to_p312(self):
        """Both are verbatim stock licences, read first-hand by `pass257`."""
        for name, path in self.EXTERNAL_STOCK:
            self.assertEqual(p312.identify(read(path))[0], "UNKNOWN-TEMPLATE",
                             name)

    def test_this_census_grades_those_same_payloads_stock(self):
        for name, path in self.EXTERNAL_STOCK:
            self.assertTrue(bc.is_stock(read(path)), name)
            self.assertFalse(bc.needs_a_human(read(path)), name)

    def test_so_unknown_template_must_never_be_read_as_bespoke(self):
        """The divergence, stated as the invariant a later pass could break."""
        for name, path in self.EXTERNAL_STOCK:
            t = read(path)
            self.assertEqual(p312.identify(t)[0], "UNKNOWN-TEMPLATE", name)
            self.assertNotEqual(bc.title_form(t), bc.BESPOKE_TITLED, name)

    def test_p312_can_name_what_it_owns_so_the_divergence_is_not_blanket(self):
        """A negative control for the negative control: p312 is not useless here.

        🔵 It answers correctly whenever it answers at all — the objection is
        only to reading its ABSTENTION as a classification.
        """
        self.assertEqual(p312.identify(read(MIT))[0], "MIT")


class TestTotality(unittest.TestCase):
    """Every payload gets exactly one form, and the census reports names."""

    def test_title_form_is_total_over_every_fixture(self):
        for p in ALL_FIXTURES:
            self.assertIn(bc.title_form(read(p)), bc.TITLE_FORMS, p)

    def test_grade_never_omits_a_field(self):
        keys = set(bc.grade(read(MIT)))
        for p in ALL_FIXTURES:
            self.assertEqual(set(bc.grade(read(p))), keys, p)

    def test_census_returns_the_population_not_only_counts(self):
        rows = [(os.path.basename(p), read(p)) for p in ALL_FIXTURES]
        c = bc.census(rows)
        self.assertEqual(c["n"], len(rows))
        self.assertEqual(
            sum(len(v) for v in c["by_title_form"].values()), len(rows))
        self.assertIn("bespoke-asthetech-6489.LICENSE", c["needs_a_human"])
        self.assertIn("mit-1091.txt", c["stock"])
        # p275: a count whose population cannot be re-checked is a ladder.
        for form, slugs in c["by_title_form"].items():
            for s in slugs:
                self.assertEqual(c["graded"][s]["title_form"], form)

    def test_stock_and_needs_a_human_are_disjoint(self):
        rows = [(os.path.basename(p), read(p)) for p in ALL_FIXTURES]
        c = bc.census(rows)
        self.assertEqual(set(c["stock"]) & set(c["needs_a_human"]), set())

    def test_tsv_row_has_one_cell_per_header_column(self):
        n = len(bc.tsv_header().split("\t"))
        for p in ALL_FIXTURES:
            row = bc.tsv_row(os.path.basename(p), bc.grade(read(p)))
            self.assertEqual(len(row.split("\t")), n, p)

    def test_no_tsv_cell_is_empty(self):
        """p277: a blank cell renders as a structural break, not as data."""
        for p in ALL_FIXTURES:
            for cell in bc.tsv_row(os.path.basename(p),
                                   bc.grade(read(p))).split("\t"):
                self.assertNotEqual(cell.strip(), "", p)


if __name__ == "__main__":
    unittest.main(verbosity=2)
