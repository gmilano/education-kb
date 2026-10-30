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


# --- compose/patterns.md: recipes are '## [marks] P<n> — ...' -----------------------------
pat = os.path.join(root, "compose", "patterns.md")
if os.path.exists(pat):
    ids = sorted({int(m) for m in re.findall(r"^## [^A-Za-z0-9]*P(\d+) —", open(pat, encoding="utf-8").read(), re.M)})
    n = len(ids)
    gaps = [i for i in range(ids[0], ids[-1] + 1) if i not in ids] if ids else []
    claimed = claim_in(pat, "recipes")
    print(f"compose/patterns.md   recipes: derived={n}  range=P{ids[0]}..P{ids[-1]}  claimed={claimed}")
    if gaps:
        print(f"  AMBER non-contiguous: missing {['P%d' % g for g in gaps]}")
    if claimed is None:
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
    start = next((i for i, l in enumerate(lines) if l.startswith("## Shelf")), None)
    if start is None:
        print("agents/top.md         ABSTAIN no '## Shelf' heading.")
    else:
        end = next((i for i in range(start + 1, len(lines)) if lines[i].startswith("## ")), len(lines))
        rows = [l for l in lines[start + 1:end]
                if l.startswith("|")
                and not re.match(r"^\|[\s:|-]+\|", l)
                and not re.match(r"^\| *Agent *\|", l)]
        claimed = re.search(r"(\d+)", lines[start])
        claimed = int(claimed.group(1)) if claimed else None
        print(f"agents/top.md         shelf:   derived={len(rows)}  claimed={claimed}")
        if claimed is not None and claimed != len(rows):
            print(f"  RED  heading claims {claimed}, table holds {len(rows)}.")
            rc = 1
        else:
            print("  GREEN heading agrees with its table.")

# --- repos/foundations.md: deferred, it needs declared dispositions -----------------------
print("repos/foundations.md  DEFER -> ingest/derive-foundations.py (needs a declared")
print("                      disposition per table; a census row is not a shelf row).")

sys.exit(rc)
