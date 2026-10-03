#!/usr/bin/env python3
"""grading-draft-gate — OFFLINE, stdlib only, no network.

Asserts the three properties of the `toshieji/moodle-grading-mcp` pattern
SEPARATELY, against a stub that reproduces Moodle's real contract, plus the
negative controls the pase 56 taught this KB to demand (P126, point 2): an
assertion that FAILS when the gate is switched off, so the suite actually
exercises the case where the pattern can fail.
"""
import sys

from gate import GradingDraftGate, GateRefused, DRAFT_STATE, DEFAULT_FOOTER
from moodle_stub import MoodleStub, WsError, STATES, RELEASED

checks = 0
failures = []


def check(label, got, want):
    global checks
    checks += 1
    if got == want:
        print(f"PASS  {label}")
    else:
        failures.append(label)
        print(f"FAIL  {label}\n        got  {got!r}\n        want {want!r}")


def raises(label, fn, exc, needle=""):
    global checks
    checks += 1
    try:
        fn()
    except exc as e:
        if needle and needle not in str(e):
            failures.append(label)
            print(f"FAIL  {label}\n        raised {exc.__name__} but "
                  f"{needle!r} not in {str(e)!r}")
        else:
            print(f"PASS  {label}")
    except Exception as e:                                  # noqa: BLE001
        failures.append(label)
        print(f"FAIL  {label}\n        raised {type(e).__name__}: {e}")
    else:
        failures.append(label)
        print(f"FAIL  {label}\n        did not raise {exc.__name__}")


def site():
    """assignment 10 has marking workflow on, 99 has it OFF."""
    return MoodleStub({10: 1, 99: 0})


def open_gate(m, **kw):
    kw.setdefault("allow_write", True)
    kw.setdefault("course_allowlist", [5])
    return GradingDraftGate(m, **kw)


# ============ the stub is a contract, not a yes-man ======================
print("-- the stub punishes what Moodle punishes --")
m = site()
raises("stub: workflowstate with an underscore -> PARAM_ALPHA rejects it",
       lambda: m.call("mod_assign_save_grade", assignmentid=10, userid=1,
                      grade=5.0, workflowstate="ready_for_review"),
       WsError, "invalidparameter")
raises("stub: a state Moodle does not define is rejected",
       lambda: m.call("mod_assign_save_grade", assignmentid=10, userid=1,
                      grade=5.0, workflowstate="draft"),
       WsError, "not a state")
raises("stub: a function outside the token raises accessexception",
       lambda: m.call("mod_assign_save_submission"), WsError,
       "accessexception")
check("stub: Moodle's six states, verbatim from locallib.php:64-69",
      list(STATES),
      ["notmarked", "inmarking", "readyforreview", "inreview",
       "readyforrelease", "released"])
check("stub: nothing was written by the four malformed calls", m.grades, {})

# ============ (i) the grade is a draft and is never released ============
print("\n-- (i) readyforreview, and never released --")
m = site()
g = open_gate(m)
check("(i) the gate writes exactly readyforreview", g.save_grade_draft(5, 10, 77, 8.5), DRAFT_STATE)
check("(i) the state Moodle now holds is readyforreview", m.flags[(10, 77)], "readyforreview")
check("(i) and it is NOT 'released'", m.flags[(10, 77)] == RELEASED, False)
check("(i) the student was not notified", m.notified, [])
check("(i) the student cannot see it", m.student_can_see(10, 77), False)
check("(i) the grade itself did land", m.grades[(10, 77)]["grade"], 8.5)
check("(i) the gate never emits 'released' for any input", 
      sorted({r.get("state") for r in g.audit if r["outcome"] == "written"}),
      ["readyforreview"])

# ============ (ii) the footer is added if missing, never duplicated =====
print("\n-- (ii) the disclosure footer --")
m = site()
g = open_gate(m)
g.save_grade_draft(5, 10, 1, 7.0, feedback="Good structure.")
check("(ii) footer appended when missing",
      m.grades[(10, 1)]["feedback"].endswith(DEFAULT_FOOTER), True)
check("(ii) the original feedback survives",
      m.grades[(10, 1)]["feedback"].startswith("Good structure."), True)
check("(ii) appended exactly once",
      m.grades[(10, 1)]["feedback"].count(DEFAULT_FOOTER), 1)

g.save_grade_draft(5, 10, 2, 7.0, feedback="Nice work.\n" + DEFAULT_FOOTER)
check("(ii) NOT duplicated when already present",
      m.grades[(10, 2)]["feedback"].count(DEFAULT_FOOTER), 1)

