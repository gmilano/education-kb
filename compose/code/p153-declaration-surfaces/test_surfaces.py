#!/usr/bin/env python3
"""p153 -- offline tests for the declaration-surface counter. No network, no clone.

Fixtures are transcribed from the real shapes this pass measured:
  * lumen        -- GPL-3.0 body + MIT badge + MIT pyproject  (the DISAGREE case)
  * canvas-mcp   -- MIT body + MIT badge                      (the AGREE case)
  * tutor-lms-mcp-- no licence file at all                    (the NONE/thin case)
"""
import os
import shutil
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import surfaces as S

GPL3_HEAD = """                    GNU GENERAL PUBLIC LICENSE
                       Version 3, 29 June 2007

 Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
 Everyone is permitted to copy and distribute verbatim copies
 of this license document, but changing it is not allowed.
"""

AGPL3_HEAD = """                    GNU AFFERO GENERAL PUBLIC LICENSE
                       Version 3, 19 November 2007

 Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
"""

LGPL3_HEAD = """                   GNU LESSER GENERAL PUBLIC LICENSE
                       Version 3, 29 June 2007
"""

GPL2_HEAD = """                    GNU GENERAL PUBLIC LICENSE
                       Version 2, June 1991
"""

MIT_BODY = """MIT License

Copyright (c) 2025 Vishal Sachdev

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction.
"""

APACHE_BODY = """                                 Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/
"""

ECL_BODY = """Educational Community License, Version 2.0

Copyright 2026 The Sakai Foundation
"""


class Tree:
    """A throwaway subject tree."""

    def __init__(self):
        self.root = tempfile.mkdtemp(prefix="p153-")

    def write(self, rel, text):
        p = os.path.join(self.root, rel)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, "w", encoding="utf-8") as fh:
            fh.write(text)
        return p

    def close(self):
        shutil.rmtree(self.root, ignore_errors=True)


class TestClassifyBody(unittest.TestCase):
    def test_gpl3_body(self):
        self.assertEqual(S.classify_body(GPL3_HEAD), "GPL-3.0")

    def test_agpl_is_not_read_as_gpl(self):
        # The AGPL body must win over the GPL marker, or canvas-lms reads as GPL.
        self.assertEqual(S.classify_body(AGPL3_HEAD), "AGPL-3.0")

    def test_lgpl_is_not_read_as_gpl(self):
        self.assertEqual(S.classify_body(LGPL3_HEAD), "LGPL-3.0")

    def test_gpl2_version_is_read_from_body(self):
        self.assertEqual(S.classify_body(GPL2_HEAD), "GPL-2.0")

    def test_mit_body(self):
        self.assertEqual(S.classify_body(MIT_BODY), "MIT")

    def test_apache_body(self):
        self.assertEqual(S.classify_body(APACHE_BODY), "Apache-2.0")

    def test_ecl_body(self):
        self.assertEqual(S.classify_body(ECL_BODY), "ECL-2.0")

    def test_unknown_body_is_none_not_a_guess(self):
        self.assertIsNone(S.classify_body("Copyright 2026. All rights reserved."))

    def test_empty_body_is_none(self):
        self.assertIsNone(S.classify_body(""))


class TestNormaliseAndFamily(unittest.TestCase):
    def test_normalise_aliases(self):
        self.assertEqual(S.normalise_id("mit"), "MIT")
        self.assertEqual(S.normalise_id("Apache 2.0"), "Apache-2.0")
        self.assertEqual(S.normalise_id("GPLv3"), "GPL-3.0")
        self.assertEqual(S.normalise_id("AGPL-3.0-only"), "AGPL-3.0-only")

    def test_normalise_strips_quotes_and_urlencoding(self):
        self.assertEqual(S.normalise_id('"MIT"'), "MIT")
        self.assertEqual(S.normalise_id("Apache%202.0"), "Apache-2.0")

    def test_normalise_blank_is_none(self):
        self.assertIsNone(S.normalise_id("   "))
        self.assertIsNone(S.normalise_id(None))

    def test_family_collapses_the_election(self):
        # T81's -only/-or-later question is NOT a disagreement for FJ's purposes.
        self.assertEqual(S.family("GPL-3.0-only"), S.family("GPL-3.0-or-later"))

    def test_family_keeps_agpl_and_gpl_apart(self):
        self.assertNotEqual(S.family("AGPL-3.0-only"), S.family("GPL-3.0-only"))

    def test_family_of_none(self):
        self.assertIsNone(S.family(None))


