"""`ACTION KF`, second half — re-run each offender and measure whether its dated
evidence file still equals the bytes committed at `HEAD`.

For each (instrument, script, dated_target) row produced by `dated_write.py`:
  1. hash the committed bytes of every dated file in that instrument;
  2. run the script from inside its own directory, with a timeout;
  3. hash again and report CHANGED / SAME / ABSENT per file;
  4. restore the instrument to `HEAD` unconditionally, so the measurement
     cannot itself destroy the evidence it is measuring.

Usage: python3 -I rerun_dated.py <repo-root> <instrument> [<instrument> ...]
"""

from __future__ import annotations

import hashlib
import subprocess
import sys
from pathlib import Path

TIMEOUT = 240


def digests(directory: Path) -> dict[str, str]:
    out = {}
    for path in sorted(directory.rglob("*")):
        if path.is_file() and any(
            part.count("-") >= 2 and part[:4].isdigit() for part in path.name.split(".")
        ):
            out[str(path.relative_to(directory))] = hashlib.sha256(path.read_bytes()).hexdigest()
    return out


def main() -> int:
    root = Path(sys.argv[1]).resolve()
    print("instrument\tscript\trc\tfile\tverdict")
    for name in sys.argv[2:]:
        directory = root / "compose" / "code" / name
        scripts = sorted(
            p
            for p in directory.iterdir()
            if p.suffix in {".py", ".sh"} and not p.name.startswith("test_")
        )
        before = digests(directory)
        for script in scripts:
            argv = (
                ["python3", "-I", script.name]
                if script.suffix == ".py"
                else ["bash", script.name]
            )
            try:
                proc = subprocess.run(
                    argv,
                    cwd=directory,
                    capture_output=True,
                    text=True,
                    timeout=TIMEOUT,
                )
                rc = str(proc.returncode)
            except subprocess.TimeoutExpired:
                rc = "timeout"
            except OSError as error:
                rc = "oserror:%s" % error.errno
            after = digests(directory)
            print("\t".join((name, script.name, rc, "-", "RAN")))
            for key in sorted(set(before) | set(after)):
                if key not in after:
                    verdict = "DELETED"
                elif key not in before:
                    verdict = "CREATED"
                elif before[key] != after[key]:
                    verdict = "CHANGED"
                else:
                    continue
                print("\t".join((name, script.name, rc, key, verdict)))
            subprocess.run(
                ["git", "-C", str(root), "checkout", "--", "compose/code/%s" % name],
                capture_output=True,
            )
            subprocess.run(
                ["git", "-C", str(root), "clean", "-fdq", "compose/code/%s" % name],
                capture_output=True,
            )
    return 0


if __name__ == "__main__":
    sys.exit(main())
