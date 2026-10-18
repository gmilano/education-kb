#!/usr/bin/env python3
"""Controls for p283's ladder-case audit.

🔵 C5 and C6 are the two overclaims the first draft of this instrument made on this
base's own corpus, kept as controls so a later pass cannot reintroduce them.
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from ladder_case import classify, spellings  # noqa: E402

FAILED = []


def run(name, toks, text, expect):
    got = classify(set(toks), text)
    ok = got == expect
    print(f"{'  ok  ' if ok else '  FAIL'} {name} (expected {expect}, got {got})")
    if not ok:
        FAILED.append(name)


# C1 — P1057's own finding: the ladder that varies the EXTENSION's case is closed.
run("C1 LICENSE.txt + LICENSE.TXT is closed",
    ["LICENSE.txt", "LICENSE.TXT"], 'p = ["LICENSE.txt", "LICENSE.TXT"]', "CASE-CLOSED")

# C2 — p282's defect: four rungs, stem case varied, extension spelled one way.
run("C2 README/readme.md with no uppercase ext is STEM-ONLY",
    ["README", "README.md", "readme.md", "README.rst"],
    'p = ["README", "README.md", "readme.md", "README.rst"]', "STEM-ONLY")

# C3 — a multi-rung ladder with no case variation at all is not a "single spelling".
# 🔴 The first draft called this SINGLE-SPELLING, which reads as "the author only
# thought of one name" when in fact they thought of four and cased them all alike.
run("C3 four rungs, no case variation, is CASE-UNVARIED",
    ["README", "README.md", "README.rst", "README.txt"],
    'p = ["README", "README.md", "README.rst", "README.txt"]', "CASE-UNVARIED")

run("C4 one rung is SINGLE-SPELLING", ["LICENSE"], 'p = "LICENSE"', "SINGLE-SPELLING")

# C5 — THE OVERCLAIM, control 1.  A `.lower()` far from the path vocabulary is not
# evidence that the PATH is folded.  The first draft returned CASE-INSENSITIVE for
# 316 of 580 ladders on this basis.
run("C5 a distant .lower() does not confer immunity",
    ["README.md"],
    'name = row.split()[0].lower()\n' + "\n" * 10 + 'p = "README.md"', "SINGLE-SPELLING")

# C6 — and the converse: a fold BESIDE the path vocabulary is a real screen hit.
run("C6 a fold beside the path is FOLD-ON-PATH",
    ["README.md"], 'for f in tree:\n    if f.lower() == "README.md".lower(): hit(f)',
    "FOLD-ON-PATH")

# C7 — enumeration beats every ladder: p275's "a path ladder cannot prove absence".
run("C7 ls-tree beside the path is TREE-ENUMERATED",
    ["LICENSE", "LICENSE.md"],
    'out = git("ls-tree", "-r", head)\nfor p in ("LICENSE", "LICENSE.md"): check(p)',
    "TREE-ENUMERATED")

# C8 — the extractor must find bare (unquoted) shell vocabulary, not just literals.
got = {t for _, t in spellings("for f in README README.MD LICENSE.TXT; do curl $f; done")}
ok = {"README", "README.MD", "LICENSE.TXT"} <= got
print(f"{'  ok  ' if ok else '  FAIL'} C8 bare shell path vocabulary is extracted (got {sorted(got)})")
if not ok:
    FAILED.append("C8")

# C9 — a family must not swallow a different family's token.
got = {f for f, _ in spellings('p = ["LICENSE.md", "README.md", "NOTICE", "COPYING"]')}
ok = got == {"licence", "readme", "notice", "copying"}
print(f"{'  ok  ' if ok else '  FAIL'} C9 families are kept apart (got {sorted(got)})")
if not ok:
    FAILED.append("C9")

# C10 — NEGATIVE CONTROL: a file with no path vocabulary yields no ladder at all.
got = spellings("def add(a, b):\n    return a + b\n")
print(f"{'  ok  ' if not got else '  FAIL'} C10 negative control: no vocabulary, no ladder")
if got:
    FAILED.append("C10")

# C11-C13 — p284: a GENERATOR is graded on what it generates, not on its literals.
run("C11 a cross-product generator is GENERATED-CASE-VARIED",
    ["notice", "NOTICE"],
    'STEMS = ("license", "notice")\n'
    'def _casings(word): return (word.upper(), word.capitalize(), word.lower())\n'
    'for ext in EXTS:\n  for stem_case in _casings(stem):\n'
    '    for ext_case in ({ext, ext.upper()} if ext else {""}): p = f"{stem_case}{ext_case}"',
    "GENERATED-CASE-VARIED")

# 🔴 The predicate must need BOTH halves.  An extension-case loop with no stem-case helper
# is not a closed generator, and grading it as one would be the same overclaim one layer in.
# 🔵 The fold idiom is held AWAY from the path vocabulary in both fixtures (the same
# 10-line separation C5 uses), because a fold sitting BESIDE the path is a legitimate
# `FOLD-ON-PATH` hit under C6 and would mask the property under test.  The first draft of
# these two controls put them on adjacent lines and read `FOLD-ON-PATH`, so the fixture was
# testing C6 over again rather than the generator predicate.
run("C12 an EXTENSION-case idiom alone is not a generator",
    ["README", "README.md"],
    'for ext_case in {ext, ext.upper()}: q = stem + ext_case\n' + "\n" * 10 +
    'paths = ["README", "README.md"]',
    "CASE-UNVARIED")
run("C13 a STEM-case helper alone is not a generator",
    ["README", "README.md", "readme.md"],
    'def _casings(word): return (word.upper(), word.lower())\n' + "\n" * 10 +
    'paths = ["README", "README.md", "readme.md"]',
    "STEM-ONLY")

# ── p286's three instrument changes, each with a NEGATIVE ARM ──────────────────────────
# 🔵 p284's lesson applied to controls, not just to bounds: a predicate asserted only in
# the direction it is supposed to fire can be satisfied by a predicate that fires always.

# C15/C16/C17 — COMMENT-ONLY.  The positive arm is `lib/license_family.sh`'s real shape:
# the only `copying` token in the file is a byte-offset note in a `#` comment.
run("C15 vocabulary only in a # comment is COMMENT-ONLY",
    ["COPYING"], '#  - GPL-3.0 seccion 13, moodle/COPYING  byte 28.272\nreturn 1', "COMMENT-ONLY")
run("C16 NEGATIVE ARM: the same vocabulary in CODE is not COMMENT-ONLY",
    ["COPYING"], 'for f in COPYING; do curl $f; done', "SINGLE-SPELLING")
run("C17 vocabulary only in a docstring is COMMENT-ONLY",
    ["COPYING"], '"""The ladder carried LICENSE.md and COPYING."""\nx = 1', "COMMENT-ONLY")

# C18/C19/C20 — the SHELL cross product, `p207-permissive-half-audit/locate.sh`'s shape.
_SH_GEN = ('for b in LICENSE License license COPYING Copying copying; do\n'
           '  for e in "" .txt .TXT .md .MD; do printf \'%s%s\\n\' "$b" "$e"; done\ndone')
run("C18 a shell stem x extension cross product is GENERATED-CASE-VARIED",
    ["COPYING", "Copying", "copying"], _SH_GEN, "GENERATED-CASE-VARIED")
run("C19 NEGATIVE ARM: a shell ext list with NO case variation is not a generator",
    ["COPYING", "Copying", "copying"],
    'for b in COPYING Copying copying; do\n  for e in "" .txt .md; do echo "$b$e"; done\ndone',
    "STEM-ONLY")
run("C20 NEGATIVE ARM: ext case varied but stems NOT is not a generator",
    ["COPYING"],
    'for b in COPYING; do\n  for e in .txt .TXT; do echo "$b$e"; done\ndone', "SINGLE-SPELLING")

# C21/C22 — a variable named `LICENCE` takes attribute access, and `BARE`'s optional
# `.ext` ate it: `p124-correction-form-marker` was graded on `LICENCE.findall`.
_attr = {t for _, t in spellings('LICENCE = re.compile(r"x")\nLICENCE.findall(s)\nLICENCE.pattern')}
ok = _attr == {"LICENCE"}
print(f"{'  ok  ' if ok else '  FAIL'} C21 a method attribute is not a path spelling (got {sorted(_attr)})")
if not ok:
    FAILED.append("C21")
_real = {t for _, t in spellings('p = ["LICENCE.txt", "LICENCE.md"]')}
ok = _real == {"LICENCE.txt", "LICENCE.md"}
print(f"{'  ok  ' if ok else '  FAIL'} C22 NEGATIVE ARM: a real extension is still a spelling (got {sorted(_real)})")
if not ok:
    FAILED.append("C22")

# C23/C24 — the regex ALTERNATION context, and the phrase that must stay out of it.
_alt = {t for _, t in spellings(r'RX = r"(?:COPYING|copying|Copying|NOTICE)"')}
ok = {"COPYING", "copying", "Copying", "NOTICE"} <= _alt
print(f"{'  ok  ' if ok else '  FAIL'} C23 an exact-word alternation yields case variants (got {sorted(_alt)})")
if not ok:
    FAILED.append("C23")
# 🔴 This is the control that rejects p286's own first attempt (`re.I` on BARE), which
# imported `general public license` from a title regex as licence-path vocabulary.
_phrase = {t for _, t in spellings(r"TITLE='^(gnu (affero |lesser )?general public license)$'")}
ok = not _phrase
print(f"{'  ok  ' if ok else '  FAIL'} C24 NEGATIVE ARM: a body-text phrase yields no spelling (got {sorted(_phrase)})")
if not ok:
    FAILED.append("C24")

# C25 — grade on what the CODE carries.  `p230-prose-path-ladder` had `COPYING` in a regex
# and `COPYING.txt` ONLY in its docstring, and was graded as a two-rung CASE-UNVARIED
# ladder on the strength of the prose rung.
run("C25 a rung that exists only in prose is not graded as a rung",
    ["COPYING", "COPYING.txt"],
    '"""...sat in the grantless class because COPYING.txt was not in the list."""\n'
    'for f in COPYING; do curl $f; done', "SINGLE-SPELLING")

# C14 — THE RATCHET, which is `p283`'s item 2.  `p283` produced these numbers and pinned
# none of them, so nothing stopped the next pass from regressing a ladder silently.
# 🔵 It is a RATCHET, not a pin, and that distinction is `p284` item 1's lesson carried
# across: an EXACT count goes red every time an instrument is added — which is how the
# `p252` census burned eight passes — while a FLOOR goes red only on an actual regression.
# Adding instruments can never break it; un-closing a ladder always will.
RATCHET = pathlib.Path(__file__).resolve().parent / "ratchet.tsv"
# ── p288's IMPORTED-LADDER arm (the third instance of p284's generator finding) ──────────
# 🔵 The real shape, from `p288-readme-channel/probe.sh`: the file spells NO rung of its own.
# Its single `readme`-family literal is the STATUS VALUE `NO-README` in its own output schema,
# and the ladder it actually walks is read out of `readme_claim.README_PATHS`, which this
# audit grades CASE-CLOSED in its own right.  Graded on literals that is SINGLE-SPELLING — a
# one-rung ladder that cannot prove an absence.  Graded on what it walks, it is closed.
run("C29 one literal plus an imported ladder is IMPORTED-LADDER",
    ["README"],
    'PATHS=$(python3 -c "import readme_claim;print(readme_claim.README_PATHS)")\n'
    'printf "%s\\tNO-README\\n" "$slug"',
    "IMPORTED-LADDER")

# C30 — 🔴 THE OVERCLAIM GUARD.  A file that imports a ladder AND spells rungs of its own
# keeps its LITERAL grade; importing must not launder a hand-spelled stem-only ladder.
run("C30 import plus own rungs keeps the literal grade",
    ["README", "README.md", "readme.md"],
    'import readme_claim\nextra = ["README", "README.md", "readme.md"]\n'
    'both = readme_claim.README_PATHS + extra',
    "STEM-ONLY")

# C31 — the identifier must belong to THIS family.  A one-rung `copying` ladder beside an
# imported README ladder is still SINGLE-SPELLING.
run("C31 a foreign identifier does not grade this family",
    ["COPYING"],
    'import readme_claim\np = readme_claim.README_PATHS\nif n == "COPYING": pass',
    "SINGLE-SPELLING")

# C32 — a LOCAL assignment is not an import: the ladder must come from a module reference,
# or every one-rung ladder could immunise itself by naming its own variable well.
run("C32 a local assignment is not an imported ladder",
    ["README"], 'README_PATHS = ["README"]\nprint("NO-README")', "SINGLE-SPELLING")

import ladder_case as _lc  # noqa: E402

_rows = _lc.audit(str(pathlib.Path(__file__).resolve().parents[3]))
_counts = {}
for _r in _rows:
    _counts[_r[2]] = _counts.get(_r[2], 0) + 1
    # 🟢 p286: `STANDING:<verdict>` keys bind only the ladders `make hooks` actually
    # invokes.  A ceiling on the ALL population goes red when an instrument is ADDED,
    # which is the p252 shape this ratchet exists to avoid.
    if _r[4] == "STANDING":
        _k = "STANDING:" + _r[2]
        _counts[_k] = _counts.get(_k, 0) + 1
# direction: MIN = must not fall below (good things); MAX = must not rise above (defects).
_BOUNDS = {}
if RATCHET.exists():
    # 🔴 p286: the header skip was pinned to line 0, so the first `#` comment line added
    # to the ratchet moved the header down and the parser tried `int("bound")`.  A file
    # format that cannot carry a comment cannot carry the reason for its own numbers.
    for _ln in RATCHET.read_text(encoding="utf-8").splitlines():
        if not _ln.strip() or _ln.lstrip().startswith("#"):
            continue
        _p = _ln.split("\t")
        if _p[0] == "verdict":
            continue
        if len(_p) >= 3:
            _BOUNDS[_p[0]] = (_p[1], int(_p[2]))
if not _BOUNDS:
    print("  FAIL C14 ratchet.tsv is missing or empty — a ratchet nobody wrote is not a ratchet")
    FAILED.append("C14")
else:
    _bad = []
    for _v, (_dir, _bound) in sorted(_BOUNDS.items()):
        _got = _counts.get(_v, 0)
        if _dir == "MIN" and _got < _bound:
            _bad.append(f"{_v} fell to {_got}, floor {_bound}")
        if _dir == "MAX" and _got > _bound:
            _bad.append(f"{_v} rose to {_got}, ceiling {_bound}")
    if _bad:
        print("  FAIL C14 the ladder ratchet regressed: " + "; ".join(_bad))
        FAILED.append("C14")
    else:
        print(f"  ok   C14 the ladder ratchet holds ({len(_BOUNDS)} bounds)")

print(f"\n{25 - len(FAILED)}/25 controls pass")
sys.exit(1 if FAILED else 0)
