#!/usr/bin/env python3
"""Tests for the ACTION CH matcher.

p138's probe tested its path matcher against real and near-miss FILENAMES before
publishing a count. This probe's claim is stronger — it reads file CONTENT and calls
some of it a grant — so the near-misses matter more. Every assertion below is a
sentence that really appears in shipped JavaScript.

Run: python3 -I test_headers.py
"""
import os
import sys
import tempfile
import unittest

# `-I` (used throughout this probe, because it reads downloaded tarballs) drops the
# script directory from sys.path, so the module under test is added back explicitly.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import headers  # noqa: E402


def one(content, name="index.js"):
    """Classify a single file with this content."""
    with tempfile.TemporaryDirectory() as d:
        p = os.path.join(d, name)
        with open(p, "w") as fh:
            fh.write(content)
        return headers.classify(p)


class TestGrantsAreFound(unittest.TestCase):
    def test_spdx_tag(self):
        self.assertEqual({"SPDX"}, one("// SPDX-License-Identifier: MIT\nexport {};\n"))

    def test_spdx_tag_agpl(self):
        self.assertIn("SPDX", one("/* SPDX-License-Identifier: AGPL-3.0-or-later */\n"))

    def test_copyright_with_year(self):
        self.assertEqual({"COPYRIGHT"}, one("// Copyright 2026 Example University\n"))

    def test_copyright_with_c_marker(self):
        self.assertEqual({"COPYRIGHT"}, one("/* Copyright (c) Example Ltd */\n"))

    def test_mit_operative_sentence(self):
        got = one("/*\n * Copyright (c) 2026 X\n *\n * Permission is hereby granted, free of\n"
                  " * charge, to any person obtaining a copy\n */\n")
        self.assertEqual({"COPYRIGHT", "GRANT_MIT"}, got)

    def test_apache_operative_sentence(self):
        self.assertIn("GRANT_APACHE", one("// Licensed under the Apache License, Version 2.0\n"))

    def test_agpl_operative_sentence(self):
        got = one("/* This program is free software: you can redistribute it */\n")
        self.assertIn("GRANT_GPL", got)

    def test_agpl_named(self):
        self.assertIn("GRANT_GPL", one("// GNU Affero General Public License v3\n"))


class TestNearMissesAreRejected(unittest.TestCase):
    """The defect this probe could produce is counting a MENTION as a GRANT."""

    def test_manifest_style_license_field_is_not_a_grant(self):
        self.assertEqual(set(), one('const meta = { "license": "MIT" };\n'))

    def test_variable_named_license_is_not_a_grant(self):
        self.assertEqual(set(), one("const licenseKey = process.env.LICENSE_KEY;\n"))

    def test_url_to_a_licence_is_not_a_grant(self):
        self.assertEqual(set(), one("// See https://opensource.org/licenses/MIT\n"))

    def test_prose_about_licensing_is_not_a_grant(self):
        self.assertEqual(set(), one("// TODO: check the license before shipping\n"))

    def test_spdx_without_the_colon_tag_is_not_a_grant(self):
        self.assertEqual(set(), one("// this file is SPDX clean, honest\n"))

    def test_copyright_word_alone_is_not_a_grant(self):
        """No year, no (c), no holder -- an assertion about copyright, not a notice."""
        self.assertEqual(set(), one("// copyright information is in the README\n"))

    def test_dependency_name_is_not_a_grant(self):
        self.assertEqual(set(), one('import x from "license-checker";\n'))


class TestScopeRules(unittest.TestCase):
    def test_grant_below_the_header_window_is_not_a_header_grant(self):
        """A bundled dependency's notice 40 KB into a build artefact is not the
        package's own grant, and counting it would inflate every `dist/` row."""
        content = ("x\n" * 5000) + "Permission is hereby granted, free of charge\n"
        self.assertEqual(set(), one(content))

    def test_binary_content_is_skipped(self):
        with tempfile.TemporaryDirectory() as d:
            p = os.path.join(d, "blob.js")
            with open(p, "wb") as fh:
                fh.write(b"\x00\x01Copyright (c) 2026\x00")
            self.assertEqual(set(), headers.classify(p))

    def test_missing_file_is_not_a_crash(self):
        self.assertEqual(set(), headers.classify("/nonexistent/nope.js"))

    def test_strongest_is_the_strongest_not_the_first(self):
        """A file carrying both a copyright line and an AGPL sentence reports AGPL."""
        got = one("/* Copyright (c) 2026 X\n * This program is free software */\n")
        self.assertEqual({"COPYRIGHT", "GRANT_GPL"}, got)


