#!/usr/bin/env python3
"""p436 — Gap 435-B leg 2: extract every `Promoted` claim from the trend shelves.

Gap 435-B: "There are 19 `Promoted` claims across the two trend shelves in at
least four different notations ... A regex over that prose would under-report
and call it green, which is worse than no gate."

So this does NOT try to be one regex.  It classifies each claim site by
NOTATION first, and extracts the (slug, target) pairs by the rule that notation
licenses.  Sites whose notation names no slug are emitted as UNRESOLVED rather
than dropped, which is the under-reporting Gap 435-B warns about.
"""
import os
import re
import sys

SLUG = re.compile(r"github\.com/([A-Za-z0-9](?:[A-Za-z0-9._-]*[A-Za-z0-9])?)/([A-Za-z0-9](?:[A-Za-z0-9._-]*[A-Za-z0-9])?)")
BACKTICK_SLUG = re.compile(r"`([A-Za-z0-9](?:[A-Za-z0-9._-]*[A-Za-z0-9])?/[A-Za-z0-9](?:[A-Za-z0-9._-]*[A-Za-z0-9])?)`")
PROMOTED = re.compile(r"\bPromoted\b", re.IGNORECASE)
# A claim site is POSITIVE only if its `Promoted` is not negated.  `\bPromoted\b`
# matches "deliberately NOT promoted", "cannot be promoted" and "still not
# promoted" -- which inverts the verdict and accuses rows whose absence is
# CORRECT.  Measured on this tree: 10 of 39 HEADER sites are negative claims.
NEGATED = re.compile(
    # Anchored BACKWARD from `promoted` over a short window that may not cross a
    # comma, semicolon, period or table pipe.  The wide version of this rule
    # ("never" within 40 chars) falsely negated
    # `agents/trending.md:8317` -- "nine never-before-seen slugs, two promoted" --
    # which is a POSITIVE claim.  Caught by the negative control, not by luck.
    r"(?:\bnot\b|\bnever\b|\bcannot\b|\bcan't\b|\bno\b|\bnone\b|\bnor\b)"
    r"[^.;,|]{0,25}?\bpromoted\b"
    r"|\bpromoted\b[ ]{0,3}(?:\*\*)?(?:none|zero|0)\b"
    r"|\bwhy (?:it )?is not promoted\b"
    # "rather than promoted" / "withdrawn rather than promoted" is a refusal.
    # Kept ADJACENT (<=12 chars, no comma) so it cannot reach across a clause.
    r"|\brather than[^.;,|]{0,12}?\bpromoted\b",
    re.IGNORECASE)
# Within a positive block, a decline marker opens a tier whose addresses are
# NOT claimed.  Truncate the block there rather than capturing them.
DECLINE_LINE = re.compile(
    r"Declin|Refus|NO-GRANT|no grant to read|not shelved|Deferred|not promoted",
    re.IGNORECASE)
HEADER = re.compile(r"^#{2,4}\s")
TARGETS = [
    ("agents/top.md", re.compile(r"agents/top\.md|\btop\.md\b|the curated tier|the shelf|the agent shelf|the MCP tier")),
    ("repos/foundations.md", re.compile(r"repos/foundations\.md|foundations\.md|\bfoundations\b")),
    ("verticals/solutions.md", re.compile(r"verticals/solutions\.md|solutions\.md")),
    ("intel/market.md", re.compile(r"intel/market\.md|market\.md")),
    ("intel/trends.md", re.compile(r"intel/trends\.md|trends\.md")),
    ("compose/patterns.md", re.compile(r"compose/patterns\.md|patterns\.md")),
]
SHELVES = [t for t, _ in TARGETS]


# p449 (`Gap 445-H`, registered by `p445` and carried untouched by `p446`-`p448` because
# "no gate run is available to verify a fix"): a backticked `a/b` whose OWNER position is a
# directory of THIS repository's own source tree is a LOCAL PATH, not a GitHub address.
# `lib/measure` is the specimen -- it held `gate-promotion-ledger` red from `p445` to `p448`
# as two C1-UNADJUDICATED promotion claims that name no repository at all.
# Safety, measured before narrowing rather than asserted: over all eight live shelves, each
# owner below was checked against every `github.com/<owner>/` URL on those same shelves.
# NONE of them is also a real GitHub owner here, so this arm drops 21 local paths and zero
# addresses.  The `github.com/...` extraction path above is untouched.
LOCAL_TREE_OWNER = frozenset({
    "lib", "src", "bin", "test", "tests", "docs", "doc", "scripts", "script",
    "compose", "evidence", "ingest", "archive", "scratchpad", "fixtures",
    "node_modules",
})


