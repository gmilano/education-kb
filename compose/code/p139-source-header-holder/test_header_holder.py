#!/usr/bin/env python3
"""Tests for `header_holder`. Run: python3 -I test_header_holder.py

Every fixture below is a line really present in one of the three repositories probed
this pass, or a line the first draft of the probe got wrong.
"""
import sys
import unittest
from pathlib import Path

# `python3 -I` drops the script's directory from sys.path, so add it explicitly
# rather than requiring the caller to set PYTHONPATH.
sys.path.insert(0, str(Path(__file__).resolve().parent))

import header_holder as hh  # noqa: E402

FRAPPE_OWN = ["Frappe", "Frappe Technologies"]
ACADEMICO_OWN = ["Thomas Debay", "academico"]


class TestVcsArtifact(unittest.TestCase):
    """The regression that caused this file to exist."""

    def test_git_sample_hook_is_a_vcs_artifact(self):
        # The first draft reported this as a foreign holder of openeducat/openeducat_erp.
        self.assertTrue(hh.is_vcs_artifact(".git/hooks/pre-rebase.sample"))
        self.assertTrue(hh.is_vcs_artifact("foo/.git/config"))

    def test_repo_source_paths_are_not_artifacts(self):
        self.assertFalse(hh.is_vcs_artifact("lms/tests/test_utils.py"))
        self.assertFalse(hh.is_vcs_artifact("public/js/filament/filament/echo.js"))
        # A path that merely contains the letters: not a .git directory.
        self.assertFalse(hh.is_vcs_artifact("docs/gitignore-notes.md"))


class TestExtraction(unittest.TestCase):
    def test_frappe_and_foss_united_are_separate_holders(self):
        self.assertEqual(
            hh.extract_holder("# Copyright (c) 2026, Frappe and Contributors"), "Frappe")
        self.assertEqual(
            hh.extract_holder("# Copyright (c) 2021, FOSS United and contributors"), "FOSS United")

    def test_full_corporate_name_survives(self):
        got = hh.extract_holder("# Copyright (c) 2021, Frappe Technologies Pvt. Ltd. and Contributors")
        self.assertEqual(got, "Frappe Technologies Pvt. Ltd")

    def test_today_year_token(self):
        got = hh.extract_holder("#    Copyright (C) 2009-TODAY OpenEduCat Inc(<http://www.openeducat.org>)")
        self.assertTrue(got.startswith("OpenEduCat Inc"), got)

    def test_present_year_token(self):
        self.assertEqual(hh.extract_holder(" * Copyright 2015-present Chen Fengyuan"), "Chen Fengyuan")

    def test_year_then_comma_holder(self):
        self.assertEqual(hh.extract_holder(" * Copyright 2020, Pusher"), "Pusher")

    def test_mit_root_holder_with_contributor_tail(self):
        got = hh.extract_holder("Copyright (c) 2020 Thomas Debay and project contributors")
        self.assertEqual(got, "Thomas Debay")

    def test_angle_bracket_url_is_stripped_and_steward_detected(self):
        got = hh.extract_holder("Copyright (C) 2007 Free Software Foundation, Inc. <http://fsf.org/>")
        self.assertEqual(got, "Free Software Foundation, Inc")
        self.assertTrue(hh.is_steward(got))

    def test_prose_is_not_a_header(self):
        self.assertIsNone(hh.extract_holder("   copyright notices during"))
        self.assertIsNone(hh.extract_holder("copyright notice for the Library among"))
        self.assertIsNone(
            hh.extract_holder("For copyright information, please see the COPYRIGHT file."))

    def test_agpl_body_prose_is_not_a_holder(self):
        """The eight lines of frappe/lms's own license.txt that the first run published.

        Five of these were emitted as FOREIGN holders of frappe/lms before the year/(c)
        marker was made mandatory. They are quoted verbatim from AGPL-3.0 §0-§2.
        """
        for line in [
            "with two steps: (1) assert copyright on the software, and (2) offer",
            '"Copyright" also means copyright-like laws that apply to other kinds of',
            '"The Program" refers to any copyrightable work licensed under this',
            "in a fashion requiring copyright permission, other than the making of an",
            "infringement under applicable copyright law, except executing it on a",
            "feature that (1) displays an appropriate copyright notice, and (2)",
            "copyright on the Program, and are irrevocable provided the stated",
            "rights of fair use or other equivalent, as provided by copyright law.",
        ]:
            self.assertIsNone(hh.extract_holder(line), line)

    def test_openeducat_file_reference_line_is_not_a_holder(self):
        # Sits directly above the real header in 3 OpenEduCat source files.
        self.assertIsNone(hh.extract_holder(
            "# Part of OpenEduCat. See LICENSE file for full copyright & licensing details."))

    def test_jsdoc_trailing_year_form(self):
        """js-sha256, vendored into academico-sis/academico via Filament.

        Making the marker mandatory dropped this holder on the first corrected run;
        it is a real foreign grant and the form has to be matched.
        """
        got = hh.extract_holder("   * @copyright Chen, Yi-Cyuan 2014-2023")
        self.assertEqual(got, "Chen, Yi-Cyuan")
        self.assertEqual(hh.classify(got, ACADEMICO_OWN), "FOREIGN")

    def test_marker_is_required(self):
        # No year and no (c): not a header, however name-shaped the tail looks.
        self.assertIsNone(hh.extract_holder("copyright Acme Corporation"))
        # With a marker, the same tail is a header.
        self.assertEqual(hh.extract_holder("copyright (c) Acme Corporation"), "Acme Corporation")

    def test_non_header_lines(self):
        self.assertIsNone(hh.extract_holder(""))
        self.assertIsNone(hh.extract_holder(None))
        self.assertIsNone(hh.extract_holder("'copyright': 3,"))


class TestClassification(unittest.TestCase):
    def test_own_matches_on_containment_both_ways(self):
        self.assertEqual(hh.classify("Frappe", FRAPPE_OWN), "OWN")
        self.assertEqual(hh.classify("Frappe Technologies Pvt. Ltd", FRAPPE_OWN), "OWN")

    def test_foss_united_is_foreign_to_frappe(self):
        # The finding this pass turns on: a second legal entity, named only in source.
        self.assertEqual(hh.classify("FOSS United", FRAPPE_OWN), "FOREIGN")

    def test_vendored_frontend_holders_are_foreign(self):
        self.assertEqual(hh.classify("Pusher", ACADEMICO_OWN), "FOREIGN")
        self.assertEqual(hh.classify("Chen Fengyuan", ACADEMICO_OWN), "FOREIGN")

    def test_classify_passes_none_through(self):
        self.assertIsNone(hh.classify(None, FRAPPE_OWN))

    def test_steward_detection(self):
        self.assertTrue(hh.is_steward("Free Software Foundation, Inc"))
        self.assertFalse(hh.is_steward("Pusher"))
        self.assertFalse(hh.is_steward(None))


if __name__ == "__main__":
    unittest.main(verbosity=2)
