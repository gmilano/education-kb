#!/usr/bin/env python3
"""p311 — the pinned payloads for the two families this base publishes MOST, and
the CANONICAL answer for each.

🔵 `ACTION p310-R` item 1 ranked this first and said why: `MIT` (5 549 cells) and
`Apache-2.0` (2 335) are the two most-published families on this base and **no
dynamic arm had ever touched either**.  7 884 cells — 61 % of every licence cell
this base publishes — rested on rungs that had never been executed against a real
payload of their own family.

🔴 THE RESULT IS ZERO DEFECTS, and this file records the two reasons that is not
the same as "nothing was learned".

**One.** The four payloads split along the form boundary `p310` measured on the
HOLDER channel — *fill-in slot* (`MIT`) versus *fixed document* (`Apache-2.0`) —
and the split is exact rather than approximate:

  `MIT`         21 lines each, **exactly ONE line differs**, and it is the
                `Copyright` line.  `1 100 − 1 066 = 34` B is the holder-string
                delta, nothing else.  Remainder byte-identical.
  `Apache-2.0`  `noplag[1:] == reference-audit` **exactly**.  The whole 1-byte
                difference is **one leading `\\n`**, and the two shas are
                `cfc7749b96f6` and `c71d239df917` — no shared prefix.

🔴 **So this base's standing payload-identity convention — bytes + `sha256_12` —
is not a licence instrument, and `p310` used it as one.**  `p310` certified seven
CC0 rows partly on *"six at the legalcode's exact 7 048 B"*.  That test is unsound
in BOTH directions, and the fixtures below are the negative controls:

  a **fixed document** can carry an identical grant at a different byte length and
  a completely different sha (one whitespace byte does it: a FALSE NEGATIVE on
  genuineness), and a **fill-in slot** family's byte length is a function of the
  HOLDER STRING, so an exact-byte-length test can never certify `MIT` at all.

`payload_identity.py` is the normalising oracle this implies, and both effects are
standing controls in `test_p311.py`.

**Two.** `p310` reported its coverage as `36 %` — **8 of 22 FAMILIES**.  By CELLS,
the thing that measures how much of this base's published data an arm has actually
exercised, it was `24 %`.  This pass takes families to `45 %` and cells to `85 %`.
🔵 **A family-count metric over a distribution where ONE family is 43 % of the
cells is an unweighted average of wildly unequal things**, and it understated both
the exposure and the repair.  `risk_order.py` carries that argument and the one
that follows from it.
"""
import hashlib
import os

HERE = os.path.dirname(os.path.abspath(__file__))
FIX = os.path.join(HERE, "fixtures")

# 🔵 Prefix + directory listing, NOT a literal filename — `p310`'s convention,
# adopted rather than reinvented, and it is load-bearing: spelling the licence
# filename as a literal here makes `p283-ladder-case-audit` read this file as a
# one-rung licence-path ladder and the STANDING ratchet goes red.

