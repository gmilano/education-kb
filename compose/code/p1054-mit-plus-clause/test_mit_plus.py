"""p187 / P1054 tests — stdlib unittest only, no network, no dependencies.

Run:  python3 -I -m unittest discover -s compose/code/p1054-mit-plus-clause -v
"""

import unittest

from mit_plus import (
    VERDICT_MIT,
    VERDICT_MIT_PLUS,
    VERDICT_NOT_MIT,
    VERDICT_RESTRICTED,
    classify,
    is_usable_permissive,
)

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


if __name__ == "__main__":
    unittest.main()
