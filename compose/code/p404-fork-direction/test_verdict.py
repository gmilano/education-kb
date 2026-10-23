"""Controls for `p404`'s fork-direction rule.  Run from this directory:

    python3 test_verdict.py

Explicit non-zero exit and an asserted control total, per `p251`'s `ACTION XM`
finding and `p252`'s silent-zero population: a suite wired through
`unittest.main()` passes while collecting nothing, so this one never is.

The three MEASURED pairs are pinned as controls.  They are the pairs `p402`
left open, and they are the cases a ref-set test gets wrong (the first two) or
grades as "unrelated" (the third).
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from verdict import grade

passed = failed = 0


def chk(name, got, want):
    global passed, failed
    if got == want:
        passed += 1
        print("ok   %-66s" % name)
    else:
        failed += 1
        print("FAIL %-66s got=%r want=%r" % (name, got, want))


def chk_raises(name, *args, **kw):
    global passed, failed
    try:
        grade(*args, **kw)
    except ValueError:
        passed += 1
        print("ok   %-66s" % name)
    else:
        failed += 1
        print("FAIL %-66s no ValueError" % name)


# ── the three measured pairs, 2026-10-23 ─────────────────────────────────────
# ADORSYS-GIS (a) vs lmscloud-io (b): 0 shared commits, 1 shared tree, and the
# shared tree is ADORSYS-GIS's ROOT tree -> ADORSYS-GIS is the copy.
chk("aiprovider_openaicompatible is a CONTENT-COPY, direction a",
    grade(0, 1, False, False, root_tree_owner="a"), ("CONTENT-COPY", "a"))
# astiusa (a) 91 commits vs macewan-cs (b) 89; 89 shared, b's HEAD is an
# ancestor of a's -> astiusa continues macewan-cs.
chk("the lti pair is a SUPERSET, not a name collision",
    grade(89, 89, True, False), ("SUPERSET", "a"))
# lmscloud-io vs peancor: nothing shared at either level.
chk("the moodle-mcp-server pair is INDEPENDENT",
    grade(0, 0, False, False), ("INDEPENDENT", None))

# ── negative controls ────────────────────────────────────────────────────────
chk("a copy with no root signal is given NO direction",
    grade(0, 3, False, False), ("CONTENT-COPY", None))
chk("a diverged fork is not graded as a superset",
    grade(40, 40, False, False), ("DIVERGED-FORK", None))
chk("the superset verdict is symmetric",
    grade(12, 12, False, True), ("SUPERSET", "b"))
chk("identical heads are SAME-HEAD, not SUPERSET",
    grade(5, 5, True, True), ("SAME-HEAD", None))
# 🔴 The load-bearing one: this is the exact mistake a commit-only test makes.
chk("0 shared commits with shared trees is NEVER reported INDEPENDENT",
    grade(0, 1, False, False)[0] == "INDEPENDENT", False)
chk_raises("a negative count is refused, not graded", -1, 0, False, False)
chk_raises("mutual ancestry with no shared commits is refused", 0, 0, True, True)

chk("control total", passed + failed, 10)
print("\n%d/%d passed" % (passed, passed + failed))
sys.exit(1 if failed else 0)
