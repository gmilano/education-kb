#!/usr/bin/env python3
"""p308 — offline controls for the shelf-consistency gate.

Every control is a defect this base actually published, or the exact
false-positive class that would have made the gate unrunnable.  No network,
no filesystem outside `fixtures/`.
"""
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from shelf_consistency import (  # noqa: E402
    claim_from_window, disagreements, extract_claims, licences_in, split_row,
)

GH = "https://github.com"


class TheDefectThisGateExistsFor(unittest.TestCase):
    """p307's headline: AGPL-3.0 carried for two passes against three
    shelves that said GPL, and one that said GPL-3.0 @ p212."""

    def test_agpl_is_not_gpl3(self):
        # The substring trap: "AGPL-3.0" contains "GPL-3.0".
        self.assertEqual(licences_in("AGPL-3.0")[0][0], "AGPL-3.0")
        self.assertEqual([n for n, _ in licences_in("AGPL-3.0")], ["AGPL-3.0"])

    def test_bare_gpl3_is_gpl3(self):
        self.assertEqual([n for n, _ in licences_in("GPL-3.0")], ["GPL-3.0"])

    def test_lgpl_is_not_gpl(self):
        self.assertEqual([n for n, _ in licences_in("LGPL-3.0")], ["LGPL-3.0"])

    def test_affero_prose_reads_as_agpl(self):
        # repos/foundations.md says "GNU Affero General Public License" in
        # prose; it must land on the same canonical name as "AGPL-3.0".
        self.assertIn("AGPL-3.0",
                      [n for n, _ in licences_in("GNU Affero General Public License")])

    def test_the_ltltutor_disagreement_is_caught(self):
        """The two shelves, as they actually read at p306."""
        a = f"| [`brownplt/LTLTutor`]({GH}/brownplt/LTLTutor) | AGPL-3.0 | 12 |"
        b = f"🔴 **[`brownplt/LTLTutor`]({GH}/brownplt/LTLTutor)** — **GNU GPL-3.0** (payload)"
        claims = (extract_claims("| name | licence | stars |\n|---|---|---|\n" + a,
                                 "agents/top.md")
                  + extract_claims(b, "repos/foundations.md"))
        d = disagreements(claims)
        self.assertIn("brownplt/ltltutor", d)
        self.assertEqual(sorted(d["brownplt/ltltutor"]), ["AGPL-3.0", "GPL-3.0"])


class CorrectionTablesAreNotClaims(unittest.TestCase):
    """p307's own shelves print the wrong value on purpose."""

    def test_carried_as_actually_header_suppresses_rows(self):
        md = (
            "| slug | payload | title line, read at `p307` | carried as | actually |\n"
            "|---|---|---|---|---|\n"
            f"| [`brownplt/LTLTutor`]({GH}/brownplt/LTLTutor) | `LICENSE.txt` 35 148 B "
            "| `GNU GENERAL PUBLIC LICENSE Version 3` | 🔴 AGPL-3.0 | 🔴 **GPL-3.0** |\n"
        )
        self.assertEqual(extract_claims(md, "agents/top.md"), [])

    def test_an_ordinary_table_still_yields_claims(self):
        md = (
            "| platform | licence | scale |\n|---|---|---|\n"
            f"| [`Selleo/mentingo`]({GH}/Selleo/mentingo) | 🟢 **MIT** | 96★ |\n"
        )
        claims = extract_claims(md, "verticals/solutions.md")
        self.assertEqual(len(claims), 1)
        self.assertEqual(claims[0]["slug"], "selleo/mentingo")
        self.assertEqual(claims[0]["licences"], {"MIT"})


class RetractionsAreNotClaims(unittest.TestCase):
    """`GPL-3.0 — CORRECTED p307 from AGPL-3.0` asserts one and quotes one."""

    def test_corrected_from(self):
        self.assertEqual(
            claim_from_window("🔴 **GPL-3.0**, CORRECTED `p307` from `AGPL-3.0`"),
            {"GPL-3.0"})

    def test_this_row_read_x_for_two_passes(self):
        self.assertEqual(
            claim_from_window("🔴 **GPL-3.0** — this row read `AGPL-3.0` for two passes"),
            {"GPL-3.0"})

    def test_not_x_but_y_keeps_only_the_assertion(self):
        self.assertEqual(claim_from_window("**GPL-3.0**, not AGPL-3.0"), {"GPL-3.0"})

    def test_a_genuine_dual_licence_survives(self):
        # No retraction vocabulary: both are asserted.
        self.assertEqual(claim_from_window("dual-licensed **MIT** and **Apache-2.0**"),
                         {"MIT", "Apache-2.0"})

    def test_a_window_that_opens_with_a_retraction_claims_nothing(self):
        self.assertIsNone(
            claim_from_window("this was wrongly carried as AGPL-3.0 by an earlier pass"))

    def test_emoji_and_table_pipes_do_not_count_as_retraction_context(self):
        self.assertEqual(claim_from_window("| 🟢 **MIT** |"), {"MIT"})


