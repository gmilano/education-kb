#!/usr/bin/env python3
"""Offline controls for `p309-affero-rung-census`.

Every false-positive class below is one THIS INSTRUMENT'S OWN FIRST DRAFT
published, in the order it published them: 36 flags, then 25, then 16, then the
dynamic arm, which found 2.  A suppression nobody can see is a suppression the
next pass re-discovers, so each is a named control.

🔵 The positive controls are the two real payloads, pinned by byte length and
`sha256_12`.  If a later pass "simplifies" the title read back into a body search,
`NaivePatternIsStillWrong` and the dynamic arm both go red.
"""
import hashlib
import io
import os
import re
import sys
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "..", "p150-gpl-affero-discrimination"))

import fixtures as FX                                               # noqa: E402
import rung_census as RC                                           # noqa: E402
from gpl_affero import title_licence                                # noqa: E402

FIX = os.path.join(HERE, "fixtures")


def read(prefix):
    return FX.body(prefix)


def raw(prefix):
    return FX.raw(prefix)


class FixturesArePinned(unittest.TestCase):
    """A fixture whose bytes drift is a control that proves nothing."""

    def test_every_fixture_matches_its_probed_length_and_digest(self):
        # 🔵 The pins live in `fixtures.py`, which owns them for all three arms.
        self.assertEqual(FX.verify(), [])
        self.assertEqual(len(FX.PINS), 4)

    def test_a_prefix_resolves_to_exactly_one_payload(self):
        self.assertTrue(os.path.isfile(FX.resolve(FX.GPL3)))
        with self.assertRaises(LookupError):
            FX.resolve("no-such-payload-")

    def test_the_gpl3_fixture_names_affero_exactly_where_p308_recorded_it(self):
        # p308 measured lines 552/556/559 on a 35 148 B payload; this is an
        # INDEPENDENT 35 191 B payload and the line numbers agree.
        lines = read(FX.GPL3).splitlines()
        hits = [i + 1 for i, l in enumerate(lines) if re.search("affero", l, re.I)]
        self.assertEqual(hits, [552, 556, 559])

    def test_section_13_of_gpl3_is_titled_with_the_affero_name(self):
        lines = read(FX.GPL3).splitlines()
        self.assertIn("Use with the GNU Affero General Public License", lines[551])


class NaivePatternIsStillWrong(unittest.TestCase):
    """The negative control: the refuted rung, kept runnable so it stays refuted."""

    def test_a_body_search_for_affero_fires_on_both_gpl3_payloads(self):
        for name in (FX.GPL3,
                     FX.GPL3_SECOND):
            self.assertIn("affero", read(name).lower())

    def test_p150s_own_naive_pattern_fires_on_gpl3(self):
        from gpl_affero import NAIVE_AGPL
        self.assertIsNotNone(NAIVE_AGPL.search(read(FX.GPL3)))

    def test_the_title_read_does_not(self):
        self.assertEqual(title_licence(read(FX.GPL3)), "GPL")
        self.assertEqual(title_licence(read(FX.GPL3_SECOND)), "GPL")
        self.assertEqual(title_licence(read(FX.AGPL3)), "AGPL-3.0")


class RungGrading(unittest.TestCase):
    def setUp(self):
        self.gpl3 = read(FX.GPL3)
        self.agpl3 = read(FX.AGPL3)

    def test_a_casefolded_phrase_fires_on_gpl3_only_when_folded(self):
        self.assertEqual(RC.grade_rung("GNU AFFERO GENERAL PUBLIC LICENSE",
                                       self.gpl3, self.agpl3),
                         "FIRES-ON-GPL3-CASEFOLD")

    def test_a_bare_lowercase_token_only_fires_when_folded(self):
        # 🟡 The control's own first expectation was EXACT and that was wrong:
        # GPL-3.0 spells the name `Affero`, title-case, so a lowercase token needs
        # the fold.  Measured, not assumed.
        self.assertEqual(RC.grade_rung("affero", self.gpl3, self.agpl3),
                         "FIRES-ON-GPL3-CASEFOLD")

    def test_the_title_cased_name_fires_case_sensitively(self):
        self.assertEqual(RC.grade_rung("Affero General Public License",
                                       self.gpl3, self.agpl3),
                         "FIRES-ON-GPL3-EXACT")

    def test_the_version_after_the_name_is_agpl_only(self):
        # 🟢 Measured, against the reading that condemns it: GPL-3.0 §13 writes
        # "version 3 of the GNU Affero General Public License" — version BEFORE
        # name — so this rung never fires on GPL-3.0.  Four files carry it.
        self.assertEqual(
            RC.grade_rung(r"gnu\s+affero\s+general\s+public\s+license[\s,]*version\s*3",
                          self.gpl3, self.agpl3),
            "AGPL-ONLY")

    def test_an_unrelated_token_is_inert(self):
        self.assertEqual(RC.grade_rung("affero-labs-internal", self.gpl3, self.agpl3),
                         "INERT")


