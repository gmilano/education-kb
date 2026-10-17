#!/usr/bin/env python3
"""p278 — the CONFLICT class, as a classifier instead of a hand-written table.

WHY THIS FILE EXISTS, and it is not the reason `p277` gave.

`p277` declared: *"this base has a grade for payload and a grade for metadata and no class at
all for CONFLICT. Declared for p278."* It ranked building that class FIRST, at zero searches.

🔴 **The class already existed.** `p121` (2026-10-11, `ACTION Q`) probed **249 addresses**,
fetched **161 manifests**, found **104 declaring a licence**, measured **10 contradictions** =
**9.6 %**, and published them in `repos/trending.md` with a four-value DIRECTION axis and an
operational rule: *"a manifest licence field is a HINT. The committed licence file is the
grant."* 🔴 **And the instance `p277` reported as a NEW defect class — `open-tutor-ai-CE`,
payload BSD-3-Clause vs `pyproject.toml` MIT — is row 8 of `p121`'s own table, carrying the
identical verdict ("both permissive, wrong name").**

🔵 **The gate for that error already exists too, and it was not run.**
`make claims TOKEN=conflict` returns `ALREADY CLAIMED … STOP` naming **26 cells in
repos/trending.md**, and exits **1**. Verified both arms this pass: exit 1 on a claimed token,
exit 0 + `NOT CLAIMED` on an absent one. **The Makefile documents this recipe as "THE GATE:
run before publishing any 'there is no X'". A pass that ranks a build FIRST without running it
spends the pass rebuilding what it owns.**

🟢 **So what `p278` owes is NOT the class. It is the half `p121` never built: `p121`'s census
was a ONE-OFF, by hand, at one moment.** This file is the classifier it lacked, so the verdict
is derived from the two families rather than typed per row -- the same `p228 -> p229` move the
Makefile's own header describes for the shelf gate.

THE AXIS, and why the asymmetry is the whole point.

`p121` measured that **7 of 10 contradictions declare something MORE PERMISSIVE than the
repository commits**, and stated the consequence: *every licence gate in a client's CI reads
the manifest.* `npm ls --json`, `pip-licenses`, most SBOM generators and most SCA scanners
report the declared field. So the two directions are NOT symmetric in cost:

  * manifest MORE permissive than payload -> the client's gate returns "pass" and the copyleft
    or commercial obligation ships undetected.  🔴 This is the one that bills.
  * manifest LESS permissive than payload -> the gate over-blocks.  🟡 `p121` called it "the
    harmless direction" and that is right: it costs a conversation, not a licence breach.

Hence a RANK, not an equality test.  Equality cannot express "dangerous in which direction".

    direction(manifest_family, payload_family) -> (verdict, severity, prose)

NEGATIVE ARM, stated because this base's instruments keep failing their first honest sweep:
a channel that was NOT READ is `SINGLE-CHANNEL`, never `AGREE`.  Silence is not agreement --
that is `p244`'s absence-states lesson, and reporting an unread channel as agreement would
manufacture exactly the false comfort this instrument exists to remove.
"""
import re
import sys

# 🔴 MEASURED ON THIS INSTRUMENT'S FIRST ADVERSARIAL SWEEP, not read in a book.
#
# The first cut of `tier_of()` normalised an unknown family onto any known family it merely
# STARTED WITH.  Three results, all wrong, two of them dangerous:
#
#     MITIGATED                         -> 0   a word beginning "MIT" became permissive
#     MIT-plus-clause                   -> 0   the added-restriction family p1054 exists for
#     Apache-2.0-with-Commons-Clause    -> 0   🔴 the Commons Clause REMOVES THE RIGHT TO SELL
#
# The third is the one that bills: a studio reading tier 0 ships a deliverable it may not
# sell.  🔵 And the fix was already written on this base, one library over -- `__decl` in
# `lib/license_family.sh` carries it as `P299`: *"A licence token is a word or it is noise"*,
# after "mit" matched as a substring of permit/submit/limit/commit/omit.  The same class, one
# layer up: here the token is a FAMILY NAME and the noise is an arbitrary suffix.
#
# So two guards, in this order:
#   1. A RESTRICTION MARKER outranks any base name.  "Apache-2.0 + Commons Clause" is not
#      Apache-2.0 for a studio's purposes; it is tier 5.  Checked FIRST, deliberately, so no
#      prefix rule can reach past it.
#   2. A prefix normalises ONLY when what follows it is a version or an SPDX scope suffix.
#      Anything else is UNPLACEABLE -- which surfaces as GREY and sends a human to the
#      payload, the one outcome that cannot silently over-permit.
RESTRICTION_MARKERS = re.compile(
    r"commons[-_ ]?clause|added[-_ ]restriction|non[-_ ]?commercial|no[-_ ]?resale"
    r"|[-_ ]nc([-_ ]|$)|[-_ ]nd([-_ ]|$)|no[-_ ]?deriv|proprietar|all[-_ ]rights[-_ ]reserved",
    re.I,
)
# A version (".0", "-3.0", "_2.1"), optionally followed by an SPDX scope or a named variant
# that does NOT change the tier.  Nothing else.
SUFFIX_OK = re.compile(r"^([-_.]?\d+(\.\d+)*)?(-only|-or-later|-Clear|-UNVERSIONED)?$", re.I)

