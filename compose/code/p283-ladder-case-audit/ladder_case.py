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
# 🟢 p286 — `BARE` IS CASE-SENSITIVE WHILE `LITERAL` IS NOT, AND SHELL LADDERS ARE THE BARE
# KIND.  Every `FAMILIES` pattern carries `re.I`, so a QUOTED `"copying"` has always been
# extracted in any case; an UNQUOTED `Copying` in a `for b in ...` list was invisible, which
# graded `p207-permissive-half-audit/locate.sh` `SINGLE-SPELLING` on the one spelling it
# could see when the line reads `for b in LICENSE LICENCE License Licence license licence
# COPYING Copying copying`.
# 🔴 p286 FIRST TRIED THE OBVIOUS FIX — `re.I` on `BARE` — AND MEASURED IT AS WRONG, so it
# is recorded here rather than shipped.  Bare lowercase family words are PROSE far more
# often than paths in this corpus, because the corpus is full of licence BODY-TEXT
# classifiers: it pulled in `GNU AFFERO GENERAL PUBLIC LICENSE` from a title regex,
# `*"unauthorized copying"*` from `lib/license_family.sh`'s restriction `case`, and
# `license="MIT"` from a setup.py fixture. `STEM-ONLY` went 22 → 125 on noise.
# 🟢 The targeted fix instead: read case-varied spellings ONLY from a shell `for` list,
# which is path vocabulary by construction.
SH_LIST = re.compile(r"for\s+\w+\s+in\s+([^;\n]*)", re.I)
# 🟢 p286 — the THIRD any-case path-vocabulary context: a regex ALTERNATION of family
# words, `(?:LICEN[CS]E|licen[cs]e|COPYING|copying|Copying|NOTICE|notice)`.  Only an
# alternative that is EXACTLY a family word is taken; `gnu (affero )?general public
# license` is a body-text phrase and its `license` stays out, which is the distinction the
# rejected `re.I` on `BARE` could not draw.
ALT_GROUP = re.compile(r"\(([^()]*\|[^()]*)\)")
# 🔴 A variable NAMED `LICENCE` takes attribute access, and `BARE`'s optional `.ext` eats it:
# `LICENCE.findall`, `LICENCE.pattern` and `LICENCE.search` were all graded as licence-path
# spellings of `p124-correction-form-marker`. Pre-existing, found while measuring the above.
_METHODS = frozenset("""findall pattern search match sub split join format strip lower upper
group groups finditer fullmatch compile keys items values get append extend startswith
endswith replace encode decode read write close name parent stem suffix""".split())
TREE = re.compile(r"ls-tree|ls-files|git\s+archive|--name-only|walk\(|iterdir\(|rglob\(")
FOLD = re.compile(r"re\.I\b|re\.IGNORECASE|\(\?i\)|\.lower\(\)|\.upper\(\)|\.casefold\(\)|tr\s+'?A-Z|-iname|grep\s+-[a-zA-Z]*i")


def spellings(text):
    out = set()
    toks = [m.group(1) for m in LITERAL.finditer(text)]
    toks += [m.group(1) for m in BARE.finditer(text)]
    # 🟢 p286: a shell `for` list is path vocabulary by construction, so its items are read
    # in ANY case — this is where `Copying`/`copying` live.
    for m in SH_LIST.finditer(text):
        toks += m.group(1).replace('"', " ").replace("'", " ").split()
    for m in ALT_GROUP.finditer(text):
        body = m.group(1)
        if body.startswith("?:"):
            body = body[2:]
        toks += [a.strip() for a in body.split("|")]
    for tok in toks:
        stem, _, ext = tok.partition(".")
        if ext and ext.lower() in _METHODS:
            continue
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


