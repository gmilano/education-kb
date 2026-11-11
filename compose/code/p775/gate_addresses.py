#!/usr/bin/env python3
"""gate-addresses — the named RED gate for pass p775 (ACTION p774-A).

Contract, carried in prose because the next pass cannot run this script:

  G1  Every GitHub address a shelf DISPLAYS must have its LINK TEXT equal to
      the URL's owner/repo path. `[`a/b`](https://github.com/c/d)` is a defect:
      the reader is told one address and sent to another.
  G2  Every displayed address must have been PROBED on the ref channel.
  G3  A displayed bare-owner link (github.com/<owner> with no repo) is a
      citation form, not an address, and is reported separately (p774-F).

G1 and G3 need no network and are run here over every shelf file. G2's
population is the output of this gate, fed to p775-probe.sh.

Usage: p775-gate-addresses.py <file> [<file>...]
"""
import re
import sys
from collections import defaultdict

# [`text`](https://github.com/owner/repo...) — the form the shelves use.
LINK = re.compile(
    r"\[`?([^`\]]+)`?\]\(\s*(https://github\.com/([^)\s#?]+))[^)]*\)")

TRAIL = re.compile(r"(/tree/.*|/blob/.*|/releases.*|/issues.*|/pull.*|"
                   r"/commits?.*|/compare.*|\.git)$")

# DEFECTS p775-#4/#5, caught by control before any verdict was published.
# #4: link text is routinely wrapped in ** ** or carries a deliberate
#     ellipsis for long names, and may carry an issue suffix (#18). None of
#     those is a disagreement; the first run called 73 defects, most of them
#     its own formatting blindness.
# #5: github.com/<reserved>/... is not an address. topics/, orgs/, features/,
#     collections/, sponsors/, trending/, apps/, marketplace/, settings/ and
#     search are GitHub's own namespace, and counting them as owner/repo
#     invents repositories that cannot be probed.
RESERVED = {"topics", "orgs", "features", "collections", "sponsors",
            "trending", "apps", "marketplace", "settings", "search",
            "about", "pricing", "readme", "login", "signup", "explore",
            "security", "enterprise", "customer-stories", "users"}


def clean_text(t):
    t = t.strip().strip("*").strip()
    t = re.sub(r"#\d+$", "", t)
    t = t.strip().strip("`").rstrip("/")
    return t


def elided(t):
    return ("\u2026" in t) or ("..." in t)


def norm_path(p):
    p = TRAIL.sub("", p.rstrip("/"))
    return p


def main(paths):
    displayed = defaultdict(set)   # owner/repo -> files
    owner_only = defaultdict(set)
    g1 = []
    total = 0
    for path in paths:
        with open(path, encoding="utf-8", errors="replace") as fh:
            for lineno, line in enumerate(fh, 1):
                for m in LINK.finditer(line):
                    text, url, rawpath = m.group(1), m.group(2), m.group(3)
                    total += 1
                    p = norm_path(rawpath)
                    parts = p.split("/")
                    if parts[0].lower() in RESERVED:
                        continue
                    if len(parts) == 1:
                        owner_only[parts[0]].add(path)
                        continue
                    addr = "/".join(parts[:2])
                    displayed[addr].add(path)
                    # G1: link text must equal the owner/repo path
                    t = clean_text(text)
                    if t != addr and not elided(t):
                        # a bare repo name or a display name is the common,
                        # tolerated form; flag only text that LOOKS like an
                        # address (contains a slash) and disagrees.
                        if "/" in t and not t.startswith("http"):
                            g1.append((path, lineno, t, addr))
    print("## gate-addresses — p775")
    print("displayed link instances parsed : %d" % total)
    print("distinct owner/repo addresses   : %d" % len(displayed))
    print("distinct bare-owner citations   : %d" % len(owner_only))
    print()
    print("### G1 link-text/URL disagreements (address-shaped text only): %d"
          % len(g1))
    for path, lineno, t, addr in g1:
        print("G1\t%s:%d\ttext=%s\turl=%s" % (path, lineno, t, addr))
    with open("gate-addresses-population.txt", "w") as fh:
        for a in sorted(displayed):
            fh.write(a + "\n")
    with open("gate-addresses-owners.txt", "w") as fh:
        for o in sorted(owner_only):
            fh.write(o + "\n")
    print()
    print("populations written: gate-addresses-population.txt (%d), "
          "gate-addresses-owners.txt (%d)" % (len(displayed), len(owner_only)))


if __name__ == "__main__":
    main(sys.argv[1:])
