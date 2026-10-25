"""Offline controls for `p435-promotion-sweep/recency.py`.

No network.  Every control is a fixture, so the suite is admissible in `make hooks`
while the sweeps themselves (`sweep.sh`, `head_dates.sh`) stay online and out of it.
"""
import datetime
import os
import subprocess
import sys
import tempfile
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import recency                                            # noqa: E402

TODAY = datetime.date(2026, 10, 25)
HDR = ("slug\tfamily\tref\tpath\tbytes\tsha12\thead\thead_committed\t"
       "tz_offset\tfamily_channel\trecency_channel\n")


def row(slug, fam, hd, off="+00:00"):
    return (f"{slug}\t{fam}\t{'main'}\tLICENSE\t1067\tdeadbeefcafe\tfeedfacefeed\t"
            f"{hd}\t{off}\traw.githubusercontent.com\tgit-clone-depth1-bare-filter-tree0\n")


def table(*rows):
    fh = tempfile.NamedTemporaryFile("w", suffix=".tsv", delete=False, encoding="utf-8")
    fh.write(HDR)
    for r in rows:
        fh.write(r)
    fh.close()
    return fh.name


class Window(unittest.TestCase):
    def test_C1_fresh_permissive_is_a_slate_row(self):
        rows = recency.read_grades(table(row("o/fresh", "MIT", "2026-10-20")))
        slate, _ = recency.classify(rows, TODAY)
        self.assertEqual([r[0] for r in slate], ["o/fresh"])

    def test_C2_stale_permissive_is_not_a_slate_row(self):
        rows = recency.read_grades(table(row("o/stale", "MIT", "2019-07-18")))
        slate, rej = recency.classify(rows, TODAY)
        self.assertEqual(slate, [])
        self.assertEqual(rej[0][3], "STALE->2y")

    def test_C3_the_window_edge_is_inclusive(self):
        edge = (TODAY - datetime.timedelta(days=30)).isoformat()
        over = (TODAY - datetime.timedelta(days=31)).isoformat()
        rows = recency.read_grades(table(row("o/edge", "MIT", edge),
                                         row("o/over", "MIT", over)))
        slate, _ = recency.classify(rows, TODAY)
        self.assertEqual([r[0] for r in slate], ["o/edge"])

    def test_C4_fresh_but_copyleft_is_rejected_on_the_LICENCE(self):
        """The error direction that would put unusable supply in a deliverable."""
        rows = recency.read_grades(table(row("o/agpl", "AGPL-3.0", "2026-10-25")))
        slate, rej = recency.classify(rows, TODAY)
        self.assertEqual(slate, [])
        self.assertEqual(rej[0][3], "NOT-PERMISSIVE")

    def test_C5_fresh_but_NO_GRANT_is_rejected(self):
        rows = recency.read_grades(table(row("o/none", "NO-GRANT", "2026-10-25")))
        slate, _ = recency.classify(rows, TODAY)
        self.assertEqual(slate, [])

    def test_C6_CC_BY_SA_is_not_permissive(self):
        """`p434`'s load-bearing negative, carried: 4 771 stars did not make it usable."""
        rows = recency.read_grades(table(row("o/cc", "CC-BY-SA-4.0", "2026-10-25")))
        slate, _ = recency.classify(rows, TODAY)
        self.assertEqual(slate, [])


class ReachBound(unittest.TestCase):
    def test_C7_an_undated_permissive_row_is_a_reach_bound_not_a_finding(self):
        rows = recency.read_grades(table(row("o/undated", "MIT", "-")))
        slate, rej = recency.classify(rows, TODAY)
        self.assertEqual(slate, [])
        self.assertEqual(rej[0][3], "NO-DATE")

    def test_C8_an_empty_date_cell_is_also_NO_DATE_not_a_crash(self):
        rows = recency.read_grades(table(row("o/blank", "MIT", "")))
        slate, rej = recency.classify(rows, TODAY)
        self.assertEqual(slate, [])
        self.assertEqual(rej[0][3], "NO-DATE")


