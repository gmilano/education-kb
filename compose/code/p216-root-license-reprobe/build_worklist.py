#!/usr/bin/env python3
"""Build ACTION QH's worklist: the 94 ABSENT rows of p211 minus the 25 p215 recovered.

Inputs are this KB's own evidence files, so the worklist is reproducible from disk:
  evidence/ungranted-after-18-forms.2026-10-15-p211.tsv   (the 94)
  evidence/lstree-grant-recovery.2026-10-15-p215.tsv      (the 25)
"""

import sys

EV = "evidence/"
ABSENT = EV + "ungranted-after-18-forms.2026-10-15-p211.tsv"
RECOVERED = EV + "lstree-grant-recovery.2026-10-15-p215.tsv"


def rows(path, col=0):
    out = []
    with open(path) as fh:
        for line in fh:
            line = line.strip()
            if not line or line.startswith("#") or line == "repo":
                continue
            field = line.split("\t")[col].strip()
            if field and "/" in field:
                out.append(field)
    return out


def main():
    absent = sorted(set(rows(ABSENT)))
    recovered = set(rows(RECOVERED))
    remaining = [r for r in absent if r not in recovered]
    sys.stderr.write(
        f"absent={len(absent)} recovered_listed={len(recovered)} remaining={len(remaining)}\n"
    )
    for r in remaining:
        print(r)


if __name__ == "__main__":
    main()
