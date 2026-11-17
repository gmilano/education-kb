#!/usr/bin/env python3
"""p868 — discharge of `867-G2`: the liveness gate, applied to the rows ALREADY SHELVED.

WHY THIS EXISTS.  `p867`'s promotion ranker refused three addresses `p866` had filed as
current rows — `iwangjian/Coding-Tutor` (`533` days since its last push),
`luffycodes/Tutorbot-Spock` (`~744`), `xoubinha/tutor.ia` (`416`).  The gate caught them at
FILING time.  Nothing in this base had ever applied the same test to the rows already on
its three shelves, and `867-G2` registered the asymmetry in one sentence worth repeating:

    a stale row is worse than a missing one in a client engagement — it is an active
    recommendation to adopt something nobody maintains.

WHAT IT IS.  Two halves, deliberately separated:

  * OFFLINE — extract every address the count gate CREDITS, per shelf.  The signatures are
    read out of `ingest/derive-counts.py` with `ast`, never copied: `p867-licence-predicate.py`
    established that idiom precisely so a second hand-maintained list cannot drift from the
    gate's.  `--addresses` stops here and prints the population.
  * ONLINE — `gh api search/repositories` with `repo:` qualifiers, BATCHED.  `repos/{o}/{r}`
    is `403` for this session; `search/repositories` is `200` and accepts repeated `repo:`
    qualifiers as an implicit OR (measured this pass: 8 qualifiers in 175 characters
    returned `total_count` 8).  So ~`1,140` addresses cost ~`115` requests, not `1,140`.

🔴 WHAT A MISSING ANSWER MEANS.  An address absent from a `repo:` batch result is NOT
necessarily dead: it may be renamed, made private, or deleted.  The endpoint cannot tell
those apart, so they are reported as `UNRESOLVED` and counted separately from `STALE`.
`867-G2` asked for the stale count "whatever it is" and also warned that a figure near `0`
should itself be disbelieved — so the unresolved arm is published beside it rather than
folded into it.

Usage:
    python3 -I ingest/p868-liveness-census.py --root . --addresses
    python3 -I ingest/p868-liveness-census.py --root . --probe \
        --tsv evidence/liveness-census.2026-11-17-p868.tsv
"""
import argparse
import ast
import datetime
import json
import os
import re
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
STALE_DAYS = 365
BATCH = 10          # ~220 chars of query; the endpoint's limit is 256
SLEEP = 2.4         # 30 search requests/minute


def shelves_from_gate(root):
    """Read SHELVES out of derive-counts.py with `ast` — never a second copy of the list."""
    src = open(os.path.join(root, "ingest", "derive-counts.py"), encoding="utf-8").read()
    tree = ast.parse(src)
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(
                isinstance(t, ast.Name) and t.id == "SHELVES" for t in node.targets):
            return ast.literal_eval(node.value)
    raise SystemExit("derive-counts.py: SHELVES not found")


def tables(lines):
    i = 0
    while i < len(lines) - 1:
        h = lines[i].strip()
        sep = lines[i + 1].strip()
        if h.startswith("|") and re.match(r"^\|[\s:|-]+\|$", sep) and "-" in sep:
            j = i + 2
            body = []
            while j < len(lines) and lines[j].strip().startswith("|"):
                body.append(lines[j])
                j += 1
            yield h, body
            i = j
        else:
            i += 1


ADDR = re.compile(r"github\.com/([A-Za-z0-9][A-Za-z0-9._-]*)/([A-Za-z0-9][A-Za-z0-9._-]*)")


def counted_addresses(root):
    """Return {shelf: {address: first row seen}} for every row the count gate credits."""
    out = {}
    for rel, signatures, _excluded in shelves_from_gate(root):
        path = os.path.join(root, rel)
        if not os.path.exists(path):
            continue
        sigset = set(signatures)
        found = {}
        lines = open(path, encoding="utf-8").read().split("\n")
        for header, body in tables(lines):
            if header not in sigset:
                continue
            for row in body:
                if "github.com/" not in row:
                    continue
                m = ADDR.search(row)
                if not m:
                    continue
                owner, repo = m.group(1), m.group(2).rstrip(".")
                if repo.endswith(".git"):
                    repo = repo[:-4]
                found.setdefault("%s/%s" % (owner, repo), row.strip()[:120])
        out[rel] = found
    return out


