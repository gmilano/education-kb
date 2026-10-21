#!/usr/bin/env python3
"""`p354-grant-path` — ACTION ZZ-au: every PUBLISHED grant path must resolve `200`.

p353 found `sandraschi/classroom-mcp` published as **MIT, read at `main/LICENSE`**, which is
**404**.  The licence was real and the path was wrong: the default branch is `master`, and
`raw.githubusercontent.com` carries NO branch default, so a wrong branch fails **CLOSED** -- a
permissively licensed repository reads as ungranted.  p353 also established that this is a
REGRESSION rather than a discovery: `agents/top.md:1316` had already published the same
repository at `master` with the same byte count, so a later pass normalised a correct `master`
into an assumed `main`.

🔵 That is the whole argument for a gate rather than care.  A reader cannot see the difference
between `main/LICENSE` and `master/LICENSE` by looking, the wrong one looks exactly like a
repository with no grant, and the pass that introduced it had the right value in its own file.

So this instrument answers one question over the live shelves:

    for every published (slug, branch, path) grant claim -- does it resolve 200?

🟢 The OFFLINE half -- what `make hooks` runs -- is the EXTRACTOR.  It is the half that can be
wrong in a way nobody notices, because a claim it fails to see is a claim the online arm never
probes, and a silent under-count would make this gate report green over an unchecked corpus.
So the controls bind the PARSE, and the parser declares `NO-PATH` rows rather than dropping
them.

🔴 The extraction hazard, named, because it is this base's own recurring shape.  `p351` found
`THIRD_PARTY_SCOPE` (a licence token beside a slug belongs to something else); `p352` found the
same shape on a STAR FIGURE; `p353` found a cell that reads like a table header but is not.
The same shape appears here, and p353's own corrective row is the instance:

    | ... | 🔴 **`master/LICENSE`** -- corrected at p353; this cell read `main/LICENSE`,
            which is **404** | ...

🔴 **That cell names TWO paths, and one of them is named in order to be REFUTED.**  A parser
that takes the last, or takes all, probes `main/LICENSE`, gets the 404 p353 documented, and
reports a defect against the one cell on the shelf that was just repaired.  The gate would
accuse the correction.

🟢 **The rule is FIRST-WINS, and it is a contract rather than a convenience.**  The live claim
is the first backticked `branch/path` in the cell; anything after it is commentary -- a
superseded value, a comparison, a note.  This matches how every row on these shelves is
written (the asserted value leads, the history follows) and it is the only rule under which
p353's repaired cell parses to what p353 actually verified.

🔵 Bound honestly: FIRST-WINS is a rule about CELL ORDER, not about truth.  A pass that writes
the refuted path first would be mis-parsed by this instrument, and no gate here can catch that.
What this gate does guarantee is that whatever the cell asserts FIRST is reachable -- so a
cell whose leading path 404s is RED, which is exactly the p353 defect.
"""
import argparse
import os
import re
import sys

# 🔵 The six REWRITABLE shelves.  A file absent from the tree is skipped rather than fatal:
# this base's shelf set has changed before.
SHELF_FILES = [
    "agents/top.md", "repos/foundations.md", "verticals/solutions.md",
    "intel/market.md", "intel/trends.md", "compose/patterns.md",
]

# 🔴 `agents/trending.md` and `repos/trending.md` are APPEND-ONLY by the standing brief: every
# section in them is a dated record of what was true when it was measured, and nothing in them
# is ever rewritten.  They are EXCLUDED, and the exclusion is a contract rather than a
# convenience -- a gate that demanded a 2026-10-06 trending row's path resolve today would
# force exactly the retro-editing this base's `dated-by-measurement` convention forbids.
# 🟢 This is `p352`'s "only the live occurrence is judged" rule, applied to a whole file.
HISTORY_ONLY_SHELVES = ("agents/trending.md", "repos/trending.md")

# 🟢 Inside a rewritable shelf the same boundary is drawn by the shelves themselves, in a
# heading this base has carried since p339/p340:
#     `## ⏷ Carried history — everything below this line predates Pass 339 and was NOT
#      rewritten`
# Everything ABOVE it is live and answerable today; everything below is a dated record.
# 🔵 Matched on the stable token rather than the pass number, which varies by file (p339 on
# five shelves, p340 on `compose/patterns.md`) and will move again.
HISTORY_MARKER_RE = re.compile(r"^##\s*⏷?\s*Carried history", re.MULTILINE)


