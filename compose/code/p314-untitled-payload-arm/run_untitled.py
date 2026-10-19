#!/usr/bin/env python3
"""p314 — the dynamic arm on the UNTITLED-GRANT class: `ACTION p313-R` item 5,
widened by this pass's own finding from one family to two.

🔵 THE GRADER IS IMPORTED FROM `p310`, not restated — `grade`, `_answer`,
`ENTRY_POINTS`, `OUT_OF_DOMAIN`, the whole calibration. That is this base's
standing rule (`p309`: *"import the discriminator, never restate it"*) and `p311`
records why it is not politeness: `p310` paid for that calibration twice, its
first build condemning six correct instruments and its second still condemning
`p419` four times.

🔴 WHAT THIS ARM ASKS, and no arm on this base has asked it before. Every arm so
far has been keyed on a FAMILY — `p311` on MIT and Apache-2.0, `p312` on five,
`p313` on the noncommercial four. This one is keyed on a **payload SHAPE**, and
it holds the family constant to do it: each family enters twice, once with the
family name in its first line and once without.

🟢 So a reading here is a DIFFERENCE, not a level. If a classifier reads the
titled payload and abstains on the untitled one, the family is not what it is
reading — the title line is, and the grant it cannot read is just as binding.

🔴 THE SECOND CHANNEL, AND IT IS THE ONE THAT MATTERS: being right is not the
same as being right for a reason. `crewAIInc/crewAI`'s payload contains no `MIT`
token, and the substring form `"mit" in low` returns True on it anyway — it
matches inside *permit*. So this arm reports, per classifier, both
  • the verdict the imported grader assigns, and
  • whether the family token is PRESENT in the payload at all,
because a `CORRECT` on a payload whose family token is absent is either real
pattern-reading or an accident, and the two must not be counted together.
"""
import importlib.util
import io
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
CODE = os.path.normpath(os.path.join(HERE, ".."))
P310 = os.path.join(CODE, "p310-family-coverage")
P311 = os.path.join(CODE, "p311-permissive-family-arm")


def _load(name, path, extra_path=None):
    """Load a file as `name`, stdout muted, with an optional `sys.path` entry.

    🔴 `name` is namespaced by pass and `extra_path` is removed again. Both are
    `p310`'s defences, inherited: `-I` strips the script's own directory from
    `sys.path` (`p355-cwd-portability`), and three instruments in this tree ship
    a `fixtures.py`, so first loader wins (`p150-identifier-collision`).
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


_fx = _load("p314_fixtures", os.path.join(HERE, "fixtures.py"), HERE)
_pid = _load("p314_identity", os.path.join(P311, "payload_identity.py"), P311)

# 🔵 IMPORTED, all of it. The calibration lives at p310 and is read from there.
_arm = _load("p314_p310_arm", os.path.join(P310, "run_families.py"), P310)
ENTRY_POINTS = list(_arm.ENTRY_POINTS)
grade = _arm.grade
_answer = _arm._answer
OUT_OF_DOMAIN = dict(_arm.OUT_OF_DOMAIN)

# 🔵 The family TOKEN, as a title channel would look for it: the distinctive word
# of the family name, not the whole SPDX string. Built from the family rather
# than written per row so a new family cannot arrive without one.
_TOKEN = {"MIT": "mit", "BSD-3-Clause": "bsd"}

# 🔴 The substring form this base has refuted three times, kept LIVE here as the
# accident channel. `p306` met it as `"affero" in low` and again as `"cc0" in
# low`; this arm is the first place it has a payload that makes the accident
# visible rather than merely possible.
def _substring_says(token, text):
    return token in text.lower()


def _token_present(token, text):
    """Is the family token in the payload AS A WORD? 🔵 This is the question the
    substring form is *trying* to ask, and the difference between the two
    answers on one payload is this arm's second finding."""
    return bool(re.search(r"\b%s\b" % re.escape(token), text, re.I))


