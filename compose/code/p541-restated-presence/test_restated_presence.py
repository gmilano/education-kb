"""p541's controls.

Every control is a shape this base has actually published.  The five marked
CLASS 1-5 are the false-positive and false-negative classes this instrument's
own draft had before it was committed; they are recorded as controls rather
than tidied away, so a successor cannot re-widen the predicate without a red
suite.

🔵 No network, and no dependence on this repository's real contents: each
control builds its own corpus in a temp dir, because the predicate is about the
RELATION between a candidate and a corpus and nothing else.  The real rows
quoted are the ones read first-hand at p540 and p541.
"""

import os
import subprocess
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import restated_presence as rp  # noqa: E402

# Real text, as committed at p540.
ROW_MOODLE_MCP = ("| 🔴 🆕 **`p538`** — [loyaniu/moodle-mcp](https://github.com/loyaniu/moodle-mcp) "
                  "| 🔴 **52** · 14 forks | Nothing. No licence entry in the sidebar. |")
PROSE_OPENWEBUI = ("> the [`open-webui/open-webui`](https://github.com/open-webui/open-webui) "
                   "branding clause, known since `p441`, is not a permissive grant")
HIST_CLAWED = ("- 🆕 [`SirhanMacx/Claw-ED`](https://github.com/SirhanMacx/Claw-ED) — "
               "local-first AI teaching assistant, read at p490")


def write(root, rel, text):
    full = os.path.join(root, rel)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as fh:
        fh.write(text)


class Corpus:
    """A temp repo with the nine pages, optionally committed to a git ref."""

    def __init__(self, curated=None, history=None, archive=None, commit=False):
        self.dir = tempfile.mkdtemp()
        for rel in rp.CURATED:
            write(self.dir, rel, (curated or {}).get(rel, "# page\n"))
        for rel in rp.HISTORY:
            write(self.dir, rel, (history or {}).get(rel, "# page\n"))
        for rel, text in (archive or {}).items():
            write(self.dir, rel, text)
        self.ref = None
        if commit:
            env = dict(os.environ, GIT_AUTHOR_NAME="t", GIT_AUTHOR_EMAIL="t@t",
                       GIT_COMMITTER_NAME="t", GIT_COMMITTER_EMAIL="t@t")
            for cmd in (["init", "-q"], ["add", "-A"], ["commit", "-qm", "c"]):
                subprocess.run(["git", "-C", self.dir] + cmd, check=True, env=env,
                               capture_output=True)
            self.ref = "HEAD"

    def index(self):
        return rp.index_corpus(self.dir, ref=self.ref)

    def outside(self):
        return rp.outside_scan(self.dir, ref=self.ref, self_dir=os.path.join(self.dir, "__none__"))

    def cleanup(self):
        import shutil
        shutil.rmtree(self.dir, ignore_errors=True)


class TestRoleGrading(unittest.TestCase):
    """The four roles, each on text the base really published."""

    def grade_one(self, cand, **kw):
        c = Corpus(**kw)
        try:
            ak, bk = c.outside()
            rows = rp.grade([cand], c.index(), {}, ak, bk)
            return rows[0]
        finally:
            c.cleanup()

    def test_filed_is_red(self):
        r = self.grade_one("loyaniu/moodle-mcp",
                           curated={"agents/top.md": ROW_MOODLE_MCP})
        self.assertEqual(r["verdict"], "FILED")
        self.assertFalse(r["ok"])

    def test_prose_is_red(self):
        """p540's own miss: four of its five candidates were this role."""
        r = self.grade_one("open-webui/open-webui",
                           curated={"intel/market.md": PROSE_OPENWEBUI})
        self.assertEqual(r["verdict"], "PROSE")
        self.assertFalse(r["ok"])

    def test_history_only_is_amber_and_passes(self):
        """529-A's debt class.  Owned but unfiled is a PROMOTION, not a
        restatement, so it must not fail the gate."""
        r = self.grade_one("SirhanMacx/Claw-ED",
                           history={"agents/trending.md": HIST_CLAWED})
        self.assertEqual(r["verdict"], "HISTORY")
        self.assertTrue(r["ok"])

    def test_absent_is_new(self):
        r = self.grade_one("UFPA-LAMIC/EduAcess")
        self.assertEqual(r["verdict"], "ABSENT")
        self.assertTrue(r["ok"])