class TestVendoredNoticesAreNotOwnGrants(unittest.TestCase):
    """The clause this probe added after reading its own first result.

    `@owen-x-tech/canvas-mcp` reported a COPYRIGHT grant on the first run. The notice
    was Meta's, for React, hoisted by a bundler to byte 1197 of a 572 657-byte
    minified `.html` -- inside the header window, and not the package's grant at all.
    Position alone cannot attribute a notice; these tests pin the correction.
    """

    def test_notice_in_minified_bundle_is_vendored(self):
        bundle = ("/**\n * @license React\n *\n * Copyright (c) Meta Platforms, Inc. "
                  "and affiliates.\n *\n * This source code is licensed under the MIT "
                  "license found in the\n * LICENSE file in the root directory.\n */\n")
        bundle += "var a=1;" * 600 + "\n"      # one very long line: minified output
        self.assertEqual({"VENDORED"}, one(bundle, name="mcp-app.html"))

    def test_same_notice_in_authored_source_is_a_grant(self):
        """Identical bytes, short lines: this is the package's own header."""
        src = ("/**\n * Copyright (c) 2026 Example Ltd\n *\n"
               " * Permission is hereby granted, free of charge\n */\n"
               "export const x = 1;\n")
        self.assertEqual({"COPYRIGHT", "GRANT_MIT"}, one(src))

    def test_minified_file_with_no_notice_stays_clean(self):
        self.assertEqual(set(), one("var a=1;" * 600 + "\n"))

    def test_vendored_is_never_the_strongest_grant(self):
        """A tier whose only notice is vendored must report NONE, not a grant."""
        import contextlib
        import io
        with tempfile.TemporaryDirectory() as d:
            pkg = os.path.join(d, "package")
            os.makedirs(pkg)
            with open(os.path.join(pkg, "bundle.js"), "w") as fh:
                fh.write("/* Copyright (c) Meta Platforms, Inc. */\n" + "var a=1;" * 600 + "\n")
            buf = io.StringIO()
            with contextlib.redirect_stdout(buf):
                headers.main(d)
            text_files, with_grant, classes, strongest, vendored = buf.getvalue().strip().split("\t")
            self.assertEqual("1", text_files)
            self.assertEqual("0", with_grant)      # not the package's own
            self.assertEqual("VENDORED", classes)  # but recorded, not discarded
            self.assertEqual("NONE", strongest)
            self.assertEqual("1", vendored)


class TestWalkCounts(unittest.TestCase):
    def test_package_json_is_excluded_from_the_denominator(self):
        """The manifest is p138's instrument, not this one's: its `license` field is
        the very thing this probe exists to distinguish a header grant from."""
        with tempfile.TemporaryDirectory() as d:
            pkg = os.path.join(d, "package")
            os.makedirs(pkg)
            with open(os.path.join(pkg, "package.json"), "w") as fh:
                fh.write('{"license":"MIT"}')
            with open(os.path.join(pkg, "index.js"), "w") as fh:
                fh.write("export {};\n")
            import io
            import contextlib
            buf = io.StringIO()
            with contextlib.redirect_stdout(buf):
                headers.main(d)
            text_files, with_grant, classes, strongest, vendored = buf.getvalue().strip().split("\t")
            self.assertEqual("1", text_files)
            self.assertEqual("0", with_grant)
            self.assertEqual("NONE", classes)
            self.assertEqual("NONE", strongest)
            self.assertEqual("0", vendored)


if __name__ == "__main__":
    unittest.main(verbosity=2)
