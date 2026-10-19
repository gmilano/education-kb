#!/usr/bin/env python3
"""p309 — WHICH of this base's licence rungs actually fire on a real GPL-3.0 payload.

🔴 Why it exists, and it is not a hypothesis.  At `p309` the standing prober
`p306-licence-probe` graded FOUR payloads `AGPL-3.0` — every AGPL verdict in
its life — and TWO of them are GPL-3.0 by title:

    GatorEducator/gatorgrader    LICENSE.md  35 191 B  57756125771d  GNU GENERAL PUBLIC LICENSE
    five-plus-one/AI-Marker-Suite LICENSE    35 154 B  1ab858f515df  GNU GENERAL PUBLIC LICENSE
    sourcegrade/jagr             LICENSE     34 523 B  0d96a4ff68ad  GNU AFFERO GENERAL PUBLIC LICENSE
    ai-lingnan/econai-agent-platform LICENSE 34 523 B  0d96a4ff68ad  GNU AFFERO GENERAL PUBLIC LICENSE

The rung is `elif "affero" in low:`, ordered BEFORE `elif "gnu general public"`,
applied to the whole lowercased body.  GPL-3.0 names the Affero licence three
times — §13 is TITLED *"Use with the GNU Affero General Public License"* — so
no GPL-3.0 payload can ever reach the GPL rung.

🔴 **And the fix was already in this base.**  `p150-gpl-affero-discrimination`
refuted this exact test, named `p145`/`p147`/`p149` as its carriers, and shipped
`title_licence()` plus the §13 clause cross-check.  `p306` was written LATER and
RESTATED the refuted body test instead of importing the discriminator.  🔵 `p308`
learned "import the canonical list, never restate it" for SHELF DATA; nobody
applied it to the CLASSIFIERS, and this is what that costs.

🟢 What this instrument adds that reading the code does not: it does not GRADE a
rung by its shape.  It runs every affero-bearing literal in the tree against a
REAL GPL-3.0 payload and a REAL AGPL-3.0 payload, both pinned in `fixtures/`
with their byte lengths and `sha256_12` in the filename, and reports which
rungs fire on which.  A rung's shape is an argument; this is a measurement.

🔵 Why that distinction earns its keep: the obvious reading says a case-insensitive
match of `GNU AFFERO GENERAL PUBLIC LICENSE` is unsafe and a case-sensitive one is
safe.  Measured, that is right — and the SAME reading says
`gnu\\s+affero\\s+general\\s+public\\s+license[\\s,]*version\\s*3` is unsafe, while
measurement says it is SAFE, because GPL-3.0 §13 writes *"version 3 of the GNU
Affero General Public License"* with the version BEFORE the name.  Four files carry
that rung.  A census by shape would have condemned them.

    verdict                  meaning
    FIRES-ON-GPL3-EXACT      matches the GPL-3.0 payload case-SENSITIVELY — unsafe
                             however the caller compiles it
    FIRES-ON-GPL3-CASEFOLD   matches GPL-3.0 only under re.I / .lower() — unsafe
                             exactly when its caller casefolds, which is measured
                             separately per file
    AGPL-ONLY                matches the AGPL-3.0 payload and NEVER the GPL-3.0 one
    INERT                    matches neither payload (a token rung, a prose string)

A FILE is CONFIRMED-EXPOSED when it carries a GPL3-firing rung AND casefolds AND
does not import `p150`'s discriminator.  That conjunction, not any one of its
parts, is the defect `p309` measured in production.
"""
import ast
import io
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import fixtures as _fx  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
FIXTURES = os.path.join(HERE, "fixtures")

# The two payloads every rung is measured against.  Pinned by byte length in the
# name, probed first-hand at p309 over raw.githubusercontent.com.
# 🔵 Named by PREFIX through `fixtures.py`, never by filename: a lone capitalised
# filename literal is what `p283`'s ladder ratchet grades as a one-rung path
# ladder, and it is right to.
GPL3_FIXTURE = _fx.GPL3
AGPL3_FIXTURE = _fx.AGPL3

# p150 owns the discriminator.  A file that imports it is out of scope by
# construction — that is the remedy, not a suppression.
IMPORTS_DISCRIMINATOR = ("gpl_affero", "title_licence", "title_window")

CASEFOLDS = (".lower()", "re.I", "re.IGNORECASE", "IGNORECASE", ".casefold()")

