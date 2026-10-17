"""Controls for `pass262-scoped-reservation-audit`.  Run from this directory.

Every payload assertion reads `fixtures-p262/`, which was fetched first-hand at `p262` on
`ls-remote`-resolved refs.  Nothing here is hand-typed from a shelf.
"""

import os
import sys
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(os.path.dirname(HERE), "pass261-current-state-tier-run"))

import reservation_audit as ra            # noqa: E402
import current_state as p261              # noqa: E402

FIX = os.path.join(HERE, "fixtures-p262")


def fixture(name):
    with open(os.path.join(FIX, name), "rb") as f:
        return f.read()


def text(name):
    return fixture(name).decode("utf-8", "replace")


SCOPED = p261.reservation_verdict_scoped


# ─────────────────────────────────────────────────────────────────────────────
class BytesAreNotCharacters(unittest.TestCase):
    """🔴 The finding that stopped this pass publishing two corrections it did not owe."""

    def test_payload_size_reports_bytes_for_bytes(self):
        self.assertEqual(ra.payload_size(b"abc"), 3)

    def test_payload_size_reports_bytes_for_str(self):
        # "é" is one character and two bytes.  A sweep that reports characters under-counts.
        self.assertEqual(ra.payload_size("é"), 2)
        self.assertEqual(len("é"), 1)

    def test_size_disagreement_names_the_delta(self):
        b, c, d = ra.size_disagreement("héllo")
        self.assertEqual((b, c, d), (6, 5, 1))

    def test_ascii_payload_has_no_delta(self):
        _b, _c, d = ra.size_disagreement("plain ascii")
        self.assertEqual(d, 0)

    def test_the_two_real_payloads_that_caused_it(self):
        # 🔴 dssg's LICENSE: the shelf-shaped byte figure and the char figure differ.
        b, c, d = ra.size_disagreement(fixture("dssg-LICENSE.uchicago.txt"))
        self.assertEqual(b, 2069)
        self.assertGreater(d, 0, "this fixture is the one that exposed the bug")
        self.assertEqual(b - c, d)

    def test_sdv_payload_byte_size_is_the_published_quantity(self):
        self.assertEqual(ra.payload_size(fixture("sdv-LICENSE.busl.txt")), 4818)


# ─────────────────────────────────────────────────────────────────────────────
class StewardReservation(unittest.TestCase):
    """🔴 `sdv-dev/SDV`: the third-party reservation `p261`'s scoped guard cannot see."""

    def setUp(self):
        self.busl = text("sdv-LICENSE.busl.txt")

    def test_p261_guard_answers_reserved_on_the_busl_payload(self):
        # The premise of the whole finding.  If this ever stops being true the finding is
        # stale and this control says so rather than the prose.
        self.assertEqual(SCOPED(self.busl), "RESERVED")

    def test_aggregate_sections_is_empty_so_the_scoped_guard_is_blind(self):
        # 🔵 This is WHY p261's fix cannot reach it: a steward notice is a SENTENCE, not a
        # rule-delimited SECTION, so there is no span to scope to.
        self.assertEqual(p261.aggregate_sections(self.busl), [])
        start, end = p261.subject_span(self.busl)
        self.assertEqual(start, 0)
        self.assertEqual(end, len(self.busl.splitlines()))

    def test_p262_names_it_a_steward_reservation(self):
        self.assertEqual(ra.reservation_verdict_v2(self.busl, scoped=SCOPED),
                         ra.V_STEWARD)

    def test_the_steward_notice_is_found_at_its_line(self):
        spans = ra.steward_reservation_spans(self.busl)
        self.assertEqual(len(spans), 1)
        line = self.busl.splitlines()[spans[0] - 1]
        self.assertIn("MariaDB", line)
        self.assertIn("License text copyright", line)

    def test_the_steward_is_one_this_base_has_read(self):
        self.assertEqual(ra.names_known_steward(self.busl), ["MariaDB Corporation Ab"])

    def test_the_subject_holder_is_not_the_reserving_party(self):
        # DataCebo is the Licensor; MariaDB reserves rights in the FORM.  The two must not
        # be confused, which is the entire content of the verdict.
        self.assertIn("DataCebo", self.busl)
        notice = self.busl.splitlines()[ra.steward_reservation_spans(self.busl)[0] - 1]
        self.assertNotIn("DataCebo", notice)

    def test_a_payload_with_no_steward_notice_is_not_a_steward_reservation(self):
        self.assertEqual(ra.steward_reservation_spans(text("nosuggest-LICENSE.txt")), [])

    def test_elastic_2_0_carries_no_steward_reservation(self):
        # 🔵 Measured, not assumed: not every source-available form reserves in its text.
        soda = text("soda-core-LICENSE.elastic.txt")
        self.assertEqual(ra.steward_reservation_spans(soda), [])
        self.assertEqual(ra.reservation_verdict_v2(soda, scoped=SCOPED), ra.V_NONE)

    def test_an_unknown_steward_is_reported_rather_than_blessed(self):
        made_up = "License text copyright (c) 2030 Some Other Body, All Rights Reserved."
        self.assertEqual(len(ra.steward_reservation_spans(made_up)), 1)
        self.assertEqual(ra.names_known_steward(made_up), [])


