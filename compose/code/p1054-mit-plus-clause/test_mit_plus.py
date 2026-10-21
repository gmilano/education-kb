"""p187 / P1054 tests — stdlib unittest only, no network, no dependencies.

Run:  python3 -I -m unittest discover -s compose/code/p1054-mit-plus-clause -v
"""

import os
import sys
import unittest

# P241 (pase 241).  `p355-cwd-portability`, y es la razon MECANICA por la que este
# instrumento -- que CLASIFICA BIEN -- nunca entro en `make hooks`.
#
# El docstring de arriba manda correr la suite con `python3 -I -m unittest discover`, y esa
# invocacion es exactamente la que NO PUEDE funcionar: `-I` quita del `sys.path` el
# directorio del script, asi que `from mit_plus import ...` muere con ModuleNotFoundError.
# La suite pasa 16/16 desde su propia carpeta y falla desde cualquier otra, que es la
# condicion que el encabezado del `Makefile` nombra como «the whole reason a working gate
# stayed a one-off: it could not be invoked from the place a hook runs».
#
# Medido en p241: `family_of` (el classifier compartido, EN hooks) devuelve `MIT` pelado
# sobre `savvides/edtechfounderstack` (1 408 B, `800fcaf5fcc1`), y ESTE instrumento lo
# llama `NOT-OPEN-SOURCE:added-restriction` -- correctamente, porque el payload excluye
# `data/operator-lessons.md` del MIT y lo deja en non-commercial.  El veredicto correcto
# existia en este repo desde el pase 188 y no llegaba a la compuerta.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from mit_plus import (
    ALL_VERDICTS,
    LENGTH_IN_BAND,
    LENGTH_LONG,
    LENGTH_SHORT,
    MIT_CANONICAL_HIGH,
    MIT_CANONICAL_LOW,
    USABLE_VERDICTS,
    VERDICT_MIT,
    VERDICT_MIT_PLUS,
    VERDICT_NOT_MIT,
    VERDICT_RESTRICTED,
    VERDICT_SHORT,
    classify,
    is_usable_permissive,
    length_state,
)

# `p252` / `ACTION XQ` — the canonical Commons Clause payload, read from `p207`'s own
# fixture rather than retyped here, so this suite cannot drift from the file the ACTION
# was measured against.  Path is derived from `__file__`: `p355-cwd-portability`.
_FIXTURE = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "..", "p207-permissive-half-audit", "fixtures", "commons-clause-mit.txt",
)
with open(_FIXTURE, encoding="utf-8") as _fh:
    COMMONS_CLAUSE = _fh.read()

# The same payload with the rider block CUT OUT, leaving only the abridged MIT body.
# This is road 2: no rider vocabulary left to hit, so only the length state can refuse.
COMMONS_CLAUSE_NO_RIDER = COMMONS_CLAUSE[COMMONS_CLAUSE.index("MIT License\n\nCopyright"):]

# `p362` — SATA, read from the two fixtures this pass pinned rather than retyped, for the
# same reason the Commons Clause one is read from `p207`'s.
#
#   * the REAL payload: `QingdaoU/Judger`, `newnew/LICENSE`, 1 823 B, the row this pass
#     corrected from a published `MIT` on three shelves;
#   * a SYNTHETIC in-band one, and it is synthetic DELIBERATELY: it is the same rider on
#     an MIT body abridged by about as much as SATA adds, which is the shape the length
#     limb cannot see.  Before this pass added the anchors it graded `MIT` / usable.
_SATA_REAL = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "fixtures", "sata-mit-qingdaou-judger-1823.LICENSE",
)
_SATA_INBAND = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "fixtures", "sata-mit-inband-1072.synthetic.txt",
)
with open(_SATA_REAL, encoding="utf-8") as _fh:
    SATA = _fh.read()
with open(_SATA_INBAND, encoding="utf-8") as _fh:
    SATA_IN_BAND = _fh.read()

# Canonical MIT, padded with a copyright line to land in the measured 1062-1093 B band.
MIT = """MIT License

Copyright (c) 2026 A Licensor

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

# graspful's actual shape: MIT's grant, then a numbered anti-SaaS condition.
OSAASY = """# O'Saasy License Agreement

Copyright 2025, A Licensor.

Permission is hereby granted, free of charge, to any person obtaining a copy of this
software and associated documentation files (the "Software"), to deal in the Software
without restriction, including without limitation the rights to use, copy, modify,
merge, publish, distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to the following
conditions:

