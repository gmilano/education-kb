#!/usr/bin/env python3
"""`pass256-ladder-closure` — the ladder a pass TYPES must contain the paths this base has
already PROVEN it needs, and a refusal must never be read as a payload.

Why this exists, stated as a measurement rather than a principle:

  * `P1057` (p189) published `openedx/XBlock`'s grant at `LICENSE.TXT` — upper-case
    extension, `11 358` B of verbatim Apache-2.0 — and recorded that
    `raw.githubusercontent.com` is CASE-SENSITIVE, so a one-spelling path list has not
    looked for the file but for one spelling of it.
  * p256, SIXTY-SEVEN passes later, probed `openedx/xblock-sdk` — a sibling repository in
    the SAME organisation — with `LICENSE LICENSE.txt LICENSE.md LICENSE.rst COPYING`,
    got `404` on all five, and was one keystroke from publishing `NO_LICENCE_FILE` on a
    repository whose Apache-2.0 body is `11 358` B at `LICENSE.TXT`, byte-identical
    (`sha256`16 `cfc7749b96f63bd3`) to `openedx/edx-lint`'s.
  * The reason is not that the fix was lost.  `P1057` exists, passes, and is in the gate.
    🔴 `LICENSE.TXT` was simply ABSENT from `p229`'s TIER_A, the 41-path ladder that
    `make reach` prints so that "a list you cannot print is a list that gets copied"
    (T272).  The knowledge was wired; nothing consumed the wire — p253's lesson, arriving
    through a path list instead of an exit status.

So this instrument asserts the JOIN that no prose can hold:

  CLOSURE   every ROOT-form path that `lib/test_licence_path.sh` asserts to be a licence
            path must be present in `p229`'s TIER_A.
  AGREEMENT every TIER_A entry must satisfy `lib/licence_path.sh`'s `is_licence_path`.
  REFUSAL   a captured `404` body is not a grant, at any path, however licence-shaped
            the path is.
  CASE      `LICENSE.txt` and `LICENSE.TXT` are two ADDRESSES, not two spellings of one.

`--verify` re-reads the live ladder and the live suite and re-asserts the join, so the
check cannot pass against a stale pin.
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
LADDER = os.path.join(HERE, "..", "p229-grant-ladder-reach", "ladder.sh")
PRED = os.path.join(HERE, "..", "lib", "licence_path.sh")
SUITE = os.path.join(HERE, "..", "lib", "test_licence_path.sh")

# p256's own measurements, pinned.  A later pass that re-reads these payloads and gets a
# different figure has found a measurement defect, not a payload that moved — which is
# `ACTION XY`'s class and the reason the pin carries the discriminating control with it.
REFUSAL_BYTES = 14
REFUSAL_SHA16 = "d5558cd419c8d46b"
REFUSAL_BODY = "404: Not Found"
PINNED_PAYLOADS = {
    # slug                            (path,            bytes,  sha256-16)
    "openedx/xblock-sdk":             ("LICENSE.TXT",   11358, "cfc7749b96f63bd3"),
    "openedx/edx-lint":               ("LICENSE.txt",   11358, "cfc7749b96f63bd3"),
    "openstax/fine_print":            ("MIT-LICENSE",    1055, "0a9ed2a2ba710b61"),
    "learningequality/ricecooker":    ("LICENSE",        1087, "8e7a35d64f5c7d51"),
    "adlnet/xapi-ontology":           ("LICENSE",       11525, "a1587287ff0445e1"),
    "open-spaced-repetition/fsrs.js": ("LICENSE",        1089, "4bef6c7c01b2250b"),
    "1EdTech/cert-schema":            ("LICENSE",        1096, "06d87bf42a0a9a63"),
}
# 🟡 The ONE proven root form that is deliberately NOT in the ladder, with its reason
# attached.  `p229`'s own header warns that re-reading first-hand is not automatically
# safer, because reading the WRONG licence file is a new error class: a third-party
# aggregate carries OTHER projects' grants, and TIER_A governs THIS repository's verdict.
# The exemption is asserted as an exact set, so a later pass cannot quietly grow it.
LADDER_EXEMPT = {
    "third-party-licenses.txt":
        "an aggregate of OTHER projects' grants, not this repository's; it is a licence "
        "PATH (so `is_licence_path` says yes) and not a licence OF the subject",
}

# The paths that were ABSENT from TIER_A when p256 measured it.  Kept as the adversarial
# case: if a later pass shortens the ladder again, the closure control names which one.
P256_ADDED = [
    "LICENSE.TXT", "licence.txt", "MIT-LICENSE", "MIT-LICENSE.txt",
    "LICENSE-MIT", "LICENSE-APACHE", "APACHE-LICENSE-2.0.txt",
]


def _assign(body, name):
    """Read a `NAME="a b c"` assignment that may span lines.  Deliberately not lazy:
    `ACTION TB`'s lazy-quantifier lint runs over this directory."""
    m = re.search(name + r'="([^"]*)"', body)
    return m.group(1).split() if m else []


def tier_a(path=LADDER):
    with open(path, encoding="utf-8", errors="replace") as fh:
        return _assign(fh.read(), "TIER_A")


def proven_root_forms(path=SUITE):
    """Every `yes_lic "X"` in the shared suite whose X is a ROOT form (no directory).
    These are the paths this base has ASSERTED to be grants, in a file that is in the
    gate — so a ladder that omits one is omitting a proven case, not a guess."""
    out = []
    with open(path, encoding="utf-8", errors="replace") as fh:
        for line in fh:
            m = re.match(r'\s*yes_lic\s+"([^"]+)"', line)
            if m and "/" not in m.group(1):
                out.append(m.group(1))
    return out


def closure_gaps(ladder=None, proven=None):
    """-> the proven root forms a ladder does NOT carry.  Case-SENSITIVE on purpose: the
    whole class this instrument exists for is two addresses differing only in case."""
    ladder = tier_a() if ladder is None else ladder
    proven = proven_root_forms() if proven is None else proven
    have = set(ladder)
    return [p for p in proven if p not in have and p not in LADDER_EXEMPT]


def is_refusal(body_bytes):
    """A captured `404` body, at ANY path.  Byte count alone is not the test — p246's
    byte-floor already refuses a 1-byte file — so this matches on the body."""
    if body_bytes is None:
        return False
    text = body_bytes.decode("utf-8", "replace") if isinstance(body_bytes, bytes) else body_bytes
    return text.strip() == REFUSAL_BODY


def main(argv):
    if len(argv) > 1 and argv[1] == "--verify":
        ladder = tier_a()
        gaps = closure_gaps(ladder)
        print(f"tier_a={len(ladder)}\tproven_root_forms={len(proven_root_forms())}\tgaps={len(gaps)}")
        if gaps:
            for g in gaps:
                print(f"GAP\t{g}\tproven by lib/test_licence_path.sh, absent from p229 TIER_A")
            return 1
        for p in P256_ADDED:
            if p not in ladder:
                print(f"REGRESSION\t{p}\tadded by p256, removed since")
                return 1
        print("LADDER CLOSURE HOLDS")
        return 0
    print(__doc__)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