# ─────────────────────────────────────────────────────────────────────────────
class WidenedPermissiveTest(unittest.TestCase):
    """🔴 `dssg/student-early-warning`: a real grant that `p261` graded as a refusal."""

    def setUp(self):
        self.uc = text("dssg-LICENSE.uchicago.txt")

    def test_p261_guard_calls_the_uchicago_grant_a_reservation(self):
        self.assertEqual(SCOPED(self.uc), "RESERVED")

    def test_the_payload_does_grant(self):
        self.assertIsNotNone(ra.permissive_grant(self.uc))

    def test_it_is_the_x11_variant_not_mit(self):
        # MIT's exact phrase is absent; that absence is the whole bug.
        self.assertNotIn("free of charge", self.uc.lower())
        self.assertIn("permission to use, copy, modify, and distribute", self.uc.lower())

    def test_p262_calls_it_a_conditional_grant(self):
        self.assertEqual(ra.reservation_verdict_v2(self.uc, scoped=SCOPED),
                         ra.V_CONDITIONAL)

    def test_the_field_of_use_limits_are_named(self):
        limits = ra.field_of_use_limits(self.uc)
        self.assertTrue(limits, "a conditional grant must say what the condition is")

    def test_conditional_is_not_the_same_as_usable(self):
        # 🔵 p257's lesson: "there is a grant" and "a studio may ship it" are different
        # questions.  CONDITIONAL-GRANT answers the first and refuses the second.
        self.assertNotEqual(ra.V_CONDITIONAL, ra.V_BOILERPLATE)
        self.assertIn(ra.V_CONDITIONAL, ra.ALL_VERDICTS)

    def test_bsd_boilerplate_is_still_boilerplate(self):
        for name in ("x5moodle-LICENSE.bsd2.txt", "opentutorai-LICENSE.bsd3.txt"):
            with self.subTest(name):
                body = text(name)
                self.assertEqual(SCOPED(body), "BOILERPLATE")
                self.assertEqual(ra.reservation_verdict_v2(body, scoped=SCOPED),
                                 ra.V_BOILERPLATE)

    def test_a_bare_refusal_is_still_reserved(self):
        ns = text("nosuggest-LICENSE.txt")
        self.assertEqual(ra.reservation_verdict_v2(ns, scoped=SCOPED), ra.V_RESERVED)
        self.assertIsNone(ra.permissive_grant(ns))

    def test_isc_phrasing_is_recognised(self):
        isc = ("Permission to use, copy, modify, and/or distribute this software for any "
               "purpose with or without fee is hereby granted.")
        self.assertIsNotNone(ra.permissive_grant(isc))

    def test_the_widening_does_not_bless_a_refusal_that_merely_says_permission(self):
        hostile = ("All rights reserved.  No permission to use, copy or modify this "
                   "software is granted to anyone.")
        self.assertEqual(ra.reservation_verdict_v2(hostile, scoped=SCOPED), ra.V_RESERVED)


