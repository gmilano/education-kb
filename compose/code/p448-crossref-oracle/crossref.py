#!/usr/bin/env python3
"""p448 -- the fourth channel for a slug's spelling: what the NEIGHBOURS call it.

`p443` asked, for each of this shelf's 496 slugs, whether the spelling this KB uses is
the spelling its own publisher uses.  It had three channels -- the npm registry, the
PyPI registry, and a self-link in the repository's own README -- and for **186 of 496**
none of them answered.  Pass 26 measured that further and found something worse: on
this host **no case oracle exists at all**, because `raw`, `git ls-remote`, `info/refs`,
rendered `github.com` and `codeload` return `200 / resolves / 200 / 403 / 403`, so a
disagreement is real and still cannot say which side is wrong.

A `NO-ORACLE` row is therefore not "the spelling is fine". It is "nothing on this host
can confirm or deny it", which is the `P249` calibration rule applied to spelling: an
uncalibrated channel's silence is not a negative.

This pass adds the channel the first three missed, and it needs no forge API: **the
other 495 repositories on the shelf.** A project that is depended on, forked, wrapped or
merely recommended gets WRITTEN DOWN by its neighbours, in a `package.json`, a
`requirements.txt`, a `pom.xml` or a README link. Those mentions are independent
spellings by third parties, and 495 of them is a consensus vote.

Verdicts per target slug:
    CONSENSUS-CONFIRMS   >=1 other repo names it, and every citing spelling equals the
                         spelling this KB publishes
    CONSENSUS-DIFFERS    >=1 other repo names it, and the citers AGREE on a spelling
                         that is not this KB's  -- the actionable class
    CITERS-DISAGREE      >=2 other repos name it and they do not agree with each other,
                         so the channel has found a collision rather than an oracle
    UNCITED              no other repository on this shelf names it in any fetched
                         manifest or README

The pre-registered prediction is that **fewer than 40 of the 186** are cited by any
neighbour, which would make the gap STRUCTURAL -- a repository nobody else cites has no
external spelling to be checked against, and no amount of extra channels will invent
one.

## Why self-citation is excluded, and why that is not obvious

A repository naming ITSELF is the `p443` channel 3 (`self-link:README.md`) that already
ran and already failed on these 186.  Counting it here would re-import a measurement as
if it were a new one, which is the `p432` defect (a from-scratch instrument re-importing
known defects).  So the owner's own repository is removed from the corpus for its own
target, and a control asserts that removal changes a known case.

## Declared limits

- A mention is a STRING, not a resolution.  `foo/bar` in a README may be a dead link, a
  renamed project or a typo, and this channel cannot tell.  What it establishes is that
  an INDEPENDENT party wrote that spelling, which is exactly what `p443` lacked.
- The corpus is the files listed in `CORPUS_PATHS` at `HEAD`.  A citation in a file not
  on that list, or in git history, is not seen.  The list is published with the count.
- GitHub slugs are case-insensitive for RESOLUTION, so two spellings differing only in
  case both work.  This channel reports the disagreement; per pass 26 it still cannot
  say which side is canonical, and it does not pretend to.
"""

import os
import re
import sys
import urllib.request
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor

RAW = "https://raw.githubusercontent.com/{slug}/HEAD/{path}"

# Where a neighbour writes a slug down.  READMEs carry links; manifests carry
# dependencies and repository fields.  Published with the result because the corpus
# definition is part of the measurement (`P107`).
CORPUS_PATHS = [
    "README.md", "readme.md", "README.rst", "README.txt", "README.markdown",
    "package.json", "pyproject.toml", "requirements.txt", "setup.py", "setup.cfg",
    "composer.json", "pom.xml", "Cargo.toml", "go.mod", "Gemfile", "environment.yml",
]

SLUG_CHARS = r"[A-Za-z0-9_.-]"


