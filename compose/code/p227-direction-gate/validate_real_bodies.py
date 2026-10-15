#!/usr/bin/env python3
"""p227: run family_of() against the REAL licence bodies, read first-hand 2026-10-15.
A fixture control proves the logic; this proves it on the files that caused the error."""
import hashlib
import pathlib
import sys
import urllib.request

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import direction_gate as g

CASES = [
    ("GibbonEdu/core", "master", "LICENSE", "GPL-3.0"),
    ("openedx/openedx-platform", "master", "LICENSE", "AGPL-3.0"),
]

rc = 0
print(f"{'repo':32} {'bytes':>7} {'sha256-12':14} {'naive grep':10} {'family_of':10} {'expected':10} ok")
for slug, ref, path, expected in CASES:
    url = f"https://raw.githubusercontent.com/{slug}/{ref}/{path}"
    body = urllib.request.urlopen(url, timeout=30).read().decode("utf-8", "replace")
    sha = hashlib.sha256(body.encode()).hexdigest()[:12]
    fam, chan, note = g.family_of(body)
    naive = g.naive_affero_grep(body)
    ok = fam == expected
    rc |= 0 if ok else 1
    print(f"{slug:32} {len(body.encode()):>7} {sha:14} {naive:10} {str(fam):10} {expected:10} {'PASS' if ok else 'FAIL'}")
    print(f"{'':32} channel={chan}; {note}")

print()
print("The naive-grep column is the point: it is WRONG on GibbonEdu/core and RIGHT on")
print("openedx, which is exactly how a broken method survives 56 passes undetected.")
sys.exit(rc)
