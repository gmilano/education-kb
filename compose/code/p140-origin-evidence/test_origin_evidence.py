#!/usr/bin/env python3
"""Tests for `origin_evidence`. Run: python3 -I test_origin_evidence.py

The placeholder fixtures are the ones that matter. The first draft of this probe used a
hand-written list of placeholder hosts and BOOKED NORTH AMERICA THREE TIMES off
`d2l.myschool.edu`, `school.edu` and `moodle.example.edu` -- three regional findings off
three worked examples, which is the error class p139's `T24` was published to prevent.
Every placeholder below is verbatim from one of the eight payloads probed this pass.
"""
import sys
import tempfile
import textwrap
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import origin_evidence as oe  # noqa: E402


class TestPlaceholderRejection(unittest.TestCase):
    """Verbatim placeholders from the payloads. Each one booked a false region once."""

    VERBATIM_PLACEHOLDERS = [
        "d2l.myschool.edu",              # @n35da/brightspace-mcp
        "school.edu",                    # canvas-mcp-server (in an email)
        "moodle.example.edu",            # moodle-mcp-server-aql
        "moodle.your-university.edu",    # eth-moodle-mcp README
        "your-moodle-instance.example",  # moodle-mcp-server-aql
        "moodle.instance.com",           # moodle-mcp-server-aql
        "your-instance.instructure.com",
        "127.0.0.1",                     # @ink-waffle/moodle-mcp
    ]

    def test_verbatim_placeholders_are_all_rejected(self):
        for host in self.VERBATIM_PLACEHOLDERS:
            with self.subTest(host=host):
                self.assertTrue(oe.is_placeholder(host), "%s booked a region" % host)

    def test_reserved_tlds_are_rejected(self):
        for host in ("foo.example", "bar.invalid", "x.test", "y.localhost", "z.local"):
            with self.subTest(host=host):
                self.assertTrue(oe.is_placeholder(host))

    def test_hyphen_and_underscore_variants_are_rejected(self):
        """`your-university`, `your_org` and `youruniversity` are one token."""
        for host in ("moodle.your-university.edu", "lms.your_org.edu",
                     "x.youruniversity.edu", "a.my-school.edu"):
            with self.subTest(host=host):
                self.assertTrue(oe.is_placeholder(host))

    def test_bare_ip_is_rejected(self):
        self.assertTrue(oe.is_placeholder("10.0.0.1"))
        self.assertTrue(oe.is_placeholder("192.168.1.1"))

    def test_real_institutional_hosts_survive(self):
        """The two hosts this pass books regions on. If either is rejected, the pass's
        only measured regional evidence disappears."""
        for host in ("moodle-app2.let.ethz.ch", "safari.ethz.ch", "canvas.ust.hk"):
            with self.subTest(host=host):
                self.assertFalse(oe.is_placeholder(host), "%s was rejected" % host)

    def test_other_real_university_hosts_survive(self):
        for host in ("moodle.unibe.ch", "canvas.harvard.edu", "lms.u-tokyo.ac.jp",
                     "aulavirtual.uc.cl"):
            with self.subTest(host=host):
                self.assertFalse(oe.is_placeholder(host))