class TestFalsePositiveClasses(unittest.TestCase):

    def test_class1_bare_repo_name_is_not_an_address(self):
        """CLASS 1 — the hand `grep -rl Claw-ED .` this gate replaces matched a
        bare repo name, which collides across owners.  `moodle-mcp` is
        published by at least three owners on this base and `moodler-mcp` is a
        FORK of a different one (p538).  A bare name is refused, not guessed."""
        self.assertIsNone(rp.parse_candidate("moodle-mcp"))
        self.assertIsNone(rp.parse_candidate("Claw-ED"))
        c = Corpus(curated={"agents/top.md": ROW_MOODLE_MCP})
        try:
            idx = c.index()
            # The committed row is loyaniu's.  A DIFFERENT owner's same-named
            # repo must not inherit its presence.
            self.assertEqual(rp.classify("tosuki/moodle-mcp", idx), "ABSENT")
            self.assertEqual(rp.classify("loyaniu/moodle-mcp", idx), "FILED")
        finally:
            c.cleanup()

    def test_class2_case_folds_in_the_key_only(self):
        """CLASS 2 — GitHub redirects on case, so `aied-innovations/...` and
        `AIEd-Innovations/...` are one repository (p537).  The key folds; the
        payload keeps the spelling the corpus wrote."""
        c = Corpus(curated={"agents/top.md":
                            "| [x](https://github.com/AIEd-Innovations/assessment_agent) |"})
        try:
            ak, bk = c.outside()
            rows = rp.grade(["aied-innovations/assessment_agent"], c.index(), {}, ak, bk)
            self.assertEqual(rows[0]["verdict"], "FILED")
            self.assertEqual(rows[0]["address"], "aied-innovations/assessment_agent")
            self.assertEqual(rows[0]["match_key"], "aied-innovations/assessment_agent")
            # And the key never carries upper case, whichever way it was written.
            self.assertEqual(rp.parse_candidate("AIEd-Innovations/Assessment_Agent")[1],
                             "aied-innovations/assessment_agent")
            self.assertEqual(rp.parse_candidate("AIEd-Innovations/Assessment_Agent")[0],
                             "AIEd-Innovations/Assessment_Agent")
        finally:
            c.cleanup()

    def test_class3_archive_only_is_a_recovery_not_a_restatement(self):
        """CLASS 3 — the one this author got wrong first.  Twenty of the
        thirty-one paths a hand grep returned for `Claw-ED` were under
        `archive/`.  An address surviving only there is on a page the base
        DELETED; p495 calls failing to recover it a LOSS.  Green, not red."""
        c = Corpus(archive={"archive/2026-10-06-pre-reset/agents-top.md": HIST_CLAWED})
        try:
            ak, bk = c.outside()
            rows = rp.grade(["SirhanMacx/Claw-ED"], c.index(), {}, ak, bk)
            self.assertEqual(rows[0]["verdict"], "ARCHIVE")
            self.assertTrue(rows[0]["ok"])
        finally:
            c.cleanup()

    def test_class4_markdown_link_and_bare_url_both_count(self):
        """CLASS 4 — an address reaches a page in at least three spellings:
        a markdown link, a bare URL, and a backticked slug inside a link."""
        for text in ("see https://github.com/portabilis/i-educar for the SIS",
                     "[`portabilis/i-educar`](https://github.com/portabilis/i-educar)",
                     "| a | https://github.com/portabilis/i-educar | b |"):
            c = Corpus(curated={"verticals/solutions.md": text})
            try:
                self.assertIn(rp.classify("portabilis/i-educar", c.index()),
                              ("FILED", "PROSE"))
            finally:
                c.cleanup()

    def test_class6_a_suites_own_fixtures_are_not_corpus(self):
        """CLASS 6 — found by this gate failing on its own author.

        p541's first run graded `UFPA-LAMIC/EduAcess` as already-held on the
        strength of a single occurrence: the fixture in THIS file.  An
        instrument that walks `compose/code/` reads its own test data as
        corpus, and the suites on this base quote real rows on purpose (p392),
        so every address a suite cites would become a false presence.  A
        `test_*.py` file is not a finding."""
        c = Corpus()
        try:
            write(c.dir, "compose/code/p541-x/test_fixtures.py",
                  "ROW = 'https://github.com/UFPA-LAMIC/EduAcess'")
            write(c.dir, "compose/code/p541-x/real_census.py",
                  "# measured: https://github.com/cjescudero/asistente-docente")
            ak, bk = rp.outside_scan(c.dir, self_dir=os.path.join(c.dir, "__none__"))
            self.assertNotIn("ufpa-lamic/educacess", ak | bk)
            # ...while a NON-test file in the same directory still counts.
            self.assertIn("cjescudero/asistente-docente", bk)
        finally:
            c.cleanup()

    def test_class6b_the_instruments_own_directory_is_not_corpus(self):
        """The same defect by the other route: this instrument's own module and
        docstring name the addresses it was built to grade."""
        c = Corpus()
        try:
            own = os.path.join(c.dir, "compose/code/p541-restated-presence")
            write(c.dir, "compose/code/p541-restated-presence/restated_presence.py",
                  "# p540 held https://github.com/open-webui/open-webui")
            ak, bk = rp.outside_scan(c.dir, self_dir=own)
            self.assertNotIn("open-webui/open-webui", ak | bk)
        finally:
            c.cleanup()

    def test_archive_and_backlog_are_different_instructions(self):
        """A deleted page says RECOVER; an evidence row says PROMOTE.  p541's
        first run returned one verdict for both and could not tell a successor
        which to do."""
        c = Corpus()
        try:
            write(c.dir, "archive/2026-10-27-p490-pre-rewrite/top.md",
                  "| [x](https://github.com/jesusgarciafernandez/Aula-y-Comunidad-Educativa-Aumentada) |")
            write(c.dir, "evidence/verified-repos.2026-10-23-p396.tsv",
                  "github.com/cjescudero/asistente-docente\tLIVE\n")
            ak, bk = rp.outside_scan(c.dir, self_dir=os.path.join(c.dir, "__none__"))
            idx = c.index()
            self.assertEqual(
                rp.classify("jesusgarciafernandez/aula-y-comunidad-educativa-aumentada",
                            idx, ak, bk), "ARCHIVE")
            self.assertEqual(
                rp.classify("cjescudero/asistente-docente", idx, ak, bk), "BACKLOG")
        finally:
            c.cleanup()

    def test_an_address_on_a_deleted_page_and_in_evidence_is_a_recovery_first(self):
        """Both arms hit: the deleted page wins, because it was once judged
        good enough to shelve and the evidence row never was."""
        c = Corpus()
        try:
            write(c.dir, "archive/old/top.md", "https://github.com/a/b")
            write(c.dir, "evidence/x.tsv", "github.com/a/b")
            ak, bk = rp.outside_scan(c.dir, self_dir=os.path.join(c.dir, "__none__"))
            self.assertIn("a/b", ak)
            self.assertNotIn("a/b", bk)
            self.assertEqual(rp.classify("a/b", c.index(), ak, bk), "ARCHIVE")
        finally:
            c.cleanup()

    def test_class5_worktree_self_match_is_why_the_ref_is_read(self):
        """CLASS 5 — the failure that would have made this gate useless.

        A pass writes its new row, then runs the gate.  Against the WORKING
        tree the pass's own row is a presence, so every genuinely new address
        grades FILED and the gate is red exactly when the work is good.
        Against the committed ref the same candidate is ABSENT."""
        c = Corpus(curated={"agents/top.md": "# page\n"}, commit=True)
        try:
            # The pass now writes its new finding to the working tree.
            write(c.dir, "agents/top.md",
                  "| [x](https://github.com/UFPA-LAMIC/EduAcess) | MIT |\n")
            worktree = rp.index_corpus(c.dir, ref=None)
            committed = rp.index_corpus(c.dir, ref="HEAD")
            self.assertEqual(rp.classify("ufpa-lamic/educaess", worktree), "ABSENT")
            self.assertEqual(rp.classify("ufpa-lamic/educacess", worktree), "ABSENT")
            key = rp.parse_candidate("UFPA-LAMIC/EduAcess")[1]
            self.assertEqual(rp.classify(key, worktree), "FILED")   # the trap
            self.assertEqual(rp.classify(key, committed), "ABSENT")  # the fix
        finally:
            c.cleanup()


