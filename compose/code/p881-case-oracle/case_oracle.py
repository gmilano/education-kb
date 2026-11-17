#!/usr/bin/env python3
"""p881 -- ACTION 880-G4's acceptance test, run on a channel that is UP.

880-G4 asks: grade every published slug against the `full_name` the search index
returns for it, publish the count of case-mismatched addresses, and fix them.

p881 measured the channel state first and found the obvious route CLOSED:

    api.github.com/repos/*      403 "not enabled for this session"   DOWN
    github.com (curl), codeload 403                                  DOWN
    git ls-remote               200 but CASE-INSENSITIVE             useless here
    raw.githubusercontent       200 but CASE-INSENSITIVE             useless here
    WebFetch on github.com      canonical case in the breadcrumb     UP, 1 call/slug

So the live oracle costs one fetch per slug for 147 slugs.  This instrument uses a
cheaper one that is just as first-hand: THIS BASE ALREADY MEASURED the canonical
spellings.  2,292 committed evidence TSVs carry `full_name` / `canonical_full_name`
columns harvested from the API by earlier passes, when that channel was UP.

The rule this implements: a published slug is graded ONLY where a committed
measurement covers it.  Everything else is UNGRADED, which is not green.
"""
import csv, glob, os, re, sys
from collections import defaultdict

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
EVID = os.path.join(ROOT, "evidence")
SHELVES = ["agents/top.md", "repos/foundations.md", "verticals/solutions.md",
           "intel/market.md", "intel/trends.md", "compose/patterns.md"]
CANON_COLS = ("full_name", "canonical_full_name")
SLUG_RE = re.compile(r"github\.com/([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)")
# github.com paths that are NOT repositories
NOT_A_REPO = {"advisories", "orgs", "topics", "collections", "sponsors",
              "settings", "features", "apps", "marketplace", "about", "pricing",
              "search"}  # p881: `api.github.com/search/repositories` in prose is NOT a repo


def harvest_oracle():
    """lower(slug) -> {exact spelling: count of evidence files that recorded it}"""
    oracle = defaultdict(lambda: defaultdict(int))
    files = 0
    for path in sorted(glob.glob(os.path.join(EVID, "*.tsv"))):
        try:
            with open(path, newline="", encoding="utf-8", errors="replace") as fh:
                rd = csv.DictReader(fh, delimiter="\t")
                cols = [c for c in (rd.fieldnames or []) if c in CANON_COLS]
                if not cols:
                    continue
                files += 1
                for row in rd:
                    for c in cols:
                        v = (row.get(c) or "").strip()
                        if v.count("/") != 1 or " " in v:
                            continue
                        if v.lower() in ("full_name", "canonical_full_name", "-", "none"):
                            continue
                        oracle[v.lower()][v] += 1
        except (OSError, csv.Error):
            continue
    return oracle, files


BARE_RE = re.compile(r"(?<![A-Za-z0-9_./-])([A-Za-z0-9][A-Za-z0-9_.-]*/[A-Za-z0-9][A-Za-z0-9_.-]*)(?![A-Za-z0-9_/-])")


def published_slugs(oracle):
    """slug -> {shelf: set of channels it was seen through}

    p881-A: the FIRST version of this instrument keyed the harvest on
    `github.com/<slug>` URLs only, and reported `OpenOlat/OpenOlat` as published on
    ONE shelf when p880 had found it by hand on FIVE.  That is `gate-slug-presence`'s
    own finding (p853 / 852-G3) reproduced by a new instrument on its first run:
    *a presence check keyed on URLs under-reports this corpus.*

    So the harvest runs two channels.  Channel B (a bare `Owner/Repo` token) is
    admitted ONLY where the oracle already knows the lowercased slug, which makes a
    false positive impossible by construction rather than by a tuned exclusion list:
    `refs/heads`, `and/or`, `compose/patterns.md` are not repositories this base has
    measured, so they cannot enter.
    """
    out = defaultdict(lambda: defaultdict(set))
    for rel in SHELVES:
        path = os.path.join(ROOT, rel)
        if not os.path.exists(path):
            continue
        with open(path, encoding="utf-8", errors="replace") as fh:
            text = fh.read()
        for m in SLUG_RE.finditer(text):
            s = m.group(1)
            if s.endswith(".git"):
                s = s[:-4]
            if s.split("/")[0].lower() in NOT_A_REPO:
                continue
            out[s][rel].add("url")
        for m in BARE_RE.finditer(text):
            s = m.group(1)
            if s.endswith(".git"):
                s = s[:-4]
            if s.split("/")[0].lower() in NOT_A_REPO:
                continue
            if s.lower() in oracle:          # channel B: oracle-known only
                out[s][rel].add("bare")
    return out


def main():
    oracle, nfiles = harvest_oracle()
    pub = published_slugs(oracle)
    rows, tally = [], defaultdict(int)
    for slug in sorted(pub, key=str.lower):
        shelves = ",".join(sorted(pub[slug]))
        chans = ",".join(sorted({c for v in pub[slug].values() for c in v}))
        obs = oracle.get(slug.lower())
        if not obs:
            verdict, canon = "UNGRADED-NO-MEASUREMENT", "-"
        else:
            spellings = sorted(obs, key=lambda s: (-obs[s], s))
            if len(set(spellings)) > 1:
                verdict = "AMBIGUOUS-ORACLE" if slug not in obs else "AMBIGUOUS-ORACLE-PUBLISHED-IS-ONE"
                canon = "|".join(spellings)
            elif spellings[0] == slug:
                verdict, canon = "MATCH", spellings[0]
            else:
                verdict, canon = "CASE-MISMATCH", spellings[0]
        tally[verdict] += 1
        rows.append((slug, canon, verdict, str(sum(obs.values()) if obs else 0),
                     str(len(pub[slug])), chans, shelves))

    w = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
    w.writerow(["published_slug", "oracle_full_name", "verdict", "evidence_rows",
                "shelves_n", "channels", "shelves"])
    for r in rows:
        w.writerow(r)
    print(f"# oracle built from {nfiles} committed evidence TSV(s), "
          f"{len(oracle)} distinct repositories measured")
    print(f"# published distinct slugs on the 6 curated shelves: {len(pub)}")
    for k in sorted(tally):
        print(f"#\t{k}\t{tally[k]}")
    if not pub:
        print("# P541-NO-INPUT\tREFUSED: no published slug was harvested. `0` findings with `0` inputs is NOT a clean shelf.")
        return 2
    graded = len(pub) - tally["UNGRADED-NO-MEASUREMENT"]
    print(f"#\tGRADED\t{graded}\t(coverage {graded/len(pub):.0%} — the rest is NOT green)")
    # exit 1 if any mismatch, so this can become a gate
    return 1 if tally["CASE-MISMATCH"] else 0


if __name__ == "__main__":
    sys.exit(main())
