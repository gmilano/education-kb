"""26 tests for `p149-common-title-licence`. Authored fixtures, offline, no network."""

import json
import os
import shutil
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common_title as ct  # noqa: E402


def write(root, rel, text):
    path = os.path.join(root, rel)
    os.makedirs(os.path.dirname(path) or root, exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)


class TitleFormTest(unittest.TestCase):
    def test_apache_title_with_version_word(self):
        self.assertEqual(ct.title_licence("Apache License, Version 2.0"), "Apache-2.0")

    def test_apache_title_without_version_word(self):
        self.assertEqual(ct.title_licence("Licensed under the Apache License 2.0"),
                         "Apache-2.0")

    def test_bare_apache_2_0_with_space(self):
        self.assertEqual(ct.title_licence("released under Apache 2.0"), "Apache-2.0")

    def test_gplv2_compact(self):
        self.assertEqual(ct.title_licence("this is GPLv2 code"), "GPL")

    def test_gpl_v3_spaced(self):
        self.assertEqual(ct.title_licence("licensed GPL v3"), "GPL")

    def test_gnu_gpl_spelled_out(self):
        self.assertEqual(ct.title_licence("GNU General Public License, Version 3"), "GPL")

    def test_affero_is_AGPL_and_not_GPL(self):
        # 🔴 Ordering matters: "GNU Affero General Public License" contains "General
        # Public License" and must not be read as a bare GPL.
        self.assertEqual(ct.title_licence("GNU Affero General Public License v3"),
                         "AGPL-3.0")

    def test_lesser_is_LGPL_and_not_GPL(self):
        self.assertEqual(ct.title_licence("GNU Lesser General Public License v2.1"),
                         "LGPL")

    def test_bsd_3_clause_with_space(self):
        self.assertEqual(ct.title_licence("BSD 3-Clause licence"), "BSD")

    def test_three_clause_bsd_reversed(self):
        self.assertEqual(ct.title_licence("a 3-Clause BSD licence"), "BSD")

    def test_mpl_title_and_token(self):
        self.assertEqual(ct.title_licence("Mozilla Public License, Version 2.0"),
                         "MPL-2.0")
        self.assertEqual(ct.title_licence("MPL 2.0"), "MPL-2.0")

    def test_mit_license_title(self):
        self.assertEqual(ct.title_licence("The MIT License"), "MIT")

    def test_ecl_title(self):
        self.assertEqual(ct.title_licence("Educational Community License, Version 2.0"),
                         "ECL-2.0")

    def test_cc0_and_unlicense(self):
        self.assertEqual(ct.title_licence("dedicated via CC0"), "CC0-1.0")
        self.assertEqual(ct.title_licence("The Unlicense"), "Unlicense")

    def test_prose_with_no_licence_name_returns_None(self):
        self.assertIsNone(ct.title_licence("See the documentation for terms of use."))

    def test_the_earliest_match_wins(self):
        # A row's own heading precedes a dependency notice further down the file.
        self.assertEqual(ct.title_licence("## License\nMIT License\n\nDeps: Apache 2.0"),
                         "MIT")


class IdentifyExtTest(unittest.TestCase):
    def test_an_spdx_token_still_wins_unchanged(self):
        self.assertEqual(ct.identify_ext("SPDX: Apache-2.0"), "Apache-2.0")

    def test_a_body_hint_still_wins_unchanged(self):
        self.assertEqual(
            ct.identify_ext("Permission is hereby granted, free of charge"), "MIT")

    def test_a_title_form_is_read_where_the_published_matcher_gives_up(self):
        self.assertEqual(ct.identify_ext("Distributed under the Apache License 2.0."),
                         "Apache-2.0")

    def test_unreadable_text_is_still_UNIDENTIFIED(self):
        self.assertEqual(ct.identify_ext("no terms stated anywhere"), "UNIDENTIFIED")


class PayloadRootTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def test_an_npm_extraction_directory_descends_into_package(self):
        # 🔴 The harness defect this module shipped and fixed.
        root = os.path.join(self.tmp, "npm-row")
        write(root, "package/package.json", json.dumps({"name": "x", "license": "MIT"}))
        self.assertEqual(ct.payload_root(root), os.path.join(root, "package"))

    def test_a_git_clone_root_is_returned_unchanged(self):
        root = os.path.join(self.tmp, "clone")
        write(root, "README.md", "# x\n")
        write(root, "src/a.py", "x = 1\n")
        self.assertEqual(ct.payload_root(root), root)

    def test_a_root_holding_package_plus_siblings_is_not_descended(self):
        root = os.path.join(self.tmp, "mixed")
        write(root, "package/x.js", "x\n")
        write(root, "README.md", "# x\n")
        self.assertEqual(ct.payload_root(root), root)

    def test_a_missing_root_is_returned_unchanged(self):
        missing = os.path.join(self.tmp, "nope")
        self.assertEqual(ct.payload_root(missing), missing)


class CensusExtTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def test_a_licence_file_naming_apache_in_words_is_identified(self):
        root = os.path.join(self.tmp, "a")
        write(root, "LICENSE", "Apache License 2.0\n\nTerms follow.\n")
        got = ct.census_ext(root, "a")
        self.assertEqual(got["grant"], "FILE")
        self.assertEqual(got["licence"], "Apache-2.0")
        self.assertTrue(got["evidence"].endswith("+title"))

    def test_an_identified_row_is_left_exactly_as_published(self):
        root = os.path.join(self.tmp, "b")
        write(root, "LICENSE", "Permission is hereby granted, free of charge\n")
        got = ct.census_ext(root, "b")
        self.assertEqual((got["grant"], got["licence"], got["evidence"]),
                         ("FILE", "MIT", "LICENSE"))

    def test_a_row_with_no_grant_at_all_stays_NONE(self):
        root = os.path.join(self.tmp, "c")
        write(root, "src/a.py", "x = 1\n")
        self.assertEqual(ct.census_ext(root, "c")["grant"], "NONE")


if __name__ == "__main__":
    unittest.main(verbosity=2)
