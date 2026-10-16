#!/usr/bin/env python3
"""`p245-apache-canonical` — the TEXT axis of an Apache-2.0 grant, which is a different
question from the FAMILY axis every instrument on these shelves already answers.

Why this exists (pass 245 del 2026-10-16)
-----------------------------------------
`lib/license_family.sh::family_of` answers `Apache-2.0` for a payload whose title block is
Apache's. That is the right answer to the question it asks, and this pass measured a case
where it is not the whole truth:

    Crosstalk-Solutions/project-nomad  (40 351 stars, the offline education server)
    rohitg00/k8sgames                  (1 407 stars, the Kubernetes skills lab)

Both ship a `LICENSE` that is **byte-identical to each other** and **not** byte-identical to
`https://www.apache.org/licenses/LICENSE-2.0.txt`. Three word-level deviations, measured:

| where | canonical | these payloads |
|---|---|---|
| §1, the `Contribution` definition | `submitted to Licensor` | `submitted to **the** Licensor` |
| §1, the `Contributor` definition | `received by Licensor` | `received by **the** Licensor` |
| §4(d), the NOTICE condition | `excluding **those** notices` | `excluding **any** notices` |

🔴 **The §4(d) marker is why this instrument anchors on left context and not on the phrase.**
The sentence *"excluding those notices that do not pertain"* appears **twice** in canonical
Apache — once in §4(c), for notices in the Source form, and once in §4(d), for the NOTICE
file. These payloads altered **only the §4(d) instance**, so a naive presence/absence test
finds the canonical phrase still present (from §4(c)) and reports the payload clean. This
pass wrote that bug and its own controls caught it; the anchors below therefore carry the
disambiguating left context, and `test_apache_canonical.py` asserts the §4(c) instance stays
untouched.

🔴 The §4(d) one sits inside an **operative redistribution condition** — the sentence that
says what a Derivative Work must carry. 🟢 The permission grant, the conditions and the
limitations are otherwise intact, so the *family* is genuinely Apache-2.0 and `family_of` is
not wrong. What is wrong is to report `Apache-2.0` and stop, because:

1. A licence scanner that matches by exact text or payload hash (most SPDX tooling, and every
   OSS-review gate built on it) returns `Apache-2.0 AND-modified` or `UNKNOWN`, not a clean
   pass. Due diligence then stalls on a 40k-star dependency at the worst moment.
2. The deviations are **paraphrase-shaped** — an inserted article, `those`→`any` — which is
   what reproduction FROM RECALL looks like, not what copying a file looks like. Two
   unrelated holders (a US LLC and an individual) shipping the same paraphrase means a
   non-canonical Apache text is in circulation, and these shelves will meet it again.

🔵 So the verdict here is deliberately NOT a licence verdict. It answers one question:
**is this payload the canonical text?** A `NON-CANONICAL` payload is still Apache-2.0.

What is NOT a deviation (the controls that keep this instrument honest)
----------------------------------------------------------------------
🟢 **Dropping the `APPENDIX`** and replacing it with a real copyright line is the practice
Apache's own appendix *instructs*. `robocode-dev/tank-royale` does exactly that and is
canonical in every operative line — it is a fixture here precisely so a later pass cannot
"fix" this instrument into flagging it. 🟢 Trailing whitespace and a leading blank line are
not deviations either: this pass measured a one-byte leading-newline difference on payloads
that are otherwise exact.

Usage
-----
    python3 -I apache_canonical.py <payload-file>     # prints the verdict, exits 0
    from apache_canonical import verdict              # verdict(text) -> str

Verdicts: `NOT-APACHE` · `CANONICAL` · `NON-CANONICAL:<marker>[,<marker>...]`
"""
import re
import sys

#: The title anchor. Apache's terms carry this; Apache's *NOTICE* boilerplate does not, which
#: is the `P971` class (a LICENSE file holding the header notice rather than the terms).
_TITLE = re.compile(r"Apache License\s*\n?\s*Version 2\.0", re.IGNORECASE)

#: The operative anchors, as (marker, canonical-fragment, deviation-fragment) triples.
#: Both fragments are matched on WHITESPACE-COLLAPSED text, because the canonical file hard-wraps
#: these sentences and a reflowed payload is not thereby a different licence.
#:
#: 🔴 Each fragment carries enough LEFT CONTEXT to be unique in the canonical text. The
#: `any-notices` one must: its bare phrase occurs twice (§4(c) and §4(d)) and only the §4(d)
#: instance is altered by the variant this instrument was built for.
_ANCHORS = (
    (
        "the-Licensor",
        "submitted to Licensor for inclusion in the Work",
        "submitted to the Licensor for inclusion in the Work",
    ),
    (
        "received-by-the-Licensor",
        "has been received by Licensor and subsequently",
        "has been received by the Licensor and subsequently",
    ),
    (
        "any-notices",
        "within such NOTICE file, excluding those notices",
        "within such NOTICE file, excluding any notices",
    ),
)


def _collapse(text):
    """Whitespace-collapse so hard-wrapping is not mistaken for a textual change."""
    return re.sub(r"\s+", " ", text)


def is_apache(text):
    """True when the payload carries Apache's TERMS (not merely the word 'Apache')."""
    if not text or not text.strip():
        return False
    if not _TITLE.search(text):
        return False
    # The grant sentence itself. A NOTICE-boilerplate payload names the licence and omits this.
    return "perpetual, worldwide, non-exclusive, no-charge, royalty-free" in _collapse(text)


def deviations(text):
    """The markers whose canonical fragment is ABSENT and whose deviation is PRESENT.

    A fragment that matches neither form is not reported: an unknown rewrite is a different
    finding, and this instrument does not claim to enumerate every way a text can differ.
    """
    flat = _collapse(text)
    out = []
    for marker, canonical, deviant in _ANCHORS:
        if canonical not in flat and deviant in flat:
            out.append(marker)
    return out


def verdict(text):
    if not is_apache(text):
        return "NOT-APACHE"
    devs = deviations(text)
    if devs:
        return "NON-CANONICAL:" + ",".join(devs)
    return "CANONICAL"


def main(argv):
    if len(argv) != 2:
        print(__doc__.strip().splitlines()[0], file=sys.stderr)
        print("usage: apache_canonical.py <payload-file>", file=sys.stderr)
        return 2
    with open(argv[1], "r", encoding="utf-8", errors="replace") as fh:
        print(verdict(fh.read()))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
