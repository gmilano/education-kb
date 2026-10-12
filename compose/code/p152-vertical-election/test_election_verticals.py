#!/usr/bin/env python3
"""Authored fixtures, offline. No network, no clone, stdlib only.

🔵 The cases that carry this suite are the NEGATIVE ones: the three election forms that
must be told apart, and the two reasons a tree reads `SILENT` that must NOT be told alike.
"""
import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import election_verticals as e  # noqa: E402
import omission as o  # noqa: E402

# ── the three real notice shapes, transcribed from the trees p152 measured ─────────────
MOODLE = """\
<?php
// This file is part of Moodle - http://moodle.org/
//
// Moodle is free software: you can redistribute it and/or modify
// it under the terms of the GNU General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.
"""

CANVAS = """\
# frozen_string_literal: true
#
# Copyright (C) 2016 - present Instructure, Inc.
#
# This file is part of Canvas.
#
# Canvas is free software: you can redistribute it and/or modify it under
# the terms of the GNU Affero General Public License as published by the Free
# Software Foundation, version 3 of the License.
"""

BBB = """\
/*
    BigBlueButton open source conferencing system - http://www.bigbluebutton.org/

    This program is free software; you can redistribute it and/or modify it under the
    terms of the GNU Lesser General Public License as published by the Free Software
    Foundation; either version 3.0 of the License, or (at your option) any later
    version.
*/
"""

ONLY_WORDED = """\
// Licensed under the GNU General Public License version 3 only.
"""

NOTICE_NO_VERSION = """\
# Released under the GNU General Public License. See LICENSE.
"""

PLAIN = "import os\n\n\ndef f():\n    return 1\n"


def tree(files):
    d = tempfile.mkdtemp()
    for rel, body in files.items():
        p = os.path.join(d, rel)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, "w", encoding="utf-8") as fh:
            fh.write(body)
    return d


class TheThreeElectionForms(unittest.TestCase):
    """🟢 The point of the module: three forms, told apart."""

    def test_or_later_is_read(self):
        self.assertEqual(o.classify(e.normalise(MOODLE)), "OR_LATER")

    def test_only_worded_is_read(self):
        self.assertEqual(o.classify(e.normalise(ONLY_WORDED)), "ONLY_WORDED")

    def test_only_by_OMISSION_is_read(self):
        """🔴 The form p151's matchers call `SILENT`. This is the whole finding."""
        self.assertEqual(o.classify(e.normalise(CANVAS)), "ONLY_OMISSION")

    def test_p151s_matchers_are_silent_on_the_omission_form(self):
        """🔴 Asserted, not described: the omission form fires NEITHER p151 matcher."""
        t = e.normalise(CANVAS)
        self.assertIsNone(e.ELECTION_LATER.search(t))
        self.assertIsNone(e.ELECTION_ONLY.search(t))
        self.assertIsNotNone(e.GNU_NOTICE.search(t), "but it IS a GNU notice")

    def test_lgpl_with_a_dotted_version_still_reads_or_later(self):
        """`version 3.0 of the License` -- BBB's real shape, not GPL's `version 3`."""
        self.assertEqual(o.classify(e.normalise(BBB)), "OR_LATER")


class TheTwoReasonsForSilence(unittest.TestCase):
    """🔴 `P42`: a tree with no notice and a tree whose notices decline to elect both
    read zero on p151's instrument, and they are not the same fact."""

    def test_no_notice_at_all(self):
        self.assertEqual(o.classify(e.normalise(PLAIN)), "NO_NOTICE")

    def test_notice_that_never_reaches_a_version(self):
        """🟢 All 17 notice-bearing files in p151's seven rows are THIS class."""
        self.assertEqual(o.classify(e.normalise(NOTICE_NO_VERSION)),
                         "NOTICE_NO_VERSION")

    def test_the_notice_denominator_separates_them(self):
        kolibri = tree({"a.py": PLAIN, "b.py": PLAIN})
        canvasish = tree({"a.rb": CANVAS, "b.rb": CANVAS})
        rk, _ = o.measure(kolibri)
        rc, _ = o.measure(canvasish)
        self.assertEqual((rk["scanned"], rk["NO_NOTICE"]), (2, 2))
        self.assertEqual(rc["ONLY_OMISSION"], 2)
        # 🔴 p151's instrument reports both as SILENT; the denominator does not.
        self.assertEqual(e.measure(kolibri)["election"], "SILENT")
        self.assertEqual(e.measure(canvasish)["election"], "SILENT")
        self.assertEqual(e.measure(kolibri)["notices"], 0)
        self.assertEqual(e.measure(canvasish)["notices"], 2)


class TheCommentPrefixDefect(unittest.TestCase):
    """🔵 p151's defect 1, re-asserted here because this module re-implements it."""

    def test_a_block_comment_does_not_break_the_phrase(self):
        self.assertIn("or (at your option) any later version",
                      e.normalise(MOODLE).lower())

    def test_without_normalisation_the_match_is_lost(self):
        raw = MOODLE
        self.assertIsNone(e.ELECTION_LATER.search(raw),
                          "the raw text must NOT match -- that is why normalise() exists")
        self.assertIsNotNone(e.ELECTION_LATER.search(e.normalise(raw)))