class SiblingsInDescriptionCellsAreNotClaims(unittest.TestCase):
    """p307 hit this class twice in one pass."""

    def test_the_subject_is_the_first_slug_bearing_cell(self):
        md = (
            "| repo | licence | description |\n|---|---|---|\n"
            f"| [`a/one`]({GH}/a/one) | MIT | pairs well with "
            f"[`b/two`]({GH}/b/two), which is AGPL-3.0 |\n"
        )
        claims = extract_claims(md, "compose/patterns.md")
        self.assertEqual([c["slug"] for c in claims], ["a/one"])
        self.assertEqual(claims[0]["licences"], {"MIT"})

    def test_without_a_licence_column_the_row_is_read_narrowly(self):
        md = (
            "| role | component | note |\n|---|---|---|\n"
            f"| tutor | [`a/one`]({GH}/a/one) | 🟢 **MIT** |\n"
        )
        claims = extract_claims(md, "compose/patterns.md")
        self.assertEqual(claims[0]["licences"], {"MIT"})


class MetaRowsAboutLicenceIdentityAreNotClaims(unittest.TestCase):
    def test_a_title_line_row_is_skipped(self):
        self.assertIsNone(claim_from_window(
            "the title line reads `GNU GENERAL PUBLIC LICENSE Version 3`, "
            "so the AGPL-3.0 label was wrong"))

    def test_a_length_series_row_is_skipped(self):
        self.assertIsNone(claim_from_window(
            "5th distinct AGPL payload length (33 893 · 35 149) — GPL-3.0 sits inside it"))


class TableMechanics(unittest.TestCase):
    def test_separator_row_is_not_a_row(self):
        self.assertIsNone(split_row("|---|---|"))
        self.assertIsNone(split_row("| :--- | ---: |"))

    def test_prose_line_is_not_a_row(self):
        self.assertIsNone(split_row("🟢 **MIT** — a prose claim"))

    def test_cells_are_stripped(self):
        self.assertEqual(split_row("| a |  b  |"), ["a", "b"])


class SlugFolding(unittest.TestCase):
    def test_case_folds_so_one_row_is_one_slug(self):
        md_a = f"| r | licence |\n|---|---|\n| [`OpenOLAT/OpenOLAT`]({GH}/OpenOLAT/OpenOLAT) | LGPL-2.1 |\n"
        md_b = f"| r | licence |\n|---|---|\n| [`openolat/OpenOLAT`]({GH}/openolat/OpenOLAT) | Apache-2.0 |\n"
        d = disagreements(extract_claims(md_a, "a.md") + extract_claims(md_b, "b.md"))
        self.assertIn("openolat/openolat", d)

    def test_agreement_is_not_a_disagreement(self):
        md_a = f"| r | licence |\n|---|---|\n| [`a/one`]({GH}/a/one) | MIT |\n"
        md_b = f"| r | licence |\n|---|---|\n| [`a/one`]({GH}/a/one) | 🟢 **MIT** |\n"
        self.assertEqual(disagreements(extract_claims(md_a, "a.md")
                                       + extract_claims(md_b, "b.md")), {})


class ProseClaimsAreExtracted(unittest.TestCase):
    """foundations.md:764 said "GNU GPL" in PROSE, and that is where p307's
    right answer was hiding.  A table-only gate would have missed it."""

    def test_a_hard_wrapped_prose_claim_is_read(self):
        body = (f"🔴 **[`brownplt/LTLTutor`]({GH}/brownplt/LTLTutor)** — **GNU GPL-3.0**\n"
                "(payload `LICENSE.txt`, 35 148 B)\n")
        claims = extract_claims(body, "repos/foundations.md")
        self.assertTrue(any(c["kind"] == "prose" and c["licences"] == {"GPL-3.0"}
                            for c in claims))

    def test_a_claim_split_across_the_wrap_is_still_read(self):
        body = (f"🔴 **[`brownplt/LTLTutor`]({GH}/brownplt/LTLTutor)** — the payload is\n"
                "**GPL-3.0**, 35 148 B\n")
        claims = extract_claims(body, "repos/foundations.md")
        self.assertTrue(any(c["licences"] == {"GPL-3.0"} for c in claims))




