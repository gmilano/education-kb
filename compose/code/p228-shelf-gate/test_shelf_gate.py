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

class TestDottedRepoName(unittest.TestCase):
    """p250 / `ACTION XJ` — the dot-suffix truncation, pinned as behaviour.

    `p233` named this defect, `p247` reproduced it, `p249` repaired `6` slugs BY HAND,
    and none of them pinned it, so it came back each time.  `p230`'s `lazy_lint.py`
    guards the regex SHAPE; these controls guard the ANSWER, which is the thing the
    shelves actually consume.  Every slug below is a real row carried on these shelves.
    """
    REAL = [
        "dmitry-viskov/pylti1.3",
        "dmitry-viskov/pylti1.3-django-example",
        "ucfopen/pylti1.3",
        "UOC/java-lti-1.3",
        "UOC/java-lti-1.3-provider-example",
        "ramsrigouthamg/Questgen.ai",
        "JuliaPluto/Pluto.jl",
        "theopenem/oneroster.net",
        "jdolny/OneRoster.NET",
        "processing/p5.js",
        "eclipse/paho.mqtt.java",
        "eecs-autograder/autograder.io",
        "Ed-Fi-Alliance-OSS/EdFi.Installer.AppCommon",
        "JushBJJ/Mr.-Ranedeer-AI-Tutor",
    ]

    def test_a_dotted_repository_name_survives_the_harvest_whole(self):
        for slug in self.REAL:
            line = "| [`x`](https://github.com/%s) | `MIT` |" % slug
            self.assertEqual(H.slugs_on(line), [slug], slug)

    def test_case_is_preserved_by_the_harvester(self):
        # p249 reported the harvester as case-folding too.  It does NOT: the fold lives
        # downstream, in `p235-carried-index`'s normaliser and in the `gate-mit-tier`
        # recipe's `tolower($3)`.  Pinned so the attribution cannot drift again.
        line = "| [`x`](https://github.com/ramsrigouthamg/Questgen.ai) | `MIT` |"
        self.assertEqual(H.slugs_on(line), ["ramsrigouthamg/Questgen.ai"])

    def test_a_trailing_sentence_dot_is_still_shed(self):
        self.assertEqual(H.slugs_on("see github.com/theopenem/oneroster.net."),
                         ["theopenem/oneroster.net"])

    def test_a_clone_url_folds_onto_the_bare_repository_name(self):
        for url, bare in (("github.com/ucfopen/pylti1.3.git", "ucfopen/pylti1.3"),
                          ("github.com/Cvmcosta/ltijs.git", "Cvmcosta/ltijs"),
                          ("github.com/trilogy-group/oneroster-ts.git",
                           "trilogy-group/oneroster-ts")):
            self.assertEqual(H.slugs_on("url %s)" % url), [bare], url)

    def test_the_undotted_population_is_unaffected(self):
        for slug in ("pykt-team/pykt-toolkit", "openedx/XBlock", "HKUDS/DeepTutor",
                     "CAHLR/OATutor", "microsoft/ai-agents-for-beginners"):
            line = "| [`x`](https://github.com/%s) | `MIT` |" % slug
            self.assertEqual(H.slugs_on(line), [slug], slug)

    def test_a_dotted_OWNER_is_still_rejected_as_a_hostname(self):
        # T224-2 must survive the fix: greediness must not turn a hostname into an account.
        self.assertEqual(H.slugs_on("see github.com/docs.example.com/thing)"), [])



