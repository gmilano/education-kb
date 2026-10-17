#!/usr/bin/env python3
"""p274 — T37 as a STANDING re-count, which is what `p273`'s backlog item 7 asked for.

`T37` (p272) says: "a quantity inside a gap statement is a carried datum -- re-count it
from the rows, on every shelf that states it."  It was written as an amendment and never
built.  This is the instrument.

For each QUANTIFIED CLAIM registered below it re-derives the number from the rows of the
live shelves and prints MATCH or STALE.  No network.  No searches.  Run it before
publishing any sentence with a numeral in it:

    python3 -I recount.py --root /path/to/education-kb
"""
import argparse
import os
import re
import sys

SHELVES = [
    "agents/top.md", "agents/trending.md", "repos/foundations.md", "repos/trending.md",
    "verticals/solutions.md", "intel/market.md", "intel/trends.md", "compose/patterns.md",
]

# 🟢 p274: GREEDY, not lazy -- ACTION TB lints lazy quantifiers out of every
# instrument on this base, and it caught this line.  Greedy is also correct here:
# every delimiter a slug can end at -- ")", whitespace, backtick, comma, "|" -- is
# outside the character class, so the match stops on its own.  The one character
# that is INSIDE the class and can trail a slug is ".", which rows_with_slugs()
# strips; a lazy quantifier would instead have stopped at the first "." INSIDE a
# repo name, truncating any slug that contains one.
SLUG_RE = re.compile(r"github\.com/([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)")

# A row is an MCP server if its slug or its row text says so.  "mewcp" is deliberately
# matched too: `AStheTECH/mewcp-google-classroom` is an MCP server whose slug does not
# contain the substring "mcp", and a count that greps for "mcp" silently drops it.
MCP_HINT = re.compile(r"mcp|mewcp|model context protocol", re.I)

# platform -> the names a row uses for it.  Order matters: first match wins.
PLATFORMS = [
    ("Canvas", [r"\bcanvas\b"]),
    ("Moodle", [r"\bmoodle\b"]),
    ("Google Classroom / Workspace for Education", [r"google[- ]classroom", r"workspace for education", r"\bclassroom-mcp\b"]),
    ("Brightspace / D2L", [r"brightspace", r"\bd2l\b", r"dtu[- ]learn"]),
    ("Anki", [r"\banki\b"]),
    ("Blackboard", [r"blackboard"]),
    ("Open edX", [r"open ?edx"]),
    ("Sakai", [r"\bsakai\b"]),
    ("Chamilo", [r"chamilo"]),
    ("ILIAS", [r"\bilias\b"]),
]


def read(root, rel):
    path = os.path.join(root, rel)
    if not os.path.exists(path):
        return ""
    with open(path, encoding="utf-8", errors="replace") as fh:
        return fh.read()


def rows_with_slugs(text):
    """Yield (line, [slugs]) for every line that mentions at least one repo slug."""
    for line in text.splitlines():
        slugs = SLUG_RE.findall(line)
        if slugs:
            # strip a trailing "." (sentence punctuation inside the character class)
            # and a trailing ".git" (clone URLs appear in these shelves too): both name
            # the same repository as the bare slug, and counting them twice is exactly
            # the double-count this instrument exists to prevent.
            cleaned = []
            for s in slugs:
                s = s.rstrip(".")
                if s.endswith(".git"):
                    s = s[:-4]
                cleaned.append(s)
            yield line, cleaned


def mcp_slugs(text):
    """Distinct slugs this shelf presents as MCP servers.

    STRICT: the SLUG ITSELF must carry the MCP marker.  An earlier draft of this
    instrument accepted a slug whose LINE mentioned MCP, and that let a platform's own
    repository (`chamilo/chamilo-lms`) and unrelated rows (`huggingface/transformers`)
    into a per-platform tally -- a false positive in a counting instrument is exactly the
    defect the instrument exists to catch, so the looser rule is not kept as an option.
    Cost of the strict rule, stated: a server whose slug does not say "mcp" is missed, so
    this count is a FLOOR.  `AStheTECH/mewcp-google-classroom` is the known such case and
    MCP_HINT matches it explicitly.
    """
    found = {}
    for line, slugs in rows_with_slugs(text):
        for s in slugs:
            if MCP_HINT.search(s):
                # GitHub owner/repo is CASE-INSENSITIVE: p274 proved it first-hand --
                # ahmedEid1/Lumen and ahmedEid1/lumen return the IDENTICAL HEAD SHA,
                # which also settles the collision p196 recorded between them.  A
                # case-sensitive census counts one repository twice.
                found.setdefault(s.lower(), line)
    return found


def platform_of(slug, line):
    """SLUG FIRST, then the line.

    Classifying on the row text alone put `felipedias-ie/blackboard-mcp` under Canvas,
    because the row mentions Canvas in prose.  A platform name in a sentence is a
    reference; a platform name in a slug is the subject.
    """
    for hay in (slug, line):
        for name, pats in PLATFORMS:
            for p in pats:
                if re.search(p, hay, re.I):
                    return name
    return None


