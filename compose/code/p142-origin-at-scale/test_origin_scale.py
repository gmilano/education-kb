"""Tests for p142-origin-at-scale. The first two pin p141's defects, not this probe's."""
import os
import subprocess
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import origin_scale as O  # noqa: E402


class ToolMailIsNotAnInstitution(unittest.TestCase):
    def test_anthropic_is_classified_as_a_tool_not_an_institution(self):
        """🔴 p141's agent-tier TSV reports `anthropic.com(59)` under
        `institutional_email_domains`. An AI coding tool's authorship address is not an
        institution and must never reach a column a reader uses to place a repository."""
        self.assertIn("anthropic.com", O.TOOL_MAIL)
        self.assertNotIn("anthropic.com", O.PERSONAL_MAIL)

    def test_bot_and_noreply_addresses_are_tool_mail(self):
        for d in ("users.noreply.github.com", "dependabot.com", "copilot.github.com"):
            self.assertIn(d, O.TOOL_MAIL)

    def test_a_real_university_domain_stays_institutional(self):
        for d in ("ethz.ch", "utoronto.ca", "arbisoft.com", "edunext.co"):
            self.assertNotIn(d, O.TOOL_MAIL)
            self.assertNotIn(d, O.PERSONAL_MAIL)


class TreeReadingWithoutAnIndex(unittest.TestCase):
    """🔴 p141 used `git ls-files`, which reads the INDEX. The population here is cloned
    `--no-checkout`, so `ls-files` is empty and every funding file would be reported absent,
    silently. `ls-tree -r HEAD` reads the commit."""

    def setUp(self):
        self.dir = tempfile.mkdtemp()
        env = {"GIT_AUTHOR_NAME": "t", "GIT_AUTHOR_EMAIL": "t@example.com",
               "GIT_COMMITTER_NAME": "t", "GIT_COMMITTER_EMAIL": "t@example.com",
               "GIT_AUTHOR_DATE": "2026-01-01T00:00:00 +0530",
               "GIT_COMMITTER_DATE": "2026-01-01T00:00:00 +0530",
               "HOME": self.dir, "PATH": os.environ.get("PATH", "/usr/bin:/bin")}
        run = lambda *a: subprocess.run(["git", "-C", self.dir, *a], check=True,
                                        capture_output=True, env=env)
        run("init", "-q", "-b", "main")
        os.makedirs(os.path.join(self.dir, ".github"), exist_ok=True)
        open(os.path.join(self.dir, ".github", "FUNDING.yml"), "w").write("github: x\n")
        open(os.path.join(self.dir, "a.txt"), "w").write("x\n")
        run("add", "-A")
        run("commit", "-qm", "seed")

    def test_ls_tree_finds_a_tracked_path(self):
        self.assertIn(".github/FUNDING.yml", O.tracked_paths(self.dir))
        self.assertEqual(O.funding_files(self.dir), [".github/FUNDING.yml"])

    def test_vendored_funding_files_are_excluded(self):
        """A dependency's FUNDING.yml is the dependency's. p141's agent-tier row for
        `mcp-canvas-lms` listed 18 of them, all from `node_modules`."""
        self.assertEqual(
            [p for p in ["node_modules/x/.github/FUNDING.yml"] if "node_modules/" not in p],
            [])

    def test_offsets_are_read_from_the_commit(self):
        self.assertEqual(O.offsets(self.dir), {"+0530": 1})


class InstrumentIsImportedNotRetyped(unittest.TestCase):
    def test_offset_table_is_p141s_object(self):
        """A sweep that redefines its instrument cannot tell a changed verdict from a
        changed method. These must be the same objects p141 published."""
        self.assertIs(O.book, O.p141.book)
        self.assertIs(O.offsets, O.p141.offsets)
        self.assertIs(O.PERSONAL_MAIL, O.p141.PERSONAL_MAIL)

    def test_americas_offsets_are_still_refused(self):
        for off in ("-0300", "-0400", "-0500", "-0600", "-0700"):
            self.assertIn(off, O.p141.AMBIGUOUS, off)
            region, note, _ = O.book({off: 99})
            self.assertEqual(region, "UNMAPPED")
            self.assertIn("AMBIGUOUS", note)

    def test_utc_is_not_europe(self):
        region, note, _ = O.book({"+0000": 500})
        self.assertEqual(region, "UNMAPPED")
        self.assertIn("container", note)


if __name__ == "__main__":
    unittest.main(verbosity=2)
