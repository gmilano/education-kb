#!/usr/bin/env python3
"""The MIRROR control of `trend-backlink-audit`: does a pass DELIVER an action
that its own corpus already answered?

Pase 58 (trend 398) diagnosed the defect and asked pase 59 for the instrument:
`trend-backlink-audit/` verifies that every CITED trend has a definition; the
missing direction is the other one -- that no action handed forward asks for
something already closed.

    python3 crosscheck.py          # the report
    python3 crosscheck.py --tsv    # one row per gap citation in an action
    python3 test_crosscheck.py     # the controls

WHAT PASE 59 FOUND BEFORE WRITING A LINE, and it changes the spec it was given:

(1) The fixture the action named IS NOT REAL. Pase 58 wrote that "action 3 of
    pase 57" asked to resolve "two incompatible dates", and that trend 392 of
    the same pase had already closed it. Pase 57's action block cites gaps
    249, 232 and 100 -- and contains no date claim at all. The "two dates"
    question is `gap 56`, whose action lived in pase 32 and which the ledger
    closed at pase 39. So the mandated negative control ("it has to FAIL on
    the real pair action 3 <-> trend 392 of pase 57") cannot be satisfied: the
    pair does not exist. Pase 58's own evidence for a cross-referencing defect
    was itself a cross-referencing error.

(2) The defect is CROSS-pass, not same-pass. Pase 58 specified "a gap that a
    trend OF THE SAME PASS declares closed". Measured over the corpus, the
    citations that matter are of gaps closed in EARLIER passes -- which is why
    this instrument compares against the ledger's closure pass, not against
    the citing pass's own trends.

(3) A gap-number scan DOES NOT WORK, and the corpus proves it. Pase 48's
    action block mentions `gap 51`, which was closed at pase 29. A naive
    detector flags it. The sentence is:

        "el metodo que cerro el gap 51 y rindio dos altas en el pase 34"

    That is a citation of a closed gap's METHOD -- precedent, the correct use
    of a closed gap -- not a request to close it again. So the unit of
    judgement is not the gap number: it is the SPEECH ACT of the clause that
    carries it. This file classifies that, and reports the classification so a
    reader can overrule it, because a regex over Spanish prose is a weaker
    instrument than a code read and saying so is the point.
"""
from __future__ import annotations

import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
TRENDS = "intel/trends.md"

ACTION_HDR = re.compile(r"^##\s+.*acciones que el pase\s+(\d+)\s+deja escritas")
GAP_CITE = re.compile(r"gaps?\s+(\d+)")

# A clause that ASKS: the verbs this KB uses when it hands work forward.
REQUEST = re.compile(
    r"\b(medir|determinar|resolver|cerrar|cerrarlo|cerrarla|verificar|escribir"
    r"|pedir|establecer|ampliar|extiende|abierto|abierta|sin cerrar|queda)\b",
    re.IGNORECASE,
)
# A clause that CITES: the shapes this KB uses when it leans on a closed gap.
PRECEDENT = re.compile(
    r"(que\s+cerr[oó]|cerrad[oa]\s+(?:en|por)|el\s+m[eé]todo\s+que"
    r"|ya\s+cerrad[oa]|rindi[oó]|como\s+(?:en|lo hizo))",
    re.IGNORECASE,
)


def _clause(text: str, at: int, width: int = 160) -> str:
    """The sentence-ish window a gap number sits in. Prose, so approximate."""
    lo = max(0, at - width)
    hi = min(len(text), at + width)
    return re.sub(r"\s+", " ", text[lo:hi]).strip()


def action_blocks(path: str) -> dict[int, str]:
    """pass number -> the text of the action block that pass handed forward."""
    blocks: dict[int, str] = {}
    cur = None
    buf: list[str] = []
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            m = ACTION_HDR.match(line)
            if m:
                if cur is not None:
                    blocks[cur] = " ".join(buf)
                cur, buf = int(m.group(1)), []
                continue
            if line.startswith("## ") and cur is not None:
                blocks[cur] = " ".join(buf)
                cur, buf = None, []
                continue
            if cur is not None:
                buf.append(line.rstrip("\n"))
    if cur is not None:
        blocks[cur] = " ".join(buf)
    return blocks


