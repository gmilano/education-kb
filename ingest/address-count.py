#!/usr/bin/env python3
"""address-count.py -- the instrument Gap 546-B demanded (p547).

WHY THIS EXISTS
  p545 reported "162 shelf addresses" on repos/foundations.md. p546 tried to
  reproduce it with five extraction rules and got 100 / 169 / 175 / 191 / 191.
  None of them yielded 162. p546 wrote: "This is not a claim that p545 was wrong
  -- it is a claim that nobody can tell", and registered Gap 546-B.

  The defect is not the number. It is that the number was PASS ARITHMETIC: a
  figure typed into prose by the pass that computed it, with the rule that
  produced it left in that pass's head. Gap 544-E was the same defect one level
  down (a carried "seventy-two" that understated the page by 84 rows).

  The durable fix is not a better number. It is that the rule ships WITH the
  number, as runnable code, so any later pass can re-derive it and disagree.

WHAT IT GUARANTEES
  1. Every rule is NAMED and its count is reported -- no rule is privileged by
     being the only one printed.
  2. One rule is designated CANONICAL and the designation is in this file, not
     in a pass's prose. Changing it is a diff, not a recollection.
  3. Non-repository GitHub paths (topics/, orgs/, sponsors/, ...) are excluded
     from the repository rules and the exclusion list is visible here.
  4. It takes the path as an argument, so it is not bound to one page.

USAGE   ./address-count.py [path.md ...]        (default: the four shelf pages)
OUTPUT  TSV: page  rule  count         plus a CANONICAL line per page.
"""
import re
import sys
import pathlib

# A GitHub owner path that is not a repository. Gap 546-B's fifth rule.
NOT_A_REPO = {
    "topics", "orgs", "sponsors", "collections", "features", "about",
    "pricing", "settings", "marketplace", "apps", "login", "join",
    "trending", "explore", "readme", "search", "notifications", "new",
}

# Gap 547-I, found by this script against the page that introduced it: writing the
# literal pattern `github.com/OWNER/REPO` inside a TABLE ROW makes that row match,
# so documenting the rule next to the count invented a phantom address named
# `owner/repo`. That is the "never leave an example row as data" defect, committed
# by the instrument's own documentation. Placeholder owners are therefore excluded,
# and the page prose now uses bracket glyphs as well -- two independent fixes,
# because either alone would regress the moment someone rewrites the other.
PLACEHOLDER = {
    "owner", "user", "username", "org", "organisation", "organization",
    "example", "your-org", "yourorg", "your-name", "someone", "foo", "repo",
    "slug", "account",
}

LINK_TEXT = re.compile(r"\[\s*([A-Za-z0-9._-]+/[A-Za-z0-9._-]+)\s*\]\(")
PAIR = re.compile(r"github\.com/([A-Za-z0-9._-]+)/([A-Za-z0-9._-]+)")

# The rule this base reports when it says "addresses on this page", stated here
# so that it is a diff and not a recollection. Chosen to match p546's third
# rule, the one it used for its own published denominators (175 / 98).
CANONICAL = "pairs_in_table_rows_deduped"


def is_repo(owner: str, repo: str) -> bool:
    o = owner.lower()
    return o not in NOT_A_REPO and o not in PLACEHOLDER


def strip_ext(repo: str) -> str:
    return repo[:-4] if repo.endswith(".git") else repo


def counts(text: str) -> dict:
    lines = text.splitlines()
    rows = [ln for ln in lines if ln.lstrip().startswith("|")]

    def pairs(src):
        out = set()
        for ln in src:
            for owner, repo in PAIR.findall(ln):
                repo = strip_ext(repo)
                if is_repo(owner, repo):
                    out.add(f"{owner}/{repo}".lower())
        return out

    link_text = {m.lower() for ln in rows for m in LINK_TEXT.findall(ln)}
    return {
        "markdown_link_text_is_owner_repo": len(link_text),
        "pairs_in_table_rows_deduped": len(pairs(rows)),
        "pairs_anywhere_on_page_deduped": len(pairs(lines)),
        "table_data_rows": sum(
            1 for ln in rows if not re.match(r"^\s*\|[\s|:-]+\|?\s*$", ln)
        ),
    }


def main(argv):
    pages = argv[1:] or [
        "agents/top.md", "repos/foundations.md",
        "verticals/solutions.md", "compose/patterns.md",
    ]
    print("page\trule\tcount")
    for p in pages:
        path = pathlib.Path(p)
        if not path.exists():
            print(f"{p}\tMISSING\t-")
            continue
        c = counts(path.read_text(encoding="utf-8", errors="replace"))
        for rule, n in sorted(c.items()):
            print(f"{p}\t{rule}\t{n}")
        print(f"{p}\tCANONICAL::{CANONICAL}\t{c[CANONICAL]}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
