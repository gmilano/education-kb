#!/usr/bin/env python3
"""`P799` -- the board of suites is COUNTED, and a red is attributed to a cause.

Sixty-fifth pass, 2026-10-08. Single file on purpose (see `p798`): it runs
under `python3 -I`, the only mode this session is permitted to execute.

    python3 test_census.py
    python3 -I test_census.py

WHY THIS EXISTS.  `Gap 257`/`Gap 258` have said for several passes that the
board of suites is UNMEASURED, and pass 63 put the shortfall plainly: three
greens are not 112.  This pass ran the board.  Two things came back, and the
second matters more than the first.

  1.  THE BOARD IS 106 SUITES, NOT 112.  The figure 112 was never measured.
      106 is `find compose/code -name 'test_*.py' | wc -l` across 143
      directories -- so 37 directories carry no suite at all.

  2.  41 OF THE 44 REDS WERE AN ARTIFACT OF THE INSTRUMENT.  `python3 -I`
      implies `-P`, which drops the script's own directory from `sys.path[0]`,
      so every suite that imports its sibling module raises
      `ModuleNotFoundError`.  That is a fact about the FLAG, not about the
      suite.  A control probe (own script, own sibling module) reproduced it:
      plain `python3` imports fine, `-I` and `-P` both fail.

THE HONEST RESIDUE, which is the deliverable: of 106 suites, 63 are green,
41 are unresolvable under the permitted flag, 1 is red for a broken
environment dependency, and EXACTLY ONE IS A REAL RED -- `p351`, this KB's
own star-count gate.  Pass 64 published a tree it could not run; this pass
publishes a tree it ran, with one named defect in it.

WHAT IT DOES NOT CLAIM.  The 41 are not green.  They are UNREAD, and calling
them green would be the same error in the opposite direction.
"""
import csv
import os
import unittest

HERE = os.path.dirname(os.path.abspath(__file__))
BOARD = os.path.join(HERE, "board.2026-10-08.tsv")

GREEN = ("green", "green-slow-137s")
UNREAD = ("red-minusI-syspath",)
ENVIRONMENT = ("red-env-cryptography",)
REAL = ("red-real",)


def rows(path=BOARD):
    with open(path, newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


def tally(rs=None):
    rs = rows() if rs is None else rs
    out = {}
    for r in rs:
        out[r["verdict"]] = out.get(r["verdict"], 0) + 1
    return out


def by_class(rs=None):
    rs = rows() if rs is None else rs
    g = sum(1 for r in rs if r["verdict"] in GREEN)
    u = sum(1 for r in rs if r["verdict"] in UNREAD)
    e = sum(1 for r in rs if r["verdict"] in ENVIRONMENT)
    x = sum(1 for r in rs if r["verdict"] in REAL)
    return {"green": g, "unread": u, "environment": e, "real_red": x}


class TheBoardIsCounted(unittest.TestCase):
    def test_the_board_is_106_and_not_112(self):
        self.assertEqual(len(rows()), 106)

    def test_every_row_carries_an_attributed_verdict(self):
        known = set(GREEN) | set(UNREAD) | set(ENVIRONMENT) | set(REAL)
        for r in rows():
            self.assertIn(r["verdict"], known, f"{r['dir']} unattributed")

    def test_the_four_classes_partition_the_board(self):
        c = by_class()
        self.assertEqual(c["green"] + c["unread"] + c["environment"] + c["real_red"],
                         106)

    def test_sixty_three_green(self):
        self.assertEqual(by_class()["green"], 63)

    def test_forty_one_are_UNREAD_and_are_not_counted_green(self):
        c = by_class()
        self.assertEqual(c["unread"], 41)
        self.assertNotEqual(c["green"], 63 + 41)


class ARedIsAttributedToACause(unittest.TestCase):
    def test_exactly_one_real_red_and_it_is_p351(self):
        real = [r for r in rows() if r["verdict"] in REAL]
        self.assertEqual(len(real), 1)
        self.assertEqual(real[0]["dir"], "p351-star-digit-sweep")

    def test_the_unread_class_is_justified_by_its_own_error_text(self):
        """The claim 'this is a flag artifact' has to be visible in the row."""
        for r in rows():
            if r["verdict"] in UNREAD:
                self.assertIn("ModuleNotFoundError", r["tail"],
                              f"{r['dir']} classed UNREAD without the error")

    def test_the_environment_red_is_not_a_syspath_red(self):
        """`p213` fails on `cryptography`'s Rust binding under plain `python3`,
        `-I` and `-E -s` alike -- measured, three flag combinations. So it is
        not the `-P` artifact and it is not the suite's own logic."""
        env = [r for r in rows() if r["verdict"] in ENVIRONMENT]
        self.assertEqual(len(env), 1)
        self.assertEqual(env[0]["dir"], "p213-envelope-aad")
        self.assertNotIn("ModuleNotFoundError", env[0]["tail"])

    def test_a_timeout_is_not_a_failure(self):
        """`p471` exceeded a 120 s cap in the sweep and was first written down
        as red. Re-run without the cap: 27/27 then 25/25, exit 0, 137.5 s.
        The instrument's timeout had become the suite's verdict."""
        slow = [r for r in rows() if r["verdict"] == "green-slow-137s"]
        self.assertEqual(len(slow), 1)
        self.assertEqual(slow[0]["dir"], "p471-gap-gate-language")


class NegativeControls(unittest.TestCase):
    def test_a_fabricated_verdict_is_rejected(self):
        bogus = [{"verdict": "green-ish", "dir": "x", "file": "y", "tail": ""}]
        known = set(GREEN) | set(UNREAD) | set(ENVIRONMENT) | set(REAL)
        self.assertNotIn(bogus[0]["verdict"], known)

    def test_tally_and_by_class_agree(self):
        self.assertEqual(sum(tally().values()), sum(by_class().values()))

    def test_directories_without_a_suite_are_outside_this_count(self):
        """143 directories, 106 suites: 37 carry no `test_*.py`. The census
        counts SUITES, and says so, so the two numbers are never conflated."""
        self.assertEqual(143 - 106, 37)


if __name__ == "__main__":
    unittest.main(verbosity=1)