class TestRegionMapping(unittest.TestCase):
    def test_the_two_booked_rows(self):
        self.assertEqual(oe.map_domain("moodle-app2.let.ethz.ch")[0], "EMEA")
        self.assertEqual(oe.map_domain("canvas.ust.hk")[0], "APAC")

    def test_closed_vocabulary_only(self):
        """`region` is a closed vocabulary of five values plus the explicit UNMAPPED.
        A sixth bucket silently breaks the filter it feeds."""
        allowed = {"North America", "EMEA", "APAC", "LATAM", "Global", "UNMAPPED"}
        for region, _ in oe.KNOWN_DOMAINS.values():
            self.assertIn(region, allowed)
        for region in oe.SUFFIX_REGION.values():
            self.assertIn(region, allowed)

    def test_longest_suffix_wins(self):
        """`.ac.jp` must beat `.jp` and `.edu.au` must beat both `.au` and `.edu`,
        or a Japanese university books as whatever the shorter suffix says."""
        self.assertEqual(oe.map_domain("www.u-tokyo.ac.jp")[0], "APAC")
        self.assertEqual(oe.map_domain("lms.unimelb.edu.au")[0], "APAC")

    def test_dotcom_is_unmapped_not_guessed(self):
        """A wrong region is worse than a missing one: it reads as coverage."""
        self.assertEqual(oe.map_domain("n35da.com")[0], "UNMAPPED")
        self.assertEqual(oe.map_domain("csmediapro.com")[0], "UNMAPPED")

    def test_dotio_is_unmapped(self):
        """`overhang.io` and `edly.io` carry no country signal, whatever is known
        about the companies from reporting. Secondary facts are not measurements."""
        self.assertEqual(oe.map_domain("overhang.io")[0], "UNMAPPED")
        self.assertEqual(oe.map_domain("edly.io")[0], "UNMAPPED")

    def test_known_org_domain_overrides_meaningless_suffix(self):
        """`axim.org` is a `.org`, which maps nowhere; Axim Collaborative is a US
        non-profit, and that is recorded as data with a note, not inferred."""
        region, note = oe.map_domain("axim.org")
        self.assertEqual(region, "North America")
        self.assertIn("Axim", note)


class TestInfraRejection(unittest.TestCase):
    def test_vendor_and_infra_hosts_carry_no_author_signal(self):
        for host in ("github.com", "raw.githubusercontent.com", "registry.npmjs.org",
                     "canvas.instructure.com", "moodle.org", "www.apache.org"):
            with self.subTest(host=host):
                self.assertTrue(oe.is_infra(host) or oe.is_placeholder(host))

    def test_institutional_host_is_not_infra(self):
        self.assertFalse(oe.is_infra("moodle-app2.let.ethz.ch"))
        self.assertFalse(oe.is_infra("canvas.ust.hk"))


class TestPayloadScan(unittest.TestCase):
    def _payload(self, **files):
        tmp = tempfile.TemporaryDirectory()
        for name, body in files.items():
            (Path(tmp.name) / name.replace("__", ".")).write_text(textwrap.dedent(body))
        return tmp

    def test_hardcoded_host_is_booked(self):
        """The shape that books EMEA: a host compiled into a request path."""
        tmp = self._payload(index__js="""
            return canvasRequest("https://moodle-app2.let.ethz.ch/api/courses");
        """)
        rows = oe.evidence_rows(tmp.name, label="x")
        tmp.cleanup()
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["kind"], "HOST_IN_CODE")
        self.assertEqual(rows[0]["region"], "EMEA")

    def test_placeholder_only_payload_books_nothing(self):
        tmp = self._payload(README__md="""
            Set CANVAS_BASE_URL, e.g. https://d2l.myschool.edu or https://moodle.example.edu
        """)
        rows = oe.evidence_rows(tmp.name, label="x")
        tmp.cleanup()
        self.assertEqual(rows[0]["kind"], "NONE")
        self.assertEqual(rows[0]["region"], "UNMAPPED")

    def test_personal_mail_is_not_origin_evidence(self):
        tmp = self._payload(package__json='{"author":"D M <dmontg@gmail.com>"}')
        rows = oe.evidence_rows(tmp.name, label="x")
        tmp.cleanup()
        self.assertEqual(rows[0]["kind"], "NONE")

    def test_empty_payload_reports_none_not_crash(self):
        tmp = tempfile.TemporaryDirectory()
        rows = oe.evidence_rows(tmp.name, label="x")
        tmp.cleanup()
        self.assertEqual(rows[0]["kind"], "NONE")


if __name__ == "__main__":
    unittest.main(verbosity=2)
