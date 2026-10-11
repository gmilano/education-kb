#!/usr/bin/env python3
"""ACTION C (layer P) — place an address from its reverse-DNS namespace.

A namespace PLACES a repository only when its leading segment is a country
code (or `eu`). A generic TLD segment — org, com, io, net, dev, work — carries
no geography, and guessing one from the organisation name after it is layer 0,
not layer P. Those are reported as NO-PLACEMENT so the denominator stays
honest.

Region vocabulary is CLOSED: North America | EMEA | APAC | LATAM | Global.
"""
import sys

CC = {
    "us": ("United States", "North America"), "ca": ("Canada", "North America"),
    "mx": ("Mexico", "LATAM"), "br": ("Brazil", "LATAM"),
    "ar": ("Argentina", "LATAM"), "cl": ("Chile", "LATAM"),
    "co": ("Colombia", "LATAM"), "pe": ("Peru", "LATAM"),
    "uy": ("Uruguay", "LATAM"), "ec": ("Ecuador", "LATAM"),
    "cr": ("Costa Rica", "LATAM"), "bo": ("Bolivia", "LATAM"),
    "de": ("Germany", "EMEA"), "fr": ("France", "EMEA"),
    "nl": ("Netherlands", "EMEA"), "uk": ("United Kingdom", "EMEA"),
    "gb": ("United Kingdom", "EMEA"), "ch": ("Switzerland", "EMEA"),
    "at": ("Austria", "EMEA"), "es": ("Spain", "EMEA"),
    "it": ("Italy", "EMEA"), "pt": ("Portugal", "EMEA"),
    "se": ("Sweden", "EMEA"), "no": ("Norway", "EMEA"),
    "dk": ("Denmark", "EMEA"), "fi": ("Finland", "EMEA"),
    "be": ("Belgium", "EMEA"), "ie": ("Ireland", "EMEA"),
    "pl": ("Poland", "EMEA"), "cz": ("Czechia", "EMEA"),
    "gr": ("Greece", "EMEA"), "tr": ("Turkey", "EMEA"),
    "il": ("Israel", "EMEA"), "za": ("South Africa", "EMEA"),
    "ng": ("Nigeria", "EMEA"), "ke": ("Kenya", "EMEA"),
    "ru": ("Russia", "EMEA"), "ua": ("Ukraine", "EMEA"),
    "eu": ("European Union", "EMEA"),
    "jp": ("Japan", "APAC"), "cn": ("China", "APAC"),
    "in": ("India", "APAC"), "kr": ("South Korea", "APAC"),
    "au": ("Australia", "APAC"), "nz": ("New Zealand", "APAC"),
    "sg": ("Singapore", "APAC"), "id": ("Indonesia", "APAC"),
    "my": ("Malaysia", "APAC"), "th": ("Thailand", "APAC"),
    "vn": ("Vietnam", "APAC"), "ph": ("Philippines", "APAC"),
    "tw": ("Taiwan", "APAC"), "hk": ("Hong Kong", "APAC"),
    "pk": ("Pakistan", "APAC"), "bd": ("Bangladesh", "APAC"),
}
# Generic TLDs that look like a leading segment but place nothing.
GENERIC = {
    "org", "com", "net", "io", "dev", "work", "app", "xyz", "info", "biz",
    "me", "cc", "tech", "ai", "cloud", "site", "online", "codes", "tools",
}


def place(groupid: str):
    """Return (country, region, leading_segment) or None."""
    seg = groupid.strip().lower().split(".")[0]
    if seg in CC:
        country, region = CC[seg]
        return country, region, seg
    return None


def main():
    placed, unplaced = [], []
    for line in sys.stdin:
        parts = line.rstrip("\n").split("\t")
        if len(parts) < 4:
            continue
        addr, branch, path, gid = parts[0], parts[1], parts[2], parts[3]
        p = place(gid)
        if p:
            placed.append((addr, gid, p[0], p[1], f"{branch}/{path}"))
        else:
            unplaced.append((addr, gid))
    for r in placed:
        print("PLACED\t" + "\t".join(r))
    for r in unplaced:
        print("NO-PLACEMENT\t" + "\t".join(r))
    print(f"\n# placed={len(placed)} no-placement={len(unplaced)}", file=sys.stderr)
    by = {}
    for r in placed:
        by[r[3]] = by.get(r[3], 0) + 1
    print("# by region: " + ", ".join(f"{k}={v}" for k, v in sorted(by.items())),
          file=sys.stderr)


if __name__ == "__main__":
    main()
