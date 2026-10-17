#!/usr/bin/env python3
"""p278 — the OFFLINE half: p121's hand-typed verdicts, pinned to the classifier.

WHAT THIS GATE IS FOR.

`p121` published a ten-row contradiction table in `repos/trending.md` with a DIRECTION typed
per row.  Typed verdicts rot in two ways a row-count gate cannot see:

  1. a later pass re-reads a payload, updates the family cell, and leaves the direction cell
     saying what it said before;
  2. the direction was wrong when it was typed.

🔴 **Both are live on this base.**  `p278`'s sweep found `cccareers/open-source-curriculum`'s
payload is **CC-BY-NC-SA-4.0** -- NON-COMMERCIAL -- while `p121`'s own row glosses the
committed file as *"**CC-BY** family"* and types the direction *"permissive over
attribution-share"*.  **Attribution-share reads as "ship it with credit"; NC forbids the
deliverable outright.**  A curriculum repository is exactly the kind of row a studio reuses,
so that gloss is the expensive kind of wrong.

So the gate re-derives each row's verdict from its two FAMILY cells through
`direction.py` -- the same classifier the online sweep uses -- and fails when the published
direction disagrees.  No network.

🔵 It also fails when a row cannot be PARSED.  A gate that silently skips rows it no longer
recognises reports green on a table whose shape changed, which is `p252`'s silent-zero class
(`ACTION XR`) and `p277`'s deleted-boundary class in one.  Unparseable is RED, not skipped.
"""
import argparse
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from direction import direction, tier_of, UNPLACEABLE_BY_DESIGN  # noqa: E402

# p121's prose directions -> this instrument's verdict tokens.
# The mapping is deliberately MANY-TO-ONE: p121 named the destination tier in prose
# ("over copyleft", "over nothing"), which the tier table now derives, so every
# overstatement collapses to one verdict and the tier carries the detail.
PROSE_TO_VERDICT = {
    "permissive over proprietary": "MANIFEST-OVERSTATES",
    "permissive over network copyleft": "MANIFEST-OVERSTATES",
    "permissive over copyleft": "MANIFEST-OVERSTATES",
    "permissive over attribution-share": "MANIFEST-OVERSTATES",
    "permissive over nothing": "MANIFEST-OVERSTATES",
    # 🟢 Added at p278 when the gate REFUSED the correction p278 itself made: the cccareers
    # row's direction was retyped as "permissive over non-commercial" and this table did not
    # know the phrase, so the gate failed the row.  That is the gate working -- a new
    # direction phrase must be declared, not silently accepted -- and it is recorded here
    # because the alternative (quietly widening the match to anything starting "permissive
    # over") would have made the vocabulary unbounded and the gate decorative.
    "permissive over non-commercial": "MANIFEST-OVERSTATES",
    "permissive over billed": "MANIFEST-OVERSTATES",
    "both permissive, wrong name": "SAME-TIER-WRONG-NAME",
    "restrictive over permissive": "MANIFEST-UNDERSTATES",
}

# Family names as the shelves SPELL them in a cell, mapped onto classifier tokens.  A shelf
# cell is prose with emphasis, so the spelling is not always the token.
CELL_FAMILY = [
    (r"\bAGPL-?3(\.0)?\b", "AGPL-3.0"),
    (r"\bGPL-?3(\.0)?\b", "GPL-3.0"),
    (r"\bGPL-?2(\.0)?\b", "GPL-2.0"),
    (r"\bLGPL-?3(\.0)?\b", "LGPL-3.0"),
    (r"\bLGPL-?2\.1\b", "LGPL-2.1"),
    (r"\bMPL-?2(\.0)?\b", "MPL-2.0"),
    (r"\bApache-?2(\.0)?\b", "Apache-2.0"),
    (r"\bBSD\b", "BSD"),
    (r"\bISC\b", "ISC"),
    (r"\bMIT\b", "MIT"),
    # NC/ND spellings MUST be tested before the bare CC-BY arm, or a non-commercial grant
    # reads as attribution-share -- the exact error this gate was built after finding.
    (r"CC-BY-NC-SA", "CC-BY-NC-SA-4.0"),
    (r"CC-BY-NC", "CC-BY-NC-4.0"),
    (r"CC-BY-SA", "CC-BY-SA-4.0"),
    (r"\bCC-BY\b", "CC-BY-4.0"),
    (r"CC-?BY family", "CC-UNSPECIFIED"),
    (r"Fair.?[Cc]ode", "FAIRCODE"),
    (r"BUSL", "BUSL-1.1"),
    (r"no licence file|no license file|author claim only|none\b", "NONE"),
]


