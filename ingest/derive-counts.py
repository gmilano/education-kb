#!/usr/bin/env python3
"""derive-counts.py -- the general form of Gap 543-E / 534-E / 544-E.

ONE defect class, now caught three times in three different files:
  * p543 -- agents/top.md's shelf heading, stale by a whole pass
  * p545 -- repos/foundations.md's "seventy-two" against a derived 156 (pass arithmetic
            frozen at p534 while nine later passes filed rows)
  * p545 -- compose/patterns.md's "Thirty-eight" against 47 recipes actually present

The class is: A COUNT WRITTEN IN PROSE BESIDE THE ROWS IT COUNTS. It goes stale the moment
a pass adds a row and forgets the sentence, and no amount of care prevents it -- only
derivation does.

This script derives every such count that CAN be derived from a page's own structure, and
abstains loudly where it cannot. repos/foundations.md needs a declared disposition per
table and is handled by its own script, derive-foundations.py, which this one defers to.

usage: python3 -I ingest/derive-counts.py [repo-root]
exit 0 all green / 1 a header disagrees with its page / 2 a page could not be parsed
"""
import os
import re
import sys

root = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
rc = 0

def header_of(path, lines=40):
    return "\n".join(open(path, encoding="utf-8").read().split("\n")[:lines])


def claim_in(path, noun):
    """Read an EXPLICIT machine-readable claim: 'derived <noun>: **N**'.

    p545's first draft matched any '**N** recipes' in the header and picked up the digit
    inside its own retraction sentence ("this page held **47** recipes"), reporting RED on
    a page that was right. A count claim must be unambiguous to a reader AND to the gate,
    so the page carries one marked form and the gate reads only that.
    """
    m = re.search(r"derived %s: \*\*(\d+)\*\*" % re.escape(noun), header_of(path), re.I)
    return int(m.group(1)) if m else None


# --- compose/patterns.md: recipes are '## [marks] P-<n>-<X> — ...' ------------------------
# p568: the id scheme on the page is FAMILY-SUFFIXED -- 'P-571-A', not 'P571'. The original
# pattern (r"P(\d+) —") matched none of the 17 headings present, so `ids` came back empty and
# `ids[0]` raised IndexError at this line, ABORTING THE WHOLE GATE before agents/top.md and
# intel/trends.md were ever reached. Two fixes, both deliberate:
#   * accept the hyphenated, letter-suffixed form (and the bare 'P<n>' form, for history);
#   * count RECIPE HEADINGS, not distinct family numbers -- 'P-571-A' and 'P-571-B' are two
#     recipes, and counting families under-reported a page that carries several per family.
# Contiguity is still checked over the FAMILY numbers, which is where a missing id is a signal.
pat = os.path.join(root, "compose", "patterns.md")
if os.path.exists(pat):
    body = open(pat, encoding="utf-8").read()
    found = re.findall(r"^## [^A-Za-z0-9]*P-?(\d+)(?:-([A-Z]))? —", body, re.M)
    n = len(found)
    fams = sorted({int(num) for num, _ in found})
    gaps = [i for i in range(fams[0], fams[-1] + 1) if i not in fams] if fams else []
    claimed = claim_in(pat, "recipes")
    if not found:
        print("compose/patterns.md   recipes: ABSTAIN -- no recipe heading matched; id scheme changed?")
        rc = 2
    else:
        rng = f"P-{fams[0]}..P-{fams[-1]}"
        print(f"compose/patterns.md   recipes: derived={n}  families={len(fams)}  range={rng}  claimed={claimed}")
    if gaps:
        print(f"  AMBER non-contiguous families: missing {['P-%d' % g for g in gaps]}")
    if not found:
        pass  # already abstained above; do not also grade a count we could not derive
    elif claimed is None:
        print("  AMBER no 'derived recipes: **N**' claim in the header.")
    elif claimed != n:
        print(f"  RED  header claims {claimed}, page holds {n} -- rewrite the header, not the page.")
        rc = 1
    else:
        print("  GREEN header agrees with its page.")