def slugs_in(text):
    out = []
    for owner, repo in SLUG.findall(text):
        repo = repo.rstrip(".")
        if repo.endswith(".git"):
            repo = repo[:-4]
        out.append("%s/%s" % (owner, repo))
    for s in BACKTICK_SLUG.findall(text):
        # a backticked a/b is a slug only if it is not a path to a .md/.tsv file
        if re.search(r"\.(md|tsv|json|sh|py|txt|xml|ts|yml|yaml)$", s):
            continue
        # p449 / `Gap 445-H`: nor is it a slug if its owner is this tree's own directory.
        if s.partition("/")[0].lower() in LOCAL_TREE_OWNER:
            continue
        out.append(s)
    seen, uniq = set(), []
    for s in out:
        if s not in seen:
            seen.add(s)
            uniq.append(s)
    return uniq


def targets_in(text):
    return [t for t, rx in TARGETS if rx.search(text)]


def notation(line):
    stripped = line.strip()
    if HEADER.match(stripped):
        return "HEADER"
    if stripped.startswith("|"):
        return "TABLE-CELL"
    if stripped.startswith("-") or stripped.startswith("*"):
        return "BULLET"
    return "PROSE"


def extract(path, label):
    with open(path, encoding="utf-8", errors="replace") as fh:
        lines = fh.read().splitlines()
    claims = []
    for i, line in enumerate(lines):
        if not PROMOTED.search(line):
            continue
        if NEGATED.search(line):
            claims.append((label, i + 1, "NEGATED", "", "", line.strip()[:200]))
            continue
        # a line that merely *discusses* the claim count is not a claim
        if re.search(r"`Promoted`\s+claims|claims across the two trend", line):
            claims.append((label, i + 1, "META", "", "", line.strip()[:200]))
            continue
        note = notation(line)
        here = slugs_in(line)
        tg = targets_in(line)
        if note == "HEADER" and not here:
            # a header claim licenses the block that follows it
            block = []
            for j in range(i + 1, min(i + 60, len(lines))):
                if HEADER.match(lines[j].strip()):
                    break
                if DECLINE_LINE.search(lines[j]):
                    break
                block.append(lines[j])
            here = slugs_in("\n".join(block))
            if not tg:
                tg = targets_in(line)
        if not here:
            claims.append((label, i + 1, note + "-UNRESOLVED", "", ";".join(tg), line.strip()[:200]))
            continue
        for s in here:
            claims.append((label, i + 1, note, s, ";".join(tg), line.strip()[:200]))
    return claims


def live_shelf_rows(root):
    """Slugs occupying a TABLE ROW on each live shelf -- not slugs merely mentioned.

    A mention is not a shelf row, and treating it as one hides the defect: p436's
    own decline note names `davemckain/qtiworks` in prose, and a mention-based
    read counted that DECLINED address as landed.  Measured difference on this
    tree: 142 un-landed by mention vs 148 by row.
    """
    live = {}
    for rel in SHELVES:
        p = os.path.join(root, rel)
        rows = set()
        if os.path.exists(p):
            with open(p, encoding="utf-8", errors="replace") as fh:
                for line in fh:
                    if line.lstrip().startswith("|"):
                        rows |= set(slugs_in(line))
        live[rel] = rows
    return live


def main(argv):
    if len(argv) != 1:
        sys.stderr.write("usage: claims.py REPO_ROOT\n")
        return 2
    root = argv[0]
    live = live_shelf_rows(root)
    live_any = set()
    for v in live.values():
        live_any |= v

    claims = []
    for rel, label in (("agents/trending.md", "agents/trending.md"),
                       ("repos/trending.md", "repos/trending.md")):
        p = os.path.join(root, rel)
        if not os.path.exists(p):
            sys.stderr.write("claims.py: missing %s\n" % rel)
            return 2
        claims += extract(p, label)

    print("source\tline\tnotation\tslug\tclaimed_target\tverdict\tpresent_in\tclaim_text")
    counts = {}
    for label, ln, note, slug, tg, text in claims:
        if not slug:
            verdict = {"META": "META", "NEGATED": "NEGATED"}.get(note, "UNRESOLVED")
            present = ""
        else:
            present = ";".join(r for r in SHELVES if slug in live[r])
            named = [t for t in tg.split(";") if t]
            if named:
                verdict = "LANDED" if any(slug in live[t] for t in named) else (
                    "MOVED" if slug in live_any else "NOT-LANDED")
            else:
                verdict = "LANDED-TARGET-UNNAMED" if slug in live_any else "NOT-LANDED"
        counts[verdict] = counts.get(verdict, 0) + 1
        print("\t".join([label, str(ln), note, slug, tg, verdict, present, text]))
    sys.stderr.write("claim rows=%d  %s\n" % (
        len(claims), "  ".join("%s=%d" % kv for kv in sorted(counts.items()))))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
