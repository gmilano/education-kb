"""Controls for `p228-shelf-gate`.

Every control below exists because a defect reached a draft, in this pass or an
earlier one. The three marked REGRESSION are defects this pass's own instrument
had before publishing.
"""
import unittest

import classify_grant as C
import harvest_cells as H
import gate as G

GPL3_HEAD = "GNU GENERAL PUBLIC LICENSE\n   Version 3, 29 June 2007\n"
AGPL3_HEAD = "GNU AFFERO GENERAL PUBLIC LICENSE\n   Version 3, 19 November 2007\n"
# GPL-3.0's compatibility clause NAMES the Affero licence in full (p227 T227-V3).
GPL3_S13 = "\n  13. Use with the GNU Affero General Public License.\n...GNU Affero General Public License..."
# AGPL-3.0's own section 13 names the GNU GPL -- the exact mirror.
AGPL3_S13 = "\n  13. Remote Network Interaction; Use with the GNU General Public License.\n"


class TestFamilyPositional(unittest.TestCase):
    def test_gpl3_body_carrying_the_agpl_title_in_s13_is_gpl3(self):
        fam, chan, _ = C.classify(GPL3_HEAD + GPL3_S13)
        self.assertEqual(fam, "GPL-3.0")

    def test_agpl3_body_carrying_the_gpl_title_in_s13_is_agpl3(self):
        """The mirror of T227-V3. A whole-body search inverts this one."""
        fam, _, _ = C.classify(AGPL3_HEAD + AGPL3_S13)
        self.assertEqual(fam, "AGPL-3.0")

    def test_affero_grep_is_the_unsafe_channel_and_stays_demonstrably_wrong(self):
        body = GPL3_HEAD + GPL3_S13
        self.assertEqual(C.classify(body)[0], "GPL-3.0")
        self.assertIn("affero", body.lower())   # the naive channel would say AGPL

    def test_lgpl_title_is_not_matched_by_the_gpl_pattern(self):
        body = "GNU LESSER GENERAL PUBLIC LICENSE\n  Version 3, 29 June 2007\n"
        self.assertEqual(C.classify(body)[0], "LGPL-3.0")

    def test_gpl2_and_gpl3_separated_on_the_version_line(self):
        self.assertEqual(C.classify("GNU GENERAL PUBLIC LICENSE\nVersion 2, June 1991\n")[0], "GPL-2.0")

    def test_swad_identity_control(self):
        """acanas/swad-core, read first-hand at p228: AGPL, not GPL."""
        fam, _, note = C.classify(AGPL3_HEAD + AGPL3_S13)
        self.assertEqual(fam, "AGPL-3.0")
        self.assertIn("13", note)


class TestDualGrant(unittest.TestCase):
    def test_dual_preamble_beats_the_earliest_title(self):
        """REGRESSION: Elgg returned `MIT` because the MIT title sits at 346 and
        the dual grant is stated at 0, before any title."""
        body = ('Bundled plugins (the contents of the "/mod" directory) are available\n'
                "only under the GPLv2 license.\n\n"
                "The remainder of the project is available under either MIT or GPLv2.\n\n"
                "The MIT License (MIT)\nPermission is hereby granted, free of charge\n"
                + GPL3_HEAD)
        fam, chan, _ = C.classify(body)
        self.assertEqual(fam, "MIT OR GPL-2.0")
        self.assertEqual(chan, "dual-grant preamble")

    def test_a_cell_naming_one_option_is_incomplete_not_wrong(self):
        v, _, _ = G.verdict("GPL-2", "MIT OR GPL-2.0")
        self.assertEqual(v, "INCOMPLETE-DUAL")

    def test_a_cell_naming_neither_option_is_still_a_family_defect(self):
        v, _, _ = G.verdict("Apache-2.0", "MIT OR GPL-2.0")
        self.assertEqual(v, "FAMILY")


class TestHarvestSubjects(unittest.TestCase):
    """The five NON-GRANT subjects. Nine false findings came from these."""

    def _status(self, line):
        rows = H.harvest("f.md", line)
        return rows[0]["status"] if rows else None

    def test_directory_scoped_cell_is_not_a_repository_cell(self):
        self.assertEqual(self._status(
            "| [pupilfirst/pupilfirst](https://github.com/pupilfirst/pupilfirst) | **978** | "
            "`docs/**` | **CC-BY-SA-4.0** | content ShareAlike attaches |"), "DIRECTORY-SCOPED")

    def test_body_content_token_is_not_a_grant(self):
        self.assertEqual(self._status(
            "| [`odoo/odoo`](https://github.com/odoo/odoo) | **`43 529`** | full -- "
            "`GPL-3.0` included by **value** |"), "BODY-CONTENT")

    def test_correction_narrative_token_is_not_live(self):
        self.assertEqual(self._status(
            "[`towardsai/ai-tutor-app`](https://github.com/towardsai/ai-tutor-app) "
            "was published **`MIT` in"), "CORRECTION-NARRATIVE")

    def test_quoted_external_claim_is_evidence_about_a_source(self):
        self.assertEqual(self._status(
            'table, rank `8`, reads *"the `MIT` LMS"* for '
            "[`frappe/lms`](https://github.com/frappe/lms)."), "QUOTED-EXTERNAL-CLAIM")

    def test_unlinked_co_subject_makes_attribution_ambiguous(self):
        self.assertEqual(self._status(
            "[`OpenEduCat`](https://github.com/openeducat/openeducat_erp), Open edX *(`AGPL-3`)*."),
            "UNLINKED-CO-SUBJECT")

    def test_a_plain_table_row_is_still_LIVE(self):
        self.assertEqual(self._status(
            "| [`acanas/swad-core`](https://github.com/acanas/swad-core) | `GPL-3.0` "
            "*(`34 501` B, full text)* | EMEA | `76` stars |"), "LIVE")

    def test_grant_stored_under_docs_is_not_directory_scoped(self):
        """REGRESSION: the first scope pattern excluded 553 cells by matching
        ordinary markdown emphasis, openSIS's `docs/License.txt` among them."""
        self.assertEqual(self._status(
            "| [`OS4ED/openSIS-Classic`](https://github.com/OS4ED/openSIS-Classic) | "
            "**`GPL-2.0`** | `docs/License.txt` | `17 286` |"), "LIVE")

    def test_emphasis_around_a_licence_token_is_not_a_glob(self):
        """REGRESSION, same bug, minimal case."""
        self.assertEqual(self._status(
            "| [`a/b`](https://github.com/a/b) | **`MIT`** | `main/LICENSE` `1 072` B |"), "LIVE")


