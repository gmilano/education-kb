#!/usr/bin/env python3
"""p774 distribution-grant probe -- ACTION p773-E, owed a THIRD time.

p773-E: "If a third pass cannot run it, RETIRE it rather than carry it a fourth
time." This pass runs it, so it is discharged rather than retired.

The question it answers as a MEASUREMENT: what grant does the DISTRIBUTED
artefact carry, as opposed to the repository root? A studio that redistributes
ships the packaging tree, not the README. `EnergyPlus`'s CMake-templated EULA
has been this base's only known instance since p771 and was never generalised.

Paths probed per address (the four p772-E/p773-E name):
  debian/control, debian/copyright   -- Debian source package metadata
  installer/, packaging/             -- directory presence via a known index file
  *license*.in                       -- a TEMPLATED grant, the EnergyPlus shape
"""
import sys, urllib.request, urllib.error
from concurrent.futures import ThreadPoolExecutor

PATHS = ["debian/control", "debian/copyright", "debian/rules",
         "packaging/LICENSE", "packaging/license.txt", "installer/LICENSE",
         "LICENSE.in", "license.in", "COPYING.in", "LICENSE.txt.in",
         "cmake/LICENSE.in", "resources/LICENSE.in"]
UA = {"User-Agent": "kb-ingest-dist-probe/1.0"}

def head(url):
    try:
        r = urllib.request.Request(url, headers=UA, method="GET")
        with urllib.request.urlopen(r, timeout=15) as f:
            return f.status, len(f.read(4096))
    except urllib.error.HTTPError as e:
        return e.code, 0
    except Exception:
        return 0, 0

def work(t):
    slug, branch = t
    hits = []
    for p in PATHS:
        code, n = head(f"https://raw.githubusercontent.com/{slug}/{branch}/{p}")
        if code == 200 and n > 0:
            hits.append(f"{p}({n}B+)")
    return f"{slug}\t{branch}\t" + (";".join(hits) if hits else "NONE")

if __name__ == "__main__":
    targets = [l.rstrip("\n").split("\t")[:2] for l in open(sys.argv[1]) if l.strip()]
    with ThreadPoolExecutor(max_workers=12) as ex:
        for line in ex.map(work, targets):
            print(line, flush=True)
