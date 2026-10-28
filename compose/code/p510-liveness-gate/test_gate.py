"""Offline controls for p510's liveness gate. No network: fixtures are recorded reads."""
import sys

from liveness_gate import (LIVE, UNREADABLE, ControlFailure, KNOWN_BAD,
                           KNOWN_GOOD, Read, classify, run_controls, sweep)

LIVE_OUT = ("ref: refs/heads/main\tHEAD\n"
            "1ea7df1554470000000000000000000000000000\tHEAD\n")
DEVELOP_OUT = ("ref: refs/heads/develop\tHEAD\n"
               "08e3ecace444873e80977d545ddae5a6b6029834\tHEAD\n")
ABSENT_ERR = "fatal: could not read Username for 'https://github.com': terminal prompts disabled\n"

CASES = []


def check(name, got, want):
    CASES.append((name, got == want, f"got {got!r} want {want!r}"))


# --- the classifier itself -------------------------------------------------
check("live reads LIVE+branch+head",
      classify(LIVE_OUT, ""), Read(LIVE, "main", "1ea7df155447"))
check("non-main default branch is preserved verbatim",
      classify(DEVELOP_OUT, "").branch, "develop")
check("absent is NOT asserted as absent",
      classify("", ABSENT_ERR).state, UNREADABLE)
check("a private repo is indistinguishable from an absent one",
      classify("", ABSENT_ERR).state, classify("", ABSENT_ERR).state)

# --- the gate refuses to publish a count unless both controls behave ------
def fake(mapping):
    return lambda slug: mapping.get(slug, Read("ERROR"))


both_ok = fake({KNOWN_GOOD: Read(LIVE, "main", "abc123abc123"), KNOWN_BAD: Read(UNREADABLE)})
try:
    run_controls(both_ok)
    check("controls pass when instrument discriminates", True, True)
except ControlFailure as exc:  # pragma: no cover
    check("controls pass when instrument discriminates", f"raised {exc}", True)

for name, mapping in (
    ("known-good dead -> refuse", {KNOWN_GOOD: Read(UNREADABLE), KNOWN_BAD: Read(UNREADABLE)}),
    ("known-bad LIVE -> refuse", {KNOWN_GOOD: Read(LIVE, "main", "a" * 12),
                                  KNOWN_BAD: Read(LIVE, "main", "b" * 12)}),
):
    try:
        run_controls(fake(mapping))
        check(name, "no raise", "ControlFailure")
    except ControlFailure:
        check(name, True, True)

# a count is unreachable while the controls fail
try:
    sweep(["a/b"], fake({KNOWN_GOOD: Read(UNREADABLE), KNOWN_BAD: Read(UNREADABLE)}))
    check("sweep refuses a count behind failing controls", "returned", "ControlFailure")
except ControlFailure:
    check("sweep refuses a count behind failing controls", True, True)

passed = sum(1 for _, ok, _ in CASES if ok)
for name, ok, detail in CASES:
    print(f"{'ok  ' if ok else 'FAIL'} {name}" + ("" if ok else f" -- {detail}"))
print(f"{passed}/{len(CASES)} controls green")
sys.exit(0 if passed == len(CASES) else 1)