class TestMulanGrant(unittest.TestCase):
    """Controls for `883-G2`, closed at p884.

    The gate returned `(None, None, 'no recognised licence title')` on
    `ECNU/EduWork`'s real `LICENSE` - 9,233 B, `sha256_12 eb7a1d713eb9` - which is
    an OSI-approved PERMISSIVE grant. That is a false ABSENCE, the mirror of
    p877's false PRESENCE on PageLM, and the rule both obey is `T14`:
    an abstention is not a licence finding in either direction.
    """

    # Reproduced from the measured payload. The separator is U+FF0C, NOT an ASCII
    # comma, and the Chinese title legitimately precedes the English one.
    MULAN_CN = "\n\u6728\u5170\u5bbd\u677e\u8bb8\u53ef\u8bc1, \u7b2c2\u7248\n"
    MULAN_EN = "Mulan Permissive Software License\uff0cVersion 2 (Mulan PSL v2)\n"
    PUBL_EN = "Mulan Public License\uff0cVersion 2 (Mulan PubL v2)\n"

    def test_the_measured_eduwork_shape_resolves_to_mulanpsl2(self):
        """883-G2's acceptance test, positive half."""
        fam, chan, _ = C.classify(self.MULAN_CN + self.MULAN_EN)
        self.assertEqual(fam, "MulanPSL-2.0")
        self.assertIsNotNone(chan)

    def test_a_mulan_body_is_not_read_as_apache(self):
        """883-G2's acceptance test, negative half.

        Mulan PSL is Apache-LIKE in effect, which is exactly why a lazy fix would
        map it onto Apache-2.0. The family must be reported as what it is.
        """
        fam, _, _ = C.classify(self.MULAN_CN + self.MULAN_EN)
        self.assertNotEqual(fam, "Apache-2.0")

    def test_english_only_payload_resolves(self):
        self.assertEqual(C.classify(self.MULAN_EN)[0], "MulanPSL-2.0")

    def test_chinese_only_payload_resolves(self):
        """A Chinese-only body is the realistic APAC case and must not abstain."""
        self.assertEqual(C.classify(self.MULAN_CN)[0], "MulanPSL-2.0")

    def test_REGRESSION_the_fullwidth_comma_is_load_bearing(self):
        """The trap that would have reproduced the original false absence.

        An ASCII-comma pattern (`License,?\\s*Version`) cannot match U+FF0C: it is
        neither `,` nor whitespace. A fix written without reading the bytes fails
        SILENTLY and looks like a pass.
        """
        import re
        naive = re.compile(r"Mulan\s+Permissive\s+Software\s+License,?\s*Version\s+2", re.I)
        self.assertIsNone(naive.search(self.MULAN_EN))
        self.assertEqual(C.classify(self.MULAN_EN)[0], "MulanPSL-2.0")

    def test_mulan_PUBLIC_is_not_reported_as_the_PERMISSIVE_grant(self):
        """PubL carries a copyleft-style obligation; publishing it as MulanPSL
        would be p877's PageLM class in a new family."""
        fam, _, _ = C.classify(self.PUBL_EN)
        self.assertEqual(fam, "MulanPubL-2.0")
        self.assertNotEqual(fam, "MulanPSL-2.0")

    def test_an_unrelated_body_still_abstains(self):
        """The row must not make the classifier credulous."""
        self.assertIsNone(C.classify("Some bespoke terms, all rights withheld.\n")[0])


class TestSplitFileGrant(unittest.TestCase):
    """Controls for the SPLIT-FILE dual grant, added p884.

    Measured case: `RWTH-OS/eduOS-rs`, 493 stars, the highest-starred education
    repository p884's owner sweep returned. All 16 single-file probes in
    `fetch_grants.sh` 404'd, so the probe reported NO-GRANT-FILE on a repository
    carrying TWO real grants - `LICENSE-APACHE` (9,722 B) and `LICENSE-MIT`
    (1,023 B). GitHub's single `license.spdx_id` field reports `Apache-2.0` alone.
    """

    APACHE = "                              Apache License\n                        Version 2.0, January 2004\n"
    MIT = "Permission is hereby granted, free of charge, to any person obtaining a copy\n"

    def test_the_two_halves_resolve_to_a_dual_cell(self):
        fam, chan, _ = C.split_grant(self.APACHE, self.MIT)
        self.assertEqual(fam, "Apache-2.0 OR MIT")
        self.assertEqual(chan, "split-file grant")

    def test_each_half_read_ALONE_looks_single_and_that_is_the_whole_trap(self):
        """Neither file contains any hint that the other exists."""
        self.assertEqual(C.classify(self.APACHE)[0], "Apache-2.0")
        self.assertEqual(C.classify(self.MIT)[0], "MIT")

    def test_the_order_is_stable_regardless_of_which_path_answered_first(self):
        self.assertEqual(C.split_grant(self.APACHE, self.MIT)[0],
                         C.split_grant(self.MIT, self.APACHE)[0])

    def test_one_resolvable_half_is_NOT_reported_as_dual(self):
        """A 200 on one path and junk on the other must not invent a second grant."""
        fam, chan, note = C.split_grant(self.MIT, "not a licence at all\n")
        self.assertEqual(fam, "MIT")
        self.assertIn("one half", note)
        self.assertNotIn("OR", fam)

    def test_split_file_is_a_DIFFERENT_shape_from_the_dual_preamble(self):
        """`dual_grant` reads prose; `split_grant` reads layout. Keep them apart:
        neither eduOS file carries a dual-grant preamble, so dual_grant sees nothing."""
        self.assertIsNone(C.dual_grant(self.APACHE))
        self.assertIsNone(C.dual_grant(self.MIT))
        self.assertEqual(C.split_grant(self.APACHE, self.MIT)[0], "Apache-2.0 OR MIT")


if __name__ == "__main__":
    unittest.main(verbosity=2)
