#!/usr/bin/env python3
"""p867 -- discharge of `866-G1`: ONE command that orders a triaged bucket for filing.

WHY THIS EXISTS.  `865-G4` removed hand-grading from the three-way SPLIT of a sweep
(NEW / UNGRADED / SHELVED) by building `ingest/p866-triage.py`.  `p866` then chose which
`15` of its `27` UNGRADED addresses to file BY READING THEIR DESCRIPTIONS -- the same
hand-grading, one step downstream, which is what `866-G1` registered.

WHAT IT IS.  Two GATES and one RANK, over metadata this base already collects:

  GATE grant     -- the heading of `agents/top.md` promises MIT / Apache-2.0 / BSD / ISC /
                    0BSD.  An address whose field licence is outside that set cannot be
                    filed on it, so it is refused before any ordering happens.  (The FIELD
                    is a screen, never a grade: `T81` is this base's standing finding that
                    `search/repositories` and the payload disagree, and a row still needs
                    its byte-read before it is filed.)
  GATE liveness  -- archived, or no push in 365 days, is refused.  `promotion-rank.py`
                    (p533) recorded why: 4 of 35 queue-head addresses were dead and a
                    recall count cannot notice that an address has died.
  RANK           -- materiality band by stars (p533's bands, unchanged), then forks, then
                    recency.  Stars are a weak proxy for how much an address matters and
                    three orders of magnitude better than a mention count.

WHAT IT IS NOT.  It is not a quality judgement and does not pretend to be one.  It orders
a queue; a pass still reads the top of that queue and still byte-reads the grant.  The
measurable claim `866-G1` asked for is the HIT RATE: of the rows a pass filed by hand,
how many sit in the ranker's top N.  `--against` computes exactly that and prints it
whether it flatters the ranker or not.

Usage:
    python3 -I ingest/p867-promotion-rank.py --meta sweep.tsv --bucket ungraded.txt
    python3 -I ingest/p867-promotion-rank.py --meta m.tsv --bucket b.txt \
        --against filed.txt --top 15 --tsv evidence/promotion-rank.<date>-p867.tsv
"""
import argparse
import datetime
import sys

PERMISSIVE = {"mit", "apache-2.0", "bsd-3-clause", "bsd-2-clause", "isc", "0bsd",
              "unlicense", "ecl-2.0", "bsd-4-clause"}
COPYLEFT = {"gpl-2.0", "gpl-3.0", "agpl-3.0", "lgpl-2.1", "lgpl-3.0", "mpl-2.0", "epl-2.0",
            "eupl-1.2", "osl-3.0", "cecill-2.1"}
UNSTATED = {"noassertion", "none", "", "-"}
STALE_DAYS = 365

# 🟢 p867's first run of this instrument against `p866`'s own choices measured a 52% hit
# rate and the TEN misses had exactly two causes, neither of them ranking noise:
#
#   (i)  the grant gate was keyed to ONE shelf's predicate.  `agents/top.md` promises
#        MIT / Apache-2.0 / BSD / ISC / 0BSD; `verticals/solutions.md` carries GPL-3.0 BY
#        OBLIGATION (a Moodle plugin links against Moodle -- p866's own finding), and
#        `repos/foundations.md` states no licence predicate at all.  Four of the ten were
#        GPL-3.0 Moodle-estate rows filed on the shelf that admits them.  A promotion
#        ranker that refuses them is not screening, it is deleting a destination.
#   (ii) five were `NOASSERTION`, which is `T81`'s subject: the FIELD and the PAYLOAD
#        disagree often enough that this base byte-reads every grant it files.  An unstated
#        field is the reason to byte-read, never the reason to refuse.
#
# So the gate is now per-DESTINATION and unstated grants get their own tier.
SHELF_PREDICATE = {
    "build-safe": PERMISSIVE,                   # agents/top.md's heading, verbatim
    "platform": PERMISSIVE | COPYLEFT,          # verticals/solutions.md -- copyleft admitted
    "foundation": PERMISSIVE | COPYLEFT,        # repos/foundations.md -- no stated predicate
}


