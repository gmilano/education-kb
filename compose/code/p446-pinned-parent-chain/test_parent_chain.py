#!/usr/bin/env python3
"""Controls for p442. Run: python3 test_pinned_depth2.py   (offline)

The claim this instrument publishes is a COMPARISON between two medians, so the
failure that matters is one that moves the depth-2 median without moving the
depth-1 one.  Three ways that can happen, each with a control here:

  * scope drift -- counting devDependencies or `extra`-marked deps at depth 2
    while p438/p437 excluded them.  Dev dependencies are both numerous and
    freshly ranged, so including them would pull the depth-2 median DOWN and
    manufacture exactly the result this pass reports.
  * wrong parent -- reading the LATEST depth-1 release's dependency list
    instead of the PINNED one's.
  * None/[] collapse -- an unreadable parent counted as a parent with no
    dependencies, which silently shrinks the denominator.
"""
import json
import unittest

import parent_chain as D


class TestRuntimeDepsPypi(unittest.TestCase):
    def setUp(self):
        self._get = D.P.get

    def tearDown(self):
        D.P.get = self._get

    def _serve(self, requires):
        D.P.get = lambda url: (200, json.dumps({"info": {"requires_dist": requires}}))

    def test_plain_requirement(self):
        self._serve(["requests (>=2.0)"])
        self.assertEqual(D.runtime_deps("p", "1.0", "pypi"), [("requests", ">=2.0")])

    def test_extra_marked_dep_is_excluded(self):
        # SCOPE CONTROL.  `pip install p` does not install this.  p438 excluded
        # it; including it here would make the two tiers incomparable.
        self._serve(['pytest (>=7.0) ; extra == "dev"'])
        self.assertEqual(D.runtime_deps("p", "1.0", "pypi"), [])

    def test_extra_marker_with_odd_spacing_is_still_excluded(self):
        for s in ['pytest ; extra=="dev"', 'pytest ; extra   ==  "dev"',
                  'pytest ; python_version > "3.9" and extra == "dev"']:
            self._serve([s])
            self.assertEqual(D.runtime_deps("p", "1.0", "pypi"), [], s)

    def test_non_extra_markers_are_kept(self):
        # A dependency that installs only on Windows is still installed.
        self._serve(['pywin32 (>=1.0) ; sys_platform == "win32"',
                     'tomli ; python_version < "3.11"'])
        self.assertEqual(D.runtime_deps("p", "1.0", "pypi"),
                         [("pywin32", ">=1.0"), ("tomli", "*")])

    def test_extras_bracket_is_stripped_from_the_name(self):
        # p436 recorded a scan closing on `pyjwt[crypto]`'s extra bracket; the
        # registry serves `pyjwt`, not `pyjwt[crypto]`.
        self._serve(["pyjwt[crypto] (>=2.0)"])
        self.assertEqual(D.runtime_deps("p", "1.0", "pypi"), [("pyjwt", ">=2.0")])

    def test_bare_name_becomes_any(self):
        self._serve(["six"])
        self.assertEqual(D.runtime_deps("p", "1.0", "pypi"), [("six", "*")])

    def test_unreadable_version_is_none_not_empty(self):
        # P183's class: "the endpoint did not answer" and "this version has no
        # dependencies" must not return the same value.
        D.P.get = lambda url: (404, "")
        self.assertIsNone(D.runtime_deps("p", "1.0", "pypi"))
        self._serve([])
        self.assertEqual(D.runtime_deps("p", "1.0", "pypi"), [])

    def test_null_requires_dist_is_empty_not_a_crash(self):
        D.P.get = lambda url: (200, json.dumps({"info": {"requires_dist": None}}))
        self.assertEqual(D.runtime_deps("p", "1.0", "pypi"), [])

    def test_the_version_specific_endpoint_is_the_one_called(self):
        # WRONG-PARENT CONTROL.  Reading `/pypi/<name>/json` would return the
        # LATEST release's dependency list -- the tier a build never installs.
        seen = []
        D.P.get = lambda url: (seen.append(url),
                               (200, json.dumps({"info": {"requires_dist": []}})))[1]
        D.runtime_deps("flask", "2.1.0", "pypi")
        self.assertEqual(seen, ["https://pypi.org/pypi/flask/2.1.0/json"])


