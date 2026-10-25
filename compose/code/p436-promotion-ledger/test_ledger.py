#!/usr/bin/env python3
"""p436 — offline controls for the promotion ledger and its gate.

Two of these controls are regressions for defects THIS pass's own instruments
had, both caught by their own negative controls rather than by luck:

  C6   `\\bPromoted\\b` matches "deliberately NOT promoted".  The first build
       accused 218 addresses; 47 of them were negative claims.
  C9   a slug MENTIONED in prose on a shelf is not a slug occupying a ROW.  The
       mention-based read counted p436's own DECLINED note as a landing.
  C17  grading register citations against the CURATED shelves reported 462 dead
       citations -- an artefact of a denominator that holds 3 finding IDs.
"""
import os
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import claims as C
import ledger as L

PASS, FAIL = [], []


def ok(name, cond, detail=""):
    (PASS if cond else FAIL).append(name)
    print("  %s %s%s" % ("PASS" if cond else "FAIL", name,
                         "" if cond else "  -- " + detail))


def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)


def fixture(tmp, agents_trending="", repos_trending="", top="", foundations="",
            ledger_rows=()):
    for rel, txt in (("agents/trending.md", agents_trending),
                     ("repos/trending.md", repos_trending),
                     ("agents/top.md", top),
                     ("repos/foundations.md", foundations),
                     ("verticals/solutions.md", ""),
                     ("intel/market.md", ""),
                     ("intel/trends.md", ""),
                     ("compose/patterns.md", "")):
        write(os.path.join(tmp, rel), txt)
    led = os.path.join(tmp, "ledger.tsv")
    head = ["slug", "claim_source", "claim_line", "notation", "claimed_target",
            "live_verdict", "archive_partition", "p436_verdict",
            "reverified_evidence"]
    with open(led, "w", encoding="utf-8") as fh:
        fh.write("\t".join(head) + "\n")
        for r in ledger_rows:
            fh.write("\t".join(list(r) + [""] * (len(head) - len(r))) + "\n")
    return led


def run(script, *args):
    p = subprocess.run([sys.executable, "-I", os.path.join(HERE, script)] + list(args),
                       capture_output=True, text=True)
    return p.returncode, p.stdout, p.stderr


def notations(text):
    tmp = tempfile.mkdtemp()
    try:
        p = os.path.join(tmp, "t.md")
        write(p, text)
        return C.extract(p, "t.md")
    finally:
        shutil.rmtree(tmp)


