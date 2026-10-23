#!/usr/bin/env python3
"""Controls for `p400-candidate-membership`.

Group 1 — the DEFECT's own specimen, which is why this module exists.
Group 2 — the TWO-CHANNEL controls: addresses carried only as backticked text.
Group 3 — shape, delegated to `p351`/`p375` and never re-spelled here.
Group 4 — the negative controls other instruments pinned, which this one must not eat.
Group 5 — no fixture may pin a LIVE derived total (p376's rule; a total is not a control).
Group 6 — P541: an empty population is a refusal, not an empty answer.
"""
import importlib.util
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, os.pardir, os.pardir, os.pardir))


def _mod():
    path = os.path.join(HERE, "membership.py")
    spec = importlib.util.spec_from_file_location("p400_membership", path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


M = _mod()

# 🔴 THE RULE CONTROLS READ A FIXTURE, NOT THE LIVE TREE.  `p400`'s first suite pinned its
# specimen's verdict over the shelves, and `p400`'s OWN write falsified it inside the hour: the
# address graded SHELVED-EXACT because the pass shelved it.  That is `gate-census-currency`'s
# ordering defect reproduced inside a test fixture — a control whose input is the shelves is
# stale the moment the pass writes to them.  🟢 The fixture carries the CONTAINING name and not
# the contained one, which is the only relationship the substring class is about.
FIXTURE = M.Shelf([os.path.join(HERE, "fixture", "shelf-a.md")])
LIVE = M.Shelf(M.shelf_paths(ROOT))
checks = 0
fails = []


def want(candidate, verdict, why, shelf=None):
    global checks
    checks += 1
    got, ev = (shelf or FIXTURE).classify(candidate)
    if got != verdict:
        fails.append(f"🔴 {why}\n     candidate: {candidate}\n     got:  {got} ({ev})\n     want: {verdict}")


# ── Group 1 — the specimen.  A bare `grep ai-grader` over this tree returns hits, every one
# from `moocupv/lti-ai-grader`.  If this control ever reads SHELVED-EXACT, either the address
# was promoted (update the control deliberately) or the test has stopped testing anything.
want("andres-tovar-purdue/ai-grader", M.NAME_SUBSTRING_ONLY,
     "1. p400's live specimen: a name CONTAINED by a shelved name is not membership")
want("moocupv/lti-ai-grader", M.SHELVED_EXACT,
     "2. the containing address itself IS shelved — the positive half of the same pair")

# 🔵 Direction control: the pair must not be symmetric.  `lti-ai-grader` contains `ai-grader`,
# never the reverse, so a substring rule applied the wrong way round fails here and only here.
checks += 1
_v1, _e1 = FIXTURE.classify("andres-tovar-purdue/ai-grader")
_v2, _e2 = FIXTURE.classify("moocupv/lti-ai-grader")
if (_v1, _v2) == (_v2, _v1):
    fails.append("🔴 3. the containment pair graded symmetrically; substring is a DIRECTED relation")
else:
    pass

# ── Group 2 — both channels.  These two are carried on `agents/trending.md` as backticked
# `owner/repo` with their grants read, and NEITHER is written as a `github.com/` link.  A
# membership test keyed on URLs alone answers UNSHELVED for both, which is `p374`'s defect
# re-committed in the acceptance direction.
want("dymchenkko/claude-study-agent", M.SHELVED_EXACT,
     "4. channel B: a backticked address with no URL is still carried")
want("i-ninte/grad-agent", M.SHELVED_EXACT,
     "5. channel B again, on a row whose grant read was ABSENT — a verdict is not a grant")

# ── Group 3 — shape is `p351`'s and `p375`'s, asked before membership.
want("topics/ai-tutor", M.NOT_AN_ADDRESS,
     "6. p351's navigation namespace is not an address, whatever the text contains")
want("owner/main", M.NOT_AN_ADDRESS,
     "7. p375's NAME-REF-OR-PATH arm, reused rather than re-spelled")
want("not-an-address", M.NOT_AN_ADDRESS,
     "8. a bare word has no owner/name shape")

# ── Group 4 — negative controls other instruments pinned and measured LIVE.  `p375` records
# `skills` as 2 LIVE / 0 ABSENT and forbids its own vocabulary from holding it.
want("mattpocock/skills", M.SHELVED_EXACT,
     "9. p375's pinned name-position negative control survives this module's shape gate")
want("vercel-labs/skills", M.SHELVED_EXACT,
     "10. the second of p375's pinned pair")

# ── Group 4b — a true same-name collision is NOT a substring case and must not be conflated.
# The shelf carries several `*/ai-tutor` owners, so an unshelved owner of that exact name is
# NAME-OTHER-OWNER: still unshelved as an address, but for a different reason, and the
# distinction is the whole point of having two classes instead of one.
want("zz-not-a-real-owner-p400/ai-tutor", M.NAME_OTHER_OWNER,
     "11. same name under an uncarried owner is a collision, not a substring artefact")

# 🟢 Group 4c -- the LIVE tree, asserting only what a pass cannot invalidate by writing.
# 🔴 Deliberately NOT the specimen's verdict: p400 shelved it, so over the live tree it is
# now SHELVED-EXACT, and a control asserting otherwise would fail for a correct reason.
want("moocupv/lti-ai-grader", M.SHELVED_EXACT,
     "11b. the containing address is carried on the LIVE tree too", shelf=LIVE)
want("topics/ai-tutor", M.NOT_AN_ADDRESS,
     "11c. shape is tree-independent, so it holds on the live tree as well", shelf=LIVE)

# ── Group 5 — no fixture pins a live derived total.
checks += 1
_src = open(os.path.join(HERE, "membership.py"), encoding="utf-8").read()
import re as _re
_totals = [n for n in _re.findall(r"\b\d{4,}\b", _src)
           if n not in ("2024", "2025", "2026", "2027")]
if _totals:
    fails.append("🔴 12. membership.py pins what looks like a derived total: "
                 + ",".join(_totals) + " — a census figure is derived, never compiled in")

# ── Group 6 — P541.
checks += 1
_r = subprocess.run([sys.executable, "-I", os.path.join(HERE, "membership.py"), "classify"],
                    capture_output=True, text=True)
if _r.returncode != 2:
    fails.append(f"🔴 13. an empty population must exit 2, got {_r.returncode}")

# ── Group 6b — the two classes must stay distinguishable in the CLI, not just in the API.
checks += 1
_r2 = subprocess.run([sys.executable, "-I", os.path.join(HERE, "membership.py"),
                      "audit", os.path.join(HERE, "fixture", "candidates.txt"),
                      os.path.join(HERE, "fixture", "shelf-a.md")],
                     capture_output=True, text=True, cwd=ROOT)
if M.NAME_SUBSTRING_ONLY not in _r2.stdout:
    fails.append("🔴 14. the CLI does not report the defect's class: " + _r2.stdout[:300])

# ── Group 7 — `p406`'s guard: a PARTIAL shelf set, which is NOT an empty one.
# 🔴 Run from this module's own directory, the only `SHELVES` entry that exists is its own
# `README.md`, so the population is 6 addresses and group 6's emptiness control does NOT
# fire.  `p406` graded nine shelved addresses `UNSHELVED` that way.  Both halves are
# asserted: the partial root must REFUSE, and the real root must still answer.
checks += 1
_r3 = subprocess.run([sys.executable, "-I", os.path.join(HERE, "membership.py"),
                      "classify", "HKUDS/DeepTutor"],
                     capture_output=True, text=True, cwd=HERE)
if _r3.returncode != 2 or "PARTIAL population" not in _r3.stderr:
    fails.append("🔴 15. a partial shelf set must exit 2 and say so, got rc=%d %r"
                 % (_r3.returncode, _r3.stderr[:200]))

checks += 1
_r4 = subprocess.run([sys.executable, os.path.join(HERE, "membership.py"),
                      "classify", "HKUDS/DeepTutor"],
                     capture_output=True, text=True, cwd=ROOT)
if _r4.returncode != 0 or "SHELVED-EXACT" not in _r4.stdout:
    fails.append("🔴 16. the guard must not break the real root, got rc=%d %r"
                 % (_r4.returncode, _r4.stdout[:200]))

if fails:
    print(f"🔴 p400-candidate-membership: {len(fails)} of {checks} controls FAILED")
    for f in fails:
        print("  " + f)
    sys.exit(1)
print(f"ok — {checks} checks, 0 failures")