# 🟢 The third conjunct, and without it 24 flags are wrong.  A rung applied to a
# TITLE WINDOW cannot see GPL-3.0 §13 at line 552 whatever its pattern says, and
# `p198-title-line-family` is an instrument built on exactly that discipline
# without importing `p150`.  🔵 A file-level marker cannot prove THIS rung runs
# inside the window — so a windowed ladder is reported as a READ, with a
# denominator, never as a finding.  That is `p308`'s census contract.
# 🔴 AND THE MARKERS MUST BE BILINGUAL.  The first draft's list was English-only
# and missed `p419-copyleft-identity`, which reads a title window through a helper
# named `_encabezado()` — so the census called a CORRECT instrument a misgrade.
# 🔵 `p471-gap-gate-language` recorded this exact failure for `p370-gap-gate`:
# half of this base's instruments are written in Spanish, and an English-only
# filter reads their discipline as its absence.  Measured, not inferred:
# `familia()` returns `('GPL-3.0', 'encabezado: GENERAL PUBLIC LICENSE + Version 3')`
# on the 35 191 B payload.
WINDOW_MARKERS = ("TITLE_WINDOW", "title_window", "title_line", "titleline",
                  "splitlines()[:", "lines[:", "first_lines", "head_lines",
                  "[:TITLE", "window_lines", "_window(",
                  "encabezado", "cabecera", "titulo", "primeras_lineas",
                  "lineas[:", "_titulo(")

# 🔴 A SECOND input kind, and it is not a suppression either.  `p222`'s `_family`
# and `p221`'s `_family_of` take a DECLARED TOKEN — `AGPL-3.0`, `GPL-3.0-or-later`
# out of a manifest — never a licence body.  Running a payload fixture through them
# is a category error, and grading them by a payload rung condemns a correct
# instrument.  Measured on tokens: `AGPL-3.0 -> AGPL`, `GPL-3.0 -> GPL`.
TOKEN_INPUT_MARKERS = ("def _family(tok", "def _family_of(tok", "parse_range",
                       "or-later", "OR-LATER", "spdx_token", "declared_token")

SKIP_DIR_PARTS = ("fixtures", "fixtures-pending", "__pycache__", ".git")


def load(prefix):
    return _fx.body(prefix)


# A label that is AGPL-SPECIFIC is the only one whose misfire is a defect.
# 🔴 THE INSTRUMENT'S OWN FIRST DRAFT got this wrong and flagged 36 of 54 files,
# because it graded a rung by WHETHER it fires on GPL-3.0 and never asked WHAT
# IT THEN CALLS IT.  Three classes of correct rung fire on GPL-3.0 by design:
#
#   1. THE DISCRIMINATOR ITSELF.  `p228-shelf-gate` carries
#      `13\.\s*Use\s+with\s+the\s+GNU\s+Affero` — a pattern whose whole purpose
#      is to fire on GPL-3.0 and prove the payload is NOT AGPL.  The first draft
#      called it exposed.
#   2. THE FAMILY MATCHER.  `p152-vertical-election` and `p221-licence-version-range`
#      match `GNU (Affero|Lesser|)General Public` and label the hit GPL-FAMILY.
#      Firing on GPL-3.0 is the correct answer.
#   3. THE GRANT DETECTOR.  `p1052-stale-absence` asks "is there any grant text
#      here at all"; GPL-3.0 is grant text.
#
# 🔵 So the defect is a CONJUNCTION of three measured facts, not one: the rung
# fires on a real GPL-3.0 payload, its caller casefolds, AND the label it
# assigns names AGPL in particular.  Any two of the three are not a finding.
AGPL_LABEL = re.compile(r"\bAGPL\b|\bAGPL-?3|affero\s+general\s+public", re.I)
# 🔴 `GPL-3\.0` matches INSIDE `AGPL-3.0`, so the first draft of this pattern graded
# every AGPL label as a GPL-family label and the verdict came back
# `AGPL-AMONG-FAMILY` for a file carrying nothing but an AGPL rung and an AGPL
# label.  A lookbehind for the A and the L is the whole fix, and the control that
# names it is `test_an_agpl_label_beside_an_agpl_rung_is_agpl_specific`.
# 🔵 Same shape as the defect this pass is about: a substring test standing in for
# an identity test.
FAMILY_LABEL = re.compile(r"GPL-FAMILY|COPYLEFT|GRANT|(?<![AL])GPL-[23]\.0|\bLGPL\b",
                          re.I)