def live_region(text):
    """The part of a rewritable shelf that asserts something about TODAY.

    🔴 A shelf with NO marker is judged WHOLE rather than skipped.  The alternative fails
    open: a pass that dropped the heading would silently remove its file from this gate's
    scope, and a gate whose coverage can be reduced by deleting a line is not a gate.
    """
    m = HISTORY_MARKER_RE.search(text)
    return text if m is None else text[:m.start()]

# 🟢 A slug, in a markdown cell.  Accepts the bare and the `https://github.com/` forms, and
# stops at the characters markdown uses as furniture.  Trailing `.git` and a trailing `/` are
# presentation; `p348` settled that an address's identity is case-insensitive but its CASING is
# published, so the slug is returned as written and folded only for comparison.
_SLUG = r"[A-Za-z0-9][A-Za-z0-9._-]*/[A-Za-z0-9][A-Za-z0-9._-]*"
SLUG_RE = re.compile(r"https?://github\.com/(" + _SLUG + r")")

# 🔵 A grant path is `branch/path`, backticked, with at least one `/`.  The path half may carry
# further segments (`main/docs/License.txt` -- `p275` found a real grant at `docs/License.txt`)
# and an uppercase extension (`p283`'s ladder-case axis).
GRANT_CELL_RE = re.compile(r"`([A-Za-z0-9][A-Za-z0-9._/-]*?/[A-Za-z0-9][A-Za-z0-9._/-]*)`")

# 🔴 Template placeholders are NOT addresses and NOT paths.  `p351`'s `address_shape` rejects
# these on the slug side with a published denominator; the same shapes occur on the path side
# inside command examples (`raw.githubusercontent.com/<slug>/<branch>/<path>`), so they are
# rejected here too rather than probed.
PLACEHOLDER_TOKENS = ("<", ">", "{", "}", "OWNER", "REPO", "yourusername", "your-org",
                      "BRANCH", "PATH", "...", "$")

# 🟢 A grant lives in a FILE, so the last segment must look like one.  This is the only filter
# that is about meaning rather than shape, and it exists because a "Platform reached" or
# "What it does" cell can legitimately contain a backticked `a/b` that is not a path at all
# (`COLUNAS_DISTINCT_PERMITIDAS`, `refs/heads/master`, `ankimcp/anki-mcp-server-addon`).
# 🔵 Measured against the live shelves rather than guessed: every published grant path on this
# base ends in one of these.
#
# 🔴 THIS LADDER IS WRITTEN CASE-CLOSED, AND IT WAS NOT ON THE FIRST DRAFT.  The first draft
# listed lowercase spellings only and folded the candidate with `.lower()` forty lines below.
# `make gate-ladder-case` — p283's audit — graded it `STEM-ONLY` on the `licence` family and
# `SINGLE-SPELLING` on `notice` the moment this gate entered `HOOK_GATES`, breaching p286's
# ratchet (STEM-ONLY 3→4, SINGLE-SPELLING 17→18), and it was RIGHT to: p283's predicate is
# PROXIMITY, because *"an immunity claim resting on any unrelated string-folding in a 400-line
# script"* is the overclaim this base's instruments keep being caught by.
# 🟢 So the remedy is the one `p352` took when the same audit graded ITS anchor ladder: write
# the case variation into the literals, where an auditor can read it, rather than leave it
# implied by a distant fold.  Each family now varies stem case AND extension case.
# 🔵 The `.lower()` at the point of definition is what keeps BEHAVIOUR unchanged — membership
# is tested against a folded candidate, so the set must be folded too.  The uppercase literals
# are redundant to the match and load-bearing to the audit, which is the correct trade: the
# instrument says in code what it previously only did.
GRANT_BASENAMES = tuple(n.lower() for n in (
    "LICENSE", "LICENCE", "License", "Licence", "license", "licence",
    "LICENSE.md", "LICENSE.MD", "LICENCE.md", "LICENCE.MD", "License.md",
    "LICENSE.txt", "LICENSE.TXT", "LICENCE.txt", "LICENCE.TXT", "License.txt",
    "LICENSE.rst", "LICENSE.RST", "LICENSE-MIT", "LICENSE-APACHE",
    "LICENSE.apache", "LICENSE.mit", "UNLICENSE", "Unlicense",
    "COPYING", "Copying", "copying", "COPYING.txt", "COPYING.TXT", "Copying.txt",
    "NOTICE", "Notice", "notice", "NOTICE.txt", "NOTICE.TXT", "Notice.txt",
    "COPYRIGHT", "Copyright", "COPYRIGHT.txt", "COPYRIGHT.TXT",
))


