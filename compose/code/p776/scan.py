#!/usr/bin/env python3
"""p776 shelf scanner -- written from scratch. Two jobs:

ACTION p775-D : fold case before counting, EVERYWHERE, and state the folded
                number. p775 measured 105 of 5,583 displayed addresses as
                case-duplicates and warned that every census keyed on the
                literal address string is over-counted by 105 until this is
                done. D10 has now recurred on three separate axes.

ACTION p775-A : the named gate `gate-claims` -- no licence CELL on any shelf
                may contradict the licence BODY for the same repository. Leg A
                is complete and needs no network: the same repository claimed
                with INCOMPATIBLE licences on two shelves contradicts itself,
                and one of the two cells must be wrong.
"""
import collections, json, pathlib, re, sys

SHELVES = ["agents/top.md", "agents/trending.md", "repos/foundations.md",
           "repos/trending.md", "verticals/solutions.md", "intel/market.md",
           "intel/trends.md", "compose/patterns.md", "intel/open-gaps.md",
           "README.md"]

# a github address inside a markdown link target
ADDR = re.compile(r"https?://github\.com/([A-Za-z0-9][\w.-]*)/([\w.-]+?)(?:[/#?)\s]|$)")
# GitHub's reserved namespace -- these are not user repositories. p774's
# gate-addresses had to learn this the hard way (it reported 73 defects, most
# of them its own blindness).
RESERVED = {"topics", "features", "about", "pricing", "orgs", "sponsors",
            "collections", "trending", "marketplace", "apps", "settings",
            "login", "join", "explore", "readme", "security", "enterprise",
            "customer-stories", "newsroom", "git-guides", "mobile", "codespaces"}

LICENCE_TOKEN = re.compile(
    r"\b(MIT|Apache-2\.0|Apache 2\.0|BSD-2-Clause|BSD-3-Clause|BSD-4-Clause|"
    r"AGPL-3\.0(?:-only|-or-later)?|GPL-3\.0(?:-only|-or-later)?|"
    r"GPL-2\.0(?:-only|-or-later)?|LGPL-3\.0(?:-only|-or-later)?|LGPL-2\.1(?:-only)?|"
    r"MPL-2\.0|EPL-2\.0|ECL-2\.0|ECL-1\.0|ISC|Unlicense|Zlib|CC0-1\.0|0BSD|"
    r"CC-BY-4\.0|CC-BY-SA-4\.0|CC-BY-NC-4\.0|CC-BY-NC-SA-4\.0|CDDL-1\.0|"
    r"EUPL-1\.[012]|OSL-3\.0|AFL-3\.0|CECILL-2\.1|BUSL-1\.1|BSL-1\.0|"
    r"PolyForm Noncommercial(?: 1\.0\.0)?|Commons Clause|"
    r"SustainableUseLicense|Sustainable Use License)\b", re.I)

# families that cannot both be true of one payload
PERMISSIVE = {"mit", "apache-2.0", "bsd-2-clause", "bsd-3-clause", "bsd-4-clause",
              "isc", "unlicense", "zlib", "cc0-1.0", "0bsd", "mpl-2.0", "epl-2.0",
              "ecl-2.0", "ecl-1.0", "bsl-1.0", "afl-3.0", "osl-3.0"}
COPYLEFT = {"agpl-3.0", "agpl-3.0-only", "agpl-3.0-or-later", "gpl-3.0",
            "gpl-3.0-only", "gpl-3.0-or-later", "gpl-2.0", "gpl-2.0-only",
            "gpl-2.0-or-later", "lgpl-3.0", "lgpl-3.0-only", "lgpl-3.0-or-later",
            "lgpl-2.1", "lgpl-2.1-only", "cecill-2.1", "eupl-1.1", "eupl-1.2",
            "eupl-1.0", "cddl-1.0"}
NONFREE = {"cc-by-nc-4.0", "cc-by-nc-sa-4.0", "busl-1.1", "polyform noncommercial",
           "polyform noncommercial 1.0.0", "commons clause", "sustainableuselicense",
           "sustainable use license"}


def bucket(tok):
    t = tok.lower().replace("apache 2.0", "apache-2.0")
    if t in NONFREE:
        return "NONFREE"
    if t in COPYLEFT:
        return "COPYLEFT"
    if t in PERMISSIVE:
        return "PERMISSIVE"
    return "OTHER"


