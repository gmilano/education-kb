#!/usr/bin/env python3
"""p499 — sector-wide operative-body edit rate (Gap 488-T).

Reads p498's 76-row grant-path census, fetches each recorded grant payload at
the PINNED head_sha, and grades its operative body against the retained
canonical set (Gap 498-B).

Gap 498-L assertion: output rows MUST equal input rows. A sweep that silently
drops rows and exits 0 is the failure mode that gap names, so the count is
checked and a mismatch is a hard error, not a warning.
"""
import csv, os, sys, time, urllib.request, urllib.error, hashlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from grade_licence import load_canon, grade, git_blob_sha

CENSUS = sys.argv[1]
OUT = sys.argv[2]
canon = load_canon()
assert canon, "no canonical set"

rows = list(csv.DictReader(open(CENSUS), delimiter="\t"))
N_IN = len(rows)
print("input rows: %d   canonical payloads: %d" % (N_IN, len(canon)), flush=True)


def get(url, tries=4):
    for a in range(1, tries + 1):
        try:
            with urllib.request.urlopen(url, timeout=30) as r:
                return r.status, r.read()
        except urllib.error.HTTPError as e:
            if e.code in (403, 429) and a < tries:
                time.sleep(a * a * 2); continue
            return e.code, b""
        except Exception:
            if a < tries:
                time.sleep(a * 2); continue
            return 0, b""
    return 0, b""


out = []
for i, r in enumerate(rows, 1):
    repo, sha = r["repo"], r["head_sha"]
    paths = [p for p in (r.get("root_grant_paths") or "").split(",") if p and p != "-"]
    rec = dict(repo=repo, head_sha=sha, path="", http="", bytes="", blob="",
               closest="", op_verdict="", op_del="", op_ins="", whole_verdict="", note="")
    if not paths:
        rec["op_verdict"] = "NO_ROOT_GRANT"
        out.append(rec); continue
    path = paths[0]
    rec["path"] = path
    url = "https://raw.githubusercontent.com/%s/%s/%s" % (repo, sha, path)
    code, body = get(url)
    rec["http"] = code
    if code != 200 or not body:
        rec["op_verdict"] = "UNREAD"
        out.append(rec); continue
    rec["bytes"] = len(body)
    rec["blob"] = git_blob_sha(body)[:12]
    w, res = grade(body, canon, operative_only=True)
    _, resf = grade(body, canon, operative_only=False)
    b = res[0]
    bf = [x for x in resf if x[0] == b[0]][0]
    rec.update(closest=b[0], op_verdict=b[1], op_del=b[2], op_ins=b[3],
               whole_verdict=bf[1],
               note=(b[4][0][:170] if (b[1] == "DEVIANT" and b[4]) else ""))
    out.append(rec)
    if i % 10 == 0:
        print("  %d/%d" % (i, N_IN), flush=True)

# --- Gap 498-L assertion -------------------------------------------------
if len(out) != N_IN:
    sys.exit("ROW-COUNT ASSERTION FAILED: in=%d out=%d" % (N_IN, len(out)))
print("row-count assertion PASSED: in=%d out=%d" % (N_IN, len(out)))

with open(OUT, "w", newline="") as f:
    wr = csv.DictWriter(f, fieldnames=list(out[0].keys()), delimiter="\t")
    wr.writeheader(); wr.writerows(out)

from collections import Counter
print("\nop_verdict:", dict(Counter(r["op_verdict"] for r in out)))
graded = [r for r in out if r["op_verdict"] in ("IDENTICAL", "DEVIANT")]
dev = [r for r in graded if r["op_verdict"] == "DEVIANT"]
print("graded: %d   operative-body DEVIANT: %d" % (len(graded), len(dev)))
if graded:
    print("OPERATIVE-BODY EDIT RATE = %d/%d = %.1f%%" % (len(dev), len(graded), 100*len(dev)/len(graded)))
ph = [r for r in graded if r["op_verdict"]=="IDENTICAL" and r["whole_verdict"]=="DEVIANT"]
print("clean operative body but filled placeholder: %d (these are the false positives"
      " a whole-payload gate would raise)" % len(ph))
print("\n--- DEVIANT operative bodies ---")
for r in dev:
    print("  %-46.46s %-22.22s -%s/+%s  %s" % (r["repo"], r["closest"], r["op_del"], r["op_ins"], r["note"][:95]))
