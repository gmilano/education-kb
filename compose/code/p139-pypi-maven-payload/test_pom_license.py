#!/usr/bin/env python3
"""Tests for `pom_license`. Run: python3 -I test_pom_license.py

The first three fixtures are the regression that caused `pom_license.py` to exist: the
`sed` version of this read returned a DEVELOPER's name as the licence for all three
coordinates probed this pass.
"""
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import pom_license as pl  # noqa: E402

# Shape of edu.ksu.ome.lti:lti-launch — a licence, then a developer whose <name> the
# greedy regex reached. Trimmed, with the element order of the real POM preserved.
LTI_LAUNCH = """<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0">
  <groupId>edu.ksu.ome.lti</groupId>
  <artifactId>lti-launch</artifactId>
  <version>1.4.7</version>
  <name>LTI Launch</name>
  <licenses>
    <license>
      <name>GNU Lesser General Public License (LGPL), Version 3</name>
      <url>http://www.fsf.org/licensing/licenses/lgpl.txt</url>
    </license>
  </licenses>
  <developers>
    <developer>
      <name>Toby Murray</name>
    </developer>
  </developers>
</project>
"""

# A POM with no <licenses> at all, but with developers -- the case where the regex
# version invented a licence out of nothing.
NO_LICENCE = """<project xmlns="http://maven.apache.org/POM/4.0.0">
  <artifactId>a</artifactId>
  <developers><developer><name>Sakai Core Team</name></developer></developers>
</project>
"""

NO_NAMESPACE = """<project>
  <licenses><license><name>Apache-2.0</name><url>https://apache.org/</url></license></licenses>
</project>
"""

TWO_LICENCES = """<project xmlns="http://maven.apache.org/POM/4.0.0">
  <licenses>
    <license><name>EPL-2.0</name><url>https://e/</url></license>
    <license><name>GPL-2.0-with-classpath-exception</name><url>https://g/</url></license>
  </licenses>
</project>
"""

# <licenses> inside a profile is not the artefact's own grant.
LICENCE_IN_PROFILE = """<project xmlns="http://maven.apache.org/POM/4.0.0">
  <profiles><profile><licenses><license><name>MIT</name></license></licenses></profile></profiles>
</project>
"""


def write(text):
    f = tempfile.NamedTemporaryFile("w", suffix=".pom", delete=False)
    f.write(text)
    f.close()
    return f.name


class TestDeclaredLicences(unittest.TestCase):
    def test_developer_name_is_not_a_licence(self):
        """The regression. `sed` returned `Toby Murray` here."""
        got = pl.declared_licences(write(LTI_LAUNCH))
        self.assertEqual(len(got), 1)
        self.assertEqual(got[0][0], "GNU Lesser General Public License (LGPL), Version 3")
        self.assertNotIn("Toby Murray", [n for n, _ in got])

    def test_no_licences_element_means_none_declared(self):
        self.assertEqual(pl.declared_licences(write(NO_LICENCE)), [])

    def test_namespace_optional(self):
        got = pl.declared_licences(write(NO_NAMESPACE))
        self.assertEqual(got, [("Apache-2.0", "https://apache.org/")])

    def test_dual_licensing_returns_both(self):
        got = pl.declared_licences(write(TWO_LICENCES))
        self.assertEqual([n for n, _ in got], ["EPL-2.0", "GPL-2.0-with-classpath-exception"])

    def test_licence_inside_a_profile_is_not_the_artefacts_grant(self):
        self.assertEqual(pl.declared_licences(write(LICENCE_IN_PROFILE)), [])

    def test_unparseable_pom_is_reported_not_crashed(self):
        got = pl.declared_licences(write("<project><unclosed>"))
        self.assertEqual(got[0][0], "PARSE_ERROR")

    def test_missing_file_is_reported_not_crashed(self):
        got = pl.declared_licences("/nonexistent/path/to.pom")
        self.assertEqual(got[0][0], "PARSE_ERROR")


if __name__ == "__main__":
    unittest.main(verbosity=2)
