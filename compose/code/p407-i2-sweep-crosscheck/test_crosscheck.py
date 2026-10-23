#!/usr/bin/env python3
"""Offline controls for `p407-i2-sweep-crosscheck`. No network, no repository code executed."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from crosscheck import (I2_ABSENT_CLASSES, LIVE_SHELVES, RECORD_FILES,  # noqa: E402
                        SWEPT_SHELVES, UNCLASSIFIED_SHELVES, classify_string, decay,
                        grade, i2_predicate, load_i2_absent, load_sweep, rows,
                        shelf_lines, substring_inflation)

FAIL = []
N = 0


def check(label, got, want):
    global N
    N += 1
    if got != want:
        FAIL.append(f"{label}: got {got!r}, want {want!r}")


ROOT = sys.argv[1] if len(sys.argv) > 1 else "."
SWEEP = os.path.join(ROOT, "evidence/carried-existence.2026-10-23-p406.tsv")
REPROBE = os.path.join(ROOT, "evidence/dead-citation-reprobe.2026-10-21-p372.tsv")

# ── C1-C2: the join key is folded, and the fold is load-bearing ──────────────────────────
check("C1 fold joins p372's casing to p406's",
      "EastArctica/canvas-mcp".lower(), "eastarctica/canvas-mcp")
_orig, _folded = load_i2_absent(REPROBE)
_mixed = [s for s in _orig if s != s.lower()]
# C2: a RAW join would lose every mixed-case slug — that is the false-disagreement count.
check("C2 a raw join would miss mixed-case slugs (fold is load-bearing)", len(_mixed) > 0, True)

# ── C3-C6: p372's string taxonomy, reproduced ────────────────────────────────────────────
check("C3 neg-control by marker", classify_string("openedx/fake-repo-zzz999"), "NEG-CONTROL")
check("C4 url-path fragment", classify_string("repos/HKUDS"), "URL-PATH-FRAGMENT")
check("C5 placeholder owner", classify_string("your-username/SafeTutors"), "PLACEHOLDER")
check("C6 a real address", classify_string("apereo/opencast"), "ADDRESS")

# ── C7-C10: I2's detector, and its measured blind spots ──────────────────────────────────
check("C7 fires on a markdown link", i2_predicate("see [x](https://github.com/a/b)", "a/b"), True)
check("C8 fires on a bare url with trailing space",
      i2_predicate("at https://github.com/a/b and", "a/b"), True)
check("C9 silent on a backticked slug (prose, not a link)",
      i2_predicate("| `a/b` | dead |", "a/b"), False)
# 🔴 a deeper path is a LINK and the detector cannot see it.
check("C10a silent on a deep link (measured limit)",
      i2_predicate("[x](https://github.com/a/b/tree/main)", "a/b"), False)
# 🔴 THE REPAIR TRAP: the folded population plus the shipped case-sensitive detector.
check("C10b case-sensitive detector misses a mixed-case link",
      i2_predicate("[G](https://github.com/Mckaroff/GraphLMS)", "mckaroff/graphlms"), False)
check("C10c the same line, folded, is seen",
      i2_predicate("[G](https://github.com/Mckaroff/GraphLMS)".lower(), "mckaroff/graphlms"), True)

# ── C11: CROSS-INSTRUMENT — reproduce p372's published non-address partition ─────────────
# 🟢 This is the control that stops the reimplementation above from becoming a second
# classifier. p372 published 5 NEG-CONTROL, 4 URL-PATH, 1 PLACEHOLDER over its 46 rows.
_rp = list(rows(REPROBE))
check("C11 the re-probe still holds 46 rows", len(_rp), 46)
_want = {"NOT-AN-ADDRESS/NEG-CONTROL": ("NEG-CONTROL", 5),
         "NOT-AN-ADDRESS/URL-PATH": ("URL-PATH-FRAGMENT", 4),
         "NOT-AN-ADDRESS/PLACEHOLDER": ("PLACEHOLDER", 1)}
for _cls, (_shape, _n) in _want.items():
    _got = [r["slug"] for r in _rp if r["class_p372"] == _cls]
    check(f"C11 {_cls} count", len(_got), _n)
    check(f"C11 {_cls} all classify as {_shape}",
          all(classify_string(s) == _shape for s in _got), True)
# and every other row must be a well-formed address
_addr_rows = [r for r in _rp if r["class_p372"] not in _want]
check("C11 every graded row is a well-formed address",
      all(classify_string(r["slug"]) == "ADDRESS" for r in _addr_rows), True)

# ── C12: the shelf-set guard is on COMPLETENESS, not existence (Gap 406-B) ───────────────
# 🔴 The refusal must be the GUARD's, not an incidental `open()` blowing up three frames
# later: a guard that only "works" because the read fails is not a guard.
try:
    shelf_lines(ROOT, SWEPT_SHELVES[:1] + ("does/not/exist.md",))
    _c12 = "no refusal"
except SystemExit:
    _c12 = "SystemExit"
except OSError:
    _c12 = "OSError — the guard did not fire; the read did"
check("C12 a missing shelf refuses in the guard", _c12, "SystemExit")

# ── C13: the taxonomy is INCOMPLETE and the instrument says so out loud ─────────────────
# 🔴 compose/patterns.md, intel/market.md and intel/trends.md are in NEITHER of p372's
# tuples, so I2 never reads them and no rule says a dead address there is a defect.
check("C13 three swept shelves are classified by neither tuple",
      UNCLASSIFIED_SHELVES,
      ("intel/market.md", "intel/trends.md", "compose/patterns.md"))
check("C13 the two tuples are disjoint",
      set(LIVE_SHELVES) & set(RECORD_FILES), set())

# ── C14: decay arithmetic reproduces p406's published rate ───────────────────────────────
_sweep = load_sweep(SWEEP)
_res, _unres, _pub, _corr = decay(_sweep, 0)
check("C14 p406's unresolved count", _unres, 59)
check("C14 p406's published rate rounds to 2.20%", round(_pub * 100, 2), 2.20)
check("C14 removing contaminants lowers the rate", decay(_sweep, 6)[3] < _pub, True)

# ── C15: a zero population refuses rather than publishing a rate ────────────────────────
check("C15 no rate over an empty graded half", decay({}, 0)[2], None)

# ── C16: I2's absent-class list is the gate's, by value ─────────────────────────────────
check("C16 I2 absent classes", len(I2_ABSENT_CLASSES), 4)
check("C16 p372's absent set size", len(_orig), 34)

# ── C17: grading is total — every ABSENT-OR-PRIVATE row gets exactly one mechanism ───────
_live = shelf_lines(ROOT, LIVE_SHELVES)
_graded = grade(_sweep, _orig, _folded, _live)
check("C17 every unresolved row is graded", len(_graded), 59)
check("C17 every row carries a mechanism", all(r["mechanism"] for r in _graded), True)

# ── C19-C20: the PUBLISHED partition is pinned to the rows ──────────────────────────────
# 🔴 This suite's own first draft had no control here, and the mutation `shape = "ADDRESS"`
# inside `grade()` changed nothing: the classifier was imported, checked in isolation, and
# then not actually load-bearing on any assertion. That is `p400`'s "an emptiness guard does
# not fire" in a new costume. These two controls are the repair, and they are `T37`/`recount`
# discipline: a figure this pass publishes may not drift from the rows it came from.
import collections as _c  # noqa: E402
_dist = _c.Counter(r["mechanism"] for r in _graded)
check("C19 the published mechanism partition", dict(_dist), {
    "AGREE-OFF-LIVE-SHELVES": 41,
    "DISAGREE-I2-POPULATION-FROZEN": 9,
    "NOT-DECAY-P372-REFUTES": 5,
    "AGREE-NOT-A-LIVE-CLAIM": 4,
})
check("C19 the partition sums to the sweep's unresolved count", sum(_dist.values()), 59)
# C20: the five fabricated negative controls must reach the mechanism BY the classifier.
_negs = sorted(r["address"] for r in _graded if r["mechanism"] == "NOT-DECAY-P372-REFUTES")
check("C20 the neg-controls are the five planted slugs", _negs, [
    "moodle/moodle-definitely-not-a-real-repo-p152",
    "openedx/fake-repo-zzz999",
    "this-definitely-does-not-exist-xyz123/nope",
    "this-org-does-not-exist-zzz9/nope",
    "unitime/this-repo-does-not-exist-xyz123",
])
check("C20 every one is NEG-CONTROL by the imported classifier",
      all(classify_string(a) == "NEG-CONTROL" for a in _negs), True)
# C21: the two mixed-case specimens are exactly the folded/caseless disagreement.
_casegap = sorted(r["address"] for r in _graded
                  if r["i2_fires_caseless"] > r["i2_fires_folded"])
check("C21 the case-sensitivity specimens", _casegap,
      ["ai-matrix-engine/aidream", "mckaroff/graphlms"])

# ── C18: substring inflation is detected where it exists ────────────────────────────────
check("C18 the detector finds a planted containment",
      substring_inflation({"a/b": ("x", ()), "a/bc": ("x", ())}), [("a/b", "a/bc")])

if FAIL:
    print(f"🔴 p407-i2-sweep-crosscheck — {len(FAIL)} of {N} controls FAILED:")
    for f in FAIL:
        print(f"   - {f}")
    sys.exit(1)
print(f"🟢 p407-i2-sweep-crosscheck — {N}/{N} offline controls pass")
