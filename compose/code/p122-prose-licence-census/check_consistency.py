#!/usr/bin/env python3
"""ACTION T + ACTION U, asserted mechanically over the tree.

ACTION T — the ledger (intel/open-gaps.md), the root README pass log and the
newest instrument README must name the SAME pass and the SAME open actions.
P121-G showed the three drift apart silently: the ledger stopped at p118
while p119 and p120 both ran, and ACTION C and ACTION D fell out of the
record for four passes because nothing forced the three to agree.

ACTION U — GitHub slugs are case-insensitive for addressing, so every join
must fold case. P121-D showed one address counted as two between two
instruments.

usage: check_consistency.py KB_ROOT
"""
import glob
import os
import re
import sys

ORDINALS = {
    "hundred-and-fourteenth": 114, "hundred-and-fifteenth": 115,
    "hundred-and-sixteenth": 116, "hundred-and-seventeenth": 117,
    "hundred-and-eighteenth": 118, "hundred-and-nineteenth": 119,
    "hundred-and-twentieth": 120, "hundred-and-twenty-first": 121,
    "hundred-and-twenty-second": 122, "hundred-and-twenty-third": 123,
}
ACTION = re.compile(r"\bACTION\s+([A-Z])\b")


def readme_pass(root):
    """Highest `## Pass NNN` in the root README."""
    text = open(os.path.join(root, "README.md"), encoding="utf-8").read()
    nums = [int(n) for n in re.findall(r"^##\s*Pass\s+(\d+)", text, re.M)]
    return max(nums) if nums else None


def ledger_pass(root):
    """Highest pass in the ledger, which spells its passes as ORDINAL WORDS."""
    text = open(os.path.join(root, "intel/open-gaps.md"), encoding="utf-8").read()
    found = [n for word, n in ORDINALS.items() if word in text.lower()]
    found += [int(n) for n in re.findall(r"^##\s*.*?pass\s+(\d+)", text, re.M | re.I)]
    return max(found) if found else None


def instrument_dirs(root):
    """Every compose/code/pNNN-* directory, as {number: [paths]}."""
    out = {}
    for d in sorted(glob.glob(os.path.join(root, "compose/code/p*-*"))):
        m = re.match(r"p(\d+)-", os.path.basename(d))
        if m:
            out.setdefault(int(m.group(1)), []).append(d)
    return out


def instrument_pass(root, pass_no=None):
    """Resolve the instrument belonging to a GIVEN pass, by exact match.

    p122: `max(pNNN)` is NOT the newest pass's instrument. The pNNN prefix is
    an instrument INDEX, not a pass number: it runs to p1040 over 182
    directories while this KB is on pass 122. Taking the maximum answers
    "which instrument has the largest index", which is a different question
    and silently returns an instrument from another era. The only mechanical
    link from a pass to its instrument is an EXACT name match, and that link
    exists only because recent passes happen to have used their own number.
    """
    dirs = instrument_dirs(root)
    if pass_no is not None:
        return pass_no if pass_no in dirs else None
    return max(dirs) if dirs else None


def _newest_section(text, heading_rx):
    """Text of the NEWEST pass section only.

    p122: comparing whole files makes `ACTION T` report drift that is not
    drift — a record that recaps the PREVIOUS pass's discharged actions names
    letters the other records have correctly stopped carrying. The question
    `ACTION T` asks is whether the three agree about what is OPEN NOW, so each
    record is sliced at its second pass heading.
    """
    marks = [m.start() for m in heading_rx.finditer(text)]
    if not marks:
        return text
    stop = marks[1] if len(marks) > 1 else len(text)
    return text[marks[0]:stop]


def open_actions(root):
    """Actions named in the NEWEST pass section of each of the three places."""
    out = {}
    readme = open(os.path.join(root, "README.md"), encoding="utf-8").read()
    out["readme"] = set(ACTION.findall(
        _newest_section(readme, re.compile(r"^##\s*Pass\s+\d+", re.M))))
    ledger = open(os.path.join(root, "intel/open-gaps.md"), encoding="utf-8").read()
    out["ledger"] = set(ACTION.findall(
        _newest_section(ledger, re.compile(r"^##\s+\S*\s*Hundred", re.M))))
    ip = instrument_pass(root, readme_pass(root))
    out["instrument"] = set()
    for d in glob.glob(os.path.join(root, f"compose/code/p{ip}-*")):
        f = os.path.join(d, "README.md")
        if os.path.exists(f):
            out["instrument"] |= set(ACTION.findall(open(f, encoding="utf-8").read()))
    return out


def fold_census(root):
    """ACTION U: fold every address in the tree and count the collisions."""
    addr = re.compile(r"github\.com/([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+?)(?=[)\s>`\"']|$)")
    exact = set()
    for pat in ("*.md", "*.tsv", "*.json", "*.sh", "*.py", "*.txt"):
        for f in glob.glob(os.path.join(root, "**", pat), recursive=True):
            if "/.git/" in f:
                continue
            try:
                text = open(f, encoding="utf-8", errors="replace").read()
            except OSError:
                continue
            for a in addr.findall(text):
                exact.add(a.rstrip(".").rstrip(")"))
    groups = {}
    for a in exact:
        groups.setdefault(a.lower(), set()).add(a)
    collided = {k: v for k, v in groups.items() if len(v) > 1}
    return exact, groups, collided


def main(root):
    rp, lp = readme_pass(root), ledger_pass(root)
    dirs = instrument_dirs(root)
    ip = instrument_pass(root, rp)
    print("== ACTION T — do the three records name the same pass? ==")
    print(f"  root README.md pass log : {rp}")
    print(f"  intel/open-gaps.md      : {lp}")
    print(f"  instrument for pass {rp}  : {'p%d-* present' % ip if ip else 'ABSENT'}")
    print(f"  instrument dirs total   : {len(dirs)}  "
          f"(max index p{max(dirs)} — NOT a pass number)")
    agree_pass = (rp == lp) and ip is not None
    print(f"  VERDICT: {'AGREE' if agree_pass else 'DISAGREE'}")
    acts = open_actions(root)
    print("\n== ACTION T — do they name the same open actions? ==")
    for k in ("readme", "ledger", "instrument"):
        print(f"  {k:11s}: {' '.join(sorted(acts[k])) or '(none)'}")
    union = acts["readme"] | acts["ledger"] | acts["instrument"]
    common = acts["readme"] & acts["ledger"] & acts["instrument"]
    missing = {k: sorted(union - acts[k]) for k in acts}
    print(f"  union      : {' '.join(sorted(union))}")
    print(f"  in all three: {' '.join(sorted(common)) or '(none)'}")
    for k, v in missing.items():
        if v:
            print(f"  MISSING from {k}: {' '.join(v)}")
    agree_acts = not any(missing.values())
    print(f"  VERDICT: {'AGREE' if agree_acts else 'DISAGREE'}")

    exact, groups, collided = fold_census(root)
    print("\n== ACTION U — slug case folding ==")
    print(f"  distinct addresses, case-SENSITIVE : {len(exact)}")
    print(f"  distinct addresses, case-FOLDED    : {len(groups)}")
    print(f"  addresses double-counted           : {len(exact) - len(groups)}")
    print(f"  folded keys with >1 spelling       : {len(collided)}")
    for k, v in sorted(collided.items())[:12]:
        print(f"    {k}  <-  {' | '.join(sorted(v))}")
    print(f"  VERDICT: {'NOT REFUTED' if len(collided) >= 2 else 'REFUTED'} "
          f"(clause: refuted if fewer than 2 addresses change verdict)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
