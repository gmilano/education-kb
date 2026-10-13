"""Second iteration of `suite_sweep.py`'s classifier, run ONLY over the rows the
first iteration could not name. The first iteration's `other` bucket was 88 rows;
this one re-runs each and applies two cue classes the first one lacked:

  usage, shell shapes   - `$1: unbound variable`, `${1:?message}`, `line N: 1: label`
                          A POSIX shell script that refuses to run without its
                          first positional argument prints none of the cues a
                          Python argparse exit prints.
  assert, tally shapes  - `N/M controls passed` with N < M, `N/M` with N < M.
                          A control suite that reports its own score in prose
                          fails a sweep looking for the word FAILED.

Both corrections move rows OUT of `other`, and one of them (`assert`) moves a row
into the only class that means the instrument disagrees with the repository — so
the correction runs in both directions and is not merely flattering.
"""
from __future__ import annotations
import re, subprocess, sys
from pathlib import Path

SHELL_USAGE = ("unbound variable", "parameter null or not set")
LINE_LABEL = re.compile(r"line \d+: \d+: \S")
TALLY = re.compile(r"\b(\d+)\s*/\s*(\d+)\b")

def reclassify(out: str, err: str) -> str:
    text = err + "\n" + out
    if any(c in text for c in SHELL_USAGE) or LINE_LABEL.search(text):
        return "usage"
    for m in TALLY.finditer(text):
        got, want = int(m.group(1)), int(m.group(2))
        if want and got < want:
            return "assert"
    return "other"

def main() -> int:
    root = Path(sys.argv[1])
    print("instrument\tscript\tkind\trc\tverdict_1\tverdict_2")
    for line in Path(sys.argv[2]).read_text().splitlines():
        inst, script, kind, rc, verdict = line.split("\t")
        if verdict != "other":
            continue
        path = root / inst / script
        argv = ["python3", path.name] if path.suffix == ".py" else ["bash", path.name]
        try:
            proc = subprocess.run(argv, cwd=path.parent, capture_output=True,
                                  text=True, timeout=12)
            out, err = proc.stdout, proc.stderr
        except subprocess.TimeoutExpired as exc:
            out, err = exc.stdout or "", exc.stderr or ""
        if isinstance(out, bytes): out = out.decode("utf-8", "replace")
        if isinstance(err, bytes): err = err.decode("utf-8", "replace")
        print(f"{inst}\t{script}\t{kind}\t{rc}\t{verdict}\t{reclassify(out, err)}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
