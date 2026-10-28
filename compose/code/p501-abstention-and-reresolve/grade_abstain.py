#!/usr/bin/env python3
"""p501 — closes Gap 499-B: the canonical grader had no way to DECLINE.

p499 fed Wakoma/nimble's CERN-OHL-S-2.0 payload (outside the retained set) to a
nearest-neighbour matcher and got back the meaningless label "BSD-2-Clause,
-90/+1947". A grader that cannot abstain will label anything.

The guard, in one clause: label only when the best canonical match's RELATIVE
operative distance is within BAND; otherwise ABSTAIN and name the distance.

    rel = (insertions + deletions) / canonical_operative_words
    label  if rel <= BAND (0.15)
    ABSTAIN otherwise

It also carries p500's rule: grade against EVERY canonical form held for a
licence family and keep the BEST match, so the two legitimate Apache-2.0 forms
cannot manufacture a phantom -19.
"""
import sys, os, re, difflib

BAND = 0.15
CANON_DIR = sys.argv[1]
IN_TSV    = sys.argv[2]
OUT_TSV   = sys.argv[3]

MARKERS = ("APPENDIX: How to apply the Apache License",
           "How to Apply These Terms to Your New Programs",
           "END OF TERMS AND CONDITIONS")

def operative(text):
    cut = len(text)
    for m in MARKERS:
        i = text.find(m)
        if i != -1:
            cut = min(cut, i)
    keep = []
    for line in text[:cut].splitlines():
        s = line.strip().lower()
        if s.startswith("copyright") and (("(c)" in s) or ("©" in s)
                or re.search(r"\b(?:19|20)\d\d\b|\byyyy\b|<year>", s)):
            continue
        keep.append(line)
    return re.findall(r"\S+", " ".join(keep))

# family name from the filename: "Apache-2.0.apache-org.txt" and "Apache-2.0.txt" are
# two FORMS of one family.
canon = {}
for fn in sorted(os.listdir(CANON_DIR)):
    if not fn.endswith(".txt"):
        continue
    words = operative(open(os.path.join(CANON_DIR, fn), encoding="utf-8", errors="replace").read())
    fam = fn[:-4]
    for suffix in (".apache-org",):
        if fam.endswith(suffix):
            fam = fam[:-len(suffix)]
    canon.setdefault(fam, []).append((fn, words))

def distance(a, b):
    sm = difflib.SequenceMatcher(a=a, b=b, autojunk=False)
    ins = dele = 0
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "delete":   dele += i2 - i1
        elif tag == "insert": ins  += j2 - j1
        elif tag == "replace":
            dele += i2 - i1; ins += j2 - j1
    return ins, dele

rows_in = rows_out = 0
out = [("label_input", "payload_bytes", "payload_words", "best_family", "best_form",
        "ins", "del", "rel", "verdict")]
with open(IN_TSV) as f:
    for line in f:
        line = line.rstrip("\n")
        if not line.strip() or line.startswith("#"):
            continue
        rows_in += 1
        name, path = line.split("\t")[:2]
        raw = open(path, encoding="utf-8", errors="replace").read()
        pw = operative(raw)
        best = None
        for fam, forms in canon.items():
            for fn, cw in forms:
                ins, dele = distance(cw, pw)
                rel = (ins + dele) / max(1, len(cw))
                if best is None or rel < best[4]:
                    best = (fam, fn, ins, dele, rel)
        fam, fn, ins, dele, rel = best
        verdict = fam if rel <= BAND else "ABSTAIN(nearest=%s rel=%.2f)" % (fam, rel)
        out.append((name, os.path.getsize(path), len(pw), fam, fn, ins, dele,
                    "%.4f" % rel, verdict))
        rows_out += 1

with open(OUT_TSV, "w") as f:
    for r in out:
        f.write("\t".join(str(x) for x in r) + "\n")

print("BAND=%.2f  canonical families=%d  forms=%d" % (BAND, len(canon), sum(len(v) for v in canon.values())))
print("rows_in=%d rows_out=%d  ASSERT %s" % (rows_in, rows_out, "PASS" if rows_in == rows_out else "FAIL"))
for r in out[1:]:
    print("%-46s %-18s ins=%-5s del=%-5s rel=%-7s -> %s" % (r[0], r[3], r[5], r[6], r[7], r[8]))
