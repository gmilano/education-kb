"""`ACTION KF` — detect instruments that WRITE a dated evidence file under a
date that is hardcoded in the script rather than taken from the clock.

The rule, stated so it can be argued with:

A script is an OFFENDER when BOTH hold.

1. It WRITES to a path whose basename carries an ISO date — `*.YYYY-MM-DD*.(tsv|csv|json|md|txt)`.
   A write is a shell redirection (`>`, `>>`, `tee`) or a Python write
   (`open(..., "w"|"a")`, `.write_text(`, `.write_bytes(`, `csv.writer` onto an
   opened handle). Merely READING or naming such a path is not a write: a
   script that cites yesterday's evidence is doing the right thing.
2. The date in that written path is a LITERAL in the script.

The rule's BOUNDARY, stated because the suite asserts it rather than assuming
it: a path assembled from the clock (`result.$STAMP.tsv`, `f"x.{today}.tsv"`)
carries no literal date, so condition 1 never matches and such a script is out
of scope entirely — it cannot overwrite a dated record, because every run names
a different file.

The `clock` classification therefore covers only the AMBIGUOUS middle: a script
that writes a literal dated path AND also calls the clock (`date +%F`,
`datetime.now`, `date.today`, `strftime`, `utcnow`) somewhere. The clock call
may or may not reach that path, and this gate resolves the ambiguity in favour
of the script — over-reporting an offender is the one error it must not make,
because its output drives a repair.

Why the distinction matters: an offender overwrites, on every later run, the
file that a published claim cites. The record becomes a LATEST-RUN artefact,
and "the value committed at pass N" stops being checkable from the file.

Usage:
    python3 -I dated_write.py <root>            # TSV to stdout
    python3 -I dated_write.py <root> --summary
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

DATED = r"[A-Za-z0-9_.-]*\.(?:19|20)[0-9]{2}-[0-9]{2}-[0-9]{2}[A-Za-z0-9_.-]*\.(?:tsv|csv|json|md|txt)"
CLOCK = re.compile(r"date\s+[\"']?\+|datetime\.now|date\.today|strftime|utcnow|\$\(date|time\.time")

# A dated name appearing immediately after a shell redirection or inside a
# Python write call. Both forms are deliberately narrow: a bare mention of the
# filename does not match.
SH_WRITE = re.compile(r"(?:>>?|\|\s*tee(?:\s+-a)?)\s+[\"']?(?:[^\s\"'|;]*/)?(" + DATED + r")")
PY_WRITE = re.compile(
    r"(?:open\(\s*[^)]*?(" + DATED + r")[^)]*?[\"'][wa]"
    r"|(" + DATED + r")[\"'][^)]*?\)\s*\.\s*write_(?:text|bytes)\("
    r"|write_(?:text|bytes)\(\s*[^)]*(" + DATED + r")"
    r")"
)
# `p = DIR / "x.2026-10-13.tsv"` followed later by `p.write_text(` is the
# commonest real shape, so a variable bound to a dated literal that is then
# written counts too.
PY_BIND = re.compile(r"(\w+)\s*=\s*[^\n]*?[\"'](" + DATED + r")[\"']")


# This gate's own positive controls are deliberate offenders. Counting them when
# sweeping the repository would inflate every figure the gate publishes, so they
# are excluded by an explicit path rather than by a `fixtures/` heuristic — a
# blanket rule would hide real offenders in other instruments' fixture trees.
# The gate's own directory is excluded whole, not just its fixtures: its rule
# prose, its tests and its controls all quote dated filenames on purpose, so a
# gate that measured itself would report its own documentation as a defect.
SELF_FIXTURES = ("p175-dated-evidence-gate/",)


def offenders(root: Path, *, exclude_self: bool = True):
    rows = []
    for path in sorted(root.rglob("*")):
        if path.suffix not in {".py", ".sh"} or not path.is_file():
            continue
        if exclude_self and any(marker in path.as_posix() for marker in SELF_FIXTURES):
            continue
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        written: set[str] = set()
        for match in SH_WRITE.finditer(text):
            written.add(match.group(1))
        for match in PY_WRITE.finditer(text):
            written.add(next(g for g in match.groups() if g))
        for name, dated in PY_BIND.findall(text):
            if re.search(r"\b" + re.escape(name) + r"\s*\.\s*write_(?:text|bytes)\(", text):
                written.add(dated)
            elif re.search(r"open\(\s*" + re.escape(name) + r"\s*,\s*[\"'][wa]", text):
                written.add(dated)
        if not written:
            continue
        clocked = bool(CLOCK.search(text))
        for name in sorted(written):
            rows.append(
                (
                    str(path.relative_to(root)),
                    name,
                    "clock" if clocked else "hardcoded",
                )
            )
    return rows


def main() -> int:
    root = Path(sys.argv[1]).resolve()
    rows = offenders(root)
    hard = [r for r in rows if r[2] == "hardcoded"]
    instruments = sorted({r[0].split("/")[0] for r in hard})
    if "--summary" in sys.argv:
        print("rows\t%d" % len(rows))
        print("hardcoded_writes\t%d" % len(hard))
        print("instruments\t%d" % len(instruments))
        for name in instruments:
            print("instrument\t%s" % name)
        return 0
    print("script\tdated_target\tdate_source")
    for row in rows:
        print("\t".join(row))
    return 0


if __name__ == "__main__":
    sys.exit(main())