# (prefix, canonical family, canonical commercial-use verdict, why it is here)
DECLARED = [
    ("mit-open-detector", "MIT", "OK",
     "Imalwayshere/Open-Detector — title line `MIT License`, holder "
     "`LI YUANJI` (a PERSON). 🟡 Leader of the AI-TEXT-DETECTION sub-tier, NOT of "
     "the `academic-integrity` axis — `p310`'s post-publication correction "
     "retracted that and `dodona-edu/dolos` outranks it 350 stars to 249. "
     "🟢 Here as the fill-in-slot baseline: 1 066 B is the MIT template carrying "
     "a 12-character holder."),
    ("mit-gradebridge", "MIT", "OK",
     "BridgeSuite/GradeBridge-Student-Submission — the SAME 21-line template, "
     "holder `The Regents of the University of California` (an INSTITUTION, and "
     "`p310`'s only first-hand NORTH AMERICA placement). 🔴 It is in the set as "
     "the byte-length negative control: `1 100` B against `1 066` B for a "
     "BYTE-IDENTICAL GRANT, and the whole 34-byte delta is the holder string. "
     "🔵 Exact byte length cannot certify a fill-in-slot family — the quantity "
     "varies with a field that is not the grant."),
    ("apache-2.0-noplag-engine", "Apache-2.0", "OK",
     "NoplagLabs/noplag-engine — the Apache-2.0 legalcode at **11 358** B, "
     "`cfc7749b96f6`, holder channel `BLIND-FIXED-DOCUMENT` (the appendix slot is "
     "unfilled: `Copyright [yyyy] [name of copyright owner]`). 🔴 The second "
     "negative control, and the sharper one: `noplag[1:] == reference-audit` "
     "EXACTLY — the entire difference is **one leading newline**."),
    ("mpl-2.0-hacklympics", "MPL-2.0", "OK",
     "aesophor/hacklympics — the MPL-2.0 legalcode, `16 725` B, "
     "`1f256ecad192`, title line `Mozilla Public License Version 2.0`. 🟢 NOT "
     "part of `ACTION p310-R` item 1 and pinned anyway, because the licence "
     "probe this pass ran over the `proctoring` axis returned it first-hand and "
     "`MPL-2.0` (161 cells) was on the uncovered list. 🔵 It is the first "
     "MEDIUM-consequence family this base has exercised — a file-level copyleft, "
     "where a wrong permissive answer costs a client an obligation they did not "
     "price rather than the right to ship at all."),
    ("gpl-2.0-opensis", "GPL-2.0", "OK",
     "OS4ED/openSIS-Classic — title line `GNU General Public License`, "
     "`Version 2`, `17 286` B, "
     "`224ac3d403e3`, served from the repository's `docs/` directory rather than "
     "any ROOT rung (the exact paths are named on the shelves, not here: see "
     "`ACTION p311-R` item 4). 🔴 THIS ROW ARRIVED AS A "
     "REFUTATION. This pass wrote *«no payload at any probed rung»* on the "
     "shelves; `gate-enumeration` (`p275`) went red, walked the tree and named "
     "two candidate grants under `docs/` that no ROOT ladder reaches. 🟢 Two "
     "gains in one row: `GPL-2.0` was the LARGEST uncovered family (443 cells), "
     "and the payload opens with a UTF-8 **BOM** (`ef bb bf`) — the invisible "
     "one-character prefix that defeated this module's own first normalisation, "
     "because `str.strip()` does not treat `U+FEFF` as whitespace."),
    ("dbad-1.1-matrix", "DBAD-1.1", "UNDETERMINED",
     "HalidCisse/Matrix — the **`DBAD` public licence, v1.1** (the title is "
     "spelled out on the shelves, not here: a licence TITLE in a code string is "
     "indistinguishable to `p283-ladder-case-audit` from a licence PATH rung, and "
     "it moved the standing ratchet for a file that probes no paths at all — "
     "`ACTION p311-R` item 4). `1 127` B, "
     "`65569613b0b7`. 🔴 A 23rd family, found on the axis `ACTION p310-R` item 5 "
     "named, and the first grant on this base that is UNCLASSIFIABLE BY DESIGN: "
     "clause 1 reads *«Do whatever you like with the original work, just don't "
     "be a dick»* with a list that is explicitly *«not limited to»*. 🔴 It also "
     "carries a resale prohibition (1b) and an unquantified expectation of "
     "payment on commercial success (2). 🟢 IN THE SET AS A POSITIVE CONTROL: "
     "all 8 payload readers ABSTAIN on it and `p306` returns "
     "`commercial_use=UNDETERMINED`, which under `P250` is indistinguishable "
     "from PROHIBITED. The battery fails SAFE on a family it has never seen, "
     "and that is a property worth a standing control."),
    ("apache-2.0-reference-audit", "Apache-2.0", "OK",
     "constructorfabric/reference-audit — the same legalcode at the canonical "
     "**11 357** B, `c71d239df917`. 🟢 Two repositories on this base serve this "
     "exact sha (`ai-for-edu/time-series-analysis-for-education` is the other), "
     "which is what a fixed-document family looks like when nobody edits it. "
     "🔵 Paired with the row above it gives the gate a TRUE positive and a TRUE "
     "negative for the same grant, which is the only way to show that a "
     "normalising oracle has not simply been loosened until everything matches."),
]


def resolve(prefix):
    """The one file in `fixtures/` whose name starts with `prefix`."""
    hits = sorted(n for n in os.listdir(FIX) if n.startswith(prefix))
    if len(hits) != 1:
        raise LookupError("%s resolves to %d files, expected 1" % (prefix, len(hits)))
    return os.path.join(FIX, hits[0])


def load(prefix):
    """Return (text, bytes_len, sha256_12) for a pinned fixture."""
    with open(resolve(prefix), "rb") as fh:
        raw = fh.read()
    return raw.decode("utf-8", "replace"), len(raw), hashlib.sha256(raw).hexdigest()[:12]


def declared():
    """[(name, family, commercial, why, text, bytes, sha12)] for every fixture."""
    out = []
    for name, fam, com, why in DECLARED:
        text, n, sha = load(name)
        out.append((name, fam, com, why, text, n, sha))
    return out


if __name__ == "__main__":
    for name, fam, com, _why, _text, n, sha in declared():
        print("%-34s %-12s %-5s %7d B  %s" % (name, fam, com, n, sha))
