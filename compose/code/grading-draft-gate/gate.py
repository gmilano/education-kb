#!/usr/bin/env python3
"""The `toshieji/moodle-grading-mcp` pattern, extracted so it can be asserted.

Three properties, read out of that project's README (fetched over
raw.githubusercontent.com, 8.326 bytes, rama `main`):

  (i)   "Grades are written as `workflowstate=readyforreview` (graded but
        UNRELEASED). This server never releases."
  (ii)  "An AI-assistance disclosure footer is appended if missing (override
        via MOODLE_AI_FOOTER_FILE)."
  (iii) "Writes go only to allowlisted course IDs
        (MOODLE_WRITE_COURSE_ALLOWLIST); empty = no write target.
        MOODLE_ALLOW_WRITE=1 is also required."

and a FOURTH that the project does not state and this KB measured in the
pase 57: (i) is only true when the target assignment has `markingworkflow=1`.
Moodle mails the grade when `markingworkflow=0` whatever workflowstate says
(locallib.php:3001). `require_marking_workflow` is therefore ON by default
here: the pattern as published is conditional, and the condition is a
per-assignment setting in Moodle that the server does not own.
"""

DRAFT_STATE = "readyforreview"
DEFAULT_FOOTER = (
    '<p class="ai-disclosure">This feedback was drafted with AI assistance '
    'and reviewed by a human grader.</p>'
)


class GateRefused(Exception):
    """The gate refused the write. Carries a stable reason code."""

    def __init__(self, reason, detail=""):
        super().__init__(f"{reason}: {detail}" if detail else reason)
        self.reason = reason


class GradingDraftGate:
    def __init__(self, moodle, allow_write=False, course_allowlist=(),
                 footer=DEFAULT_FOOTER, require_marking_workflow=True):
        self.moodle = moodle
        self.allow_write = bool(allow_write)
        self.course_allowlist = frozenset(course_allowlist)
        self.footer = footer
        self.require_marking_workflow = bool(require_marking_workflow)
        self.audit = []          # JSONL-shaped: every attempt, denial, success

    def _log(self, outcome, **rest):
        self.audit.append(dict(outcome=outcome, **rest))

    def add_footer(self, text):
        """(ii) appended if missing, never duplicated."""
        body = text or ""
        if self.footer in body:
            return body
        return (body + "\n" + self.footer) if body else self.footer

    def _marking_workflow_on(self, assignmentid):
        got = self.moodle.call("mod_assign_get_assignments")
        for course in got["courses"]:
            for a in course["assignments"]:
                if a["id"] == assignmentid:
                    return bool(a["markingworkflow"])
        raise GateRefused("unknown-assignment", str(assignmentid))

    def save_grade_draft(self, courseid, assignmentid, userid, grade,
                         feedback=""):
        attempt = dict(course=courseid, assignment=assignmentid, user=userid)

        # (iii) the startup gate, both halves, before anything is sent.
        if not self.allow_write:
            self._log("denied-allow-write", **attempt)
            raise GateRefused("allow-write-off",
                              "MOODLE_ALLOW_WRITE is not 1")
        if not self.course_allowlist:
            self._log("denied-empty-allowlist", **attempt)
            raise GateRefused("empty-allowlist",
                              "MOODLE_WRITE_COURSE_ALLOWLIST is empty")
        if courseid not in self.course_allowlist:
            self._log("denied-not-allowlisted", **attempt)
            raise GateRefused("not-allowlisted", f"course {courseid}")

        # the precondition the published pattern does not check
        if self.require_marking_workflow:
            if not self._marking_workflow_on(assignmentid):
                self._log("denied-no-marking-workflow", **attempt)
                raise GateRefused(
                    "marking-workflow-off",
                    f"assignment {assignmentid} has markingworkflow=0, so "
                    "readyforreview would be released to the student")

        self.moodle.call(
            "mod_assign_save_grade",
            assignmentid=assignmentid, userid=userid, grade=grade,
            workflowstate=DRAFT_STATE,          # (i) never 'released'
            attemptnumber=-1, addattempt=0, applytoall=1,
            plugindata={"assignfeedbackcomments_editor": {
                "text": self.add_footer(feedback), "format": 1}},
        )
        self._log("written", state=DRAFT_STATE, **attempt)
        return DRAFT_STATE