class TestSurfaces(unittest.TestCase):
    def setUp(self):
        self.t = Tree()

    def tearDown(self):
        self.t.close()

    def test_file_surface_found_and_classified(self):
        self.t.write("LICENSE", GPL3_HEAD)
        s = S.surface_file(self.t.root)
        self.assertEqual((s["surface"], s["spdx"], s["where"]), ("FILE", "GPL-3.0", "LICENSE"))

    def test_file_surface_absent(self):
        self.assertIsNone(S.surface_file(self.t.root))

    def test_file_surface_present_but_unclassifiable(self):
        self.t.write("LICENSE", "All rights reserved, 2026.")
        s = S.surface_file(self.t.root)
        self.assertEqual(s["surface"], "FILE")
        self.assertIsNone(s["spdx"])

    def test_badge_surface_from_shields_io(self):
        self.t.write("README.md", "# x\n\n[![License: MIT]"
                     "(https://img.shields.io/badge/license-MIT-yellow)](LICENSE)\n")
        s = S.surface_badge(self.t.root)
        self.assertEqual(s["spdx"], "MIT")
        self.assertEqual(s["where"], "README.md:3")

    def test_badge_surface_from_plain_text(self):
        self.t.write("README.md", "# x\nLicense: Apache-2.0\n")
        self.assertEqual(S.surface_badge(self.t.root)["spdx"], "Apache-2.0")

    def test_badge_decodes_the_shields_double_hyphen_escape(self):
        # The defect this pass found in its OWN matcher: "Apache--2.0" is Apache-2.0,
        # and a non-greedy capture read it as "Apache", producing a false DISAGREE.
        self.t.write("README.md", "# x\n[![License]"
                     "(https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)\n")
        self.assertEqual(S.surface_badge(self.t.root)["spdx"], "Apache-2.0")

    def test_badge_decodes_underscore_as_space(self):
        self.t.write("README.md", "[![L]"
                     "(https://img.shields.io/badge/license-Apache_2.0-blue.svg)](x)\n")
        self.assertEqual(S.surface_badge(self.t.root)["spdx"], "Apache-2.0")

    def test_badge_with_query_string_is_trimmed(self):
        self.t.write("README.md", "[![L]"
                     "(https://img.shields.io/badge/license-MIT-yellow?style=flat-square)](L)\n")
        self.assertEqual(S.surface_badge(self.t.root)["spdx"], "MIT")

    def test_badge_message_without_colour_still_decodes(self):
        self.assertEqual(S.decode_badge_message("MIT"), "MIT")

    def test_badge_absent_when_readme_silent(self):
        self.t.write("README.md", "# x\nnothing here\n")
        self.assertIsNone(S.surface_badge(self.t.root))

    def test_metadata_pyproject_text_form(self):
        self.t.write("apps/backend/pyproject.toml",
                     '[project]\nname = "b"\nlicense = { text = "MIT" }\n')
        got = S.surface_metadata(self.t.root)
        self.assertEqual([(g["surface"], g["spdx"]) for g in got], [("METADATA", "MIT")])

    def test_metadata_package_json_root(self):
        self.t.write("package.json", '{"name":"x","license":"Apache-2.0"}')
        got = S.surface_metadata(self.t.root)
        self.assertEqual(got[0]["spdx"], "Apache-2.0")

    def test_metadata_package_json_malformed_is_skipped_not_crashed(self):
        self.t.write("package.json", "{not json")
        self.assertEqual(S.surface_metadata(self.t.root), [])

    def test_spdx_header_surface(self):
        self.t.write("src/a.py", "# SPDX-License-Identifier: AGPL-3.0-only\nx = 1\n")
        got = S.surface_spdx(self.t.root)
        self.assertEqual([(g["surface"], g["spdx"]) for g in got],
                         [("SPDX", "AGPL-3.0-only")])

    def test_spdx_skips_vendored_trees(self):
        self.t.write("node_modules/dep/a.js", "// SPDX-License-Identifier: GPL-2.0\n")
        self.assertEqual(S.surface_spdx(self.t.root), [])


class TestVerdict(unittest.TestCase):
    def setUp(self):
        self.t = Tree()

    def tearDown(self):
        self.t.close()

    def test_lumen_shape_is_three_surfaces_and_DISAGREE(self):
        """The real finding: GPL-3.0 body, MIT badge, MIT pyproject."""
        self.t.write("LICENSE", GPL3_HEAD)
        self.t.write("README.md", "# lumen\n\n[![License: MIT]"
                     "(https://img.shields.io/badge/license-MIT-yellow)](LICENSE)\n")
        self.t.write("apps/backend/pyproject.toml", 'license = { text = "MIT" }\n')
        got = S.audit(self.t.root)
        self.assertEqual(len(got), 3)
        self.assertEqual(S.verdict(got), "DISAGREE")
        self.assertEqual(S.authoritative(got), "GPL-3.0")

    def test_agreeing_two_surfaces(self):
        self.t.write("LICENSE", MIT_BODY)
        self.t.write("README.md", "License: MIT\n")
        got = S.audit(self.t.root)
        self.assertEqual(S.verdict(got), "AGREE")

    def test_single_surface(self):
        self.t.write("LICENSE", MIT_BODY)
        self.assertEqual(S.verdict(S.audit(self.t.root)), "SINGLE")

    def test_no_surface_at_all(self):
        self.assertEqual(S.verdict(S.audit(self.t.root)), "NONE")
        self.assertIsNone(S.authoritative(S.audit(self.t.root)))

    def test_election_variants_do_not_count_as_disagreement(self):
        self.t.write("LICENSE", GPL3_HEAD)
        self.t.write("src/a.py", "# SPDX-License-Identifier: GPL-3.0-or-later\n")
        got = S.audit(self.t.root)
        self.assertEqual(S.verdict(got), "AGREE")

    def test_unclassified_file_only_is_not_agreement(self):
        # Authored expectation was SINGLE; the module returned UNCLASSIFIED and the
        # module is RIGHT -- a body that could not be classified must never be reported
        # as a known declaration. The test was corrected, not the matcher.
        self.t.write("LICENSE", "All rights reserved.")
        self.assertEqual(S.verdict(S.audit(self.t.root)), "UNCLASSIFIED")


if __name__ == "__main__":
    unittest.main(verbosity=2)
