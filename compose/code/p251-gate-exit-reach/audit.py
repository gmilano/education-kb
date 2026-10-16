"""`ACTION XM`'s runner: the exit-code reachability audit over `make hooks`.

    python3 audit.py <repo-root>            # TSV on stdout

One row per command in the `gate-offline` recipe.  Columns:
  line, instrument, suite, invocation, stdout_suppressed, stderr_suppressed,
  layer1_failure_capable, layer2_signal, silent_zero, collected, floor, verdict
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gate_reach import classify_recipe_line, suite_signal, silent_zero, collected_tests, FLOORS

def recipe(makefile_text, target="gate-offline"):
    lines = makefile_text.splitlines()
    out, inside = [], False
    for i, raw in enumerate(lines, 1):
        if re.match(r"^%s:" % re.escape(target), raw):
            inside = True
            continue
        if inside:
            if raw and not raw.startswith("\t"):
                break
            body = raw.lstrip("\t").lstrip("@")
            if body.strip() and not body.strip().startswith("echo "):
                out.append((i, body))
    return out

# two invocation shapes in this gate: `cd <instr> && <runner> <suite>` and
# `<runner> -I compose/code/<instr>/<suite>`.  A single lazy pattern read the
# flag `-I` as the instrument name (measured at p251), so both are explicit.
SUITE_PATH = re.compile(r"compose/code/([A-Za-z0-9._-]+)/((?:test_|lazy_lint)[A-Za-z0-9._-]*\.(?:py|sh))")
SUITE_CD = re.compile(r"cd\s+compose/code/([A-Za-z0-9._/-]+?)\s+&&.*?((?:test_|lazy_lint)[A-Za-z0-9._-]*\.(?:py|sh))")

def main(root):
    mk = open(os.path.join(root, "Makefile"), encoding="utf-8").read()
    rows = []
    for lineno, body in recipe(mk):
        if body.strip() in ("cd - >/dev/null;", "cd - >/dev/null; \\", "set -e;", "set -e; \\"):
            continue
        rec = classify_recipe_line(body)
        m = SUITE_PATH.search(body) or SUITE_CD.search(body)
        instr, suite = (m.group(1), m.group(2)) if m else ("-", "-")
        path = os.path.join(root, "compose", "code", instr, suite) if instr != "-" else ""
        src = open(path, encoding="utf-8").read() if path and os.path.exists(path) else ""
        lang = "shell" if suite.endswith(".sh") else "python"
        sig = suite_signal(src, lang=lang) if src else "NO-SUITE"
        rel = "%s/%s" % (instr, suite)
        floor = FLOORS.get(rel, "")
        coll = collected_tests(src) if src else ""
        sz = silent_zero(sig)
        verdict = ("SWALLOWED" if not rec["failure_capable"]
                   else "SILENT-ZERO-UNLESS-PINNED" if sz and not floor
                   else "PINNED" if sz and floor
                   else "FAILURE-CAPABLE" if sig == "EXPLICIT-EXIT"
                   else "NO-SIGNAL" if sig == "NONE" else "NOT-A-SUITE")
        rows.append([str(lineno), instr, suite, body.strip().rstrip("\\").strip()[:70],
                     "yes" if rec["stdout_suppressed"] else "no",
                     "yes" if rec["stderr_suppressed"] else "no",
                     "yes" if rec["failure_capable"] else "no",
                     sig, "yes" if sz else "no", str(coll), str(floor), verdict])
    print("\t".join(["makefile_line", "instrument", "suite", "command", "stdout_suppressed",
                     "stderr_suppressed", "layer1_failure_capable", "layer2_signal",
                     "silent_zero", "collected_tests", "pinned_floor", "verdict"]))
    for r in rows:
        print("\t".join(r))
    return rows

if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else ".")