# Permissiveness tiers.  LOWER = more permissive = fewer obligations on a studio deliverable.
# The tier, not the name, decides direction: MIT and Apache-2.0 differ in patent and notice
# terms, and a studio's ANSWER ("yes, you can ship this") is the same for both.
# 🟢 p278 — THIS TABLE IS BOUND TO `lib/license_family.sh`'s OUTPUT VOCABULARY.
#
# Why that binding is the point, and not housekeeping.  `P255` on this base is *"three
# instruments, three answers, one payload"*, and `lib/license_family.sh` exists because a
# pass rewrote a classifier from scratch and reintroduced a defect five instruments had
# already fixed.  This file does not classify payloads -- it consumes that classifier's
# answer -- so the failure mode available to it is NARROWER and quieter: a family the shared
# classifier CAN emit but this table does not list arrives `UNPLACEABLE`, and an unplaceable
# row is a row silently dropped from conflict detection.
#
# 🔴 Measured, not hypothesised: the first sweep returned `FAIRCODE` for `leemonade/leemons`
# -- the €100 000-past-1 000-users grant, tier 5, the single most expensive row in `p121`'s
# table -- and this table spelled it `FAIR-CODE`.  The most costly row was the one that went
# `UNPLACEABLE`.
#
# 🟢 So `test_direction.py` now asserts that EVERY token `license_family.sh` can emit is
# either placed here or listed as deliberately unplaceable.  Add a family there and the
# control here fails until it is placed.
TIERS = {
    # 0 — permissive.  A deliverable ships with attribution and nothing else.
    "MIT": 0, "MIT-0": 0, "ISC": 0, "BSD-2-Clause": 0, "BSD-3-Clause": 0, "BSD-4-Clause": 0,
    "BSD": 0, "0BSD": 0, "X11": 0, "Zlib": 0, "Unlicense": 0, "CC0-1.0": 0,
    "Apache-2.0": 0, "Apache-1.1": 0, "Apache-1.0": 0, "Apache-1.x-UNVERSIONED": 0,
    "PSF-2.0": 0,
    # ECL-2.0 is the Educational Community License: Apache-2.0 with a patent-scope amendment.
    # It is permissive, and it is the grant under BOTH Sakai and Opencast on this base's
    # shelves -- so misfiling it as copyleft would mis-grade two of the largest platforms here.
    "ECL-2.0": 0,
    # 1 — attribution-share, content licences.  Derivatives of the CONTENT inherit the terms;
    # code can usually still ship.  `p258` built this family for exactly this reason.
    # NOTE: only the NON-NC, NON-ND spellings sit here.  `RESTRICTION_MARKERS` pulls any
    # CC spelling carrying `NC` or `ND` up to tier 5 BEFORE this table is consulted.
    "CC-BY-4.0": 1, "CC-BY": 1, "CC-BY-SA-4.0": 1, "CC-BY-SA": 1,
    # 2 — weak / file-scope copyleft.  Linking is the question; distribution of the library's
    # own modifications is the obligation.
    "LGPL-2.1": 2, "LGPL-3.0": 2, "LGPL": 2,
    "MPL-1.0": 2, "MPL-1.1": 2, "MPL-2.0": 2, "MPL-UNVERSIONED": 2,
    "EPL": 2, "EPL-1.0": 2, "EPL-2.0": 2, "EPL-UNVERSIONED": 2,
    "EUPL": 2, "EUPL-1.1": 2, "EUPL-1.2": 2,
    # 3 — copyleft on distribution.
    "GPL-2.0": 3, "GPL-3.0": 3, "GPL": 3, "GPL-UNVERSIONED": 3,
    # 4 — network copyleft.  A HOSTED deliverable triggers it, which is most of what a studio
    # builds, so this tier is where an undetected overstatement costs the most.
    "AGPL-3.0": 4, "AGPL": 4,
    # 5 — non-commercial, source-available-but-billed, bespoke, and absent.  All share the
    # property that matters: a studio may NOT simply ship it.  `p276`'s P-N1 is the rule --
    # a refuted absence is not a permission -- and NONE sits here for the same reason.
    "CC-BY-NC-4.0": 5, "CC-BY-NC": 5, "BUSL-1.1": 5, "BUSL": 5, "PROPRIETARY": 5,
    "FAIRCODE": 5, "FAIR-CODE": 5, "ARR": 5, "NONE": 5,
    "NONCOMMERCIAL-NOT-OSI": 5, "PolyForm": 5, "Elastic": 5, "SUL": 5,
}