class TestTableRowPredicate(unittest.TestCase):

    def test_leading_pipe_is_a_row_and_an_inline_pipe_is_not(self):
        """p277's axis, reused rather than re-derived."""
        self.assertTrue(rp.is_table_row("| a | b |"))
        self.assertTrue(rp.is_table_row("   | indented row |"))
        self.assertFalse(rp.is_table_row("the grant is MIT | Apache-2.0 dual"))
        self.assertFalse(rp.is_table_row("> quoted prose about github.com/a/b"))


class TestRegistrations(unittest.TestCase):

    def reg(self, text):
        fd, path = tempfile.mkstemp()
        os.close(fd)
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(text)
        try:
            return rp.read_registrations(path)
        finally:
            os.unlink(path)

    def test_a_registered_restatement_passes_the_gate(self):
        by_key, problems = self.reg(
            "loyaniu/moodle-mcp\tcarried deliberately as the ungranted leader of "
            "the Moodle census; re-read this pass to confirm no licence appeared\n")
        self.assertEqual(problems, [])
        c = Corpus(curated={"agents/top.md": ROW_MOODLE_MCP})
        try:
            ak, bk = c.outside()
            rows = rp.grade(["loyaniu/moodle-mcp"], c.index(), by_key, ak, bk)
            self.assertEqual(rows[0]["verdict"], "FILED")
            self.assertTrue(rows[0]["ok"])
            self.assertIn("ungranted leader", rows[0]["registered"])
        finally:
            c.cleanup()

    def test_a_placeholder_reason_does_not_register(self):
        """Otherwise the gate is cleared by typing a hyphen."""
        for bad in ("-", "TODO", "n/a", "dup", "known", "?"):
            by_key, problems = self.reg(f"a/b\t{bad}\n")
            self.assertEqual(by_key, {}, bad)
            self.assertEqual(len(problems), 1, bad)

    def test_a_short_reason_does_not_register(self):
        by_key, problems = self.reg("a/b\talready there\n")
        self.assertEqual(by_key, {})
        self.assertTrue(any("minimum" in p for p in problems))

    def test_a_header_row_is_not_a_registration(self):
        """p277's lesson at this file's width: `address<TAB>reason` is a header,
        and this base has compiled a header row into an entity before."""
        by_key, problems = self.reg("address\treason\nloyaniu/moodle-mcp\t"
                                    "carried deliberately, see the Moodle census above\n")
        self.assertEqual(problems, [])
        self.assertEqual(list(by_key), ["loyaniu/moodle-mcp"])

    def test_a_missing_file_is_no_registrations_and_no_error(self):
        by_key, problems = rp.read_registrations("/nonexistent/restatements.tsv")
        self.assertEqual((by_key, problems), ({}, []))


