"""`ACTION ZZ-ap` — the PER-SUBTREE grant classifier.  Registered at p377 and carried
unbuilt through p378, p379, p380 and p381; ranked FIRST by p381 with three live fixtures.

🔴 THE DEFECT IT CLOSES, in p381's own words: *"A classifier that reads the root `LICENSE`
and stops is right about the code and wrong about the repository — and that is this base's
entire ladder."*  Every grant instrument on this base answers ONE licence id for ONE
repository.  A repository whose root grant covers only PART of its tree is therefore recorded
as permissive when it is not, and `agents/top.md`'s licence column is the thing a Globant
engagement reads before building.

🟢 WHAT IS NEW HERE, and why it is not a fourth normaliser.  `p307` answers GRANT / POINTER /
RESERVED for a payload.  `p348-grant-scope` answers a SCOPE and a PROVENANCE.  Neither
answers *"which SUBTREES does this grant reach, and which does it leave ungranted?"*  This
instrument answers only that, and it returns the subtree PATHS the payload itself names.

🔵 THE THREE FIXTURES ARE THREE DIFFERENT MECHANISMS, which is why one rule cannot catch them
and why p381's `Pattern 37` (read the README too) is an interim and not a fix:

  A. `DECLARED-SPLIT`         `oaknational/oak-curriculum-ontology`, `main/LICENSE.md`, 1 867 B
     The payload names its own parts: OGL-3.0 over `ontology/`, `data/`, `docs/`; MIT over
     `scripts/`, `.github/workflows/`, `pyproject.toml`.  Two grants, both real, disjoint.

  B. `STOCK-SCOPE-LIMITED`    `withmarbleapp/os-taxonomy`, `main/LICENSE`, 25 289 B
     🔴 The subtlest of the three, and the one no README check would find.  The payload is
     the UNMODIFIED stock ODbL text — and the stock text limits its own scope in its own
     preamble: *"the ODbL only governs the rights over the Database, and not the contents of
     the Database individually.  Licensors should use the ODbL together with another license
     for the contents."*  So a correct, unedited, recognised licence file can still leave the
     repository's actual payload ungranted, and nothing about the FILE looks unusual.

  C. `NARROWED-OPERATIVE`     `aaryansamanta/nextgen-ai`, `main/LICENSE`, 1 327 B
     The operative clause is edited by hand: MIT's *"a copy of this software and associated
     documentation files"* becomes *"a copy of the source code files in this repository"*,
     the title line is `MIT License (Code)`, and a trailing note excludes `website/img`,
     `website/video` and the top-level PDFs.  🔴 This payload does NOT fold to p378's MIT
     constant, which is how p381 caught it — but folding is a whole-text test, and a pass
     that reads only the title line sees `MIT`.

🟢 Deliberately SELF-CONTAINED: no sibling import.  `p355-cwd-portability` and the eleven-pass
history of `ACTION QO` say that a suite which needs its own directory on `sys.path` is a suite
that cannot be invoked from where a hook runs.  This module imports only the stdlib, so it
runs under `python3 -I` from any directory.
"""

import re

UNIFORM = "UNIFORM"
DECLARED_SPLIT = "DECLARED-SPLIT"
STOCK_SCOPE_LIMITED = "STOCK-SCOPE-LIMITED"
NARROWED_OPERATIVE = "NARROWED-OPERATIVE"

# 🟢 CLOSED list, in p378's style: every pattern below was observed first-hand on a payload
# these shelves carry, and is named with it.  A pattern added without a payload behind it is
# the band this instrument exists to retire.
_BACKTICK_PATH = re.compile(r"`([^`\n]+?)`")
_APPLIES_TO = re.compile(r"^#{0,6}\s*applies to\s*$", re.I | re.M)
_LICENCE_HEADING = re.compile(
    r"^#{1,6}\s*(?:part\s*\d+\s*[:\-–]\s*)?.*?"
    r"(MIT License|Open Government Licence|Apache License|BSD[ -]\d-Clause|"
    r"Creative Commons[A-Za-z0-9 .\-]*|ODbL|Open Database License|GNU [A-Z]+)",
    re.I | re.M)

# B. The stock texts that limit their own scope, with the clause that does it.
_STOCK_SCOPE_CLAUSES = (
    (r"only governs the rights over the Database,?\s*and not the\s*contents",
     "ODbL", "Database", "the Database's CONTENTS are not granted by this file"),
)

# C. MIT's operative object, and the edits observed in its place.
_MIT_CANONICAL_OBJECT = re.compile(
    r"obtaining a copy\s+of this software and associated documentation files",
    re.I)
_MIT_NARROWED_OBJECT = re.compile(
    r"obtaining a copy\s+of (?!this software and associated documentation files)([^(]{3,80}?)\s*\(the",
    re.I)
_TITLE_QUALIFIED = re.compile(r"^\s*(MIT License|Apache License|BSD[ -]\d-Clause)\s*\(([^)]+)\)",
                              re.I | re.M)
_EXCLUSION_NOTE = re.compile(
    r"(?:applies to the [a-z ]+ only|are not covered by|remain[s]? ©|not covered by the)",
    re.I)


