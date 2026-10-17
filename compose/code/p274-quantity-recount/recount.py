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


def _tier_rows(text, heading):
    """Table rows between `heading` and the NEXT `## ` heading.

    STRUCTURAL, deliberately.  See the note at the call site: the previous boundary was a
    literal copy of the number being checked, and correcting that number deleted it.
    """
    if heading not in text:
        return []
    after = text.split(heading, 1)[1]
    out = []
    for line in after.splitlines():
        if line.startswith("## "):
            break
        if line.startswith("|") and "github.com/" in line:
            out.append(line)
    return out


def _section_rows(text, heading_prefix):
    """Table rows of ONE section, bounded by the next heading at the same depth or shallower.

    `heading_prefix` is matched as a line prefix, e.g. "### Agents over the systems".
    """
    lines = text.splitlines()
    start = None
    for i, line in enumerate(lines):
        if line.startswith(heading_prefix):
            start = i + 1
            break
    if start is None:
        return []
    depth = len(heading_prefix) - len(heading_prefix.lstrip("#"))
    out = []
    for line in lines[start:]:
        if line.startswith("#"):
            d = len(line) - len(line.lstrip("#"))
            if d <= depth:
                break
        if line.startswith("|") and "github.com/" in line:
            out.append(line)
    return out


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

    # 🟢 p278 (`p277`'s declared item 2) — THE RECONCILIATION, and the gate was right.
    #
    # `p277` reported `published 20 · measured 21 · STALE`, wrote a fresh enumeration that
    # returned **20**, concluded *"two predicates disagree by one row, so the defect is in a
    # predicate, not the shelf"*, and deliberately left the shelf at 20.
    #
    # 🔴 `p278` reproduced BOTH numbers and the disagreement is fully explained: `p277`'s
    # enumeration was described as *"every `github.com/<owner>/<repo>` whose slug contains
    # `mcp`"*, and run exactly that way it returns 20 — because it drops
    # `AStheTECH/mewcp-google-classroom`, whose slug does not contain the substring `mcp`.
    # 🔵 **MCP_HINT's own code comment, five lines above the predicate, already said so:**
    # *"a count that greps for `mcp` silently drops it."*  `p277` read this file, wrote the
    # predicate this file warns against, and trusted it over the gate.
    # 🔴 And the dropped row is the PROPRIETARY one — the single row on that shelf a studio
    # may NOT use.  The count that drops it under-reports the only row carrying commercial
    # risk, so "leave it at 20" was the costly way to be wrong.
    #
    # 🟢 The durable fix is not picking a winner: it is making the SCOPE part of the claim.
    # A bare "20 MCP server slugs" cannot be checked, because three defensible scopes give
    # 19, 20 and 21.  Both scopes are registered below, each with its boundary in code.
    m["mcp_slugs_in_mcp_section"] = len({
        s.lower() for line in _section_rows(top, "### Agents over the systems")
        for s in SLUG_RE.findall(line) if MCP_HINT.search(s)
    })

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

    # permissive rows in agents/top.md's build-on tier.
    # 🟢 p278 (`p277`'s declared item 3): the boundary is STRUCTURAL now -- the tier heading
    # to the NEXT `## ` heading -- and no longer a copy of the number under test.
    # 🔴 What it replaced, and why: p277 bounded this tier with the literal string
    # `"**24 permissive rows"`.  Correcting the shelf to `27` DELETED that boundary, so the
    # measurement silently became "every table row in the rest of the file" and reported 63.
    # The verdict stayed STALE for an entirely new reason -- a red gate that looks like the
    # same red gate, which is the shape that survives a careless pass.  A checker anchored on
    # the stale text cannot survive the correction it asks for.
    # 🔵 A `## ` heading cannot be deleted by fixing a numeral, so this boundary is stable
    # under exactly the edit that broke the last one.
    m["permissive_rows_in_build_on_tier"] = len(_tier_rows(top, "## Build-on-this tier"))
    return m


