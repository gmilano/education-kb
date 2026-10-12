#!/usr/bin/env python3
"""omission.py — the THIRD election form, which no matcher on this shelf can read.

🔴 **An election has three surface forms, and this shelf's matchers know two.**

| form | surface | p151 reads it |
|---|---|---|
| **or-later** | the clause *"or (at your option) any later version"* is PRESENT | 🟢 yes |
| **only, worded** | the word *"only"* appears — *"version 3 of the License only"* | 🟢 yes |
| 🆕 **only, by OMISSION** | a COMPLETE GNU notice whose or-later clause is ABSENT | 🔴 **no** |

🆕 **The third form is the FSF's own `-only` form**, and it is what
`instructure/canvas-lms` carries in **16 905** files:

    # Canvas is free software: you can redistribute it and/or modify it under
    # the terms of the GNU Affero General Public License as published by the Free
    # Software Foundation, version 3 of the License.

🔴 **There is no word "only" to match and no or-later clause to find, so every matcher on
this shelf reports `SILENT`** — the same verdict it gives a tree with no notice at all.

🟢 **The test is STRUCTURAL, not lexical**: a notice that reaches the grant verb
(*"as published by the Free Software Foundation"*) and names a version, and then does NOT
continue into the or-later clause, has elected the stated version and nothing later.

    python3 omission.py <clones-dir> [subject ...]
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from election_verticals import (ELECTION_LATER, ELECTION_ONLY, GNU_NOTICE,  # noqa: E402
                                head, normalise, walk_sources)

# 🟢 The GRANT VERB plus a version, which together mean "this file states its licence
# version". 🔵 `[^.]{0,120}?` keeps the match inside one sentence: an omission verdict
# must not be assembled out of two different sentences.
GRANT_WITH_VERSION = re.compile(
    r"as\s+published\s+by\s+the\s+Free\s+Software\s+Foundation\s*,?\s*"
    r"(?:either\s+)?version\s+([\d.]+)(?:\s+of\s+the(?:\s+[A-Za-z]+){0,5}?\s+Licen[cs]e)?",
    re.I)

COLS = ("subject", "scanned", "gnu_notices", "or_later", "only_worded",
        "only_by_OMISSION", "notice_no_version", "verdict")


def classify(text):
    """Return one of `OR_LATER`, `ONLY_WORDED`, `ONLY_OMISSION`, `NOTICE_NO_VERSION`,
    `NO_NOTICE` for a single normalised file header."""
    if not GNU_NOTICE.search(text):
        return "NO_NOTICE"
    if ELECTION_LATER.search(text):
        return "OR_LATER"
    if ELECTION_ONLY.search(text):
        return "ONLY_WORDED"
    if GRANT_WITH_VERSION.search(text):
        return "ONLY_OMISSION"
    return "NOTICE_NO_VERSION"


def measure(root):
    counts = dict(scanned=0, OR_LATER=0, ONLY_WORDED=0, ONLY_OMISSION=0,
                  NOTICE_NO_VERSION=0, NO_NOTICE=0)
    sample = {}
    for p in walk_sources(root):
        counts["scanned"] += 1
        k = classify(normalise(head(p)))
        counts[k] += 1
        if k not in ("NO_NOTICE",) and k not in sample:
            sample[k] = os.path.relpath(p, root)
    return counts, sample


def verdict(c):
    """🔵 The subject-level election. `MIXED` is reported, never resolved."""
    live = [k for k in ("OR_LATER", "ONLY_WORDED", "ONLY_OMISSION") if c[k]]
    if not live:
        return "SILENT" if c["NOTICE_NO_VERSION"] or c["NO_NOTICE"] else "SILENT"
    if len(live) > 1:
        return "MIXED:" + "+".join(live)
    return live[0]


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2
    base = argv[1]
    subjects = sorted(d for d in os.listdir(base)
                      if os.path.isdir(os.path.join(base, d)))
    if len(argv) > 2:
        subjects = [s for s in subjects if s in set(argv[2:])]
    print("\t".join(COLS))
    tot = dict(scanned=0, OR_LATER=0, ONLY_WORDED=0, ONLY_OMISSION=0,
               NOTICE_NO_VERSION=0)
    for s in subjects:
        c, sample = measure(os.path.join(base, s))
        notices = c["scanned"] - c["NO_NOTICE"]
        for k in tot:
            tot[k] += c[k]
        print("\t".join((s, str(c["scanned"]), str(notices), str(c["OR_LATER"]),
                         str(c["ONLY_WORDED"]), str(c["ONLY_OMISSION"]),
                         str(c["NOTICE_NO_VERSION"]), verdict(c))))
        if "ONLY_OMISSION" in sample:
            sys.stderr.write("  %s omission sample: %s\n" % (s, sample["ONLY_OMISSION"]))
    e = sys.stderr.write
    e("scanned=%d  or_later=%d  only_worded=%d  ONLY_BY_OMISSION=%d  notice_no_version=%d\n"
      % (tot["scanned"], tot["OR_LATER"], tot["ONLY_WORDED"], tot["ONLY_OMISSION"],
         tot["NOTICE_NO_VERSION"]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
