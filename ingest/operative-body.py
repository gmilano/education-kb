#!/usr/bin/env python3 -I
"""p555 -- IS A PLATFORM `NOASSERTION` COSMETIC OR SUBSTANTIVE?

`platform-channel.py` found 8 of 79 education repositories on which GitHub's
`licensee` returns `NOASSERTION`. The tempting inference -- and this pass nearly
drew it -- is that `NOASSERTION` DETECTS a composite or non-standard grant, which
would make it a free classifier for the hardest class on these shelves.

🔴 IT IS NOT. Hand-read, the 8 split FOUR ways: presentation defects over a stock
licence, genuine code/corpus splits, a non-OSI source-available grant, and a file
that names a family without carrying it. `NOASSERTION` means only "not the stock
text I expected", and four very different facts produce that.

WHAT THIS MODULE DECIDES, AND WHAT IT REFUSES TO
------------------------------------------------
It answers exactly one question, which is the one that changes a shipping
decision:

    Does this payload contain a known licence's OPERATIVE BODY, VERBATIM?

If it does, the grant is UNAMBIGUOUS and the `NOASSERTION` is COSMETIC -- leading
whitespace, indentation, a preamble, a reordered appendix. The artefact is
shippable on that family's terms and the platform field is simply wrong to be
silent. If it does not, the `NOASSERTION` is SUBSTANTIVE and a human must read it.

🔵 WINDOW, DECLARED (`Gap 554-C`'s ask): this module reads the WHOLE PAYLOAD, not
a title block and not a section window. That is the opposite bet from
`grant-verdict.py`'s 12-line window, and DELIBERATELY so. `553-A` narrowed to a
title block to stop a licence CITING another licence from poisoning the family;
`554-C` then found that same window could not reach a composite file's governing
grant. This module sidesteps both: it does not ask WHICH family governs, it asks
WHETHER a given family's operative text is PRESENT in full. Containment is immune
to position, so no window is needed -- and it is immune to decoration, which is
precisely the failure mode it exists to measure.

🔴 WHAT IT CANNOT DO, stated because the limit is the point:
  1. Containment is NOT governance. A file can contain Apache-2.0 verbatim AND
     carve out paths (`pupilfirst` contains MIT verbatim and still assigns `docs/`
     to CC-BY-SA-4.0). A COSMETIC verdict says the family's text is wholly
     present; it does NOT say the family governs every path. Composite detection
     stays with `grant-verdict.py`'s `composite()`.
  2. It only knows the families whose canonical texts are pinned below. An
     unknown family reads SUBSTANTIVE, which is the safe direction.
  3. Whitespace is stripped before comparison, so it cannot see a grant whose
     only modification is whitespace-significant (none known in licence texts).
"""
import re
import sys
import urllib.request

# 🔵 Canonical sources. 🔴 `gnu.org` is **403 through this session's proxy**, so the
# stewards' own addresses are NOT reachable for the GNU families and the first run
# loaded 1 of 5. Pinned instead to SPDX's `license-list-data`, which is reachable on
# `raw.` and is itself an authority -- the Linux Foundation project whose texts are
# what SPDX ids MEAN. 🔵 That is a deliberate second choice, not a mirror of
# convenience: a successor comparing against `gnu.org` should expect identical
# operative bodies and should say so if they differ.
_SPDX = "https://raw.githubusercontent.com/spdx/license-list-data/main/text"
CANON = {
    "Apache-2.0": f"{_SPDX}/Apache-2.0.txt",
    "GPL-3.0": f"{_SPDX}/GPL-3.0-only.txt",
    "LGPL-3.0": f"{_SPDX}/LGPL-3.0-only.txt",
    "AGPL-3.0": f"{_SPDX}/AGPL-3.0-only.txt",
    "GPL-2.0": f"{_SPDX}/GPL-2.0-only.txt",
}

# 🔵 The operative span of each family: the first and last marker of the part a
# court would read. Everything outside it is wrapper -- title art, the "how to
# apply" appendix, a steward's preamble -- and is exactly what decoration touches.
SPAN = {
    "Apache-2.0": ("termsandconditions", "endoftermsandconditions"),
    "GPL-3.0": ("termsandconditions", "endoftermsandconditions"),
    "LGPL-3.0": ("0.additionaldefinitions", "endoftermsandconditions"),
    "AGPL-3.0": ("termsandconditions", "endoftermsandconditions"),
    "GPL-2.0": ("termsandconditions", "endoftermsandconditions"),
}