# --- intel/trends.md: trends are numbered '## <n>. ' or '## ... Trend <n>:' ---------------
tre = os.path.join(root, "intel", "trends.md")
if os.path.exists(tre):
    body = open(tre, encoding="utf-8").read()
    ids = {int(m) for m in re.findall(r"^## (\d+)\. ", body, re.M)}
    ids |= {int(m) for m in re.findall(r"^## .*?Trend (\d+):", body, re.M)}
    # p812: the ONLY id scheme this page has ever used is '## T<n> — ...'. The two patterns
    # above accept '## 31. ' and '## ... Trend 31:' and matched NEITHER of the 33 headings
    # present, so the gate reported derived=0/claimed=None -- an AMBER abstain, which in
    # `make hooks` output is indistinguishable from a pass -- for every pass since it was
    # written. Widened to the page's actual convention, exactly as p568 widened the recipe
    # pattern for family-suffixed ids ('P-571-A') and p718 replaced prose-keying with column
    # signatures. Same defect class, third file.
    ids |= {int(m) for m in re.findall(r"^## [^A-Za-z0-9]*T(\d+)\b", body, re.M)}
    n = len(ids)
    claimed = claim_in(tre, "trends")
    print(f"intel/trends.md       trends:  derived={n}  claimed={claimed}")
    if claimed is None:
        print("  AMBER no 'derived trends: **N**' claim in the header.")
    elif claimed != n:
        print(f"  RED  header claims {claimed}, page holds {n}.")
        rc = 1
    else:
        print("  GREEN header agrees with its page.")

# --- p718: all three shelves, located by COLUMN-HEADER SIGNATURE ------------------------
# 🔴 p718's primary finding. This block previously looked for the *wording* of the prose
# heading ('## Shelf', widened at p568 to '## The shelf'). agents/top.md's heading has since
# been reworded to '## The agents -- N rows', so the predicate stopped matching and the gate
# ABSTAINED -- silently passing -- on the one shelf it was built for. That is the THIRD time
# this same predicate has been defeated by a rewrite (p543 built it, p568 widened it, p718
# found it abstaining again), and in the interval foundations.md went stale by 10 and
# solutions.md by 5 while `make hooks` reported no count defect at all.
#
# 🟢 The fix is to stop keying on prose. A shelf table is identified by its own COLUMN-HEADER
# ROW -- a structural contract the shelves' own prose already says they use (`680-F2`) and
# which a rewrite of the surrounding sentence cannot touch. The count claim is then read from
# the nearest PRECEDING '## ' heading. Reword the heading however you like; the gate still
# finds the table and still grades the number in it.
# --- p813: ACTION p811-A, discharged with option (a) --------------------------------------
# 🔴 p811 recorded the defect: this list assumed ONE canonical table per file with a fixed
# column signature, while repos/foundations.md (14 tables) and verticals/solutions.md (10)
# are deliberately SECTIONED BY ARCHITECTURAL LAYER. Both files had been RED since p718 --
# not stale, not neglected, structurally ungradeable -- and the expected signatures below
# were additionally wrong on their face ('Licence' where both files write 'License',
# 'Default branch' and 'Branch | Stack' columns that have never existed).
#
# 🟢 p811 chose between (a) teach the gate a LIST of signatures per file and sum the rows,
# and (b) give each file one roll-up table and demote the layer tables to prose -- and chose
# (a), because the layering IS the value of those files. This is (a).
#
# 🟢 And it closes the defect CLASS, not just the instance. Every previous repair here
# (p543, p568, p718, p812) widened a predicate and left the gate able to go blind again the
# next time the pages changed shape. So the sum is now accompanied by UNCOUNTED-TABLE
# DETECTION: any table in the file whose body carries github.com addresses but whose header
# is not in the list below is a RED naming the line. A new layer table can be added freely;
# it cannot be added SILENTLY.
SHELVES = [
    ("agents/top.md", [
        "| Name | Repo | Licence | Stars | Region | Description |",
    ], [
        # 🟢 Declared NOT-counted, deliberately: the shelf figure is the build-safe table.
        # Declaring them is what makes the detector below meaningful -- an undeclared table
        # is an omission, a declared one is a decision.
        "| Agent | Repo | License | Stars | What it does |",            # copyleft
        "| Candidate | Repo | Actual license | Stars | Why rejected |",  # rejected
    ]),
    ("repos/foundations.md", [
        "| Repo | License | Stars | Notes |",
        "| Repo | License | Stars | What it is, and what it is not |",
    ], []),
    ("verticals/solutions.md", [
        "| Platform | Repo | License | Stars | Notes |",
        "| Platform | Repo | Licence | Stars | What it is |",
        "| Platform | Repo | License | Stars | Why it is the right base for education admissions |",
        "| Platform | Repo | License | Stars | Where it is the incumbent | AI customization surface |",
        "| Platform | Repo | License (payload-verified) | Stars | What you actually get | What you do NOT get |",
        "| Platform | What institutions run it | Agent surface found this pass | License | Risk posture |",
        "| Platform | What institutions run it | Agent surface added this pass | License | Risk posture |",
        "| Platform | Operated by | Country | Agent surface found this pass | Licence | Stars |",
        "| Platform | Incumbent where | Open agent surface found | License | Stars |",
        "| Library | Repo | License | Stars | Use when |",
    ], []),
]


