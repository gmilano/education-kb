#!/usr/bin/env python3
"""Gap 529-A instrument: compact every GitHub address in the KB into one index.

Why this exists.  The nine KB files are an append-only history of ~100k lines.
An address is described once, inside a dated pass section, and is thereafter
unreachable except by full-text search for a string nobody remembers -- so every
pass pays to rediscover addresses the base already owns.  p529 measured the
cost: of 80 census addresses, 25 were already in the history and only 9 had ever
reached a shelf, including the field's #1 and #2.

This reads the files the base already has and emits one row per address.  It
collects nothing from the network, so it is safe to run in front of every pass,
which is where the control belongs -- not after a rewrite.

Usage:
    python3 -I ingest/address-ledger.py [--repo-root .] [--out evidence/address-ledger.tsv]
    python3 -I ingest/address-ledger.py --debt     # unfiled addresses only
"""

import argparse
import glob
import os
import re
import sys

# The nine files.  CURATED are the ones a reader is pointed at -- an address
# present here is "filed".  HISTORY is the append-only record: an address that
# appears only here is owned-but-unfiled, which is exactly the debt 529-A names.
CURATED = [
    "agents/top.md",
    "repos/foundations.md",
    "verticals/solutions.md",
    "intel/market.md",
    "intel/trends.md",
    "compose/patterns.md",
]
HISTORY = [
    "agents/trending.md",
    "repos/trending.md",
    "intel/open-gaps.md",
]

ADDR = re.compile(r"github\.com/([A-Za-z0-9][A-Za-z0-9_.-]*)/([A-Za-z0-9][A-Za-z0-9_.-]*)")
HEADING = re.compile(r"^(#{1,6})\s")
# A `##` heading delimits a dated pass section.  The formats in use across the
# history are not one format -- `## 2026-10-16 - Pass 248`, `## Pass 240 -
# 2026-10-16`, `` ## 🆕 `p529` - `2026-10-29` `` and a Spanish `pase N` all
# appear -- so the pass token is read loosely and the NON-delimiters are
# excluded by name instead.  This matters: p530's first run of this instrument
# attributed 26,000 lines to `p209` because a `###` sub-heading mentioned that
# pass in passing, and min() over the file then reported p209 as the
# first_seen_pass of almost every address in the base.
# p531: the word forms are case-folded on their first letter; the BARE token
# stays case-sensitive, because this base writes passes lower-case (`p530`)
# and proposals upper-case (`P553`) and only the case separates them.  A
# blanket re.I here merges the two namespaces -- p531 tried it and
# p531-ledger-gate's C1 refuted it (1 128 sections -> 1 375, 4 ascending
# violations -> 13, "ascents" to p795/p865/p1024 that are proposal numbers).
# 🔴 The fold itself is load-bearing: `## ... (pass N) ...` and `## Live gaps
# declared by pass N` are 234 headings across the three history files and the
# p530 matcher saw NONE of them, so 212 sections -- 15.8% of the corpus --
# were attributed to the newer pass above them.
PASS_IN_HEAD = re.compile(r"`p(\d{1,4})`|\b[Pp]ass\s+(\d{1,4})\b|\b[Pp]ase\s+(\d{1,4})\b|\bp(\d{1,4})\b")
DATE_TOK = re.compile(r"(\d{4}-\d{2}-\d{2})")
# Headings that name a pass without being that pass's section: forward
# registrations and the gap-roll-up blocks that sit INSIDE a section.
# p531 adds the three roll-up dialects the fold exposed: `Actions opened by pN`,
# `Live gaps declared by pass N` and `The rows pass N changed`.  Each names a
# pass inside another pass's section; counting one as a section is what made
# `intel/open-gaps.md:17901` look like out-of-order history.
NOT_A_SECTION = re.compile(
    r"(🔜|Registered for|Pre-registered|Gaps OPEN after|Gaps CLOSED|"
    r"gaps opened|(Actions|Gaps)\s+(opened|closed)\s+(by|after)|"
    r"(Live\s+)?gaps\s+declared\s+(by|after)|"
    r"Verdicts on|rows pass|The rows? \S+ changed|one row pass)", re.I)

# Owners that are never a repository address: GitHub's own namespaces plus the
# path prefixes that appear in links to pages rather than repos.
NOT_OWNERS = {
    "orgs", "topics", "search", "features", "about", "pricing", "marketplace",
    "settings", "notifications", "explore", "sponsors", "collections", "apps",
    "login", "join", "new", "codespaces", "users", "site", "contact", "security",
}
# Trailing path segments that mean the second component is not the repo name.
STRIP_SUFFIX = re.compile(r"\.git$")

