#!/usr/bin/env python3
"""Controls for p1058.  Every fixture is a payload READ FIRST-HAND at pass 243,
from `raw.githubusercontent.com` at the branch `git ls-remote --symref` reported.

The control that matters most is `test_gpl3_section13_still_in_payload`: it asserts
the offending word is STILL THERE and still not read as evidence, so deleting the
guard fails the suite rather than quietly passing it.  That is p242's rule, kept.
"""
import hashlib
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from empty_payload_gate import (  # noqa: E402
    SHA256_EMPTY, canonical_body_of, family_token_evidence, grant_qualifier,
    is_usable_grant, payload_state, report,
)

FIX = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fixtures")


def fx(name):
    with open(os.path.join(FIX, name), encoding="utf-8", errors="replace") as fh:
        return fh.read()


class EmptyPayload(unittest.TestCase):
    """1 — the headline: a 200 at the declared path with zero bytes."""

    def test_meineschule_license_is_zero_bytes(self):
        body = fx("meineschule-digital.LICENSE.empty")
        self.assertEqual(len(body), 0)

    def test_empty_payload_sha_is_the_empty_string_sha(self):
        body = fx("meineschule-digital.LICENSE.empty")
        self.assertEqual(hashlib.sha256(body.encode()).hexdigest(), SHA256_EMPTY)

    def test_state_is_empty_payload_not_a_family(self):
        self.assertEqual(payload_state(fx("meineschule-digital.LICENSE.empty")),
                         "EMPTY-PAYLOAD")

    def test_empty_payload_is_not_usable(self):
        self.assertFalse(is_usable_grant(fx("meineschule-digital.LICENSE.empty")))

    def test_whitespace_only_is_also_empty(self):
        self.assertEqual(payload_state("\n\n   \t\n"), "EMPTY-PAYLOAD")
        self.assertFalse(is_usable_grant("   "))

    def test_non_200_is_unreadable_not_empty(self):
        self.assertEqual(payload_state("", 404), "UNREADABLE")
        self.assertEqual(payload_state("MIT License\n\nPermission is hereby granted", 500),
                         "UNREADABLE")

    def test_none_is_unreadable(self):
        self.assertEqual(payload_state(None), "UNREADABLE")

    def test_report_does_not_ask_the_family_question_on_an_empty_payload(self):
        r = report(fx("meineschule-digital.LICENSE.empty"))
        self.assertEqual(r["state"], "EMPTY-PAYLOAD")
        self.assertFalse(r["usable"])
        self.assertIsNone(r["canonical"])
        self.assertEqual(r["grant"][0], "NOT-ASKED")

    def test_a_real_grant_is_non_empty(self):
        self.assertEqual(payload_state(fx("campus-cli.LICENSE.isc")), "NON-EMPTY")
        self.assertTrue(is_usable_grant(fx("campus-cli.LICENSE.isc")))


class SelfReference(unittest.TestCase):
    """2 — P171's class, blocked structurally rather than by deleting a token."""

    def test_edupage_payload_is_gpl3_canonical_body(self):
        self.assertEqual(canonical_body_of(fx("edupage-api.LICENSE.gpl3")), "GPL-3.0")

    def test_gpl3_section13_still_in_payload(self):
        # THE control: the word is present.  Remove the guard and the next test fails.
        body = fx("edupage-api.LICENSE.gpl3").lower()
        self.assertIn("affero", body)
        self.assertIn("use with the gnu affero general public license", body)

    def test_affero_in_gpl3_is_self_reference_not_evidence(self):
        verdict, basis = family_token_evidence(fx("edupage-api.LICENSE.gpl3"), "affero")
        self.assertEqual(verdict, "SELF-REFERENCE")
        self.assertIn("section 13", basis)

    def test_token_absent_is_reported_absent(self):
        verdict, _ = family_token_evidence(fx("campus-cli.LICENSE.isc"), "affero")
        self.assertEqual(verdict, "ABSENT")

    def test_non_canonical_payload_may_be_read_by_the_matcher(self):
        verdict, _ = family_token_evidence(
            "This project is licensed under the GNU Affero General Public License v3.",
            "affero")
        self.assertEqual(verdict, "EVIDENCE")

    def test_canonical_bodies_are_identified_for_the_pass_families(self):
        self.assertEqual(canonical_body_of(fx("hogwarts.LICENSE.sspl")), "SSPL-1.0")
        self.assertEqual(canonical_body_of(fx("aula.LICENCE.polyform-nc")),
                         "PolyForm-Noncommercial-1.0.0")

    def test_a_short_permissive_grant_is_not_a_canonical_copyleft_body(self):
        self.assertIsNone(canonical_body_of(fx("campus-cli.LICENSE.isc")))