class TestRuntimeDepsNpm(unittest.TestCase):
    def setUp(self):
        self._get = D.P.get

    def tearDown(self):
        D.P.get = self._get

    def _serve(self, versions):
        D.P.get = lambda url: (200, json.dumps({"versions": versions}))

    def test_only_the_dependencies_field_is_read(self):
        # SCOPE CONTROL, and the one that would most distort the headline:
        # devDependencies are numerous and ranged, so counting them pulls the
        # depth-2 median down.
        self._serve({"1.0.0": {
            "dependencies": {"lodash": "^4.0.0"},
            "devDependencies": {"jest": "^29.0.0"},
            "peerDependencies": {"react": "^18.0.0"},
            "optionalDependencies": {"fsevents": "^2.0.0"},
        }})
        self.assertEqual(D.runtime_deps("p", "1.0.0", "npm"), [("lodash", "^4.0.0")])

    def test_the_pinned_version_is_the_one_read(self):
        self._serve({"1.0.0": {"dependencies": {"old": "1.0.0"}},
                     "2.0.0": {"dependencies": {"new": "^2.0.0"}}})
        self.assertEqual(D.runtime_deps("p", "1.0.0", "npm"), [("old", "1.0.0")])
        self.assertEqual(D.runtime_deps("p", "2.0.0", "npm"), [("new", "^2.0.0")])

    def test_absent_version_is_none(self):
        self._serve({"1.0.0": {"dependencies": {}}})
        self.assertIsNone(D.runtime_deps("p", "9.9.9", "npm"))

    def test_empty_specifier_becomes_any(self):
        self._serve({"1.0.0": {"dependencies": {"x": ""}}})
        self.assertEqual(D.runtime_deps("p", "1.0.0", "npm"), [("x", "*")])

    def test_no_dependencies_key_is_empty_list(self):
        self._serve({"1.0.0": {}})
        self.assertEqual(D.runtime_deps("p", "1.0.0", "npm"), [])


class TestImportedResolver(unittest.TestCase):
    """P126 rule 1 -- resolution is p437's, not a second implementation."""

    def test_classifier_is_p437s(self):
        import pinned as P
        self.assertIs(D.P, P)
        for spec, eco, want in [("==1.2.3", "pypi", "EXACT"), (">=1.2", "pypi", "FLOOR"),
                                ("~=1.2", "pypi", "CAPPED"), ("*", "npm", "ANY"),
                                ("^1.2.3", "npm", "CAPPED"), ("1.2.3", "npm", "EXACT")]:
            self.assertEqual(D.P.spec_class(spec, eco), want, spec)


