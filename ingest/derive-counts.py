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

# --- agents/top.md: the shelf table (p543's original case) --------------------------------
top = os.path.join(root, "agents", "top.md")
if os.path.exists(top):
    lines = open(top, encoding="utf-8").read().split("\n")
    # p568: the page's heading is '## The shelf', not '## Shelf', so the exact-prefix test
    # abstained SILENTLY on p543's original case -- the gate built to catch a stale shelf
    # count could not see the shelf. Matched case-insensitively, with or without the article.
    start = next((i for i, l in enumerate(lines)
                  if re.match(r"^## (the )?shelf\b", l, re.I)), None)
    if start is None:
        print("agents/top.md         ABSTAIN no shelf heading ('## Shelf' / '## The shelf').")
    else:
        end = next((i for i in range(start + 1, len(lines)) if lines[i].startswith("## ")), len(lines))
        rows = [l for l in lines[start + 1:end]
                if l.startswith("|")
                and not re.match(r"^\|[\s:|-]+\|", l)
                and not re.match(r"^\| *Agent *\|", l)]
        claimed = re.search(r"(\d+)", lines[start])
        claimed = int(claimed.group(1)) if claimed else None
        print(f"agents/top.md         shelf:   derived={len(rows)}  claimed={claimed}")
        if claimed is None:
            # p568: was GREEN here, which reported agreement with a claim that does not
            # exist -- the other two blocks AMBER in this case and this one now matches.
            # NOTE the scan spans every table between this '##' and the next, so a page
            # with '###' sub-tables (carried-with-defect, skill bundles) derives MORE than
            # its shelf. See gap 568-E: the shelf count lives in BODY prose, unreachable here.
            print("  AMBER no count in the shelf heading; nothing to compare against.")
        elif claimed != len(rows):
            print(f"  RED  heading claims {claimed}, table holds {len(rows)}.")
            rc = 1
        else:
            print("  GREEN heading agrees with its table.")

# --- repos/foundations.md: deferred, it needs declared dispositions -----------------------
print("repos/foundations.md  DEFER -> ingest/derive-foundations.py (needs a declared")
print("                      disposition per table; a census row is not a shelf row).")

sys.exit(rc)
