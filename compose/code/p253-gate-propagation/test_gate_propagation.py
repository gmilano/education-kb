"""Controls for `p253-gate-propagation`.  Explicit exit; cannot pass while asserting nothing."""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gate_propagation as gp  # noqa: E402

FAILED = []
RAN = 0


def chk(name, got, want):
    global RAN
    RAN += 1
    if got != want:
        FAILED.append("  FAIL %s\n       got  %r\n       want %r" % (name, got, want))
    else:
        print("  OK   %s" % name)


# The defect, asserted rather than described: `set -e` does NOT save the old shape.
chk("the OLD recipe shape swallows a failing step and reaches the banner",
    gp.run_shape(gp.OLD_SHAPE), (0, True))
chk("the HARDENED shape aborts and the banner is unreachable",
    gp.run_shape(gp.NEW_SHAPE), (1, False))

LINES = gp.recipe_lines()
chk("the gate still has its steps", len(gp.pass_steps(LINES)) >= 25, True)
chk("every PASS step carries an explicit `|| exit 1`", gp.unguarded(LINES), [])
chk("the success banner is unreachable while any step is unguarded",
    gp.banner_guarded(LINES), True)

# And the instrument must FAIL on a recipe that regresses.
REGRESSED = [
    '\t@set -e; \\',
    '\techo "-- step"; \\',
    '\tcd compose/code/x && python3 t.py >/dev/null && echo "   PASS"; \\',
    '\techo "ALL OFFLINE LICENCE CONTROLS PASS"',
]
chk("a regressed recipe is reported as unguarded", len(gp.unguarded(REGRESSED)), 1)
chk("and its banner is not guarded", gp.banner_guarded(REGRESSED), False)

print()
if FAILED:
    print("\n".join(FAILED))
    print("test_gate_propagation.py: %d/%d checks passed, %d FAILED"
          % (RAN - len(FAILED), RAN, len(FAILED)))
    sys.exit(1)
print("test_gate_propagation.py: %d/%d checks passed" % (RAN, RAN))
sys.exit(0)