1. The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
2. No licensee or downstream recipient may use the Software (including any modified or
derivative versions) to directly compete with the original Licensor by offering it to
third parties as a hosted, managed, or Software-as-a-Service (SaaS) product or cloud
service where the primary value of the service is the functionality of the Software
itself.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF
CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE
OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

APACHE_NOTICE = """Copyright 2016 Newcastle University

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0
"""


class TestGenuineMIT(unittest.TestCase):
    def test_canonical_mit_is_mit(self):
        self.assertEqual(classify(MIT)["verdict"], VERDICT_MIT)

    def test_canonical_mit_is_usable(self):
        self.assertTrue(is_usable_permissive(MIT))

    def test_canonical_mit_lands_in_measured_band(self):
        # The band is an empirical claim about this shelf; if this fails the band moved.
        self.assertTrue(1020 <= classify(MIT)["bytes"] <= 1150, classify(MIT)["bytes"])

    def test_genuine_mit_has_no_restriction_hits(self):
        self.assertEqual(classify(MIT)["hits"], [])

    def test_a_long_copyright_line_alone_does_not_fire(self):
        # The honest failure mode for a size-only probe: a licensor with a long name.
        padded = MIT.replace(
            "Copyright (c) 2026 A Licensor",
            "Copyright (c) 2026 A Very Long Institutional Licensor Name, "
            "Faculty of Education, Some University",
        )
        self.assertEqual(classify(padded)["verdict"], VERDICT_MIT)


class TestTheTrap(unittest.TestCase):
    def test_osaasy_is_not_open_source(self):
        self.assertEqual(classify(OSAASY)["verdict"], VERDICT_RESTRICTED)

    def test_osaasy_is_not_usable_permissive(self):
        self.assertFalse(is_usable_permissive(OSAASY))

    def test_osaasy_still_matches_the_mit_body(self):
        # The whole point: the naive signal fires. It must not be the deciding one.
        self.assertTrue(classify(OSAASY)["mit_body"])

    def test_osaasy_names_the_terms_that_condemn_it(self):
        hits = classify(OSAASY)["hits"]
        self.assertIn("compete", hits)
        self.assertTrue(
            any("software-as-a-service" in h or "saas" in h for h in hits), hits
        )

    def test_osaasy_is_materially_larger_than_canonical(self):
        self.assertGreater(classify(OSAASY)["excess"], 0)


class TestAdjacentShapes(unittest.TestCase):
    def test_apache_notice_is_not_an_mit_body(self):
        # P971's shape must not be swept up by this instrument.
        self.assertEqual(classify(APACHE_NOTICE)["verdict"], VERDICT_NOT_MIT)

    def test_empty_file_is_not_an_mit_body(self):
        self.assertEqual(classify("")["verdict"], VERDICT_NOT_MIT)

    def test_mit_body_with_unknown_addition_is_flagged_not_blessed(self):
        # An added clause written in vocabulary RESTRICTION_TERMS does not know.
        padded = MIT + "\n" + ("Additional bespoke term. " * 60)
        v = classify(padded)
        self.assertEqual(v["verdict"], VERDICT_MIT_PLUS)
        self.assertFalse(is_usable_permissive(padded))

    def test_bytes_is_utf8_length_not_character_count(self):
        self.assertEqual(classify("é")["bytes"], 2)


class TestP252CommonsClauseRider(unittest.TestCase):
    """`ACTION XQ`: the payload this instrument blessed for three passes."""

    def test_fixture_is_the_measured_621_byte_payload(self):
        self.assertEqual(classify(COMMONS_CLAUSE)["bytes"], 621)

    def test_fixture_is_shorter_than_canonical_mit(self):
        self.assertEqual(classify(COMMONS_CLAUSE)["length_state"], LENGTH_SHORT)

    def test_fixture_still_matches_the_mit_body(self):
        # The naive signal fires, exactly as it did at p248. That is the trap.
        self.assertTrue(classify(COMMONS_CLAUSE)["mit_body"])

    def test_fixture_is_refused(self):
        self.assertEqual(classify(COMMONS_CLAUSE)["verdict"], VERDICT_RESTRICTED)

    def test_fixture_is_not_usable_permissive(self):
        # 🔴 `ACTION XQ`'s falsifier. This assertion is the whole discharge: it
        # returned True at p248, p249, p250 and p251.
        self.assertFalse(is_usable_permissive(COMMONS_CLAUSE))

    def test_fixture_names_the_rider_that_condemns_it(self):
        self.assertIn("commons clause", classify(COMMONS_CLAUSE)["riders"])

    def test_the_old_excess_signal_was_blind_to_it(self):
        # Published as a control because it is the STRUCTURAL half of the miss: a
        # byte-excess test cannot see a rider that makes the file shorter.
        self.assertEqual(classify(COMMONS_CLAUSE)["excess"], 0)

    def test_the_old_restriction_vocabulary_was_blind_to_it(self):
        # And the lexical half: none of RESTRICTION_TERMS appears in this payload.
        self.assertEqual(classify(COMMONS_CLAUSE)["hits"], [])