g.save_grade_draft(5, 10, 3, 7.0, feedback="")
check("(ii) empty feedback still carries the disclosure",
      m.grades[(10, 3)]["feedback"], DEFAULT_FOOTER)
check("(ii) and carries nothing else",
      m.grades[(10, 3)]["feedback"].count(DEFAULT_FOOTER), 1)

# ============ (iii) the startup gate, both halves =======================
print("\n-- (iii) the course allowlist and the write flag --")
m = site()
raises("(iii) a course outside the allowlist is refused",
       lambda: open_gate(m).save_grade_draft(6, 10, 1, 9.0),
       GateRefused, "not-allowlisted")
check("(iii) and nothing reached Moodle", m.grades, {})

m = site()
raises("(iii) an EMPTY allowlist is no write target, not a wildcard",
       lambda: GradingDraftGate(m, allow_write=True,
                                course_allowlist=[]).save_grade_draft(5, 10, 1, 9.0),
       GateRefused, "empty-allowlist")
check("(iii) and nothing reached Moodle", m.grades, {})

m = site()
raises("(iii) MOODLE_ALLOW_WRITE unset refuses even an allowlisted course",
       lambda: GradingDraftGate(m, allow_write=False,
                                course_allowlist=[5]).save_grade_draft(5, 10, 1, 9.0),
       GateRefused, "allow-write-off")
check("(iii) and nothing reached Moodle", m.grades, {})
check("(iii) zero web-service calls were made on a refusal", m.calls, 0)

m = site()
g = open_gate(m)
try:
    g.save_grade_draft(6, 10, 1, 9.0)
except GateRefused:
    pass
check("(iii) the denial is in the audit log",
      [r["outcome"] for r in g.audit], ["denied-not-allowlisted"])

# ============ (iv) NEGATIVE CONTROLS ====================================
# A suite that only ever runs the gate switched ON never touches the case
# where the pattern fails. These four do.
print("\n-- (iv) negative controls: the assertions that fail if the gate is off --")

# (iv-a) the gate switched off at its own level: the write goes through.
m = site()
ungated = GradingDraftGate(m, allow_write=True, course_allowlist=[5, 6])
ungated.save_grade_draft(6, 10, 1, 9.0)
check("(iv-a) widening the allowlist DOES let course 6 through "
      "(so the refusal above was the gate, not an accident)",
      m.grades[(10, 1)]["grade"], 9.0)

# (iv-b) THE ONE THAT MATTERS: the server does everything right, and the
# draft is released anyway, because the assignment has markingworkflow=0.
m = site()
bare = GradingDraftGate(m, allow_write=True, course_allowlist=[5],
                        require_marking_workflow=False)
state = bare.save_grade_draft(5, 99, 42, 4.0)
check("(iv-b) the server still sent readyforreview", state, DRAFT_STATE)
check("(iv-b) 🔴 and Moodle NOTIFIED the student anyway "
      "(markingworkflow=0, locallib.php:3001)", m.notified, [42])
check("(iv-b) 🔴 so the student CAN see the 'unreleased' draft",
      m.student_can_see(99, 42), True)
check("(iv-b) 🔴 and the workflowstate did not even register "
      "(locallib.php:7960)", m.flags[(99, 42)], None)

# (iv-c) with the precondition check ON, the same write is refused.
m = site()
guarded = open_gate(m)
raises("(iv-c) the precondition check refuses the markingworkflow=0 assignment",
       lambda: guarded.save_grade_draft(5, 99, 42, 4.0),
       GateRefused, "marking-workflow-off")
check("(iv-c) and the student was never notified", m.notified, [])
check("(iv-c) the refusal names the real reason in the audit log",
      [r["outcome"] for r in guarded.audit], ["denied-no-marking-workflow"])

# (iv-d) the control proves the two assignments differ only in that setting.
m = site()
g = open_gate(m)
g.save_grade_draft(5, 10, 7, 6.0)
check("(iv-d) same gate, same call, markingworkflow=1 -> no notification",
      m.notified, [])
raises("(iv-d) same gate, same call, markingworkflow=0 -> refused",
       lambda: g.save_grade_draft(5, 99, 7, 6.0),
       GateRefused, "marking-workflow-off")
check("(iv-d) the ONLY difference between the two is markingworkflow",
      sorted(m.assignments.items()), [(10, 1), (99, 0)])

print()
print(f"{checks - len(failures)}/{checks} checks passed")
ok = not failures
print("ALL CHECKS PASSED" if ok else f"SOME CHECKS FAILED: {failures}")
sys.exit(0 if ok else 1)
