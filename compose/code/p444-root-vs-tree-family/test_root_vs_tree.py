#!/usr/bin/env python3
"""Controls for p444. Run: python3 test_root_vs_tree.py   (offline)

This instrument publishes a list of repositories whose root licence is INCOMPLETE, so
its dangerous failure is a false positive: telling a reader that a cleanly-licensed
project has a hidden second grant. All three of its own first-run defects were that,
and each has a control here:

  * root family INHERITED from `p436`'s pass-25 TSV, which predates pass 26's family
    reordering. Comparing a tree classified today against a root classified last pass
    reports classifier version skew as a licence disagreement.
  * a root file NAMED for third-party licences (`LICENSE-3RD-PARTY.txt`) read as a
    second grant by this project.
  * the root file itself counted among the "extras" it is being compared against.
"""
import unittest

import root_vs_tree as R


class TestThirdPartyExclusion(unittest.TestCase):
    def test_third_party_notice_names_are_excluded(self):
        # The live case: `dequelabs/axe-core`'s root `LICENSE-3RD-PARTY.txt` is a real
        # MIT text that reads "Applies to: colorjs.io; core-js-pure; ...". It is
        # p441's BUNDLED class wearing a root path.
        for p in ["LICENSE-3RD-PARTY.txt", "LICENSE-3rd-party.md", "THIRD-PARTY-LICENSES",
                  "licenses/third_party.txt", "NOTICE-3rdparty"]:
            self.assertTrue(R.THIRD_PARTY_RE.search(p), p)

    def test_a_projects_own_split_grants_are_NOT_excluded(self):
        # POSITIVE CONTROL, and the one that matters: `LICENSE-CODE` and
        # `LICENSE-docs` are this project's OWN grants split by artefact, which is the
        # whole shape this instrument exists to find. An over-broad rule would delete
        # the finding along with the false positive.
        for p in ["LICENSE-CODE", "LICENSE-docs", "LICENSE/LICENSE.code",
                  "docs/LICENSE", "docs-site/LICENSE", "ggml/LICENSE",
                  "aoe-web-backend/LICENSE", "LICENSE.md"]:
            self.assertFalse(R.THIRD_PARTY_RE.search(p), p)


class TestEscalationDirection(unittest.TestCase):
    """The direction of the class difference is the finding, not its existence."""

    def test_the_classes_are_disjoint(self):
        self.assertFalse(R.COPYLEFT & R.PERMISSIVE)

    def test_bare_CC_BY_is_in_NEITHER_class_on_purpose(self):
        # `p445` measured that `family_of` reports plain `CC-BY` for five CC-BY-NC
        # payloads -- `facebookresearch/seamless_communication` among them, which
        # `agents/top.md` correctly calls a "hard reject for anything billable".
        # So a `CC-BY` from THIS classifier does not establish that commercial use is
        # permitted, and putting it in PERMISSIVE would let a NonCommercial root be
        # reported as a permissive one. It is deliberately in neither set: such a row
        # escalates to SAME-CLASS and the commercial axis is answered by `p445`.
        self.assertNotIn("CC-BY", R.PERMISSIVE)
        self.assertNotIn("CC-BY", R.COPYLEFT)
        for f in ("CC-BY-NC-4.0", "CC-BY-NC-SA-4.0"):
            self.assertNotIn(f, R.PERMISSIVE)

    def test_copyleft_set_covers_the_families_this_shelf_carries(self):
        for f in ["GPL-2.0", "GPL-3.0", "AGPL-3.0", "LGPL", "EUPL-1.2", "MPL-2.0"]:
            self.assertIn(f, R.COPYLEFT, f)