def measure(root):
    m = {}
    top = read(root, "agents/top.md")
    trend = read(root, "agents/trending.md")

    top_mcp = mcp_slugs(top)
    m["mcp_slugs_on_agents_top"] = len(top_mcp)

    all_mcp = dict(top_mcp)
    for s, line in mcp_slugs(trend).items():
        all_mcp.setdefault(s, line)
    m["mcp_slugs_on_agent_shelves"] = len(all_mcp)

    plats_top = {}
    for s, line in top_mcp.items():
        p = platform_of(s, line)
        if p:
            plats_top.setdefault(p, set()).add(s)
    # a tutoring loop with no external system is not a platform
    m["lms_platforms_on_agents_top"] = len([p for p in plats_top if p != "Anki"])

    plats_all = {}
    for s, line in all_mcp.items():
        p = platform_of(s, line)
        if p:
            plats_all.setdefault(p, set()).add(s)
    m["lms_platforms_on_agent_shelves"] = len([p for p in plats_all if p != "Anki"])
    m["_platform_detail"] = {p: sorted(v) for p, v in sorted(plats_all.items())}

    # permissive rows in agents/top.md's build-on tier: count the table between the
    # tier heading and the sentence that states the count.
    # 🔴 p277: this sentinel is a LITERAL COPY OF THE NUMBER BEING CHECKED, so correcting
    # the shelf DELETES the boundary and the measurement silently becomes "every table row
    # in the rest of the file" -- 27 became 63 the moment `24` was fixed to `27`, and the
    # verdict stayed STALE for a new reason.  A checker anchored on the stale text cannot
    # survive the correction it asks for.  Anchored on the row of dashes instead would be
    # better still; the sentinel is moved here because the pin must move WITH the change
    # (p261's remedy), and widening the anchor is left as a declared item.
    tier = top.split("## Build-on-this tier")[-1].split("**27 permissive rows")[0] if "## Build-on-this tier" in top else ""
    rows = [l for l in tier.splitlines() if l.startswith("|") and "github.com/" in l]
    m["permissive_rows_in_build_on_tier"] = len(rows)
    return m


# claim -> (measured key, published value, where it is published)
CLAIMS = [
    ("MCP server slugs tabled on agents/top.md", "mcp_slugs_on_agents_top", 20,
     "agents/top.md MCP section + intel/trends.md T21, both set to 20 by p274 AFTER it added 5 rows"),
    ("LMS platforms reachable by MCP, agents/top.md", "lms_platforms_on_agents_top", 6,
     "agents/top.md MCP section (p274). Was 3 on both shelves before this pass"),
    ("LMS platforms reachable by MCP, both agent shelves", "lms_platforms_on_agent_shelves", 6,
     "intel/trends.md T24 (p274). Was 3"),
    # 🟢 p275: 23 -> 24.  ls1intum/Athena moved UP from the licence-UNVERIFIED table after
    # 12 of its 14 manifests were found to declare MIT.  Not a new repo -- a re-graded one.
    # 🟢 p277: 24 -> 27.  p276 added three rows (DMontgomery40/mcp-canvas-lms,
    # fsrs4anki-helper, ECNU-ICALK/EduChat) and did not move the count; this re-count
    # reported it STALE, an independent row-by-row enumeration agreed at 27, and the shelf
    # is corrected.  🔵 Note what `published` IS here: a Python CONSTANT, not a value read
    # from the shelf -- so this claim detects ROW drift and is blind to TEXT drift.  A pass
    # that edits the sentence and not this literal leaves the gate green and the shelf
    # wrong, which is the inverse of the failure p277 hit.
    ("permissive rows in the build-on tier", "permissive_rows_in_build_on_tier", 27,
     "agents/top.md ('27 permissive rows', corrected from 24 at p277)"),
]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
    args = ap.parse_args()
    root = os.path.abspath(args.root)

    m = measure(root)
    out = sys.stdout
    out.write("# p274 -- T37 standing re-count.  Every number below is derived from the rows, "
              "not copied from the sentence that last stated it.\n")
    out.write("claim\tpublished\tmeasured\tverdict\twhere_published\n")
    stale = 0
    for claim, key, published, where in CLAIMS:
        measured = m[key]
        verdict = "MATCH" if measured == published else "STALE"
        if verdict == "STALE":
            stale += 1
        out.write(f"{claim}\t{published}\t{measured}\t{verdict}\t{where}\n")
    out.write(f"# STALE={stale} of {len(CLAIMS)} registered claims\n")
    out.write("# MCP servers by platform, across agents/top.md AND agents/trending.md:\n")
    for p, slugs in m["_platform_detail"].items():
        out.write(f"#   {p}\t{len(slugs)}\t{', '.join(slugs)}\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