# 🟢 p278 — `published` IS READ FROM THE SHELF NOW, not carried as a Python constant.
#
# `p277` declared this defect precisely: *"`published` turns out to be a Python CONSTANT, not
# a value read from the shelf — so `T37` detects ROW drift and is BLIND TO TEXT drift."*  A
# pass that edited the sentence and not the literal left the gate green and the shelf wrong,
# the exact inverse of the failure `p277` hit.
#
# Each claim therefore carries an ANCHOR: (shelf, regex with one capturing group).  The
# published figure is whatever the shelf currently says, so BOTH drifts are now visible:
#   * the rows change and the sentence does not -> STALE (row drift, as before)
#   * the sentence changes and the rows do not  -> STALE (text drift, new)
#   * the sentence disappears entirely          -> NO-ANCHOR, which is a FAILURE, not a pass.
#
# 🔵 NO-ANCHOR must be loud.  A silently-missing anchor would read as "nothing to check",
# which is how `p277`'s deleted tier boundary hid for a pass.
#
# 🔵 Every anchor is WHITESPACE-TOLERANT (\s+, not a literal space).  These shelves are
# hard-wrapped prose: p278's own first anchor MISSED because the phrase it pinned wrapped
# across two lines, and a later pass merely REFLOWING a paragraph would otherwise delete the
# pin and fail the gate for a cosmetic edit.  An anchor that breaks on rewrapping is the same
# brittleness class as an anchor copied from the number under test.
#
# claim -> (measured key, anchor_file, anchor_regex, where it is published)
CLAIMS = [
    # 🔴 p278: corrected 20 -> 21 after reproducing BOTH predicates.  See the long note in
    # measure(): the 21st row is `AStheTECH/mewcp-google-classroom`, the proprietary one, and
    # p277's enumeration dropped it for the reason MCP_HINT's own comment already named.
    ("MCP server slugs tabled on agents/top.md (whole file, MCP_HINT)",
     "mcp_slugs_on_agents_top", "intel/trends.md",
     r"\*\*(\d+)\s+distinct\s+education\s+MCP\s+server\s+slugs\s+are\s+shelved",
     "intel/trends.md T21 + agents/top.md MCP section"),
    # 🟢 p278: the SCOPED companion.  Three defensible scopes give 19, 20 and 21, so a bare
    # count cannot be checked at all; registering the scope is the durable half of the fix.
    ("MCP server slugs in the MCP SECTION's table (agents/top.md)",
     "mcp_slugs_in_mcp_section", "agents/top.md",
     r"\*\*(\d+)\s+rows\s+in\s+the\s+table\s+below\*\*",
     "agents/top.md, the MCP section's own lead sentence (new at p278)"),
    ("LMS platforms reachable by MCP, agents/top.md", "lms_platforms_on_agents_top",
     "agents/top.md", r"\*\*(\d+)\s+platforms\*\*\s+are\s+reachable",
     "agents/top.md MCP section (p274). Was 3 on both shelves before this pass"),
    ("LMS platforms reachable by MCP, both agent shelves", "lms_platforms_on_agent_shelves",
     "intel/trends.md", r"MCP\s+reaches\s+\*\*(\d+)\s+distinct\s+LMS\s+platforms\*\*",
     "intel/trends.md T24 (p274). Was 3"),
    # 🟢 p275: 23 -> 24 (Athena re-graded).  🟢 p277: 24 -> 27 (p276's three unmoved rows).
    ("permissive rows in the build-on tier", "permissive_rows_in_build_on_tier",
     "agents/top.md", r"\*\*(\d+)\s+permissive\s+rows",
     "agents/top.md ('N permissive rows'), tier bounded STRUCTURALLY since p278"),
]


def published_of(root, anchor_file, anchor_re):
    """The figure the shelf CURRENTLY states, or None when the anchor is gone.

    None is not "no claim" -- it is a broken pin, and main() reports it as a failure.
    """
    text = read(root, anchor_file)
    if not text:
        return None
    hit = re.search(anchor_re, text)
    return int(hit.group(1)) if hit else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
    args = ap.parse_args()
    root = os.path.abspath(args.root)

    m = measure(root)
    out = sys.stdout
    out.write("# p274 -- T37 standing re-count.  Every number below is derived from the rows, "
              "not copied from the sentence that last stated it.\n")
    out.write("# p278 -- `published` is READ FROM THE SHELF, so TEXT drift is visible too.\n")
    out.write("claim\tpublished\tmeasured\tverdict\twhere_published\n")
    stale = 0
    broken = 0
    for claim, key, anchor_file, anchor_re, where in CLAIMS:
        measured = m[key]
        published = published_of(root, anchor_file, anchor_re)
        if published is None:
            verdict = "NO-ANCHOR"
            broken += 1
            shown = "-"
        else:
            verdict = "MATCH" if measured == published else "STALE"
            shown = published
            if verdict == "STALE":
                stale += 1
        out.write(f"{claim}\t{shown}\t{measured}\t{verdict}\t{where}\n")
    out.write(f"# STALE={stale} NO-ANCHOR={broken} of {len(CLAIMS)} registered claims\n")
    out.write("# MCP servers by platform, across agents/top.md AND agents/trending.md:\n")
    for p, slugs in m["_platform_detail"].items():
        out.write(f"#   {p}\t{len(slugs)}\t{', '.join(slugs)}\n")
    # 🔴 p278: a broken anchor is a FAILURE.  A pin that silently vanishes reads as "nothing
    # to check", which is exactly how p277's deleted tier boundary hid for a whole pass.
    if broken:
        out.write("# 🔴 NO-ANCHOR means the sentence this claim checks is GONE from the shelf. "
                  "Restore the sentence or re-point the anchor; do not ignore it.\n")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
