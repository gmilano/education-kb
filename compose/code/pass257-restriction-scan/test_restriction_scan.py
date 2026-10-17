"""Controls for `pass257-restriction-scan`.

Every fixture is a REAL payload read first-hand from `raw.githubusercontent.com` at
`p257` on an `ls-remote`-resolved ref, not text this base wrote for itself — which
is the gap `p255` named when `p252`'s hardening had only ever been tested against
its own fixtures.

Run from this directory (`p355-cwd-portability`: `python3 -I` strips the script's
directory from `sys.path`, so the suite only imports from its own cwd).
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import restriction_scan as rs  # noqa: E402

FIX = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fixtures-p257")

PASS = 0
FAIL = 0


def check(name, got, want):
    global PASS, FAIL
    if got == want:
        PASS += 1
    else:
        FAIL += 1
        print(f"FAIL {name}\n     got  {got!r}\n     want {want!r}")


def truthy(name, got):
    global PASS, FAIL
    if got:
        PASS += 1
    else:
        FAIL += 1
        print(f"FAIL {name}: expected truthy, got {got!r}")


def load(fname):
    with open(os.path.join(FIX, fname), encoding="utf-8", errors="replace") as fh:
        return fh.read()


USC = load("usc-academic-1812.txt")
APACHE = load("apache-2.0-11356.txt")
GPL = load("gpl-3.0-35146.txt")
MIT = load("mit-1091.txt")
NOTFOUND = load("notfound-14.txt")

# ── 1. The USC academic licence: restricted, and SAID to be restricted ───────────
usc = rs.scan(USC)
check("usc.verdict", usc["verdict"], rs.VERDICT_RESTRICTED)
check("usc.family", usc["family"], None)
check("usc.bytes", usc["bytes"], 1812)
check("usc.usable", rs.is_usable_permissive(USC), False)
# 🔴 The whole point: the EVIDENCE is non-empty.  `p1054` reports `[]` here.
truthy("usc.hits non-empty", len(usc["hits"]) > 0)
for token in ("non-profit", "commercial use", "research purposes",
              "all rights reserved", "without a written agreement"):
    truthy(f"usc.hits carries {token!r}", token in usc["hits"])

# ── 2. Verbatim Apache-2.0: permissive, and not confused with the above ─────────
ap = rs.scan(APACHE)
check("apache.verdict", ap["verdict"], rs.VERDICT_PERMISSIVE)
check("apache.family", ap["family"], "Apache-2.0")
check("apache.bytes", ap["bytes"], 11356)
check("apache.hits", ap["hits"], ())
check("apache.usable", rs.is_usable_permissive(APACHE), True)

# ── 3. Verbatim GPL-3.0: the benign-hit trap, measured ──────────────────────────
gpl = rs.scan(GPL)
check("gpl.family", gpl["family"], "GPL")
check("gpl.verdict", gpl["verdict"], rs.VERDICT_COPYLEFT)
# The token IS present and IS reported — it is simply not EFFECTIVE for this family.
check("gpl.hits", gpl["hits"], ("noncommercial",))
check("gpl.benign_hits", gpl["benign_hits"], ("noncommercial",))
check("gpl.effective_hits", gpl["effective_hits"], ())
check("gpl.usable", rs.is_usable_permissive(GPL), False)

# ── 4. Verbatim MIT: agrees with p1054 by construction ──────────────────────────
mit = rs.scan(MIT)
check("mit.family", mit["family"], "MIT")
check("mit.verdict", mit["verdict"], rs.VERDICT_PERMISSIVE)
check("mit.usable", rs.is_usable_permissive(MIT), True)

# ── 5. The 404 body is never a grant ────────────────────────────────────────────
nf = rs.scan(NOTFOUND)
check("notfound.bytes", nf["bytes"], 14)
check("notfound.family", nf["family"], None)
check("notfound.verdict", nf["verdict"], rs.VERDICT_UNCLASSIFIED)
check("notfound.usable", rs.is_usable_permissive(NOTFOUND), False)

# ── 6. THE REGRESSION CONTROL — these six assertions FAIL against p1054 ─────────
# They are the measurement that justifies this instrument existing, kept as code so
# a later pass cannot re-derive the defect by hand.  `p1054` is imported if it is
# reachable; if it is not, the controls are declared SKIPPED rather than passed.
P1054 = os.path.join(os.path.dirname(FIX), "..", "p1054-mit-plus-clause")
_p1054_ok = False
if os.path.isdir(P1054):
    sys.path.insert(0, os.path.abspath(P1054))
    try:
        import mit_plus  # noqa: E402

        _p1054_ok = True
    except Exception as exc:  # pragma: no cover - reported, never swallowed
        print(f"NOTE p1054 unimportable ({exc!r}); its controls are SKIPPED, not passed")
else:
    # 🔴 Said out loud, because the alternative is a count that shrinks silently.
    # The mutation run that proved this suite's failure capability executed from a
    # scratch copy where `p1054` was not on the expected relative path, and the
    # control count simply dropped 57 -> 49 with nothing printed.  A skip that does
    # not announce itself is indistinguishable from coverage, which is the exact
    # defect class this base keeps re-finding.
    print(
        f"NOTE p1054 not found at {P1054!r}; "
        "8 cross-instrument controls are SKIPPED, not passed"
    )

if _p1054_ok:
    # p1054 collapses all three distinct payloads onto one verdict with no evidence.
    for nm, body in (("usc", USC), ("apache", APACHE), ("gpl", GPL)):
        old = mit_plus.classify(body)
        check(f"p1054 collapses {nm} to NOT-MIT-BODY", old["verdict"], "NOT-MIT-BODY")
        check(f"p1054 reports no evidence for {nm}", list(old["hits"]), [])
    # 🟢 And this instrument separates them: three payloads, three verdicts.
    verdicts = {rs.scan(b)["verdict"] for b in (USC, APACHE, GPL)}
    check("p257 separates the three payloads", len(verdicts), 3)
    # The vocabulary must never drift BELOW p1054's.
    truthy(
        "vocabulary is a superset of p1054's",
        set(mit_plus.RESTRICTION_TERMS).issubset(set(rs.RESTRICTION_TERMS)),
    )

# ── 7. An MIT body with a non-commercial rider (the PageLM shape, p255) ─────────
# Not published as permissive, and it reaches a verdict that names a human.
pagelm_shape = MIT.replace(
    "to deal",
    "for personal, educational, or non-commercial research purposes, to deal",
)
pl = rs.scan(pagelm_shape)
check("pagelm_shape.family", pl["family"], "MIT")
check("pagelm_shape.verdict", pl["verdict"], rs.VERDICT_FAMILY_PLUS)
check("pagelm_shape.usable", rs.is_usable_permissive(pagelm_shape), False)
truthy("pagelm_shape hits non-commercial", "non-commercial" in pl["hits"])

# ── 8. THE TITLE-ANCHOR REGRESSION, pinned ──────────────────────────────────────
# 🔴 This instrument's FIRST draft matched family anchors body-wide and graded the
# real GPL-3.0 fixture as AGPL, because GPL-3.0 §13 is titled "Use with the GNU
# Affero General Public License".  The next controls fail against that draft.
truthy(
    "the GPL fixture really does quote the Affero GPL (the trap is real)",
    "gnu affero general public license" in GPL.lower(),
)
check("GPL fixture is not graded AGPL", rs.family_of(GPL), "GPL")
# And the converse: a real AGPL payload still grades AGPL, by its own title line.
agpl = (
    "                    GNU AFFERO GENERAL PUBLIC LICENSE\n"
    "                       Version 3, 19 November 2007\n\n"
    "...incorporated under version 3 of the GNU General Public License...\n"
)
check("agpl grades by its title line", rs.family_of(agpl), "AGPL")
# A licence NAME appearing only deep in the body does not name the family.
deep = "Copyright (c) 2026 Someone\n\n" + ("filler\n" * 40) + "Apache License\n"
check("a deep mention is not a title", rs.family_of(deep), None)
# A BSD grant opening on a bare copyright line is still reached, via stage two.
bsd = (
    "Copyright (c) 2026 Example Institution\nAll rights reserved.\n\n"
    "Redistribution and use in source and binary forms, with or without\n"
    "modification, are permitted provided that the following conditions are met:\n"
)
check("bsd reached by operative clause", rs.family_of(bsd), "BSD")
# 🔴 ...and that payload carries `all rights reserved`, which is in the vocabulary.
# A real BSD grant says that phrase benignly, so the verdict must name a human
# rather than either publishing it as permissive or burying the hit.
bsd_scan = rs.scan(bsd)
truthy("bsd hit is reported", "all rights reserved" in bsd_scan["hits"])
check("bsd verdict names a human", bsd_scan["verdict"], rs.VERDICT_FAMILY_PLUS)
check("bsd is not auto-published as permissive", rs.is_usable_permissive(bsd), False)

# ── 9. Every verdict in ALL_VERDICTS is reachable, and the usable arm is closed ──
reached = {
    rs.scan(USC)["verdict"],
    rs.scan(APACHE)["verdict"],
    rs.scan(GPL)["verdict"],
    rs.scan(NOTFOUND)["verdict"],
    rs.scan(pagelm_shape)["verdict"],
}
check("all verdicts reachable", sorted(reached), sorted(rs.ALL_VERDICTS))
truthy("usable arm is closed", rs.USABLE_VERDICTS == frozenset({rs.VERDICT_PERMISSIVE}))
for v in rs.ALL_VERDICTS:
    if v != rs.VERDICT_PERMISSIVE:
        truthy(f"{v} is not usable", v not in rs.USABLE_VERDICTS)

# ── 10. Bytes are counted as UTF-8, not as characters (the ©️ in the USC header) ─
truthy("usc header is non-ascii", any(ord(c) > 127 for c in USC))
check("usc utf8 byte count", usc["bytes"], len(USC.encode("utf-8")))
truthy("usc bytes exceed char count", usc["bytes"] > len(USC))

print(f"{PASS}/{PASS + FAIL} controls pass")
sys.exit(1 if FAIL else 0)