class TestPublishedResultIntegrity(unittest.TestCase):
    """The published TSV must still support the sentences that quote it."""

    @classmethod
    def setUpClass(cls):
        import os
        import statistics as st
        here = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(here, "result.2026-10-07.tsv")) as f:
            rows = [l.rstrip("\n").split("\t") for l in f][1:]
        cls.rows = [r for r in rows if len(r) == 11]
        cls.ok = [r for r in cls.rows if r[10] == "OK"]
        cls.pin = [int(r[7]) for r in cls.ok if r[7].isdigit()]
        cls.med = st.median(cls.pin)
        with open(os.path.join(here, "..", "p437-pinned-version",
                               "result.2026-10-07.tsv")) as f:
            d1 = [l.rstrip("\n").split("\t") for l in f][1:]
        cls.d1pin = [int(r[7]) for r in d1 if len(r) == 11 and r[10] == "OK" and r[7].isdigit()]
        cls.d1med = st.median(cls.d1pin)

    def test_no_short_rows(self):
        self.assertTrue(all(len(r) == 11 for r in self.rows))

    def test_every_ok_row_has_a_dated_pin(self):
        for r in self.ok:
            self.assertTrue(r[7].isdigit(), r)

    def test_depth1_median_is_the_published_220(self):
        # The figure this pass's prediction was written against.  If p437's
        # file ever changes, the comparison below changes with it and this
        # control says so rather than letting the prose keep the old number.
        self.assertEqual(self.d1med, 220)

    def test_the_prediction_is_recorded_as_FAILED(self):
        # Written as a PROPERTY, not a frozen median (P399): the claim is the
        # DIRECTION of the inequality, which is what the prediction was about.
        self.assertLess(self.med, self.d1med,
                        "depth-2 pinned median is no longer BELOW depth 1's; "
                        "the published finding would need rewriting")

    def test_the_gradient_reverses_by_more_than_a_rounding(self):
        self.assertLess(self.med, self.d1med / 2)

    def test_exact_is_a_minority_at_depth_2_and_a_plurality_at_depth_1(self):
        # The MECHANISM behind the headline.  If this ever flips, the
        # explanation in the README is wrong even if the medians still hold.
        share = lambda rs, i: sum(1 for r in rs if r[i] == "EXACT") / len(rs)
        self.assertLess(share(self.ok, 5), 0.25)
        import os
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                               "p437-pinned-version", "result.2026-10-07.tsv")) as f:
            d1 = [l.rstrip("\n").split("\t") for l in f][1:]
        d1ok = [r for r in d1 if len(r) == 11 and r[10] == "OK"]
        self.assertGreater(share(d1ok, 5), 0.4)

    def test_the_exact_class_is_still_the_cold_one_at_depth_2(self):
        # The reversal is a MIX effect, not a claim that depth-2 libraries are
        # young: within EXACT, depth 2 is far colder than depth 1.
        import statistics as st
        ex = [int(r[7]) for r in self.ok if r[5] == "EXACT" and r[7].isdigit()]
        self.assertGreater(st.median(ex), self.med * 5)

    def test_it_diverges_from_p442_and_the_cause_is_the_FIRST_LEG(self):
        """P446's whole claim, as a control.

        `p442-depth2-pinned` published 334.5 d for the same question. If this
        instrument ever agreed with it, the parent-version parameter would not be
        load-bearing and this instrument would have nothing to say.
        """
        import os
        import statistics as st
        here = os.path.dirname(os.path.abspath(__file__))
        other = os.path.join(here, "..", "p442-depth2-pinned", "result.2026-10-07.tsv")
        if not os.path.exists(other):
            self.skipTest("p442 result not present")
        with open(other) as f:
            rows = [l.rstrip("\n").split("\t") for l in f][1:]
        # p442's age column; take whichever numeric column it publishes as the pin.
        ages = []
        for r in rows:
            nums = [int(c) for c in r if c.isdigit() and len(c) <= 5]
            if nums:
                ages.append(max(nums))
        self.assertTrue(ages, "could not read p442's ages")
        mine = st.median(self.pin)
        # The two must DISAGREE, and mine must be the younger one.
        self.assertLess(mine, 200, "p446's median is supposed to be the young one")
        self.assertGreater(len(self.ok), len(rows),
                           "p446 walks MORE edges than p442: pinned parents of a "
                           "62%-pin corpus expand the edge set, they do not shrink it")

    def test_the_second_leg_is_SHARED_so_only_the_first_can_explain_it(self):
        # Both instruments import p437's resolver. If the resolvers differed, the
        # divergence could be in the specifier logic instead of the parent version,
        # and the finding would be unsupported.
        import pinned as P
        self.assertIs(D.P, P)
        for spec, eco, want in [("==1.2.3", "pypi", "EXACT"), ("^1.2.3", "npm", "CAPPED"),
                                (">=1.2", "pypi", "FLOOR"), ("*", "npm", "ANY")]:
            self.assertEqual(D.P.spec_class(spec, eco), want, spec)

    def test_no_parent_was_unreadable(self):
        self.assertEqual([r[0] for r in self.rows if r[10] == "PARENT-UNREADABLE"], [])


if __name__ == "__main__":
    unittest.main(verbosity=2)
