"""`ACTION XM` (p250) — exit-code REACHABILITY over the standing gate.

p250 found `lazy_lint.py` reporting two real findings on every run and exiting
`0` regardless, so `make hooks` printed `ALL OFFLINE LICENCE CONTROLS PASS`
underneath its own failure.  XM asks the general question: how many of the
gate's controls can ACTUALLY fail?

Two layers have to agree for a control to be failure-capable:

  1. the RECIPE line must let a non-zero status out (`set -e`, `&&`, no
     `|| true`, no trailing `exit 0`, no leading `-`, and the subject must be
     the LAST stage of any pipeline), and
  2. the SUITE must return non-zero when one of its own controls fails.

Layer 2 has a measured trap of its own: `unittest.main()` exits `0` when it
collects ZERO tests, and it exits `0` when every test is skipped (both measured
at p251).  A suite wired into the gate through `unittest.main()` therefore has
a SILENT-ZERO mode: rename its methods off the `test_` prefix and the control
keeps printing nothing and keeps passing.  The gate pipes exactly those suites
through `2>&1`, which is the only channel on which `Ran 0 tests` would appear.

So this module reports, per recipe line, `failure_capable` (layer 1) and
`silent_zero` (layer 2), and it pins a FLOOR on the number of tests each
unittest suite must collect, because a floor is the only thing that makes
layer 2 fail out loud.
"""
import re

# ── layer 1: the recipe line ───────────────────────────────────────────────────
SWALLOWERS = (
    (re.compile(r"\|\|\s*true\b"),            "|| true"),
    (re.compile(r"\|\|\s*:\s*(;|$)"),         "|| :"),
    (re.compile(r";\s*exit\s+0\b"),           "; exit 0"),
    (re.compile(r"^\s*-"),                    "leading - (make ignores status)"),
)
# a pipeline whose last stage is a reader, not the subject: the status is the
# reader's.  `set -o pipefail` is NOT set in this gate, measured at p251.
PIPE_READERS = re.compile(r"\|\s*(tail|head|cat|tee|sort|wc|awk|grep|cut|sed|column)\b")

def classify_recipe_line(line):
    """Return a record for one shell command taken from a make recipe."""
    cmd = line.strip().rstrip("\\").strip()
    swallow = []
    for rx, name in SWALLOWERS:
        if rx.search(cmd):
            swallow.append(name)
    if PIPE_READERS.search(cmd):
        swallow.append("pipeline: status is the reader's (no pipefail)")
    return {
        "cmd": cmd,
        "stdout_suppressed": ">/dev/null" in cmd or "> /dev/null" in cmd,
        "stderr_suppressed": "2>&1" in cmd or "2>/dev/null" in cmd,
        "swallowers": swallow,
        "failure_capable": not swallow,
    }

# ── layer 2: how a suite signals failure ──────────────────────────────────────
EXPLICIT = (
    re.compile(r"sys\.exit\("),
    re.compile(r"raise\s+SystemExit"),
    re.compile(r"(?:^|\|\||;|&&|then)\s*exit\s+1\b", re.M),
    re.compile(r"\[\s*\"?\$\{?\w+\}?\"?\s*(-eq|=)\s*\"?0\"?\s*\]\s*(\|\|\s*exit\s+1)?\s*$", re.M),
)
UNITTEST_MAIN = re.compile(r"unittest\.main\(")

TRIPLE = re.compile(r'(""".*?"""|\'\'\'.*?\'\'\')', re.S)
STRING = re.compile(r"('[^'\n]*'|\"[^\"\n]*\")")
COMMENT = re.compile(r"(?m)(?:^|\s)#.*$")

def _code_only(src):
    """Docstrings and comments are PROSE, not a call.

    🔴 Measured at p251 on this instrument's own suites, twice. First: both say
    *"deliberately NOT a `unittest.main()` suite"* in their docstring, and a
    bare source-text search graded both as `UNITTEST-MAIN`. Then, after
    docstrings were stripped, THIS suite was still graded `UNITTEST-MAIN`
    because it passes a `unittest.main()` source to the classifier as a string
    LITERAL. A call is never inside quotes, so literals go too. A classifier
    that reads a sentence about a call as the call is the same class of defect
    as a gate that cannot fail.
    """
    return COMMENT.sub("", STRING.sub("''", TRIPLE.sub("", src)))

def suite_signal(src, lang="python"):
    """`UNITTEST-MAIN` (silent-zero mode), `EXPLICIT-EXIT`, or `NONE`.

    🔴 `lang` is not decoration. Stripping string literals is right for Python
    and WRONG for shell: `[ "$fail" -eq 0 ]` — the exit expression of five
    suites in this gate — is mostly quoted, and the first version of this
    function stripped it away and graded `p207` as `NONE`. Measured at p251 by
    this suite's own control, which is why the control is still here.
    """
    if lang == "python":
        src = _code_only(src)
    if UNITTEST_MAIN.search(src):
        return "UNITTEST-MAIN"
    for rx in EXPLICIT:
        if rx.search(src):
            return "EXPLICIT-EXIT"
    return "NONE"

def silent_zero(signal):
    """True when the control passes while asserting nothing.

    Measured at p251 with two throwaway suites: `unittest.main(verbosity=0)`
    exits `0` both with zero collected tests and with every test skipped.
    """
    return signal == "UNITTEST-MAIN"

def collected_tests(src):
    """Statically count the methods `unittest` would collect."""
    return len(re.findall(r"^\s*def\s+test\w*\s*\(", src, re.M))

# FLOORS: measured by running every suite individually at p251 (the gate itself
# is not runnable from that session; each suite was invoked on its own).  A
# rename, a mass skip or a dropped class drops the count below its floor.
FLOORS = {
    "p222-ecosystem-bound-grammar/test_bound_grammar.py": 32,
    "p228-shelf-gate/test_shelf_gate.py": 36,
    "p1054-mit-plus-clause/test_mit_plus.py": 34,   # p252: raised from 14 by ACTION XQ
    "p242-grant-delta/test_grant_delta.py": 23,
    "p1058-empty-payload-gate/test_empty_payload_gate.py": 29,
}

def floor_verdict(relpath, src):
    """`OK`, `BELOW-FLOOR` or `UNPINNED` for a unittest-style suite."""
    floor = FLOORS.get(relpath)
    if floor is None:
        return "UNPINNED", None, None
    n = collected_tests(src)
    return ("OK" if n >= floor else "BELOW-FLOOR"), n, floor