class DualAndSplitLicencesAreNotContradictions(unittest.TestCase):
    """The intersection rule — the gate's first run got this wrong on 15 rows."""

    def test_dual_licence_against_one_of_its_halves_agrees(self):
        a = f"| r | licence |\n|---|---|\n| [`a/one`]({GH}/a/one) | dual **MIT** and **Apache-2.0** |\n"
        b = f"| r | licence |\n|---|---|\n| [`a/one`]({GH}/a/one) | 🟢 **MIT** |\n"
        self.assertEqual(disagreements(extract_claims(a, "x.md")
                                      + extract_claims(b, "y.md")), {})

    def test_code_and_content_licences_on_one_row_are_not_a_conflict(self):
        # ankitects/anki: AGPL-3.0 code, CC-BY-SA-4.0 shared decks.
        md = (f"| r | licence |\n|---|---|\n| [`ankitects/anki`]({GH}/ankitects/anki) "
              "| **AGPL-3.0** code, **CC-BY-SA-4.0** content |\n")
        self.assertEqual(disagreements(extract_claims(md, "x.md")), {})

    def test_a_genuine_contradiction_still_fails(self):
        a = f"| r | licence |\n|---|---|\n| [`a/one`]({GH}/a/one) | **MIT** |\n"
        b = f"| r | licence |\n|---|---|\n| [`a/one`]({GH}/a/one) | **Apache-2.0** |\n"
        self.assertIn("a/one", disagreements(extract_claims(a, "x.md")
                                            + extract_claims(b, "y.md")))


class ClauseFamilyNotesAreNotClaims(unittest.TestCase):
    """p307's prober emits `clause=MIT/ISC`; the shelves quote it."""

    def test_clause_mit_isc_is_one_claim_not_two(self):
        self.assertEqual(claim_from_window("🟢 **MIT** `1 072 B` clause=MIT/ISC"), {"MIT"})

    def test_clause_apache_mpl_does_not_add_mpl(self):
        self.assertEqual(claim_from_window("🟢 **Apache-2.0** clause=Apache/MPL"),
                         {"Apache-2.0"})

    def test_clause_gpl_family_does_not_add_a_second_gpl(self):
        self.assertEqual(claim_from_window("🔴 **GPL-3.0** clause=GPL-family"),
                         {"GPL-3.0"})


class ProseSubjectDiscipline(unittest.TestCase):
    """The class the first draft fixed for tables and reintroduced in prose."""

    def test_a_neighbours_licence_does_not_attach(self):
        body = (f"Use [`moodle/moodle`]({GH}/moodle/moodle) as the base.\n"
                f"Then add [`b/two`]({GH}/b/two), which is **Apache-2.0**.\n")
        claims = extract_claims(body, "compose/patterns.md")
        for c in claims:
            if c["slug"] == "moodle/moodle":
                self.fail(f"moodle collected a neighbour's licence: {c}")

    def test_a_licence_before_the_slug_does_not_attach(self):
        body = ("...Apache-2.0, Open Badges + CLR). Still nothing for QTI.\n"
                f"🟢 p231: QTI CLOSED ([`feyst/qti3-validator`]({GH}/feyst/qti3-validator), `MIT`,\n")
        claims = extract_claims(body, "intel/open-gaps.md")
        for c in claims:
            if c["slug"] == "feyst/qti3-validator":
                self.assertEqual(c["licences"], {"MIT"})

    def test_the_subjects_own_licence_still_attaches(self):
        body = f"🔴 **[`brownplt/LTLTutor`]({GH}/brownplt/LTLTutor)** — **GNU GPL-3.0** payload\n"
        claims = extract_claims(body, "repos/foundations.md")
        self.assertTrue(any(c["licences"] == {"GPL-3.0"} for c in claims))


class UnlicensedIsAnAbsenceNotTheUnlicense(unittest.TestCase):
    def test_the_adjective_does_not_match(self):
        self.assertEqual([n for n, _ in licences_in('*(none — "unlicensed")*')], [])

    def test_the_licence_still_matches(self):
        self.assertEqual([n for n, _ in licences_in("released under the Unlicense")],
                         ["Unlicense"])

    def test_an_unlicensed_row_beside_a_real_grant_claims_the_grant(self):
        md = (f'| repo | licence | note |\n|---|---|---|\n'
              f'| [`a/one`]({GH}/a/one) | *(none — "unlicensed")* | **MIT**, at `main/LICENCE` |\n')
        d = disagreements(extract_claims(md, "intel/trends.md"))
        self.assertEqual(d, {})


