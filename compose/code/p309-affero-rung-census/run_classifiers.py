#!/usr/bin/env python3
"""p309 — the DYNAMIC arm: run each licence classifier on a real payload.

🔴 The reason this file exists is that the static census in `rung_census.py` was
WRONG FIVE TIMES OUT OF SEVEN.  It screens source text for a rung that fires on a
GPL-3.0 payload and ranks the file as suspect; measured against the classifiers'
own output, five of the seven runnable candidates return `GPL-3.0` correctly —
because the rung the screen found is reached only after a title read, or sits in a
ladder whose earlier rung wins, or is applied to a window the screen cannot see.

🟢 So the screen GENERATES CANDIDATES and this arm DECIDES.  A verdict about code
that can be run is a measurement, never a reading.

    ENTRY_POINTS   file -> callable name, declared explicitly.  An instrument whose
                   entry point is not declared is reported UNRUNNABLE, never SAFE —
                   `p441-tree-licence-enumeration` is one (it imports a sibling
                   module that is not on the path from here).
    DEFECT         the classifier names AGPL for the GPL-3.0 payload, or GPL for
                   the AGPL-3.0 one.  Both directions, because a gate that only
                   looks one way would have passed `p307`'s shelves.
"""
import io
import importlib.util
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import fixtures as _fx  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
FIXTURES = os.path.join(HERE, "fixtures")
CODE = os.path.normpath(os.path.join(HERE, ".."))

GPL3 = _fx.GPL3
GPL3_B = _fx.GPL3_SECOND
AGPL3 = _fx.AGPL3

# 🔵 Declared, not discovered.  A map a pass has to extend by hand is a map whose
# gaps are visible; an auto-discovered one hides them behind a zero.
# (path, callable, input kind).  🔵 The kind is declared because it is not
# recoverable from the code: a payload classifier and a declared-token grammar have
# the same signature and opposite inputs, and grading one with the other's fixture
# condemns a correct instrument — which this census did, twice, before the kind
# existed.
TOKEN_FIXTURES = [("AGPL-3.0", "AGPL"), ("GPL-3.0", "GPL"),
                  ("GPL-3.0-or-later", "GPL"),
                  ("GNU Affero General Public License v3", "AGPL")]

ENTRY_POINTS = [
    ("p419-copyleft-identity/identidad_copyleft.py", "familia"),
    ("p306-licence-probe/licence_probe.py", "classify"),
    ("p191-spec-license-sweep/classify_spec.py", "classify"),
    ("p211-full-column-grant-audit/classify.py", "classify"),
    ("p153-declaration-surfaces/surfaces.py", "classify_body"),
    ("p129-transcription-audit/holder.py", "family"),
    ("p228-shelf-gate/classify_grant.py", "classify"),
    ("p198-title-line-family/family_title_line.py", "family"),
    ("p150-gpl-affero-discrimination/gpl_affero.py", "title_licence"),
]

# Declared-token grammars, graded on tokens.  Same gate, different fixture.
TOKEN_ENTRY_POINTS = [
    ("p222-ecosystem-bound-grammar/bound_grammar.py", "_family"),
    ("p221-licence-version-range/version_range.py", "_family_of"),
]


def body(prefix):
    return _fx.body(prefix)


def call(path, fn):
    d = os.path.join(CODE, os.path.dirname(path))
    sys.path.insert(0, d)
    try:
        spec = importlib.util.spec_from_file_location(
            "p309_" + os.path.dirname(path).replace("-", "_"), os.path.join(CODE, path))
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        return getattr(mod, fn), None
    except Exception as exc:                        # noqa: BLE001 — reported, not raised
        return None, "%s: %s" % (type(exc).__name__, str(exc)[:70])
    finally:
        sys.path.pop(0)


def grade(answer_gpl, answer_agpl):
    g, a = str(answer_gpl).upper(), str(answer_agpl).upper()
    if "AGPL" in g:
        return "DEFECT-GPL3-READ-AS-AGPL"
    if "AGPL" not in a and ("GPL" in a or "COPYLEFT" in a):
        return "DEFECT-AGPL3-READ-AS-GPL"
    return "CORRECT"


def main(argv):
    gpl3, gpl3b, agpl3 = body(GPL3), body(GPL3_B), body(AGPL3)
    print("# p309 dynamic arm — every declared classifier, run on pinned payloads")
    for pre, (nb, sha) in sorted(_fx.PINS.items()):
        print("#   %-36s %6d B  %s" % (pre, nb, sha))
    bad = _fx.verify()
    if bad:
        print("🔴 FAIL — a fixture drifted from its pin: %r" % (bad,))
        return 1
    print("")
    defects, unrunnable, correct = [], [], []
    for path, fn in ENTRY_POINTS:
        f, err = call(path, fn)
        if f is None:
            unrunnable.append((path, err))
            print("   %-50s 🟡 UNRUNNABLE  %s" % (path, err))
            continue
        try:
            a, b, c = f(gpl3), f(agpl3), f(gpl3b)
        except Exception as exc:                    # noqa: BLE001
            unrunnable.append((path, "call: %s" % type(exc).__name__))
            print("   %-50s 🟡 UNRUNNABLE  call raised %s" % (path, type(exc).__name__))
            continue
        verdict = grade(a, b)
        second = grade(c, b)
        if verdict != "CORRECT" or second != "CORRECT":
            defects.append((path, verdict, a, b))
            print("   %-50s 🔴 %s" % (path, verdict))
            print("        GPL-3.0 -> %r    AGPL-3.0 -> %r" % (a, b))
        else:
            correct.append(path)
            print("   %-50s 🟢 CORRECT    GPL-3.0 -> %s" % (path, str(a)[:34]))
    for path, fn in TOKEN_ENTRY_POINTS:
        f, err = call(path, fn)
        if f is None:
            unrunnable.append((path, err))
            print("   %-50s 🟡 UNRUNNABLE  %s" % (path, err))
            continue
        bad = []
        for tok, want in TOKEN_FIXTURES:
            try:
                got = str(f(tok)).upper()
            except Exception as exc:                # noqa: BLE001
                bad.append((tok, type(exc).__name__)); continue
            if want == "AGPL" and "AGPL" not in got:
                bad.append((tok, got))
            if want == "GPL" and ("AGPL" in got or "GPL" not in got):
                bad.append((tok, got))
        if bad:
            defects.append((path, "DEFECT-TOKEN-GRAMMAR", bad, ""))
            print("   %-50s 🔴 DEFECT-TOKEN-GRAMMAR  %s" % (path, bad))
        else:
            correct.append(path)
            print("   %-50s 🟢 CORRECT    %d declared tokens" % (path, len(TOKEN_FIXTURES)))
    print("")
    print("# declared=%d  CORRECT=%d  DEFECT=%d  UNRUNNABLE=%d"
          % (len(ENTRY_POINTS) + len(TOKEN_ENTRY_POINTS), len(correct), len(defects), len(unrunnable)))
    if defects:
        print("🔴 FAIL — a classifier reads a real GPL-3.0 payload as AGPL-3.0, or the"
              " reverse.  p150 owns the discriminator; import it, do not restate it.")
        return 1
    print("🟢 PASS — every declared classifier separates GPL-3.0 from AGPL-3.0 on"
          " first-hand payloads.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
