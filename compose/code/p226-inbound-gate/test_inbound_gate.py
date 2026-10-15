"""Controls for the p226 inbound gate.

A gate that reports 0 is worthless unless it is PROVEN able to report more than 0. These
controls are p225's own two inbound strings - the hazard that caused ACTION SH to be registered.
MUST-FIRE controls prove sensitivity; MUST-NOT-FIRE controls prove the gate is not a date grep.
"""

import os
import subprocess
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from inbound_gate import load_table, scan, split_records  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
EVID = os.path.abspath(os.path.join(HERE, "..", "..", "..", "evidence"))
TABLE_P224 = os.path.join(EVID, "sa-refuted-claims.2026-10-15-p224.tsv")
TABLE_P226 = os.path.join(EVID, "sh-refuted-claims.2026-10-15-p226.tsv")

# --- p225's two INBOUND strings, verbatim from p225-inbound-reassertion ---------------------
P225_EU = ('The EU AI Act treats education AI as high-risk, and that obligation takes effect '
           'in August 2026')
P225_BOSTON = ('Boston Public Schools recently became the first major US district to mandate AI '
               'fluency as a graduation requirement, starting in September 2026')

# --- this pass's own inbound text, which must NOT fire --------------------------------------
P226_EMEA_NEARMISS = (
    'EU AI Act: Sources agree it treats education AI as high-risk when it affects access, '
    'assessment, or exam scoring. The timing is unclear. One source says it entered into force '
    'in August 2024, and its general application date was 2 August 2026.')
P226_VIETNAM = (
    'Vietnam passed a standalone AI law that uses a risk-based classification. Education is '
    'named among high-risk sectors. One says it took effect on March 1, 2026.')
KB_CORRECT_FORM = (
    'Annex III education high-risk applies 2027-12-02 under Reg. (EU) 2026/1744; 2026-08-02 is '
    'Article 50 transparency, a different obligation.')
BOSTON_CORRECT_FORM = (
    'Boston Public Schools announced an AI literacy programme 2026-03-26 with UMass Boston and '
    'Paul English, USD 1M. It is a course, not a graduation requirement.')


def run(text, table):
    rows = load_table(table)
    return scan(split_records(text), rows)


class SensitivityP224Table(unittest.TestCase):
    """What the EXISTING 3-row table can and cannot do on inbound text."""

    def test_p225_eu_string_fires(self):
        hits, _ = run(P225_EU, TABLE_P224)
        self.assertEqual(len(hits), 1, "the gate must be live on p225's EU string")

    def test_p225_boston_string_does_not_fire(self):
        """THE COVERAGE GAP. Not a sensitivity failure - there is no Boston row to fire."""
        hits, _ = run(P225_BOSTON, TABLE_P224)
        self.assertEqual(len(hits), 0)


class SpecificityP224Table(unittest.TestCase):
    def test_p226_emea_nearmiss_does_not_fire(self):
        """'general application date was 2 August 2026' is TRUE of the Act as a whole."""
        hits, near = run(P226_EMEA_NEARMISS, TABLE_P224)
        self.assertEqual(len(hits), 0)
        self.assertEqual(len(near), 1, "but it must be REPORTED as a near miss, not silently passed")

    def test_vietnam_high_risk_does_not_fire(self):
        hits, _ = run(P226_VIETNAM, TABLE_P224)
        self.assertEqual(len(hits), 0)

    def test_kb_correct_form_is_exempt(self):
        hits, _ = run(KB_CORRECT_FORM, TABLE_P224)
        self.assertEqual(len(hits), 0)

    def test_bare_date_without_subject_does_not_fire(self):
        hits, _ = run("Erasmus+ calls close in August 2026.", TABLE_P224)
        self.assertEqual(len(hits), 0)

    def test_bare_subject_without_date_does_not_fire(self):
        hits, _ = run("Annex III lists high-risk systems for education.", TABLE_P224)
        self.assertEqual(len(hits), 0)


class ExtendedP226Table(unittest.TestCase):
    """p226 adds the Boston row the coverage gap exposed."""

    def setUp(self):
        if not os.path.exists(TABLE_P226):
            self.skipTest("p226 table not yet written")

    def test_boston_string_now_fires(self):
        hits, _ = run(P225_BOSTON, TABLE_P226)
        self.assertEqual(len(hits), 1, "the added row must catch the string that escaped p225")

    def test_boston_correct_form_still_exempt(self):
        hits, _ = run(BOSTON_CORRECT_FORM, TABLE_P226)
        self.assertEqual(len(hits), 0, "the KB's own published form must never fire")

    def test_eu_row_survives_the_addition(self):
        hits, _ = run(P225_EU, TABLE_P226)
        self.assertEqual(len(hits), 1)

    def test_p226_results_clean_for_the_THREE_ORIGINAL_subjects(self):
        """The original 3 subjects did not recur this pass. The extended table's one hit is a
        subject p226 added, which is the pass's finding - see CoverageRowsAddedAtP226."""
        raw = os.path.join(HERE, "p226-raw-results.txt")
        if not os.path.exists(raw):
            self.skipTest("raw results not vendored")
        hits, _ = run(open(raw, encoding="utf-8").read(), TABLE_P224)
        self.assertEqual(len(hits), 0)


class CoverageRowsAddedAtP226(unittest.TestCase):
    """The rows p226 added after finding the KB had refuted these claims and never tabled them."""

    def setUp(self):
        if not os.path.exists(TABLE_P226):
            self.skipTest("p226 table not yet written")

    def test_frappe_mit_claim_fires(self):
        """Refuted at p209 with a first-hand payload; returned INBOUND at p226."""
        hits, _ = run("Frappe LMS is listed as MIT in one comparison.", TABLE_P226)
        self.assertEqual(len(hits), 1)

    def test_frappe_corrected_form_is_exempt(self):
        hits, _ = run("frappe/lms is AGPL-3.0 (license.txt, 33 893 B), not MIT.", TABLE_P226)
        self.assertEqual(len(hits), 0)

    def test_openedx_bare_mit_claim_fires(self):
        hits, _ = run("Open edX is MIT licensed.", TABLE_P226)
        self.assertEqual(len(hits), 1)

    def test_openedx_claim_flagged_by_its_own_source_is_exempt(self):
        """This pass's actual text: the source flagged its own conflict, so it is not a
        reassertion. The exempt column is what tells those two cases apart."""
        hits, _ = run("One comparison lists Open edX as MIT, which conflicts with the AGPL "
                      "listings elsewhere.", TABLE_P226)
        self.assertEqual(len(hits), 0)

    def test_this_pass_fires_exactly_once_under_the_extended_table(self):
        raw = os.path.join(HERE, "p226-raw-results.txt")
        if not os.path.exists(raw):
            self.skipTest("raw results not vendored")
        hits, _ = run(open(raw, encoding="utf-8").read(), TABLE_P226)
        self.assertEqual(len(hits), 1)
        self.assertIn("frappe", hits[0][2].lower())


class RecordUnit(unittest.TestCase):
    def test_subject_and_date_in_DIFFERENT_records_do_not_pair(self):
        """ACTION QY: the line is the unit precisely so this cannot happen."""
        text = ("Annex III lists high-risk systems for education.\n"
                "Separately, the rules take effect in August 2026.\n")
        hits, _ = run(text, TABLE_P224)
        self.assertEqual(len(hits), 0)

    def test_query_header_lines_are_not_records(self):
        recs = split_records("=====QUERY: a query\nreal line\n")
        self.assertEqual(len(recs), 1)
        self.assertEqual(recs[0][0], "a query")


if __name__ == "__main__":
    unittest.main(verbosity=2)
