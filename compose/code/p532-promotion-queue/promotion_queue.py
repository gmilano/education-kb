#!/usr/bin/env python3
"""Gap 531-B: make the RANKING the input to a promotion sweep.

Why this exists, in the gap's own words.  p530 filed twelve standards repos as
"the integration layer" and left `Cvmcosta/ltijs` (28 passes unfiled) and
`dmitry-viskov/pylti1.3` (27) -- the #1 and #2 most-described unfiled permissive
addresses in the live corpus -- unfiled, in the very layer it was filing.  The
cause is input order: a sweep that starts from a SUBJECT sees what its query
surfaces; a sweep that starts from the RANKING cannot miss the top of it.

Two deliberate differences from `ingest/address-ledger.py`:

  * It ranks on DISTINCT PASSES, not `mentions`.  `mentions` is an occurrence
    count, so one pass that names an address eight times outranks eight passes
    that each name it once.  "Most-described" is the second thing.
  * `filed_on` is recomputed against the LIVE curated files on every run.  The
    committed ledger column is the previous pass's opening balance, which is
    why p531 had to recompute it by hand.

Usage:
    cd compose/code/p532-promotion-queue
    python3 promotion_queue.py --repo-root ../../.. [--out ../../../evidence/...tsv] [--top 25]
"""

import argparse
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def _load_pass_reader(repo_root):
    """Import the single-source heading reader from ingest/.

    `python3 -I` strips the script's own directory from sys.path, which is the
    whole reason this repo's Makefile `cd`s into each instrument (see the note
    at the top of the Makefile).  The import path is therefore built explicitly
    rather than assumed.
    """
    for cand in (os.path.join(repo_root, "ingest"),
                 os.path.abspath(os.path.join(HERE, "..", "..", "..", "ingest"))):
        if os.path.exists(os.path.join(cand, "pass_section.py")):
            sys.path.insert(0, cand)
            from pass_section import pass_of_heading  # noqa: E402
            return pass_of_heading
    raise SystemExit("🔴 ingest/pass_section.py not found — cannot read pass headings")


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
NOT_A_SECTION = re.compile(
    r"(🔜|Registered for|Pre-registered|Gaps OPEN after|Gaps CLOSED|"
    r"gaps opened|(Actions|Gaps)\s+(opened|closed)\s+(by|after)|"
    r"(Live\s+)?gaps\s+declared\s+(by|after)|"
    r"Verdicts on|rows pass|The rows? \S+ changed|one row pass)", re.I)
NOT_OWNERS = {
    "orgs", "topics", "search", "features", "about", "pricing", "marketplace",
    "settings", "notifications", "explore", "sponsors", "collections", "apps",
    "login", "join", "new", "codespaces", "users", "site", "contact", "security",
}
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

# ECL-2.0 is Apache-2.0 with an academic patent-grant tweak and this base
# already treats it as permissive (verticals/solutions.md, Sakai).  MPL-2.0 is
# weak copyleft and is deliberately absent.
PERMISSIVE = {"MIT", "Apache-2.0", "BSD", "ECL-2.0", "CC0-1.0"}


def norm(owner, repo):
    repo = STRIP_SUFFIX.sub("", repo).rstrip(".,;:)]}'\"")
    owner = owner.rstrip(".,;:)]}'\"")
    return f"{owner}/{repo}".lower(), f"{owner}/{repo}"


def verdict_of(text):
    hits = [name for name, pat in LICENCE_PATTERNS if pat.search(text)]
    return "|".join(hits[:2]) if hits else "unstated"


def is_permissive(verdict):
    """Permissive only if EVERY token is.

    A verdict of `AGPL-3.0|MIT` means the prose named a copyleft grant in the
    same breath.  Promoting that as permissive is how a base ships a licence
    error, so the conservative reading is the one that ships.
    """
    if verdict in ("unstated", "no-grant", "absent"):
        return False
    return all(tok in PERMISSIVE for tok in verdict.split("|"))