class TestP252TwoRoadsAreIndependent(unittest.TestCase):
    """Each signal must refuse on its own, or the fix is one signal wearing two hats."""

    def test_short_mit_body_with_no_rider_vocabulary_is_still_refused(self):
        v = classify(COMMONS_CLAUSE_NO_RIDER)
        self.assertEqual(v["riders"], [])
        self.assertEqual(v["hits"], [])
        self.assertEqual(v["verdict"], VERDICT_SHORT)
        self.assertFalse(is_usable_permissive(COMMONS_CLAUSE_NO_RIDER))

    def test_a_rider_on_a_full_length_grant_is_caught_by_the_anchor(self):
        # The Commons Clause as it is normally shipped: PREPENDED to a complete MIT
        # text, so the file is LONGER than the band and the length state cannot decide.
        wrapped = (
            '"Commons Clause" License Condition v1.0\n\n'
            "Without limiting other conditions in the License, the grant of rights\n"
            "under the License will not include, and the License does not grant to\n"
            "you, the right to Sell the Software.\n\n" + MIT
        )
        v = classify(wrapped)
        self.assertEqual(v["length_state"], LENGTH_LONG)
        self.assertEqual(v["verdict"], VERDICT_RESTRICTED)
        self.assertFalse(is_usable_permissive(wrapped))

    def test_length_state_boundaries_are_inclusive_at_both_ends(self):
        self.assertEqual(length_state(MIT_CANONICAL_LOW - 1), LENGTH_SHORT)
        self.assertEqual(length_state(MIT_CANONICAL_LOW), LENGTH_IN_BAND)
        self.assertEqual(length_state(MIT_CANONICAL_HIGH), LENGTH_IN_BAND)
        self.assertEqual(length_state(MIT_CANONICAL_HIGH + 1), LENGTH_LONG)

    def test_a_short_file_with_no_mit_body_is_still_NOT_MIT_BODY(self):
        # Precedence control: the absence of an MIT body outranks the length state,
        # so P971's shape does not get relabelled by this pass's new verdict.
        self.assertEqual(classify(APACHE_NOTICE)["verdict"], VERDICT_NOT_MIT)
        self.assertEqual(classify("")["verdict"], VERDICT_NOT_MIT)


class TestP252ConsumingArmIsClosed(unittest.TestCase):
    """`p248`'s hazard: a new state that falls through into the permissive branch."""

    def test_every_verdict_is_graded(self):
        # Adding a verdict without deciding its usability fails HERE, not in a row.
        for v in ALL_VERDICTS:
            self.assertEqual(v in USABLE_VERDICTS, v == VERDICT_MIT, v)

    def test_exactly_one_verdict_is_usable(self):
        self.assertEqual(set(USABLE_VERDICTS), {VERDICT_MIT})

    def test_the_new_state_was_refused_before_it_was_emitted(self):
        self.assertNotIn(VERDICT_SHORT, USABLE_VERDICTS)

    def test_all_verdicts_are_distinct(self):
        self.assertEqual(len(set(ALL_VERDICTS)), len(ALL_VERDICTS))