class TestSubstringHazards(unittest.TestCase):
    def test_gpl3_is_not_harvested_from_inside_agpl3(self):
        """p227 T227-V2: `GPL-3.0` is a substring of `AGPL-3.0`."""
        self.assertEqual(H.licences_on("x `AGPL-3.0` y"), ["AGPL-3.0"])

    def test_or_later_is_not_truncated_to_the_bare_token(self):
        self.assertEqual(H.licences_on("`GPL-3.0-or-later`"), ["GPL-3.0-or-later"])

    def test_dotted_owner_is_a_hostname_not_an_account(self):
        """p224 T224-2."""
        self.assertEqual(H.slugs_on("https://raw.githubusercontent.com/a/b"), [])

    def test_two_slugs_on_a_line_yield_no_attributable_cell(self):
        """p224 T224-3."""
        rows = H.harvest("f.md", "| github.com/a/b and github.com/c/d are `MIT` |")
        self.assertEqual(rows[0]["status"], "AMBIGUOUS-MULTI-SLUG")


class TestBoundIsNotDecided(unittest.TestCase):
    def test_bound_is_never_asserted_from_a_root_licence(self):
        """p225 and p227: or-later lives in a CHANNEL the canonical body lacks."""
        v, _, _ = G.verdict("GPL-3.0-or-later", "GPL-3.0")
        self.assertEqual(v, "BOUND")

    def test_notation_difference_is_reported_separately_from_a_defect(self):
        self.assertEqual(G.verdict("GPL-3", "GPL-3.0")[0], "NOTATION")

    def test_agreement_is_agreement(self):
        self.assertEqual(G.verdict("MIT", "MIT")[0], "AGREE")

    def test_a_cell_over_a_repo_with_no_grant_file_is_its_own_class(self):
        self.assertEqual(G.verdict("MIT", "NO-GRANT")[0], "CELL-WITHOUT-GRANT")

    def test_an_unrecognised_body_is_never_turned_into_a_defect(self):
        self.assertEqual(G.verdict("MIT", "UNRECOGNISED")[0], "UNDECIDABLE-BODY")



class TestActionSP(unittest.TestCase):
    """`ACTION SP` asked for the EU AI Act subject to be bound to a jurisdiction.
    Measurement refutes that and hands back a better fix."""

    import narrow_subject as N  # noqa: E402

    OLD = r"(?i)(ai act|annex iii|anexo iii|alto riesgo|high-risk)"
    BOUNDED = r"(?i)(\bai act\b|annex\s+iii|anexo\s+iii|alto riesgo|high-risk)"

    def test_jurisdiction_binding_drops_a_genuine_eu_record(self):
        """LIMB 2. The record is EU by the QUERY it came from; its text names no
        jurisdiction, so binding the subject to a jurisdiction token loses it."""
        import re
        t = ("Education tools that evaluate learners or influence access to "
             "qualifications fall into the high-risk category")
        self.assertTrue(re.search(self.OLD, t))
        self.assertFalse(re.search(self.N.NEW, t))

    def test_jurisdiction_binding_also_GAINS_an_irrelevant_record(self):
        """Strictly worse on both sides, which is why the pattern is left alone."""
        import re
        t = "EU enterprise AI adoption stood at 19.95%, which is business-wide"
        self.assertFalse(re.search(self.OLD, t))
        self.assertTrue(re.search(self.N.NEW, t))

    def test_the_real_defect_is_a_word_boundary(self):
        """`ai act` matches inside `AI action plan`. Found by running ACTION SH on
        p228's own records -- p227's table carries this defect live."""
        import re
        t = "the states should develop a joint AI action plan with measurable goals"
        self.assertEqual(re.search(self.OLD, t).group(0).lower(), "ai act")
        self.assertIsNone(re.search(self.BOUNDED, t))

    def test_the_boundary_fix_costs_no_genuine_match(self):
        import re
        for t in ("the EU AI Act coming into effect step by step",
                  "Annex III education high-risk applies 2027-12-02",
                  "the AI Act itself entering force",
                  "fall into the high-risk category"):
            self.assertTrue(re.search(self.OLD, t), t)
            self.assertTrue(re.search(self.BOUNDED, t), t)

if __name__ == "__main__":
    unittest.main(verbosity=2)
