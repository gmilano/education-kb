#!/usr/bin/env python3
"""p869 -- 868-G2: mark every counted row whose p868 census verdict is STALE or ARCHIVED,
IN PLACE, in the table a client actually reads.

868-G2 is explicit that the marking must READ the committed census and not re-measure:
"A marking pass that re-measures instead of reading the committed census has misunderstood
the gap."  So the only input is evidence/liveness-census.2026-11-17-p868.tsv.

Word boundaries are load-bearing (p853): `XPRIZE/GLEXP-Team-onebillion` must not match
`XPRIZE/GLEXP-Team-onebillion-PhraseAnal`, which is a DIFFERENT shelved row with a
different star count.  The address is therefore matched as github.com/<addr> followed by a
character that cannot continue a repository name.

The marker is appended INSIDE the row's final cell, so the row still renders as a row
(p277's gate-tables contract).  Idempotent: a row already carrying the marker is skipped.
"""
import argparse, csv, os, re, sys

MARK = "STALE-ROW"

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", required=True)
    ap.add_argument("--census", required=True)
    ap.add_argument("--apply", action="store_true")
    a = ap.parse_args()

    rows = []
    with open(a.census, newline="", encoding="utf-8") as fh:
        for r in csv.DictReader(fh, delimiter="\t"):
            if r["verdict"] in ("STALE", "ARCHIVED"):
                rows.append(r)

    # address -> (verdict, pushed, age_days); shelves come from the census row itself
    by_shelf = {}
    for r in rows:
        for sh in [s.strip() for s in r["shelves"].split(",") if s.strip()]:
            by_shelf.setdefault(sh, []).append(r)

    total_addr = len(rows)
    marked_rows = already = addr_hit = addr_miss = 0
    missing = []
    report = []

    for shelf, recs in sorted(by_shelf.items()):
        path = os.path.join(a.root, shelf)
        if not os.path.exists(path):
            print(f"!! shelf absent: {shelf}", file=sys.stderr); continue
        with open(path, encoding="utf-8") as fh:
            lines = fh.readlines()
        changed = False
        for rec in recs:
            addr = rec["address"]
            # github.com/<addr> not followed by a name-continuing character
            pat = re.compile(r"github\.com/" + re.escape(addr) + r"(?![A-Za-z0-9._\-])")
            hits = 0
            for i, ln in enumerate(lines):
                if not ln.lstrip().startswith("|"):
                    continue
                if not pat.search(ln):
                    continue
                if MARK in ln:
                    already += 1; hits += 1; continue
                stripped = ln.rstrip("\n")
                # append inside the final cell: insert before the trailing pipe
                m = re.search(r"\|\s*$", stripped)
                marker = (f" 🔴 **`{MARK}` — last pushed `{rec['pushed']}`"
                          f" (`{int(rec['age_days']):,}` days), census verdict"
                          f" `{rec['verdict']}` (`p868`), marked `p869`.**")
                if m:
                    new = stripped[:m.start()] + marker + " " + stripped[m.start():]
                else:
                    new = stripped + marker
                lines[i] = new + "\n"
                marked_rows += 1; hits += 1; changed = True
            if hits:
                addr_hit += 1
            else:
                addr_miss += 1; missing.append((shelf, addr))
        if changed and a.apply:
            with open(path, "w", encoding="utf-8") as fh:
                fh.writelines(lines)
        report.append((shelf, len(recs)))

    print(f"census STALE+ARCHIVED addresses : {total_addr}")
    for shelf, n in report:
        print(f"  {shelf:28s} census addresses: {n}")
    print(f"addresses located in their shelf : {addr_hit}")
    print(f"addresses NOT located           : {addr_miss}")
    print(f"table rows marked               : {marked_rows}")
    print(f"rows already carrying the marker: {already}")
    print(f"mode                            : {'APPLY' if a.apply else 'DRY-RUN'}")
    if missing:
        print("-- not located (shelf, address) --")
        for s, ad in missing[:40]:
            print(f"   {s}\t{ad}")
        if len(missing) > 40:
            print(f"   ... and {len(missing)-40} more")

main()
