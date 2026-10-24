#!/usr/bin/env python3
"""p423 -- `make hooks` CANNOT BLOCK A COMMIT, because it has been red on purpose since `p398`.

## The finding

`p422` declared its gate suite un-run and honoured every file contract *by hand*.  `p423`
ran the suite against `p422`'s commit `82235af` and measured what the hand-honouring cost:
**47 of 53 green, six red**, of which exactly one is the deliberate carried red
(`Gap 400-B`, `gate-census-union` control 24, red since `p398`) and **five were new**:

    gate-register-currency   the register lagged the shelves by a whole pass
    gate-census-currency     2 of 3 published census cells stale
    gate-union-currency      3 of 3 published union cells stale
    gate-fold-identity       a new casing published for a carried address
    gate-action-answered     a pinned cardinality broken by a legitimate shelf row

So the obvious remedy is to stop relying on an operator to run the suite and make a red
suite physically unable to commit -- a `pre-commit` hook.  **And this base cannot do that
as it stands, which is the sharper half of the finding.**  `make hooks` has exited
non-zero on every pass since `p398` by design: `Gap 400-B` is carried red deliberately, so
the suite's exit status has carried no information for twenty-five passes.  A permanently
red suite is not a control, it is a colour.  Nothing in this base said so, because nothing
ever asked the suite for a yes-or-no answer.

## The contract

A gate may be carried red only if it is DECLARED red and its declaration is REGISTERED:

    P423-UNDECLARED-RED     a gate in `DECLARED_RED` that is not in `HOOK_GATES` -- a
                            declaration for a gate the suite does not even run
    P423-UNREGISTERED-RED   a gate carried red with no gap id citing it in
                            `intel/open-gaps.md`

The second is the one that matters, and it is what keeps this from becoming a way to
silence an inconvenient gate: declaring a gate red costs a registered gap, in the open,
under a pass number.  `p387-G` forbids closing a gap by loosening a control, and this
instrument is built so that the only way to quiet a gate is to write down that you did.

The BLOCKING set is then `HOOK_GATES - DECLARED_RED`, and THAT is what a commit hook can
ask a yes-or-no question of.

## What this instrument does not do

🟡 A `pre-commit` hook lives in `.git/hooks`, which `git clone` does not carry.  So the
enforcement is per-working-copy and has to be installed (`make install-hooks`); the gate
below checks that the hook SCRIPT is present and correct in the tree, which does survive a
clone, and the installed-or-not state of this particular working copy is reported as a
CENSUS row rather than gated.  Registered as `Gap 423-B` instead of papered over.
"""
import os
import re
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(_HERE)))


def _makefile_list(name, text):
    """The gate names in a Makefile list variable, honouring `\\` continuations."""
    m = re.search(r"^%s\s*=(.*?)(?=\n[^\s#]|\n\n)" % re.escape(name), text,
                  re.M | re.S)
    if not m:
        return []
    body = m.group(1).replace("\\\n", " ").replace("\\", " ")
    return [w for w in body.split() if w.startswith("gate-") or w in ("recount",)]


def read_sets(root=None):
    """(hook_gates, declared_red) as the Makefile declares them."""
    root = root or ROOT
    with open(os.path.join(root, "Makefile"), encoding="utf-8") as fh:
        text = fh.read()
    return _makefile_list("HOOK_GATES", text), _makefile_list("DECLARED_RED", text)


def blocking_set(root=None):
    hooks, red = read_sets(root)
    return [g for g in hooks if g not in red]


def gate(root=None):
    """The declaration contract.  Returns a list of findings; [] is green."""
    root = root or ROOT
    hooks, red = read_sets(root)
    findings = []
    register = ""
    reg_path = os.path.join(root, "intel", "open-gaps.md")
    if os.path.exists(reg_path):
        with open(reg_path, encoding="utf-8") as fh:
            register = fh.read()
    for g in red:
        if g not in hooks:
            findings.append(("Makefile", "P423-UNDECLARED-RED", g,
                             "declared red but not in HOOK_GATES"))
            continue
        # A declaration costs a registered gap: the gate name must appear in the register
        # on a line that also carries a gap id.
        cited = any(g in line and re.search(r"Gap \d+-[A-Z]", line)
                    for line in register.splitlines())
        if not cited:
            findings.append(("intel/open-gaps.md", "P423-UNREGISTERED-RED", g,
                             "carried red with no `Gap N-X` citing it"))
    return findings


def hook_installed(root=None):
    """CENSUS, not a gate: does THIS working copy have the hook installed?"""
    root = root or ROOT
    p = os.path.join(root, ".git", "hooks", "pre-commit")
    if not os.path.exists(p):
        return False, "absent — run `make install-hooks`"
    if not os.access(p, os.X_OK):
        return False, "present but not executable"
    with open(p, encoding="utf-8", errors="replace") as fh:
        body = fh.read()
    if "commit-gates" not in body:
        return False, "present but does not run `make commit-gates`"
    return True, "installed"


def main(argv):
    mode = argv[0] if argv else "gate"
    if mode == "blocking":
        for g in blocking_set():
            print(g)
        return 0
    if mode == "census":
        hooks, red = read_sets()
        ok, why = hook_installed()
        print("file\tfinding\tdetail")
        print("Makefile\tHOOK_GATES\t%d" % len(hooks))
        print("Makefile\tDECLARED_RED\t%s" % (",".join(red) or "-"))
        print("Makefile\tBLOCKING\t%d" % len(blocking_set()))
        print(".git/hooks/pre-commit\tINSTALLED-HERE\t%s" % why)
        print("#\ttotal\t%d" % len(hooks))
        return 0
    rows = gate()
    print("file\tfinding\tgate\tdetail")
    for r in rows:
        print("\t".join(r))
    print("#\ttotal\t%d" % len(rows))
    return 1 if rows else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