class Refutation(unittest.TestCase):
    """The measured reason this predicate is not `p434`'s predicate."""

    def test_C9_permissiveness_alone_selects_the_MAJORITY_of_this_population(self):
        """59.1 % measured over 2 450 addresses, so it classifies rather than detects."""
        rows = recency.read_grades(table(
            *[row(f"o/p{i}", "MIT", "2019-01-01") for i in range(59)],
            *[row(f"o/c{i}", "AGPL-3.0", "2019-01-01") for i in range(41)]))
        permissive = [r for r in rows if r["family"] in recency.PERMISSIVE]
        self.assertEqual(len(permissive), 59)
        slate, _ = recency.classify(rows, TODAY)
        self.assertEqual(slate, [], "and recency cuts all 59, because none is live")

    def test_C10_recency_is_orthogonal_to_the_licence_axis(self):
        rows = recency.read_grades(table(
            row("o/fresh-mit", "MIT", "2026-10-24"),
            row("o/fresh-agpl", "AGPL-3.0", "2026-10-24"),
            row("o/stale-mit", "MIT", "2020-01-01"),
            row("o/stale-agpl", "AGPL-3.0", "2020-01-01")))
        slate, _ = recency.classify(rows, TODAY)
        self.assertEqual([r[0] for r in slate], ["o/fresh-mit"])

    def test_C11_no_star_column_is_read_even_when_one_is_present(self):
        """`Gap 434-B`: a star count is advisory colour, never a predicate."""
        name = table(row("o/x", "MIT", "2026-10-24"))
        with open(name, encoding="utf-8") as fh:
            self.assertNotIn("stars", fh.readline())
        rows = recency.read_grades(name)
        slate, _ = recency.classify(rows, TODAY)
        self.assertEqual(len(slate), 1)


class Provenance(unittest.TestCase):
    def test_C12_the_offset_channel_survives_into_the_slate(self):
        """So `gate-offset-region` can place a slate row without a second probe."""
        rows = recency.read_grades(table(row("o/pl", "MIT", "2026-10-25", "+01:00")))
        slate, _ = recency.classify(rows, TODAY)
        self.assertEqual(slate[0][3], "+01:00")

    def test_C13_PERMISSIVE_is_imported_and_not_restated(self):
        sys.path.insert(0, os.path.join(HERE, "..", "p444-root-vs-tree-family"))
        import root_vs_tree
        self.assertIs(recency.PERMISSIVE, root_vs_tree.PERMISSIVE)

    def test_C14_a_future_committer_date_is_reported_not_clamped(self):
        rows = recency.read_grades(table(row("o/future", "MIT", "2026-11-01")))
        slate, _ = recency.classify(rows, TODAY)
        self.assertEqual(slate[0][4], -7)


class Refusals(unittest.TestCase):
    """`P541` / `Gap 243`: an empty input is a refusal, never a green run."""

    def _run(self, *args):
        return subprocess.run([sys.executable, "-I",
                               os.path.join(HERE, "recency.py"), *args],
                              capture_output=True, text=True)

    def test_C15_no_mode_refuses_with_exit_2(self):
        self.assertEqual(self._run().returncode, 2)

    def test_C16_no_table_refuses_with_exit_2(self):
        self.assertEqual(self._run("classify").returncode, 2)

    def test_C17_an_empty_table_refuses_with_exit_2(self):
        fh = tempfile.NamedTemporaryFile("w", suffix=".tsv", delete=False)
        fh.write(HDR)
        fh.close()
        r = self._run("classify", fh.name)
        self.assertEqual(r.returncode, 2)
        self.assertIn("refusing", r.stderr)

    def test_C18_a_real_table_exits_0(self):
        r = self._run("classify", table(row("o/x", "MIT", "2026-10-24")),
                      "--today", "2026-10-25")
        self.assertEqual(r.returncode, 0)
        self.assertIn("o/x", r.stdout)


if __name__ == "__main__":
    unittest.main(verbosity=2)
