"""Controls for `p242-grant-delta`.

Every fixture in `fixtures/` is a payload read FIRST-HAND from
`raw.githubusercontent.com` during pass 242 (2026-10-16), at the branch
`git ls-remote --symref` reported, and is stored byte-for-byte as served. None is
hand-written, because a hand-written licence fixture proves only that the author
and the matcher agree.

  mit-canonical.txt                  RohanMuppa/brightspace-mcp-server   1 068 B
  mit-plus-attribution.txt           AnonymousOnyx22/brightspace-d2l-mcp 1 200 B
  mit-long-holder.txt                sxnnyside-scholarships/promediatum  1 100 B
  agpl-standard.txt                  purysho/EduBoard                   34 523 B
  transition-agpl-to-proprietary.txt snflwr-ai/snflwr.ai                 2 833 B
  polyform.txt                       BreraDMR/calculating_student_grades 4 984 B
  apache-notice-stated.txt           projectfedena/fedena                  680 B
"""

import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from grant_delta import (  # noqa: E402
    CLEAN,
    DISCLOSURE,
    NARROWING,
    STANDARD,
    TRANSITION,
    addition_is_disclosure_only,
    delta_of,
    is_relicensing,
    resolve_mit_plus,
)

FIX = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fixtures")


def fx(name):
    with open(os.path.join(FIX, name), encoding="utf-8", errors="replace") as fh:
        return fh.read()


# `willwearing/graspful`'s clause 2, as quoted verbatim in p1054's README. This is the
# one fixture that is a QUOTE rather than a whole file: the repo's own payload is
# p1054's to hold, and this suite only needs the clause to prove NARROWING still wins.
GRASPFUL_CLAUSE = """O'Saasy License Agreement

Copyright (c) 2026 Will Wearing

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, subject to the following conditions:

1. The above copyright notice shall be included in all copies.

2. No licensee or downstream recipient may use the Software (including any
modified or derivative versions) to directly compete with the original Licensor
by offering it to third parties as a hosted, managed, or Software-as-a-Service
(SaaS) product or cloud service where the primary value of the service is the
functionality of the Software itself.
"""


class TheHeadline(unittest.TestCase):
    """An MIT body plus an UPSTREAM ATTRIBUTION is usable, and p1054 said it was not."""

    def test_attribution_is_disclosure_not_narrowing(self):
        d = delta_of(fx("mit-plus-attribution.txt"))
        self.assertEqual(d["kind"], DISCLOSURE)
        self.assertEqual(d["narrowing_hits"], [])
        self.assertGreater(d["disclosure_hits"], 0)

    def test_attribution_resolves_p1054_to_usable(self):
        r = resolve_mit_plus(fx("mit-plus-attribution.txt"))
        self.assertEqual(r["p1054_verdict"], "MIT-BODY-PLUS:unclassified-addition")
        self.assertEqual(r["delta_kind"], DISCLOSURE)
        self.assertEqual(r["resolution"], "RESOLVED-disclosure-only")
        self.assertTrue(r["usable_permissive"])

    def test_the_excess_is_fifty_bytes_and_it_is_the_attribution(self):
        """Pin the measurement, so a later pass can see if the payload changed."""
        r = resolve_mit_plus(fx("mit-plus-attribution.txt"))
        self.assertEqual(r["bytes"], 1200)
        self.assertEqual(r["p1054_excess"], 50)

    def test_the_named_upstream_is_itself_canonical_mit(self):
        """The disclosure is only reassuring because the upstream grant was READ."""
        up = delta_of(fx("mit-canonical.txt"))
        self.assertEqual(up["kind"], STANDARD)
        self.assertEqual(up["standard_family"], "MIT")
        self.assertEqual(up["bytes"], 1068)
        self.assertTrue(addition_is_disclosure_only(fx("mit-plus-attribution.txt")))
        self.assertFalse(addition_is_disclosure_only(fx("mit-canonical.txt")))


