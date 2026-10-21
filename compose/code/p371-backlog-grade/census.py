#!/usr/bin/env python3
"""p371 — the census, per SLUG. adjudicate.py emits one row per grant FILE, so a repo
carrying LICENSE + licenses/ appears twice; every figure below dedupes on the slug and
keeps the strongest grant for it."""
import csv, sys, collections, re

PERMISSIVE = {"MIT", "Apache-2.0", "BSD-3-Clause", "BSD-2-Clause", "BSD-2-Clause-FreeBSD",
              "ECL-2.0", "ISC", "Unlicense", "CC0-1.0", "Zlib", "MPL-2.0-permissive"}
COPYLEFT = {"GPL-3.0", "GPL-2.0", "AGPL-3.0", "LGPL-3.0", "LGPL-2.1", "GPL-?", "MPL-2.0",
            "EPL-2.0", "SSPL-1.0", "OSL-3.0"}
CONTENT = {"CC-BY-4.0", "CC-BY-SA-4.0", "CC-BY-NC-SA-4.0", "CC-BY-NC-4.0",
           "CC-BY-NC-ND-4.0", "CC-BY-3.0", "ODbL-1.0", "CC-BY-SA-3.0"}
RESTRICTED = {"PolyForm", "BUSL-1.1", "Elastic-2.0", "NON-COMMERCIAL"}

adj = list(csv.DictReader(open(sys.argv[1]), delimiter="\t"))
reg = {r["slug"]: r for r in csv.DictReader(open(sys.argv[2]), delimiter="\t")}

# 🔴 D6, found on the 1 859-address run. `Dungeon-CampusMinden/Dungeon` carries FIVE
# grant files — LICENSE.md (MIT, the CODE), LICENSE-ASSETS.md (CC0), LICENSE-ICONS.md,
# LICENSE-NOTICE.md (LGPL-?), LICENSE-PAPER.md (CC-BY-SA-4.0) — and the first draft of
# this census ranked by permissiveness, so the repo's licence cell came from its ASSET
# grant. 🟢 `gate-grant-scope` already says a grant has a SCOPE: an unscoped root file
# is the code grant, and `LICENSE-<SCOPE>` describes something else. 160 of these 1 859
# addresses carry more than one grant file, so this is not a corner case.
SCOPED = re.compile(r"licen[cs]e[-_.]?(assets?|icons?|paper|docs?|data|media|fonts?|"
                    r"images?|content|examples?|third[-_]?party|deps|vendor|notice)",
                    re.I)
UNSCOPED = re.compile(r"^(licen[cs]e|copying|unlicen[cs]e)(\.(md|txt|rst|html))?$", re.I)

by_slug = {}
for r in adj:
    by_slug.setdefault(r["slug"], []).append(r)


def code_grant(rows):
    """-> (row, scope_note). The CODE grant, or a declared refusal to pick one."""
    unscoped = [r for r in rows if UNSCOPED.match((r["licence_path"] or "").strip())]
    if len(unscoped) == 1:
        return unscoped[0], "single-root"
    if len(unscoped) > 1:
        # several unscoped roots: a dual licence. Reported, never collapsed.
        return unscoped[0], "MULTI-ROOT"
    unscopedish = [r for r in rows if not SCOPED.search(r["licence_path"] or "")
                   and (r["licence_path"] or "-") != "-"]
    if len(unscopedish) == 1:
        return unscopedish[0], "single-nonscoped"
    if not unscopedish:
        if any((r["licence_path"] or "-") != "-" for r in rows):
            # every grant file in the tree is SCOPED — the code is ungranted
            return rows[0], "SCOPED-ONLY"
        return rows[0], "no-grant"
    return unscopedish[0], "AMBIGUOUS"


best, scope_note = {}, {}
for sl, rows in by_slug.items():
    row, note = code_grant(rows)
    best[sl] = row
    scope_note[sl] = note

def klass(f):
    if f in PERMISSIVE: return "permissive"
    if f in COPYLEFT: return "copyleft"
    if f in CONTENT: return "content"
    if f in RESTRICTED: return "restricted"
    if f == "NO-GRANT-IN-TREE": return "no-grant"
    return "unclassified"

print(f"addresses graded\t{len(best)}")
import collections as _c
print("  multi-grant addresses\t" + str(sum(1 for v in by_slug.values() if len(v) > 1)))
for k, v in _c.Counter(scope_note.values()).most_common():
    print(f"  scope {k}\t{v}")
by_status = collections.Counter(r["status"] for r in best.values())
for k, v in by_status.most_common(): print(f"  status {k}\t{v}")
by_dom = collections.Counter(r["domain"] for r in best.values())
print()
for k, v in by_dom.most_common(): print(f"  domain {k}\t{v}")

indomain = {s: r for s, r in best.items() if r["domain"] == "EDUCATION"}
print(f"\nIN DOMAIN\t{len(indomain)}")
by_k = collections.Counter(klass(r["family"]) for r in indomain.values())
for k, v in by_k.most_common(): print(f"  {k}\t{v}")

perm = {s: r for s, r in indomain.items() if klass(r["family"]) == "permissive"}
print(f"\nIN DOMAIN + PERMISSIVE\t{len(perm)}")

print("\n=== in-domain x ORIGIN region ===")
rows = collections.Counter()
for s, r in indomain.items():
    rr = reg.get(s, {})
    rows[(rr.get("origin_region", "Global"), klass(r["family"]))] += 1
regions = ["North America", "EMEA", "APAC", "LATAM", "Global"]
kinds = ["permissive", "copyleft", "content", "restricted", "no-grant", "unclassified"]
print("region\t" + "\t".join(kinds) + "\ttotal")
for g in regions:
    cells = [rows[(g, k)] for k in kinds]
    print(f"{g}\t" + "\t".join(str(c) for c in cells) + f"\t{sum(cells)}")

print("\n=== in-domain + permissive, PLACED only, by region, top by refs ===")
for g in ["North America", "EMEA", "APAC", "LATAM"]:
    cand = [(int(r["refs"] or 0), s, r["family"], reg[s]["origin_channel"],
             reg[s]["origin_evidence"], r["licence_path"], r["head"])
            for s, r in perm.items()
            if reg.get(s, {}).get("origin_region") == g]
    cand.sort(reverse=True)
    print(f"\n-- {g} ({len(cand)} addresses)")
    for refs, s, fam, ch, ev, path, head in cand[:12]:
        print(f"   {refs:5d}  {s:52s} {fam:14s} {ch:11s} {ev[:34]:34s} {path} @ {head}")
