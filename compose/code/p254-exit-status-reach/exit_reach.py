#!/usr/bin/env python3
"""p254 — `ACTION XZ` (registered by p253): does a FAILING STEP reach a SUCCESS MESSAGE?

p253 found `gate-offline` printing `ALL OFFLINE LICENCE CONTROLS PASS` with a failing suite,
for all 31 steps, and registered XZ to ask the same question of *everything else this base
runs*: `make hooks`, `gate-online`, `gate-mit-tier`, `reach`, `status`, `exists`, `index`,
`carried`, `claims`.

🔴 The answer, measured rather than read, is worse than p253's own finding:

    claims:  @... carried_index.py claims "$(TOKEN)" . || true

`carried_index.py claims` returns **1 exactly when the shelves ALREADY claim the token** —
exit 1 IS the STOP signal, and it is the whole purpose of the recipe, whose own `##` comment
reads "THE GATE: run before publishing any 'there is no X'".  `|| true` destroys it.  The
verdict still PRINTS, so a human reading the terminal is fine and a hook, a CI step or
`make claims TOKEN=x && publish` is not.

🔵 The class, stated so it outlives this instance: p253's defect was a gate that could not
hear its controls.  This one is a gate that cannot speak.  Both are the same shape —
**a signal exists, is correct, and nothing consumes it** — which is the property p253's
trends shelf named as this base's recurring failure mode.

What this file grades, per recipe line of every target in the Makefile:

    GUARDED        ends in `|| exit 1` — a failure aborts the recipe            (can fail)
    CONSUMED       a plain command; make itself consumes a non-zero status      (can fail)
    SWALLOWED-TRUE `|| true` — the status is discarded by construction          (CANNOT fail)
    SWALLOWED-PIPE a pipeline whose LAST element is not the asserting command   (CANNOT fail)
    SWALLOWED-SUBST  the command runs only inside `$(...)`, inside an `echo`    (CANNOT fail)
    IGNORED-PREFIX `-cmd` — make is told to ignore the status                   (CANNOT fail)
    INERT          `echo`, `cd -`, a comment: asserts nothing, so nothing to lose

A target is CONTRACTED when it publishes a verdict another step may act on.  For those,
`--verify` fails if ANY line is in a SWALLOWED/IGNORED state.  A target that only PRINTS for
a human (`status`, `reach`) is UNCONTRACTED and is censused, not enforced: recorded so a
later pass does not read its absence from the contract as an oversight.
"""
import re
import subprocess
import sys

# Targets that publish a verdict something else may act on.  `index` is deliberately NOT
# here: it prints three counts for a human and its own `main` swallows BrokenPipeError by
# design, so `| head -3` is correct usage rather than a defect.
CONTRACTED = {"hooks", "gate-offline", "claims", "carried", "exists"}

SWALLOWED = {"SWALLOWED-TRUE", "SWALLOWED-PIPE", "SWALLOWED-SUBST", "IGNORED-PREFIX"}

# The last element of a pipeline, when it is one of these, is a FORMATTER: it exits 0
# whatever the command feeding it did, so the pipeline's status says nothing about the
# assertion.  `grep` is absent on purpose — a trailing `grep -q` IS an assertion.
FORMATTERS = {"head", "tail", "cut", "sort", "uniq", "tr", "wc", "column", "tee", "fmt",
              "nl", "cat", "awk", "sed"}

RECIPE = re.compile(r"^\t")
TARGET = re.compile(r"^([A-Za-z0-9_.-]+):")


def _strip(line):
    """Recipe line -> the shell text, minus the tab, the `@`/`-` prefixes and continuations."""
    body = line[1:].rstrip("\n")
    body = body.rstrip("\\").strip()
    prefix = ""
    while body[:1] in ("@", "-", "+"):
        prefix += body[0]
        body = body[1:].lstrip()
    return prefix, body


