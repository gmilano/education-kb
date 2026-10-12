"""Tests for p147-licence-language. Authored fixtures only; nothing is cloned."""
import os
import shutil
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import licence_language as L  # noqa: E402

MIT_BODY = "MIT License\n\nPermission is hereby granted, free of charge, to any person\n"


class Base(unittest.TestCase):
    def setUp(self):
        self.d = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.d, ignore_errors=True)

    def write(self, rel, body):
        p = os.path.join(self.d, rel)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, "w", encoding="utf-8") as fh:
            fh.write(body)

    def base(self):
        return L.census(self.d, "s", L.BASELINE_README, allow_informal=False)

    def ext(self):
        return L.census(self.d, "s", L.EXTENDED_README, allow_informal=True)


class TestThePatternGap(Base):
    def test_portuguese_heading_is_invisible_to_the_baseline(self):
        """🔴 `T63`: `licen[cs]e` cannot match `Licença`."""
        self.write("README.md", "# x\n\n## Licença\n\nEste projeto está licenciado sob a "
                                "licença MIT. Veja o arquivo `LICENSE` para detalhes.\n")
        self.assertEqual(self.base()["grant"], "NONE")
        e = self.ext()
        self.assertEqual((e["grant"], e["licence"]), ("README_ONLY", "MIT"))

    def test_spanish_heading_is_invisible_to_the_baseline(self):
        self.write("README.md", "# Licencia\nUsted es libre de copiar y modificar lo que "
                                "quiera de esta repo.\n")
        self.assertEqual(self.base()["grant"], "NONE")
        e = self.ext()
        self.assertEqual((e["grant"], e["licence"]), ("README_ONLY", "UNIDENTIFIED"))

    def test_an_informal_grant_is_unidentified_and_not_a_licence(self):
        """🔵 A grant whose terms cannot be named is not silence and not a licence."""
        self.write("README.md", "## Licencia\nHaga lo que quiera con esto.\n")
        self.assertEqual(self.ext()["licence"], "UNIDENTIFIED")

    def test_informal_grant_without_any_heading_still_reads(self):
        self.write("README.md", "Notes\n\nYou are free to copy this however you like.\n")
        self.assertEqual(self.base()["grant"], "NONE")
        self.assertEqual(self.ext()["evidence"], "README_INFORMAL")

    def test_german_and_italian_headings(self):
        self.write("README.md", "## Lizenz\nMIT\n")
        self.assertEqual(self.ext()["licence"], "MIT")

    def test_english_heading_reads_identically_on_both(self):
        self.write("README.md", "## License\n\nMIT\n")
        self.assertEqual(self.base()["grant"], self.ext()["grant"])
        self.assertEqual(self.base()["licence"], self.ext()["licence"])


class TestNoFalsePositives(Base):
    def test_prose_about_licensing_is_not_a_grant(self):
        self.write("README.md", "Check that your institution permits this.\n")
        self.assertEqual(self.ext()["grant"], "NONE")

    def test_a_licence_file_still_wins_over_a_readme(self):
        self.write("LICENSE", MIT_BODY)
        self.write("README.md", "## Licença\nAGPL-3.0\n")
        r = self.ext()
        self.assertEqual((r["grant"], r["licence"]), ("FILE", "MIT"))

    def test_package_json_only_is_unchanged_by_the_language_fix(self):
        self.write("package.json", '{"name":"x","license":"MIT"}')
        self.assertEqual(self.base()["grant"], "PKG_ONLY")
        self.assertEqual(self.ext()["grant"], "PKG_ONLY")

    def test_silence_stays_silence(self):
        self.write("src/a.py", "x = 1\n")
        self.assertEqual(self.base()["grant"], "NONE")
        self.assertEqual(self.ext()["grant"], "NONE")


class TestBodyIdentification(Base):
    def test_agpl_body_beats_an_spdx_token_in_the_same_file(self):
        self.write("LICENSE", "GNU AFFERO GENERAL PUBLIC LICENSE\nVersion 3\nMIT\n")
        self.assertEqual(self.ext()["licence"], "AGPL-3.0")

    def test_unidentified_body_is_named_as_such(self):
        self.write("LICENSE", "Do whatever, no warranty.\n")
        self.assertEqual(self.ext()["licence"], "UNIDENTIFIED")

    def test_missing_root_is_no_clone_not_none(self):
        r = L.census(os.path.join(self.d, "absent"), "s", L.EXTENDED_README)
        self.assertEqual(r["grant"], "NO_CLONE")


if __name__ == "__main__":
    unittest.main(verbosity=2)