class LabelDiscrimination(unittest.TestCase):
    def test_the_section_13_pattern_is_the_discriminator_not_a_defect(self):
        self.assertEqual(
            RC.label_class(["AGPL-3.0"], r"13\.\s*Use\s+with\s+the\s+GNU\s+Affero"),
            "DISCRIMINATOR")

    def test_a_family_matcher_is_graded_by_its_pattern_not_its_neighbours(self):
        self.assertEqual(
            RC.label_class(["AGPL-3.0"],
                           r"GNU\s+(?:Affero\s+General\s+Public|Lesser\s+General\s+Public"
                           r"|General\s+Public)\s+Licen[cs]e"),
            "FAMILY-BY-PATTERN")

    def test_an_agpl_label_beside_an_agpl_rung_is_agpl_specific(self):
        self.assertEqual(RC.label_class(["AGPL-3.0"], "gnu affero general public license"),
                         "AGPL-SPECIFIC")

    def test_a_ladder_carrying_both_labels_is_a_ladder(self):
        self.assertEqual(
            RC.label_class(["AGPL-3.0", "GPL-3.0"], "GNU AFFERO GENERAL PUBLIC LICENSE"),
            "AGPL-AMONG-FAMILY")

    def test_the_agpls_full_name_used_as_a_label_is_agpl_specific(self):
        self.assertEqual(RC.label_class(["GNU Affero General Public License"],
                                        "gnu affero"), "AGPL-SPECIFIC")

    def test_a_nearby_literal_that_is_the_rung_itself_is_not_its_label(self):
        self.assertEqual(RC.label_class(["gnu affero"], "gnu affero"), "UNLABELLED")


class LadderOrderScope(unittest.TestCase):
    """🔴 The bug that made 27 files read `LADDER-NO-GPL-RUNG`: the order check was
    handed the AFFERO-bearing literals only, so a plain GPL rung could never be in
    it.  The rule was right and the SCOPE was wrong."""

    def test_a_plain_gpl_rung_is_found_among_all_literals(self):
        lits = [(10, "gnu affero general public license"),
                (11, "gnu general public license")]
        self.assertEqual(RC.gpl_rung_lines(lits), [11])

    def test_an_affero_literal_is_never_counted_as_the_gpl_rung(self):
        self.assertEqual(RC.gpl_rung_lines([(10, "gnu affero general public")]), [])

    def test_a_long_prose_literal_is_not_a_rung(self):
        prose = ("GPL-3.0 section 13 is titled Use with the GNU Affero General Public "
                 "License. That is why a body search misgrades it, and this sentence "
                 "is documentation rather than a pattern a caller compiles.")
        self.assertTrue(RC.is_prose(prose))
        self.assertFalse(RC.is_prose("gnu affero general public license"))


class FileVerdicts(unittest.TestCase):
    def row(self, graded, casefolds=True, imports=False, lits=(), windowed=False):
        return ("f.py", "OK", graded, casefolds, imports, list(lits), windowed)

    def test_importing_the_discriminator_closes_the_question(self):
        self.assertEqual(
            RC.verdict(self.row([(1, "affero", "FIRES-ON-GPL3-EXACT", "AGPL-SPECIFIC")],
                                imports=True)),
            "IMPORTS-DISCRIMINATOR")

    def test_an_agpl_specific_unwindowed_rung_is_the_defect(self):
        self.assertEqual(
            RC.verdict(self.row([(1, "affero general public license",
                                  "FIRES-ON-GPL3-CASEFOLD", "AGPL-SPECIFIC")])),
            "MISGRADES-GPL3-AS-AGPL")

    def test_the_same_rung_in_a_windowed_file_is_a_read_not_a_finding(self):
        self.assertEqual(
            RC.verdict(self.row([(1, "affero general public license",
                                  "FIRES-ON-GPL3-CASEFOLD", "AGPL-SPECIFIC")],
                                windowed=True)),
            "MISGRADES-ONLY-IF-UNWINDOWED")

    def test_a_casefold_rung_in_a_file_that_never_folds_is_only_exposure(self):
        self.assertEqual(
            RC.verdict(self.row([(1, "GNU AFFERO GENERAL PUBLIC LICENSE",
                                  "FIRES-ON-GPL3-CASEFOLD", "AGPL-SPECIFIC")],
                                casefolds=False)),
            "EXPOSED-IF-CASEFOLDED")

    def test_ladder_order_decides_a_two_rung_file(self):
        graded = [(10, "GNU AFFERO GENERAL PUBLIC LICENSE",
                   "FIRES-ON-GPL3-CASEFOLD", "AGPL-AMONG-FAMILY")]
        first = self.row(graded, lits=[(10, "GNU AFFERO GENERAL PUBLIC LICENSE"),
                                       (11, "GNU GENERAL PUBLIC LICENSE")])
        self.assertEqual(RC.verdict(first), "LADDER-AGPL-RUNG-FIRST")
        graded2 = [(12, "GNU AFFERO GENERAL PUBLIC LICENSE",
                    "FIRES-ON-GPL3-CASEFOLD", "AGPL-AMONG-FAMILY")]
        second = self.row(graded2, lits=[(11, "GNU GENERAL PUBLIC LICENSE"),
                                         (12, "GNU AFFERO GENERAL PUBLIC LICENSE")])
        self.assertEqual(RC.verdict(second), "LADDER-GPL-RUNG-FIRST")

    def test_a_file_with_no_rung_is_not_a_verdict(self):
        self.assertEqual(RC.verdict(self.row([])), "NO-RUNG")