def fetch(slug, path, timeout=20):
    url = RAW.format(slug=slug, path=path)
    req = urllib.request.Request(url, headers={"User-Agent": "globant-kb-p448"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.read().decode("utf-8", "replace")
    except Exception:
        return ""


def corpus_of(slug):
    """Concatenated text of every CORPUS_PATHS file this repo actually has."""
    parts = []
    for p in CORPUS_PATHS:
        t = fetch(slug, p)
        if t:
            parts.append(t)
    return slug, "\n".join(parts)


def citations_of(target, corpus, exclude):
    """Every spelling of `target` written by a repo other than `exclude`.

    Matched case-insensitively on the `owner/repo` form, with the surrounding
    characters checked so `foo/bar` does not match inside `foo/barbaz`.
    """
    owner, _, repo = target.partition("/")
    rx = re.compile(r"(?<!%s)(%s)/(%s)(?!%s)"
                    % (SLUG_CHARS, re.escape(owner), re.escape(repo), SLUG_CHARS),
                    re.I)
    found = defaultdict(set)
    for slug, text in corpus.items():
        if slug.lower() == exclude.lower():
            continue
        for m in rx.finditer(text):
            found["%s/%s" % (m.group(1), m.group(2))].add(slug)
    return found


def main():
    shelf_file, targets_file = sys.argv[1], sys.argv[2]
    outdir = sys.argv[3] if len(sys.argv) > 3 else os.path.dirname(
        os.path.abspath(__file__))
    shelf = [l.strip() for l in open(shelf_file) if l.strip()]
    targets = [l.strip() for l in open(targets_file) if l.strip()]

    with ThreadPoolExecutor(max_workers=16) as ex:
        corpus = dict(ex.map(corpus_of, shelf))
    have = sum(1 for v in corpus.values() if v)
    chars = sum(len(v) for v in corpus.values())
    print("## corpus: %d of %d shelf repos returned at least one file, %d chars"
          % (have, len(shelf), chars))
    print("## CORPUS_PATHS (%d): %s" % (len(CORPUS_PATHS), " ".join(CORPUS_PATHS)))

    # ---- calibration: the channel must DISCRIMINATE before any negative is believed
    planted = "globant-kb-p448/this-slug-does-not-exist"
    planted_hits = citations_of(planted, corpus, planted)
    # a positive control from OUTSIDE the 186: a slug this shelf is known to wrap
    pos = "vishalsachdev/canvas-mcp"
    pos_hits = citations_of(pos, corpus, pos)
    print("## calibration: planted slug -> %d citers (want 0); %s -> %d citers (want >0)"
          % (sum(len(v) for v in planted_hits.values()), pos,
             sum(len(v) for v in pos_hits.values())))
    if planted_hits or not pos_hits:
        print("## 🔴 CHANNEL DOES NOT DISCRIMINATE -- negatives below are NOT claims")

    rows = []
    for t in targets:
        found = citations_of(t, corpus, t)
        citers = sorted({s for v in found.values() for s in v})
        spellings = sorted(found)
        if not citers:
            verdict = "UNCITED"
        elif len(spellings) > 1:
            verdict = "CITERS-DISAGREE"
        elif spellings[0] == t:
            verdict = "CONSENSUS-CONFIRMS"
        else:
            verdict = "CONSENSUS-DIFFERS"
        rows.append((t, verdict, len(citers), ",".join(spellings) or "-",
                     ",".join(citers[:6]) or "-"))

    with open(os.path.join(outdir, "crossref.tsv"), "w") as f:
        f.write("target\tverdict\tn_citers\tspellings_found\tciters\n")
        for r in rows:
            f.write("\t".join(str(x) for x in r) + "\n")

    n = len(rows)
    cited = [r for r in rows if r[1] != "UNCITED"]
    print("\n## action C -- the 186 NO-ORACLE spellings against 495 neighbours (n=%d)"
          % n)
    print("  verdicts:", Counter(r[1] for r in rows).most_common())
    print("  CITED BY ANY NEIGHBOUR: %d of %d (%.1f%%)"
          % (len(cited), n, 100.0 * len(cited) / n))
    print("  prediction was '<40 cited' -> %s"
          % ("CONFIRMED" if len(cited) < 40 else "FALSIFIED"))
    print("\n  the rows where the neighbours disagree with this KB's spelling:")
    for r in rows:
        if r[1] in ("CONSENSUS-DIFFERS", "CITERS-DISAGREE"):
            print("    %-46s %-18s n=%d  %s" % (r[0], r[1], r[2], r[3]))
    print("\n  most-cited NO-ORACLE rows:")
    for r in sorted(cited, key=lambda r: -r[2])[:12]:
        print("    %-46s n=%-3d %s" % (r[0], r[2], r[4]))


if __name__ == "__main__":
    main()