def _is_placeholder(tok):
    return any(p in tok for p in PLACEHOLDER_TOKENS)


def _looks_like_grant_path(tok):
    """`main/LICENSE` yes; `refs/heads/master` no; `owner/repo` no.

    🔵 The basename test is case-insensitive because the ladder-case axis is real: `p347`
    found a grant whose `LICENSE` is a DIRECTORY and `p283` asked which ladders can find an
    uppercase extension.  Casing is published; matching is folded.
    """
    if "/" not in tok or _is_placeholder(tok):
        return False
    return tok.rsplit("/", 1)[-1].lower() in GRANT_BASENAMES


def split_row(line):
    """A markdown table row -> its cells, or None if the line is not a row.

    🔵 Leading and trailing pipes are furniture.  A line with fewer than three cells is not a
    data row on these shelves (every grant-bearing table is at least Name | Repo | Licence |
    Grant read at), and the separator row is dropped by the all-dashes test.
    """
    s = line.strip()
    if not s.startswith("|") or s.count("|") < 3:
        return None
    cells = [c.strip() for c in s.strip("|").split("|")]
    if all(set(c) <= set("-: ") and c for c in cells):
        return None  # the `|---|---|` separator
    return cells


# 🔴 THE SCOPE THAT MAKES THIS GATE CORRECT, and it was learned by getting it wrong.
#
# This instrument's FIRST run over the live tree reported three defects and all three were its
# own fault.  `agents/top.md:341` publishes `tests/stubs/LICENSE.md`, `:386` publishes
# `canvas-lms-mcp/LICENSE`, `:387` publishes `packages/xapi/LICENSE` -- every one a TRUE,
# first-hand, REPO-RELATIVE path, and every one read by a `branch/path` parser as a branch
# called `tests`, `canvas-lms-mcp` or `packages`.  Probed as raw URLs they 404, so the gate
# accused three correct cells.
#
# 🔵 That is this base's own recurring shape for the fourth consecutive pass -- `p351` on a
# licence (`THIRD_PARTY_SCOPE`), `p352` on a star figure, `p353` on a cell that reads like a
# table header, and now on a PATH:
#
#     🔵 A token's MEANING is given by the cell it sits in, never by its shape.
#
# `master/docs/License.txt` and `packages/xapi/LICENSE` are the same shape and different
# claims, so no amount of regex can separate them.  🟢 **What separates them is the COLUMN.**
# The live tiers publish a dedicated `Grant read at` column holding exactly a `branch/path`
# for a raw read; a pass write-up's table has no such column and its path cells are
# tree-relative. So the parse binds to the HEADER, which is structural, cannot be fooled by
# prose, and is precisely the set `ACTION ZZ-au` means by "every published grant path".
GRANT_COLUMN_HEADERS = ("grant read at",)


def _norm_header(cell):
    return re.sub(r"\s+", " ", re.sub(r"[`*]", "", cell)).strip().lower()