def _tables(lines):
    """Yield (header_index, header_text, [body rows]) for every markdown table."""
    i = 0
    while i < len(lines) - 1:
        h = lines[i].strip()
        sep = lines[i + 1].strip()
        if h.startswith("|") and re.match(r"^\|[\s:|-]+\|$", sep) and "-" in sep:
            j = i + 2
            body = []
            while j < len(lines) and lines[j].strip().startswith("|"):
                body.append(lines[j])
                j += 1
            yield i, h, body
            i = j
        else:
            i += 1


for rel, signatures, excluded in SHELVES:

    path = os.path.join(root, rel)
    if not os.path.exists(path):
        print("%-22s ABSTAIN file absent." % rel)
        continue
    lines = open(path, encoding="utf-8").read().split("\n")

    sigset = set(signatures)
    rows, ragged, uncounted, matched = [], 0, [], 0
    for hi, header, body in _tables(lines):
        linked = [r for r in body if "github.com/" in r]
        if header in sigset:
            matched += 1
            ncol = len(header.strip().strip("|").split("|"))
            rows.extend(linked)
            ragged += sum(1 for r in linked
                          if len(r.strip().strip("|").split("|")) != ncol)
        elif linked and header not in set(excluded):
            uncounted.append((hi + 1, header, len(linked)))

    if matched == 0:
        print("%-22s RED  none of the %d declared column-header signatures was found; "
              "no table can be located." % (rel, len(signatures)))
        for sig in signatures:
            print("                       expected: %s" % sig)
        rc = 1
        continue

    if uncounted:
        print("%-22s RED  %d table(s) carry github.com rows but no declared signature; "
              "they are NOT counted." % (rel, len(uncounted)))
        for ln, header, n in uncounted:
            print("                       line %d (%d rows): %s" % (ln, n, header))
        rc = 1
    # p718: the count claim is NOT in the nearest preceding '## ' -- every shelf carries pass
    # narrative between its count heading and its table. It lives in the file's UNIQUE
    # canonical count heading, of the shape '## <name> -- N rows'. Graded as a SINGLETON
    # (`p699`'s rule): zero such headings or more than one is itself a RED, because both are
    # states in which a reader cannot tell which number is the shelf's.
    CLAIM = re.compile(r"^## .*?[\u2014-]\s*(\d[\d,]*)\s+rows\b")
    claims = [(j, m) for j, l in enumerate(lines)
              if l.startswith("## ") for m in [CLAIM.match(l)] if m]
    claimed = None
    if len(claims) == 1:
        claimed = int(claims[0][1].group(1).replace(",", ""))
    elif len(claims) == 0:
        print("  RED  no canonical count heading ('## <name> - N rows') in the file.")
        rc = 1
    else:
        print("  RED  %d canonical count headings; the shelf's figure is ambiguous: lines %s."
              % (len(claims), ", ".join(str(j + 1) for j, _ in claims)))
        rc = 1
    subj = []
    for r in rows:
        m = re.search(r"github\.com/([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)", r)
        subj.append(m.group(1).lower().rstrip(".)") if m else None)
    nolink = sum(1 for s in subj if not s)
    seen, dupes = set(), 0
    for s in subj:
        if s and s in seen:
            dupes += 1
        elif s:
            seen.add(s)
    # 🟢 p813: on a file summed across LAYER tables, one repository legitimately appears in
    # two layers (frappe/education sits in the Frappe layer and in the ERP layer, and that
    # repetition is the point of the layering). So a repeat is a duplicate ROW, not a
    # duplicate SUBJECT, and the claim is graded against DISTINCT subjects. On a
    # single-table shelf a repeat is still a defect and still RED.
    multi = len(signatures) > 1
    distinct = len(seen)
    graded = distinct if multi else len(rows)
    print("%-22s shelf: tables=%d rows=%d distinct=%d graded=%d claimed=%s "
          "ragged=%d nolink=%d dupes=%d"
          % (rel, matched, len(rows), distinct, graded, claimed, ragged, nolink, dupes))
    if claimed is None:
        print("  AMBER no 'N rows' claim in the heading above the table; nothing to compare.")
    elif claimed != graded:
        print("  RED  heading claims %d, the file holds %d." % (claimed, graded))
        rc = 1
    else:
        print("  GREEN heading agrees with its page.")
    if ragged:
        print("  RED  %d row(s) disagree with their header's column count (the p674 L55 class)." % ragged)
        rc = 1
    if nolink:
        print("  RED  %d row(s) carry no repository link." % nolink)
        rc = 1
    if dupes and multi:
        print("  INFO %d repository/ies appear in more than one layer table; counted once."
              % dupes)
    elif dupes:
        print("  RED  %d duplicate subject(s)." % dupes)
        rc = 1

sys.exit(rc)