def _short(prefix):
    """The repository half of a fixture prefix — the family half is already in
    the column beside it. 🔵 The first build printed `prefix.split("-")[-1]`,
    which rendered `bsd-3-clause-open-tutor-ai-ce` as `ce`."""
    for fam in sorted(_TOKEN, key=len, reverse=True):
        slug = fam.lower() + "-"
        if prefix.startswith(slug):
            return prefix[len(slug):]
    return prefix


def _title_line(text):
    """The payload's first non-blank line — what a title channel reads."""
    for line in text.lstrip("﻿").splitlines():
        if line.strip():
            return line.strip()
    return ""


def main():
    rows = _fx.declared()
    pairs = _fx.shape_pairs()
    arm_rows = [r for r in rows if r[1] in _TOKEN]
    by_prefix = {r[0]: r for r in rows}

    print("# p314 dynamic arm — keyed on payload SHAPE, with the family held constant.")
    print("# `ACTION p313-R` item 5, widened from BSD-3-Clause to MIT by this pass.")
    print()
    print("# %-28s %-14s %-9s %6s  %-12s %s"
          % ("payload", "family", "shape", "bytes", "sha", "first non-blank line"))
    for fam in sorted(pairs):
        for slot in ("titled", "untitled"):
            for prefix in pairs[fam][slot]:
                _p, f, _c, _w, text, n, sha = by_prefix[prefix]
                icon = "🟢" if slot == "titled" else "🔴"
                print("#  %s %-30s %-14s %-9s %6d  %-12s %s"
                      % (icon, prefix, f, slot, n, sha, _title_line(text)[:42]))
    print()

    # ── the token channel, a property of the PAYLOADS and not of any classifier
    print("# 🔴 THE TOKEN CHANNEL — is the family name even IN the file?")
    print("# %-28s %-14s %-10s %-10s %s"
          % ("payload", "family", "as a word", "substring", "🔴 verdict"))
    accidents = []
    for prefix, fam, _c, _w, text, _n, _s in arm_rows:
        tok = _TOKEN[fam]
        word = _token_present(tok, text)
        sub = _substring_says(tok, text)
        if sub and not word:
            note = "🔴 SUBSTRING MATCHES WITHOUT THE TOKEN — an accident"
            accidents.append((prefix, fam, tok))
        elif not sub and not word:
            note = "⚪ absent on both channels — a title rung is blind here"
        else:
            note = "🟢 present"
        print("#  %-28s %-14s %-10s %-10s %s"
              % (prefix, fam, word, sub, note))
    if accidents:
        print("#")
        for prefix, fam, tok in accidents:
            text = by_prefix[prefix][4]
            hits = sorted({m.group(0) for m in
                           re.finditer(r"\w*%s\w*" % re.escape(tok), text, re.I)
                           if m.group(0).lower() != tok})
            print("#   🔴 %s: `%s` is absent as a word; the substring matches inside %s"
                  % (prefix, tok, ", ".join("`%s`" % h for h in hits)))
    print()

    # ── the classifier channel
    tally = {}
    defects = []
    blind_on_untitled = []
    for relpath, callable_name in ENTRY_POINTS:
        if relpath in OUT_OF_DOMAIN:
            print("   %-52s ⚪ OUT-OF-DOMAIN  %s" % (relpath, OUT_OF_DOMAIN[relpath]))
            tally["OUT-OF-DOMAIN"] = tally.get("OUT-OF-DOMAIN", 0) + 1
            continue
        try:
            mod = _arm._load(relpath)
            fn = getattr(mod, callable_name)
        except Exception as exc:                        # noqa: BLE001
            print("   %-52s 🔴 UNRUNNABLE     %s: %s"
                  % (relpath, type(exc).__name__, str(exc)[:60]))
            tally["UNRUNNABLE"] = tally.get("UNRUNNABLE", 0) + 1
            continue

        verdicts = {}
        for prefix, fam, _c, _w, text, _n, _s in arm_rows:
            try:
                got = _answer(fn(text))
            except Exception as exc:                    # noqa: BLE001
                got, g = "raise:%s" % type(exc).__name__, "UNRUNNABLE"
            else:
                g = grade(fam, got)
            verdicts[prefix] = (fam, got, g)
            if g.startswith("DEFECT"):
                defects.append((relpath, prefix, fam, got, g))

        # 🟢 The reading this arm exists for: the SAME classifier on the SAME
        # family, titled against untitled.
        deltas = []
        for fam in sorted(pairs):
            # 🔵 ALL of a slot's payloads, not one: a classifier that reads two
            # untitled payloads and abstains on a third is not title-dependent,
            # it is something else, and averaging the slot would hide that.
            reads_titled = all(not verdicts[p][2].startswith("ABSTAIN")
                               for p in pairs[fam]["titled"])
            reads_untitled = all(not verdicts[p][2].startswith("ABSTAIN")
                                 for p in pairs[fam]["untitled"])
            if reads_titled and not reads_untitled:
                deltas.append("%s=TITLE-ONLY" % fam)
                blind_on_untitled.append((relpath, fam))
            elif reads_titled == reads_untitled:
                deltas.append("%s=%s" % (fam, "both" if reads_titled else "neither"))
            else:
                deltas.append("%s=UNTITLED-ONLY" % fam)

        grades = [v[2] for v in verdicts.values()]
        worst = ("DEFECT-COMMERCIAL" if any(g == "DEFECT-COMMERCIAL" for g in grades)
                 else "DEFECT" if any(g == "DEFECT" for g in grades)
                 else "UNRUNNABLE" if any(g == "UNRUNNABLE" for g in grades)
                 else "ABSTAIN" if any(g == "ABSTAIN" for g in grades)
                 else "COARSE" if any(g == "COARSE" for g in grades)
                 else "CORRECT")
        icon = {"CORRECT": "🟢", "COARSE": "🟢", "ABSTAIN": "🟡",
                "DEFECT": "🔴", "DEFECT-COMMERCIAL": "🔴", "UNRUNNABLE": "🔴"}[worst]
        tally[worst] = tally.get(worst, 0) + 1
        print("   %-52s %s %-18s %s" % (relpath, icon, " ".join(deltas),
              "  ".join("%s=%s" % (_short(p), v[1] or "∅")
                        for p, v in sorted(verdicts.items()))))

    print()
    print("# declared=%d  %s" % (len(ENTRY_POINTS),
          "  ".join("%s=%d" % (k, v) for k, v in sorted(tally.items()))))

    if blind_on_untitled:
        print("#")
        print("# 🔴 TITLE-ONLY readings — the classifier reads the family when the")
        print("#    first line names it and ABSTAINS on the same family's grant")
        print("#    when it does not. The grant is equally binding in both files:")
        for relpath, fam in blind_on_untitled:
            print("#     %-46s %s" % (relpath, fam))
    else:
        print("# 🟢 No classifier's reading depends on the title line.")

    if defects:
        print("#")
        print("# 🔴 DEFECTS — a wrong family or a crossed commercial boundary:")
        for relpath, prefix, fam, got, g in defects:
            print("#   %-44s %-28s %-14s said %-14s %s"
                  % (relpath, prefix, fam, got, g))
        return 1

    print("🟢 PASS — no classifier returns a WRONG family or crosses a")
    print("   commercial-use boundary on the untitled-grant class.")
    print("# 🔵 Stated precisely, because the finding is an ABSTENTION pattern and")
    print("#    not a defect: an abstention fails SAFE under `P250`")
    print("#    (`UNDETERMINED` is indistinguishable from `PROHIBITED`), so the")
    print("#    cost of the untitled shape is USABLE SUPPLY EXCLUDED — the same")
    print("#    direction as `p309`'s and `p311`'s `MPL-2.0` losses, and on")
    print("#    `MIT` + `BSD-3-Clause` it is the largest such surface this base")
    print("#    has measured.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