def extract(text, path_label):
    """Every published grant claim in one shelf, bound to the `Grant read at` column.

    Returns a list of dicts: file, line, slug, branch, path, verdict.
    🟢 `verdict` is `CLAIM` for a parsed (slug, branch, path), or `NO-PATH` for a row that
    sits in a grant-bearing table, names a slug, and carries no readable path in that
    column.  A `NO-PATH` row is DECLARED rather than dropped, because a parser that
    silently loses rows makes this gate report green over a corpus it never read.
    """
    out = []
    col = None  # the live `Grant read at` index, reset at every table boundary
    for n, line in enumerate(text.splitlines(), 1):
        cells = split_row(line)
        if cells is None:
            # 🔵 A non-row ends the table.  Without this the column index would leak into
            # the next table, which is how a parser reads one table's grammar into another.
            if not line.strip().startswith("|"):
                col = None
            continue
        norm = [_norm_header(c) for c in cells]
        hit = [i for i, h in enumerate(norm) if h in GRANT_COLUMN_HEADERS]
        if hit:
            col = hit[0]
            continue  # a header row is never data (p277 / gate-tables, from the other side)
        if col is None or col >= len(cells):
            continue
        slugs = SLUG_RE.findall(line)
        if not slugs:
            continue
        # 🔵 One row, one subject: the FIRST slug is the row's subject.  A later slug in the
        # same row is a fork, an upstream or a companion -- `p343` corrected a row that named
        # a fork, and `p351`'s THIRD_PARTY_SCOPE is this same confusion on a licence.
        slug = slugs[0]
        # 🟢 FIRST-WINS *inside the bound cell*.  See the module docstring: the asserted
        # value leads and the commentary follows, which is the only rule under which p353's
        # repaired `master/LICENSE` cell parses to what p353 actually verified.
        claim = None
        for tok in GRANT_CELL_RE.findall(cells[col]):
            if _looks_like_grant_path(tok):
                claim = tok
                break
        if claim is None:
            out.append({"file": path_label, "line": n, "slug": slug, "branch": "",
                        "path": "", "verdict": "NO-PATH"})
            continue
        branch, rest = claim.split("/", 1)
        out.append({"file": path_label, "line": n, "slug": slug, "branch": branch,
                    "path": rest, "verdict": "CLAIM"})
    return out


def harvest(root):
    """Every LIVE grant claim across the rewritable shelves, in file order.

    🔵 Scope, stated rather than implied: the two append-only trending shelves are excluded
    whole, and each rewritable shelf is cut at its `Carried history` marker.  What this gate
    judges is exactly the set of paths these shelves assert are readable TODAY.
    """
    claims = []
    for rel in SHELF_FILES:
        if rel in HISTORY_ONLY_SHELVES:
            continue
        full = os.path.join(root, rel)
        if not os.path.isfile(full):
            continue
        with open(full, encoding="utf-8") as fh:
            claims.extend(extract(live_region(fh.read()), rel))
    return claims


def raw_url(slug, branch, path):
    return "https://raw.githubusercontent.com/%s/%s/%s" % (slug, branch, path)


# ─────────────────────────────────────────────────────────────────────────────
# 🔴 ONLINE arm.  OUT of `hooks` -- `make gate-grant-path-online`.  Needs egress to
# raw.githubusercontent.com, which p353 recorded OPEN while github.com and api.github.com
# are 403.
# 🔵 It CALIBRATES first, in the shape `p293` settled: a channel that answers 404 for
# everything would report every row dead, so a known-good and a known-absent path are probed
# before any verdict is issued, and a failed control pair yields NO verdict rather than a
# guess.
# ─────────────────────────────────────────────────────────────────────────────
CALIBRATION = (
    # (slug, branch, path, expected)  -- the positive is this base's anchor row, the negative
    # is p353's own documented 404, so the control pair is drawn from measured history.
    ("HKUDS/DeepTutor", "main", "LICENSE", 200),
    ("sandraschi/classroom-mcp", "main", "LICENSE", 404),
)


def probe(url, timeout=25):
    """HEAD-equivalent status for one raw URL, via curl.  Returns an int or 0."""
    import subprocess
    try:
        r = subprocess.run(
            ["curl", "-sS", "-o", os.devnull, "-w", "%{http_code}",
             "--max-time", str(timeout), url],
            capture_output=True, text=True, timeout=timeout + 10)
        return int((r.stdout or "0").strip() or 0)
    except Exception:
        return 0