def main():
    print("p436-promotion-ledger — offline controls")

    # ---- the negation guard -------------------------------------------------
    neg = [
        ("C1 'deliberately NOT promoted'",
         "### Five new rows, licences READ, deliberately NOT promoted\n\n"
         "| [`a/b`](https://github.com/a/b) | MIT |\n"),
        ("C2 'never promoted'",
         "| `a/b` | MIT | seen since p120, never promoted |\n"),
        ("C3 'rather than promoted'",
         "The claim is withdrawn rather than promoted. `a/b`\n"),
        ("C4 'None was promoted'",
         "`a/b` (7 stars). **None was promoted** and none is in a curated table.\n"),
        ("C5 'cannot be promoted'",
         "### Two leads that cannot be promoted to rows this pass, and why\n\n"
         "- `a/b`\n"),
    ]
    for name, text in neg:
        rows = notations(text)
        ok(name, all(r[2] == "NEGATED" or not r[3] for r in rows),
           "expected NEGATED, got %r" % [(r[2], r[3]) for r in rows])

    # C6 -- the false negation the wide guard caused.  MUST be positive.
    text = ("## Pass 334 — the channel is NOT saturated; eight legs, "
            "nine never-before-seen slugs, two promoted\n\n"
            "| [`a/b`](https://github.com/a/b) | MIT |\n")
    rows = [r for r in notations(text) if r[3]]
    ok("C6 positive claim across a comma is NOT negated",
       bool(rows) and all(r[2] != "NEGATED" for r in rows),
       "got %r" % [(r[2], r[3]) for r in rows])

    # ---- the block rule ----------------------------------------------------
    text = ("### Promoted — two new addresses\n\n"
            "| [`a/b`](https://github.com/a/b) | MIT |\n"
            "| [`c/d`](https://github.com/c/d) | MIT |\n")
    got = {r[3] for r in notations(text) if r[3]}
    ok("C7 header claim captures the block that follows", got == {"a/b", "c/d"},
       "got %r" % got)

    text = ("### Promoted — one address\n\n"
            "| [`a/b`](https://github.com/a/b) | MIT |\n"
            "Declined — read first-hand, no grant to read\n"
            "| [`c/d`](https://github.com/c/d) | none |\n")
    got = {r[3] for r in notations(text) if r[3]}
    ok("C8 a decline line truncates the block", got == {"a/b"}, "got %r" % got)

    # ---- the row predicate -------------------------------------------------
    tmp = tempfile.mkdtemp()
    try:
        led = fixture(
            tmp,
            agents_trending="### Promoted\n\n| [`a/b`](https://github.com/a/b) | MIT |\n",
            top="Prose only: see [`a/b`](https://github.com/a/b) for context.\n",
            ledger_rows=[("a/b", "agents/trending.md", "1", "HEADER", "-",
                          "NOT-LANDED", "-", "BACKLOG")])
        live = C.live_shelf_rows(tmp)
        allrows = set()
        for v in live.values():
            allrows |= v
        ok("C9 a prose mention is not a shelf row", "a/b" not in allrows,
           "mention leaked into the row set")

        # C10 -- DECLINED stays un-landed even when a row names it
        led2 = fixture(
            tmp,
            agents_trending="### Promoted\n\n| [`a/b`](https://github.com/a/b) | MIT |\n",
            top="| [`a/b`](https://github.com/a/b) | MIT | declined, see note |\n",
            ledger_rows=[("a/b", "agents/trending.md", "1", "HEADER", "-",
                          "NOT-LANDED", "-", "DECLINED-p436")])
        f, unl, _n, _c = L.check(tmp, led2, 99)
        ok("C10 a DECLINED address is never counted as landed", unl == 1,
           "un-landed=%d" % unl)

        # C11/C12 -- the ratchet
        f, unl, _n, _c = L.check(tmp, led2, 0)
        ok("C11 ratchet FIRES when the backlog exceeds the pin",
           any(k == "C2-RATCHET" for k, _w, _y in f), "findings=%r" % f)
        f, unl, _n, _c = L.check(tmp, led2, 1)
        ok("C12 ratchet PASSES at equality",
           not any(k == "C2-RATCHET" for k, _w, _y in f), "findings=%r" % f)

        # C13 -- an unadjudicated claim
        led3 = fixture(
            tmp,
            agents_trending="### Promoted\n\n| [`x/y`](https://github.com/x/y) | MIT |\n",
            ledger_rows=[])
        f, _u, _n, _c = L.check(tmp, led3, 99)
        ok("C13 a claim with no ledger row is C1-UNADJUDICATED",
           any(k == "C1-UNADJUDICATED" for k, _w, _y in f), "findings=%r" % f)

        # C14 -- a restored row dropped again
        led4 = fixture(
            tmp,
            agents_trending="### Promoted\n\n| [`a/b`](https://github.com/a/b) | MIT |\n",
            top="nothing here\n",
            ledger_rows=[("a/b", "agents/trending.md", "1", "HEADER", "-",
                          "NOT-LANDED", "-", "RESTORED-p436")])
        f, _u, _n, _c = L.check(tmp, led4, 99)
        ok("C14 a RESTORED row absent from every shelf is C3-REGRESSION",
           any(k == "C3-REGRESSION" for k, _w, _y in f), "findings=%r" % f)

        # C16 -- a malformed ledger is refused, not guessed
        bad = os.path.join(tmp, "bad.tsv")
        write(bad, "slug\tclaim_source\n a/b\tx\n")
        rc, _o, err = run("ledger.py", tmp, bad, "99")
        ok("C16 a ledger missing a required column exits 2",
           rc == 2 and "missing column" in err, "rc=%d err=%r" % (rc, err[:120]))
    finally:
        shutil.rmtree(tmp)

    # ---- C15: every instrument refuses empty input (P541 class) ------------
    for script in ("ledger.py", "claims.py", "archive_drop.py",
                   "audit_blocks.py", "finding_citations.py"):
        rc, out, err = run(script)
        ok("C15 %s refuses empty input with exit 2" % script,
           rc == 2 and not out.strip(), "rc=%d out=%r" % (rc, out[:80]))

    # ---- C17: the wrong-denominator refusal --------------------------------
    tmp = tempfile.mkdtemp()
    try:
        fixture(tmp, agents_trending="P1 P2\n", repos_trending="P3\n",
                top="P4\n")
        write(os.path.join(tmp, "intel/open-gaps.md"), "cites P1 and P999\n")
        rc, out, err = run("finding_citations.py", tmp)
        ok("C17 a definition channel too small to grade is REFUSED",
           rc == 2 and "denominator looks wrong" in err,
           "rc=%d err=%r" % (rc, err[:140]))
    finally:
        shutil.rmtree(tmp)

    # ---- C18: slug extraction rejects file paths in backticks --------------
    got = C.slugs_in("see `intel/open-gaps.md` and `evidence/x.tsv` and `a/b`")
    ok("C18 a backticked file path is not a slug", got == ["a/b"], "got %r" % got)

    print("\n%d PASS, %d FAIL" % (len(PASS), len(FAIL)))
    if FAIL:
        for f in FAIL:
            print("  FAILED: %s" % f)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