def norm_repo(o, r):
    r = r.rstrip(".,;:")
    if r.endswith(".git"):
        r = r[:-4]
    return o, r


def main(root):
    root = pathlib.Path(root)
    literal = collections.Counter()
    folded = collections.Counter()
    folded_variants = collections.defaultdict(set)
    claims = collections.defaultdict(set)   # folded slug -> {(bucket, token, shelf)}
    instances = 0

    for sh in SHELVES:
        p = root / sh
        if not p.exists():
            continue
        for ln, line in enumerate(p.open(encoding="utf-8", errors="replace"), 1):
            for m in ADDR.finditer(line):
                o, r = norm_repo(m.group(1), m.group(2))
                if o.lower() in RESERVED:
                    continue
                instances += 1
                slug = f"{o}/{r}"
                literal[slug] += 1
                folded[slug.lower()] += 1
                folded_variants[slug.lower()].add(slug)
            # licence claims. Two defects, both caught by control:
            #
            # D3  attributing every licence token on a LINE to every address on
            #     it cross-products the row. 451 contradictions; the first one
            #     hand-read (1024pix/pix AGPL-3.0 vs 1024pix/pix-ui MIT) showed
            #     the SHELVES right and the gate wrong.
            # D4  cell-scoping alone is not enough. A licence token inside a
            #     long PROSE cell is commentary, not a claim -- aalramadan/
            #     peercheck "carried" six licences because one prose cell
            #     surveys them. A CLAIM is a short, licence-shaped cell.
            #
            # So: a claim is a licence token in a cell that is SHORT once markup
            # is stripped, bound to the row's subject (its first address).
            if "|" in line:
                cells = line.split("|")
                row_addrs = []
                for m in ADDR.finditer(line):
                    o, r = norm_repo(m.group(1), m.group(2))
                    if o.lower() not in RESERVED:
                        row_addrs.append(f"{o}/{r}".lower())
                subject = row_addrs[0] if row_addrs else None
                for cell in cells:
                    toks = {t.group(1) for t in LICENCE_TOKEN.finditer(cell)}
                    if not toks:
                        continue
                    bare = re.sub(r"[*`\[\]()_~#>|]", "", cell)
                    bare = re.sub(r"https?://\S+", "", bare)
                    bare = re.sub(r"[^\w\s.+-]", " ", bare)       # emoji, markers
                    bare = re.sub(r"\s+", " ", bare).strip()
                    if len(bare) > 60:                            # prose, not a claim
                        continue
                    own = []
                    for m in ADDR.finditer(cell):
                        o, r = norm_repo(m.group(1), m.group(2))
                        if o.lower() not in RESERVED:
                            own.append(f"{o}/{r}".lower())
                    targets = own or ([subject] if subject else [])
                    for a in targets:
                        for t in toks:
                            claims[a].add((bucket(t), t, f"{sh}:{ln}"))

    dupes = {k: sorted(v) for k, v in folded_variants.items() if len(v) > 1}
    print("=" * 78)
    print("ACTION p775-D -- CASE-FOLD CENSUS")
    print("=" * 78)
    print(f"  link instances scanned        : {instances}")
    print(f"  LITERAL distinct addresses    : {len(literal)}")
    print(f"  FOLDED  distinct addresses    : {len(folded)}")
    print(f"  over-count removed by folding : {len(literal) - len(folded)}")
    print(f"  slugs with >1 case variant    : {len(dupes)}")
    for k, v in sorted(dupes.items())[:25]:
        print(f"      {k}  <-  {v}")

    print()
    print("=" * 78)
    print("ACTION p775-A -- gate-claims LEG A (internal contradiction, complete, no network)")
    print("=" * 78)
    contradictions = []
    for slug, cs in claims.items():
        buckets = {b for b, _, _ in cs if b != "OTHER"}
        if len(buckets) > 1:
            contradictions.append((slug, sorted(cs)))
    print(f"  repositories carrying a licence claim : {len(claims)}")
    print(f"  repositories with CONTRADICTORY claims: {len(contradictions)}")
    for slug, cs in sorted(contradictions):
        print(f"\n  -- {slug}")
        for b, t, where in cs:
            print(f"       {b:<10} {t:<28} {where}")
    json.dump({"folded": len(folded), "literal": len(literal),
               "instances": instances, "dupes": dupes,
               "contradictions": [c[0] for c in contradictions]},
              open("scan-result.json", "w"), indent=1)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else ".")
