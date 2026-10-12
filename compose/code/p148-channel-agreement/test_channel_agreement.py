"""Tests for p148-channel-agreement. 11 tests, authored fixtures, offline.

Three of these exist because of a defect found while writing the module: a leading
blank line made `csv.DictReader` take the empty line as the header and return **zero
rows**, and the comparison then reported `DISAGREE 0 -> NOT REFUTED` over an empty
population. 🔴 **That is `T64`'s shape in a new place** -- a verdict over nothing, with
the reassuring value -- so the loader now skips blanks and the tests pin it.
"""

import os
import shutil
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import channel_agreement as ca

FAILS = []


def check(name, got, want):
    if got != want:
        FAILS.append("%s\n    got  %r\n    want %r" % (name, got, want))
        print("FAIL %s" % name)
    else:
        print("ok   %s" % name)


def tmptsv(body):
    fd, p = tempfile.mkstemp(suffix=".tsv")
    with os.fdopen(fd, "w", encoding="utf-8") as fh:
        fh.write(body)
    return p


INST = "subject\tregion\thost\thow\twhere\n" \
       "a_one\tLATAM\tx.ufpi.br\tccTLD .br\tsrc/c.go\n" \
       "a_two\tEMEA\ty.unicatt.it\tccTLD .it\tREADME.md\n" \
       "a_three\tUNPLACED\t-\t-\t-\n" \
       "a_four\tCONFLICT\tz.edu.au\tacademic ns\tlinks.json\n" \
       "a_five\tNorth America\tbb.edu\tbare .edu (LEAD)\ttest/unit.test.ts\n"

OFF = "subject\tregion\n" \
      "a/one\tUNMAPPED\n" \
      "a/two\tEMEA\n" \
      "a/three\tAPAC\n" \
      "a/four\tAPAC\n" \
      "a/five\tEMEA\n"

# 1 -- owner/repo and owner_repo are the same subject
check("norm_subject joins the two spellings",
      ca.norm_subject("a/one"), "a_one")

i, o = tmptsv(INST), tmptsv(OFF)
rows, counts, only = ca.compare(i, o)

# 2 -- the population is the intersection, and it is not empty
check("population is 5", len(rows), 5)

# 3 -- both placed, same region
check("both placed and equal -> AGREE", counts.get("AGREE"), 1)

# 4 -- offset declined, institution placed: the coverage gain
check("offset UNMAPPED + institution placed -> INSTITUTION_ONLY",
      counts.get("INSTITUTION_ONLY"), 1)

# 5 -- institution found nothing, offset placed
check("institution UNPLACED + offset placed -> OFFSET_ONLY",
      counts.get("OFFSET_ONLY"), 1)

# 6 -- a multi-region institution read is its own state, not a disagreement
check("CONFLICT is not counted as DISAGREE",
      (counts.get("INSTITUTION_CONFLICT"), counts.get("DISAGREE")), (1, 1))

# 7 -- UNMAPPED and AMBIGUOUS are declinations, not regions
check("declined values are not regions",
      (ca.classify("LATAM", "UNMAPPED"), ca.classify("LATAM", "AMBIGUOUS"),
       ca.classify("UNPLACED", "-")),
      ("INSTITUTION_ONLY", "INSTITUTION_ONLY", "NEITHER"))

# 8 -- a genuine disagreement is reported as one
check("two different regions -> DISAGREE",
      ca.classify("North America", "EMEA"), "DISAGREE")
os.unlink(i)
os.unlink(o)

# 9 -- 🔴 the defect: a leading blank line must not yield an empty population
i = tmptsv("\n" + INST)
o = tmptsv(OFF)
rows2, counts2, _ = ca.compare(i, o)
check("a leading blank line does not empty the population", len(rows2), 5)
os.unlink(i)

# 10 -- a comment line is skipped, and the header after it is still found
i = tmptsv("# 28 of 50 row(s) placed\n" + INST)
rows3, _, _ = ca.compare(i, o)
check("a leading comment line is skipped", len(rows3), 5)
os.unlink(i)

# 11 -- subjects present in only one file are reported, not silently dropped
i = tmptsv(INST + "a_six\tAPAC\tq.ac.in\tacademic ns\tmain.py\n")
rows4, _, only4 = ca.compare(i, o)
check("a subject in one file only is named, not absorbed",
      (len(rows4), only4), (5, ["a_six"]))
os.unlink(i)
os.unlink(o)

print("\n%d/%d passed" % (11 - len(FAILS), 11))
for f in FAILS:
    print("\n" + f)
sys.exit(1 if FAILS else 0)