def grade_command(cmd):
    """Grade ONE shell command (already split on `;`)."""
    c = cmd.strip()
    if not c:
        return None
    if c.startswith("#"):
        return "INERT"
    if re.match(r"^(echo|printf|cd -|true|:)\b", c) and "$(" not in c:
        return "INERT"
    if re.search(r"\|\|\s*true\s*$", c):
        return "SWALLOWED-TRUE"
    if re.search(r"\|\|\s*exit\s+\d+\s*$", c):
        return "GUARDED"
    # a command that only ever runs inside `$(...)` within an echo/printf
    if re.match(r"^(echo|printf)\b", c) and "$(" in c:
        return "SWALLOWED-SUBST"
    if "|" in c:
        # The pipeline's status is its LAST element's, unless pipefail is set.  But WHOSE
        # status is lost decides whether that matters, and the first measurement of this
        # instrument got it wrong: it flagged `exists`, whose closing
        # `awk … | sort | uniq -c` only formats a file that an already-CONSUMED step wrote.
        # Silencing a formatter costs nothing; silencing an INSTRUMENT costs the verdict.
        parts = [p.strip() for p in c.split("|")]
        last = parts[-1].split()[0] if parts[-1].split() else ""
        first = parts[0].split()[0] if parts[0].split() else ""
        if last.lstrip("$(").strip("()") in FORMATTERS:
            asserts = bool(re.search(r"\$\(PY\)|python3?\b|\.py\b|\.sh\b|bash\b", parts[0]))
            return "SWALLOWED-PIPE" if asserts else "REPORT"
        del first
    return "CONSUMED"


def grade_line(line):
    """Recipe line -> [(command, grade)].  An `&&` list is graded as ONE command: p253
    established that bash exempts every element but the last from errexit, so the guard at
    the end is what decides the whole list."""
    prefix, body = _strip(line)
    out = []
    for cmd in re.split(r";(?![^(]*\))", body):
        g = grade_command(cmd)
        if g is None:
            continue
        if "-" in prefix and g not in ("INERT",):
            g = "IGNORED-PREFIX"
        out.append((cmd.strip(), g))
    return out


def audit(path="Makefile"):
    """-> {target: [(command, grade)]}"""
    with open(path, encoding="utf-8") as fh:
        lines = fh.readlines()
    targets, current = {}, None
    for line in lines:
        if RECIPE.match(line):
            if current:
                targets[current].extend(grade_line(line))
            continue
        m = TARGET.match(line)
        if m and not line.startswith(".PHONY"):
            current = m.group(1)
            targets.setdefault(current, [])
    return targets


def violations(targets):
    """The CONTRACTED targets that carry a line which cannot fail."""
    bad = []
    for name in sorted(targets):
        if name not in CONTRACTED:
            continue
        for cmd, grade in targets[name]:
            if grade in SWALLOWED:
                bad.append((name, grade, cmd))
    return bad


def main(argv):
    path = "Makefile"
    for a in argv[1:]:
        if not a.startswith("--"):
            path = a
    targets = audit(path)

    if "--verify" in argv:
        bad = violations(targets)
        for name, grade, cmd in bad:
            print(f"🔴 {name}\t{grade}\t{cmd[:90]}", file=sys.stderr)
        if bad:
            print(f"🔴 {len(bad)} contracted recipe line(s) cannot fail", file=sys.stderr)
            return 1
        print(f"OK\t{len(CONTRACTED)} contracted targets, every line can fail")
        return 0

    census = {}
    for name in sorted(targets):
        for cmd, grade in targets[name]:
            census[grade] = census.get(grade, 0) + 1
        grades = sorted({g for _, g in targets[name]})
        mark = "CONTRACTED" if name in CONTRACTED else "uncontracted"
        print(f"{name}\t{mark}\t{len(targets[name])}\t{','.join(grades)}")
    print("# census\t" + "\t".join(f"{k}={v}" for k, v in sorted(census.items())))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