LICENCE_PATTERNS = [
    ("AGPL-3.0", re.compile(r"\bAGPL[- ]?3(\.0)?\b", re.I)),
    ("GPL-3.0", re.compile(r"(?<!A)\bGPL[- ]?3(\.0)?\b", re.I)),
    ("GPL-2.0", re.compile(r"(?<!A)\bGPL[- ]?2(\.0)?\b", re.I)),
    ("LGPL", re.compile(r"\bLGPL\b", re.I)),
    ("Apache-2.0", re.compile(r"\bApache[- ]?2(\.0)?\b", re.I)),
    ("ECL-2.0", re.compile(r"\bECL[- ]?2(\.0)?\b", re.I)),
    ("BSD", re.compile(r"\bBSD[- ]?\d?(-Clause)?\b", re.I)),
    ("MPL-2.0", re.compile(r"\bMPL[- ]?2(\.0)?\b", re.I)),
    ("CC0-1.0", re.compile(r"\bCC0\b", re.I)),
    ("CC-BY-SA", re.compile(r"\bCC[- ]BY[- ]SA\b", re.I)),
    ("CC-BY", re.compile(r"\bCC[- ]BY\b", re.I)),
    ("MIT", re.compile(r"\bMIT\b")),
    ("Elastic/SSPL/BUSL", re.compile(r"\b(SSPL|BUSL|Elastic License|Sustainable Use)\b", re.I)),
    ("no-grant", re.compile(r"\b(no licence file|no license file|ungranted|carries no licence|carries no license|no grant)\b", re.I)),
    ("absent", re.compile(r"\b(does not exist|confirmed absent|404s on|phantom)\b", re.I)),
]
STARS = re.compile(r"(\d[\d,.   ]*)\s*(k?)\s*(?:★|\*{1}\b|stars?\b)", re.I)


def norm(owner, repo):
    repo = STRIP_SUFFIX.sub("", repo).rstrip(".,;:)]}'\"")
    owner = owner.rstrip(".,;:)]}'\"")
    return f"{owner}/{repo}".lower(), f"{owner}/{repo}"


def verdict_of(text):
    """Best-effort grant reading from the prose around an address.

    This is a reading of what the base SAID, never a measurement of the repo.
    Column is named last_verdict for that reason: it is the claim on record, and
    a pass that wants the truth re-probes the address.
    """
    hits = [name for name, pat in LICENCE_PATTERNS if pat.search(text)]
    if not hits:
        return "unstated"
    # Keep order of the pattern table (most specific first), cap at two.
    return "|".join(hits[:2])


def scan(path, label):
    """Yield (key, display, pass_no, date, verdict, line_no) per address occurrence."""
    cur_pass, cur_date = None, None
    with open(path, encoding="utf-8") as fh:
        for n, line in enumerate(fh, 1):
            hm = HEADING.match(line)
            # Only a level-2 heading starts a new pass section; `###` and deeper
            # are sub-sections and routinely cite OTHER passes.
            if hm and len(hm.group(1)) == 2 and not NOT_A_SECTION.search(line):
                pm = PASS_IN_HEAD.search(line)
                if pm:
                    cur_pass = int(next(g for g in pm.groups() if g))
                    d = DATE_TOK.search(line)
                    cur_date = d.group(1) if d else cur_date
            for om in ADDR.finditer(line):
                owner, repo = om.group(1), om.group(2)
                if owner.lower() in NOT_OWNERS:
                    continue
                key, disp = norm(owner, repo)
                if "/" not in key or key.endswith("/"):
                    continue
                yield key, disp, cur_pass, cur_date, verdict_of(line), n, label


def build(root):
    rows = {}
    missing = []
    for rel, label in [(p, "curated") for p in CURATED] + [(p, "history") for p in HISTORY]:
        path = os.path.join(root, rel)
        if not os.path.exists(path):
            missing.append(rel)
            continue
        for key, disp, pno, date, verdict, ln, lab in scan(path, label):
            r = rows.setdefault(key, {
                "display": disp, "first_pass": None, "last_pass": None,
                "last_date": None, "verdicts": {}, "files": set(),
                "curated": False, "mentions": 0,
            })
            r["mentions"] += 1
            r["files"].add(rel)
            if lab == "curated":
                r["curated"] = True
            if pno is not None:
                if r["first_pass"] is None or pno < r["first_pass"]:
                    r["first_pass"] = pno
                if r["last_pass"] is None or pno > r["last_pass"]:
                    r["last_pass"] = pno
                    r["last_date"] = date
                    r["verdicts"][pno] = verdict
            elif verdict != "unstated":
                r["verdicts"].setdefault(0, verdict)
    return rows, missing