# 🟢 p284 — A GENERATOR IS NOT A LADDER, AND GRADING IT ON ITS LITERALS PUBLISHED A FALSE
# HEADLINE.  `p283` graded `p1057-licence-path-case/path_case.py` as `STEM-ONLY` for the
# `notice` family and published *"Not one `NOTICE` ladder on this base can find
# `NOTICE.TXT`"*, with `notice` *"the only family at 0.0 %"*.
# 🔴 `p1057` IS THE INSTRUMENT WHOSE JOB IS TO GENERATE THE LADDER, and its
# `candidate_paths` is a cross product over `STEMS x EXTS x _casings(stem) x {ext, ext.upper()}`
# — so `NOTICE.TXT`, `NOTICE.MD` and `Notice.txt` are all produced, for every stem.  The
# audit could not see them because it reads LITERAL path vocabulary and a cross product has
# no literal to read.  That caveat was in this file's own docstring and the headline ignored
# it, which is this base's recurring shape: a scope limit stated in prose and forgotten at
# the point of publication.
# 🟢 So the caveat is now ENFORCED IN CODE rather than documented.  An instrument that
# varies the case of BOTH halves programmatically is graded on what it generates.
# 🔵 The predicate is deliberately narrow — it requires an EXTENSION-case idiom AND a
# STEM-case idiom — so it cannot fire on a literal ladder that merely happens to call
# `.upper()` somewhere, which is exactly the overclaim `_near`'s docstring records.
_EXT_VARY = re.compile(r"ext\.upper\(\)|ext\.lower\(\)|ext_case|\{\s*ext\s*,|ext\.swapcase\(\)")
_STEM_VARY = re.compile(r"_casings\(|stem_case|stem\.upper\(\)|word\.upper\(\)|stem\.capitalize\(\)")


def generates_case_variants(text):
    """True when the file BUILDS its ladder with both halves' case varied in code.

    Both idioms are required.  An extension-case loop alone could be unrelated string
    handling; a stem-case helper alone is `STEM-ONLY` by another route.  Together they
    are the cross product `p1057` actually performs, and nothing else in this corpus
    matches both.
    """
    return bool(_EXT_VARY.search(text) and _STEM_VARY.search(text))


# 🟢 p286 — A SPELLING THAT ONLY EVER APPEARS IN A COMMENT IS NOT A LADDER.
# 🔴 Measured on this base's own corpus: of the twelve STANDING `copying` ladders, THREE
# carried no path vocabulary in code at all.  `lib/license_family.sh`'s only `copying`
# token is a byte-offset note (`# ... moodle/COPYING  byte 28.272`); `pass256-ladder-
# closure`'s is a docstring sentence; `p230-prose-path-ladder`'s two tokens are both in a
# prose paragraph, while its actual regex varies the case explicitly.  All three were
# counted as ungraded ladders in the `117`-ladder `copying` headline.
# 🔵 The predicate is deliberately crude — whole-line `#` comments and triple-quoted
# blocks — because anything cleverer would need a parser per language, and the verdict is
# named `COMMENT-ONLY` rather than folded into an immunity so the count stays readable.
_TRIPLE = re.compile(r'("""|\'\'\')(?:.|\n)*?\1')


def code_only(text):
    """`text` with triple-quoted blocks and whole-line `#` comments removed."""
    text = _TRIPLE.sub("\n", text)
    return "\n".join(ln for ln in text.splitlines() if not ln.lstrip().startswith("#"))


# 🟢 p286 — THE SHELL HALF OF `p284`'s GENERATOR FINDING.  `p284` taught this audit to
# grade a Python cross product on what it GENERATES.  The identical construction in shell
# — `for b in <stems>; do for e in "" .txt .TXT .md .MD; do printf '%s%s' "$b" "$e"` —
# was still graded on its literals.  Same defect, one language across.
_SH_FOR_LIST = re.compile(r"for\s+\w+\s+in\s+([^;\n]*)", re.I)


def shell_generates_case_variants(text, fam_spellings):
    """True when a shell `for` list varies EXTENSION case and the stems vary case too.

    Both halves are required, exactly as in `generates_case_variants`: an extension list
    alone could belong to another family's loop, and stem variants alone are `STEM-ONLY`.
    """
    exts = set()
    for m in _SH_FOR_LIST.finditer(text):
        for tok in m.group(1).replace('"', " ").replace("'", " ").split():
            if re.fullmatch(r"\.[A-Za-z]+", tok):
                exts.add(tok)
    ext_varies = len({e.lower() for e in exts}) < len(exts)
    stems = {sp.partition(".")[0] for sp in fam_spellings}
    stem_varies = len({s.lower() for s in stems}) < len(stems)
    return ext_varies and stem_varies


