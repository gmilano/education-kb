#!/usr/bin/env python3
"""`928-G1` — turn `927-R1`'s FLOOR into a MEASUREMENT by adaptive star-band sharding.

`p927` asked 35 topic words, got 3,000 rows and wrote the honest caveat: fifteen legs
reported a `total_count` above the 100-row page it fetched, so "2,298 unheld" is a floor.

This instrument removes the page cap as the binding constraint. For each leg it:
  1. asks for `total_count`;
  2. if <= 100, fetches the single page;
  3. otherwise splits the star axis recursively until every shard is <= 100 and fetches
     each shard, so the union is the COMPLETE leg, not its first page;
  4. a shard that cannot be split further (single star value) is paginated to the 1000-row
     API ceiling and recorded as TRUNCATED, so any residual floor is named, not hidden.

Usage: python3 -I shard.py <out-prefix>
"""
import json, subprocess, sys, time, os

SLEEP = 2.2           # search API: 30 req/min authenticated
MAXPAGE = 100

LEGS = [
    "topic:student-management", "topic:ai-tutor", "topic:study-tools", "topic:canvas-lms",
    "topic:tutoring", "topic:learning-analytics", "topic:plagiarism-detection",
    "topic:grading", "topic:xapi", "topic:stem-education", "topic:pedagogy",
    "topic:scorm", "topic:question-generation", "topic:lti", "topic:moodle",
    "topic:proctoring", "topic:educational", "topic:math-education", "topic:flashcards",
    "topic:gradebook", "topic:openedx", "topic:quiz", "topic:literacy",
    "topic:homework", "topic:note-taking topic:education",
]

calls = 0
def api(q, page=1):
    global calls
    for attempt in range(4):
        calls += 1
        p = subprocess.run(
            ["gh", "api", "-X", "GET", "search/repositories",
             "-f", f"q={q}", "-f", "per_page=100", "-f", f"page={page}"],
            capture_output=True, text=True)
        time.sleep(SLEEP)
        if p.returncode == 0:
            try:
                return json.loads(p.stdout)
            except Exception:
                pass
        err = (p.stderr or "")[:200]
        if "rate limit" in err.lower() or "403" in err:
            time.sleep(20 * (attempt + 1))
            continue
        if attempt == 3:
            return {"_error": err, "total_count": 0, "items": []}
        time.sleep(3)
    return {"_error": "unreachable", "total_count": 0, "items": []}

def band(lo, hi):
    if hi is None:
        return f"stars:>={lo}"
    if lo == hi:
        return f"stars:{lo}"
    return f"stars:{lo}..{hi}"

rows = {}      # slug -> record
shardlog = []

def harvest(leg, lo, hi, depth=0):
    q = f"{leg} {band(lo, hi)}"
    d = api(q)
    if "_error" in d:
        shardlog.append((leg, band(lo, hi), -1, 0, "ERROR:" + d["_error"][:80]))
        return
    tc = d.get("total_count", 0)
    if tc == 0:
        shardlog.append((leg, band(lo, hi), 0, 0, "empty"))
        return
    if tc <= MAXPAGE:
        take(leg, d.get("items", []), q)
        shardlog.append((leg, band(lo, hi), tc, len(d.get("items", [])), "complete"))
        return
    # too big: can we split?
    if hi is not None and lo == hi:
        got = len(d.get("items", []))
        take(leg, d.get("items", []), q)
        for pg in range(2, 11):
            dd = api(q, pg)
            it = dd.get("items", [])
            if not it:
                break
            take(leg, it, q)
            got += len(it)
            if got >= min(tc, 1000):
                break
        shardlog.append((leg, band(lo, hi), tc, got,
                         "TRUNCATED" if got < tc else "complete-paginated"))
        return
    if hi is None:
        # open-ended top band: walk upward in geometric steps
        nxt = max(lo * 4, lo + 50)
        harvest(leg, lo, nxt - 1, depth + 1)
        harvest(leg, nxt, None, depth + 1)
        return
    mid = lo + (hi - lo) // 2
    harvest(leg, lo, mid, depth + 1)
    harvest(leg, mid + 1, hi, depth + 1)

def take(leg, items, q):
    for it in items:
        slug = it.get("full_name", "")
        if not slug:
            continue
        k = slug.lower()
        if k in rows:
            continue
        lic = (it.get("license") or {}).get("spdx_id") or "NOLICENSE"
        rows[k] = dict(
            repo=slug, stars=it.get("stargazers_count", 0), spdx=lic,
            pushed=(it.get("pushed_at") or "")[:10],
            created=(it.get("created_at") or "")[:10],
            archived=str(it.get("archived", False)).lower(),
            desc=(it.get("description") or "").replace("\t", " ").replace("\n", " ")[:300],
            leg=leg, shard=q)

def main():
    prefix = sys.argv[1]
    totals = {}
    for leg in LEGS:
        d = api(leg)
        tot = d.get("total_count", 0)
        totals[leg] = tot
        sys.stderr.write(f"[leg] {leg} total={tot}\n"); sys.stderr.flush()
        harvest(leg, 0, None)
        sys.stderr.write(f"      -> cumulative unique rows: {len(rows)}  calls={calls}\n")
        sys.stderr.flush()
    with open(prefix + "-shardlog.tsv", "w") as fh:
        fh.write("leg\tband\ttotal_count\trows_taken\tstatus\n")
        for r in shardlog:
            fh.write("\t".join(str(x) for x in r) + "\n")
    with open(prefix + "-alltopic.tsv", "w") as fh:
        fh.write("repo\tstars\tspdx\tpushed\tcreated\tarchived\tdescription\tleg\tshard\n")
        for k in sorted(rows):
            r = rows[k]
            fh.write("\t".join([r["repo"], str(r["stars"]), r["spdx"], r["pushed"],
                                r["created"], r["archived"], r["desc"], r["leg"],
                                r["shard"]]) + "\n")
    with open(prefix + "-legtotals.tsv", "w") as fh:
        fh.write("leg\ttotal_count\n")
        for k, v in totals.items():
            fh.write(f"{k}\t{v}\n")
    sys.stderr.write(f"DONE rows={len(rows)} calls={calls} shards={len(shardlog)}\n")

main()
