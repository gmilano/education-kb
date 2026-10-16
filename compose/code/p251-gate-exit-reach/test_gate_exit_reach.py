"""Controls for `ACTION XM`'s instrument.  Run from this directory:

    python3 test_gate_exit_reach.py

Deliberately NOT a `unittest.main()` suite: this instrument exists because
`unittest.main()` has a silent-zero mode, so its own controls end in an
explicit non-zero exit and assert their own total (`P176`/`suite-total-control`).
"""
import os, subprocess, sys, tempfile, textwrap
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gate_reach import (classify_recipe_line, suite_signal, silent_zero,
                        collected_tests, floor_verdict, FLOORS, _code_only)

HERE = os.path.dirname(os.path.abspath(__file__))
CODE = os.path.dirname(HERE)
passed = failed = 0

def chk(name, got, want):
    global passed, failed
    if got == want:
        passed += 1
        print("ok   %-62s" % name)
    else:
        failed += 1
        print("FAIL %-62s got=%r want=%r" % (name, got, want))

# ── layer 1: the swallowing patterns, each one a real shape ────────────────────
chk("plain && echo PASS is failure-capable",
    classify_recipe_line('cd x && python3 t.py >/dev/null && echo "   PASS"')["failure_capable"], True)
chk("|| true is NOT failure-capable",
    classify_recipe_line('python3 carried_index.py claims "$(TOKEN)" . || true')["failure_capable"], False)
chk("trailing ; exit 0 is NOT failure-capable",
    classify_recipe_line('bash suite.sh; exit 0')["failure_capable"], False)
chk("leading - is NOT failure-capable",
    classify_recipe_line('-python3 suite.py')["failure_capable"], False)
chk("pipe into a reader is NOT failure-capable",
    classify_recipe_line('python3 suite.py | tail -3')["failure_capable"], False)
chk("|| : is NOT failure-capable",
    classify_recipe_line('bash suite.sh || :')["failure_capable"], False)
chk("suppression is not swallowing (stdout)",
    classify_recipe_line('python3 t.py >/dev/null && echo ok')["stdout_suppressed"], True)
chk("suppression is not swallowing (status still out)",
    classify_recipe_line('python3 t.py >/dev/null 2>&1 && echo ok')["failure_capable"], True)
chk("2>&1 is recorded as stderr suppression",
    classify_recipe_line('python3 t.py >/dev/null 2>&1 && echo ok')["stderr_suppressed"], True)

# ── layer 2: how a suite signals, and the silent-zero mode ────────────────────
chk("unittest.main is UNITTEST-MAIN", suite_signal("import unittest\nunittest.main()"), "UNITTEST-MAIN")
chk("UNITTEST-MAIN has a silent-zero mode", silent_zero("UNITTEST-MAIN"), True)
chk("sys.exit(1) is EXPLICIT-EXIT", suite_signal("if fails:\n    sys.exit(1)\n"), "EXPLICIT-EXIT")
chk("EXPLICIT-EXIT has no silent-zero mode", silent_zero("EXPLICIT-EXIT"), False)
chk("shell [ \"$fail\" -eq 0 ] tail is EXPLICIT-EXIT",
    suite_signal('printf "%d passed" "$pass"\n[ "$fail" -eq 0 ]\n', lang="shell"), "EXPLICIT-EXIT")
chk("and reading that shell tail AS PYTHON loses it (why `lang` exists)",
    suite_signal('printf "%d passed" "$pass"\n[ "$fail" -eq 0 ]\n'), "NONE")
chk("a printer that never exits is NONE", suite_signal('print("# 2 finding(s)")\n'), "NONE")
# p251's own defect, found by this instrument's audit of this instrument.
chk("a DOCSTRING mentioning unittest.main() is prose, not a call",
    suite_signal('"""Deliberately NOT a unittest.main() suite."""\nimport sys\nsys.exit(1)\n'),
    "EXPLICIT-EXIT")
chk("a COMMENT mentioning unittest.main() is prose, not a call",
    suite_signal('# unittest.main() would be wrong here\nimport sys\nsys.exit(1)\n'), "EXPLICIT-EXIT")