class TestOne(unittest.TestCase):
    def setUp(self):
        self._tp, self._rb, self._fo = R.E.tree_paths, R.E.read_blob, R.family_of
        self._ig, self._io = R.E.is_grant_path, R.E.is_own_path
        R.E.is_grant_path = lambda p: "licen" in p.lower() or "copying" in p.lower()
        R.E.is_own_path = lambda p: "node_modules" not in p and "vendor" not in p
        R.E.family_marks = lambda t: [t] if t else []

    def tearDown(self):
        R.E.tree_paths, R.E.read_blob, R.family_of = self._tp, self._rb, self._fo
        R.E.is_grant_path, R.E.is_own_path = self._ig, self._io

    def _run(self, paths, bodies, root="LICENSE", inherited="MIT"):
        R.E.tree_paths = lambda slug, timeout=180: paths
        R.E.read_blob = lambda slug, p, timeout=25: bodies.get(p, "")
        R.family_of = lambda body: body or "UNKNOWN"
        return dict(zip(["slug", "root_path", "root_family", "verdict", "escalation",
                         "extra_families", "extra_paths", "bundled", "multi", "skew"],
                        R.one(("o/r", root, inherited))))

    def test_the_root_family_is_RE_DERIVED_not_inherited(self):
        # THE CONTROL THAT CHANGED THE PUBLISHED TABLE. `p436`'s TSV records `GPL` for
        # `dequelabs/axe-core` because MPL s.1.12 names GPL-2.0, LGPL-2.1 and
        # AGPL-3.0; the payload is MPL-2.0. Inheriting the stale family reported a
        # disagreement that was only classifier version skew -- 14 rows of it.
        r = self._run(["LICENSE"], {"LICENSE": "MPL-2.0"}, inherited="GPL")
        self.assertEqual(r["root_family"], "MPL-2.0")
        self.assertEqual(r["skew"], "GPL->MPL-2.0")

    def test_no_skew_is_reported_when_the_families_match(self):
        r = self._run(["LICENSE"], {"LICENSE": "MIT"}, inherited="MIT")
        self.assertEqual(r["skew"], "-")

    def test_the_root_file_is_not_compared_against_itself(self):
        r = self._run(["LICENSE"], {"LICENSE": "MIT"})
        self.assertEqual(r["verdict"], "ROOT-ONLY")

    def test_tree_agrees_when_the_extra_is_the_same_family(self):
        r = self._run(["LICENSE", "app/LICENSE"],
                      {"LICENSE": "MIT", "app/LICENSE": "MIT"})
        self.assertEqual(r["verdict"], "TREE-AGREES")

    def test_tree_adds_when_the_extra_names_a_new_family(self):
        r = self._run(["LICENSE", "LICENSE-CODE"],
                      {"LICENSE": "CC-BY", "LICENSE-CODE": "MIT"}, inherited="CC-BY")
        self.assertEqual(r["verdict"], "TREE-ADDS")
        self.assertEqual(r["extra_families"], "MIT")

    def test_the_escalation_direction_is_recorded(self):
        # permissive root + copyleft deeper: the direction the prediction named, and
        # the one that reaches a contract, because the root is what a proposal quotes.
        r = self._run(["LICENSE", "server/LICENSE"],
                      {"LICENSE": "MIT", "server/LICENSE": "AGPL-3.0"})
        self.assertEqual(r["escalation"], "PERMISSIVE-ROOT-COPYLEFT-TREE")
        r = self._run(["LICENSE", "docs/LICENSE"],
                      {"LICENSE": "AGPL-3.0", "docs/LICENSE": "MIT"},
                      inherited="AGPL-3.0")
        self.assertEqual(r["escalation"], "COPYLEFT-ROOT-PERMISSIVE-TREE")

    def test_same_class_is_not_an_escalation(self):
        r = self._run(["LICENSE", "x/LICENSE"],
                      {"LICENSE": "MIT", "x/LICENSE": "Apache-2.0"})
        self.assertEqual(r["escalation"], "SAME-CLASS")

    def test_bundled_extras_do_not_make_a_finding(self):
        r = self._run(["LICENSE", "node_modules/x/LICENSE"],
                      {"LICENSE": "MIT", "node_modules/x/LICENSE": "GPL-3.0"})
        self.assertEqual(r["verdict"], "BUNDLED-ONLY-EXTRA")
        self.assertEqual(r["bundled"], "1")

    def test_a_third_party_notice_at_root_counts_as_bundled(self):
        r = self._run(["LICENSE", "LICENSE-3RD-PARTY.txt"],
                      {"LICENSE": "MPL-2.0", "LICENSE-3RD-PARTY.txt": "MIT"},
                      inherited="MPL-2.0")
        self.assertEqual(r["verdict"], "BUNDLED-ONLY-EXTRA")

    def test_an_extra_whose_payload_is_not_a_licence_is_ignored(self):
        # p441's stage-2 rule, inherited: a path containing the word "licence" whose
        # body does not classify is a NAME, not a grant.
        r = self._run(["LICENSE", "src/licence.ts"],
                      {"LICENSE": "MIT", "src/licence.ts": ""})
        self.assertEqual(r["verdict"], "ROOT-ONLY")

    def test_unresolvable_tree_is_not_a_clean_root_only(self):
        R.E.tree_paths = lambda slug, timeout=180: None
        R.E.read_blob = lambda slug, p, timeout=25: "MIT"
        R.family_of = lambda b: b or "UNKNOWN"
        self.assertEqual(R.one(("o/r", "LICENSE", "MIT"))[3], "UNRESOLVABLE")

    def test_every_row_has_ten_columns(self):
        for paths, bodies in [(["LICENSE"], {"LICENSE": "MIT"}),
                              (["LICENSE", "a/LICENSE"],
                               {"LICENSE": "MIT", "a/LICENSE": "GPL-3.0"}),
                              (["LICENSE", "node_modules/x/LICENSE"],
                               {"LICENSE": "MIT", "node_modules/x/LICENSE": "MIT"})]:
            R.E.tree_paths = lambda slug, timeout=180, _p=paths: _p
            R.E.read_blob = lambda slug, p, timeout=25, _b=bodies: _b.get(p, "")
            R.family_of = lambda b: b or "UNKNOWN"
            self.assertEqual(len(R.one(("o/r", "LICENSE", "MIT"))), 10)


class TestPublishedResultIntegrity(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        import os
        here = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(here, "result.2026-10-07.tsv")) as f:
            cls.rows = [l.rstrip("\n").split("\t") for l in f][1:]

    def test_denominator_is_the_licensed_side(self):
        self.assertEqual(len(self.rows), 412)

    def test_no_short_rows(self):
        self.assertTrue(all(len(r) == 10 for r in self.rows))

    def test_the_prediction_number_holds(self):
        # "more than five" -- written as the inequality, not the count (P399).
        self.assertGreater(len([r for r in self.rows if r[3] == "TREE-ADDS"]), 5)

    def test_the_predicted_interesting_class_is_empty(self):
        self.assertEqual(
            [r[0] for r in self.rows if r[4] == "PERMISSIVE-ROOT-COPYLEFT-TREE"], [])

    def test_the_escalation_runs_the_other_way(self):
        self.assertTrue([r for r in self.rows
                         if r[4] == "COPYLEFT-ROOT-PERMISSIVE-TREE"])

    def test_no_third_party_notice_is_in_a_finding(self):
        for r in self.rows:
            if r[3] == "TREE-ADDS":
                self.assertFalse(R.THIRD_PARTY_RE.search(r[6]), r[0])

    def test_the_classifier_skew_is_reported_and_nonzero(self):
        skew = [r for r in self.rows if r[9] != "-"]
        self.assertTrue(skew, "no skew reported -- the re-derivation is not running")
        self.assertLess(len(skew), 100)


if __name__ == "__main__":
    unittest.main(verbosity=2)
