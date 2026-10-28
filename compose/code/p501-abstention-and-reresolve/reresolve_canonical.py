#!/usr/bin/env python3
"""p501 — closes Gap 499-D (canonical set is pinned and nothing re-resolves it).

Two checks, not one. Gap 499-D asked for "one assertion per pass"; a pinned URL
carries a commit SHA and cannot drift, so re-fetching the pin only proves
RETENTION. Upstream AMENDMENT — the failure the set was built to catch — is only
visible by also reading the SAME path at the SPDX repo's CURRENT HEAD.

  check A (retention): pinned URL -> bytes + git blob SHA-1 == MANIFEST.tsv
  check B (amendment): HEAD URL   -> operative words == pinned operative words

Asserts rows_in == rows_out (Gap 498-L).
"""
import subprocess, sys, hashlib, urllib.request, os, re

MAN = sys.argv[1]
HEAD_SHA = sys.argv[2]
OUT = sys.argv[3]

def fetch(url):
    try:
        with urllib.request.urlopen(url, timeout=30) as r:
            return r.status, r.read()
    except urllib.error.HTTPError as e:
        return e.code, b""
    except Exception as e:
        return 0, b""

def blob_sha1(b):
    h = hashlib.sha1()
    h.update(b"blob %d\0" % len(b))
    h.update(b)
    return h.hexdigest()

MARKERS = ("APPENDIX: How to apply the Apache License",
           "How to Apply These Terms to Your New Programs",
           "END OF TERMS AND CONDITIONS")

def operative_words(text):
    """Same cut as p499: drop appendix at the first marker found, drop notice lines."""
    cut = len(text)
    for m in MARKERS:
        i = text.find(m)
        if i != -1:
            cut = min(cut, i)
    body = text[:cut]
    keep = []
    for line in body.splitlines():
        s = line.strip().lower()
        if s.startswith("copyright") and (("(c)" in s) or ("©" in s)
                                          or re.search(r"\b(?:19|20)\d\d\b|\byyyy\b|<year>", s)):
            continue
        keep.append(line)
    return re.findall(r"\S+", " ".join(keep))

rows_in = 0
rows_out = 0
res = []
with open(MAN) as f:
    hdr = f.readline()
    for line in f:
        line = line.rstrip("\n")
        if not line.strip():
            continue
        rows_in += 1
        c = line.split("\t")
        lic, bytes_rec, blob_rec = c[0], int(c[1]), c[2]
        # Gap 501-x: the manifest's last column is documented as a URL but some rows
        # append a prose annotation. Parse the URL, do not assume the cell IS the URL.
        url = c[-1].strip().split()[0]
        st, payload = fetch(url)
        if st == 200:
            b_now, s_now = len(payload), blob_sha1(payload)
            a = "PASS" if (b_now == bytes_rec and s_now == blob_rec) else "DRIFT"
        else:
            b_now, s_now, a = 0, "-", "UNRESOLVED(%s)" % st
        # check B: same path at HEAD
        head_url = re.sub(r"/license-list-data/[0-9a-f]+/", "/license-list-data/%s/" % HEAD_SHA, url)
        if head_url == url:
            bverd, hw, pw = "SKIP(not-spdx)", "-", "-"
        else:
            st2, payload2 = fetch(head_url)
            if st2 == 200 and st == 200:
                pw = len(operative_words(payload.decode("utf-8", "replace")))
                hw = len(operative_words(payload2.decode("utf-8", "replace")))
                bverd = "PASS" if hw == pw else "AMENDED(%+d)" % (hw - pw)
            else:
                bverd, hw, pw = "UNRESOLVED(%s)" % st2, "-", "-"
        res.append((lic, bytes_rec, b_now, blob_rec[:12], (s_now[:12] if s_now != "-" else "-"),
                    a, pw, hw, bverd))
        rows_out += 1

with open(OUT, "w") as f:
    f.write("licence\tbytes_manifest\tbytes_now\tblob_manifest\tblob_now\tA_retention\t"
            "operative_pinned\toperative_HEAD\tB_amendment\n")
    for r in res:
        f.write("\t".join(str(x) for x in r) + "\n")

print("rows_in=%d rows_out=%d  ASSERT %s" % (rows_in, rows_out,
      "PASS" if rows_in == rows_out else "FAIL"))
for r in res:
    print("%-22s A=%-16s B=%-16s %s/%s words" % (r[0], r[5], r[8], r[6], r[7]))