class TheLicenceFileExclusion(unittest.TestCase):
    """🔴 p151's defect 2: a badge image is not a licence."""

    def test_a_licence_file_is_excluded_at_any_depth(self):
        d = tree({"LICENSE": MOODLE, "deep/nested/COPYING": MOODLE, "x.py": PLAIN})
        self.assertEqual([os.path.basename(p) for p in e.walk_sources(d)], ["x.py"])
        self.assertEqual(len(e.licence_bodies(d)), 2)

    def test_a_badge_image_is_not_a_licence_file(self):
        self.assertFalse(e.LICENCE_FILE.match("license.svg"))
        self.assertTrue(e.LICENCE_FILE.match("LICENSE"))
        self.assertTrue(e.LICENCE_FILE.match("LICENCE.md"))

    def test_an_svg_is_not_a_source_file_either(self):
        d = tree({"docs/license.svg": MOODLE, "x.py": PLAIN})
        self.assertEqual([os.path.basename(p) for p in e.walk_sources(d)], ["x.py"])


class TheVendoredAttributionDefect(unittest.TestCase):
    """🔴 `T85`: Sakai's one `OR_LATER` hit is a bundled third-party library.

    🔵 The instrument CANNOT currently separate them, and this suite pins that limit as a
    known-wrong verdict rather than leaving it to be rediscovered."""

    TRIMPATH = """\
/**
 * TrimPath Template. Release 1.0.38.
 * Copyright (C) 2004, 2005 Metaha.
 *
 * This program is free software; you can redistribute it and/or
 * modify it under the terms of the GNU General Public License
 * as published by the Free Software Foundation; either version 2
 * of the License, or (at your option) any later version.
 */
"""

    def test_a_vendored_file_elects_and_the_subject_did_not(self):
        d = tree({"library/src/webapp/js/trimpath-template-latest.js": self.TRIMPATH,
                  "app/Main.java": PLAIN})
        r = e.measure(d)
        self.assertEqual(r["election"], "OR_LATER")
        self.assertEqual(len(r["later"]), 1)

    def test_the_known_limit_the_skip_dirs_do_not_catch_it(self):
        """🔴 `vendor/` is skipped; `library/src/webapp/js/` is not, and Sakai's
        bundled copy lives in the second shape."""
        self.assertIn("vendor", e.SKIP_DIRS)
        self.assertNotIn("library", e.SKIP_DIRS)

    def test_a_third_party_holder_is_visible_even_though_unused(self):
        """🟢 The signal a fix would read: the notice's own copyright holder."""
        self.assertIn("Metaha", self.TRIMPATH)


class TheVerdictLadder(unittest.TestCase):
    def test_both_directions_conflict_is_reported_not_resolved(self):
        self.assertEqual(e.verdict(["a.py"], ["b.py"], []), "BOTH_CONFLICT")

    def test_spdx_is_the_lowest_rung(self):
        self.assertEqual(e.verdict([], [], ["GPL-3.0-or-later"]), "SPDX_LATER")

    def test_silence_is_the_default(self):
        self.assertEqual(e.verdict([], [], []), "SILENT")

    def test_mixed_subject_is_reported_not_resolved(self):
        c = dict(scanned=3, OR_LATER=1, ONLY_WORDED=0, ONLY_OMISSION=1,
                 NOTICE_NO_VERSION=0, NO_NOTICE=1)
        self.assertEqual(o.verdict(c), "MIXED:OR_LATER+ONLY_OMISSION")


class TheGrantVerbWindow(unittest.TestCase):
    """🔵 An omission verdict must not be assembled out of two sentences."""

    def test_the_grant_verb_and_a_version_are_required_together(self):
        self.assertIsNone(o.GRANT_WITH_VERSION.search(
            e.normalise("Licensed under the GPL. Elsewhere: version 3 of something.")))

    def test_the_canvas_sentence_matches(self):
        m = o.GRANT_WITH_VERSION.search(e.normalise(CANVAS))
        self.assertIsNotNone(m)
        self.assertEqual(m.group(1), "3")

    def test_the_moodle_sentence_also_matches_but_or_later_wins(self):
        """🟢 Ordering is load-bearing: the or-later clause is tested FIRST, so a
        tree that states or-later is never filed as an omission."""
        self.assertIsNotNone(o.GRANT_WITH_VERSION.search(e.normalise(MOODLE)))
        self.assertEqual(o.classify(e.normalise(MOODLE)), "OR_LATER")


class TheEmptyInputGuard(unittest.TestCase):
    """🔵 `P542`: an empty walk must not be indistinguishable from a clean one."""

    def test_an_empty_tree_scans_zero_and_says_so(self):
        d = tree({})
        r = e.measure(d)
        self.assertEqual(r["scanned"], 0)
        self.assertEqual(r["notices"], 0)

    def test_a_missing_tree_does_not_crash_the_header_reader(self):
        self.assertEqual(e.head("/nonexistent/p152/nope.py"), "")


if __name__ == "__main__":
    r = unittest.main(exit=False, verbosity=0).result
    print("p152-vertical-election: %d tests, %d passed, %d failed"
          % (r.testsRun, r.testsRun - len(r.failures) - len(r.errors),
             len(r.failures) + len(r.errors)))
    sys.exit(1 if (r.failures or r.errors) else 0)
