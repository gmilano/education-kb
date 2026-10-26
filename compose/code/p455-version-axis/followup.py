#!/usr/bin/env python3
"""p455 followup -- the three resolution misses of the first probe run, and the
defect that caused one of them.

`slug_from()`'s first cut anchored on END-OF-STRING (`[^/#?]+?/?$`), so it
resolved `https://github.com/owner/repo` and FAILED on
`https://github.com/kurwjan/LanisAPI/issues` -- a `project_urls` value that
points at a sub-page of the repository rather than its root. PyPI records
`Bug Tracker` far more often than `Source`, so this is not an edge case; it is
the commonest shape of back-link PyPI actually serves. Same class as
`Gap 452-D` (the normaliser that matched `github.com` ONLY).
"""
import os
import re
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import family_version as fv
import family_title as ft
import fetch

SLUG2 = re.compile(r"github\.com[:/]+([A-Za-z0-9._-]+)/([A-Za-z0-9._-]+?)(?:\.git)?(?:/|$)", re.I)


def slug_from(url):
    """Owner/repo from ANY github URL shape, including sub-pages."""
    if not url:
        return ""
    url = url.strip().replace("git+", "").replace("git://", "https://")
    m = SLUG2.search(url)
    if not m:
        return ""
    owner, repo = m.group(1), m.group(2)
    if repo in ("issues", "tree", "blob", "wiki", "releases", "pulls"):
        return ""
    return f"{owner}/{repo}"


print("[A] slug_from, both directions")
for url, want in [
    ("https://github.com/kurwjan/LanisAPI/issues", "kurwjan/LanisAPI"),
    ("git+https://github.com/SchoolUtils/WebUntis.git", "SchoolUtils/WebUntis"),
    ("https://github.com/owner/repo/tree/main/sub", "owner/repo"),
    ("https://www.github.com/bain3/pronotepy", "bain3/pronotepy"),
    ("https://gitlab.com/owner/repo", ""),
    ("https://github.com/issues", ""),
]:
    got = slug_from(url)
    print(f"  {'ok  ' if got == want else 'FAIL'} {url!r} -> {got!r} (want {want!r})")

print("\n[B] scoped npm names -- `pawnote`/`pawdirecte` returned 200 with an EMPTY")
print("    record, which is what the registry serves for a name that exists as a")
print("    placeholder. The real packages are SCOPED.")
for name in ["pawnote", "pawdirecte", "@literate.ink/pawnote",
             "@literate.ink/pawdirecte"]:
    enc = name.replace("/", "%2f")
    r = fetch.registry("npm", enc)
    addr = slug_from(r["backlink"])
    print(f"  npm {name:28} status={r['status']} v={r['version']!r:10} "
          f"declared={r['declared']!r:20} -> {addr!r}")

print("\n[C] the resolved stragglers, read first-hand")
for label, addr in [("LanisAPI", "kurwjan/LanisAPI"),
                    ("Linkdirecte", "Scolup/Linkdirecte"),
                    ("education-crm", "asadbekme/education-crm")]:
    g = fetch.grant(addr)
    print(f"  {label:14} {addr:34} {g['verdict']:20} "
          f"{g.get('path', g.get('live_path',''))}@{g.get('ref','')} "
          f"{g.get('bytes',0)}B {g.get('sha','')} "
          f"{fv.family(g['text']) if g['verdict']=='READ' else ''}")

print("\n[D] `withmarbleapp/os-taxonomy` -- does p455 REGRESS the shelf's `ODbL` cell?")
g = fetch.grant("withmarbleapp/os-taxonomy")
print(f"  payload {g['bytes']}B {g['sha']} at {g.get('path')}@{g.get('ref')}")
print(f"  p454 family_title.family() -> {ft.family(g['text'])!r}")
print(f"  p455 family_version.family() -> {fv.family(g['text'])!r}")
print("  (if both say NOT-OSI the grade is INHERITED, not this pass's regression)")

print("\n[E] stock-payload digest collision -- lanis-rs vs maria")
a = fetch.grant("lanis-mobile/lanis-rs")
b = fetch.grant("elderguardian/maria")
print(f"  lanis-rs {a['bytes']}B {a['sha']}")
print(f"  maria    {b['bytes']}B {b['sha']}")
print(f"  identical={a['sha'] == b['sha']} -- both are the STOCK GPL-3.0 text,")
print("  so a digest match here is evidence of a stock licence, NEVER of lineage.")