class TestFatalArm(unittest.TestCase):
    """The gate must FAIL, with a nonzero exit, on the shape it exists for."""

    def test_cli_exits_nonzero_on_an_unregistered_filed_candidate(self):
        c = Corpus(curated={"agents/top.md": ROW_MOODLE_MCP}, commit=True)
        try:
            rc = subprocess.run(
                [sys.executable, "-I",
                 os.path.join(os.path.dirname(os.path.abspath(__file__)),
                              "restated_presence.py"),
                 "loyaniu/moodle-mcp", "--root", c.dir, "--ref", "HEAD",
                 "--registrations", "/nonexistent"],
                capture_output=True)
            self.assertEqual(rc.returncode, 1, rc.stderr.decode())
            self.assertIn(b"unregistered restatement", rc.stderr)
        finally:
            c.cleanup()

    def test_cli_exits_zero_on_a_genuinely_new_candidate(self):
        c = Corpus(curated={"agents/top.md": ROW_MOODLE_MCP}, commit=True)
        try:
            rc = subprocess.run(
                [sys.executable, "-I",
                 os.path.join(os.path.dirname(os.path.abspath(__file__)),
                              "restated_presence.py"),
                 "UFPA-LAMIC/EduAcess", "--root", c.dir, "--ref", "HEAD",
                 "--registrations", "/nonexistent"],
                capture_output=True)
            self.assertEqual(rc.returncode, 0, rc.stderr.decode())
            self.assertIn(b"ABSENT", rc.stdout)
        finally:
            c.cleanup()

    def test_an_empty_index_is_a_configuration_error_not_a_pass(self):
        """A wrong --root would otherwise grade every candidate ABSENT and the
        gate would be green because it read nothing.  p300's no-masking rule."""
        empty = tempfile.mkdtemp()
        try:
            rc = subprocess.run(
                [sys.executable, "-I",
                 os.path.join(os.path.dirname(os.path.abspath(__file__)),
                              "restated_presence.py"),
                 "a/b", "--root", empty, "--ref", "WORKTREE"],
                capture_output=True)
            self.assertEqual(rc.returncode, 2, rc.stderr.decode())
            self.assertIn(b"no addresses indexed", rc.stderr)
        finally:
            import shutil
            shutil.rmtree(empty, ignore_errors=True)


if __name__ == "__main__":
    unittest.main(verbosity=2)
