#!/usr/bin/env python3
"""Controls for `ACTION XZ`'s grader.

The important ones are the NEGATIVE controls: each of the four swallow shapes is reproduced
in bash here, so the grade is pinned to a MEASURED behaviour of the shell rather than to a
reading of it.  p253 earned that rule — two passes audited the gate by reading the recipe
and neither found the defect, which one `make hooks` run exposed immediately.
"""
import os
import subprocess
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import exit_reach as er  # noqa: E402

FAILS = 0


def check(name, got, want):
    global FAILS
    if got != want:
        print(f"FAIL {name}\n  got:  {got!r}\n  want: {want!r}")
        FAILS += 1


def shell_exit(script):
    """Run a bash snippet and return its exit status — the ground truth for a grade."""
    return subprocess.run(["bash", "-c", script], capture_output=True).returncode


# ── the four swallow shapes, each graded AND measured in bash ───────────────────────────
FAILING = 'python3 -c "import sys; sys.exit(1)"'

check("|| true is SWALLOWED-TRUE", er.grade_command(f"{FAILING} || true"), "SWALLOWED-TRUE")
check("…and bash agrees it cannot fail", shell_exit(f"{FAILING} || true"), 0)

check("instrument | head is SWALLOWED-PIPE",
      er.grade_command("$(PY) -I compose/code/x/y.py . | head -3"), "SWALLOWED-PIPE")
check("…and bash agrees it cannot fail", shell_exit(f"{FAILING} | head -3"), 0)

check("echo $(cmd) is SWALLOWED-SUBST",
      er.grade_command('echo "n: $$(python3 -c \'import sys; sys.exit(1)\')"'),
      "SWALLOWED-SUBST")
check("…and bash agrees it cannot fail",
      shell_exit('echo "n: $(python3 -c \'import sys; sys.exit(1)\')"'), 0)

check("p253's && list is rescued by the trailing guard",
      er.grade_command("cd d && test.py >/dev/null && echo '   PASS' || exit 1"), "GUARDED")
check("…and bash agrees the UNGUARDED form swallows (p253's defect, pinned)",
      shell_exit("set -e; cd /tmp && false >/dev/null && echo PASS; echo banner"), 0)
check("…while the guarded form does not",
      shell_exit("set -e; cd /tmp && false >/dev/null && echo PASS || exit 1; echo banner"), 1)

# ── the distinction the first measurement got wrong ─────────────────────────────────────
# A pipeline that only FORMATS a file an already-consumed step wrote loses nothing.
check("awk over a file is a REPORT, not a swallow",
      er.grade_command("awk -F'\\t' '{print $$2}' /tmp/x.tsv | sort | uniq -c"), "REPORT")
check("but the same pipe over an INSTRUMENT is a swallow",
      er.grade_command("python3 -I harvest.py . | sort | uniq -c"), "SWALLOWED-PIPE")

# ── positive controls ───────────────────────────────────────────────────────────────────
check("a plain command is CONSUMED", er.grade_command("$(PY) -I x.py --verify"), "CONSUMED")
check("echo is INERT", er.grade_command('echo "── a heading"'), "INERT")
check("a trailing grep -q is an assertion, not a formatter",
      er.grade_command("cat f | grep -q token"), "CONSUMED")

# ── the live Makefile must satisfy its own contract ─────────────────────────────────────
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..")
MK = os.path.join(ROOT, "Makefile")
if os.path.exists(MK):
    targets = er.audit(MK)
    check("every contracted target can fail", er.violations(targets), [])
    check("gate-offline is contracted", "gate-offline" in er.CONTRACTED, True)
    check("claims is contracted", "claims" in er.CONTRACTED, True)
    # the fix itself, pinned: `claims` must NOT end in `|| true` again
    claims = [g for _, g in targets.get("claims", [])]
    check("claims carries no swallowed line", [g for g in claims if g in er.SWALLOWED], [])
    # and the recipe must still exist — a contract satisfied by deletion is not a fix
    check("claims still has a step", len(targets.get("claims", [])) >= 1, True)

# ── the instrument must be able to FAIL, which is the whole point of XZ ─────────────────
with tempfile.TemporaryDirectory() as d:
    bad = os.path.join(d, "Makefile")
    with open(bad, "w", encoding="utf-8") as fh:
        fh.write('claims:\n\t@python3 -I x.py claims "$(TOKEN)" . || true\n')
    rc = subprocess.run([sys.executable, "-I", er.__file__, "--verify", bad],
                        capture_output=True).returncode
    check("--verify exits 1 on a swallowed contracted line", rc, 1)
    good = os.path.join(d, "Makefile.ok")
    with open(good, "w", encoding="utf-8") as fh:
        fh.write('claims:\n\t@python3 -I x.py claims "$(TOKEN)" .\n')
    rc = subprocess.run([sys.executable, "-I", er.__file__, "--verify", good],
                        capture_output=True).returncode
    check("--verify exits 0 once it is guarded", rc, 0)

print(f"p254-exit-status-reach: {'FAIL' if FAILS else 'PASS'} ({FAILS} failing)")
sys.exit(1 if FAILS else 0)
