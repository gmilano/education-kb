#!/usr/bin/env python3
"""P1049 limb 2, NOISE filter REMOVED — executes `ACTION MK` (registered p185).

p185 ran limb 2 with a NOISE filter that suppressed lines matching
shields.io badges, bullet items, "licence of", "third-party" and "dependenc".
It cost exactly one known real grant: haolpku/Omni-Edu, whose Apache-2.0 line
was suppressed for containing the word "third-party". The filter was kept and
the cost was recorded. ACTION MK asks what ELSE it cost.

This script re-runs the same identifier scan over the same population with
NOISE disabled, and prints every line the filter would have suppressed, so a
human reads them. It is a SCREEN, not a verdict — same discipline as limb 2.

Output: slug, readme, n_suppressed, then one line per suppressed line.
"""
import re, sys, urllib.request, urllib.error
sys.path.insert(0, __file__.rsplit("/", 1)[0])
from whole_readme_scan import IDENT, NOISE, PATHS, RAW, fetch  # noqa: E402

if __name__ == "__main__":
    slugs = [l.strip() for l in open(sys.argv[1]) if l.strip() and not l.startswith("#")]
    print("slug\treadme\tn_suppressed\tsuppressed_line")
    for s in slugs:
        path, txt = fetch(s)
        if txt is None:
            print(f"{s}\t-\t0\tNO_README")
            continue
        sup = [re.sub(r"\s+", " ", l).strip()
               for l in txt.split("\n") if IDENT.search(l) and NOISE.search(l)]
        if not sup:
            print(f"{s}\t{path}\t0\t-")
            continue
        for l in sup:
            print(f"{s}\t{path}\t{len(sup)}\t{l[:220]}", flush=True)