class DrivingRungIsTheEvidence(unittest.TestCase):
    """🔴 The first report printed the file's first GPL3-firing rung, which showed
    `p228`'s §13 DISCRIMINATOR beside a verdict a different rung had produced."""

    def test_the_rung_named_is_the_rung_that_decided(self):
        graded = [(29, "GNU AFFERO GENERAL PUBLIC LICENSE",
                   "FIRES-ON-GPL3-CASEFOLD", "AGPL-AMONG-FAMILY"),
                  (65, r"13\.\s*Use\s+with\s+the\s+GNU\s+Affero",
                   "FIRES-ON-GPL3-EXACT", "DISCRIMINATOR")]
        row = ("p228.py", "OK", graded, True, False,
               [(29, "x"), (70, "GNU GENERAL PUBLIC LICENSE")], False)
        self.assertEqual(RC.driving_rung(row, "LADDER-AGPL-RUNG-FIRST")[0], 29)


class AstExtraction(unittest.TestCase):
    def test_a_comment_is_not_a_literal(self):
        self.assertEqual(RC.affero_literals("# affero general public license\nx = 1\n"), [])

    def test_a_string_literal_is(self):
        got = RC.affero_literals('PAT = "gnu affero general public"\n')
        self.assertEqual([g[1] for g in got], ["gnu affero general public"])

    def test_an_unparseable_file_is_reported_not_skipped(self):
        self.assertIsNone(RC.affero_literals("def (:\n"))


class ProberComposesFamilyAndVersion(unittest.TestCase):
    """The fix this pass shipped, graded end to end on real bytes."""

    def load(self, rel, fn):
        import importlib.util
        path = os.path.normpath(os.path.join(HERE, "..", rel))
        sys.path.insert(0, os.path.dirname(path))
        try:
            spec = importlib.util.spec_from_file_location("t309_" + fn, path)
            mod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(mod)
            return getattr(mod, fn)
        finally:
            sys.path.pop(0)

    def test_the_prober_separates_gpl3_from_agpl3_with_versions(self):
        classify = self.load("p306-licence-probe/licence_probe.py", "classify")
        self.assertEqual(classify(read(FX.GPL3)),
                         ("GRANT", "GPL-3.0"))
        self.assertEqual(classify(read(FX.GPL3_SECOND)),
                         ("GRANT", "GPL-3.0"))
        self.assertEqual(classify(read(FX.AGPL3)),
                         ("GRANT", "AGPL-3.0"))

    def test_the_spec_sweep_separates_them_too(self):
        classify = self.load("p191-spec-license-sweep/classify_spec.py", "classify")
        self.assertEqual(classify(read(FX.GPL3))[1], "GPL-3.0")
        self.assertEqual(classify(read(FX.AGPL3))[1], "AGPL-3.0")

    def test_the_cc_content_payload_is_still_unresolved_and_says_so(self):
        # 🟡 `GarethManning/education-agent-skills`, 877★, 1 230 B: a CC BY-SA 4.0
        # grant by reference.  The prober returns NO-GRANT-CLAUSE, which is
        # `ACTION p306-R` item 2's POINTER class, still open.  Pinned here so the
        # gap cannot be mistaken for a reserved grant.
        classify = self.load("p306-licence-probe/licence_probe.py", "classify")
        verdict, fam = classify(read(FX.CC_POINTER))
        self.assertEqual(verdict, "NO-GRANT-CLAUSE")
        self.assertIn("Attribution-ShareAlike",
                      read(FX.CC_POINTER))


class BothDirections(unittest.TestCase):
    def test_gpl_read_as_agpl_is_a_defect(self):
        self.assertEqual(RC_grade("AGPL-3.0", "AGPL-3.0"), "DEFECT-GPL3-READ-AS-AGPL")

    def test_agpl_read_as_gpl_is_also_a_defect(self):
        self.assertEqual(RC_grade("GPL-3.0", "GPL-3.0"), "DEFECT-AGPL3-READ-AS-GPL")

    def test_the_correct_pair_passes(self):
        self.assertEqual(RC_grade("GPL-3.0", "AGPL-3.0"), "CORRECT")


def RC_grade(a, b):
    import importlib.util
    spec = importlib.util.spec_from_file_location(
        "p309_runner", os.path.join(HERE, "run_classifiers.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.grade(a, b)


if __name__ == "__main__":
    unittest.main(verbosity=2)
