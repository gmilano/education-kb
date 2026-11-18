"""p886 — `885-G1`'s acceptance test, executed and scored.

Compares, per shelf row: the `search/repositories` metadata grant (channel A)
against the licence BYTES on the `--symref`-resolved default branch (channel B).
Disagreement is RECORDED as a finding, never resolved toward either side.
"""
import csv
import sys

SP = sys.argv[1]


def load(path, key=0):
    with open(path, newline="", encoding="utf-8") as fh:
        rows = list(csv.reader(fh, delimiter="\t"))
    hdr = rows[0]
    return {r[key]: dict(zip(hdr, r)) for r in rows[1:] if len(r) >= len(hdr) - 1}


nonrepo = {l.strip() for l in open(SP + "/non-repos.txt") if l.strip()}
A = load(SP + "/chanA.tsv")
B0 = load(SP + "/chanB.tsv")
B2 = load(SP + "/chanB2out.tsv")
B = dict(B0)
B.update(B2)                      # repaired rows override

# normalise for comparison only; the raw cells are kept in the evidence file
def norm(x):
    if x in (None, "", "-", "null", "none"):
        return "ABSENT"
    x = x.strip()
    if x in ("NO-GRANT-FILE", "NO-ITEM", "PARSE-ERR"):
        return "ABSENT"
    if x == "NOASSERTION":
        return "NOASSERTION"
    if x == "UNRECOGNISED":
        return "UNRECOGNISED"
    x = x.replace("-DECLARED", "")
    x = x.replace("-only", "").replace("-or-later", "")
    return {"GPL-3.0": "GPL-3.0", "AGPL-3.0": "AGPL-3.0"}.get(x, x)


out = csv.writer(open(SP + "/dual-channel.tsv", "w", newline="", encoding="utf-8"),
                 delimiter="\t")
out.writerow(["slug", "A_spdx", "A_default_branch", "B_ref", "B_path", "B_bytes",
              "B_sha12", "B_family", "B_rider", "verdict", "stars", "pushed"])

tally = {}
findings = []
for slug in sorted(set(A) | set(B)):
    if slug in nonrepo:
        continue
    a = A.get(slug, {})
    b = B.get(slug, {})
    na, nb = norm(a.get("spdx")), norm(b.get("family"))
    if na == nb and na not in ("ABSENT", "NOASSERTION", "UNRECOGNISED"):
        v = "AGREE"
    elif na == "ABSENT" and nb == "ABSENT":
        v = "BOTH-ABSENT"
    elif na in ("NOASSERTION", "ABSENT") and nb not in ("ABSENT", "UNRECOGNISED"):
        v = "BYTES-ONLY"          # T14: metadata abstains, bytes carry a real grant
    elif nb == "ABSENT" and na not in ("ABSENT", "NOASSERTION"):
        v = "FIELD-ASSERTS-PAYLOAD-DENIES"   # 885-G1's own class
    elif nb == "UNRECOGNISED":
        v = "BYTES-UNRECOGNISED"
    else:
        v = "DISAGREE"
    tally[v] = tally.get(v, 0) + 1
    row = [slug, a.get("spdx", "-"), a.get("default_branch", "-"), b.get("ref", "-"),
           b.get("path", "-"), b.get("bytes", "-"), b.get("sha12", "-"),
           b.get("family", "-"), b.get("rider", ""), v,
           a.get("stars", "-"), a.get("pushed", "-")]
    out.writerow(row)
    if v in ("DISAGREE", "FIELD-ASSERTS-PAYLOAD-DENIES"):
        findings.append(row)

tot = sum(tally.values())
print("population: %d rows\n" % tot)
for k in sorted(tally, key=lambda k: -tally[k]):
    print("  %-32s %4d  %5.1f%%" % (k, tally[k], 100.0 * tally[k] / tot))
print("\n=== rows requiring adjudication ===")
for r in findings:
    print("  %-46s A=%-14s B=%-16s %s" % (r[0], r[1], r[7], r[9]))
# default-branch cross-check between the two channels
mism = [s for s in set(A) & set(B) if s not in nonrepo
        and A[s].get("default_branch") not in ("-", None)
        and B[s].get("ref") not in ("-", "", None)
        and B[s]["ref"] != A[s]["default_branch"]]
print("\n=== default-branch disagreement between channels: %d ===" % len(mism))
for s in sorted(mism):
    print("  %-46s A=%-14s B=%s" % (s, A[s]["default_branch"], B[s]["ref"]))
