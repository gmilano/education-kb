#!/usr/bin/env python3
"""Publisher-class classifier for `Gap 444-A`.

The gap's question: does an address published by the INSTITUTION that operates an
education platform carry a grant less often than one published by anybody else?

p444 answered it on five rows in one country.  To answer it at corpus scale the publisher
has to be classified from the OWNER string alone, because `api.github.com` is 403 on this
host (measured, `probe_payload.sh` header) so there is no `type: Organization` field to
read and no org membership to query.

So this classifier is deliberately PRECISION-FIRST on the INSTITUTIONAL class, in two
tiers, and its precision is then hand-measured rather than asserted (`P5`):

  Tier A -- an unambiguous institution WORD in the owner string.  A publisher called
           `universidad-de-x` is a university; nothing else is called that.
  Tier B -- an explicit ACRONYM allowlist.  Latin American and European institutional
           orgs are overwhelmingly acronyms (`ifrn`, `unal`, `usp`, `uanl`), which Tier A
           cannot see.  Every entry here is a named institution, not a pattern.

Everything else is NON-INSTITUTIONAL.  That class therefore mixes individuals, software
projects and companies: the gap asks institution-vs-everyone-else, so the complement is
the right comparison and the mixing is stated, not hidden.
"""
import re, sys

# ── Tier A: institution words. Anchored to avoid substring accidents ──────────────────
# `univ` catches universidad/universidade/university/universitat/universite/universiteit/
# universita/universitet.  `uniwersytet` is spelled out because Polish drops the `v`.
TIER_A = [
    r"univ", r"uniwersytet", r"hochschule", r"fachhochschule",
    r"instituto", r"institut\b", r"faculdade", r"facultad", r"faculte",
    r"colegio", r"escola", r"escuela", r"politecnic", r"polytechnic", r"politehnic",
    r"ministerio", r"ministry", r"minedu", r"mineduc", r"schulministerium",
    r"\bschool", r"school\b", r"\bcollege", r"college\b", r"\bcampus\b",
]
TIER_A_RE = re.compile("|".join(TIER_A), re.I)

# ── Tier B: named institutional orgs, acronym-spelled. Each is an institution. ────────
# Brazil federal institutes/universities, Mexico, Colombia, Chile, Argentina, Peru,
# Uruguay, plus the European and APAC institutional publishers this base has shelved.
TIER_B = {
    # Brazil
    "ifrn", "ifrn-oficial", "ifpb", "ifce", "ifsp", "ifmg", "ifg", "ifpe", "ifba", "ifes",
    "ifsul", "ifc", "ifro", "ifam", "ifto", "ifal", "ifpi", "ifma", "ifms", "ifmt",
    "usp", "unicamp", "ufrn", "ufpb", "ufmg", "ufsc", "ufba", "ufpe", "ufrj", "ufrgs",
    "ufc", "ufg", "ufes", "ufpr", "ufla", "ufv", "ufabc", "ufscar", "unesp", "unb",
    "cefet", "cefetmg", "fiocruz", "embrapa",
    # Mexico
    "unam", "uanl", "ipn", "udg", "buap", "uaem", "uaslp", "uady", "uas", "itesm",
    "tecnm", "cinvestav", "conacyt", "sep",
    # Colombia / Chile / Argentina / Peru / Uruguay / Bolivia / Ecuador
    "unal", "udea", "uniandes", "javeriana", "icesi", "eafit",
    "udec", "uchile", "puc", "uc-cl", "usach", "utfsm", "uai",
    "uba", "utn", "unlp", "unc", "unr", "unsam", "conicet",
    "pucp", "unmsm", "uni-pe", "upc-pe",
    "udelar", "fing-udelar", "ceibal", "plandeceibal",
    # EMEA institutional publishers
    "ethz", "epfl", "tudelft", "tue", "kuleuven", "ugent", "uio", "uib", "ntnu", "dtu",
    "chalmers", "kth", "lu-se", "aalto", "tuwien", "tum", "rwth", "kit", "lmu",
    "sorbonne", "inria", "cnrs", "uned", "upm", "upc", "uab", "uam", "us-es",
    "ox", "cam", "ucl", "imperial", "ed-ac-uk", "openuniversity",
    # APAC institutional publishers
    "nus", "ntu", "smu-sg", "iitb", "iitd", "iitm", "iitk", "iisc", "nptel",
    "tsinghua", "pku", "zju", "sjtu", "ustc", "utokyo", "kyoto-u", "titech",
    "snu", "kaist", "postech", "unimelb", "usyd", "unsw", "anu",
    # North America institutional publishers
    "mit", "harvard", "stanford", "berkeley", "cmu", "caltech", "uwaterloo", "utoronto",
    "ubc", "mcgill", "umich", "uw", "nyu", "columbia", "cornell", "yale", "princeton",
    "ucla", "ucsd", "gatech", "illinois", "wisc", "osu", "psu", "umd", "virginia",
    "cahlr", "openedx-institutional",
}

def classify(owner):
    """-> 'INSTITUTIONAL' | 'NON-INSTITUTIONAL', plus the tier that decided it."""
    o = owner.strip().lower()
    if o in TIER_B:
        return "INSTITUTIONAL", "B"
    if TIER_A_RE.search(o):
        return "INSTITUTIONAL", "A"
    return "NON-INSTITUTIONAL", "-"


def main():
    print("slug\towner\tclass\ttier\tverdict\tfrom_pass")
    next(sys.stdin)                                    # header
    for line in sys.stdin:
        parts = line.rstrip("\n").split("\t")
        if len(parts) < 3:
            continue
        slug, verdict, pno = parts[0], parts[1], parts[2]
        owner = slug.split("/")[0]
        cls, tier = classify(owner)
        print(f"{slug}\t{owner}\t{cls}\t{tier}\t{verdict}\t{pno}")


if __name__ == "__main__":
    main()