# ─────────────────────────────────────────────────────────────────────────────
class ThirdPartyReservationStillHolds(unittest.TestCase):
    """`p261`'s `nextSIS` verdict must survive every widening this module adds."""

    def test_nextsis_remains_third_party(self):
        p = os.path.join(os.path.dirname(HERE), "pass261-current-state-tier-run",
                         "fixtures-p261")
        cands = [f for f in os.listdir(p) if "nextsis" in f.lower()] if os.path.isdir(p) else []
        if not cands:
            self.skipTest("p261's nextSIS fixture is not in this checkout")
        with open(os.path.join(p, cands[0]), encoding="utf-8", errors="replace") as fh:
            body = fh.read()
        self.assertEqual(SCOPED(body), "THIRD-PARTY-RESERVATION")
        self.assertEqual(ra.reservation_verdict_v2(body, scoped=SCOPED), ra.V_THIRD_PARTY)

    def test_an_aggregate_verdict_is_never_downgraded_by_the_widened_grant_test(self):
        # A synthetic aggregate: a permissive subject span plus somebody else's reservation.
        body = "\n".join([
            "-" * 30, "1. MIT License", "-" * 30,
            "Permission is hereby granted, free of charge, to any person obtaining a copy",
            "-" * 30, "2. Vendor License", "-" * 30,
            "Copyright (c) 2020 Vendor.  All rights reserved.",
        ])
        self.assertEqual(SCOPED(body), "THIRD-PARTY-RESERVATION")
        self.assertEqual(ra.reservation_verdict_v2(body, scoped=SCOPED), ra.V_THIRD_PARTY)


# ─────────────────────────────────────────────────────────────────────────────
class CellRole(unittest.TestCase):
    """🔴 A row's state is not what the row QUOTES — the guard that saved a correction."""

    def test_the_twenty_header_is_a_claim_column(self):
        self.assertEqual(ra.cell_role("what the secondary source said"), ra.ROLE_QUOTED)

    def test_an_ordinary_grant_header_is_a_verdict_column(self):
        for h in ("grant, read first-hand", "licence", "what these shelves say today",
                  "grant", "licencia"):
            with self.subTest(h):
                self.assertEqual(ra.cell_role(h), ra.ROLE_VERDICT)

    def test_the_other_claim_headers_this_base_writes(self):
        for h in ("what the `README` actually says", "this shelf's cell before today",
                  "README, read today", "what the roundup said", "before today"):
            with self.subTest(h):
                self.assertEqual(ra.cell_role(h), ra.ROLE_QUOTED)

    def test_an_absent_header_defaults_to_verdict(self):
        # 🔵 Defaulting the other way would silence real grades under malformed tables.
        self.assertEqual(ra.cell_role(""), ra.ROLE_VERDICT)
        self.assertEqual(ra.cell_role(None), ra.ROLE_VERDICT)

    def test_quoted_claim_beats_the_restrictive_token(self):
        self.assertEqual(
            ra.grade_class("what the secondary source said",
                           '`BUSL-1.1`, *"source-available, not OSI"*'),
            ra.ROLE_QUOTED)

    def test_the_same_text_under_a_verdict_header_is_a_grade(self):
        self.assertEqual(
            ra.grade_class("grant", '`BUSL-1.1`, *"source-available, not OSI"*'),
            ra.GRADE_RESTRICTIVE)


