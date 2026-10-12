"""18 tests for `p149-placement-exclusions`. Authored fixtures, offline, no network.

The fixtures are written to a temporary directory by this file, so a run needs nothing
from the shelf and cannot be made to pass by a clone that happens to be present.
"""

import json
import os
import shutil
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import placement_exclusions as pe  # noqa: E402
import npm_region  # noqa: E402


def write(root, rel, text):
    path = os.path.join(root, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)


class PlatformHostTest(unittest.TestCase):
    def test_each_named_host_is_a_platform(self):
        for h in ("youtu.be", "youtube.com", "bit.ly", "t.co", "goo.gl", "github.io"):
            self.assertTrue(pe.is_platform_host(h), h)

    def test_subdomain_of_a_platform_is_a_platform(self):
        self.assertTrue(pe.is_platform_host("pages.github.io"))
        self.assertTrue(pe.is_platform_host("www.youtube.com"))

    def test_a_real_institution_is_not_a_platform(self):
        for h in ("kuleuven.be", "ugent.be", "sigaa.ufpi.br", "learn.uq.edu.au"):
            self.assertFalse(pe.is_platform_host(h), h)

    def test_a_host_merely_ending_in_the_same_letters_is_not_a_platform(self):
        # `notyoutu.be` must not match `youtu.be` -- the boundary is a label, not a suffix.
        self.assertFalse(pe.is_platform_host("notyoutu.be"))
        self.assertFalse(pe.is_platform_host("mybit.ly"))


class ClassifyTest(unittest.TestCase):
    def test_youtu_be_places_EMEA_with_no_exclusion(self):
        # 🔴 This is `T70` reproduced: the defect the action exists for.
        self.assertEqual(pe.classify("youtu.be")[0], "EMEA")

    def test_youtu_be_is_refused_and_recorded_as_a_lead_under_the_platform_exclusion(self):
        region, how, lead = pe.classify("youtu.be", exclude_platform=True)
        self.assertIsNone(region)
        self.assertIn("platform host youtu.be", lead)

    def test_the_edu_exclusion_does_not_refuse_youtu_be(self):
        self.assertEqual(pe.classify("youtu.be", exclude_edu=True)[0], "EMEA")

    def test_bare_edu_places_North_America_with_no_exclusion(self):
        self.assertEqual(pe.classify("bb.edu")[0], "North America")

    def test_bare_edu_is_refused_and_recorded_as_a_lead_under_the_edu_exclusion(self):
        region, how, lead = pe.classify("bb.edu", exclude_edu=True)
        self.assertIsNone(region)
        self.assertEqual(lead, "bare .edu bb.edu")

    def test_the_platform_exclusion_does_not_refuse_a_bare_edu(self):
        self.assertEqual(pe.classify("bb.edu", exclude_platform=True)[0], "North America")

    def test_an_academic_namespace_survives_both_exclusions(self):
        # `edu.au` is the national academic namespace and is NOT a bare `.edu`.
        region, how, lead = pe.classify("learn.uq.edu.au", exclude_edu=True,
                                        exclude_platform=True)
        self.assertEqual(region, "APAC")
        self.assertEqual(lead, "-")

    def test_a_grandfathered_edu_still_places_nothing_either_way(self):
        self.assertIsNone(pe.classify("unav.edu")[0])
        self.assertIsNone(pe.classify("unav.edu", exclude_edu=True)[0])

    def test_a_real_ccTLD_institution_survives_both_exclusions(self):
        self.assertEqual(
            pe.classify("sigaa.ufpi.br", exclude_edu=True, exclude_platform=True)[0],
            "LATAM")


class DevToolingHostTest(unittest.TestCase):
    """🔴 `ACTION EZ`'s refuting row: the Rust installer's `.rs` is Serbia's ccTLD."""

    def test_the_rust_installer_host_is_dev_tooling(self):
        self.assertTrue(pe.is_dev_tooling_host("sh.rustup.rs"))
        self.assertTrue(pe.is_dev_tooling_host("rustup.rs"))

    def test_it_places_EMEA_unexcluded(self):
        self.assertEqual(pe.classify("sh.rustup.rs")[0], "EMEA")

    def test_ACTION_FAs_six_hosts_do_NOT_catch_it(self):
        # 🔴 The point of the refutation: the registered exclusion misses the real cause.
        self.assertFalse(pe.is_platform_host("sh.rustup.rs"))
        self.assertEqual(pe.classify("sh.rustup.rs", exclude_platform=True)[0], "EMEA")

    def test_the_devtool_exclusion_refuses_it_and_records_a_lead(self):
        region, how, lead = pe.classify("sh.rustup.rs", exclude_devtool=True)
        self.assertIsNone(region)
        self.assertIn("dev-tooling host sh.rustup.rs", lead)

    def test_a_real_serbian_institution_is_not_dev_tooling(self):
        self.assertFalse(pe.is_dev_tooling_host("bg.ac.rs"))
        self.assertEqual(
            pe.classify("www.bg.ac.rs", exclude_devtool=True, exclude_platform=True)[0],
            "EMEA")