class MultiGrantAndScopedAbsenceAreNotContradictions(unittest.TestCase):
    def test_three_grants_in_one_repository_is_a_finding(self):
        self.assertIsNone(claim_from_window(
            "root `composer.json` **GPL-3.0-or-later** · root `package.json` **ISC** "
            "· subpackage **MIT** — three grants in one repository"))

    def test_a_branch_scoped_no_payload_is_not_a_licence_claim(self):
        self.assertIsNone(claim_from_window("— **NO-PAYLOAD** on `develop`, MIT elsewhere"))

    def test_a_manifest_only_declaration_is_not_a_payload_claim(self):
        self.assertIsNone(claim_from_window("**MIT**, declared in `package.json` only"))

class ComparatorsAreNotClaims(unittest.TestCase):
    """intel/trends.md:269 — "CC0-1.0 … more permissive than MIT"."""

    def test_more_permissive_than_mit(self):
        self.assertEqual(
            claim_from_window("is **CC0-1.0** — a public-domain dedication, "
                              "**more permissive than MIT**, no attribution"),
            {"CC0-1.0"})

    def test_unlike_apache(self):
        self.assertEqual(claim_from_window("**MIT**, unlike Apache-2.0, has no patent grant"),
                         {"MIT"})

    def test_a_real_dual_grant_is_still_both(self):
        self.assertEqual(claim_from_window("dual-licensed **MIT** and **Apache-2.0**"),
                         {"MIT", "Apache-2.0"})


class ManifestPayloadSplitsAreNotContradictions(unittest.TestCase):
    def test_mit_in_package_json_over_cc_by_nc_in_the_payload(self):
        self.assertIsNone(claim_from_window(
            "🟢 **MIT** (`package.json`) | 🔴 **`CC-BY-NC-SA-4.0`**, `LICENSE.md` **1,891 B**"))

    def test_a_first_draft_misclassification_narrative_claims_nothing(self):
        self.assertIsNone(claim_from_window(
            "v3's first draft classified it as `Unlicense/PD`. It is CC-BY-NC-SA-4.0."))

class ArrowCorrectionsNeedNoHeader(unittest.TestCase):
    """intel/open-gaps.md publishes corrections with no correction header."""

    def test_the_arrow_is_the_header(self):
        self.assertIsNone(claim_from_window(
            "🔴 `LGPL-3.0` · 18 025 B · *\"LGPL: linkable\"* | "
            "🔴 **GNU GENERAL PUBLIC LICENSE, Version 2** → **GPL-2.0**"))

    def test_an_ordinary_row_with_no_arrow_still_claims(self):
        self.assertEqual(claim_from_window("🔴 GPL-2.0 18 025 B `develop`"), {"GPL-2.0"})


class TwoSubjectRowsCarryTwoLicences(unittest.TestCase):
    """verticals/solutions.md:1468 — i-educar GPL-2.0 · i-diario AGPL-3.0."""

    def test_a_paired_row_is_skipped(self):
        md = ("| platform | repos | licence | stack |\n|---|---|---|---|\n"
              f"| **i-Educar + i-Diário** | [`portabilis/i-educar`]({GH}/portabilis/i-educar) · "
              f"[`portabilis/i-diario`]({GH}/portabilis/i-diario) | GPL-2.0 · **AGPL-3.0** | PHP |\n")
        self.assertEqual(extract_claims(md, "verticals/solutions.md"), [])

    def test_a_single_subject_row_is_not_skipped(self):
        md = ("| platform | repo | licence |\n|---|---|---|\n"
              f"| i-Educar | [`portabilis/i-educar`]({GH}/portabilis/i-educar) | GPL-2.0 |\n")
        claims = extract_claims(md, "verticals/solutions.md")
        self.assertEqual(len(claims), 1)
        self.assertEqual(claims[0]["licences"], {"GPL-2.0"})

