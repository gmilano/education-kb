#!/usr/bin/env python3
"""p310 — the DYNAMIC arm, widened: every declared classifier, run on the four
families `p309`'s corpus did not contain.

🔵 `p309` settled the method and this file does not re-argue it: *where an
instrument can be executed, executing it is the only thing that settles
anything.*  What `p309` could not settle from inside its own corpus is what
`DEFECT=0` is a statement ABOUT — see `family_coverage.py`.

🔵 `ENTRY_POINTS` IS IMPORTED FROM `p309`, not restated.  That is this pass's
subject and refusing to copy the list is the one place it costs nothing to obey:
a classifier declared at `p309` and not here would be silently ungraded, which is
exactly how the CC rungs survived.

GRADING.  A classifier is `DEFECT` on a fixture when it names a family that is
not the fixture's canonical family AND the disagreement crosses a COMMERCIAL-USE
boundary or a copyleft boundary.  Three narrower outcomes are NOT defects and are
reported separately, because conflating them is how `p309`'s static screen
condemned 34 correct files out of 36:

  `COARSE`     the classifier returns a less precise but correct answer — `CC`
               for `CC-BY-NC-4.0`, `GPL` for `GPL-3.0`.  Honest imprecision.
  `ABSTAIN`    the classifier declines (`None`, `unknown`, `CC-UNVERSIONED`,
               `NO-GRANT-CLAUSE`).  🔵 An abstention is a DIFFERENT answer from a
               wrong one and `P250` is why: `UNKNOWN` is indistinguishable from
               *"commercial use is PROHIBITED"*, so an abstention on a
               noncommercial payload is a REPORTED RISK, not a realised one.
  `OUT-OF-DOMAIN`  the classifier is a declared-token grammar, not a payload
               reader (`p221`, `p222`), or answers a different question
               (`p129/holder.py` reads the HOLDER).  Grading those on a payload
               condemned two correct instruments at `p309`.
"""
import importlib.util
import io
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
CODE = os.path.normpath(os.path.join(HERE, ".."))


def _load_module(name, path, extra_path=None):
    """Load a file as `name`, with stdout muted and an optional sys.path entry.

    🔴 `name` is NEVER the bare module name here, and that is not fastidiousness.
    Importing `p309`'s arm the obvious way — put this directory on `sys.path`,
    `import fixtures`, then exec `p309/run_classifiers.py` — makes `p309`'s own
    `import fixtures` resolve to THIS instrument's `fixtures.py`, already in
    `sys.modules`, and the arm dies on `module 'fixtures' has no attribute
    'GPL3'`. 🔵 That is `p150-identifier-collision` exactly, met while obeying
    `p309`'s own rule to import the list instead of copying it: **two
    instruments, one plausible module name, first loader wins.** Every load here
    is therefore namespaced by its pass, and `extra_path` is removed again.
    """
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    if extra_path:
        sys.path.insert(0, extra_path)
    sink, sys.stdout = sys.stdout, io.StringIO()
    try:
        spec.loader.exec_module(mod)
    finally:
        sys.stdout = sink
        if extra_path and extra_path in sys.path:
            sys.path.remove(extra_path)
    return mod


_fx = _load_module("p310_fixtures", os.path.join(HERE, "fixtures.py"), HERE)

# 🔵 The licence-token grammar, IMPORTED from this instrument's census arm, so a
# family the base starts publishing becomes gradeable here without an edit.
_cov = _load_module("p310_coverage", os.path.join(HERE, "family_coverage.py"), HERE)
_FAMILY_CLAIM = __import__("re").compile(
    "|".join("(?:%s)" % rx for _fam, rx in _cov.TOKENS), __import__("re").I)

# 🔵 IMPORTED. The list lives at p309 and is read from there.
_P309 = os.path.join(CODE, "p309-affero-rung-census")
_p309_arm = _load_module("p310_p309_arm",
                         os.path.join(_P309, "run_classifiers.py"), _P309)
ENTRY_POINTS = list(_p309_arm.ENTRY_POINTS)

# Instruments that do not answer "which family is this payload?".  Declared, with
# the reason, because an undeclared exclusion is a suppression.
OUT_OF_DOMAIN = {
    "p129-transcription-audit/holder.py":
        "reads the copyright HOLDER, not the family (p129's own subject)",
}

