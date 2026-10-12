"""p148-channel-agreement -- `ACTION ER`: the institution channel on the clone tier.

`p147-npm-region` placed **2 of 8** npm rows by institution evidence and narrowed `T59`.
`ACTION ER` moves that probe to the **44 connector clones**, where `P144-V` found its
original instance, and tests it against the channel this KB has been placing rows with:

> 🔴 *Refuted if it disagrees with any region this KB has already placed on the
> commit-timezone channel.*

🔵 **The two channels answer different questions** and `P144-V` already ruled on precedence
-- *"the institution is where it deploys; the author is wherever they were sitting"* -- so a
disagreement is not automatically an error. What it is, is a thing this KB has to resolve by
name rather than by citing the rule.

## What this module does

1. reads `p147-npm-region`'s placement for each clone (the institution channel);
2. reads `p142-origin-at-scale`'s `region` for the same subject (the offset channel);
3. classifies each row into one of six states, so that "both placed and they agree" is
   never reported in the same bucket as "only one channel could answer".

| state | meaning |
|---|---|
| `AGREE` | both channels placed the row, same region |
| `DISAGREE` | both placed it, different regions -- 🔴 **the falsifier's population** |
| `INSTITUTION_ONLY` | the offset channel declined; the institution channel placed it |
| `OFFSET_ONLY` | the institution channel found nothing; the offset channel placed it |
| `NEITHER` | no channel placed it |
| `INSTITUTION_CONFLICT` | the institution channel found hosts in 2+ regions |

🔵 **`INSTITUTION_ONLY` is the result worth having**: it is net new coverage on the axis
this KB is judged on, and it costs nothing in contradictions.

    python3 channel_agreement.py <institution.tsv> <offset.tsv>
    python3 test_channel_agreement.py    # 11 tests, authored fixtures, offline
"""

import csv
import sys

REGIONS = {"North America", "EMEA", "APAC", "LATAM"}
# Values either channel uses to mean "I could not place this", as distinct from a region.
DECLINED = {"UNPLACED", "UNMAPPED", "AMBIGUOUS", "-", ""}


def norm_subject(s):
    """`owner/repo` and `owner_repo` are the same subject across the two files."""
    return s.replace("/", "_").strip()


def load(path, subject_col, region_col):
    out = {}
    with open(path, encoding="utf-8") as fh:
        # 🟢 Skip blank lines as well as comments: a leading blank line makes
        # `DictReader` take the empty line as the header and silently return no
        # rows -- the exact "a verdict over nothing" shape `T64` names.
        lines = (l for l in fh if l.strip() and not l.startswith("#"))
        for row in csv.DictReader(lines, delimiter="\t"):
            if not row.get(subject_col):
                continue
            out[norm_subject(row[subject_col])] = row
    return out


def classify(inst_region, off_region):
    inst_placed = inst_region in REGIONS
    off_placed = off_region in REGIONS
    if inst_region == "CONFLICT":
        return "INSTITUTION_CONFLICT"
    if inst_placed and off_placed:
        return "AGREE" if inst_region == off_region else "DISAGREE"
    if inst_placed:
        return "INSTITUTION_ONLY"
    if off_placed:
        return "OFFSET_ONLY"
    return "NEITHER"


def compare(inst_path, off_path):
    inst = load(inst_path, "subject", "region")
    off = load(off_path, "subject", "region")
    rows, counts = [], {}
    for subj in sorted(set(inst) & set(off)):
        ir = inst[subj].get("region", "-").strip()
        orr = off[subj].get("region", "-").strip()
        state = classify(ir, orr)
        counts[state] = counts.get(state, 0) + 1
        rows.append(dict(subject=subj, institution=ir, offset=orr, state=state,
                         host=inst[subj].get("host", "-"),
                         how=inst[subj].get("how", "-"),
                         where=inst[subj].get("where", "-")))
    return rows, counts, sorted(set(inst) ^ set(off))


COLS = ["subject", "institution", "offset", "state", "host", "how", "where"]


def main(argv):
    if len(argv) < 3:
        print(__doc__)
        return 2
    rows, counts, only_one = compare(argv[1], argv[2])
    print("# population (in both files): %d" % len(rows))
    for k in ("AGREE", "DISAGREE", "INSTITUTION_ONLY", "OFFSET_ONLY",
              "INSTITUTION_CONFLICT", "NEITHER"):
        print("# %-22s %d" % (k, counts.get(k, 0)))
    if only_one:
        print("# in one file only: %s" % ", ".join(only_one))
    print("#")
    print("# ACTION ER falsifier -- DISAGREE count: %d  -> %s"
          % (counts.get("DISAGREE", 0),
             "REFUTED" if counts.get("DISAGREE", 0) else "NOT REFUTED"))
    print("\t".join(COLS))
    for r in rows:
        print("\t".join(str(r[c]) for c in COLS))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
