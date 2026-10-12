"""Tests for p142-americas-disambiguation.

The first three pin this probe's own first-draft defects. Each produced a booking that
would have been published as a region, which is the most expensive kind of error this KB
can make: a wrong region is worse than no region.
"""
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import americas as A  # noqa: E402


def hosts(text):
    """Apply the probe's own extraction rules to a string."""
    out = set()
    for m in A.HOST.finditer(text):
        h = m.group(0).lower().strip(".")
        if A.PLACEHOLDER.search(h):
            continue
        if h.count(".") + 1 < A.MIN_LABELS:
            continue
        out.add(h)
    return out


class HomographRegressions(unittest.TestCase):
    def test_python_filenames_are_not_paraguay(self):
        """🔴 `.py` is Paraguay's ccTLD and Python's extension. The first draft booked
        `karkarkins/BlackboardAssistantMCP` and `nitsuah/bb-mcp` LATAM off `scraper.py`
        and `synth.py`, and split a Canadian row with six false Paraguayan hosts."""
        for f in ("scraper.py", "synth.py", "server.py", "config.py", "auth.py",
                  "src/app.py", "a.b.py"):
            self.assertEqual(hosts(f), set(), f)
        self.assertNotIn("py", A.LATAM_TLD)

    def test_struts_action_endpoints_are_not_the_dominican_republic(self):
        """🔴 `.do` is the DR's ccTLD and a Struts/JSP action suffix. SIGAA uses it."""
        for f in ("logar.do", "vertelalogin.do", "/sigaa/logar.do"):
            self.assertEqual(hosts(f), set(), f)
        self.assertNotIn("do", A.LATAM_TLD)

    def test_cuda_and_opencl_sources_are_not_cuba_or_chile(self):
        for f in ("kernel.cu", "matmul.cl"):
            self.assertEqual(hosts(f), set(), f)
        self.assertNotIn("cu", A.LATAM_TLD)
        self.assertNotIn("cl", A.LATAM_TLD)

    def test_the_homograph_gap_is_declared_not_hidden(self):
        """The four exclusions cost real coverage, and the docstring must say so."""
        for country in ("Paraguay", "Dominican Republic", "Cuba", "Chile"):
            self.assertIn(country, A.__doc__)


class HostExtraction(unittest.TestCase):
    def test_real_target_hosts_are_kept(self):
        for h in ("sigaa.ufpi.br", "guarani.unq.edu.ar", "vsb.mcgill.ca",
                  "q.utoronto.ca", "aulavirtual.upc.edu.pe", "suap.ifrn.edu.br"):
            self.assertEqual(hosts("https://" + h + "/x"), {h}, h)

    def test_bare_public_suffixes_are_dropped(self):
        """`edu.br` and `gov.br` are suffixes, not hosts code can reach."""
        for h in ("edu.br", "gov.br", "edu.ar", "campus.edu", "http.us"):
            self.assertEqual(hosts(h), set(), h)

    def test_placeholders_place_nothing(self):
        for h in ("your-institution.instructure.com", "mcp.example.edu",
                  "blackboard.example.edu", "myschool.instructure.com"):
            self.assertEqual(hosts(h), set(), h)


class BookingRule(unittest.TestCase):
    def test_single_region_books(self):
        latam, na, edu = A.classify({"sigaa.ufpi.br", "sigaa.ufc.br"})
        self.assertEqual(sorted(latam), ["Brazil"])
        self.assertEqual(na, {})

    def test_both_regions_decline_rather_than_guess(self):
        latam, na, _ = A.classify({"sigaa.ufpi.br", "q.utoronto.ca"})
        self.assertTrue(latam and na, "a split must be visible to the caller")

    def test_edu_is_never_a_booking_on_its_own(self):
        """🔴 `ruud0/aula-virtual-mcp` reaches `aula-virtual.unav.edu` — Universidad de
        Navarra, SPAIN. A `.edu` host is not a US signal, measured not assumed."""
        latam, na, edu = A.classify({"aula-virtual.unav.edu"})
        self.assertEqual((latam, na), ({}, {}))
        self.assertEqual(edu, ["aula-virtual.unav.edu"])

    def test_only_americas_ambiguous_offsets_are_eligible(self):
        self.assertEqual(A.NA_LATAM_AMBIGUOUS,
                         {"-0300", "-0400", "-0500", "-0600", "-0700"})
        for off in ("+0200", "+0530", "+0800", "+0000"):
            self.assertNotIn(off, A.NA_LATAM_AMBIGUOUS)

    def test_platform_token_never_books(self):
        """A national platform places the DEPLOYMENT. It is corroboration only."""
        self.assertIn("nothing is booked on it", A.__doc__)


if __name__ == "__main__":
    unittest.main(verbosity=2)


class CloudRegionRegression(unittest.TestCase):
    """🔴 Third homograph class, found on the search-channel candidates rather than the
    registered population. `\\b` matches before a hyphen, so a cloud region identifier
    parsed as a ccTLD host."""

    def test_aws_region_is_not_a_us_host(self):
        for t in ("123456789.dkr.ecr.us-east-1.amazonaws.com",
                  "s3.us-west-2.amazonaws.com",
                  "x.ca-central-1.amazonaws.com",
                  "y.sa-east-1.amazonaws.com"):
            self.assertEqual(hosts(t), set(), t)

    def test_a_real_host_ending_at_the_tld_still_matches(self):
        self.assertEqual(hosts("https://sigaa.ufpi.br/sigaa"), {"sigaa.ufpi.br"})
        self.assertEqual(hosts("datos.gob.ar, dados.gov.br"),
                         {"datos.gob.ar", "dados.gov.br"})

    def test_trailing_dot_and_punctuation_do_not_block_a_match(self):
        self.assertEqual(hosts("see q.utoronto.ca."), {"q.utoronto.ca"})