def _licence_ids(text):
    """Every licence name that appears as a HEADING.  Order-preserving, de-duplicated."""
    out = []
    for m in _LICENCE_HEADING.finditer(text):
        name = m.group(1).strip()
        if name.lower() not in [o.lower() for o in out]:
            out.append(name)
    return out


def _sections(text):
    """Split on markdown headings that name a licence, keeping each heading with its body."""
    marks = [(m.start(), m.group(1).strip()) for m in _LICENCE_HEADING.finditer(text)]
    out = []
    for i, (pos, name) in enumerate(marks):
        end = marks[i + 1][0] if i + 1 < len(marks) else len(text)
        out.append((name, text[pos:end]))
    return out


def _paths_in(block):
    """Backticked tokens that look like PATHS, not prose.  A path has a `/` or an extension."""
    out = []
    for raw in _BACKTICK_PATH.findall(block):
        tok = raw.strip()
        if not tok or " " in tok.strip("/"):
            continue
        if "/" in tok or re.search(r"\.[A-Za-z0-9]{1,6}$", tok):
            if tok not in out:
                out.append(tok)
    return out


def root_only_verdict(text):
    """🔴 The NAIVE read this base has used everywhere: the first licence name wins.

    Kept in this module ON PURPOSE so a suite can show, rather than assert, that the
    per-subtree read contradicts it.
    """
    ids = _licence_ids(text)
    if ids:
        return ids[0]
    first = next((l.strip() for l in text.splitlines() if l.strip()), "")
    m = _TITLE_QUALIFIED.match(first)
    if m:
        return m.group(1).strip()
    for name in ("MIT License", "Apache License", "ODbL", "Open Database License"):
        if first.lower().startswith(name.lower()):
            return name
    return "UNKNOWN"


def classify(text):
    """The per-subtree verdict.

    Returns a dict:
      form        one of the four constants
      grants      [(licence_id, (path, ...), basis)]  -- paths the PAYLOAD names
      exclusions  [(path_or_class, reason)]
      contradicts_root_only  True when a root-LICENSE-only read mis-describes the repository
      notes       human-readable, one per rule that fired
    """
    grants, exclusions, notes = [], [], []
    form = UNIFORM

    # ---- A. a declared split: >=2 licence headings AND an "Applies to" list of paths
    secs = _sections(text)
    if len(secs) >= 2 and _APPLIES_TO.search(text):
        for name, block in secs:
            paths = _paths_in(block)
            if paths:
                grants.append((name, tuple(paths), "payload names the subtree"))
        if len(grants) >= 2:
            form = DECLARED_SPLIT
            notes.append("payload declares %d grants over disjoint subtrees" % len(grants))

    # ---- B. a stock text that limits its own scope
    for pattern, lic, obj, why in _STOCK_SCOPE_CLAUSES:
        if re.search(pattern, text, re.I | re.S):
            form = STOCK_SCOPE_LIMITED
            grants = [(lic, (obj,), "stock text's own scope clause")]
            exclusions.append(("the Database's contents", why))
            notes.append("%s limits its own scope to the %s" % (lic, obj))
            break

    # ---- C. a hand-narrowed operative clause
    if form in (UNIFORM,):
        narrowed = _MIT_NARROWED_OBJECT.search(text)
        qualified = _TITLE_QUALIFIED.search(text)
        if narrowed and not _MIT_CANONICAL_OBJECT.search(text):
            obj = re.sub(r"\s+", " ", narrowed.group(1)).strip()
            form = NARROWED_OPERATIVE
            grants = [("MIT License", (obj,), "operative clause edited by hand")]
            notes.append("MIT's granted object is '%s', not the whole repository" % obj)
            if qualified:
                notes.append("title line is qualified: '%s (%s)'"
                             % (qualified.group(1), qualified.group(2)))
            for m in _EXCLUSION_NOTE.finditer(text):
                tail = text[m.start():m.start() + 400]
                paths = _paths_in(tail)
                exclusions.append((tuple(paths) if paths else "non-code content",
                                   re.sub(r"\s+", " ", tail[:120]).strip()))
                break

    if form == UNIFORM:
        lic = root_only_verdict(text)
        grants = [(lic, ("<whole repository>",), "single grant, no scope limit found")]

    contradicts = form != UNIFORM
    return {"form": form, "grants": grants, "exclusions": exclusions,
            "contradicts_root_only": contradicts, "notes": notes}


def covers(text, path):
    """Does the payload grant `path`?  -> (True|False|None, licence_id|reason).

    🔵 `None` means UNDEFINED rather than False: the payload names subtrees and this path is
    not among them, so the answer is *not stated*.  p381 lost a finding to exactly this
    confusion (`p351.classify()` returns None for a VALID address, and p381 read None as
    "not an address").  An undefined grant reported as False would read as a refusal.
    """
    v = classify(text)
    if v["form"] == UNIFORM:
        return True, v["grants"][0][0]
    for lic, paths, _ in v["grants"]:
        for p in paths:
            if p.startswith("<"):
                return True, lic
            if path == p.rstrip("/") or path.startswith(p.rstrip("/") + "/"):
                return True, lic
    for excl, why in v["exclusions"]:
        if isinstance(excl, tuple):
            for p in excl:
                if path == p.rstrip("/") or path.startswith(p.rstrip("/") + "/"):
                    return False, why
    return None, "payload names subtrees and does not name this one"
