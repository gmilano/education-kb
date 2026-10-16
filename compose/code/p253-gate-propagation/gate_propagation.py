"""`p253` — the gate must propagate a failing step, not narrate one.

Measured, not read: `make hooks` printed `ALL OFFLINE LICENCE CONTROLS PASS` and exited
`0` while `compose/code/p252-ungated-floors/test_ungated_floors.py` exited `1`.

The mechanism.  Every recipe step has the shape

    cd <instrument> && $(PY) -I <suite> >/dev/null && echo "   PASS"; \\

and bash exempts a command that is NOT the last in an `&&` list from `errexit`.  So a
failing suite produces one missing `PASS` line in the middle of 27 of them, and the recipe
runs on to its success banner.

Why `ACTION XM` and `ACTION XR` could not find it.  Both audited whether each SUITE can
signal failure — `XM` enumerated all 26 commands and found the five `unittest.main()`
suites that exit `0` on zero collected tests; `XR` named the 71 ungated ones.  Neither
asked whether the GATE propagates the signal it is given.  And `p251` and `p252` both
recorded `make` as refused by their session, so the audit was done by READING the recipe.
This pass could run it; the first run exposed it.

This module checks the recipe's shape, so the defect cannot return by an edit.
"""

import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
MAKEFILE = os.path.join(REPO, "Makefile")

OLD_SHAPE = 'set -e; \necho "step 1"; \ncd /tmp && false >/dev/null && echo "   PASS"; \necho "banner"\n'
NEW_SHAPE = 'set -e; \necho "step 1"; \ncd /tmp && false >/dev/null && echo "   PASS" || exit 1; \necho "banner"\n'


def run_shape(script):
    """(exit status, whether the banner printed) for a recipe shape."""
    p = subprocess.run(["bash", "-c", script], capture_output=True, text=True)
    return p.returncode, "banner" in p.stdout


def recipe_lines(makefile=None):
    with open(makefile or MAKEFILE, encoding="utf-8") as fh:
        return fh.read().splitlines()


def pass_steps(lines):
    """Recipe lines that announce a PASS."""
    return [l for l in lines if '&& echo "   PASS"' in l]


def unguarded(lines):
    """PASS steps with no explicit `|| exit 1` — each one can swallow a failure."""
    return [l for l in pass_steps(lines) if "|| exit 1" not in l]


def banner_guarded(lines):
    """Is the success banner preceded only by guarded steps?"""
    for i, l in enumerate(lines):
        if "ALL OFFLINE LICENCE CONTROLS PASS" in l and l.lstrip().startswith("echo"):
            return not unguarded(lines[:i])
    return False


def main(argv):
    lines = recipe_lines()
    bad = unguarded(lines)
    print("PASS steps\t%d" % len(pass_steps(lines)))
    print("unguarded\t%d" % len(bad))
    print("banner guarded\t%s" % banner_guarded(lines))
    for b in bad:
        print("UNGUARDED\t%s" % b.strip()[:110])
    if "--verify" in argv[1:]:
        if bad or not banner_guarded(lines):
            print("FAIL: a failing step can reach the success banner")
            return 1
        print("OK: every gate step propagates its failure")
    return 1 if (bad and "--verify" in argv[1:]) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
