#!/usr/bin/env python3
"""p283 (`p282`'s declared item 2) — WHICH PATH LADDERS ARE CASE-CLOSED, AND WHICH ARE NOT.

🔴 Why it exists.  `P1057` (p189) established that `raw.githubusercontent.com` is
CASE-SENSITIVE, so *"a one-spelling path list has not looked for the file; it has looked
for one spelling of the file."*  That was built for LICENCE paths, and
`pass256-ladder-closure` keeps the licence ladder closed against `p229`'s TIER_A.

🔴 `p282` then found `README.MD` — uppercase extension — on `ls1intum/Pyris`, after `p268`
had published *"neither repository serves a README"* off a four-spelling ladder with **no
uppercase extension in it**.  `p282`'s words: *"`p1057`'s licence-path-case class, never
inherited by the README ladder beside it."*  It registered the generalisation as item 2:
**audit which ladders are case-closed, not just the licence one.**

🟢 THE PREDICATE, inherited from `P1057` unchanged: a ladder is case-closed when it varies
the case of the STEM **and** of the EXTENSION.  `P1057` is explicit that the extension is
the half that gets forgotten — `LICENSE.TXT` on `openedx/XBlock` and `README.MD` on
`ls1intum/Pyris` are the same defect, 93 passes apart.

🔵 FOUR VERDICTS, in order of strength.  Only the first two are immune by construction:

  TREE-ENUMERATED   the instrument lists the tree (`git ls-tree` / `ls-files`) instead of
                    guessing.  `p275` built the enumeration gate for exactly this reason
                    and wrote "a path ladder cannot prove absence".  No ladder, no risk.
  CASE-INSENSITIVE  the match is folded (`re.I`, `tr A-Z a-z`, `.lower()`), so spelling
                    cannot hide a file.
  CASE-CLOSED       a literal ladder that varies stem case AND extension case.
  STEM-ONLY         varies the stem but spells the extension ONE way.  🔴 This is
                    `p282`'s class and `P1057`'s class — the one that has now produced a
                    false absence twice.
  SINGLE-SPELLING   one spelling of the family.  Cannot prove an absence at all.

🔵 Scope, stated so the number is not read as more than it is: this reads the LITERAL path
vocabulary of each instrument under `compose/code/`.  An instrument that builds its paths
by concatenation is reported as what its literals show, and a ladder is only a finding
when the instrument uses it to decide that a file is ABSENT.
"""
import argparse
import pathlib
import re
import sys

FAMILIES = {
    "readme": re.compile(r"^readme(\.[a-z]+)?$", re.I),
    "licence": re.compile(r"^licen[sc]e(\.[a-z]+)?$", re.I),
    "copying": re.compile(r"^copying(\.[a-z]+)?$", re.I),
    "notice": re.compile(r"^notice(\.[a-z]+)?$", re.I),
}
LITERAL = re.compile(r"""['"]([A-Za-z][A-Za-z0-9_.-]{0,40})['"]""")
BARE = re.compile(r"\b((?:README|LICENSE|LICENCE|COPYING|NOTICE)(?:\.[A-Za-z]+)?)\b")
TREE = re.compile(r"ls-tree|ls-files|git\s+archive|--name-only|walk\(|iterdir\(|rglob\(")
FOLD = re.compile(r"re\.I\b|re\.IGNORECASE|\(\?i\)|\.lower\(\)|\.upper\(\)|\.casefold\(\)|tr\s+'?A-Z|-iname|grep\s+-[a-zA-Z]*i")


def spellings(text):
    out = set()
    for m in list(LITERAL.finditer(text)) + list(BARE.finditer(text)):
        tok = m.group(1)
        for fam, rx in FAMILIES.items():
            if rx.match(tok):
                out.add((fam, tok))
    return out


def _near(text, toks, rx, window=2):
    """Does `rx` match within `window` lines of one of this family's spellings?

    🔴 The first draft of this audit asked only whether the FILE contained `.lower()`
    anywhere, and returned CASE-INSENSITIVE for 316 of 580 ladders — an immunity claim
    resting on any unrelated string-folding in a 400-line script.  That is the overclaim
    this base's own instruments keep being caught by, so the predicate is now PROXIMITY:
    the fold must sit beside the path vocabulary it is supposed to protect.
    🔵 It is still a SCREEN, not a proof — stated in the verdict name, not in a footnote.
    """
    lines = text.splitlines()
    hits = [i for i, ln in enumerate(lines) if any(t in ln for t in toks)]
    for i in hits:
        if rx.search("\n".join(lines[max(0, i - window): i + window + 1])):
            return True
    return False


def classify(fam_spellings, text):
    """Return a verdict for ONE family's ladder inside one file."""
    if _near(text, fam_spellings, TREE) or TREE.search(text) and len(fam_spellings) < 2:
        return "TREE-ENUMERATED"
    if _near(text, fam_spellings, FOLD):
        return "FOLD-ON-PATH"
    if len(fam_spellings) < 2:
        return "SINGLE-SPELLING"
    stems, exts = set(), set()
    for sp in fam_spellings:
        stem, _, ext = sp.partition(".")
        stems.add(stem)
        if ext:
            exts.add(ext)
    stem_varies = len({x.lower() for x in stems}) < len(stems)
    ext_varies = len({e.lower() for e in exts}) < len(exts)
    if ext_varies:
        return "CASE-CLOSED"
    if stem_varies:
        return "STEM-ONLY"
    return "CASE-UNVARIED"


def audit(root):
    rows = []
    for p in sorted(pathlib.Path(root, "compose", "code").rglob("*")):
        if p.suffix not in (".py", ".sh") or "__pycache__" in p.parts:
            continue
        if p.name.startswith("test_"):
            continue
        try:
            text = p.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        found = spellings(text)
        if not found:
            continue
        byfam = {}
        for fam, tok in found:
            byfam.setdefault(fam, set()).add(tok)
        for fam, toks in sorted(byfam.items()):
            # 🔵 p282's sentence was literally "none of the four probed spellings
            # carried an UPPERCASE EXTENSION".  That is a narrower and more directly
            # actionable quantity than closure, so it is its own column.
            upper_ext = any(
                "." in t and t.partition(".")[2] != t.partition(".")[2].lower()
                for t in toks
            )
            rows.append((
                str(p.relative_to(root)), fam, classify(toks, text),
                "UPPER-EXT" if upper_ext else "no-upper-ext",
                " ".join(sorted(toks)),
            ))
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    ap.add_argument("--out")
    ap.add_argument("--family")
    a = ap.parse_args()
    rows = audit(pathlib.Path(a.root).resolve())
    if a.family:
        rows = [r for r in rows if r[1] == a.family]
    lines = ["instrument\tfamily\tverdict\tupper_ext\tspellings"] + ["\t".join(r) for r in rows]
    if a.out:
        pathlib.Path(a.out).write_text("\n".join(lines) + "\n", encoding="utf-8")
    tally = {}
    for r in rows:
        tally[r[2]] = tally.get(r[2], 0) + 1
    for r in rows:
        if r[2] in ("STEM-ONLY", "CASE-UNVARIED"):
            print("\t".join(r))
    print("# " + "  ".join(f"{k}={v}" for k, v in sorted(tally.items())))
    print(f"# ladders={len(rows)} instruments={len({r[0] for r in rows})}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