def nearby_labels(tree, src_lines, lineno):
    """Every short string literal within two lines of `lineno`.

    A rung and the label it assigns sit together in this base's house style —
    `(pattern, "AGPL-3.0")` in a tuple, or `fam = "AGPL-3.0"` on the next line.
    Two lines is what that style spans, measured across the 54 files.
    """
    out = []
    for node in ast.walk(tree):
        if (isinstance(node, ast.Constant) and isinstance(node.value, str)
                and abs(getattr(node, "lineno", -99) - lineno) <= 2
                and len(node.value) <= 40):
            out.append(node.value)
    return out


# 🟢 Two more discriminations, both MEASURED rather than argued, and together they
# decide 31 of the first-run's 36 flags:
#
#   FAMILY-BY-PATTERN.  A rung that also matches a PLAIN GPL-3.0 title line — no
#   Affero anywhere — is a GPL-family or any-grant matcher, not an AGPL rung.
#   `GNU\s+(?:Affero|Lesser|)\s*General\s+Public` is the shape.  Tested against a
#   synthetic title, so the verdict needs no reading of the caller.
#
#   LADDER ORDER.  A file carrying BOTH an AGPL rung and a GPL rung is a ladder,
#   and whether it misgrades depends only on which rung is tried first.
#   🔵 `p150-grant-ladder-order` OWNS that question — this instrument measures the
#   line numbers and defers the verdict to it by name, because a second opinion on
#   a question another instrument already owns is the restatement disease this
#   whole pass is about.
PLAIN_GPL3_TITLE = ("                    GNU GENERAL PUBLIC LICENSE\n"
                    "                       Version 3, 29 June 2007\n")
PLAIN_GPL_RUNG = re.compile(r"GNU\s*(?:\\s\+)?GENERAL|gnu\s*(?:\\s\+)?general|"
                            r"GENERAL\s*(?:\\s\+)?PUBLIC|general\s*(?:\\s\+)?public",
                            re.I)


def gpl_rung_lines(all_literals):
    """Lines of this file's rungs that are NOT about Affero at all.

    🔴 The first draft of this function took the GRADED list, which holds only the
    AFFERO-bearing literals — so a plain GPL rung could never appear in it and
    EVERY ladder came back `LADDER-NO-GPL-RUNG`, 27 of them.  The scope was wrong,
    not the rule.  It reads every literal in the file now.
    """
    return [ln for ln, lit in all_literals
            if not re.search(r"affero", lit, re.I) and PLAIN_GPL_RUNG.search(lit)
            and len(lit) <= 200]


def label_class(labels, rung):
    """AGPL-SPECIFIC, FAMILY, or UNLABELLED."""
    # A rung that quotes GPL-3.0's own section 13 heading is the discriminator,
    # whatever sits beside it.
    if re.search(r"13\s*\\?\.?\s*(?:\\s\*)?Use\s*(?:\\s\+)?with", rung, re.I):
        return "DISCRIMINATOR"
    if fires(rung, PLAIN_GPL3_TITLE, re.I):
        return "FAMILY-BY-PATTERN"
    # A nearby literal that IS the rung is the pattern, not its label.
    agpl = [l for l in labels if l != rung and AGPL_LABEL.search(l)]
    fam = [l for l in labels if not AGPL_LABEL.search(l) and FAMILY_LABEL.search(l)]
    if agpl and not fam:
        return "AGPL-SPECIFIC"
    if agpl and fam:
        return "AGPL-AMONG-FAMILY"
    if fam:
        return "FAMILY"
    return "UNLABELLED"


def all_literals(src):
    """Every short string literal with its line, for the ladder-order question."""
    try:
        tree = ast.parse(src)
    except SyntaxError:
        return []
    return [(getattr(n, "lineno", 0), n.value) for n in ast.walk(tree)
            if isinstance(n, ast.Constant) and isinstance(n.value, str)]


def affero_literals(src):
    """Every string literal in `src` that names the Affero licence.

    Parsed with `ast`, not matched with a regex: a regex over source text cannot
    tell a literal from a comment, and this base has written the phrase in
    comments and docstrings far more often than in rungs.
    """
    try:
        tree = ast.parse(src)
    except SyntaxError:
        return None
    out = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            if re.search(r"affero", node.value, re.I):
                # A docstring is a Constant whose parent is a module/def body.
                out.append((getattr(node, "lineno", 0), node.value))
    return out