class ClassifierRestoredTest(unittest.TestCase):
    def test_the_substituted_classifier_is_restored_after_use(self):
        original = npm_region.region_of_host
        with pe._classifier(True, True, True):
            self.assertIsNot(npm_region.region_of_host, original)
        self.assertIs(npm_region.region_of_host, original)

    def test_the_classifier_is_restored_even_when_the_body_raises(self):
        original = npm_region.region_of_host
        with self.assertRaises(RuntimeError):
            with pe._classifier(True, True, True):
                raise RuntimeError("boom")
        self.assertIs(npm_region.region_of_host, original)


class PlaceOverFixturesTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def _root(self, name):
        return os.path.join(self.tmp, name)

    def test_a_platform_only_row_is_EMEA_unexcluded_and_UNPLACED_excluded(self):
        root = self._root("platform-only")
        write(root, "app/ingest.py",
              'SOURCE = "https://youtu.be/abc123"  # lecture capture\n')
        write(root, "package.json", json.dumps({"name": "platform-only"}))
        self.assertEqual(pe.place(root, "none")["region"], "EMEA")
        row = pe.place(root, "platform")
        self.assertEqual(row["region"], "UNPLACED")
        self.assertIn("platform host youtu.be", row["lead"])

    def test_a_bare_edu_row_is_placed_unexcluded_and_UNPLACED_excluded(self):
        root = self._root("edu-only")
        write(root, "test/unit.test.js", 'const BASE = "https://bb.edu/webapps";\n')
        write(root, "package.json", json.dumps({"name": "edu-only"}))
        self.assertEqual(pe.place(root, "none")["region"], "North America")
        row = pe.place(root, "edu")
        self.assertEqual(row["region"], "UNPLACED")
        self.assertIn("bare .edu bb.edu", row["lead"])

    def test_the_edu_exclusion_resolves_a_conflict_it_was_the_cause_of(self):
        # A row whose only disagreement is a bare `.edu` against a real ccTLD must stop
        # being a CONFLICT and become the real placement -- not become UNPLACED.
        root = self._root("edu-vs-real")
        write(root, "src/locales/en.json", json.dumps({
            "demo": "https://professor-site.edu/course",
            "home": "https://canvas.unicatt.it/login",
        }))
        write(root, "package.json", json.dumps({"name": "edu-vs-real"}))
        self.assertEqual(pe.place(root, "none")["region"], "CONFLICT")
        self.assertEqual(pe.place(root, "edu")["region"], "EMEA")

    def test_mode_none_reproduces_the_unmodified_probe_exactly(self):
        root = self._root("reproduction")
        write(root, "src/auth.py",
              'BASE_URL = "https://learn.uq.edu.au"\nDOCS = "https://youtu.be/x"\n')
        write(root, "package.json", json.dumps({"name": "reproduction"}))
        baseline = npm_region.place(root)
        driven = pe.place(root, "none")
        for key in ("region", "channel", "host", "how", "where", "conflict"):
            self.assertEqual(driven[key], baseline[key], key)

    def test_the_noninst_mode_resolves_the_devtool_row_a_registered_mode_cannot(self):
        # The DesQTA shape: an Australian subject whose only ccTLD evidence is the Rust
        # installer. `platform` leaves it EMEA; `noninst` declines to place it at all.
        root = self._root("devtool-only")
        write(root, "docs/development/build-deployment.md",
              "Install the toolchain:\n\n    curl -sSf https://sh.rustup.rs | sh\n")
        write(root, "package.json", json.dumps({"name": "devtool-only"}))
        self.assertEqual(pe.place(root, "none")["region"], "EMEA")
        self.assertEqual(pe.place(root, "platform")["region"], "EMEA")
        row = pe.place(root, "noninst")
        self.assertEqual(row["region"], "UNPLACED")
        self.assertIn("dev-tooling host sh.rustup.rs", row["lead"])

    def test_an_empty_tree_is_UNPLACED_and_not_an_error(self):
        root = self._root("empty")
        os.makedirs(root)
        self.assertEqual(pe.place(root, "both")["region"], "UNPLACED")


if __name__ == "__main__":
    unittest.main(verbosity=2)
