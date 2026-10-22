"""`ACTION ZZ-ap`'s controls.  Every fixture is a payload read FIRST-HAND off its real
default ref at p382, and every one is named with its slug, ref, path and byte length so a
successor can re-read it rather than trust this file.

🔵 Fixtures live beside this file as `fixtures/*.txt`, byte-for-byte as served by
`raw.githubusercontent.com`.  p382 could not run this suite in its own sandbox (the
execution lane was DENIED for cloned code); it was authored and run in the open lane and
committed so that the first pass with an execution lane can put it under `make hooks`.
"""

import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import subtree_grant as sg  # noqa: E402

FX = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fixtures")

# slug -> (file, ref, path, bytes-as-read-at-p382)
FIXTURES = {
    "oaknational/oak-curriculum-ontology":
        ("oak-curriculum-ontology.LICENSE.md.txt", "main", "LICENSE.md", 1867),
    "withmarbleapp/os-taxonomy":
        ("os-taxonomy.LICENSE.txt", "main", "LICENSE", 25289),
    "aaryansamanta/nextgen-ai":
        ("nextgen-ai.LICENSE.txt", "main", "LICENSE", 1327),
    "THU-MAIC/OpenMAIC":
        ("OpenMAIC.LICENSE.txt", "main", "LICENSE", 1065),
}


def load(slug):
    with open(os.path.join(FX, FIXTURES[slug][0]), "rb") as fh:
        return fh.read().decode("utf-8")


class TheFixturesAreTheBytesP382Read(unittest.TestCase):
    """🟢 A fixture that has drifted from the payload invalidates every control below."""

    def test_every_fixture_is_the_byte_length_p382_published(self):
        for slug, (name, _ref, _path, nbytes) in FIXTURES.items():
            with open(os.path.join(FX, name), "rb") as fh:
                self.assertEqual(len(fh.read()), nbytes, slug)


class FixtureA_DeclaredSplit(unittest.TestCase):
    SLUG = "oaknational/oak-curriculum-ontology"

    def test_form_is_declared_split(self):
        self.assertEqual(sg.classify(load(self.SLUG))["form"], sg.DECLARED_SPLIT)

    def test_both_grants_are_found(self):
        ids = [g[0].lower() for g in sg.classify(load(self.SLUG))["grants"]]
        self.assertTrue(any("open government" in i for i in ids), ids)
        self.assertTrue(any("mit" in i for i in ids), ids)

    def test_the_data_subtrees_are_ogl_not_mit(self):
        for path in ("ontology", "data", "docs"):
            ok, lic = sg.covers(load(self.SLUG), path)
            self.assertTrue(ok, path)
            self.assertIn("open government", lic.lower(), (path, lic))

    def test_the_code_subtrees_are_mit(self):
        for path in ("scripts", ".github/workflows"):
            ok, lic = sg.covers(load(self.SLUG), path)
            self.assertTrue(ok, path)
            self.assertIn("mit", lic.lower(), (path, lic))

    def test_an_unnamed_subtree_is_UNDEFINED_and_not_false(self):
        """🔵 p381 lost a finding by reading None as False.  None means NOT STATED."""
        ok, _why = sg.covers(load(self.SLUG), "website")
        self.assertIsNone(ok)


class FixtureB_StockScopeLimited(unittest.TestCase):
    SLUG = "withmarbleapp/os-taxonomy"

    def test_form_is_stock_scope_limited(self):
        self.assertEqual(sg.classify(load(self.SLUG))["form"], sg.STOCK_SCOPE_LIMITED)

    def test_the_scope_is_the_database_not_the_contents(self):
        v = sg.classify(load(self.SLUG))
        self.assertEqual(v["grants"][0][1], ("Database",))
        self.assertTrue(v["exclusions"])

    def test_an_unedited_recognised_licence_can_still_be_scope_limited(self):
        """🔴 The finding of this fixture: nothing about the FILE looks unusual."""
        self.assertTrue(sg.classify(load(self.SLUG))["contradicts_root_only"])


class FixtureC_NarrowedOperative(unittest.TestCase):
    SLUG = "aaryansamanta/nextgen-ai"

    def test_form_is_narrowed_operative(self):
        self.assertEqual(sg.classify(load(self.SLUG))["form"], sg.NARROWED_OPERATIVE)

    def test_the_granted_object_is_the_source_code_files_only(self):
        obj = sg.classify(load(self.SLUG))["grants"][0][1][0].lower()
        self.assertIn("source code files", obj)

    def test_the_excluded_paths_are_recovered_from_the_payload(self):
        excl = sg.classify(load(self.SLUG))["exclusions"]
        self.assertTrue(excl)
        flat = [p for e, _ in excl if isinstance(e, tuple) for p in e]
        self.assertIn("website/img", flat)
        self.assertIn("website/video", flat)

    def test_an_excluded_subtree_is_FALSE_not_undefined(self):
        ok, _ = sg.covers(load(self.SLUG), "website/img")
        self.assertIs(ok, False)


class TheInstrumentEarnsItsExistence(unittest.TestCase):
    """🟢 `B-LIMB-2`, registered before this was built: on at least one fixture the
    per-subtree read must CONTRADICT a root-only read, or the instrument is redundant."""

    def test_root_only_read_says_mit_for_nextgen_ai(self):
        self.assertEqual(sg.root_only_verdict(load("aaryansamanta/nextgen-ai")),
                         "MIT License")

    def test_but_the_per_subtree_read_refuses_three_subtrees(self):
        text = load("aaryansamanta/nextgen-ai")
        self.assertIs(sg.covers(text, "website/img")[0], False)

    def test_all_three_fixtures_contradict_the_root_only_read(self):
        for slug in ("oaknational/oak-curriculum-ontology",
                     "withmarbleapp/os-taxonomy",
                     "aaryansamanta/nextgen-ai"):
            self.assertTrue(sg.classify(load(slug))["contradicts_root_only"], slug)


class NegativeControls(unittest.TestCase):
    """🔴 An instrument that flags everything is worthless.  A plain permissive payload
    must come back UNIFORM, and `OpenMAIC` is a p382 first-hand MIT read that folds to
    p378's constant."""

    def test_a_real_unmodified_mit_payload_is_uniform(self):
        v = sg.classify(load("THU-MAIC/OpenMAIC"))
        self.assertEqual(v["form"], sg.UNIFORM)
        self.assertFalse(v["contradicts_root_only"])

    def test_a_uniform_payload_covers_an_arbitrary_subtree(self):
        ok, lic = sg.covers(load("THU-MAIC/OpenMAIC"), "src/anything")
        self.assertTrue(ok)
        self.assertIn("mit", lic.lower())

    def test_empty_payload_does_not_crash_and_is_not_a_grant(self):
        v = sg.classify("")
        self.assertEqual(v["form"], sg.UNIFORM)
        self.assertEqual(v["grants"][0][0], "UNKNOWN")


if __name__ == "__main__":
    unittest.main(verbosity=2)
