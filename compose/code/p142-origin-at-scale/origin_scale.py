"""p142-origin-at-scale — `ACTION DH`: the commit-offset channel on the whole connector tier.

p141 pre-registered:

> Apply the commit-offset channel at scale: run `p141-repo-origin-layer` over the **43-row
> GitHub connector population** on `agents/top.md`, which is not npm-published and so was never
> in `ACTION CY`'s subject set. 🔴 *Refuted if the offset channel places no row that the payload
> channel could not -- which would mean it is a redundant instrument rather than an additional
> one, and `T29` should not have gained a second clause.* 🔵 **And report the LATAM count
> explicitly, including when it is zero.**

## The instrument is p141's, imported rather than re-typed

`OFFSET_REGION`, `AMBIGUOUS`, `NO_SIGNAL`, `book()` and `offsets()` are imported from
`p141-repo-origin-layer/repo_origin.py` and are not redefined here. A sweep that reimplements
its instrument cannot tell a changed verdict from a changed method; only the population is new.

## Two changes this probe DOES make, and why each is a defect in p141 rather than a preference

🔴 **1. `anthropic.com` was being counted as an institutional email domain.** p141's agent-tier
TSV reports `anthropic.com(59)` for `tutor-mcp` and `anthropic.com(98)` for `OpenTutor` under the
column `institutional_email_domains`. Those are not institutions: they are the author/committer
address an AI coding tool writes, which p141 itself measured from the other end (*"151 of 191
commits carry a `Co-Authored-By: Claude` trailer"*). Left in, the column would place a repository
in whichever country a tool vendor is incorporated. 🔵 **Nothing was booked off it** -- the region
column is driven by offsets alone -- so this corrects a misleading column, not a published
region. Tool addresses are now reported in their own `tool_mail` column.

🔴 **2. `git ls-files` reads the index, which a `--no-checkout` clone does not have.** The
population here is 44 repositories cloned `--filter=blob:none --no-checkout`, because only commit
metadata is needed and the blobs are not. `ls-files` returns empty in such a clone -- so a
funding file would be reported absent for every row, silently. `git ls-tree -r --name-only HEAD`
is used instead, and `test_origin_scale.py` pins that an unchecked-out clone still finds a known
path.

The offset table itself, and in particular its refusal to book the five offsets shared between
North America and LATAM, is untouched.
"""

import importlib.util
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
_P141 = os.path.join(HERE, "..", "p141-repo-origin-layer", "repo_origin.py")
_spec = importlib.util.spec_from_file_location("p141_repo_origin", _P141)
p141 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(p141)

book = p141.book
offsets = p141.offsets
PERSONAL_MAIL = p141.PERSONAL_MAIL

# 🔴 Addresses an AI coding tool writes into authorship. Not a location, not an institution.
TOOL_MAIL = {
    "anthropic.com", "openai.com", "cursor.com", "users.noreply.github.com",
    "bot.github.com", "github-actions.bot", "dependabot.com", "copilot.github.com",
}


def _git(repo, *args):
    return subprocess.run(["git", "-C", repo, *args], capture_output=True,
                          text=True, timeout=180).stdout


def email_classes(repo):
    """(institutional, tool, personal) domain histograms from author AND committer."""
    out = _git(repo, "log", "--format=%ae%n%ce")
    counts = {}
    for line in out.splitlines():
        if "@" in line:
            d = line.strip().rsplit("@", 1)[-1].lower()
            counts[d] = counts.get(d, 0) + 1
    inst, tool, pers = {}, {}, {}
    for d, n in counts.items():
        if d in TOOL_MAIL:
            tool[d] = n
        elif d in PERSONAL_MAIL:
            pers[d] = n
        else:
            inst[d] = n
    return inst, tool, pers


def tracked_paths(repo):
    """🔴 ls-tree, not ls-files: a --no-checkout clone has no index."""
    out = _git(repo, "ls-tree", "-r", "--name-only", "HEAD")
    return out.splitlines()


def funding_files(repo):
    return [p for p in tracked_paths(repo)
            if "funding" in p.lower() and "node_modules/" not in p]


def _fmt(h):
    return ",".join("%s(%d)" % (d, n) for d, n in sorted(h.items())) or "NONE"


COLS = ["subject", "commits", "head_date", "institutional_mail", "tool_mail",
        "funding_files", "dominant_offset", "region", "evidence_kind", "note"]


def row(subject, clone):
    commits = _git(clone, "rev-list", "--count", "HEAD").strip() or "0"
    head = _git(clone, "log", "-1", "--format=%ad", "--date=short").strip() or "-"
    inst, tool, _ = email_classes(clone)
    offs = offsets(clone)
    region, note, ev = book(offs)
    return dict(zip(COLS, [
        subject, commits, head, _fmt(inst), _fmt(tool),
        ",".join(funding_files(clone)) or "NONE",
        ev, region, "TZ_OFFSET" if region != "UNMAPPED" else "NONE", note]))


def main(argv):
    """argv: subject=clone_path pairs."""
    rows = []
    for spec in argv:
        subject, _, clone = spec.partition("=")
        if not clone or not os.path.isdir(os.path.join(clone, ".git")):
            rows.append(dict(zip(COLS, [subject, "-", "-", "-", "-", "-", "-",
                                        "UNMAPPED", "NO_CLONE", "no readable clone"])))
            continue
        rows.append(row(subject, clone))
    print("\t".join(COLS))
    for r in rows:
        print("\t".join(str(r[c]) for c in COLS))

    by = {}
    for r in rows:
        by.setdefault(r["region"], []).append(r["subject"])
    total = len(rows)
    placed = total - len(by.get("UNMAPPED", []))
    print("\n# population %d; PLACED %d (%.0f%%); UNMAPPED %d"
          % (total, placed, 100.0 * placed / total if total else 0,
             len(by.get("UNMAPPED", []))), file=sys.stderr)
    for region in ("North America", "EMEA", "APAC", "LATAM"):
        names = by.get(region, [])
        print("# %-14s %2d  %s" % (region, len(names), ", ".join(sorted(names)) or "-"),
              file=sys.stderr)
    # 🔵 Reported explicitly, including when it is zero. p141 asked for exactly this.
    print("# 🔴 LATAM count: %d of %d" % (len(by.get("LATAM", [])), total), file=sys.stderr)
    refusals = [r["subject"] for r in rows if "AMBIGUOUS" in r["note"]]
    print("# bookings REFUSED as cross-region ambiguous: %d  %s"
          % (len(refusals), ", ".join(sorted(refusals)) or "-"), file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