def band(stars):
    """p533's materiality bands, re-used rather than re-invented."""
    n = stars if isinstance(stars, int) else -1
    if n < 0:
        return "?"
    return "A" if n >= 10000 else "B" if n >= 1000 else "C" if n >= 100 \
        else "D" if n >= 10 else "E"


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--meta", required=True,
                    help="TSV: address, owner_type, stars, forks, licence, pushed, archived, ...")
    ap.add_argument("--bucket", required=True, help="file of addresses to rank, one per line")
    ap.add_argument("--against", help="file of addresses a pass actually filed, for the hit rate")
    ap.add_argument("--top", type=int, default=15)
    ap.add_argument("--shelf", default="build-safe", choices=sorted(SHELF_PREDICATE),
                    help="which shelf's licence predicate gates the queue")
    ap.add_argument("--today", default=datetime.date.today().isoformat())
    ap.add_argument("--tsv")
    args = ap.parse_args(argv)

    today = datetime.date.fromisoformat(args.today)
    meta = {}
    with open(args.meta, encoding="utf-8") as fh:
        head = fh.readline().rstrip("\n").split("\t")
        if head and head[0].lower() != "address":
            fh.seek(0)
        for line in fh:
            f = line.rstrip("\n").split("\t")
            if len(f) < 7:
                continue
            meta[f[0].lower()] = dict(address=f[0], owner_type=f[1], stars=f[2], forks=f[3],
                                      licence=f[4], pushed=f[5], archived=f[6],
                                      homepage=f[7] if len(f) > 7 else "-",
                                      vein=f[8] if len(f) > 8 else "-",
                                      desc=f[9] if len(f) > 9 else "-")

    bucket = [l.strip() for l in open(args.bucket, encoding="utf-8") if l.strip()]
    rows, refused = [], []
    for addr in bucket:
        m = meta.get(addr.lower())
        if not m:
            refused.append((addr, "NO-METADATA", "not in the sweep record"))
            continue
        lic = m["licence"].strip().lower()
        admitted = SHELF_PREDICATE[args.shelf]
        if lic in UNSTATED:
            tier = "BYTE-READ-REQUIRED"      # T81: an unstated field is not an absent grant
        elif lic in admitted:
            tier = "FIELD-PERMISSIVE" if lic in PERMISSIVE else "FIELD-COPYLEFT"
        else:
            refused.append((addr, "REFUSED-GRANT", f"{m['licence']} (outside the "
                                                   f"{args.shelf} predicate)"))
            continue
        if m["archived"].strip().lower() == "true":
            refused.append((addr, "REFUSED-DEAD", "archived"))
            continue
        try:
            age = (today - datetime.date.fromisoformat(m["pushed"][:10])).days
        except ValueError:
            age = 10 ** 6
        if age > STALE_DAYS:
            refused.append((addr, "REFUSED-DEAD", f"last push {m['pushed']} ({age} d)"))
            continue
        stars = int(m["stars"]) if m["stars"].isdigit() else -1
        forks = int(m["forks"]) if m["forks"].isdigit() else -1
        rows.append(dict(m, stars_n=stars, forks_n=forks, band=band(stars), age=age,
                         tier=tier))

    rows.sort(key=lambda r: (r["band"], -r["stars_n"], -r["forks_n"], r["age"]))

    print(f"bucket in        : {len(bucket)}      shelf predicate: {args.shelf}")
    print(f"RANKED (gated in): {len(rows)}"
          f"   [FIELD-PERMISSIVE={sum(1 for r in rows if r['tier'] == 'FIELD-PERMISSIVE')}"
          f" FIELD-COPYLEFT={sum(1 for r in rows if r['tier'] == 'FIELD-COPYLEFT')}"
          f" BYTE-READ-REQUIRED={sum(1 for r in rows if r['tier'] == 'BYTE-READ-REQUIRED')}]")
    for why in ("REFUSED-GRANT", "REFUSED-DEAD", "NO-METADATA"):
        c = sum(1 for _, w, _ in refused if w == why)
        print(f"{why:<17}: {c}")
    print()
    print(f"{'#':>3}  {'band':<4} {'★':>7} {'forks':>6}  {'licence':<14} {'pushed':<11} "
          f"{'tier':<19} address")
    for k, r in enumerate(rows, 1):
        print(f"{k:>3}  {r['band']:<4} {r['stars_n']:>7} {r['forks_n']:>6}  "
              f"{r['licence']:<14} {r['pushed'][:10]:<11} {r['tier']:<19} {r['address']}")

    if args.against:
        filed = {l.strip().lower() for l in open(args.against, encoding="utf-8") if l.strip()}
        ranked_order = [r["address"].lower() for r in rows]
        topn = set(ranked_order[:args.top])
        hits = sorted(filed & topn)
        in_ranked = filed & set(ranked_order)
        gated_out = {a for a, w, _ in refused if a.lower() in filed}
        print()
        print(f"--- 866-G1 hit rate, top {args.top} ---")
        print(f"filed by hand            : {len(filed)}")
        print(f"of those, survive the gates: {len(in_ranked)}")
        print(f"of those, in the top {args.top:<3}  : {len(hits)}"
              f"   = {100.0 * len(hits) / max(len(filed), 1):.0f}% of what was filed")
        print(f"filed but GATED OUT      : {len(gated_out)}"
              + (f"  -> {' '.join(sorted(gated_out))}" if gated_out else ""))
        missed = sorted(a for a in ranked_order[:args.top] if a not in filed)
        print(f"ranker's top {args.top} that the pass did NOT file: {len(missed)}"
              + (f"  -> {' '.join(missed)}" if missed else ""))

    if args.tsv:
        with open(args.tsv, "w", encoding="utf-8") as fh:
            fh.write("rank\taddress\tband\tstars\tforks\tlicence\tpushed\towner_type\tvein\tverdict\n")
            for k, r in enumerate(rows, 1):
                fh.write(f"{k}\t{r['address']}\t{r['band']}\t{r['stars_n']}\t{r['forks_n']}\t"
                         f"{r['licence']}\t{r['pushed'][:10]}\t{r['owner_type']}\t{r['vein']}\t"
                         f"RANKED/{r['tier']}\n")
            for a, w, why in refused:
                fh.write(f"-\t{a}\t-\t-\t-\t-\t-\t-\t-\t{w}: {why}\n")
        print(f"\nrecord -> {args.tsv}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
