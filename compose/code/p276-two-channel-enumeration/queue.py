#!/usr/bin/env python3
"""p276 - independent reimplementation of p275's enumeration-gate queue computation.

Written fresh for pass 276 because the sandbox forbids executing the cloned repo's own
scripts.  Predicates mirror compose/code/pass275-grant-enumeration/enumeration_gate.py
as read at HEAD (bc63f47); any divergence is a defect in THIS file.
"""
import glob, os, re, sys, collections

SHELVES = ["agents/top.md", "agents/trending.md", "repos/foundations.md",
           "repos/trending.md", "verticals/solutions.md", "intel/market.md",
           "intel/trends.md", "compose/patterns.md"]

NEGATIVE = re.compile(
    r"no licen[cs]e payload|no payload|no grant|serves no grant|PRE-LICEN[CS]E|"
    r"licen[cs]e[- ]unverified|licen[cs]e UNVERIFIED|all rights reserved|"
    r"treat as all-rights-reserved", re.I)
RETRACTION = re.compile(
    r"retract|RESOLVED|REFUTED|refuted|NOW READ|does not exist|UPHELD|"
    r"was FALSE|FALSE in both|no longer|correction|CORRECTED|SUPERSEDED|was wrong", re.I)
SPDX = re.compile(r"\b(MIT|Apache-2\.0|BSD-[23]-Clause|BSD|GPL-[23]\.0|GPL-2|AGPL-3\.0|"
                  r"LGPL-3\.0|CC0-1\.0|CC-BY(-NC)?(-SA)?-4\.0|MPL-2\.0|EUPL)\b")
GRANT_EVIDENCE = re.compile(
    r"[Ll]icen[cs]e\.(txt|md|rtf)|/[Ll]icen[cs]e\b|\bLICEN[CS]E\b"
    r"|\d[\d  ]*B\b|(?i:manifests? declare)|(?i:read at payload)")
SLUG = re.compile(r"github\.com/([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)")

def states_a_grant(line):
    return bool(SPDX.search(line) and GRANT_EVIDENCE.search(line))

def load_ledgers(root):
    ledger, dead = {}, set()
    for path in sorted(glob.glob(os.path.join(root, "evidence", "tree-enumeration.*.tsv"))):
        with open(path, encoding="utf-8") as fh:
            for line in fh:
                if line.startswith("#") or not line.strip():
                    continue
                cols = line.rstrip("\n").split("\t")
                if len(cols) < 5 or cols[0] == "slug":
                    continue
                slug, cell = cols[0].strip(), cols[4]
                if re.search(r"\bFAIL\b|DOES_NOT_RESOLVE", cols[1] + cell):
                    dead.add(slug); continue
                ledger[slug] = [] if re.search(r"\bNONE\b|NONE_IN_TREE", cell) \
                    else [c.strip() for c in cell.split(",")]
    return ledger, dead

def attribute(line, names=()):
    marks = [(m.start(), m.group(1).rstrip(".")) for m in SLUG.finditer(line)]
    for slug in names:
        base = slug.split("/")[-1]
        for m in re.finditer(r"\b" + re.escape(base) + r"(?!'s|’s)\b", line, re.I):
            marks.append((m.start(), slug))
    if not marks:
        return []
    marks.sort()
    owners = set()
    for phrase in NEGATIVE.finditer(line):
        before = [s for s in marks if s[0] < phrase.start()]
        owners.add(before[-1][1] if before else marks[0][1])
    return sorted(owners)

def main():
    root = sys.argv[1]
    ledger, dead = load_ledgers(root)
    queue = collections.defaultdict(list)
    refuted, verified = [], []
    for shelf in SHELVES:
        full = os.path.join(root, shelf)
        if not os.path.exists(full):
            continue
        with open(full, encoding="utf-8") as fh:
            for n, line in enumerate(fh, 1):
                if not NEGATIVE.search(line):
                    continue
                if RETRACTION.search(line) or states_a_grant(line):
                    continue
                for slug in attribute(line, ledger.keys()):
                    if slug not in ledger:
                        queue[slug].append(f"{shelf}:{n}")
                    elif [p for p in ledger[slug] if re.search(r"(^|/)(licen[cs]e|copying|notice|unlicense|eupl|copyright)", p, re.I)
                          and not re.search(r"(^|/)(vendor|node_modules|custompackages|libraries|third_party|thirdparty|precompiled-icons|plugins|samples)(/|$)", p, re.I)
                          and not re.search(r"\.(php|java|vue|py|js|ts|jsx|tsx|go|rb|cs|png|svg|jpg|gif)$", p, re.I)]:
                        refuted.append((shelf, n, slug))
                    else:
                        verified.append((shelf, n, slug))
    tot = sum(len(v) for v in queue.values())
    print(f"# REFUTED={len(refuted)} VERIFIED-ABSENT={len(verified)} QUEUE-UNENUMERATED={tot} DISTINCT-SLUGS={len(queue)}")
    print(f"# ledger slugs={len(ledger)} dead={len(dead)}")
    for slug, locs in sorted(queue.items(), key=lambda kv: (-len(kv[1]), kv[0])):
        print(f"{len(locs)}\t{slug}\t{';'.join(locs[:6])}")
if __name__ == "__main__":
    main()

VENDORED = re.compile(r"(^|/)(vendor|node_modules|custompackages|libraries|third_party|thirdparty|"
                      r"precompiled-icons|plugins|samples)(/|$)", re.I)
SOURCEY = re.compile(r"\.(php|java|vue|py|js|ts|jsx|tsx|go|rb|cs|png|svg|jpg|gif)$", re.I)
LICENCEY = re.compile(r"(^|/)(licen[cs]e|copying|notice|unlicense|eupl|copyright)", re.I)

def candidate_grants(paths):
    out = []
    for p in paths:
        p = p.strip()
        if not p or p == "NONE_IN_TREE": continue
        if not LICENCEY.search(p): continue
        if VENDORED.search(p) or SOURCEY.search(p): continue
        out.append(p)
    return out
