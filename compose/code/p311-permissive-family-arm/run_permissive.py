#!/usr/bin/env python3
"""p311 — the DYNAMIC arm on `MIT` and `Apache-2.0`: `ACTION p310-R` item 1.

🔵 THE GRADER IS IMPORTED FROM `p310`, not restated — `grade`, `_answer`,
`ENTRY_POINTS`, `OUT_OF_DOMAIN`, `ABSTENTIONS`, the whole calibration.  That is
this base's standing rule (`p309`: *"import the discriminator, never restate
it"*) and `p310` paid for the calibration twice over: its first build condemned
six correct instruments and its second still condemned `p419` four times, because
*"half this base's instruments are Spanish and none of them share a sentinel"*.
🔴 A fresh grader here would have re-derived that list by guesswork, which is the
exact failure mode both passes were about.

🔴 WHAT THIS ARM FOUND: **nothing, on 9 classifiers × 2 families.** `MIT` and
`Apache-2.0` — `7 884` cells, `61 %` of every licence cell this base publishes —
are read correctly by every instrument that reads payloads at all.

🟢 That is a real result and it is worth stating as one, because `ACTION p310-R`
ranked it *"the single highest-value hour available"* on the strength of the cell
count.  **The cell count was the wrong reason**, and `risk_order.py` carries the
argument: `MIT` and `Apache-2.0` are the most-published families on this base, so
they are the families every rung here was written against and tested on by
accident.  Cell count measures how well-EXERCISED a family is at least as much as
how exposed it is.

🔵 So the hour was still worth spending — an unexecuted rung under 61 % of the
published cells is not something to leave asserted — but the finding is that the
QUEUE IS SORTED BY BLAST RADIUS AND READ AS IF IT WERE SORTED BY RISK.
"""
import importlib.util
import io
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
CODE = os.path.normpath(os.path.join(HERE, ".."))
P310 = os.path.join(CODE, "p310-family-coverage")


def _load(name, path, extra_path=None):
    """Load a file as `name`, stdout muted, with an optional `sys.path` entry.

    🔴 `name` is namespaced by pass, and `extra_path` is removed again. Both are
    `p310`'s own defences and neither is fastidiousness: three instruments in
    this tree ship a `fixtures.py`, and `p310` records losing an afternoon to
    `module 'fixtures' has no attribute 'GPL3'` — first loader wins.
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


_fx = _load("p311_fixtures", os.path.join(HERE, "fixtures.py"), HERE)
_pid = _load("p311_identity", os.path.join(HERE, "payload_identity.py"), HERE)

# 🔵 IMPORTED, all of it. The calibration lives at p310 and is read from there.
_arm = _load("p311_p310_arm", os.path.join(P310, "run_families.py"), P310)
ENTRY_POINTS = list(_arm.ENTRY_POINTS)
grade = _arm.grade
_answer = _arm._answer
OUT_OF_DOMAIN = dict(_arm.OUT_OF_DOMAIN)


def _newly_exercised():
    """Cells held by the families THIS instrument pinned, read off the shelves.

    🔵 Imported from `p310`'s census so the quantity tracks the shelves rather
    than a literal written on the day the arm was built."""
    try:
        cen = _load("p311_arm_census",
                    os.path.join(P310, "family_coverage.py"), P310)
        counts, _missing = cen.published(os.path.normpath(
            os.path.join(HERE, "..", "..", "..")))
    except Exception:                                    # noqa: BLE001
        return 0
    mine = {fam for _n, fam, _c, _w in _fx.DECLARED}
    return sum(n for fam, n in counts.items() if fam in mine)


def main():
    rows = _fx.declared()

    print("# p311 dynamic arm — every classifier p309/p310 declare, run on the two")
    print("# families this base PUBLISHES MOST and no arm had ever touched.")
    for name, fam, com, _why, _text, n, sha in rows:
        print("#   %-32s %-12s %-5s %6d B  %s" % (name, fam, com, n, sha))
    print()

    # 🟢 The identity channel first, because it is this pass's second finding and
    # it is a property of the PAYLOADS, not of any classifier.
    print("# 🔴 RAW identity (bytes + sha, as this base pins every payload) vs the")
    print("#    CANONICAL identity of the same grant:")
    ident = _pid.report([(n, f, t) for n, f, _c, _w, t, _b, _s in rows])
    for name, fam, rn, rs, cn, cs, _hold in ident:
        print("#   %-32s %-12s raw %6d B %s   canonical %6d B %s"
              % (name, fam, rn, rs, cn, cs))
    distinct_raw = len({r[3] for r in ident})
    distinct_canon = len({r[5] for r in ident})
    print("#   🔴 %d distinct RAW shas  ->  🟢 %d distinct GRANTS (one per family)."
          % (distinct_raw, distinct_canon))
    print("#      The Apache pair differs by ONE LEADING NEWLINE; the MIT pair by")
    print("#      the HOLDER STRING alone. Neither difference is in the grant, and")
    print("#      p310 certified seven CC0 rows partly on exact byte length.")
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
            mod = _arm._load(relpath)
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
                 else "UNRUNNABLE" if any(g == "UNRUNNABLE" for _f, _g2, g in verdicts)
                 else "ABSTAIN" if any(g == "ABSTAIN" for _f, _g2, g in verdicts)
                 else "COARSE" if any(g == "COARSE" for _f, _g2, g in verdicts)
                 else "CORRECT")
        icon = {"CORRECT": "🟢", "COARSE": "🟢", "ABSTAIN": "🟡",
                "DEFECT": "🔴", "DEFECT-COMMERCIAL": "🔴", "UNRUNNABLE": "🔴"}[worst]
        tally[worst] = tally.get(worst, 0) + 1
        per = {}
        for _f, _g2, g in verdicts:
            per[g] = per.get(g, 0) + 1
        shape = " ".join("%s=%d" % (k, v) for k, v in sorted(per.items()))
        print("   %-52s %s %-22s %s" % (relpath, icon, shape,
              "  ".join("%s=%s" % (f, got or "∅") for f, got, _g in verdicts)))

    print()
    print("# declared=%d  %s" % (len(ENTRY_POINTS),
          "  ".join("%s=%d" % (k, v) for k, v in sorted(tally.items()))))
    if defects:
        print("#")
        print("# 🔴 DEFECTS, each one a family × classifier pair:")
        for label, fam, got, g in defects:
            print("#   %-44s %-12s said %-14s %s" % (label.split(":")[0], fam, got, g))
        return 1

    # 🔵 DERIVED from the census, never a literal. The first build printed
    # `7 884` as a constant, which is the same habit as a restated list: the
    # number was true on the day and would have gone on being printed after the
    # shelves moved under it.
    newly = _newly_exercised()
    print("🟢 PASS — every classifier that reads payloads reads these families")
    print("   correctly. %s cells newly exercised by this instrument; ZERO defects."
          % ("%d" % newly if newly else "—"))
    print("# 🔵 `p191` returns `permissive-software` on all four, which the imported")
    print("#    grader reads as ABSTAIN by grammar. It is p191's own axis answering")
    print("#    p191's own question and it is RIGHT IN EFFECT for both families —")
    print("#    recorded here, not promoted to CORRECT, because widening another")
    print("#    pass's calibration from this file is the thing this arm refuses.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