chk("a real call still reads as UNITTEST-MAIN",
    suite_signal('"""about unittest.main()"""\nimport unittest\nunittest.main()\n'), "UNITTEST-MAIN")
chk("_code_only drops the docstring", "unittest" in _code_only('"""unittest.main()"""\nx = 1\n'), False)
# the SECOND road to the same wrong answer, found by auditing this file itself:
# a suite that passes a `unittest.main()` source to the classifier as a string.
chk("a unittest.main() inside a STRING LITERAL is not a call",
    suite_signal('src = "import unittest; unittest.main()"\nimport sys\nsys.exit(1)\n'),
    "EXPLICIT-EXIT")

# the silent-zero mode is not a reading of the docs: it is measured, here, now.
def _exit_code(body):
    with tempfile.TemporaryDirectory() as d:
        p = os.path.join(d, "s.py")
        open(p, "w").write(textwrap.dedent(body))
        return subprocess.run([sys.executable, "-I", p], capture_output=True).returncode

chk("MEASURED: unittest.main exits 0 with zero collected tests", _exit_code("""
    import unittest
    class S(unittest.TestCase):
        def check_nothing(self):
            self.assertTrue(False)
    unittest.main(verbosity=0)
    """), 0)
chk("MEASURED: unittest.main exits 0 when every test is skipped", _exit_code("""
    import unittest
    class S(unittest.TestCase):
        @unittest.skip("x")
        def test_a(self):
            self.assertTrue(False)
    unittest.main(verbosity=0)
    """), 0)
chk("MEASURED: unittest.main exits 1 on a real failure", _exit_code("""
    import unittest
    class S(unittest.TestCase):
        def test_a(self):
            self.assertTrue(False)
    unittest.main(verbosity=0)
    """), 1)

# ── the floors: what makes layer 2 fail out loud ──────────────────────────────
chk("a renamed method drops below the floor",
    floor_verdict("p228-shelf-gate/test_shelf_gate.py", "def check_a(self): pass")[0], "BELOW-FLOOR")
chk("collected_tests counts only test_ methods",
    collected_tests("def test_a(self):\n    pass\ndef helper(self):\n    pass\n"), 1)
for rel, floor in sorted(FLOORS.items()):
    path = os.path.join(CODE, rel)
    src = open(path, encoding="utf-8").read() if os.path.exists(path) else ""
    verdict, n, fl = floor_verdict(rel, src)
    chk("floor holds: %s (>= %d, has %s)" % (rel.split("/")[0], floor, n), verdict, "OK")

# ── p250's own defect, pinned so it cannot come back ──────────────────────────
lint = os.path.join(CODE, "p230-prose-path-ladder", "lazy_lint.py")
lint_src = open(lint, encoding="utf-8").read() if os.path.exists(lint) else ""
chk("lazy_lint main() can still return non-zero (p250)",
    "return 1" in lint_src, True)

# ── and this suite asserts its own total (suite-total-control) ────────────────
# ── ACTION XS: the stand-in runner must itself be able to FAIL ────────────────
# p251's own rule, applied to p251's own script: a check that cannot fail is not
# a check.  A throwaway root with one deliberately failing suite proves it.
def _runner_exit_on_failing_root():
    with tempfile.TemporaryDirectory() as d:
        os.makedirs(os.path.join(d, "compose", "code", "x"))
        open(os.path.join(d, "compose", "code", "x", "test_x.py"), "w").write(
            "import sys\nprint('FAIL deliberate')\nsys.exit(1)\n")
        open(os.path.join(d, "Makefile"), "w").write(
            "gate-offline:\n"
            "\t@set -e; \\\n"
            "\techo \"-- x\"; \\\n"
            "\tcd compose/code/x && python3 test_x.py >/dev/null && echo \"   PASS\"; \\\n"
            "\tcd - >/dev/null; \\\n"
            "\techo DONE\n")
        r = subprocess.run(["bash", os.path.join(HERE, "run_controls.sh"), d],
                           capture_output=True, text=True)
        return r.returncode, "test_x.py" in r.stdout

chk("run_controls.sh exits non-zero when a control fails", _runner_exit_on_failing_root(), (1, True))

chk("control total", passed + failed, 33)
print("\n%d/%d passed" % (passed, passed + failed))
sys.exit(1 if failed else 0)