# ─────────────────────────────────────────────────────────────────────────────
class ScopeNoteIsNotAGrade(unittest.TestCase):
    """A cell that LEADS with a usable family is a verdict of that family."""

    def test_nvda_is_gpl_2_not_proprietary(self):
        cell = "🟡 **`GPL-2.0`** *(`53 408` B)* — ship alongside, do not link into proprietary code"
        self.assertEqual(ra.grade_class("licence", cell), ra.GRADE_SCOPE_NOTE)

    def test_nextsis_cell_is_gpl_3_not_a_reservation(self):
        cell = ("🟢 **`GPL-3.0`** — and the `All rights reserved` in its licence file is "
                "**CodeIgniter's**, not its own")
        self.assertEqual(ra.grade_class("grant", cell), ra.GRADE_SCOPE_NOTE)

    def test_a_bare_restrictive_cell_is_a_grade(self):
        self.assertEqual(ra.grade_class("grant", "🔴 **`Elastic-2.0` — NOT OSI**"),
                         ra.GRADE_RESTRICTIVE)

    def test_cc_by_nc_sa_is_not_read_as_cc_by(self):
        # 🔴 The bug this pass's own first-cut harvester had: a prefix match on `CC-BY`
        # files a non-commercial content licence as usable.
        cell = "🔴 **CC-BY-NC-SA-4.0**, `LICENSE.txt` **20 863 B**"
        self.assertEqual(ra.grade_class("licence", cell), ra.GRADE_RESTRICTIVE)

    def test_cc_by_proper_is_usable(self):
        self.assertIs(ra.leads_with_usable("🟢 **CC-BY-4.0** — attribution only"), True)

    def test_leading_family_reads_the_first_token_only(self):
        self.assertEqual(ra.leading_family("🟡 **`MIT`** then `BUSL-1.1` in `app/pro/`"), "MIT")
        self.assertEqual(ra.leading_family("🔴 **`Elastic-2.0`**"), None)

    def test_leading_family_is_none_for_prose(self):
        self.assertIsNone(ra.leading_family("🔴 **proprietary, stated**"))
        self.assertIsNone(ra.leading_family(""))

    def test_unlicensed_is_not_the_unlicense(self):
        # 🔴 The third prefix collision of this pass, and the only one whose two readings
        # are OPPOSITE: `Unlicense` dedicates to the public domain, `unlicensed` means no
        # grant at all.  A `startswith` reader drops every unlicensed row from the
        # population.
        self.assertIsNone(ra.leading_family("🔴 unlicensed — pattern only"))
        self.assertEqual(ra.leading_family("🟢 **`Unlicense`**"), "Unlicense")

    def test_an_unlicensed_cell_is_a_restrictive_grade(self):
        for cell in ("🔴 unlicensed — **pattern only, do not vendor the code**",
                     "🔴 **both UNLICENSED — read, do not fork**",
                     "absent/unlicensed, COMPONENT"):
            with self.subTest(cell):
                self.assertEqual(ra.grade_class("licence", cell), ra.GRADE_RESTRICTIVE)

    def test_a_family_with_a_version_suffix_is_still_a_family(self):
        for tok, cell in (("Apache-2.0", "🟢 **`Apache-2.0`** — 11 358 B"),
                          ("CC-BY-NC-SA-4.0", "🔴 **CC-BY-NC-SA-4.0** — non-commercial"),
                          ("GPL-3.0", "🟡 **`GPL-3.0`** — copyleft")):
            with self.subTest(tok):
                self.assertEqual(ra.leading_family(cell), tok)

    def test_a_family_name_glued_to_more_letters_is_not_that_family(self):
        self.assertIsNone(ra.leading_family("MITigation of risk"))
        self.assertIsNone(ra.leading_family("GPLv-style wording"))

    def test_a_cell_with_no_restrictive_token_has_no_grade_class(self):
        self.assertIsNone(ra.grade_class("grant", "🟢 **`MIT`** — `1 071` B"))