def last_verdict(r):
    if not r["verdicts"]:
        return "unstated"
    return r["verdicts"][max(r["verdicts"])]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo-root", default=".")
    ap.add_argument("--out", default="evidence/address-ledger.tsv")
    ap.add_argument("--debt", action="store_true",
                    help="print only addresses present in history and on no curated file")
    ap.add_argument("--archives", action="store_true",
                    help="index archive/**/*.md instead, and report addresses that "
                         "exist ONLY there (Gap 530-A: p530 measured 591)")
    args = ap.parse_args()

    rows, missing = build(args.repo_root)
    for rel in missing:
        print(f"WARN missing file: {rel}", file=sys.stderr)

    if args.archives:
        # Gap 530-A. A rewrite re-derives a file from the pass's own reading, so
        # anything verified earlier vanishes unless something carries it forward.
        # Nothing does -- this reports how much.
        live = set(rows)
        arch = {}
        pattern = os.path.join(args.repo_root, "archive", "**", "*.md")
        files = glob.glob(pattern, recursive=True)
        for path in files:
            for key, disp, pno, date, verdict, ln, lab in scan(path, "history"):
                arch.setdefault(key, disp)
        candidates = sorted(k for k in arch if k not in live)

        # The index above reads ONE address channel -- `github.com/owner/repo`
        # URLs.  This base carries a second: a bare backticked `owner/repo`,
        # which `gate-bare-slug-channel` (p367) and `gate-census-union` (p375)
        # already exist to catch.  p530 rebuilt the single-channel defect anyway
        # and measured the cost: 239 of 588 candidates -- 40.6% -- are present
        # in a live file as a bare slug.  So every candidate is re-tested
        # against the raw live text before it is called archive-only.
        live_text = []
        for rel in CURATED + HISTORY:
            fp = os.path.join(args.repo_root, rel)
            if os.path.exists(fp):
                with open(fp, encoding="utf-8", errors="replace") as fh:
                    live_text.append(fh.read().lower())
        blob = "\n".join(live_text)
        only = [k for k in candidates if arch[k].lower() not in blob]
        suppressed = len(candidates) - len(only)

        print(f"archive files: {len(files)}  archive addresses: {len(arch)}")
        print(f"candidates (URL channel only):   {len(candidates)}")
        print(f"suppressed by bare-slug channel: {suppressed}")
        print(f"ARCHIVE-ONLY (both channels):    {len(only)}")
        out_path = os.path.join(args.repo_root, "evidence", "archive-only-addresses.tsv")
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        with open(out_path, "w", encoding="utf-8") as out:
            out.write("address\n")
            for k in only:
                out.write(arch[k] + "\n")
        print(f"wrote {out_path}")
        return

    ordered = sorted(rows.items(), key=lambda kv: (-(kv[1]["mentions"]), kv[0]))
    out_path = os.path.join(args.repo_root, args.out)
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as out:
        out.write("address\tfirst_seen_pass\tlast_verdict\tfiled_on\tlast_measured\tmentions\n")
        for key, r in ordered:
            filed = ",".join(sorted(f for f in r["files"] if f in CURATED)) or "-"
            fp = f"p{r['first_pass']}" if r["first_pass"] else "unpassed"
            out.write("\t".join([
                r["display"], fp, last_verdict(r), filed,
                r["last_date"] or "-", str(r["mentions"]),
            ]) + "\n")

    filed_n = sum(1 for _, r in ordered if r["curated"])
    print(f"addresses: {len(ordered)}  filed: {filed_n}  unfiled: {len(ordered)-filed_n}")
    print(f"wrote {out_path}")

    if args.debt:
        print("\n-- owned and unfiled, by mentions --")
        for key, r in ordered:
            if r["curated"]:
                continue
            print(f"{r['mentions']:4d}  {r['display']:55s} {('p%s'%r['first_pass']) if r['first_pass'] else 'unpassed':9s} {last_verdict(r)}")


if __name__ == "__main__":
    main()
