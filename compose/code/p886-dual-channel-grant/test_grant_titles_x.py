"""p886 controls — stdlib unittest only, no network. Every fixture is a payload
byte-read from the repository named, during p886, and its size is asserted so a
silently-truncated fixture cannot pass the suite.
"""
import os
import unittest

import os
import sys
# p923: `python3 -I` (the Makefile's own invocation) strips the SCRIPT'S OWN DIRECTORY from
# sys.path, so a bare sibling import fails at IMPORT time -- before one assertion runs.  This is
# the idiom 234 of this tree's 306 test files already carry; these two did not, and `923-F8`
# measured what that cost.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import grant_titles_x as X

F = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fixtures")


def body(name):
    with open(os.path.join(F, name), encoding="utf-8", errors="replace") as fh:
        return fh.read()


def first_title(text):
    """Apply the earliest-title rule over the p886 rows alone."""
    import re
    best = None
    for fam, pat in X.TITLES_X:
        m = re.compile(pat, re.I).search(text)
        if m and (best is None or m.start() < best[1]):
            best = (fam, m.start())
    return best[0] if best else None


class FixtureIntegrity(unittest.TestCase):
    """A fixture that silently shrank would make every other control vacuous."""

    SIZES = {
        "i-diario.LICENSE.pt": 35326,
        "os-taxonomy.LICENSE": 25289,
        "frappe-education.license.txt": 19,
        "MinerU.LICENSE.md": 3301,
        "DeepTutor.LICENSE": 11408,
        "openedx-XBlock.LICENSE.TXT": 11358,
        "oppia_oppia.LICENSE": 11358,
        "OpenOLAT_OpenOLAT.LICENSE": 10982,
        "Cvmcosta_ltijs.LICENSE": 11361,
        "Ed-Fi-Alliance-OSS_Ed-Fi-ODS.LICENSE": 10172,
    }

    def test_sizes(self):
        for name, size in self.SIZES.items():
            self.assertEqual(os.path.getsize(os.path.join(F, name)), size, name)


class IberianGnuTitles(unittest.TestCase):
    def test_portuguese_agpl_is_recognised(self):
        """`portabilis/i-diario` — the row the English-only gate abstained on."""
        self.assertEqual(first_title(body("i-diario.LICENSE.pt")), "AGPL-3.0")

    def test_portuguese_version_line_resolves(self):
        self.assertTrue(X.VER3_X.search(body("i-diario.LICENSE.pt")))

    def test_portuguese_gpl_pattern_does_NOT_match_an_agpl_body(self):
        """The overlap control. `AFFERO` sits between `GERAL` and `GNU`, so the
        GPL title cannot match an AGPL body -- the same structural property that
        makes the rule sound in English. If this ever fails, the earliest-title
        rule is unsafe in Portuguese and a copyleft grant would be published one
        family too permissive."""
        import re
        gpl_pats = [p for f, p in X.TITLES_X if f == "GPL"]
        text = body("i-diario.LICENSE.pt")
        agpl_at = min(m.start() for m in
                      [re.search(p, text, re.I) for f, p in X.TITLES_X if f == "AGPL-3.0"]
                      if m)
        for p in gpl_pats:
            m = re.search(p, text, re.I)
            if m:
                self.assertGreater(m.start(), agpl_at,
                                   "a GPL title matched EARLIER than the AGPL title")

    def test_accents_are_optional_both_ways(self):
        import re
        pat = [p for f, p in X.TITLES_X if f == "AGPL-3.0"][0]
        for v in ["LICENÇA PÚBLICA GERAL AFFERO GNU",
                  "LICENCA PUBLICA GERAL AFFERO GNU",
                  "licença pública geral affero gnu"]:
            self.assertTrue(re.search(pat, v, re.I), v)

    def test_spanish_variants(self):
        self.assertEqual(first_title("LICENCIA PÚBLICA GENERAL AFFERO DE GNU"), "AGPL-3.0")
        self.assertEqual(first_title("LICENCIA PÚBLICA GENERAL DE GNU"), "GPL")
        self.assertEqual(first_title("LICENCIA PÚBLICA GENERAL REDUCIDA DE GNU"), "LGPL")