def run_online(root, out_path=None):
    print("── p354-grant-path ONLINE — ACTION ZZ-au: every published grant path resolves 200")
    cal = []
    for slug, branch, path, want in CALIBRATION:
        got = probe(raw_url(slug, branch, path))
        cal.append((slug, branch, path, want, got))
        print("   calibration  %-34s %s/%s  want=%s got=%s  %s"
              % (slug, branch, path, want, got, "OK" if got == want else "BAD"))
    if any(got != want for _, _, _, want, got in cal):
        print("🔴 REFUSED — the control pair did not reproduce, so this channel issues NO "
              "verdict (p293: a miscalibrated read is worse than no read).")
        return 2

    claims = harvest(root)
    rows, bad, nopath = [], [], []
    seen = set()
    for c in claims:
        if c["verdict"] == "NO-PATH":
            nopath.append(c)
            continue
        key = (c["slug"].lower(), c["branch"], c["path"])
        if key in seen:
            continue
        seen.add(key)
        url = raw_url(c["slug"], c["branch"], c["path"])
        code = probe(url)
        c["code"] = code
        rows.append(c)
        if code != 200:
            bad.append(c)

    print("")
    print("   cifra\tvalor")
    print("   grant_claims_published\t%d" % len([c for c in claims if c["verdict"] == "CLAIM"]))
    print("   distinct_probed\t%d" % len(rows))
    print("   resolved_200\t%d" % len([r for r in rows if r["code"] == 200]))
    print("   NOT_200\t%d" % len(bad))
    print("   rows_without_a_path\t%d" % len(nopath))

    if out_path:
        with open(out_path, "w", encoding="utf-8") as fh:
            fh.write("archivo\tlinea\tslug\tbranch\tpath\thttp\tveredicto\n")
            for r in rows:
                fh.write("%s\t%d\t%s\t%s\t%s\t%d\t%s\n" % (
                    r["file"], r["line"], r["slug"], r["branch"], r["path"], r["code"],
                    "ALIVE" if r["code"] == 200 else "DEAD"))
            for r in nopath:
                fh.write("%s\t%d\t%s\t\t\t\tNO-PATH\n" % (r["file"], r["line"], r["slug"]))
        print("   evidencia\t%s" % out_path)

    if bad:
        print("")
        print("🔴 FAIL — %d published grant path(s) do not resolve 200:" % len(bad))
        for r in bad:
            print("   %s:%d  %s  %s/%s  HTTP %d"
                  % (r["file"], r["line"], r["slug"], r["branch"], r["path"], r["code"]))
        return 1
    print("🟢 PASS — every published grant path resolves 200.")
    return 0


def run_offline(root):
    """What `make hooks` can prove without egress: the PARSE, with a denominator."""
    claims = harvest(root)
    good = [c for c in claims if c["verdict"] == "CLAIM"]
    nopath = [c for c in claims if c["verdict"] == "NO-PATH"]
    print("   cifra\tvalor")
    print("   grant_claims_parsed\t%d" % len(good))
    print("   distinct_slug_branch_path\t%d"
          % len({(c["slug"].lower(), c["branch"], c["path"]) for c in good}))
    print("   rows_without_a_path\t%d" % len(nopath))
    branches = {}
    for c in good:
        branches[c["branch"]] = branches.get(c["branch"], 0) + 1
    for b in sorted(branches, key=lambda k: (-branches[k], k)):
        print("   branch:%s\t%d" % (b, branches[b]))
    # 🔵 No assertion on the COUNT.  A gate that pinned the denominator would go red every
    # time a pass adds a row, which is noise rather than a finding -- and `p352` settled that
    # a census stated in the pass that writes is stale by construction.  What `hooks` proves
    # here is that the extractor still runs over the live tree and still sees claims; the
    # 200-check is the online arm's, by `ACTION ZZ-au`'s own wording.
    if not good:
        print("🔴 FAIL — the extractor found ZERO grant claims on the live shelves.  Either "
              "the shelves stopped publishing grant paths or this parser broke; both are "
              "findings and neither is green.")
        return 1
    print("🟢 PASS — %d grant claims parse; run `make gate-grant-path-online` for the 200s."
          % len(good))
    return 0


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--root", help="repository root to judge")
    ap.add_argument("--online", action="store_true", help="probe every path (needs egress)")
    ap.add_argument("--out", help="evidence TSV to write (online only)")
    args = ap.parse_args(argv)
    # 🔵 P541: no input is a REFUSAL (exit 2), never a pass.  A gate that reports green on an
    # empty argument list is the masking shape `p300`'s runner exists to prevent.
    if not args.root:
        print("🔴 REFUSED — no --root given.  This gate judges a tree; it does not assume one.")
        return 2
    if not os.path.isdir(args.root):
        print("🔴 REFUSED — --root %r is not a directory." % args.root)
        return 2
    if args.online:
        return run_online(args.root, args.out)
    return run_offline(args.root)


if __name__ == "__main__":
    sys.exit(main())
