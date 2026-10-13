"""`ACTION KL` — run every instrument in `compose/code/` and record its EXIT CODE,
then say WHY each non-zero one failed, because p175's `9`/`28` did not.

The rule, stated before it is coded so it can be argued with:

  A script is RUN from inside its own instrument directory, with no arguments,
  under a timeout. Its exit code is recorded verbatim. A non-zero exit is then
  classified by what the script itself printed, into one of:

    usage    - the script requires CLI arguments or an input path and said so
               (argparse exit 2, "usage:", "Usage:", "missing argument",
               IndexError on sys.argv). NOT a broken instrument: it is an
               instrument invoked wrongly by this sweep.
    network  - a name that does not resolve, a refused connect, an HTTP error,
               a proxy denial. NOT a broken instrument here: it is a channel
               this container denies (T267).
    input    - an input file or fixture the instrument expects is absent
               (FileNotFoundError, "No such file or directory") AND no argv
               complaint was printed.
    assert   - the instrument RAN and its own assertions or gate failed
               (AssertionError, unittest "FAILED", a non-zero gate verdict).
               This is the only class that means the instrument disagrees
               with the repository.
    crash    - SyntaxError, ImportError, NameError, TypeError, AttributeError:
               the instrument cannot execute at all. Broken.
    timeout  - did not finish inside the limit.
    other    - non-zero and none of the above matched.

  The classification reads stderr first, then stdout. It is ordered: `usage`
  before `input`, because a script that prints a usage line AND a
  FileNotFoundError is an instrument that wanted an argument.

Only `crash`, `assert` and `other` support the sentence "the suite is broken".
`usage` and `network` are properties of how this sweep invokes them and of the
egress policy, and a rate that does not separate them cannot answer `ACTION KL`.

Usage: python3 -I suite_sweep.py <compose/code dir> [--timeout N] [--jobs N]
       python3 -I suite_sweep.py <dir> --summary
       python3 -I suite_sweep.py <dir> --slice=0/4   # every 4th instrument
       python3 -I suite_sweep.py <dir> --no-isolate  # script dir ON sys.path

`--no-isolate` exists because `python3 -I` implies `-P` from Python `3.11`: the
script's own directory is NOT placed on `sys.path`. Every test here that imports
the instrument beside it therefore raises `ModuleNotFoundError` under the exact
command this repository's own READMEs prescribe. The flag makes the two
invocations comparable, and the sweep must report BOTH rates or it is measuring
its own argv (`T271`).

Run it IN PLACE. An instrument that resolves a repository path from its own
location (`T262`, `ACTION KC`) measures something different when it is copied
out of the tree, so a sweep over a copy reports failures the suite does not have.
"""

from __future__ import annotations

import concurrent.futures
import re
import subprocess
import sys
from pathlib import Path

TIMEOUT = 20
JOBS = 8

# Iteration 2 added the two cue classes below. The committed sweep results
# (`result.isolated.*.tsv`, `result.non-isolated.*.tsv`) were produced by
# ITERATION 1 and therefore carry 88 rows labelled `other` that this classifier
# now names; `result.reclassified.*.tsv` is the correction, and the README
# reports both. Nothing is rewritten in place (`P175-A`).
SHELL_USAGE_CUES = (
    "unbound variable",
    "parameter null or not set",
)
LINE_LABEL = re.compile(r"line \d+: \d+: \S")
TALLY = re.compile(r"\b(\d+)\s*/\s*(\d+)\b")

USAGE_CUES = (
    "usage:",
    "Usage:",
    "the following arguments are required",
    "missing argument",
    "IndexError: list index out of range",
    "expected at least",
    "argument",
)
NETWORK_CUES = (
    "Could not resolve host",
    "Name or service not known",
    "Temporary failure in name resolution",
    "NameResolutionError",
    "Connection refused",
    "Failed to connect",
    "CONNECT tunnel failed",
    "HTTP Error",
    "URLError",
    "SSLError",
    "curl: (6)",
    "curl: (7)",
    "curl: (22)",
    "curl: (35)",
    "curl: (56)",
    "403 Forbidden",
    "429",
)
INPUT_CUES = (
    "FileNotFoundError",
    "No such file or directory",
    "cannot open",
    "not found",
)
ASSERT_CUES = (
    "AssertionError",
    "FAILED (",
    "FAIL:",
    "ERROR:",
    "assertion failed",
)
CRASH_CUES = (
    "SyntaxError",
    "ImportError",
    "ModuleNotFoundError",
    "NameError",
    "TypeError",
    "AttributeError",
    "IndentationError",
    "KeyError",
    "ValueError",
    "ZeroDivisionError",
    "command not found",
)