def family_in_cell(cell):
    for pat, fam in CELL_FAMILY:
        if re.search(pat, cell, re.I):
            return fam
    return None


def find_table(text):
    """p121's contradiction table, located by its OWN header row, not by a line number.

    Anchored on the header's distinctive cell names so the gate survives the file growing
    above it -- `repos/trending.md` is append-only and every pass adds sections at the top.
    """
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if ("manifest says" in line.lower() and "direction" in line.lower()
                and line.startswith("|")):
            rows = []
            for row in lines[i + 2:]:          # skip the |---| separator
                if not row.startswith("|"):
                    break
                rows.append(row)
            return i + 1, rows
    return None, []


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    args = ap.parse_args()
    shelf = os.path.join(args.root, "repos/trending.md")
    if not os.path.exists(shelf):
        print(f"🔴 {shelf} not found")
        return 1
    text = open(shelf, encoding="utf-8").read()

    header_line, rows = find_table(text)
    if not rows:
        print("🔴 p121's contradiction table was NOT FOUND in repos/trending.md.\n"
              "   A gate that cannot find its subject must FAIL, not pass: this is the "
              "shape p277's deleted tier boundary hid in.")
        return 1

    failures, checked = [], 0
    print(f"# p278 conflict gate — p121's table at repos/trending.md:{header_line}, "
          f"{len(rows)} rows")
    for row in rows:
        cells = [c.strip() for c in row.strip().strip("|").split("|")]
        if len(cells) < 5:
            failures.append(f"UNPARSEABLE (want >=5 cells, got {len(cells)}): {row[:90]}")
            continue
        addr, _mpath, m_cell, p_cell, dir_cell = cells[0], cells[1], cells[2], cells[3], cells[4]
        m_fam, p_fam = family_in_cell(m_cell), family_in_cell(p_cell)
        if m_fam is None or p_fam is None:
            which = "manifest" if m_fam is None else "payload"
            failures.append(f"UNPARSEABLE {which} family in {addr[:48]}: "
                            f"{(m_cell if m_fam is None else p_cell)[:60]}")
            continue
        # 🔴 The first cut stripped with `[^a-z, ]`, which eats the HYPHEN -- so
        # "permissive over attribution-share" normalised to "attributionshare" and matched
        # nothing, and the gate reported UNKNOWN DIRECTION PROSE on a row whose prose was
        # perfectly well-formed.  A gate that mangles its own input reports a defect in the
        # shelf that is really a defect in the gate, which is the most expensive kind of
        # false positive this base can publish.  The hyphen is load-bearing vocabulary here.
        prose = re.sub(r"[^a-z, -]", "", dir_cell.lower()).strip()
        expected = None
        for key, verdict in PROSE_TO_VERDICT.items():
            if key in prose:
                expected = verdict
                break
        if expected is None:
            failures.append(f"UNKNOWN DIRECTION PROSE in {addr[:48]}: {dir_cell[:60]}")
            continue
        got = direction(m_fam, p_fam)[0]
        checked += 1
        if got != expected:
            # An UNPLACEABLE derivation is a DIFFERENT failure from a wrong direction: it
            # means the cell names a family nobody has classified, so say which it is.
            why = ("the payload cell names an unclassified family"
                   if p_fam in UNPLACEABLE_BY_DESIGN or tier_of(p_fam) is None
                   else "the published direction disagrees with the families in its own row")
            failures.append(
                f"{addr[:56]}\n       manifest={m_fam} payload={p_fam}\n"
                f"       published={expected} derived={got}\n       → {why}")

    if failures:
        print(f"# 🔴 {len(failures)} FAILING of {len(rows)} rows ({checked} fully derived):")
        for f in failures:
            print("    " + f)
        return 1
    print(f"# 🟢 PASS — {checked} rows, every published direction re-derived from its own "
          "family cells")
    return 0


if __name__ == "__main__":
    sys.exit(main())