def probe(addresses):
    """Batched search/repositories. Returns {lower_address: {pushed, archived, stars, lic}}."""
    got = {}
    uniq = sorted(set(addresses))
    for i in range(0, len(uniq), BATCH):
        chunk = uniq[i:i + BATCH]
        q = " ".join("repo:%s" % a for a in chunk)
        cmd = ["gh", "api", "-X", "GET", "search/repositories", "-f", "q=" + q,
               "-f", "per_page=%d" % (BATCH * 2),
               "--jq", ".items[] | [.full_name, .pushed_at[0:10], (.archived|tostring), "
                       "(.stargazers_count|tostring), ((.license.spdx_id)//\"NONE\")] | @tsv"]
        try:
            res = subprocess.run(cmd, capture_output=True, text=True, timeout=90)
        except subprocess.TimeoutExpired:
            sys.stderr.write("batch %d: timeout\n" % (i // BATCH))
            time.sleep(SLEEP)
            continue
        for line in res.stdout.splitlines():
            f = line.split("\t")
            if len(f) >= 5:
                got[f[0].lower()] = dict(full_name=f[0], pushed=f[1], archived=f[2],
                                         stars=f[3], licence=f[4])
        sys.stderr.write("\rbatch %d/%d  resolved %d" %
                         (i // BATCH + 1, (len(uniq) + BATCH - 1) // BATCH, len(got)))
        sys.stderr.flush()
        time.sleep(SLEEP)
    sys.stderr.write("\n")
    return got


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    ap.add_argument("--addresses", action="store_true", help="offline: print the population")
    ap.add_argument("--probe", action="store_true", help="online: resolve pushed_at")
    ap.add_argument("--today", default=datetime.date.today().isoformat())
    ap.add_argument("--stale-days", type=int, default=STALE_DAYS)
    ap.add_argument("--tsv")
    ap.add_argument("--cache", help="reuse/append a JSON probe cache")
    a = ap.parse_args(argv)

    shelves = counted_addresses(a.root)
    allm = {}
    for rel, found in shelves.items():
        print("%-24s counted addresses: %4d" % (rel, len(found)))
        for addr in found:
            allm.setdefault(addr.lower(), []).append(rel)
    print("%-24s distinct across shelves: %d" % ("TOTAL", len(allm)))
    if not a.probe:
        return 0

    cache = {}
    if a.cache and os.path.exists(a.cache):
        cache = json.load(open(a.cache))
    want = [k for k in allm if k not in cache]
    addr_real = {}
    for rel, found in shelves.items():
        for addr in found:
            addr_real[addr.lower()] = addr
    got = probe([addr_real[k] for k in want]) if want else {}
    cache.update(got)
    if a.cache:
        json.dump(cache, open(a.cache, "w"))

    today = datetime.date.fromisoformat(a.today)
    per_shelf = {rel: dict(LIVE=0, STALE=0, ARCHIVED=0, UNRESOLVED=0) for rel in shelves}
    rows = []
    for key, rels in sorted(allm.items()):
        m = cache.get(key)
        if not m:
            verdict, pushed, age = "UNRESOLVED", "-", -1
        elif m["archived"].lower() == "true":
            verdict, pushed = "ARCHIVED", m["pushed"]
            age = (today - datetime.date.fromisoformat(pushed)).days
        else:
            pushed = m["pushed"]
            age = (today - datetime.date.fromisoformat(pushed)).days
            verdict = "STALE" if age > a.stale_days else "LIVE"
        for rel in rels:
            per_shelf[rel][verdict] += 1
        rows.append((addr_real.get(key, key), verdict, pushed, age,
                     (m or {}).get("stars", "-"), (m or {}).get("licence", "-"),
                     ",".join(rels)))

    print("\n%-24s %6s %6s %9s %11s" % ("shelf", "LIVE", "STALE", "ARCHIVED", "UNRESOLVED"))
    for rel, c in per_shelf.items():
        print("%-24s %6d %6d %9d %11d" % (rel, c["LIVE"], c["STALE"], c["ARCHIVED"],
                                          c["UNRESOLVED"]))
    tot = dict(LIVE=0, STALE=0, ARCHIVED=0, UNRESOLVED=0)
    for _, v, _, _, _, _, _ in rows:
        tot[v] += 1
    print("%-24s %6d %6d %9d %11d   (distinct)" %
          ("TOTAL", tot["LIVE"], tot["STALE"], tot["ARCHIVED"], tot["UNRESOLVED"]))

    worst = sorted([r for r in rows if r[1] == "STALE"], key=lambda r: -r[3])[:30]
    if worst:
        print("\nthe %d oldest STALE counted rows:" % len(worst))
        for r in worst:
            print("  %-52s %s  %5d d  %s" % (r[0], r[2], r[3], r[6]))

    if a.tsv:
        with open(a.tsv, "w", encoding="utf-8") as out:
            out.write("address\tverdict\tpushed\tage_days\tstars\tlicence\tshelves\n")
            for r in rows:
                out.write("\t".join(str(x) for x in r) + "\n")
        print("\nwrote %s" % a.tsv)
    return 0


if __name__ == "__main__":
    sys.exit(main())
