#!/usr/bin/env python3
"""Offline controls for `p434-promotion-gate` — `Gap 433-A`'s gate, and the refutation
of its own prescribed predicate as a standing control rather than a claim in prose.

Every fixture family below is one this pass MEASURED on a real payload (see the table in
`promotion_gate.py`'s docstring), so the negatives are the specimens that actually occur
on this corpus and not invented ones.
"""
import os
import subprocess
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, _HERE)
from promotion_gate import (CURATED, P433_THRESHOLD, PERMISSIVE,  # noqa: E402
                            TRENDING, findings, main, read_grades,
                            shelf_addresses, unpromoted)

ok = n = 0


def check(label, got, want):
    global ok, n
    n += 1
    if got == want:
        ok += 1
        print("  ok   %s" % label)
    else:
        print("  FAIL %s\n       got  %r\n       want %r" % (label, got, want))


def repo_root():
    return os.path.abspath(os.path.join(_HERE, os.pardir, os.pardir, os.pardir))


# The grade table as measured 2026-10-25, used as the fixture population so the control
# and the live arm cannot drift apart.
GRADES = {
    "brycewang-stanford/auto-empirical-research-skills":
        {"family": "CC-BY-SA-4.0", "stars": "4771"},
    "sitor-ai/frametell": {"family": "AGPL-3.0", "stars": "400"},
    "minicoohei/ai-agent-camp": {"family": "NO-GRANT", "stars": "346"},
    "helixnow/deep-student": {"family": "AGPL-3.0", "stars": "290"},
    "ystemsrx/sql-to-er": {"family": "AGPL-3.0", "stars": "192"},
    "wenflow-org/wenflow": {"family": "MIT", "stars": "59"},
    "zhangl1001/civil-ai": {"family": "MIT", "stars": "41"},
}
POP = set(GRADES)

# ── C1-C3: membership is what the gate is about ───────────────────────────────────────
print("C1-C3 membership")
f, u = findings(POP, set(), GRADES)
check("C1 both MIT rows are findings when no curated shelf holds them",
      [r[0] for r in f], ["wenflow-org/wenflow", "zhangl1001/civil-ai"])
f, u = findings(POP, {"wenflow-org/wenflow"}, GRADES)
check("C2 an address a curated shelf already holds is NOT a finding",
      [r[0] for r in f], ["zhangl1001/civil-ai"])
check("C3 unpromoted is a set difference, not an intersection",
      unpromoted({"a/b", "c/d"}, {"a/b"}), {"c/d"})

# ── C4-C7: the families, each one a measured specimen ─────────────────────────────────
print("C4-C7 licence families — every negative is a real payload read 2026-10-25")
fams = {r[1] for r in findings(POP, set(), GRADES)[0]}
check("C4 only PERMISSIVE families appear in findings", fams, {"MIT"})
check("C5 AGPL-3.0 is not promotable (frametell / deep-student / sql-to-ER)",
      "AGPL-3.0" in PERMISSIVE, False)
# The load-bearing negative: the single highest-traction address on this corpus.
check("C6 CC-BY-SA-4.0 is not promotable — the 4 771 star specimen",
      "CC-BY-SA-4.0" in PERMISSIVE, False)
check("C7 an absent grant is not a grant", "NO-GRANT" in PERMISSIVE, False)

# ── C8-C11: THE REFUTATION OF `Gap 433-A`'s PRESCRIBED PREDICATE ──────────────────────
print("C8-C11 Gap 433-A's own predicate, run as prescribed")
f434, _ = findings(POP, set(), GRADES, predicate="p434")
f433, _ = findings(POP, set(), GRADES, predicate="p433")
check("C8 the corrected predicate finds 2", len(f434), 2)
check("C9 the PRESCRIBED predicate finds 0 on the same population", len(f433), 0)
check("C10a so the two genuinely disagree", len(f434) != len(f433), True)
check("C10b and the threshold is what suppresses them",
      all(int(GRADES[s]["stars"]) < P433_THRESHOLD for s, _f, _st, _c in f434), True)
# Reason 1: no reachable channel serves a star count, so the prescribed predicate cannot
# judge a row at all once the star column is absent.  The corrected one is unaffected.
starless = {k: {"family": v["family"], "stars": "-"} for k, v in GRADES.items()}
check("C11a with no star channel the prescribed predicate judges NOTHING",
      len(findings(POP, set(), starless, predicate="p433")[0]), 0)
check("C11b while the corrected predicate is unaffected",
      len(findings(POP, set(), starless, predicate="p434")[0]), 2)

# ── C12-C13: an ungraded address is a REACH bound, never a defect ─────────────────────
print("C12-C13 the reach bound")
f, u = findings(POP | {"never/graded"}, set(), GRADES)
check("C12 an ungraded address is reported as ungraded", u, ["never/graded"])
check("C13 and is NOT a finding", "never/graded" in [r[0] for r in f], False)

# ── C14-C15: case folding (p439's lesson) ─────────────────────────────────────────────
print("C14-C15 case folding")
f, _u = findings({"wenflow-org/wenflow"}, {"WenFlow-Org/WenFlow".lower()}, GRADES)
check("C14 a curated citation under another spelling still counts as promoted", len(f), 0)
g = read_grades(os.path.join(_HERE, "grades.2026-10-25.tsv"))
check("C15 the grade table is keyed case-folded",
      "ystemsrx/sql-to-er" in g, True)

# ── C16-C18: the population is p351's, and PERMISSIVE is p444's ───────────────────────
print("C16-C18 reuse, not reimplementation (T108)")
check("C16 PERMISSIVE is imported from p444 and holds its members",
      {"MIT", "Apache-2.0", "BSD-3-Clause"} <= PERMISSIVE, True)
check("C17a CC-BY-SA is in neither direction by accident — it is absent",
      "CC-BY-SA" in PERMISSIVE, False)
root = repo_root()
live_curated = shelf_addresses([os.path.join(root, p) for p in CURATED
                                if os.path.exists(os.path.join(root, p))])
check("C17b a nav namespace is not an address in the live curated set",
      "topics/ai-tutor" in live_curated, False)
check("C18 every curated shelf this gate names exists",
      all(os.path.exists(os.path.join(root, p)) for p in CURATED), True)
check("C18b and every trending shelf too",
      all(os.path.exists(os.path.join(root, p)) for p in TRENDING), True)

# ── C19-C21: the empty-input refusal (`P541` / `Gap 243` / `Gap 245`) ─────────────────
print("C19-C21 empty-input refusal")
check("C19 main([]) refuses with exit 2", main([]), 2)
check("C20 main(['findings']) with no root also refuses", main(["findings"]), 2)
check("C21 main(['census']) with no root also refuses", main(["census"]), 2)

# ── C22-C24: the live arm, end to end through the shell ───────────────────────────────
print("C22-C24 the live arm as `make` invokes it")
r = subprocess.run([sys.executable, "-I", os.path.join(_HERE, "promotion_gate.py"),
                    "census", root], capture_output=True, text=True)
check("C22 census exits 0", r.returncode, 0)
check("C23 census publishes a reach bound rather than hiding it",
      "ungraded_reach_bound" in r.stdout, True)
r2 = subprocess.run([sys.executable, "-I", os.path.join(_HERE, "promotion_gate.py"),
                     "findings", root, "--predicate", "p433"], capture_output=True, text=True)
check("C24 the prescribed predicate is green on the live shelves too", r2.returncode, 0)

print("\n%d/%d controls pass" % (ok, n))
sys.exit(0 if ok == n else 1)
