#!/usr/bin/env python3
"""Controls for `pass258-content-licence-family`.

Every fixture is a payload READ FIRST-HAND at `p258`, not a hand-typed excerpt:
the seven canonical Creative Commons texts from `spdx/license-list-data`, the real
Carpentries pointer from `datacarpentry/r-socialsci`, the real `CC-BY-4.0` payload
from `microsoft/AI-System`, and an `MIT` payload as the negative control.

🔴 Run from this directory (`cd compose/code/pass258-content-licence-family`): the
suite imports its subject, and `python3 -I` strips the script's own directory from
`sys.path`.  That is `p229`'s finding and the reason every Makefile recipe `cd`s.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import content_licence as cl  # noqa: E402

FIX = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fixtures-p258")

FAILURES = []
CHECKS = 0


def check(label, got, want):
    global CHECKS
    CHECKS += 1
    if got != want:
        FAILURES.append(f"{label}: got {got!r}, want {want!r}")


def payload(name):
    with open(os.path.join(FIX, name), encoding="utf-8", errors="replace") as fh:
        return fh.read()


# ── 1. The seven canonical payloads: family and verdict, read first-hand ───────────
CANON = [
    ("CC0-1.0.txt",        "CC0-1.0",         cl.VERDICT_PERMISSIVE),
    ("CC-BY-4.0.txt",      "CC-BY-4.0",       cl.VERDICT_PERMISSIVE),
    ("CC-BY-SA-4.0.txt",   "CC-BY-SA-4.0",    cl.VERDICT_COPYLEFT),
    ("CC-BY-ND-4.0.txt",   "CC-BY-ND-4.0",    cl.VERDICT_RESTRICTED_ND),
    ("CC-BY-NC-4.0.txt",   "CC-BY-NC-4.0",    cl.VERDICT_RESTRICTED_NC),
    ("CC-BY-NC-SA-4.0.txt", "CC-BY-NC-SA-4.0", cl.VERDICT_RESTRICTED_NC),
    ("CC-BY-NC-ND-4.0.txt", "CC-BY-NC-ND-4.0", cl.VERDICT_RESTRICTED_NC),
]

MISSING = []
for name, family, verdict in CANON:
    if not os.path.exists(os.path.join(FIX, name)):
        # 🔴 p257: a skip that does not announce itself is indistinguishable from
        # coverage.  An absent fixture is a FAILURE here, not a silent pass — the
        # control count must not be able to drift downward quietly.
        MISSING.append(name)
        continue
    body = payload(name)
    check(f"family({name})", cl.family_of_content(body), family)
    check(f"verdict({name})", cl.content_verdict(body), verdict)
    check(f"is_content_licence({name})", cl.is_content_licence(body), True)
    check(f"is_grant({name})", cl.is_grant(body), True)

# ── 2. `CC0`'s identifier is on LINE 2 — a line-1-only anchor misses it ───────────
cc0 = payload("CC0-1.0.txt")
check("CC0 line 1 is the generic heading",
      cc0.splitlines()[0].strip().lower(), "creative commons legal code")
check("CC0 identified despite line-2 title", cl.family_of_content(cc0), "CC0-1.0")
check("CC0 is the most permissive grant there is",
      cl.is_usable_in_deliverable(cc0), True)

# ── 3. The POINTER: names a CC licence, does not make one (`P1065`) ───────────────
ptr = payload("carpentries-pointer.md")
# 🔴 The pointer does NOT identify itself in the title window — it opens with YAML
# frontmatter and does not name Creative Commons until line 8.  That is why the
# pointer branch needs `names_content_licence`, and this pair of controls pins it.
check("pointer does not identify as a CC text in its title window",
      cl.is_content_licence(ptr), False)
check("pointer NAMES a CC licence body-wide", cl.names_content_licence(ptr), True)
check("pointer is NOT a grant", cl.is_grant(ptr), False)
check("pointer family is None", cl.family_of_content(ptr), None)
check("pointer verdict", cl.content_verdict(ptr), cl.VERDICT_POINTER)
check("a pointer is not usable on its own evidence",
      cl.is_usable_in_deliverable(ptr), False)

# ── 4. A real shelf payload: `microsoft/AI-System` is CC-BY-4.0, not UNCLASSIFIED ──
ms = payload("microsoft-AI-System-LICENSE.txt")
check("microsoft/AI-System family", cl.family_of_content(ms), "CC-BY-4.0")
check("microsoft/AI-System verdict", cl.content_verdict(ms), cl.VERDICT_PERMISSIVE)

# ── 5. Negative control: an MIT payload is not a content licence ──────────────────
mit = payload("mit-control.txt")
check("MIT is not a content licence", cl.is_content_licence(mit), False)
check("MIT verdict", cl.content_verdict(mit), cl.VERDICT_NOT_CC)
check("MIT family is None", cl.family_of_content(mit), None)
check("MIT is not usable AS A CONTENT LICENCE (ask p257 instead)",
      cl.is_usable_in_deliverable(mit), False)

# ── 6. `SA` and `ND` are mutually exclusive by construction ───────────────────────
for name in ("CC-BY-ND-4.0.txt", "CC-BY-NC-ND-4.0.txt"):
    if os.path.exists(os.path.join(FIX, name)):
        ident = cl.family_of_content(payload(name))
        check(f"no SA in {ident}", "SA" in ident.split("-"), False)

# ── 7. Strictest axis wins, so a reader cannot ship on the weakest verdict ────────
ncsa = payload("CC-BY-NC-SA-4.0.txt")
check("NC+SA grades NC, not SA", cl.content_verdict(ncsa), cl.VERDICT_RESTRICTED_NC)
check("NC+SA is unusable", cl.is_usable_in_deliverable(ncsa), False)
ncnd = payload("CC-BY-NC-ND-4.0.txt")
check("NC+ND grades NC, not ND", cl.content_verdict(ncnd), cl.VERDICT_RESTRICTED_NC)

# ── 8. The closed set fails CLOSED: an unknown verdict is never usable ────────────
check("UNUSABLE_VERDICTS is a subset of ALL_VERDICTS",
      cl.UNUSABLE_VERDICTS <= cl.ALL_VERDICTS, True)
check("a verdict outside the known set is not usable",
      cl.VERDICT_POINTER in (cl.VERDICT_PERMISSIVE, cl.VERDICT_COPYLEFT), False)

# 🔴 Added after this suite's own mutation run, which is the only reason it is here.
# Deleting `VERDICT_RESTRICTED_NC` from `UNUSABLE_VERDICTS` produced `72` controls and
# `0` failures: `is_usable_in_deliverable` ends with a closed positive list, so the
# mutant stayed behaviourally identical and the set LOOKED load-bearing while being
# decorative in that direction.  🔵 Same shape as this base's recurring defect — two
# guards, one carrying the weight and the other assumed to.  The set IS load-bearing
# for the published census total, so these controls pin BOTH uses.
check("NC is named in the unusable set, not merely rejected by the positive list",
      cl.VERDICT_RESTRICTED_NC in cl.UNUSABLE_VERDICTS, True)
check("ND is named in the unusable set",
      cl.VERDICT_RESTRICTED_ND in cl.UNUSABLE_VERDICTS, True)
check("the unusable set holds EXACTLY the two restriction verdicts",
      cl.UNUSABLE_VERDICTS,
      frozenset({cl.VERDICT_RESTRICTED_NC, cl.VERDICT_RESTRICTED_ND}))

# ── 9. `p251-prefix-collision` on IDENTIFIERS: the long token must not truncate ───
for token, want in [
    ("CC-BY-NC-SA-4.0", cl.VERDICT_RESTRICTED_NC),
    ("CC-BY-NC-ND-3.0", cl.VERDICT_RESTRICTED_NC),
    ("CC-BY-SA-4.0", cl.VERDICT_COPYLEFT),
    ("CC-BY-ND-4.0", cl.VERDICT_RESTRICTED_ND),
    ("CC-BY-4.0", cl.VERDICT_PERMISSIVE),
    ("CC0-1.0", cl.VERDICT_PERMISSIVE),
]:
    found = cl.SHELF_TOKEN.findall(token)
    check(f"SHELF_TOKEN matches {token} whole", found[:1], [token])
    check(f"classify_token({token})", cl.classify_token(token), want)

# ── 10. The REGRESSION this instrument closes, asserted against p257 itself ───────
# 🔵 Not a duplicate of p257's own suite: this asserts the SHAPE of the hole, so that
# if a later pass teaches `pass257-restriction-scan` a CC family, this control fails
# and whoever did it is told to re-scope this instrument instead of leaving two.
P257 = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                    "pass257-restriction-scan")
if os.path.isdir(P257):
    sys.path.insert(0, P257)
    try:
        import restriction_scan as rs

        check("p257 has no CC family (that is why p258 exists)",
              any("cc" in f.lower() for f in rs.PERMISSIVE_FAMILIES | rs.COPYLEFT_FAMILIES),
              False)
        check("p257 has no derivative-restriction term",
              [t for t in rs.RESTRICTION_TERMS if "deriv" in t], [])
        # The measured identity: CC0 (most permissive) and CC-BY-ND (no derivatives)
        # are indistinguishable to the live gate.
        check("p257 grades CC0 unclassified",
              rs.scan(cc0)["verdict"], rs.VERDICT_UNCLASSIFIED)
        check("p257 grades CC-BY-ND unclassified",
              rs.scan(payload("CC-BY-ND-4.0.txt"))["verdict"], rs.VERDICT_UNCLASSIFIED)
        check("p257 DOES catch the NC half (credit where due)",
              rs.scan(ncsa)["verdict"], rs.VERDICT_RESTRICTED)
        check("p258 and p257 disagree on ND, and p258 is the stricter one",
              cl.is_usable_in_deliverable(payload("CC-BY-ND-4.0.txt")), False)
    except ImportError as exc:  # pragma: no cover
        FAILURES.append(f"p257 cross-check UNRUNNABLE: {exc}")
else:  # pragma: no cover
    FAILURES.append(f"p257 cross-check SKIPPED, not passed: {P257} absent")

# ── 11. `coverage()` must report a real population, and announce absences ─────────
KB = os.path.dirname(os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__)))))
total, counts, missing_shelves = cl.coverage(KB)
check("coverage() announces no missing shelf on a full checkout", missing_shelves, [])
check("coverage() finds a non-trivial content-licence population", total > 500, True)
check("coverage() finds a non-commercial population",
      counts.get(cl.VERDICT_RESTRICTED_NC, 0) > 100, True)
check("coverage() on an empty root reports every shelf as ABSENT",
      len(cl.coverage("/nonexistent-root-p258")[2]), len(cl.SHELVES))
# The published census total is computed OVER `UNUSABLE_VERDICTS`, so the set is
# load-bearing here too and a mutation of it moves this number.
check("the census's unusable total is the sum over the unusable set",
      sum(counts.get(v, 0) for v in cl.UNUSABLE_VERDICTS),
      counts.get(cl.VERDICT_RESTRICTED_NC, 0) + counts.get(cl.VERDICT_RESTRICTED_ND, 0))

if MISSING:
    FAILURES.append(f"{len(MISSING)} fixture(s) ABSENT, SKIPPED not passed: "
                    f"{', '.join(MISSING)}")

print(f"pass258-content-licence-family: {CHECKS} controls, "
      f"{len(FAILURES)} failure(s)")
for failure in FAILURES:
    print(f"  FAIL {failure}")
sys.exit(1 if FAILURES else 0)
