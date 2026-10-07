#!/usr/bin/env python3
"""Control tests for git-recency-channel.

The point of this instrument is that its negative result means something, so the
test that matters is the discrimination test: invented slugs must FAIL while real
ones return a date. Network-dependent; skipped when the forge is unreachable.
"""
import unittest

from git_recency import head_date

REAL = "learningequality/kolibri"
FAKE = [
    "this-definitely-does-not-exist-xyz123/nope",
    "openedx/fake-repo-zzz999",
]


class TestDiscrimination(unittest.TestCase):
    def test_real_repo_returns_a_date(self):
        slug, dt, sha, status = head_date(REAL)
        if status != "OK":
            self.skipTest("forge unreachable from this environment")
        self.assertRegex(dt, r"^\d{4}-\d{2}-\d{2}T")
        self.assertTrue(sha)

    def test_invented_slugs_fail(self):
        if head_date(REAL)[3] != "OK":
            self.skipTest("forge unreachable from this environment")
        for slug in FAKE:
            with self.subTest(slug=slug):
                self.assertEqual(head_date(slug)[3], "FAIL")


if __name__ == "__main__":
    unittest.main()
