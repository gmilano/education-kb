#!/usr/bin/env python3
"""`P174` suite — the clone-path gate. Fully OFFLINE.

Every assertion runs against a fixture in `fixtures/` or against this repository's
own instrument tree, so the suite is deterministic and re-runnable.

What is tested, in increasing order of what it would catch:
  A. the classifier calls executable text LIVE                  (the measurement)
  B. the classifier calls narrative COMMENT                     (the false-positive guard)
  C. a scratch `/tmp` file and a foreign absolute path are NOT hits (the scope guard)
  D. the gate is CLEAN on the live tree, and FIRES on the frozen
     pre-patch census p174 measured                             (the control)
"""
from __future__ import annotations

import pathlib
import subprocess
import sys
import unittest

HERE = pathlib.Path(__file__).resolve().parent
KB = HERE.parents[2]
GATE = HERE / "check_clone_paths.py"
sys.path.insert(0, str(HERE))
from check_clone_paths import classify_lines, sweep  # noqa: E402

# The 13 LIVE lines p174 measured on the tree as it stood at commit f5cdcf0 (p173's
# HEAD), before the P174-KC repair. Frozen here so the gate can be shown to FIRE and
# not merely to pass.
PRE_PATCH_LIVE = {
    ("compose/code/p120-unread-grant-resolution/depth.sh", 11),
    ("compose/code/p120-unread-grant-resolution/repair.py", 17),
    ("compose/code/p120-unread-grant-resolution/score.py", 76),
    ("compose/code/p120-unread-grant-resolution/score.py", 91),
    ("compose/code/p120-unread-grant-resolution/score_after.py", 76),
    ("compose/code/p120-unread-grant-resolution/score_after.py", 91),
    ("compose/code/p120-unread-grant-resolution/test_p120.sh", 105),
    ("compose/code/p120-unread-grant-resolution/test_p120.sh", 114),
    ("compose/code/p120-unread-grant-resolution/test_p120.sh", 115),
    ("compose/code/p121-stale-token-crosspage/test_p121.sh", 5),
    ("compose/code/p172-manifest-attribution/classify_bodies.sh", 6),
    ("compose/code/p996-promotion-ledger/build_ledger.py", 2),
    ("compose/code/p996-promotion-ledger/reconcile_code_shelf.py", 2),
}


def verdicts(name: str) -> list[str]:
    path = HERE / "fixtures" / name
    rows = classify_lines(path.read_text(encoding="utf-8"), suffix=path.suffix)
    return [v for _, v, _ in rows]


class Classifier(unittest.TestCase):
    def test_executable_shell_source_line_is_live(self) -> None:
        self.assertEqual(verdicts("live_shell.sh"), ["LIVE", "LIVE"])

    def test_executable_python_assignment_is_live(self) -> None:
        self.assertEqual(verdicts("live_python.py"), ["LIVE"])

    def test_shell_comment_narrative_is_not_live(self) -> None:
        got = verdicts("comment_only.sh")
        self.assertEqual(got, ["COMMENT", "COMMENT"])
        self.assertNotIn("LIVE", got)

    def test_python_docstring_narrative_is_not_live(self) -> None:
        got = verdicts("docstring_only.py")
        self.assertEqual(got, ["COMMENT"])

    def test_scratch_tmp_files_are_not_hits_at_all(self) -> None:
        self.assertEqual(verdicts("scratch_tmp_only.sh"), [])

    def test_a_foreign_absolute_path_is_not_a_hit(self) -> None:
        # FABRICATED negative control: widening the gate to every absolute path
        # would make it fire on half the tree, so it must stay silent here.
        self.assertEqual(verdicts("fabricated_other_repo.sh"), [])

    def test_self_relative_default_is_not_a_hit(self) -> None:
        text = 'ROOT="${1:-$(cd "$(dirname "$0")/../../.." && pwd)}"\n'
        self.assertEqual(classify_lines(text, suffix=".sh"), [])


class LiveTree(unittest.TestCase):
    def test_the_instrument_tree_has_no_live_clone_path(self) -> None:
        live = [(f, n) for f, n, v, _ in sweep(KB) if v == "LIVE"]
        self.assertEqual(live, [], f"LIVE clone paths: {live}")

    def test_the_narrative_hits_are_still_there_and_still_readable(self) -> None:
        # The repair must not have been done by DELETING the history of the defect.
        comment = {f for f, _, v, _ in sweep(KB) if v == "COMMENT"}
        self.assertIn("compose/code/p173-apache11-family/sweep_family.sh", comment)
        self.assertIn("compose/code/p355-cwd-portability/test_p355.py", comment)

    def test_gate_exits_zero_on_the_live_tree(self) -> None:
        done = subprocess.run(
            [sys.executable, "-I", str(GATE), str(KB)], capture_output=True, text=True
        )
        self.assertEqual(done.returncode, 0, done.stdout[-400:])


class Control(unittest.TestCase):
    def test_gate_fires_on_every_frozen_pre_patch_line(self) -> None:
        # A gate that has only ever been seen passing is not a gate. Each of the 13
        # lines p174 removed is kept verbatim in fixtures/pre-patch-lines.tsv and must
        # classify LIVE, so the classifier is shown to CATCH them and not merely to
        # agree with a tree that no longer has them.
        rows = [
            line.split("\t")
            for line in (HERE / "fixtures" / "pre-patch-lines.tsv")
            .read_text(encoding="utf-8")
            .splitlines()
            if line and not line.startswith("#")
        ]
        self.assertEqual(len(rows), 13)
        seen = set()
        for path, lineno, text in rows:
            suffix = ".py" if path.endswith(".py") else ".sh"
            got = classify_lines(text, suffix=suffix)
            self.assertEqual(
                [v for _, v, _ in got], ["LIVE"], f"{path}:{lineno} -> {got}"
            )
            seen.add((path, int(lineno)))
        self.assertEqual(seen, PRE_PATCH_LIVE)

    def test_the_frozen_census_is_four_instruments_and_nine_files(self) -> None:
        files = {f for f, _ in PRE_PATCH_LIVE}
        instruments = {f.split("/")[2] for f in files}
        self.assertEqual(len(files), 9)
        self.assertEqual(
            instruments,
            {
                "p120-unread-grant-resolution",
                "p121-stale-token-crosspage",
                "p172-manifest-attribution",
                "p996-promotion-ledger",
            },
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