def classify(rc: int, out: str, err: str) -> str:
    if rc == 0:
        return "ok"
    if rc == -9 or rc == 124:
        return "timeout"
    text = err + "\n" + out
    if any(cue in text for cue in SHELL_USAGE_CUES) or LINE_LABEL.search(text):
        return "usage"
    for cues, label in (
        (USAGE_CUES, "usage"),
        (NETWORK_CUES, "network"),
        (ASSERT_CUES, "assert"),
        (CRASH_CUES, "crash"),
        (INPUT_CUES, "input"),
    ):
        if any(cue in text for cue in cues):
            return label
    for match in TALLY.finditer(text):
        got, want = int(match.group(1)), int(match.group(2))
        if want and got < want:
            return "assert"
    return "other"


def scripts_of(directory: Path) -> list[Path]:
    return sorted(
        p
        for p in directory.iterdir()
        if p.is_file() and p.suffix in {".py", ".sh"}
    )


def run_one(script: Path, timeout: int, isolate: bool = True) -> tuple[str, str, str, str, str]:
    if script.suffix == ".py":
        argv = ["python3", "-I", script.name] if isolate else ["python3", script.name]
    else:
        argv = ["bash", script.name]
    kind = "test" if script.name.startswith("test_") else "instrument"
    try:
        proc = subprocess.run(
            argv,
            cwd=script.parent,
            capture_output=True,
            text=True,
            timeout=timeout,
        )
        rc, out, err = proc.returncode, proc.stdout, proc.stderr
    except subprocess.TimeoutExpired as exc:
        rc, out, err = 124, exc.stdout or "", exc.stderr or ""
    except OSError as exc:
        rc, out, err = 127, "", str(exc)
    if isinstance(out, bytes):
        out = out.decode("utf-8", "replace")
    if isinstance(err, bytes):
        err = err.decode("utf-8", "replace")
    return (
        script.parent.name,
        script.name,
        kind,
        str(rc),
        classify(rc, out, err),
    )


def main() -> int:
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    flags = [a for a in sys.argv[1:] if a.startswith("--")]
    root = Path(args[0]).resolve()
    timeout = TIMEOUT
    jobs = JOBS
    for flag in flags:
        if flag.startswith("--timeout="):
            timeout = int(flag.split("=", 1)[1])
        if flag.startswith("--jobs="):
            jobs = int(flag.split("=", 1)[1])

    directories = sorted(p for p in root.iterdir() if p.is_dir())
    for flag in flags:
        if flag.startswith("--slice="):
            index, total = (int(x) for x in flag.split("=", 1)[1].split("/"))
            directories = [d for n, d in enumerate(directories) if n % total == index]
    targets: list[Path] = []
    for directory in directories:
        targets.extend(scripts_of(directory))

    rows: list[tuple[str, str, str, str, str]] = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=jobs) as pool:
        futures = [
            pool.submit(run_one, s, timeout, "--no-isolate" not in flags) for s in targets
        ]
        for future in concurrent.futures.as_completed(futures):
            rows.append(future.result())
    rows.sort()

    if "--summary" in flags:
        print("kind\tverdict\tcount")
        for kind in ("instrument", "test"):
            tally: dict[str, int] = {}
            for row in rows:
                if row[2] == kind:
                    tally[row[4]] = tally.get(row[4], 0) + 1
            for verdict, count in sorted(tally.items(), key=lambda kv: -kv[1]):
                print(f"{kind}\t{verdict}\t{count}")
        return 0

    print("instrument\tscript\tkind\trc\tverdict")
    for row in rows:
        print("\t".join(row))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
