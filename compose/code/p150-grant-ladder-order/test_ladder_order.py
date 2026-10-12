"""Tests for p150-grant-ladder-order. Authored fixtures, offline.

`ACTION FE`. The ladder is `FILE > PKG_ONLY > README_ONLY`, which is what `p145`'s
docstring documents ("README_ONLY … weaker still"). 🔴 `p147-licence-language` inverted
the last two rungs silently, demoting a declared manifest licence to a prose mention.

🔵 The tests below pin the ORDER, not the matchers: each fixture is a tree carrying a
known combination of the three surfaces, and the assertion is which rung wins.
"""
import json
import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ladder_order as L  # noqa: E402

MIT_BODY = ("MIT License\n\nCopyright (c) 2026 Someone\n\n"
            "Permission is hereby granted, free of charge, to any person obtaining a "
            "copy of this software\n")


def tree(licence_file=None, pkg_licence=None, readme=None, pyproject=None):
    """A tree carrying any combination of the three grant surfaces."""
    d = tempfile.mkdtemp()
    if licence_file is not None:
        with open(os.path.join(d, "LICENSE"), "w", encoding="utf-8") as fh:
            fh.write(licence_file)
    if pkg_licence is not None:
        with open(os.path.join(d, "package.json"), "w", encoding="utf-8") as fh:
            json.dump({"name": "x", "version": "1.0.0", "license": pkg_licence}, fh)
    if readme is not None:
        with open(os.path.join(d, "README.md"), "w", encoding="utf-8") as fh:
            fh.write(readme)
    if pyproject is not None:
        with open(os.path.join(d, "pyproject.toml"), "w", encoding="utf-8") as fh:
            fh.write(pyproject)
    return d


def grant(d):
    return L.census(d, "fixture", L.EXTENDED_README, allow_informal=True)["grant"]


def grant_p147(d):
    return L.census_p147_order(d, "fixture", L.EXTENDED_README,
                               allow_informal=True)["grant"]


class FileWinsOverEverything(unittest.TestCase):
    """🟢 Invariant to the swap: `FILE` returns before either branch is reached."""

    def test_file_beats_pkg_and_readme(self):
        d = tree(licence_file=MIT_BODY, pkg_licence="Apache-2.0",
                 readme="## License\nMIT\n")
        self.assertEqual(grant(d), "FILE")
        self.assertEqual(grant_p147(d), "FILE")

    def test_file_alone(self):
        d = tree(licence_file=MIT_BODY)
        self.assertEqual(grant(d), grant_p147(d))
        self.assertEqual(grant(d), "FILE")

    def test_the_two_arms_agree_on_every_file_row(self):
        for pkg in (None, "MIT", "AGPL-3.0"):
            for rm in (None, "## License\nMIT\n", "## Licença\nMIT\n"):
                d = tree(licence_file=MIT_BODY, pkg_licence=pkg, readme=rm)
                self.assertEqual(grant(d), "FILE")
                self.assertEqual(grant_p147(d), "FILE")


class TheRungThatMoves(unittest.TestCase):
    """🔴 The only shape where the inversion is visible: pkg AND readme, no file."""

    def setUp(self):
        self.d = tree(pkg_licence="MIT", readme="## License\nMIT, see LICENSE\n")

    def test_corrected_order_prefers_the_manifest(self):
        self.assertEqual(grant(self.d), "PKG_ONLY")

    def test_p147_order_demoted_it_to_prose(self):
        self.assertEqual(grant_p147(self.d), "README_ONLY")

    def test_the_two_arms_disagree_on_exactly_this_shape(self):
        self.assertNotEqual(grant(self.d), grant_p147(self.d))

    def test_the_direction_is_weakening(self):
        # PKG_ONLY is a declared grant in a machine-read field; README_ONLY is prose.
        self.assertEqual((grant(self.d), grant_p147(self.d)),
                         ("PKG_ONLY", "README_ONLY"))


class RungsInIsolationAreUnaffected(unittest.TestCase):
    def test_pkg_only(self):
        d = tree(pkg_licence="MIT")
        self.assertEqual(grant(d), "PKG_ONLY")
        self.assertEqual(grant_p147(d), "PKG_ONLY")

    def test_readme_only(self):
        d = tree(readme="## License\nMIT\n")
        self.assertEqual(grant(d), "README_ONLY")
        self.assertEqual(grant_p147(d), "README_ONLY")

    def test_neither(self):
        d = tree()
        self.assertEqual(grant(d), "NONE")
        self.assertEqual(grant_p147(d), "NONE")

    def test_pyproject_counts_as_a_manifest(self):
        d = tree(pyproject='[project]\nname = "x"\nlicense = "MIT"\n',
                 readme="## License\nMIT\n")
        self.assertEqual(grant(d), "PKG_ONLY")
        self.assertEqual(grant_p147(d), "README_ONLY")


class RomanceHeadingsStillReach(unittest.TestCase):
    """🟢 `T63`'s repair must survive the reorder — it is a matcher, not a rung."""

    def test_portuguese_heading_without_a_manifest(self):
        d = tree(readme="## Licença\nlicenciado sob a licença MIT\n")
        self.assertEqual(grant(d), "README_ONLY")

    def test_spanish_heading_without_a_manifest(self):
        d = tree(readme="# Licencia\nUsted es libre de copiar y modificar\n")
        self.assertEqual(grant(d), "README_ONLY")

    def test_portuguese_heading_WITH_a_manifest_now_prefers_the_manifest(self):
        # 🔵 The shape that would have moved a LATAM row, had one carried both.
        d = tree(pkg_licence="MIT", readme="## Licença\nlicenciado sob a licença MIT\n")
        self.assertEqual(grant(d), "PKG_ONLY")
        self.assertEqual(grant_p147(d), "README_ONLY")


class OrderIsDeclared(unittest.TestCase):
    def test_module_names_its_ladder(self):
        self.assertEqual(L.ORDER, ("FILE", "PKG_ONLY", "README_ONLY"))

    def test_no_clone_is_not_a_crash(self):
        self.assertEqual(
            L.census("/nonexistent/xyz", "f", L.EXTENDED_README)["grant"], "NO_CLONE")
        self.assertEqual(
            L.census_p147_order("/nonexistent/xyz", "f", L.EXTENDED_README)["grant"],
            "NO_CLONE")

    def test_empty_tree_is_none_not_a_crash(self):
        self.assertEqual(grant(tempfile.mkdtemp()), "NONE")


if __name__ == "__main__":
    unittest.main(verbosity=2)
