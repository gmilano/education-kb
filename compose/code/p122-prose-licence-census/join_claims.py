#!/usr/bin/env python3
"""Join prose licence CLAIMS against MEASURED tree licences.

Two guards this KB has paid for already:
  * P121-B — corrections are written INLINE in this KB, so a sentence that
    names a wrong token while correcting it is not a defect. Lines carrying
    correction/discussion markers are reported separately, never as defects.
  * P121-D / ACTION U — joins are case-normalised on the slug, or one address
    counts as two.
"""
import os
import re
import sys

EQUIV = {
    "apache 2.0": "apache-2.0", "apache-2.0": "apache-2.0",
    "agpl-3": "agpl-3.0", "agplv3": "agpl-3.0", "agpl-3.0": "agpl-3.0",
    "gplv3": "gpl-3.0", "gpl-3.0": "gpl-3.0",
    "gplv2": "gpl-2.0", "gpl-2.0": "gpl-2.0",
    "lgplv3": "lgpl-3.0", "lgpl-3.0": "lgpl-3.0",
    "mit": "mit",
    "bsd-3-clause": "bsd-3-clause", "bsd-2-clause": "bsd-2-clause",
    "mpl-2.0": "mpl-2.0", "epl-2.0": "epl-2.0",
    "elastic license": "elastic-2.0", "elastic-2.0": "elastic-2.0",
    "lgpl": "lgpl", "cc-by": "cc-by-4.0",
}

# A line carrying any of these is TALKING ABOUT a licence value (correcting it,
# refuting it, quoting what was published) rather than asserting it.
CORRECTION_MARKERS = [
    "was ", "⚠", "actually", "corrected", "correction", "refuted", "stale",
    "truth is", "published", "over-restrict", "wrong", "defect", "repaired",
    "instead of", "not ", "measured this pass", "claims", "claimed", "mis",
]


def fold(addresses):
    """Case-fold GitHub slugs at every join (ACTION U / P121-D).

    GitHub owner and repo names are case-insensitive for addressing, so
    `xGabrielCv/...` and `xgabrielcv/...` are ONE address. A case-sensitive
    join counts them as two, which is how p121's first tally read 4 new when
    the honest answer was 3 new plus 1 already held.
    """
    return {a.strip().lower() for a in addresses if a and a.strip()}


def norm(tok: str) -> str:
    return EQUIV.get(tok.strip().lower(), tok.strip().lower())


UNMEASURABLE = ("NO-FILE", "UNKNOWN", "EMPTY", "SPLIT:UNKNOWN", "GPL-UNTITLED",
                "STUB-SEE-DESCRIPTION")


def verdict(claim: str, measured: str) -> str:
    """Compare one prose CLAIM against the MEASURED tree token.

    A split-grant file whose PRIMARY grant is the claimed licence agrees with
    the claim: the claim is incomplete, not wrong, and the two are different
    findings. A grant resolved by REFERENCE agrees more weakly still, and the
    verdict says which tier answered.
    """
    if measured in UNMEASURABLE:
        return "UNMEASURABLE"
    if measured.startswith("SPLIT-REF:"):
        names = measured[len("SPLIT-REF:"):].split("+")
        return "AGREES-REF" if norm(claim) == norm(names[0]) else "DISAGREES"
    if measured.startswith("SPLIT:"):
        primary = measured[len("SPLIT:"):]
        return "AGREES-SPLIT" if norm(claim) == norm(primary) else "DISAGREES"
    return "AGREES" if norm(claim) == norm(measured) else "DISAGREES"


def is_correction(line: str) -> bool:
    low = line.lower()
    return any(m in low for m in CORRECTION_MARKERS)


def main(scratch: str) -> int:
    measured = {}
    with open(os.path.join(scratch, "action-r-measured.tsv"), encoding="utf-8") as fh:
        for row in fh:
            a, b, p, by, tok = row.rstrip("\n").split("\t")
            measured[a.lower()] = (tok, b, p, by)

    defects, corrections, unmeasurable, splits = [], [], [], []
    with open(os.path.join(scratch, "action-r-pairs.tsv"), encoding="utf-8") as fh:
        for row in fh:
            f, n, addr, claim, text = row.rstrip("\n").split("\t", 4)
            m = measured.get(addr.lower())
            if not m:
                continue
            tok, br, pth, by = m
            v = verdict(claim, tok)
            if v == "UNMEASURABLE":
                unmeasurable.append((f, n, addr, claim, tok))
                continue
            if v in ("AGREES", "AGREES-SPLIT"):
                continue
            if v == "AGREES-REF":
                splits.append((f, n, addr, claim, tok, by, text))
                continue
            rec = (f, n, addr, claim, tok, by, text)
            (corrections if is_correction(text) else defects).append(rec)

    for name, rows in (("DEFECT", defects), ("CORRECTION-CONTEXT", corrections),
                       ("INCOMPLETE-BY-REFERENCE", splits)):
        for r in rows:
            print(f"{name}\t" + "\t".join(r[:6]))
    for r in unmeasurable:
        print("UNMEASURABLE\t" + "\t".join(r))
    print(f"\n# defects={len(defects)} correction-context={len(corrections)} "
          f"unmeasurable={len(unmeasurable)}", file=sys.stderr)
    return len(defects)


if __name__ == "__main__":
    main(sys.argv[1])
