"""Tests for p147-npm-region. Authored fixtures only; no package is downloaded."""
import os
import shutil
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import npm_region as N  # noqa: E402


class TestHostRegion(unittest.TestCase):
    def test_swiss_academic_host(self):
        self.assertEqual(N.region_of_host("moodle-app2.let.ethz.ch"),
                         ("EMEA", "ccTLD .ch"))

    def test_hong_kong_academic_host(self):
        self.assertEqual(N.region_of_host("canvas.ust.hk")[0], "APAC")

    def test_bare_edu_is_a_lead_and_says_so(self):
        r, how = N.region_of_host("canvas.harvard.edu")
        self.assertEqual(r, "North America")
        self.assertIn("LEAD", how)

    def test_a_grandfathered_non_us_edu_is_refused(self):
        """🔴 `P144-V` placed `unav.edu` as EMEA. A `.edu`-means-US rule contradicts it."""
        self.assertEqual(N.region_of_host("aula-virtual.unav.edu"), (None, None))

    def test_brazilian_academic_namespace(self):
        self.assertEqual(N.region_of_host("sigaa.ufrn.edu.br")[0], "LATAM")

    def test_generic_suffixes_place_nothing(self):
        """🔴 `.io` and `.ai` are sold worldwide; they are not a region."""
        for h in ("foo.io", "bar.ai", "x.co", "y.me", "z.dev"):
            self.assertEqual(N.region_of_host(h), (None, None), h)

    def test_infrastructure_hosts_are_refused(self):
        for h in ("github.com", "www.gnu.org", "modelcontextprotocol.io", "localhost"):
            self.assertEqual(N.region_of_host(h), (None, None), h)


class TestPlaceholders(unittest.TestCase):
    def test_example_edu_places_nothing(self):
        """🔴 Round 1 of this probe placed a row on this host."""
        self.assertEqual(N.region_of_host("moodle.example.edu"), (None, None))

    def test_myschool_edu_places_nothing(self):
        self.assertEqual(N.region_of_host("d2l.myschool.edu"), (None, None))

    def test_hyphenated_placeholder_places_nothing(self):
        """🔴 Round 2 still placed this one: the label is hyphenated."""
        self.assertEqual(N.region_of_host("moodle.your-university.edu"), (None, None))

    def test_a_real_institution_sharing_a_word_is_not_refused(self):
        """🟢 The negative control: `school` as a label is refused, `schools` is not."""
        self.assertEqual(N.region_of_host("portal.schools.nsw.edu.au")[0], "APAC")


class TestPlacement(unittest.TestCase):
    def setUp(self):
        self.d = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.d, ignore_errors=True)

    def write(self, rel, body):
        p = os.path.join(self.d, rel)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, "w", encoding="utf-8") as fh:
            fh.write(body)

    def test_a_hardcoded_base_url_beats_an_author_domain(self):
        """🟢 `P144-V`: the institution is where it deploys; the author is incidental."""
        self.write("package.json", '{"name":"x","author":{"email":"a@b.com.br"}}')
        self.write("src/s.py", 'BASE_URL = "https://sigaa.ufrn.edu.br"\n')
        r = N.place(self.d)
        self.assertEqual(r["channel"], "hardcoded")
        self.assertEqual(r["region"], "LATAM")

    def test_the_unav_row_is_not_placed_north_american_by_this_probe(self):
        """🟢 Agreement with `P144-V` is the acceptance criterion, not a bare `.edu`."""
        self.write("package.json", '{"name":"x"}')
        self.write("src/s.py", 'BASE_URL = "https://aula-virtual.unav.edu"\n')
        self.assertEqual(N.place(self.d)["region"], "UNPLACED")

    def test_no_national_evidence_is_unplaced_not_global(self):
        """🔵 `UNPLACED` is an answer; `Global` would be a claim."""
        self.write("package.json", '{"name":"x"}')
        self.write("src/s.js", "const u = 'https://example.com';\n")
        self.assertEqual(N.place(self.d)["region"], "UNPLACED")

    def test_two_regions_in_one_channel_is_a_conflict(self):
        self.write("README.md", "https://a.ethz.ch and https://b.ust.hk\n")
        self.assertEqual(N.place(self.d)["region"], "CONFLICT")


if __name__ == "__main__":
    unittest.main(verbosity=2)