class OpenDataCommons(unittest.TestCase):
    def test_odbl_is_recognised(self):
        """`withmarbleapp/os-taxonomy` — both shelves flag it red; the gate could
        not corroborate the flag."""
        self.assertEqual(first_title(body("os-taxonomy.LICENSE")), "ODbL-1.0")

    def test_odbl_is_not_reported_as_permissive_code(self):
        self.assertNotIn(first_title(body("os-taxonomy.LICENSE")),
                         ("MIT", "Apache-2.0", "BSD-3-Clause", "ISC"))


class BareTokenGrants(unittest.TestCase):
    def test_frappe_education_19_bytes(self):
        got = X.bare_token_grant(body("frappe-education.license.txt"))
        self.assertIsNotNone(got, "a 19-byte 'License: GNU GPL V3' must not read as absence")
        self.assertEqual(got[0], "GPL-3.0-DECLARED")

    def test_declared_suffix_is_distinguishable(self):
        """A declaration must never be indistinguishable from a byte-read body."""
        got = X.bare_token_grant("License: MIT")
        self.assertTrue(got[0].endswith("-DECLARED"))

    def test_a_real_body_is_not_a_bare_token(self):
        """The length guard AND the operative-language guard, on real bodies."""
        for name in ("DeepTutor.LICENSE", "i-diario.LICENSE.pt",
                     "openedx-XBlock.LICENSE.TXT"):
            self.assertIsNone(X.bare_token_grant(body(name)), name)

    def test_short_payload_with_operative_language_is_not_a_token(self):
        self.assertIsNone(X.bare_token_grant(
            "MIT. Permission is hereby granted, free of charge, to any person."))

    def test_agpl_token_does_not_fall_through_to_gpl(self):
        self.assertEqual(X.bare_token_grant("Licensed under the GNU AGPL v3")[0],
                         "AGPL-3.0-DECLARED")

    def test_empty_payload_is_not_a_grant(self):
        self.assertIsNone(X.bare_token_grant(""))
        self.assertIsNone(X.bare_token_grant("   \n  "))


class AdditionalTermsRider(unittest.TestCase):
    def test_mineru_rider_is_detected(self):
        self.assertTrue(X.additional_terms_rider(body("MinerU.LICENSE.md")))

    def test_p872_false_positive_set_stays_clean(self):
        """🔴 THE REGRESSION THAT MATTERS. `agents/top.md` records that a substring
        grep for `additional terms` false-positives on 100% of Apache-2.0 bodies,
        because Apache-2.0 §5 reads "without any additional terms or conditions".
        p872 hit this on seven of this KB's own rows and discarded the flag rather
        than publishing it. These are four of those seven, byte-read in p886. If
        this test fails, p886 has republished p872's discarded false positive."""
        for name in ("DeepTutor.LICENSE", "Cvmcosta_ltijs.LICENSE",
                     "Ed-Fi-Alliance-OSS_Ed-Fi-ODS.LICENSE", "oppia_oppia.LICENSE",
                     "openedx-XBlock.LICENSE.TXT"):
            self.assertFalse(X.additional_terms_rider(body(name)),
                             "%s is plain Apache-2.0 and must NOT be flagged" % name)

    def test_apache_section5_phrase_alone_does_not_trip_it(self):
        self.assertFalse(X.additional_terms_rider(
            "You may not offer or impose any terms without any additional terms "
            "or conditions of this License."))

    def test_non_apache_copyleft_body_is_clean(self):
        self.assertFalse(X.additional_terms_rider(body("OpenOLAT_OpenOLAT.LICENSE")))


if __name__ == "__main__":
    unittest.main(verbosity=2)