# ─────────────────────────────────────────────────────────────────────────────
class HeaderDoesNotLeakAcrossTables(unittest.TestCase):
    """🔴 Found by mutation, not by review: `M19` removed `harvest()`'s header reset and
    `56` controls stayed green.

    The reset is what stops one table's `what the secondary source said` header from
    reaching a LATER table's rows.  🔵 **The failure direction is the dangerous one** — a
    stale claim header does not add a false grade, it SILENCES a real one, and a silenced
    restrictive grade is a row this base publishes as usable."""

    def setUp(self):
        import tempfile
        self.dir = tempfile.mkdtemp(prefix="p262-")
        self.path = os.path.join(self.dir, "shelf.md")

    def tearDown(self):
        import shutil
        shutil.rmtree(self.dir, ignore_errors=True)

    def write(self, body):
        with open(self.path, "w", encoding="utf-8") as fh:
            fh.write(body)
        return ra.harvest(self.path)

    def test_a_claim_header_does_not_reach_a_later_tables_rows(self):
        rows = self.write(
            "| repo | what the secondary source said |\n"
            "|---|---|\n"
            "| [a](https://github.com/o/quoted) | `BUSL-1.1` |\n"
            "\n"
            "Some prose between the two tables.\n"
            "\n"
            "| repo | grant |\n"
            "|---|---|\n"
            "| [b](https://github.com/o/graded) | 🔴 **`Elastic-2.0` — NOT OSI** |\n")
        by = {r[0]: r[3] for r in rows}
        self.assertEqual(by["o/quoted"], ra.ROLE_QUOTED)
        self.assertEqual(by["o/graded"], ra.GRADE_RESTRICTIVE,
                         "the second table's own header must govern its rows")

    def test_a_stray_pipe_row_after_prose_is_not_governed_by_a_stale_header(self):
        # No rule line of its own, so only the RESET can stop the claim header reaching it.
        rows = self.write(
            "| repo | what the secondary source said |\n"
            "|---|---|\n"
            "| [a](https://github.com/o/quoted) | `BUSL-1.1` |\n"
            "\n"
            "Prose resets the table context.\n"
            "\n"
            "| [c](https://github.com/o/stray) | 🔴 **proprietary, stated** |\n")
        by = {r[0]: r[3] for r in rows}
        self.assertEqual(by["o/stray"], ra.GRADE_RESTRICTIVE)

    def test_rows_inside_one_table_do_keep_its_header(self):
        rows = self.write(
            "| repo | what the secondary source said |\n"
            "|---|---|\n"
            "| [a](https://github.com/o/one) | `BUSL-1.1` |\n"
            "| [b](https://github.com/o/two) | 🔴 **proprietary** |\n")
        by = {r[0]: r[3] for r in rows}
        self.assertEqual(by["o/one"], ra.ROLE_QUOTED)
        self.assertEqual(by["o/two"], ra.ROLE_QUOTED,
                         "the reset must not fire BETWEEN rows of the same table")


# ─────────────────────────────────────────────────────────────────────────────
class HarvestOverTheLiveShelves(unittest.TestCase):
    """The population `ACTION ZI` actually ran over, pinned so a later pass can re-derive it."""

    @classmethod
    def setUpClass(cls):
        root = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
        cls.root = root
        cls.rows = []
        for shelf in ("agents/top.md", "agents/trending.md", "repos/foundations.md",
                      "repos/trending.md", "verticals/solutions.md", "intel/market.md",
                      "intel/trends.md", "compose/patterns.md", "intel/open-gaps.md"):
            p = os.path.join(root, shelf)
            if os.path.exists(p):
                cls.rows.extend(ra.harvest(p))

    def test_the_shelves_are_where_this_module_thinks_they_are(self):
        self.assertTrue(os.path.exists(os.path.join(self.root, "agents", "top.md")),
                        "harvest() is resolving the repository root wrongly")

    def test_the_harvest_is_not_empty(self):
        self.assertGreater(len(self.rows), 20)

    def test_every_row_carries_one_of_the_three_classes(self):
        ok = {ra.GRADE_RESTRICTIVE, ra.GRADE_SCOPE_NOTE, ra.ROLE_QUOTED}
        self.assertTrue(all(r[3] in ok for r in self.rows),
                        sorted({r[3] for r in self.rows} - ok))

    def test_the_twenty_row_is_classified_as_a_quoted_claim(self):
        # 🔴 The single row that, taken as a verdict, re-asserts a claim p249 refuted.
        # 🔴 p265: this pinned the PRESENCE of the row in the live shelves.  p264's
        # rewrite of the six reference documents dropped it legitimately, so the
        # control went red on a shelf edit, not on a classifier regression (measured
        # on a clean HEAD tree).  The classifier's behaviour on that row stays pinned
        # on its fixture elsewhere in this suite; what the LIVE shelves owe is the
        # invariant: if the row is carried, it is carried as a QUOTED claim.
        quoted = {r[0] for r in self.rows if r[3] == ra.ROLE_QUOTED}
        carried = {r[0] for r in self.rows}
        if "twentyhq/twenty" in carried:
            self.assertIn("twentyhq/twenty", quoted)
        else:
            self.assertNotIn("twentyhq/twenty", carried)

    def test_twenty_has_no_live_restrictive_grade_anywhere(self):
        grades = {(r[0], r[3]) for r in self.rows}
        self.assertNotIn(("twentyhq/twenty", ra.GRADE_RESTRICTIVE), grades)

    def test_the_scope_note_class_is_non_empty_and_holds_nvda(self):
        # 🟢 p265: the CLASS must stay non-empty on the live shelves — that is the
        # real regression guard.  The named member is checked only while carried.
        notes = {r[0] for r in self.rows if r[3] == ra.GRADE_SCOPE_NOTE}
        self.assertTrue(notes, "the scope-note class went empty on the live shelves")
        if "nvaccess/nvda" in {r[0] for r in self.rows}:
            self.assertIn("nvaccess/nvda", notes)

    def test_the_restrictive_class_is_non_empty_and_holds_a_known_member(self):
        # 🟢 p265: same repair — the class non-empty is the invariant; the named member
        # is pinned only while the live shelves carry it.
        grades = {r[0] for r in self.rows if r[3] == ra.GRADE_RESTRICTIVE}
        self.assertTrue(grades, "the restrictive class went empty on the live shelves")
        if "jagmarques/asqav-compliance" in {r[0] for r in self.rows}:
            self.assertIn("jagmarques/asqav-compliance", grades)

    def test_anaistack_is_restrictive_not_a_scope_note(self):
        grades = {r[0] for r in self.rows if r[3] == ra.GRADE_RESTRICTIVE}
        self.assertIn("anaistack/cefr-asag-corpus", grades)


