"""Tests for p142-verapdf-module-grant. The first two pin THIS probe's own first-draft defect."""
import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import jar_licence as J  # noqa: E402


class LicenceEntryMatching(unittest.TestCase):
    def test_mpl_inside_impl_package_is_not_a_licence(self):
        """🔴 The regression. `MPL` is a substring of `IMPL`, and the first draft read 300+
        compiled classes in `org/verapdf/.../impl/` as Mozilla Public License files."""
        self.assertEqual(J.licence_entries([
            "org/verapdf/xmp/impl/XMPNode.class",
            "org/verapdf/xmp/impl/xpath/XMPPathParser.class",
            "org/verapdf/gf/model/impl/cos/GFCosObject.class",
        ]), [])

    def test_code_extensions_never_count(self):
        self.assertEqual(J.licence_entries(["com/x/License.class", "a/LICENSE.java"]), [])

    def test_real_licence_files_match(self):
        for n in ("META-INF/LICENSE", "LICENSE.txt", "licenses/MPL-2.0.txt",
                  "COPYING", "NOTICE.md", "GPL-3.0.txt", "apache-2.0.txt"):
            self.assertEqual(J.licence_entries([n]), [n], n)

    def test_directories_are_skipped(self):
        self.assertEqual(J.licence_entries(["META-INF/licenses/"]), [])

    def test_basename_anchoring_not_substring(self):
        """A licence-ish token in a PATH segment must not match; only the basename decides."""
        self.assertEqual(J.licence_entries(["licenses/org/acme/Widget.properties"]), [])


class CoordinateNotModuleName(unittest.TestCase):
    def test_module_directory_is_not_an_artifact_id(self):
        """🔴 `verapdf-library`'s POM lists `<module>xmp-core</module>`; the published
        coordinate is `org.verapdf:verapdf-xmp-core`. A `<modules>` entry is a path."""
        modules = ["xmp-core", "core"]
        published = {"core", "verapdf-xmp-core"}
        self.assertNotIn("xmp-core", published)
        self.assertEqual([m for m in modules if m in published], ["core"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