class ActionVU(unittest.TestCase):
    """`ACTION VU` as registered fires on ordinary copyleft. As corrected, it does not."""

    def test_standard_agpl_is_not_a_relicensing(self):
        text = fx("agpl-standard.txt")
        self.assertFalse(is_relicensing(text))
        d = delta_of(text)
        self.assertNotEqual(d["kind"], TRANSITION)

    def test_standard_agpl_names_gpl_as_its_own_cross_reference(self):
        """The reason VU over-fired: the AGPL text NAMES the GPL. P171, one level up."""
        d = delta_of(fx("agpl-standard.txt"))
        self.assertTrue(d["standard_cross_reference"])

    def test_fsf_publication_dates_are_not_material(self):
        """`19 November 2007` is the AGPL's own date, not an effective date."""
        d = delta_of(fx("agpl-standard.txt"))
        for stamp in ("19 november 2007", "28 march 2007", "29 june 2007"):
            self.assertNotIn(stamp, d["material_dates"])

    def test_the_real_relicensing_is_detected(self):
        text = fx("transition-agpl-to-proprietary.txt")
        self.assertTrue(is_relicensing(text))
        d = delta_of(text)
        self.assertEqual(d["kind"], TRANSITION)
        self.assertIn("2026-09-18", d["material_dates"])
        self.assertIn("2026-02-27", d["material_dates"])

    def test_transition_outranks_its_own_third_party_disclosure(self):
        """snflwr.ai ALSO carries a third-party notice. The transition must win:
        it is the fact that decides whether a studio may use the code at all."""
        text = fx("transition-agpl-to-proprietary.txt")
        d = delta_of(text)
        self.assertEqual(d["kind"], TRANSITION)
        self.assertGreater(d["transition_hits"], 0)


class NarrowingStillWins(unittest.TestCase):
    """The relaxation must not reach a payload that actually restricts."""

    def test_graspful_clause_is_narrowing(self):
        d = delta_of(GRASPFUL_CLAUSE)
        self.assertEqual(d["kind"], NARROWING)
        self.assertTrue(d["narrowing_hits"])

    def test_graspful_is_not_cleared_by_resolution(self):
        r = resolve_mit_plus(GRASPFUL_CLAUSE)
        self.assertFalse(r["usable_permissive"])
        self.assertEqual(r["delta_kind"], NARROWING)

    def test_attribution_plus_a_saas_clause_is_still_narrowing(self):
        """A licensor who discloses provenance AND restricts use is restricting."""
        both = fx("mit-plus-attribution.txt") + (
            "\n\nAdditional term: you may not offer this Software as a "
            "Software-as-a-Service product.\n"
        )
        self.assertEqual(delta_of(both)["kind"], NARROWING)
        self.assertFalse(resolve_mit_plus(both)["usable_permissive"])
        self.assertFalse(addition_is_disclosure_only(both))


class RefusalIsStillTheDefault(unittest.TestCase):
    """p241's rule: the absence of known restriction vocabulary is NEVER permission."""

    def test_unreadable_addition_stays_unresolved(self):
        """An addition in a vocabulary no list here knows must NOT be cleared."""
        unknown = fx("mit-canonical.txt") + (
            "\n\nZusatzbedingung: Die Nutzung ist ausschliesslich fuer "
            "Bildungszwecke an oeffentlichen Schulen zulaessig, und jede andere "
            "Verwendung bedarf der vorherigen schriftlichen Zustimmung des "
            "Urhebers in Textform nach deutschem Recht.\n"
        )
        r = resolve_mit_plus(unknown)
        self.assertEqual(r["p1054_verdict"], "MIT-BODY-PLUS:unclassified-addition")
        self.assertEqual(r["resolution"], "UNRESOLVED-addition-unreadable")
        self.assertFalse(r["usable_permissive"])

    def test_a_canonical_payload_is_not_disclosure(self):
        """Clearing needs POSITIVE evidence — a plain payload must not read as one."""
        self.assertEqual(delta_of(fx("mit-canonical.txt"))["kind"], STANDARD)
        self.assertFalse(addition_is_disclosure_only(fx("mit-canonical.txt")))

    def test_long_copyright_holder_is_not_an_addition(self):
        """promediatum is 1 100 B purely because its holder name is long."""
        text = fx("mit-long-holder.txt")
        self.assertEqual(delta_of(text)["kind"], STANDARD)
        r = resolve_mit_plus(text)
        self.assertEqual(r["p1054_verdict"], "MIT")
        self.assertTrue(r["usable_permissive"])
        self.assertEqual(r["bytes"], 1100)