def is_prose(lit):
    """A docstring or comment-grade sentence is not a rung.

    The discriminator is length plus sentence punctuation: a rung is a phrase or
    a pattern, never a sentence.  Measured on this tree, every literal over 120
    chars that contains '. ' is explanatory text.
    """
    return len(lit) > 120 and ". " in lit


def fires(lit, body, flags=0):
    """Does `lit`, read as a pattern, match `body`?

    A literal that is not a valid regex is tested as a plain substring, which is
    how a caller that does `lit in body` would use it.
    """
    try:
        return re.search(lit, body, flags) is not None
    except re.error:
        hay = body.lower() if flags & re.I else body
        needle = lit.lower() if flags & re.I else lit
        return needle in hay


def grade_rung(lit, gpl3, agpl3):
    if fires(lit, gpl3, 0):
        return "FIRES-ON-GPL3-EXACT"
    if fires(lit, gpl3, re.I):
        return "FIRES-ON-GPL3-CASEFOLD"
    if fires(lit, agpl3, re.I):
        return "AGPL-ONLY"
    return "INERT"


def census(root):
    gpl3, agpl3 = load(GPL3_FIXTURE), load(AGPL3_FIXTURE)
    rows = []
    for dirpath, dirs, files in os.walk(root):
        if any(p in dirpath.split(os.sep) for p in SKIP_DIR_PARTS):
            continue
        for fn in sorted(files):
            if not fn.endswith(".py") or fn.startswith("test_"):
                continue
            path = os.path.join(dirpath, fn)
            rel = os.path.relpath(path, root)
            if "p309-affero-rung-census" in rel or "p150-gpl-affero" in rel:
                continue
            try:
                src = io.open(path, encoding="utf-8", errors="replace").read()
            except OSError:
                continue
            if not re.search(r"affero", src, re.I):
                continue
            lits = affero_literals(src)
            if lits is None:
                rows.append((rel, "UNPARSED", [], False, False, [], False))
                continue
            tree = ast.parse(src)
            lines = src.splitlines()
            graded = [(ln, lit, grade_rung(lit, gpl3, agpl3),
                       label_class(nearby_labels(tree, lines, ln), lit))
                      for ln, lit in lits if not is_prose(lit)]
            casefolds = any(c in src for c in CASEFOLDS)
            windowed = any(w in src for w in WINDOW_MARKERS)
            token_kind = any(t in src for t in TOKEN_INPUT_MARKERS)
            imports = any(i in src for i in IMPORTS_DISCRIMINATOR)
            rows.append((rel, "OK", graded, casefolds, imports,
                         all_literals(src), windowed or token_kind))
    return rows


def verdict(row):
    """The bucket.  `driving_rung(row)` returns the literal that produced it —
    🔴 the first report printed `worst[0]` instead, which showed `p228`'s §13
    DISCRIMINATOR beside a ladder verdict that a different rung in the same file
    had produced.  A report that names the wrong evidence is worse than none."""
    rel, state, graded, casefolds, imports, lits, windowed = row
    if imports:
        return "IMPORTS-DISCRIMINATOR"
    def gpl3_firing(g):
        if g[2] == "FIRES-ON-GPL3-EXACT":
            return True
        return g[2] == "FIRES-ON-GPL3-CASEFOLD" and casefolds
    firing = [g for g in graded if gpl3_firing(g)]
    agpl_specific = [g for g in firing if g[3] == "AGPL-SPECIFIC"]
    ladder = [g for g in firing if g[3] == "AGPL-AMONG-FAMILY"]
    ambiguous = [g for g in firing if g[3] == "UNLABELLED"]
    if agpl_specific:
        return ("MISGRADES-ONLY-IF-UNWINDOWED" if windowed
                else "MISGRADES-GPL3-AS-AGPL")
    if ladder:
        gpl_lines = gpl_rung_lines(lits)
        if gpl_lines and min(g[0] for g in ladder) < min(gpl_lines):
            return ("LADDER-AGPL-FIRST-WINDOWED" if windowed
                    else "LADDER-AGPL-RUNG-FIRST")
        if gpl_lines:
            return "LADDER-GPL-RUNG-FIRST"
        return "LADDER-NO-GPL-RUNG"
    if ambiguous:
        return "FIRES-BUT-LABEL-UNCLEAR"
    if firing:
        return "FIRES-BY-DESIGN"
    if [g for g in graded if g[2] == "FIRES-ON-GPL3-CASEFOLD"]:
        return "EXPOSED-IF-CASEFOLDED"
    if graded:
        return "SAFE"
    return "NO-RUNG"


