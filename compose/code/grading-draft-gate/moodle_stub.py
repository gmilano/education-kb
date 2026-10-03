#!/usr/bin/env python3
"""A stub of Moodle's `mod_assign_save_grade` — stdlib only, no network.

It is NOT a mock that says yes. Every behaviour below was read out of
moodle/moodle @ main (Moodle 5 layout, tree relocated under `public/`) and is
cited by file and line so the gate under test is proved against the real
contract and not against a convenience:

  public/mod/assign/externallib.php:1987
      'workflowstate' => new external_value(PARAM_ALPHA, 'The next marking workflow state')
      -> PARAM_ALPHA is [a-zA-Z] only (public/lib/moodlelib.php:86-89), so
         'ready_for_review' or 'readyforreview ' are rejected by Moodle itself.

  public/mod/assign/locallib.php:64-69
      the six legal marking-workflow states.

  public/mod/assign/locallib.php:2991-3001   <-- the one that decides this suite
      "If marking workflow is enabled, the workflow state is at 'released'."
      WHERE (a.markingworkflow = 0 OR (a.markingworkflow = 1 AND uf.workflowstate = :wfreleased))
      -> when markingworkflow = 0 the grade is mailed to the student whatever
         workflowstate says. The draft is NOT a draft.

  public/mod/assign/locallib.php:7960
      $modified->workflowstatechanged = $this->get_instance()->markingworkflow && ...
      -> with markingworkflow = 0 a workflowstate change does not even register.
"""

STATES = ("notmarked", "inmarking", "readyforreview",
          "inreview", "readyforrelease", "released")
RELEASED = "released"


class WsError(Exception):
    """A Moodle web-service exception, with the Moodle error key."""

    def __init__(self, errorcode, message=""):
        super().__init__(f"{errorcode}: {message}")
        self.errorcode = errorcode


class MoodleStub:
    """One Moodle site. `assignments[id] = markingworkflow (0 or 1)`.

    `notified` is the measurement that matters: a userid lands in it exactly
    when locallib's mailing query would pick the grade up.
    """

    def __init__(self, assignments, allowed_functions=None):
        self.assignments = dict(assignments)
        self.allowed_functions = set(
            allowed_functions if allowed_functions is not None
            else ("mod_assign_save_grade", "mod_assign_get_assignments"))
        self.grades = {}        # (assignmentid, userid) -> {grade, feedback}
        self.flags = {}         # (assignmentid, userid) -> workflowstate
        self.notified = []      # userids Moodle would mail — the real test
        self.calls = 0

    # -- the transport ----------------------------------------------------
    def call(self, wsfunction, **params):
        self.calls += 1
        if wsfunction not in self.allowed_functions:
            # Moodle's own error key when a token lacks the function.
            raise WsError("accessexception", f"{wsfunction} not in token")
        if wsfunction == "mod_assign_get_assignments":
            return {"courses": [{"assignments": [
                {"id": a, "markingworkflow": mw}
                for a, mw in sorted(self.assignments.items())]}]}
        if wsfunction == "mod_assign_save_grade":
            return self._save_grade(**params)
        raise WsError("invalidrecord", wsfunction)

    # -- mod_assign_save_grade -------------------------------------------
    def _save_grade(self, assignmentid, userid, grade, workflowstate,
                    attemptnumber=-1, addattempt=0, applytoall=1,
                    plugindata=None):
        if assignmentid not in self.assignments:
            raise WsError("invalidrecord", "no such assignment")

        # PARAM_ALPHA, externallib.php:1987 + moodlelib.php:86-89.
        if workflowstate != "" and not workflowstate.isalpha():
            raise WsError("invalidparameter", "workflowstate is PARAM_ALPHA")
        if workflowstate != "" and workflowstate not in STATES:
            raise WsError("invalidparameter", f"not a state: {workflowstate}")

        key = (assignmentid, userid)
        self.grades[key] = {
            "grade": grade,
            "feedback": (plugindata or {}).get(
                "assignfeedbackcomments_editor", {}).get("text", ""),
        }

        markingworkflow = self.assignments[assignmentid]
        if markingworkflow:
            self.flags[key] = workflowstate or "notmarked"
            released = self.flags[key] == RELEASED
        else:
            # locallib.php:7960 — the change does not even register...
            self.flags[key] = None
            # ...and locallib.php:3001 — markingworkflow = 0 mails anyway.
            released = True

        if released:
            self.notified.append(userid)
        return None

    # -- what an auditor would ask ---------------------------------------
    def student_can_see(self, assignmentid, userid):
        return userid in self.notified