# 🔵 DELIBERATELY UNPLACEABLE — these are answers, not gaps.
#
# Each of these is a token `license_family.sh` emits when it has read a payload and CANNOT
# decide the question this instrument asks.  Giving them a tier would convert "unknown" into
# a permission or a prohibition, and both are inventions.  `UNPLACEABLE` routes the row to a
# human, which is the only correct destination for a grant nobody has classified.
#
# 🔴 `UNCLASSIFIED` in particular was tier 5 in this file's first cut.  That reads as
# "proprietary", and it is not: it means the classifier could not identify the TEXT.  An
# absent grant (`NONE`) is a MEASUREMENT and stays at tier 5; unreadable text is not.
UNPLACEABLE_BY_DESIGN = {
    "UNCLASSIFIED",            # the classifier read a payload and could not name it
    "CC-UNSPECIFIED",          # a CC licence whose NC/ND/SA arms are unknown -- the whole question
    "MULTI-GRANT-FRAMEWORK",   # more than one grant in one payload; tiering it hides the choice
}

# The channels this base reads# The channels this base reads, and what each one licenses you to conclude (`p259`).
UNREAD = {"", "-", None, "UNREAD", "NOT-READ", "404", "ABSENT-AT-ADDRESS"}

PROSE = {
    0: "permissive", 1: "attribution-share", 2: "weak copyleft", 3: "copyleft",
    4: "network copyleft", 5: "non-commercial / proprietary / absent",
}


def tier_of(family):
    """Tier for a family name, or None when this instrument cannot place it.

    Returning None rather than guessing a tier is deliberate: an UNPLACEABLE family must
    surface as `UNPLACEABLE` so a human reads the payload, never as a silent tier-0 pass.
    """
    if family is None:
        return None
    f = family.strip()
    if f in UNPLACEABLE_BY_DESIGN:
        return None
    if f in TIERS:
        return TIERS[f]
    # GUARD 1 — a restriction marker outranks any base name.  Checked before the prefix rule
    # so that "Apache-2.0-with-Commons-Clause" can never reach the Apache-2.0 tier.
    if RESTRICTION_MARKERS.search(f):
        return 5
    # GUARD 2 — a suffixed spelling places on its base family ONLY when the suffix is a
    # version or an SPDX scope.  "GPL-3.0-or-later" normalises; "MITIGATED" does not.
    for known, tier in sorted(TIERS.items(), key=lambda kv: -len(kv[0])):
        if f.upper().startswith(known.upper()) and SUFFIX_OK.match(f[len(known):]):
            return tier
    return None


def direction(manifest_family, payload_family):
    """(verdict, severity, prose) for one row's two channels.

    severity: "RED" (bills), "YELLOW" (costs a conversation), "GREEN" (agree),
              "GREY" (not a conflict claim -- a channel is missing or unplaceable).
    """
    m_missing = (manifest_family or "").strip() in UNREAD
    p_missing = (payload_family or "").strip() in UNREAD

    # Both silent: this row has no channel at all.  Not a conflict, and not an agreement.
    if m_missing and p_missing:
        return ("NO-CHANNEL", "GREY", "neither channel read — this row carries no grade")
    # One silent.  THE NEGATIVE ARM: never AGREE.
    if m_missing:
        return ("SINGLE-CHANNEL-PAYLOAD", "GREY",
                "payload read, manifest NOT read — agreement is unestablished, not established")
    if p_missing:
        return ("SINGLE-CHANNEL-MANIFEST", "GREY",
                "manifest read, payload NOT read — this is the grade p121 calls a HINT")

    mf, pf = manifest_family.strip(), payload_family.strip()
    mt, pt = tier_of(mf), tier_of(pf)
    if mt is None or pt is None:
        which = "manifest" if mt is None else "payload"
        return ("UNPLACEABLE", "GREY",
                f"{which} family not placeable by this instrument — read the payload by hand")

    if mf == pf:
        return ("AGREE", "GREEN", f"both channels say {mf}")
    if mt == pt:
        # Same obligations, different name.  `p121`: "both permissive, wrong name".
        return ("SAME-TIER-WRONG-NAME", "YELLOW",
                f"{mf} vs {pf} — same tier ({PROSE[mt]}), so nothing a studio may do changes; "
                "the ATTRIBUTION obligation does")
    if mt < pt:
        # 🔴 The direction that bills.  The client's CI reads the manifest and passes.
        return ("MANIFEST-OVERSTATES", "RED",
                f"manifest declares {mf} ({PROSE[mt]}) over a committed {pf} ({PROSE[pt]}) — "
                "a manifest-reading gate returns PASS and the obligation ships undetected")
    return ("MANIFEST-UNDERSTATES", "YELLOW",
            f"manifest declares {mf} ({PROSE[mt]}) over a committed {pf} ({PROSE[pt]}) — "
            "p121's harmless direction: over-blocks, does not under-report")


def main():
    if len(sys.argv) != 3:
        sys.stderr.write("usage: direction.py <manifest_family> <payload_family>\n")
        return 2
    v, s, prose = direction(sys.argv[1], sys.argv[2])
    print(f"{v}\t{s}\t{prose}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
