#!/usr/bin/env python3
"""Controls for `P1060` (p191). Offline — every fixture is authored in this file.

🔵 **The obligatory cases are the ones where a CLAIM and an ENFORCEMENT look alike**, because
that distinction is the whole reason this module exists: p190 published an authorisation
model read from a README and had to retract it one pass later. A suite that only counted
attributes would pass with the prose/code confusion fully intact.

    python3 test_surface.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from surface import classify, guard_report, summarise, tools_in  # noqa: E402

PASS = FAIL = 0


def check(name, got, want):
    global PASS, FAIL
    if got == want:
        PASS += 1
    else:
        FAIL += 1
        print(f"FAIL {name}\n  got  {got!r}\n  want {want!r}")


# A tool whose DESCRIPTION promises a permission check and whose BODY has none.
CLAIM_ONLY = """<?php
final readonly class PromiseTool
{
    #[McpTool(
        name: 'update_course_settings',
        description: 'Change course properties. Only available to the course teacher, and
            every capability respects the permissions of the authenticated user.',
    )]
    public function updateCourseSettings(int $courseId): array
    {
        return $this->repo->save($courseId);
    }
}
"""

# The same tool, with the check actually in the body.
ENFORCED = """<?php
final readonly class RealTool
{
    #[McpTool(
        name: 'update_user_roles',
        description: 'Change a user\\'s roles on this portal.',
    )]
    public function updateUserRoles(int $userId): array
    {
        if (!$this->security->isGranted('ROLE_ADMIN')) {
            throw new AccessDeniedException('Only administrators can change user roles.');
        }
        return $this->repo->save($userId);
    }
}
"""

check("a tool is found from its attribute",
      [t["name"] for t in tools_in(CLAIM_ONLY)], ["update_course_settings"])
check("🔴 a permission PROMISE in a description is 0 enforcement",
      guard_report(CLAIM_ONLY)["enforced"], 0)
check("🔴 and the promise is reported as prose, not dropped",
      guard_report(CLAIM_ONLY)["in_prose"], ["permission"])
check("🟢 an isGranted + throw in the body IS enforcement",
      guard_report(ENFORCED)["enforced"] >= 2, True)
check("🟢 the role it enforces is named", guard_report(ENFORCED)["roles"], ["ROLE_ADMIN"])
check("a role named only inside an ATTRIBUTE is not enforcement",
      guard_report("""<?php
      #[McpTool(name: 'x', description: 'Requires ROLE_ADMIN access.')]
      public function x(): void {}
      """)["roles"], [])

check("read verbs classify read", [classify(n) for n in
                                   ("get_course_tests", "list_documents",
                                    "read_course_document", "find_recent_activity")],
      ["read", "read", "read", "read"])
check("write verbs classify write", [classify(n) for n in
                                     ("create_course", "upsert_course_test_description",
                                      "remove_learning_path_item", "close_ticket")],
      ["write", "write", "write", "write"])
check("an unknown verb is NOT silently filed as a read",
      classify("frobnicate_course"), "unclassified")

s = summarise({"a.php": CLAIM_ONLY, "b.php": ENFORCED})
check("two files, two tools", s["n_tools"], 2)
check("both are writes", (s["reads"], s["writes"]), (0, 2))
check("only one file enforces anything", s["files_with_enforcement"], 1)
check("the prose-only guard word is surfaced at the summary level",
      s["guard_words_in_prose_only"], ["permission"])
check("nothing is left unclassified in the fixture", s["unclassified"], [])

# A verb a NAME cannot settle must be LISTED, which is this instrument's version of
# `p441`'s rule: where it cannot decide, it hands over a reading list.
s2 = summarise({"c.php": """<?php
#[McpTool(name: 'generate_student_success_feedback', description: 'Write feedback.')]
#[McpTool(name: 'review_course_quality', description: 'Report on a course.')]
"""})
check("verb-ambiguous tools are listed, not guessed",
      s2["ambiguous"], ["generate_student_success_feedback", "review_course_quality"])

# `P355`: an empty source set is a path fault. Asserted here because the runner exits 2.
check("an empty surface summarises to 0 rather than crashing",
      summarise({})["n_tools"], 0)

print(f"\nP1060 — {PASS} passed, {FAIL} failed  ({PASS + FAIL} controls)")
sys.exit(1 if FAIL else 0)
