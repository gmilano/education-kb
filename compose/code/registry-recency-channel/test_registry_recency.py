#!/usr/bin/env python3
"""Control tests for registry-recency-channel.

Written as *invariant properties with negative controls*, the shape pass 122
converted the older suites to: a test that asserts a frozen cardinality of the
corpus ("exactly 3 deps are cold") expires on the next pass and teaches nothing.
Every assertion below must hold for any corpus, and each one is paired with a
control proving the original defect is still detectable.

    python3 -I test_registry_recency.py
"""
import datetime as dt
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from registry_recency import (age_days, ecosystem_of, is_local_spec,
                              npm_release, pypi_release, read_closure)

HERE = os.path.dirname(os.path.abspath(__file__))
RESULT = os.path.join(HERE, "data", "recency-2026-10-07.tsv")

# The four names swept blind alongside the real corpus. If ANY of them resolves,
# the probe cannot tell absence from presence and no negative result from this
# channel may be published. This is the pass-22 lesson: a GitLab control that
# 302s on an invented slug proves nothing.
CONTROLS = {
    "this-package-does-not-exist-xyz123-globant",
    "@globant-kb/no-such-package-zzz999",
    "kolibri-oral-fluency-fake-probe-0000",
    "moodle-mcp-nonexistent-control-4242",
}


def rows():
    with open(RESULT, encoding="utf-8") as fh:
        head = fh.readline().rstrip("\n").split("\t")
        return [dict(zip(head, l.rstrip("\n").split("\t"))) for l in fh if l.strip()]


class EcosystemRouting(unittest.TestCase):
    """A manifest filename, not a guess, decides which registry is asked."""

    def test_package_json_routes_to_npm(self):
        self.assertEqual(ecosystem_of("package.json"), "npm")
        self.assertEqual(ecosystem_of("client/package.json"), "npm")

    def test_python_manifests_route_to_pypi(self):
        for m in ("pyproject.toml", "requirements.txt", "python/pyproject.toml",
                  "pyproject.toml#base"):
            self.assertEqual(ecosystem_of(m), "pypi", m)

    def test_negative_control_routing_is_not_constant(self):
        # Defect being guarded: a router that returns one value for everything
        # would pass every test above if they all expected the same registry.
        self.assertNotEqual(ecosystem_of("package.json"),
                            ecosystem_of("pyproject.toml"))


class LocalSpecClassification(unittest.TestCase):
    """A path/link/git spec is not served by a registry, so its 404 is correct."""

    def test_non_registry_specs_are_local(self):
        for spec in ("file:./common", "link:../pkg", "workspace:*",
                     "git+https://github.com/o/r.git", "./vendor/x", "/abs/path"):
            self.assertTrue(is_local_spec(spec), spec)

    def test_version_ranges_are_not_local(self):
        for spec in ("^1.2.3", "~2.0", ">=3,<4", "1.0.0", "*", ""):
            self.assertFalse(is_local_spec(spec), spec)

    def test_negative_control_the_discrimination_is_real(self):
        # Defect being guarded: an is_local_spec() that always returns True would
        # silently excuse every genuinely missing package.
        self.assertNotEqual(is_local_spec("file:./common"), is_local_spec("^1.2.3"))


class AgeArithmetic(unittest.TestCase):
    """Ages are whole days against an explicit reference date, not 'today'."""

    def test_age_is_measured_from_the_reference_date(self):
        self.assertEqual(age_days("2026-10-05T10:00:00Z", dt.date(2026, 10, 7)), 2)

    def test_zulu_and_offset_stamps_agree(self):
        ref = dt.date(2026, 10, 7)
        self.assertEqual(age_days("2026-09-23T16:17:20-05:00", ref),
                         age_days("2026-09-23T16:17:20Z", ref))

    def test_unparseable_and_empty_yield_no_age_not_zero(self):
        # Defect being guarded: returning 0 for an unreadable date would file
        # every unmeasured package as brand new.
        # NOTE, recorded because this test was written wrong first: "20261005"
        # is NOT an unparseable value. It is ISO-8601 *basic* format and
        # datetime.fromisoformat accepts it on Python 3.11+, so the first
        # version of this test asserted a defect that was not there. Only
        # genuinely non-ISO shapes belong in this list.
        for bad in ("", "not-a-date", "2026/10/05", "Oct 5 2026"):
            self.assertEqual(age_days(bad, dt.date(2026, 10, 7)), "", bad)

    def test_iso_basic_format_is_accepted_not_rejected(self):
        # The positive half of the correction above: the compact form is valid
        # and must date, not blank.
        self.assertEqual(age_days("20261005", dt.date(2026, 10, 7)), 2)