def driving_rung(row, key):
    rel, state, graded, casefolds, imports, lits, windowed = row
    firing = [g for g in graded
              if g[2] == "FIRES-ON-GPL3-EXACT"
              or (g[2] == "FIRES-ON-GPL3-CASEFOLD" and casefolds)]
    if key.startswith("MISGRADES"):
        want = [g for g in firing if g[3] == "AGPL-SPECIFIC"]
    elif key.startswith("LADDER"):
        want = [g for g in firing if g[3] == "AGPL-AMONG-FAMILY"]
    else:
        want = firing
    return (want or firing or graded)[0]


def main(argv):
    root = argv[1] if len(argv) > 1 else os.path.join(HERE, "..")
    rows = census(root)
    buckets = {}
    for row in rows:
        buckets.setdefault(verdict(row), []).append(row)
    order = ["MISGRADES-GPL3-AS-AGPL", "LADDER-AGPL-RUNG-FIRST",
             "MISGRADES-ONLY-IF-UNWINDOWED", "LADDER-AGPL-FIRST-WINDOWED",
             "LADDER-NO-GPL-RUNG", "LADDER-GPL-RUNG-FIRST",
             "FIRES-BUT-LABEL-UNCLEAR",
             "FIRES-BY-DESIGN", "EXPOSED-IF-CASEFOLDED", "SAFE",
             "IMPORTS-DISCRIMINATOR", "NO-RUNG", "UNPARSED"]
    print("# p309 affero-rung census — every rung run against a REAL GPL-3.0 and a")
    print("# REAL AGPL-3.0 payload.  A rung's SHAPE is an argument; this is a measurement.")
    print("#   GPL-3.0  fixture %s" % GPL3_FIXTURE)
    print("#   AGPL-3.0 fixture %s" % AGPL3_FIXTURE)
    print("")
    for key in order:
        got = buckets.get(key, [])
        print("## %-22s %3d file(s)" % (key, len(got)))
        if key in ("MISGRADES-GPL3-AS-AGPL", "LADDER-AGPL-RUNG-FIRST",
                   "MISGRADES-ONLY-IF-UNWINDOWED", "LADDER-AGPL-FIRST-WINDOWED",
                   "LADDER-NO-GPL-RUNG", "FIRES-BUT-LABEL-UNCLEAR",
                   "EXPOSED-IF-CASEFOLDED"):
            for rel, state, graded, casefolds, imports, lits, windowed in got:
                drive = driving_rung((rel, state, graded, casefolds, imports,
                                      lits, windowed), key)
                ln, lit, grade, lab = drive
                print("   %-56s :%-5s %-22s label=%s" % (rel, ln, grade, lab))
                print("        %r" % (lit[:84],))
    print("")
    confirmed = len(buckets.get("MISGRADES-GPL3-AS-AGPL", []))
    print("# files=%d  MISGRADES-GPL3-AS-AGPL=%d  LADDER-AGPL-FIRST=%d  LADDER-NO-GPL-RUNG=%d"
          % (len(rows), confirmed, len(buckets.get("LADDER-AGPL-RUNG-FIRST", [])),
             len(buckets.get("LADDER-NO-GPL-RUNG", []))))
    print("#   WINDOWED-READS=%d (a read, not a finding)"
          % (len(buckets.get("LADDER-AGPL-FIRST-WINDOWED", []))
             + len(buckets.get("MISGRADES-ONLY-IF-UNWINDOWED", []))))
    print("#   LADDER-GPL-FIRST=%d  LABEL-UNCLEAR=%d  BY-DESIGN=%d  SAFE=%d  IMPORTS=%d"
          % (len(buckets.get("LADDER-GPL-RUNG-FIRST", [])),
             len(buckets.get("FIRES-BUT-LABEL-UNCLEAR", [])),
             len(buckets.get("FIRES-BY-DESIGN", [])),
             len(buckets.get("SAFE", [])), len(buckets.get("IMPORTS-DISCRIMINATOR", []))))
    print("# 🔵 LADDER-* verdicts defer to p150-grant-ladder-order, which owns rung order.")
    return confirmed


if __name__ == "__main__":
    sys.exit(0 if main(sys.argv) >= 0 else 1)