def closed_gaps(path: str) -> dict[int, int]:
    """gap -> the pass that declared it closed.

    Two forms carry a closure in this corpus, and both are required:
      1. `## 158. **Gap 50, CERRADO:** ... (agregado en el pase 43 ...)`
      2. a `| **56** (...) | CERRADO ...` row under a `... al cierre del pase N`
         header, where the pass comes from the HEADER, not the row.
    """
    closures: dict[int, int] = {}
    ledger_pass = None
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            if line.startswith("## "):
                m = re.search(r"al cierre del pase\s+(\d+)", line)
                ledger_pass = int(m.group(1)) if m else None
                m2 = re.search(r"[Gg]ap\s+(\d+)[^|]{0,40}CERRAD", line)
                if m2:
                    m3 = re.search(r"pase\s+(\d+)", line)
                    if m3:
                        g, p = int(m2.group(1)), int(m3.group(1))
                        closures.setdefault(g, p)
                continue
            if ledger_pass is not None and line.lstrip().startswith("|"):
                m4 = re.match(r"\s*\|\s*\*\*(\d+)\*\*", line)
                if m4 and "CERRAD" in line.upper():
                    closures.setdefault(int(m4.group(1)), ledger_pass)
    return closures


def classify(clause: str) -> str:
    """REQUEST, PRECEDENT, or UNCLEAR -- never a silent guess."""
    req, prec = bool(REQUEST.search(clause)), bool(PRECEDENT.search(clause))
    if prec and not req:
        return "PRECEDENT"
    if req and not prec:
        return "REQUEST"
    if prec and req:
        return "PRECEDENT"  # "el metodo que cerro el gap 51" also says "cerro"
    return "UNCLEAR"


def citations(path: str):
    """Every gap citation inside an action block, classified."""
    blocks, closures = action_blocks(path), closed_gaps(path)
    for pas in sorted(blocks):
        text = blocks[pas]
        for m in GAP_CITE.finditer(text):
            gap = int(m.group(1))
            clause = _clause(text, m.start())
            kind = classify(clause)
            closed_at = closures.get(gap)
            stale = (
                kind == "REQUEST"
                and closed_at is not None
                and closed_at <= pas
            )
            yield {
                "pass": pas, "gap": gap, "kind": kind,
                "closed_at": closed_at, "stale": stale, "clause": clause,
            }


def main(argv) -> int:
    path = os.path.join(ROOT, TRENDS)
    if not os.path.exists(path):
        print("missing %s" % path)
        return 2
    rows = list(citations(path))
    if "--tsv" in argv:
        print("pass\tgap\tkind\tclosed_at\tstale\tclause")
        for r in rows:
            print("%d\t%d\t%s\t%s\t%s\t%s" % (
                r["pass"], r["gap"], r["kind"],
                "" if r["closed_at"] is None else r["closed_at"],
                "YES" if r["stale"] else "no", r["clause"]))
        return 0
    stale = [r for r in rows if r["stale"]]
    unclear = [r for r in rows if r["kind"] == "UNCLEAR"]
    print("gap citations inside action blocks : %d" % len(rows))
    print("  classified REQUEST              : %d"
          % sum(1 for r in rows if r["kind"] == "REQUEST"))
    print("  classified PRECEDENT            : %d"
          % sum(1 for r in rows if r["kind"] == "PRECEDENT"))
    print("  UNCLEAR (read these by hand)    : %d" % len(unclear))
    print("  STALE (asks for a closed gap)   : %d" % len(stale))
    for r in stale:
        print("    pase %d asks gap %d, closed at pase %s"
              % (r["pass"], r["gap"], r["closed_at"]))
    for r in unclear:
        print("    UNCLEAR pase %d gap %d: %s" % (r["pass"], r["gap"],
                                                  r["clause"][:110]))
    return 1 if stale else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