class ReleaseParsing(unittest.TestCase):
    """Each registry's own shape, including the yanked-latest fallback."""

    def test_pypi_prefers_the_latest_version_files(self):
        doc = {"info": {"version": "1.2.0"},
               "urls": [{"upload_time_iso_8601": "2026-01-01T00:00:00Z"},
                        {"upload_time_iso_8601": "2026-01-02T00:00:00Z"}]}
        self.assertEqual(pypi_release(doc), ("1.2.0", "2026-01-02T00:00:00Z"))

    def test_pypi_falls_back_when_latest_has_no_files(self):
        doc = {"info": {"version": "9.9.9"}, "urls": [],
               "releases": {"9.9.9": [{"upload_time_iso_8601": "2025-05-05T00:00:00Z"}]}}
        self.assertEqual(pypi_release(doc)[1], "2025-05-05T00:00:00Z")

    def test_npm_reads_the_latest_dist_tag_not_modified(self):
        doc = {"dist-tags": {"latest": "2.0.0"},
               "time": {"2.0.0": "2026-03-03T00:00:00Z",
                        "modified": "2026-09-09T00:00:00Z"}}
        self.assertEqual(npm_release(doc), ("2.0.0", "2026-03-03T00:00:00Z"))

    def test_negative_control_modified_is_only_a_fallback(self):
        # Defect being guarded: reading time.modified first would date a package
        # by its last metadata edit (a deprecation, an owner change) and report
        # an abandoned library as fresh.
        doc = {"dist-tags": {"latest": "2.0.0"},
               "time": {"modified": "2026-09-09T00:00:00Z"}}
        self.assertEqual(npm_release(doc)[1], "2026-09-09T00:00:00Z")


class PublishedResultIntegrity(unittest.TestCase):
    """Properties of the published TSV that must hold on any future re-run."""

    def setUp(self):
        if not os.path.exists(RESULT):
            self.skipTest("no published result in data/")
        self.rows = rows()

    def test_every_planted_control_failed_to_resolve(self):
        seen = {r["dep"]: r["status"] for r in self.rows if r["dep"] in CONTROLS}
        self.assertEqual(set(seen), CONTROLS, "a control is missing from the sweep")
        for dep, status in seen.items():
            self.assertNotEqual(status, "OK", "control %s RESOLVED" % dep)

    def test_real_corpus_did_resolve_so_the_probe_discriminates(self):
        real = [r for r in self.rows if r["dep"] not in CONTROLS]
        ok = [r for r in real if r["status"] == "OK"]
        self.assertGreater(len(ok), 0.9 * len(real),
                           "fewer than 90% of real deps dated: channel degraded")

    def test_every_ok_row_carries_a_version_a_date_and_an_age(self):
        for r in self.rows:
            if r["status"] != "OK":
                continue
            self.assertTrue(r["latest_version"], r["dep"])
            self.assertTrue(r["release_date"], r["dep"])
            self.assertRegex(r["age_days"], r"^-?\d+$", r["dep"])

    def test_no_row_is_a_header_or_placeholder(self):
        # The KB's standing defect: a header row compiled as an entity.
        banned = {"dep", "nombre", "repo", "licencia", "name", "licence", "-", ""}
        for r in self.rows:
            self.assertNotIn(r["dep"].strip().lower(), banned, repr(r))

    def test_ages_are_consistent_with_their_dates(self):
        ref = dt.date(2026, 10, 7)
        for r in self.rows:
            if r["status"] != "OK":
                continue
            self.assertEqual(int(r["age_days"]), age_days(r["release_date"], ref),
                             "%s: age does not recompute from its own date" % r["dep"])


class ClosureReader(unittest.TestCase):
    """The reader must dedupe on (name, ecosystem) and drop the '-' sentinel."""

    def test_sentinel_and_duplicate_rows_are_dropped(self):
        import tempfile
        body = ("slug\tmanifest\tdep\tlicence_raw\tfield\tclass\n"
                "a/b\tpackage.json\tleft-pad\tMIT\tlicense\tPERMISSIVE\n"
                "a/b\tpackage.json\tleft-pad\tMIT\tlicense\tPERMISSIVE\n"
                "c/d\tpyproject.toml\tleft-pad\tMIT\tlicense\tPERMISSIVE\n"
                "e/f\trequirements.txt\t-\t-\tparsed-zero\tNO-DEPS\n")
        fh = tempfile.NamedTemporaryFile("w", suffix=".tsv", delete=False)
        fh.write(body)
        fh.close()
        try:
            got = read_closure(fh.name)
        finally:
            os.unlink(fh.name)
        # Same name in two ecosystems is two distinct packages, not a duplicate.
        self.assertEqual(got, [("left-pad", "npm"), ("left-pad", "pypi")])


if __name__ == "__main__":
    unittest.main(verbosity=2)
