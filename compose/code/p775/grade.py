#!/usr/bin/env python3
"""p775 grant grader — written from scratch for pass p775.

Re-implements, rather than executes, the p774 instruments (code execution
inside the cloned repository is denied; see ACTION p774-A / p774-I).

Three jobs:
  A. widened-set re-grade  (ACTION p774-B) — the 8 NOT-IN-CANONICAL-SET rows
     against the canonical set grown from 27 to 36 texts.
  B. deontic guard         (ACTION p774-C) — standing contract for every
     verdict; re-grade the 138 body:near-canonical rows and report survivors.

Grading rungs (absolute edit budget, per ACTION p773-D/p774-C):
  body:canonical        normalised operative bodies identical
  body:near-canonical   abs char delta <= 64 AND deontic multiset unchanged
  OPERATIVE-TEXT-ALTERED otherwise, when a canonical text is the closest match
  NOT-IN-CANONICAL-SET  no canonical text reaches 0.60 similarity

The deontic guard is the part that is new as a *contract*: a 6-character edit
that moves a negation, a modal or a scope word is an alteration at ANY
document size, so it can veto the near-canonical rung but never grant it.
"""
import difflib
import os
import re
import sys

CANON_DIR = sys.argv[1] if len(sys.argv) > 1 else "canonical"
EDIT_BUDGET = 64
SIM_FLOOR = 0.60

# Operators whose movement changes who owes what to whom.
DEONTIC = [
    "not", "no", "nor", "never", "cannot", "shall", "must", "may",
    "except", "unless", "only", "without", "non", "prohibited",
    "required", "requires", "restricted", "limited", "disclaim",
    "disclaimed", "warranty", "warranties", "liability", "liable",
    "merchantability", "permitted", "subject",
]

# Lines that are instance data, not operative text.
NOISE = re.compile(
    r"^\s*(copyright|\(c\)|©|all rights reserved|licensed under|"
    r"spdx-license-identifier)", re.I)


def normalise(text):
    """Strip instance data and whitespace variation; keep operative wording."""
    out = []
    for line in text.splitlines():
        if NOISE.match(line):
            continue
        line = re.sub(r"<[^>]{0,80}>", "", line)      # <year>, <holders>
        line = re.sub(r"\[[^\]]{0,80}\]", "", line)   # [yyyy] [name]
        line = re.sub(r"\b(19|20)\d{2}\b", "", line)  # bare years
        out.append(line)
    joined = " ".join(out).lower()
    joined = joined.replace("“", '"').replace("”", '"')
    joined = joined.replace("‘", "'").replace("’", "'")
    joined = re.sub(r"[^a-z0-9\s]", " ", joined)
    return re.sub(r"\s+", " ", joined).strip()


def deontic_profile(norm):
    words = norm.split()
    return {op: words.count(op) for op in DEONTIC}


def family(lid):
    """Collapse the only/or-later axis.

    CONTROL FINDING p775: the four GNU pairs (GPL-2.0, GPL-3.0, LGPL-3.0,
    AGPL-3.0) have BYTE-IDENTICAL operative bodies after normalisation —
    similarity 1.000. The only/or-later distinction lives in the project's
    NOTICE ("either version 3 ... or (at your option) any later version"),
    never in the LICENSE payload. So a body match CANNOT decide that axis and
    any verdict that names -only or -or-later from a body alone is unsound.
    Grade to the family; let notice prose resolve the suffix or leave it open.
    """
    return re.sub(r"-(only|or-later)$", " group", lid)


def similarity(a, b):
    """Symmetric word-level ratio.

    CONTROL FINDING p775 (defect #2, caught before any verdict was published):
    difflib.SequenceMatcher's `autojunk` heuristic treats any element present
    in >1% of the SECOND sequence as junk. On character sequences of licence
    length that is nearly every letter, so the ratio becomes both wrong and
    ASYMMETRIC: canonical BUSL-1.1 against sdv-dev/SDV scores 0.0817 in
    (candidate, canonical) order and 0.8494 reversed — the same pair, a 10x
    spread, purely from argument order. Any grader that compares licence text
    character-wise with default difflib settings is unsound, and the failure
    mode is silent: it reports "no canonical text is close" for a body that
    is in fact an 87% match. Fix: autojunk=False and compare WORDS, which is
    symmetric and is also the unit a licence's meaning lives in.
    """
    return difflib.SequenceMatcher(None, a.split(), b.split(),
                                   autojunk=False).ratio()


def load_canon(d):
    canon = {}
    for fn in sorted(os.listdir(d)):
        if not fn.endswith(".txt"):
            continue
        with open(os.path.join(d, fn), encoding="utf-8", errors="replace") as fh:
            raw = fh.read()
        n = normalise(raw)
        canon[fn[:-4]] = (n, deontic_profile(n), len(raw))
    return canon


def grade(body, canon):
    """Return (verdict, licence_id, similarity, abs_delta, deontic_note)."""
    n = normalise(body)
    if not n:
        return ("EMPTY-AFTER-NORMALISE", "-", 0.0, 0, "-")
    prof = deontic_profile(n)
    best_id, best_sim = "-", 0.0
    for lid, (cn, _cp, _cb) in canon.items():
        sim = similarity(n, cn)
        if sim > best_sim:
            best_id, best_sim = lid, sim
    if best_sim < SIM_FLOOR:
        return ("NOT-IN-CANONICAL-SET(long bespoke text)", "-", best_sim, 0, "-")
    cn, cprof, _ = canon[best_id]
    fam = family(best_id)
    delta = abs(len(n) - len(cn))
    if n == cn:
        return ("body:canonical", fam, best_sim, 0, "clean")
    moved = sorted(op for op in DEONTIC if prof.get(op, 0) != cprof.get(op, 0))
    if moved:
        note = "deontic=" + ",".join(moved[:4])
        return ("OPERATIVE-TEXT-ALTERED", fam, best_sim, delta, note)
    if delta <= EDIT_BUDGET:
        return ("body:near-canonical", fam, best_sim, delta, "clean")
    return ("OPERATIVE-TEXT-ALTERED", fam, best_sim, delta, "budget")


if __name__ == "__main__":
    canon = load_canon(CANON_DIR)
    sys.stderr.write("canonical texts loaded: %d\n" % len(canon))
    # self-control: every canonical text must grade to itself, cleanly.
    defects = 0
    for lid, (cn, _p, _b) in canon.items():
        with open(os.path.join(CANON_DIR, lid + ".txt"), encoding="utf-8",
                  errors="replace") as fh:
            v, got, sim, d, note = grade(fh.read(), canon)
        if v != "body:canonical" or family(got) != family(lid):
            sys.stderr.write("CONTROL-DEFECT %s -> %s %s sim=%.3f\n"
                             % (lid, v, got, sim))
            defects += 1
    sys.stderr.write("control: %d/%d canonical texts self-identify, %d defects\n"
                     % (len(canon) - defects, len(canon), defects))
    for line in sys.stdin:
        path = line.strip()
        if not path:
            continue
        with open(path, encoding="utf-8", errors="replace") as fh:
            body = fh.read()
        v, lid, sim, d, note = grade(body, canon)
        print("\t".join([os.path.basename(path), v, lid,
                         "%.4f" % sim, str(d), note, str(len(body))]))