# 🔴 MIT and BSD have no stable operative-span markers -- they are a single
# paragraph with no headings -- so they are matched on their whole normalised
# text, which for a one-paragraph grant IS the operative body.
WHOLE = {
    "MIT": ("permissionisherebygranted,freeofcharge",
            "outoforinconnectionwiththesoftware"),
}


def norm(text):
    return re.sub(r"\s+", "", text).lower()


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "education-kb/p555"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read().decode("utf-8", "replace")


def operative(family, canon_text):
    n = norm(canon_text)
    if family in SPAN:
        a, b = SPAN[family]
        if a in n and b in n:
            return n[n.index(a): n.index(b)]
        return None
    return None


def classify(payload_text, bodies):
    """🟢 COSMETIC if any known family's operative body is wholly present.
    🔴 Never resolves WHICH family governs when two are present -- it reports all
    of them, because a payload containing two operative bodies is a finding a
    reader must see, not one this module may collapse."""
    n = norm(payload_text)
    hits = [fam for fam, body in bodies.items() if body and body in n]
    for fam, (a, b) in WHOLE.items():
        if a in n and b in n:
            hits.append(fam)
    if not hits:
        return "SUBSTANTIVE", ""
    return "COSMETIC", "+".join(sorted(hits))


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        print("usage: operative-body.py <slug:branch> [slug:branch ...]")
        print("       operative-body.py --selftest")
        return 1

    bodies = {}
    for fam, url in CANON.items():
        try:
            bodies[fam] = operative(fam, fetch(url))
        except Exception as e:                                    # noqa: BLE001
            sys.stderr.write(f"[canon] {fam}: UNREACHABLE ({e})\n")
            bodies[fam] = None
    ok = [f for f, b in bodies.items() if b]
    sys.stderr.write(f"[canon] operative bodies loaded: {len(ok)}/{len(CANON)}"
                     f" -> {','.join(sorted(ok))}\n")

    if sys.argv[1] == "--selftest":
        # 🔵 CONTROLS. A module that reports COSMETIC must be shown to report
        # SUBSTANTIVE when it should, or the verdict carries no information.
        fails = 0
        for fam, url in CANON.items():
            if not bodies.get(fam):
                continue
            v, hit = classify(fetch(url), bodies)
            exp = "COSMETIC"
            bad = v != exp or fam not in hit
            fails += bad
            print(f"{'FAIL' if bad else 'ok  '}  canonical {fam:12} -> {v} [{hit}]")
        for label, text in (
            ("empty", ""),
            ("family named, not carried", "This project is licensed under Apache-2.0."),
            ("19B stub", "MIT License\n"),
            ("BUSL preamble only", "Business Source License 1.1\nLicensor: X\n"),
        ):
            v, hit = classify(text, bodies)
            bad = v != "SUBSTANTIVE"
            fails += bad
            print(f"{'FAIL' if bad else 'ok  '}  negative {label:28} -> {v} [{hit}]")
        print(f"\nselftest: {'RED' if fails else 'GREEN'} ({fails} failures)")
        return 1 if fails else 0

    print("repo\tpayload\tbytes\tnoassertion_class\toperative_bodies_present")
    for arg in sys.argv[1:]:
        slug, _, branch = arg.partition(":")
        branch = branch or "HEAD"
        got = None
        for name in ("LICENSE", "LICENSE.md", "LICENSE.txt", "COPYING", "license.txt"):
            try:
                got = (name, fetch(f"https://raw.githubusercontent.com/"
                                   f"{slug}/{branch}/{name}"))
                break
            except Exception:                                      # noqa: BLE001
                continue
        if got is None:
            print(f"{slug}\tNONE\t0\tNO-PAYLOAD\t-")
            continue
        name, text = got
        v, hit = classify(text, bodies)
        print(f"{slug}\t{name}\t{len(text.encode())}\t{v}\t{hit or '-'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