# The canonical CC oracle. 🔵 `p124-correction-form-marker/cc_version.py` already
# solved this family 186 passes ago — *"ZERO is NOT consulted here ... CC0 is
# reachable by channel 1 and 2 only, on purpose"* — and is the module every CC
# rung on this base should delegate to.
def _cc_oracle():
    path = os.path.join(CODE, "p124-correction-form-marker", "cc_version.py")
    spec = importlib.util.spec_from_file_location("cc_version", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.resolve


# 🔴 THE FIRST BUILD OF THIS FILE CONDEMNED SIX CORRECT INSTRUMENTS, and it did
# it in `p309`'s exact way — `p309` recorded *"grading them with a payload fixture
# condemned two correct instruments"* and this grader then read every house
# spelling of *"I decline"* as a wrong answer: `p419` returned `unclassified` on
# all four fixtures and was reported `DEFECT` ×4, `p211` returned `unrecognised`,
# `p228` returned `no recognised licence title`, `p198` returned `no-family`.
# 🔵 Half this base's instruments are Spanish and none of them share a sentinel,
# so an abstention vocabulary assembled by guesswork is a defect generator. Every
# token below was READ OFF a live classifier's output on these four payloads.
ABSTENTIONS = {"", "-", "unknown", "none", "no-grant-clause", "cc-unversioned",
               "not-cc", "undecidable-body", "reserved-no-grant", "no_payload",
               "unclassified", "unclasificado", "unrecognised", "unrecognized",
               "no recognised licence title", "no recognized license title",
               "no-family", "sin-familia", "sin familia", "indeterminado"}

# A family answer that is a correct PREFIX of the canonical one is COARSE, not
# wrong. Spelled as an explicit map rather than string-prefix logic, because
# `GPL-3.0` is a prefix of nothing and `CC` is a prefix of `CC0-1.0` too.
COARSE = {
    "CC-BY-NC-4.0": {"cc", "cc-other", "cc-by-nc", "cc-nc", "cc-by-nc-unversioned"},
    # 🟢 `permissive-software` for CC-BY-4.0 is `p191`'s own axis answering its own
    # question, and it is RIGHT in effect: CC-BY carries an attribution condition
    # and no commercial restriction. It is coarse, not wrong.
    "CC-BY-4.0": {"cc", "cc-other", "cc-by", "cc-by-unversioned",
                  "permissive-software", "content-permissive"},
    "PolyForm-Noncommercial-1.0.0": {"polyform", "noncommercial",
                                     "noncommercial-not-osi", "source-available"},
    "proprietary": {"reserved", "all-rights-reserved", "noncommercial-not-osi"},
    # 🔴 ADDED AT p311. This map was written for the five families `p310` pinned,
    # and `p311` pinned three more — at which point `p191`'s `permissive-software`,
    # already declared COARSE for `CC-BY-4.0` five lines above, graded as a DEFECT
    # on MIT and Apache-2.0 for no reason but absence from this dict.
    # 🔵 This file's own docstring warns that an abstention vocabulary assembled
    # by guesswork is a defect generator. A COARSE vocabulary that does not grow
    # with the corpus is the same instrument failing the same way: it would have
    # condemned `p191` four times across the two MOST-published families on this
    # base. The grade belongs to the ANSWER, not to the fixture set's age.
    "MIT": {"permissive-software", "permissive", "mit-0"},
    "Apache-2.0": {"permissive-software", "permissive", "apache"},
    "BSD-2-Clause": {"permissive-software", "permissive", "bsd", "bsd-2",
                     "bsd-unversioned"},
    "BSD-3-Clause": {"permissive-software", "permissive", "bsd", "bsd-3",
                     "bsd-unversioned"},
}

# A wrong answer that CROSSES a commercial-use boundary. This is the grade that
# matters: it is the set of families a studio may ship.
PERMISSIVE = {"cc0-1.0", "mit", "apache-2.0", "bsd", "bsd-3-clause", "bsd-2-clause",
              "0bsd", "isc", "unlicense", "cc-by-4.0", "cc-by-sa-4.0", "mpl-2.0",
              "epl-2.0", "ecl-2.0", "gpl-3.0", "gpl-2.0", "gpl", "lgpl",
              "lgpl-3.0", "agpl-3.0"}


def _load(relpath):
    path = os.path.join(CODE, relpath)
    name = "p310_" + relpath.replace("/", "_").replace(".py", "").replace("-", "_")
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    here = os.path.dirname(path)
    sys.path.insert(0, here)
    sink, sys.stdout = sys.stdout, io.StringIO()
    try:
        spec.loader.exec_module(mod)
    finally:
        sys.stdout = sink
        sys.path.remove(here)
    return mod


# 🔵 A VERDICT is not a FAMILY. These instruments return `(verdict, family)` —
# `P250`'s two columns — and a flattener that takes the first non-empty element
# grades the grant axis against the family axis. Declared, because `p306` gained
# `GRANT-NONCOMMERCIAL`, `POINTER` and `POINTER-NONCOMMERCIAL` at p310 and the
# first build of this grader read `grant-noncommercial` as that row's family and
# reported ABSTAIN where the answer was exactly right.
VERDICT_TOKENS = {"grant", "grant-noncommercial", "pointer",
                  "pointer-noncommercial", "copyleft-software",
                  "content-permissive", "permissive", "own-grant-at-root"}


def _answer(value):
    """Flatten a classifier's return into a comparable lowercase FAMILY token."""
    if value is None:
        return ""
    if isinstance(value, (tuple, list)):
        parts = [str(v) for v in value if v is not None]
        for p in parts:
            low = p.lower()
            if low in VERDICT_TOKENS:
                continue
            if low not in ABSTENTIONS and any(c.isalpha() for c in low):
                return low
        # Nothing but verdicts and abstentions: report the verdict, so a row that
        # says only `GRANT-NONCOMMERCIAL` is graded on the axis it did answer.
        for p in parts:
            if p.lower() in VERDICT_TOKENS:
                return p.lower()
        return parts[-1].lower() if parts else ""
    if isinstance(value, dict):
        for key in ("family", "familia", "licence", "license"):
            if key in value:
                return str(value[key]).lower()
        return str(value).lower()
    return str(value).lower()


def _names_a_family(got):
    """Does this answer NAME a licence family at all?

    🔴 THE SECOND BUILD OF THIS GRADER STILL CONDEMNED `p419`, four times, and the
    reason is the one lesson this base keeps paying for. `p419` does not return a
    token; it returns a SENTENCE — *«el encabezado no nombra una familia — tratar
    como no-osi (`p412`)»* — which is an abstention WITH THE SAFE ADVICE ATTACHED,
    and on these four payloads it is the soundest answer any of the nine gives.
    A longer `ABSTENTIONS` list does not fix that: I had already guessed
    `sin-familia` and guessed wrong, which is the same defect as the `p306` rung
    under audit — a vocabulary asserted instead of read.

    🟢 So the default is INVERTED and the test is grammatical: an answer counts as
    a family CLAIM only if it matches the licence-token grammar this base
    publishes, IMPORTED from `family_coverage.TOKENS`. Anything else — a sentence,
    a house sentinel in any language, an empty string — is an abstention. 🔵 An
    instrument is then condemned only for naming a family, which is the only thing
    a classifier can be wrong about.
    """
    return _FAMILY_CLAIM.search(got) is not None


def grade(canonical, got):
    got = got.strip().lower()
    canon = canonical.lower()
    if got in ABSTENTIONS or not got:
        return "ABSTAIN"
    if got == canon:
        return "CORRECT"
    if got in COARSE.get(canonical, set()):
        return "COARSE"
    if not _names_a_family(got):
        return "ABSTAIN"
    if got in PERMISSIVE and canonical in ("CC-BY-NC-4.0",
                                           "PolyForm-Noncommercial-1.0.0",
                                           "proprietary"):
        return "DEFECT-COMMERCIAL"
    if got in PERMISSIVE and canon not in PERMISSIVE:
        return "DEFECT-COMMERCIAL"
    return "DEFECT"


def main():
    cc_resolve = _cc_oracle()
    rows = _fx.declared()

    print("# p310 dynamic arm — every classifier p309 declares, run on the %d"
          % len(rows))
    print("# families p309's corpus did not contain.")
    for name, fam, com, _why, _text, n, sha in rows:
        print("#   %-50s %-30s %-11s %6d B  %s" % (name, fam, com, n, sha))
    print()
    print("# 🟢 the canonical CC oracle, for reference — p124/cc_version.resolve():")
    for name, fam, _com, _why, text, _n, _sha in rows:
        print("#   %-50s %-14s -> %s" % (name, fam, cc_resolve(text) or "NOT-CC"))
    print()

    tally = {}
    defects = []
    for relpath, callable_name in ENTRY_POINTS:
        label = "%s:%s" % (relpath, callable_name)
        if relpath in OUT_OF_DOMAIN:
            print("   %-52s ⚪ OUT-OF-DOMAIN  %s" % (relpath, OUT_OF_DOMAIN[relpath]))
            tally["OUT-OF-DOMAIN"] = tally.get("OUT-OF-DOMAIN", 0) + 1
            continue
        try:
            mod = _load(relpath)
            fn = getattr(mod, callable_name)
        except Exception as exc:                        # noqa: BLE001
            print("   %-52s 🔴 UNRUNNABLE     %s: %s"
                  % (relpath, type(exc).__name__, str(exc)[:60]))
            tally["UNRUNNABLE"] = tally.get("UNRUNNABLE", 0) + 1
            continue
        verdicts = []
        for _name, fam, _com, _why, text, _n, _sha in rows:
            try:
                got = _answer(fn(text))
            except Exception as exc:                    # noqa: BLE001
                got, g = "raise:%s" % type(exc).__name__, "UNRUNNABLE"
            else:
                g = grade(fam, got)
            verdicts.append((fam, got, g))
            if g.startswith("DEFECT"):
                defects.append((label, fam, got, g))
        worst = ("DEFECT-COMMERCIAL" if any(g == "DEFECT-COMMERCIAL" for _f, _g2, g in verdicts)
                 else "DEFECT" if any(g == "DEFECT" for _f, _g2, g in verdicts)
                 else "ABSTAIN" if any(g == "ABSTAIN" for _f, _g2, g in verdicts)
                 else "COARSE" if any(g == "COARSE" for _f, _g2, g in verdicts)
                 else "CORRECT")
        icon = {"CORRECT": "🟢", "COARSE": "🟢", "ABSTAIN": "🟡",
                "DEFECT": "🔴", "DEFECT-COMMERCIAL": "🔴"}[worst]
        tally[worst] = tally.get(worst, 0) + 1
        # 🔵 The row prints its DISTRIBUTION, not only its worst grade. `p306`
        # after this pass's fix is right on three families and abstains on the
        # fourth; a bare `ABSTAIN` would hide the three and read as a regression.
        per = {}
        for _f, _g2, g in verdicts:
            per[g] = per.get(g, 0) + 1
        shape = " ".join("%s=%d" % (k, v) for k, v in sorted(per.items()))
        print("   %-52s %s %-28s %s" % (relpath, icon, shape,
              "  ".join("%s=%s" % (f.replace("PolyForm-Noncommercial-1.0.0", "PolyForm"),
                                   got or "∅") for f, got, _g in verdicts)))

    print()
    print("# declared=%d  %s" % (len(ENTRY_POINTS),
          "  ".join("%s=%d" % (k, v) for k, v in sorted(tally.items()))))
    if defects:
        print("#")
        print("# 🔴 DEFECTS, each one a family × classifier pair:")
        for label, fam, got, g in defects:
            print("#   %-44s %-30s said %-14s %s" % (label.split(":")[0], fam, got, g))
        print("#")
        print("# 🔴 `DEFECT-COMMERCIAL` is the direction that COSTS: a noncommercial")
        print("#    grant reported as a family a studio may ship. p309's defect ran the")
        print("#    other way (usable supply excluded), which is why it cost nothing")
        print("#    before it was found and this one does not have that mercy.")
        return 1
    print("🟢 PASS — no classifier crosses a commercial-use boundary on these %d families."
          % len(rows))
    return 0


if __name__ == "__main__":
    sys.exit(main())
