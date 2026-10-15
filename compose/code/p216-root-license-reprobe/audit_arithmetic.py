#!/usr/bin/env python3
"""Check p215's published arithmetic before spending ACTION QH's budget on it.

open-gaps.md (p216 registration) states: "this KB's ungranted population is 63, not 94" and
asks QH to "re-probe the 63 remaining ungranted rows". But 94 - 25 = 69. Either the recovery
file lists repositories that were never in the 94, or the 63 is wrong. Establish which, from
the two evidence files on disk, before any network call.
"""

ABSENT = "evidence/ungranted-after-18-forms.2026-10-15-p211.tsv"
RECOVERED = "evidence/lstree-grant-recovery.2026-10-15-p215.tsv"
TRAPS = "evidence/lstree-traps-and-nongrants.2026-10-15-p215.tsv"
PROBE = ["thm-mni-ii/feedbacksystem", "skhdemo/uoft-quercus-mcp"]


def rows(path):
    out = []
    with open(path) as fh:
        for line in fh:
            line = line.strip()
            if not line or line.startswith("#") or line == "repo":
                continue
            f = line.split("\t")[0].strip()
            if f and "/" in f and " " not in f:
                out.append(f)
    return out


absent = set(rows(ABSENT))
recovered = set(rows(RECOVERED))
traps = set(rows(TRAPS))

print(f"ABSENT population (p211)        : {len(absent)}")
print(f"RECOVERED rows listed (p215)    : {len(recovered)}")
print(f"  of which inside the ABSENT set: {len(recovered & absent)}")
print(f"  of which NOT in the ABSENT set: {len(recovered - absent)}")
for r in sorted(recovered - absent):
    print(f"      + {r}")
print(f"TRAP/non-grant rows listed      : {len(traps)}")
print(f"  of which inside the ABSENT set: {len(traps & absent)}")
print()
print(f"94 - 25            = {len(absent) - len(recovered)}")
print(f"ABSENT minus RECOVERED (set)    = {len(absent - recovered)}  <- the real remainder")
print()
for p in PROBE:
    print(f"T215-2 probe row {p}:")
    print(f"   in ABSENT population : {p in absent}")
    print(f"   in RECOVERED list    : {p in recovered}")