class GrantQualifier(unittest.TestCase):
    """3 — the restriction placed BEFORE the grant verb."""

    def test_mit_sentence_is_verbatim_in_the_chinese_payload(self):
        body = fx("123xiaojun.LICENSE.mit-prefixed-nc").lower()
        self.assertIn("permission is hereby granted, free of charge, to any person "
                      "obtaining", body)

    def test_the_qualifier_is_detected(self):
        verdict, basis = grant_qualifier(fx("123xiaojun.LICENSE.mit-prefixed-nc"))
        self.assertEqual(verdict, "QUALIFIED-GRANT")
        self.assertIn("non-commercial", basis)

    def test_plain_mit_is_unqualified(self):
        verdict, _ = grant_qualifier(fx("nfc-attendance-reader.LICENSE.mit-plus-scope"))
        self.assertEqual(verdict, "UNQUALIFIED-GRANT")

    def test_truncated_mit_is_still_an_unqualified_grant(self):
        # 797 B, holderless, warranty clause cut off mid-paragraph: defective, granted.
        verdict, _ = grant_qualifier(fx("webuntis-ha.LICENSE.mit-truncated"))
        self.assertEqual(verdict, "UNQUALIFIED-GRANT")

    def test_isc_grant_verb_is_recognised(self):
        verdict, _ = grant_qualifier(fx("campus-cli.LICENSE.isc"))
        self.assertEqual(verdict, "UNQUALIFIED-GRANT")

    def test_gpl3_section6_noncommercially_is_not_a_qualifier(self):
        # p242-grant-delta returned NARROWING on all 8 copyleft payloads for exactly
        # this reason.  The canonical body's own words are its terms.
        body = fx("edupage-api.LICENSE.gpl3")
        self.assertIn("noncommercially", body.lower())
        verdict, basis = grant_qualifier(body)
        self.assertEqual(verdict, "UNQUALIFIED-GRANT")
        self.assertIn("GPL-3.0", basis)
        self.assertIn("window not read", basis)

    def test_sspl_is_not_reported_as_a_qualified_grant(self):
        verdict, _ = grant_qualifier(fx("hogwarts.LICENSE.sspl"))
        self.assertEqual(verdict, "UNQUALIFIED-GRANT")

    def test_no_grant_verb_is_reported_as_such(self):
        verdict, _ = grant_qualifier("Copyright (c) 2026 X. All rights reserved.")
        self.assertEqual(verdict, "NO-GRANT-VERB")

    def test_a_restriction_far_from_the_grant_is_not_attributed_to_it(self):
        text = ("Permission is hereby granted, free of charge, to any person "
                "obtaining a copy. " + ("filler. " * 60) + "Non-commercial users "
                "should contact us for support.")
        verdict, _ = grant_qualifier(text)
        self.assertEqual(verdict, "UNQUALIFIED-GRANT")

    def test_the_window_boundary_is_exercised_from_both_sides(self):
        near = "For non-commercial purposes, permission is hereby granted"
        self.assertEqual(grant_qualifier(near)[0], "QUALIFIED-GRANT")
        far = "non-commercial " + ("x" * 200) + " permission is hereby granted"
        self.assertEqual(grant_qualifier(far)[0], "UNQUALIFIED-GRANT")


class Integration(unittest.TestCase):
    def test_every_fixture_is_readable_and_reported(self):
        names = sorted(os.listdir(FIX))
        self.assertEqual(len(names), 8)
        for n in names:
            r = report(fx(n))
            self.assertIn(r["state"], ("EMPTY-PAYLOAD", "NON-EMPTY"))

    def test_only_one_fixture_is_empty(self):
        empties = [n for n in sorted(os.listdir(FIX))
                   if payload_state(fx(n)) == "EMPTY-PAYLOAD"]
        self.assertEqual(empties, ["meineschule-digital.LICENSE.empty"])

    def test_only_one_fixture_carries_a_qualified_grant(self):
        q = [n for n in sorted(os.listdir(FIX))
             if grant_qualifier(fx(n))[0] == "QUALIFIED-GRANT"]
        self.assertEqual(q, ["123xiaojun.LICENSE.mit-prefixed-nc"])


if __name__ == "__main__":
    unittest.main(verbosity=0)