def build(root, pass_of_heading):
    rows, missing = {}, []
    for rel, label in [(p, "curated") for p in CURATED] + [(p, "history") for p in HISTORY]:
        path = os.path.join(root, rel)
        if not os.path.exists(path):
            missing.append(rel)
            continue
        cur_pass, cur_date = None, None
        with open(path, encoding="utf-8", errors="replace") as fh:
            for line in fh:
                hm = HEADING.match(line)
                if hm and len(hm.group(1)) == 2 and not NOT_A_SECTION.search(line):
                    pno, _d = pass_of_heading(line)
                    if pno is not None:
                        cur_pass = pno
                        dm = re.search(r"(\d{4}-\d{2}-\d{2})", line)
                        cur_date = dm.group(1) if dm else cur_date
                for om in ADDR.finditer(line):
                    owner, repo = om.group(1), om.group(2)
                    if owner.lower() in NOT_OWNERS:
                        continue
                    key, disp = norm(owner, repo)
                    if "/" not in key or key.endswith("/"):
                        continue
                    r = rows.setdefault(key, {
                        "display": disp, "first_pass": None, "verdicts": {},
                        "curated": False, "mentions": 0, "passes": set(),
                        "last_date": None, "last_pass": None,
                    })
                    r["mentions"] += 1
                    if label == "curated":
                        r["curated"] = True
                    v = verdict_of(line)
                    if cur_pass is not None:
                        r["passes"].add(cur_pass)
                        if r["first_pass"] is None or cur_pass < r["first_pass"]:
                            r["first_pass"] = cur_pass
                        if r["last_pass"] is None or cur_pass > r["last_pass"]:
                            r["last_pass"] = cur_pass
                            r["last_date"] = cur_date
                            r["verdicts"][cur_pass] = v
                    elif v != "unstated":
                        r["verdicts"].setdefault(0, v)
    return rows, missing


def last_verdict(r):
    return r["verdicts"][max(r["verdicts"])] if r["verdicts"] else "unstated"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo-root", default="../../..")
    ap.add_argument("--out", default=None)
    ap.add_argument("--top", type=int, default=25)
    args = ap.parse_args()

    root = args.repo_root
    pass_of_heading = _load_pass_reader(root)
    rows, missing = build(root, pass_of_heading)
    for rel in missing:
        print(f"WARN missing file: {rel}", file=sys.stderr)

    queue = []
    for r in rows.values():
        if r["curated"]:
            continue
        v = last_verdict(r)
        if not is_permissive(v):
            continue
        queue.append((len(r["passes"]), r["mentions"], r["display"], v,
                      f"p{r['first_pass']}" if r["first_pass"] else "unpassed",
                      r["last_date"] or "-"))
    queue.sort(key=lambda q: (-q[0], -q[1], q[2].lower()))

    filed = sum(1 for r in rows.values() if r["curated"])
    print(f"addresses: {len(rows)}   filed: {filed}   unfiled: {len(rows)-filed}")
    print(f"unfiled AND permissive (the queue): {len(queue)}")
    print(f"\n{'passes':>6} {'ments':>6}  {'address':52s} {'verdict':12s} first")
    for dp, mn, disp, v, fp, _ld in queue[:args.top]:
        print(f"{dp:6d} {mn:6d}  {disp:52s} {v:12s} {fp}")

    if args.out:
        out = args.out if os.path.isabs(args.out) else os.path.join(root, args.out)
        os.makedirs(os.path.dirname(out), exist_ok=True)
        with open(out, "w", encoding="utf-8") as fh:
            fh.write("rank\tdistinct_passes\tmentions\taddress\tlast_verdict\t"
                     "first_seen_pass\tlast_measured\n")
            for i, (dp, mn, disp, v, fp, ld) in enumerate(queue, 1):
                fh.write(f"{i}\t{dp}\t{mn}\t{disp}\t{v}\t{fp}\t{ld}\n")
        print(f"\nwrote {out}")


if __name__ == "__main__":
    main()