def classify(fam_spellings, text):
    """Return a verdict for ONE family's ladder inside one file."""
    # 🟢 p286: re-extract with the IDENTICAL rules over code-only text.  An earlier draft
    # used a looser case-insensitive membership test here and let `lib/license_family.sh`'s
    # `*"unauthorized copying"*` keep a ladder alive, which is the very prose the targeted
    # extractor exists to exclude.  The predicate must be the census's own.
    code_toks = {tok for _, tok in spellings(code_only(text))} & set(fam_spellings)
    if not code_toks:
        return "COMMENT-ONLY"
    # 🔵 And grade on what the CODE carries: `p230-prose-path-ladder` showed `COPYING` in a
    # regex and `COPYING.txt` only in its docstring, which graded as a two-rung ladder.
    fam_spellings = code_toks
    if _near(text, fam_spellings, TREE) or TREE.search(text) and len(fam_spellings) < 2:
        return "TREE-ENUMERATED"
    if generates_case_variants(text) or shell_generates_case_variants(text, fam_spellings):
        return "GENERATED-CASE-VARIED"
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


# 🟢 p286 — THE `117`-LADDER HEADLINE WAS COUNTING SUPERSEDED SCRIPTS AS LIVE RISK.
# 🔴 `p285` ranked *"case-close the `copying` family"* first on the measurement
# *"117 ladders, 0 CASE-CLOSED"*.  Bucketed by whether the instrument is INVOKED by
# `make hooks`, those 117 are **100 historical one-off pass scripts + 5 superseded or
# negative-control files + 12 STANDING ladders** — and two of the five carry `SUPERSEDED`
# in their own filename.  The actionable population was never 117; it was 12, of which 5
# were real defects (fixed this pass), 3 were `COMMENT-ONLY`, 1 was a shell generator
# mis-graded as `SINGLE-SPELLING`, and the rest were already immune.
# 🔵 This is `p284` item 1's lesson in a second place: a corpus-wide count over an
# append-only archive measures HISTORY, not EXPOSURE, and a reader who acts on it rewrites
# frozen evidence to move a number.  The column is `standing`, so the two quantities can
# never again be read as one.
_SUPERSEDED = ("SUPERSEDED", "DEPRECATED", "negative-control")


def standing_dirs(root):
    """The `compose/code/<instrument>` dirs named by a recipe in the Makefile."""
    mk = pathlib.Path(root, "Makefile")
    if not mk.exists():
        return set()
    return set(re.findall(r"compose/code/[A-Za-z0-9_-]+", mk.read_text(encoding="utf-8")))


def standing_of(rel, live):
    if any(m in rel for m in _SUPERSEDED):
        return "SUPERSEDED"
    return "STANDING" if "/".join(rel.split("/")[:3]) in live else "HISTORICAL"


def audit(root):
    live = standing_dirs(root)
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
            rel = str(p.relative_to(root))
            rows.append((
                rel, fam, classify(toks, text),
                "UPPER-EXT" if upper_ext else "no-upper-ext",
                standing_of(rel, live),
                " ".join(sorted(toks)),
            ))
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    ap.add_argument("--out")
    ap.add_argument("--family")
    ap.add_argument("--standing", help="restrict to STANDING / HISTORICAL / SUPERSEDED")
    a = ap.parse_args()
    rows = audit(pathlib.Path(a.root).resolve())
    if a.family:
        rows = [r for r in rows if r[1] == a.family]
    if a.standing:
        rows = [r for r in rows if r[4] == a.standing]
    lines = ["instrument\tfamily\tverdict\tupper_ext\tstanding\tspellings"] + ["\t".join(r) for r in rows]
    if a.out:
        pathlib.Path(a.out).write_text("\n".join(lines) + "\n", encoding="utf-8")
    tally, standing_tally = {}, {}
    for r in rows:
        tally[r[2]] = tally.get(r[2], 0) + 1
        if r[4] == "STANDING":
            standing_tally[r[2]] = standing_tally.get(r[2], 0) + 1
    # 🟢 p286: only a STANDING defect is printed as an actionable row.  A historical
    # one-off's ladder cannot produce a false absence again — it has already run.
    for r in rows:
        if r[2] in ("STEM-ONLY", "CASE-UNVARIED") and r[4] == "STANDING":
            print("\t".join(r))
    print("# ALL       " + "  ".join(f"{k}={v}" for k, v in sorted(tally.items())))
    print("# STANDING  " + "  ".join(f"{k}={v}" for k, v in sorted(standing_tally.items())))
    print(f"# ladders={len(rows)} instruments={len({r[0] for r in rows})} "
          f"standing={sum(standing_tally.values())}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