class PossessiveAndQuotedMentions(unittest.TestCase):
    def test_a_possessive_licence_is_a_template_not_a_claim(self):
        # open-gaps:4879 — a RESERVED licence described as MIT's text negated.
        self.assertIsNone(claim_from_window(
            "— view-only, `MIT`'s verb list negated item by item, "
            "`MIT`'s warranty paragraph kept verbatim"))

    def test_a_quoted_licence_is_someone_elses_claim(self):
        # solutions:797 — p296 caught a comparison publishing lms as "MIT".
        self.assertIsNone(claim_from_window(
            'a 2026 comparison publishing it as *"MIT"* when its sidebar says otherwise'))

    def test_an_unquoted_bold_licence_is_still_a_claim(self):
        self.assertEqual(claim_from_window("🟢 **MIT**, at `main/LICENCE`"), {"MIT"})


class ProseTakesTheFirstLicenceOnly(unittest.TestCase):
    def test_a_bare_name_sibling_does_not_add_its_licence(self):
        body = (f"  [`portabilis/i-educar`]({GH}/portabilis/i-educar) (GPL-2.0, 34,948 commits) and\n"
                "  `i-diario` (AGPL-3.0) — and it arrives copylefted.\n")
        claims = extract_claims(body, "intel/market.md")
        for c in claims:
            if c["slug"] == "portabilis/i-educar":
                self.assertEqual(c["licences"], {"GPL-2.0"})


class ScopedThirdPartyGrantsAreNotThisRowsGrant(unittest.TestCase):
    """p351 — the gate's one RED on the live shelves, and the shelf was right.

    `jtylek/EpesiCRM` is MIT, read payload-first at the root.  Two shelves
    also mention the GPL-3 Roundcube that the repository's own `LICENSE`
    declares "not part of this software".  The gate bound that GPL-3 to the
    slug and called the shelves self-contradictory.

    🔵 Both directions are pinned here, because THIRD_PARTY_SCOPE makes the
    gate QUIETER and a wrong alternative would hide a real disagreement.
    """

    def test_the_live_defect_a_scoped_grant_before_any_other_token(self):
        # intel/market.md:61, verbatim shape — GPL-3 is the ONLY token.
        self.assertIsNone(claim_from_window(
            " is positioned by its own README as a kickstarter for custom ERP, "
            "and it scopes its vendored dependencies and an optional GPL-3 "
            "Roundcube explicitly"))

    def test_the_rows_own_grant_still_survives_a_later_scope(self):
        # verticals/solutions.md:19 — MIT first, then the scoping sentence.
        got = claim_from_window(
            " 🟢 **MIT**, `LICENSE` at ROOT, holder `Janusz Tylek`, 2006-2026 "
            "— stock MIT terms. And it scopes itself explicitly: a "
            '"Third-party software" section states `vendor/` (Laravel, '
            "Filament, Livewire) carry their own licences, and that Roundcube "
            "webmail is NOT part of this software — GPL-3")
        self.assertEqual(got, {"MIT"})

    def test_the_two_shelves_now_agree(self):
        body = (
            f"- [`jtylek/EpesiCRM`]({GH}/jtylek/EpesiCRM) is positioned by its "
            "own README as a kickstarter for custom ERP, and it scopes its "
            "vendored dependencies and an optional GPL-3 Roundcube explicitly.\n")
        claims = extract_claims(body, "intel/market.md")
        self.assertEqual(
            [c for c in claims if c["slug"] == "jtylek/epesicrm"], [],
            "a scoped third-party grant must not reach the disagreement set")

    def test_a_submodule_grant_is_scoped_too(self):
        # p346 shipped a row granted on three channels, one of them a
        # submodule.  A submodule's licence is not the superproject's.
        self.assertIsNone(claim_from_window(
            " — its sub-module vendors an Apache-2.0 tokenizer"))

    # 🔴 The other direction: these must STILL be claims, or the fix has
    # bought a false positive by creating a false negative.
    def test_a_plain_grant_is_unaffected(self):
        self.assertEqual(claim_from_window("🟢 **Apache-2.0**, `LICENSE` at ROOT"),
                         {"Apache-2.0"})

    def test_the_word_optional_far_from_any_licence_is_harmless(self):
        self.assertEqual(
            claim_from_window("🟢 **BSD-3-Clause** at ROOT; the web UI is optional"),
            {"BSD-3-Clause"})

    def test_a_genuine_two_licence_disagreement_still_fires(self):
        # No scope and no retraction vocabulary: both tokens stand, which is
        # what p307's AGPL/GPL defect needed and must not be lost.
        self.assertEqual(
            claim_from_window("**AGPL-3.0** at ROOT, and the shelf says MIT"),
            {"AGPL-3.0", "MIT"})


if __name__ == "__main__":
    unittest.main(verbosity=2)