class OtherFamilies(unittest.TestCase):
    """This module reads the DELTA; it never pretends to be the family classifier."""

    def test_polyform_is_standard_text_not_an_addition(self):
        """PolyForm Noncommercial IS restrictive — and that is the FAMILY classifier's
        answer, not this module's. Its `noncommercial` is its own term, so there is no
        delta here to grade. `lib/license_family.sh` already returns `PolyForm`."""
        d = delta_of(fx("polyform.txt"))
        self.assertEqual(d["kind"], STANDARD)
        self.assertEqual(d["standard_family"], "PolyForm")

    def test_apache_notice_is_disclosure(self):
        """fedena's root NOTICE discloses provenance; it is not a grant body.
        The shelves already record it as STATED-not-BODIED (p210/P214-2)."""
        d = delta_of(fx("apache-notice-stated.txt"))
        self.assertEqual(d["kind"], DISCLOSURE)
        self.assertEqual(d["narrowing_hits"], [])

    def test_disclosure_does_not_assert_a_family(self):
        """DISCLOSURE on a NOTICE must not be read as 'usable Apache-2.0'.
        resolve_mit_plus only speaks about MIT bodies, and a NOTICE is not one."""
        r = resolve_mit_plus(fx("apache-notice-stated.txt"))
        self.assertEqual(r["p1054_verdict"], "NOT-MIT-BODY")
        self.assertFalse(r["usable_permissive"])


class TheDefectThisModuleFoundInItself(unittest.TestCase):
    """The first full sweep returned NARROWING on all 8 GPL/AGPL payloads, because
    `p1054`'s vocabulary contains `noncommercial` and the STANDARD GPL-3.0 text uses
    that word in its section 6. That is `P171`'s class a third time, committed by the
    instrument built to stop it. These controls are why it cannot come back."""

    def test_standard_copyleft_is_not_narrowing(self):
        d = delta_of(fx("agpl-standard.txt"))
        self.assertEqual(d["kind"], STANDARD)
        self.assertEqual(d["standard_family"], "GPL-family")

    def test_the_offending_token_is_still_present_in_the_payload(self):
        """Proof the control is load-bearing: the word IS there, and is not read as
        an addition. If a later pass deletes the STANDARD branch, this fails."""
        text = fx("agpl-standard.txt")
        self.assertIn("noncommercial", text.lower())
        self.assertIn("noncommercial", delta_of(text)["narrowing_hits"])
        self.assertEqual(delta_of(text)["kind"], STANDARD)

    def test_mit_is_held_to_a_stricter_test_than_the_long_licences(self):
        """The asymmetry, stated as a control. A narrowing clause SHORTER than
        `p1054`'s size headroom must still be graded, because MIT's canonical text
        carries no restriction vocabulary at all."""
        self.assertLess(len(GRASPFUL_CLAUSE.encode()), 1150)
        self.assertEqual(delta_of(GRASPFUL_CLAUSE)["kind"], NARROWING)
        self.assertEqual(delta_of(GRASPFUL_CLAUSE)["standard_family"], "")

    def test_a_transition_bolted_onto_standard_text_still_reads_as_transition(self):
        """STANDARD must not shadow a relicensing notice appended to a licence body."""
        text = (
            "Effective 2026-09-18.\n\nThis software was published under the GNU "
            "Affero General Public License, version 3, from 2026-02-27 until "
            "2026-09-18.\n\n" + fx("agpl-standard.txt")
        )
        self.assertEqual(delta_of(text)["kind"], TRANSITION)
        self.assertTrue(is_relicensing(text))


class Portability(unittest.TestCase):
    """p355-cwd-portability: the sibling import must survive `python3 -I`."""

    def test_p1054_vocabulary_is_imported_not_copied(self):
        import grant_delta

        self.assertIn("saas", grant_delta.RESTRICTION_TERMS)
        self.assertIs(grant_delta.RESTRICTION_TERMS, grant_delta._p1054.RESTRICTION_TERMS)


if __name__ == "__main__":
    unittest.main(verbosity=2)
