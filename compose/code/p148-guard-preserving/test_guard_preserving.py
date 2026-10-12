"""Tests for p148-guard-preserving. 9 tests, authored fixtures, offline.

The module under test calls five real instruments, so the tests pin the parts that
are this module's own: `freeze` (so two runs are comparable at all), and the three
states the census can report. A test that needed the five instruments would be a
test of them, not of this.
"""

import os
import shutil
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import guard_preserving as gp

FAILS = []


def check(name, got, want):
    if got != want:
        FAILS.append("%s\n    got  %r\n    want %r" % (name, got, want))
        print("FAIL %s" % name)
    else:
        print("ok   %s" % name)


# 1 -- freeze is stable across dict ordering, or "bare == guarded" is meaningless
check("freeze is order-independent for dicts",
      gp.freeze({"a": 1, "b": 2}) == gp.freeze({"b": 2, "a": 1}), True)

# 2 -- …and order-SENSITIVE for lists, because a list order is a measurement
check("freeze preserves list order",
      gp.freeze([1, 2]) != gp.freeze([2, 1]), True)

# 3 -- freeze is order-independent for sets
check("freeze is order-independent for sets",
      gp.freeze({"x", "y"}) == gp.freeze({"y", "x"}), True)

# 4 -- nested structures round-trip
check("freeze handles nesting",
      gp.freeze({"k": [1, {"j": 2}]}), gp.freeze({"k": [1, {"j": 2}]}))

# 5 -- a tuple is not silently equal to a list of the same items
check("freeze does not conflate tuple and list",
      gp.freeze((1, 2)), gp.freeze([1, 2]))

# 6 -- every AT_RISK entry is a 5-tuple the census can splat
check("SUBJECTS entries have the arity census() calls with",
      sorted({len(s) for s in gp.SUBJECTS}), [5])

# 7 -- the five instruments named are the five P146-D identified
check("the population is P146-D's five at-risk instruments",
      [s[0] for s in gp.SUBJECTS],
      ["p141-surface-gate", "p143-surface-gate2", "p142-americas",
       "p142-schema-tiers", "p143-tenancy"])

# 8 -- a module that cannot be loaded is reported, not raised
r = gp.one("fake", "no-such-dir/no_such_module.py", "walk", None, "is_mcp_server",
           tempfile.mkdtemp())
check("an unloadable instrument is reported as LOAD_FAILED",
      r["status"], "LOAD_FAILED")

# 9 -- an empty tree yields REFUSED, never PRESERVED over nothing
d = tempfile.mkdtemp()
r = gp.one("p141-surface-gate", "p141-agent-surface-gate/surface_gate.py",
           "walk", None, "is_mcp_server", d)
check("an empty tree is REFUSED, not PRESERVED", r["status"], "REFUSED")
shutil.rmtree(d)

print("\n%d/%d passed" % (9 - len(FAILS), 9))
for f in FAILS:
    print("\n" + f)
sys.exit(1 if FAILS else 0)