# ─────────────────────────────────────────────────────────────────────────────
class ModuleContracts(unittest.TestCase):
    """The refusals this module makes, pinned so a later pass cannot quietly drop them."""

    def test_it_does_not_hold_its_own_copy_of_the_cc_axes(self):
        with open(os.path.join(HERE, "reservation_audit.py"), encoding="utf-8") as fh:
            src = fh.read()
        self.assertNotIn("noncommercial", src.lower().replace("non-commercial", ""),
                         "the CC axes belong to p258; this module must delegate")

    def test_the_p258_classifier_is_reachable(self):
        self.assertIsNot(ra._cc, None,
                         "p258's content classifier must be importable from here")

    def test_classifier_unavailable_is_a_distinct_answer(self):
        # 🔵 p261's rule: a classifier that could not run is a different measurement from a
        # classifier that ran and said nothing.
        self.assertNotIn(ra.CLASSIFIER_UNAVAILABLE,
                         {ra.GRADE_RESTRICTIVE, ra.GRADE_SCOPE_NOTE, ra.ROLE_QUOTED})

    def test_every_verdict_constant_is_in_all_verdicts(self):
        for v in (ra.V_NONE, ra.V_BOILERPLATE, ra.V_RESERVED, ra.V_THIRD_PARTY,
                  ra.V_STEWARD, ra.V_CONDITIONAL):
            self.assertIn(v, ra.ALL_VERDICTS)

    def test_verdict_delta_reports_both_guards(self):
        old, new, changed = ra.verdict_delta(text("sdv-LICENSE.busl.txt"), SCOPED)
        self.assertEqual(old, "RESERVED")
        self.assertEqual(new, ra.V_STEWARD)
        self.assertTrue(changed)

    def test_verdict_delta_reports_agreement_too(self):
        old, new, changed = ra.verdict_delta(text("nosuggest-LICENSE.txt"), SCOPED)
        self.assertEqual(old, new)
        self.assertFalse(changed)

    def test_every_fixture_is_non_empty(self):
        names = [f for f in os.listdir(FIX) if f.endswith(".txt")]
        self.assertGreaterEqual(len(names), 9)
        for n in names:
            with self.subTest(n):
                self.assertGreater(len(fixture(n)), 0)


if __name__ == "__main__":
    unittest.main(verbosity=1)
