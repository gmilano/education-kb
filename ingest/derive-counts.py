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
SHELVES = [
    ("agents/top.md",
     "| Name | Repo | Licence | Stars | Region | Description |", 6),
    ("repos/foundations.md",
     "| Repo | Licence | Stars | Default branch | Why it is a foundation |", 5),
    ("verticals/solutions.md",
     "| Platform | Repo | Licence | Branch | Stack | Use case |", 6),
]

for rel, signature, ncol in SHELVES:
    path = os.path.join(root, rel)
    if not os.path.exists(path):
        print("%-22s ABSTAIN file absent." % rel)
        continue
    lines = open(path, encoding="utf-8").read().split("\n")
    hi = next((i for i, l in enumerate(lines) if l.strip() == signature), None)
    if hi is None:
        # Not a silent abstain: a shelf whose column header has changed is a RED, because
        # that is exactly the condition under which this gate used to go blind.
        print("%-22s RED  column-header signature not found; the table cannot be located." % rel)
        print("                       expected: %s" % signature)
        rc = 1
        continue
    i = hi + 2                      # skip the |---|---| separator
    rows = []
    while i < len(lines) and lines[i].strip().startswith("|"):
        rows.append(lines[i])
        i += 1
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
    ragged = sum(1 for r in rows if len(r.strip().strip("|").split("|")) != ncol)
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
    print("%-22s shelf: derived=%d claimed=%s ragged=%d nolink=%d dupes=%d"
          % (rel, len(rows), claimed, ragged, nolink, dupes))
    if claimed is None:
        print("  AMBER no 'N rows' claim in the heading above the table; nothing to compare.")
    elif claimed != len(rows):
        print("  RED  heading claims %d, table holds %d." % (claimed, len(rows)))
        rc = 1
    else:
        print("  GREEN heading agrees with its table.")
    if ragged:
        print("  RED  %d row(s) disagree with the header's %d columns (the p674 L55 class)." % (ragged, ncol))
        rc = 1
    if nolink:
        print("  RED  %d row(s) carry no repository link." % nolink)
        rc = 1
    if dupes:
        print("  RED  %d duplicate subject(s)." % dupes)
        rc = 1

sys.exit(rc)
