#!/usr/bin/env python3
"""Tests for the licence-path matcher in scan_npm_payload.sh.

The probe's whole verdict rests on one grep. If that pattern is wrong, every
NONE in result.2026-10-12.tsv is wrong in the same direction, so the pattern is
tested against the filenames npm packages really use -- and against the
near-misses that must NOT count as a licence grant.

Run: python3 -I test_payload.py
"""
import re
import subprocess
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
SCRIPT = HERE / "scan_npm_payload.sh"

# The pattern as it appears in the probe. Kept in sync by test_pattern_is_the_shipped_one.
PATTERN = r'(^|/)(licen[cs]e|copying|notice)([.-][a-z0-9]+)?$'


def matches(path: str) -> bool:
    return re.search(PATTERN, path, re.IGNORECASE) is not None


class LicencePathMatcher(unittest.TestCase):
    def test_real_licence_paths_match(self):
        """Every form the census actually met, plus the common spellings it did not."""
        for path in [
            "package/LICENSE",
            "package/LICENCE",
            "package/license",
            "package/LICENSE.md",
            "package/LICENSE.txt",
            "package/LICENSE-MIT",
            "package/COPYING",
            "package/NOTICE",
            "package/notice.txt",
            "package/dist/vendor/LICENSE",
        ]:
            with self.subTest(path=path):
                self.assertTrue(matches(path), f"{path} should count as a licence file")

    def test_near_misses_do_not_match(self):
        """A file that merely mentions a licence is not the grant.

        `package.json` carrying "license": "MIT" is exactly the defect this probe
        measures, so a manifest must never be counted as the licence text.
        """
        for path in [
            "package/package.json",
            "package/README.md",
            "package/dist/licenseChecker.js",
            "package/src/licensing/index.ts",
            "package/LICENSE.d.ts.map",
            "package/licenses/",
        ]:
            with self.subTest(path=path):
                self.assertFalse(matches(path), f"{path} must not count as a licence file")

    def test_pattern_is_the_shipped_one(self):
        """Guards against the test drifting away from the script it certifies."""
        self.assertIn(PATTERN, SCRIPT.read_text())


class CommittedResult(unittest.TestCase):
    """The committed TSV is a published measurement; keep it self-consistent."""

    def setUp(self):
        tsv = HERE / "result.2026-10-12.tsv"
        if not tsv.exists():
            self.skipTest("no committed result")
        lines = tsv.read_text().strip().splitlines()
        self.header = lines[0].split("\t")
        self.rows = [dict(zip(self.header, l.split("\t"))) for l in lines[1:]]

    def test_header_is_not_data(self):
        self.assertEqual(self.header[0], "package")
        self.assertTrue(all(r["package"] != "package" for r in self.rows))

    def test_every_row_resolved(self):
        """No row may be published as a fetch failure or an identity mismatch."""
        for r in self.rows:
            with self.subTest(pkg=r["package"]):
                self.assertNotIn("FAILED", r["paths"])
                self.assertNotEqual(r["paths"], "SHASUM_MISMATCH")

    def test_licence_file_column_agrees_with_the_matcher(self):
        for r in self.rows:
            if r["licence_file"] == "NONE":
                continue
            for path in r["licence_file"].split(","):
                with self.subTest(pkg=r["package"], path=path):
                    self.assertTrue(matches(path))

    def test_the_headline_count_is_reproducible(self):
        """7 of 21 carry an SPDX id and no licence text; 2 more carry neither."""
        id_no_text = [r for r in self.rows
                      if r["spdx_id"] not in ("ABSENT", "NO_MANIFEST")
                      and r["licence_file"] == "NONE"]
        no_signal = [r for r in self.rows
                     if r["spdx_id"] == "ABSENT" and r["licence_file"] == "NONE"]
        self.assertEqual(len(self.rows), 21)
        self.assertEqual(len(id_no_text), 7)
        self.assertEqual(len(no_signal), 2)


if __name__ == "__main__":
    unittest.main(verbosity=2)