class TestP252NoRegression(unittest.TestCase):
    def test_genuine_mit_is_in_band_and_still_usable(self):
        v = classify(MIT)
        self.assertEqual(v["length_state"], LENGTH_IN_BAND)
        self.assertEqual(v["verdict"], VERDICT_MIT)
        self.assertTrue(is_usable_permissive(MIT))

    def test_osaasy_is_unchanged_by_the_new_state(self):
        v = classify(OSAASY)
        self.assertEqual(v["verdict"], VERDICT_RESTRICTED)
        self.assertEqual(v["length_state"], LENGTH_LONG)

    def test_the_shelves_shortest_mit_cell_is_a_MANIFEST_not_a_payload(self):
        # 🔴 The honest risk of the new length state: it REFUSES a short MIT body, so a
        # genuine minimal MIT payload would be downgraded to ungradeable. Swept at p252
        # over every `MIT` cell carrying a byte figure on all eight shelves: the only
        # figure below MIT_CANONICAL_LOW is `1 005` B, and it occurs five times as a
        # `package.json` — a MANIFEST. A manifest declares `"license": "MIT"` and does
        # NOT contain the grant body, so `NOT-MIT-BODY` decides it before the length
        # state is ever consulted. The false-refusal rate on current shelf data is 0.
        manifest = '{\n  "name": "scorm-again",\n  "version": "1.1.0",\n  "license": "MIT"\n}\n'
        v = classify(manifest)
        self.assertEqual(v["verdict"], VERDICT_NOT_MIT)
        self.assertFalse(v["mit_body"])
        self.assertLess(v["bytes"], MIT_CANONICAL_LOW)
        # The precedence is what makes it safe, so pin it:
        self.assertEqual(v["length_state"], LENGTH_SHORT)

    def test_mit_plus_unclassified_addition_survives(self):
        padded = MIT + "\n" + ("Additional bespoke term. " * 60)
        self.assertEqual(classify(padded)["verdict"], VERDICT_MIT_PLUS)


class TestP362Sata(unittest.TestCase):
    """`p362` — the Star And Thank Author License, found on a PUBLISHED row.

    `QingdaoU/Judger` (496 ★) was carried as `MIT` on `repos/foundations.md`,
    `repos/trending.md` and `verticals/solutions.md`, and load-bearing in Pattern 9's
    permissive path.  Its payload is SATA.  Corroborated independently: GitHub's own
    classifier reads the same repository as `NOASSERTION`.
    """

    def test_the_real_payload_is_refused_and_the_rider_is_NAMED(self):
        v = classify(SATA)
        self.assertEqual(v["bytes"], 1823)
        self.assertTrue(v["mit_body"])
        self.assertEqual(v["verdict"], VERDICT_RESTRICTED)
        # The point of the change: WHAT is wrong, not merely that something is.
        self.assertTrue(v["riders"], "SATA must report as a named rider")
        self.assertFalse(is_usable_permissive(SATA))

    def test_the_in_band_rider_is_the_control_that_earns_the_anchors(self):
        # 🔴 This is the case the length limb is blind to by construction, and it is the
        # reason the anchors were added rather than relying on the 673 B of excess the
        # real file happens to carry.  Measured BEFORE the change: verdict `MIT`,
        # is_usable_permissive True — i.e. publishable as permissive.
        v = classify(SATA_IN_BAND)
        self.assertEqual(v["length_state"], LENGTH_IN_BAND)
        self.assertGreaterEqual(v["bytes"], MIT_CANONICAL_LOW)
        self.assertLessEqual(v["bytes"], MIT_CANONICAL_HIGH)
        self.assertEqual(v["verdict"], VERDICT_RESTRICTED)
        self.assertFalse(is_usable_permissive(SATA_IN_BAND))

    def test_the_length_limb_alone_would_have_called_it_unclassified(self):
        # Pins the pre-change verdict as a fact rather than a recollection: strip the
        # rider vocabulary from the real payload and only the byte excess is left.
        stripped = SATA.replace("Star And Thank Author", "Example").replace(
            "you shall star/+1/like", "you may enjoy"
        ).replace("thank the author(s)", "credit the maintainers")
        v = classify(stripped)
        self.assertEqual(v["verdict"], VERDICT_MIT_PLUS)
        self.assertEqual(v["riders"], [])
        self.assertGreater(v["excess"], 0)

    def test_genuine_mit_fires_no_sata_anchor(self):
        # The false-positive side: the new anchors must not reach canonical MIT, nor the
        # Commons Clause fixture's classification.
        self.assertEqual(classify(MIT)["riders"], [])
        self.assertEqual(classify(MIT)["verdict"], VERDICT_MIT)
        self.assertEqual(classify(COMMONS_CLAUSE)["verdict"], VERDICT_RESTRICTED)

    def test_the_word_star_alone_is_not_enough(self):
        # 🟡 The honest hazard of an anchor this short: `star` occurs in ordinary prose.
        # The anchors are PHRASES for that reason, so a licence merely mentioning stars
        # is untouched.
        innocent = MIT.replace(
            "Copyright (c) 2026 A Licensor",
            "Copyright (c) 2026 A Licensor\n\nSee the star chart in README.md.",
        )
        self.assertEqual(classify(innocent)["riders"], [])


if __name__ == "__main__":
    unittest.main()
