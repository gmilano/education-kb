#!/usr/bin/env python3
"""p436 — Gap 435-B's NOTATION, and the gate that joins it against the live shelves.

Gap 435-B asked for exactly this and said why a regex alone will not do:

    "There are 19 `Promoted` claims across the two trend shelves in at least four
     different notations ... A regex over that prose would under-report and call
     it green, which is worse than no gate.  Remedy and cost: a notation first --
     one line per promotion in a committed ledger with the slug and the target
     file -- then a gate that joins the ledger against the live shelves."

The committed ledger is `evidence/promotion-ledger.<date>-p436.tsv`.  This module
is the join.  Its predicate is a RATCHET rather than a pass/fail on the backlog,
because the backlog is 146 rows and a gate that fires 146 times is a classifier,
not a detector -- the error `Gap 435-A` recorded against `gate-promotion`.

Three controls, all offline:

  C1 UNADJUDICATED  a positive promotion claim on a live trend shelf whose slug
                    has no ledger row.  This is the control that makes the
                    notation binding: a later pass cannot claim a promotion
                    without recording a verdict for it.
  C2 RATCHET        the count of distinct un-landed claimed slugs may not EXCEED
                    the pinned figure.  It may only fall.
  C3 REGRESSION     a slug this ledger records as RESTORED must still be on a
                    live shelf.  This is the control aimed at the mechanism
                    Gap 435-B identified: a full-file rewrite that silently drops
                    restored rows would otherwise be invisible again.
"""
import os
import sys

# `$(PY) -I` implies `-P` on 3.11+, so the script directory is NOT on sys.path.
# Same shape as p434-promotion-gate and p435-promotion-sweep.
_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)

import claims as C

RESTORED_PREFIX = "RESTORED-"


def read_ledger(path):
    with open(path, encoding="utf-8") as fh:
        lines = [l.rstrip("\n") for l in fh if l.strip()]
    if not lines:
        raise ValueError("ledger is empty: %s" % path)
    head = lines[0].split("\t")
    need = ["slug", "claim_source", "claim_line", "notation", "claimed_target",
            "live_verdict", "archive_partition", "p436_verdict"]
    for col in need:
        if col not in head:
            raise ValueError("ledger %s is missing column %r" % (path, col))
    idx = {c: head.index(c) for c in head}
    rows = []
    for ln in lines[1:]:
        parts = ln.split("\t")
        while len(parts) < len(head):
            parts.append("")
        rows.append({c: parts[idx[c]] for c in head})
    return rows


def live_shelf_slugs(root):
    """The row predicate, defined once in claims.py and reused here."""
    return C.live_shelf_rows(root)


def derive_claims(root):
    """Positive, slug-resolved promotion claims on the live trend shelves."""
    out = []
    for rel in ("agents/trending.md", "repos/trending.md"):
        p = os.path.join(root, rel)
        if not os.path.exists(p):
            continue
        for label, ln, note, slug, tg, text in C.extract(p, rel):
            if not slug or note in ("META", "NEGATED") or note.endswith("-UNRESOLVED"):
                continue
            out.append((rel, ln, note, slug, tg))
    return out


def check(root, ledger_path, ratchet):
    findings = []
    rows = read_ledger(ledger_path)
    live = live_shelf_slugs(root)
    live_any = set()
    for v in live.values():
        live_any |= v

    ledger_slugs = {r["slug"] for r in rows}
    derived = derive_claims(root)

    # C1 -- a claim with no ledger row
    for rel, ln, note, slug, tg in derived:
        if slug not in ledger_slugs:
            findings.append(("C1-UNADJUDICATED", slug,
                             "%s:%s claims promotion; no ledger row" % (rel, ln)))

    # C2 -- the ratchet.  A DECLINED address stays un-landed by construction: the
    # ledger decided it, so no prose mention of it may move the count.
    declined = {r["slug"] for r in rows if r["p436_verdict"].startswith("DECLINED-")}
    unlanded = sorted({slug for _r, _l, _n, slug, _t in derived
                       if slug not in live_any or slug in declined})
    if len(unlanded) > ratchet:
        findings.append(("C2-RATCHET", "%d" % len(unlanded),
                         "un-landed claimed slugs rose above the pinned %d" % ratchet))

    # C3 -- a restored row dropped again
    for r in rows:
        if r["p436_verdict"].startswith(RESTORED_PREFIX) and r["slug"] not in live_any:
            findings.append(("C3-REGRESSION", r["slug"],
                             "recorded %s and is on NO live shelf" % r["p436_verdict"]))

    return findings, len(unlanded), len(rows), len(derived)


def main(argv):
    if len(argv) < 2:
        sys.stderr.write(
            "usage: ledger.py REPO_ROOT LEDGER_TSV [RATCHET]\n"
            "  REPO_ROOT   the education-kb checkout to judge\n"
            "  LEDGER_TSV  the committed promotion ledger\n"
            "  RATCHET     max distinct un-landed claimed slugs (default 146)\n")
        return 2
    root, ledger_path = argv[0], argv[1]
    ratchet = int(argv[2]) if len(argv) > 2 else 146
    if not os.path.isdir(root):
        sys.stderr.write("ledger.py: not a directory: %s\n" % root)
        return 2
    if not os.path.exists(ledger_path):
        sys.stderr.write("ledger.py: no ledger at %s\n" % ledger_path)
        return 2
    try:
        findings, unlanded, nrows, nclaims = check(root, ledger_path, ratchet)
    except ValueError as exc:
        sys.stderr.write("ledger.py: %s\n" % exc)
        return 2
    print("ledger rows=%d  positive claims derived=%d  un-landed distinct=%d  ratchet=%d"
          % (nrows, nclaims, unlanded, ratchet))
    for kind, who, why in findings:
        print("%s\t%s\t%s" % (kind, who, why))
    if findings:
        print("%d finding(s)" % len(findings))
        return 1
    print("PASS — every claim adjudicated, backlog at or below the ratchet, "
          "no restored row dropped")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
