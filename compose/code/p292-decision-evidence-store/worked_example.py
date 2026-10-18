"""`ACTION p292` — the worked example, run as a demonstration and committed as evidence.

🔵 Four surfaces, one substrate.  `P45` admissions, `P46` retention, `P47` grading, `P48`
vocational — each writes into the SAME chain with its OWN closed act vocabulary.  That is the
honest version of `p291`'s "one build": one substrate and four schemas, not one component.

Run: `python3 worked_example.py --out <path.jsonl>`  (no network, no dependencies)
"""
import argparse
import sys

from decision_store import Refused, Store, anchor_statement

READER = {"id": "reader-7741", "kind": "human"}
ADVISER = {"id": "adviser-0219", "kind": "human"}
MARKER = {"id": "marker-5583", "kind": "human"}
ASSESSOR = {"id": "assessor-1140", "kind": "human"}

ROWS = [
    # --- P45 admissions: the agent recommends, the human decides, they DISAGREE -----------
    dict(decision_id="adm-2027-0001", surface="admissions", decision="admit",
         annex_limb="III-3-a-admission", decider=READER, rubric_version="ug-2027-rev3",
         subject_ref="appl-9f2c1b", decided_at="2026-10-18T09:14:02Z",
         agent={"slug": "iblai/higher-education-agents", "ref": "1a2d898bbd04",
                "recommendation": "refer-to-committee", "role": "advisory"},
         shown={"academic": ["GPA 3.4, in-context against school profile"],
                "contextual": ["first-generation applicant"],
                "anomalies": ["unexplained 2024 gap — recorded as an observation"],
                "not_captured": ["portfolio", "interview", "reference letters"]}),
    # --- P45 admissions: concurrence, recorded as such ------------------------------------
    dict(decision_id="adm-2027-0002", surface="admissions", decision="refer-to-committee",
         annex_limb="III-3-a-admission", decider=READER, rubric_version="ug-2027-rev3",
         subject_ref="appl-4d7e08", decided_at="2026-10-18T09:31:48Z",
         agent={"slug": "iblai/higher-education-agents", "ref": "1a2d898bbd04",
                "recommendation": "refer-to-committee", "role": "advisory"},
         shown={"academic": ["grade trajectory inconsistent with self-report"],
                "anomalies": ["self-reported data conflicts with transcript — observation"],
                "not_captured": ["portfolio", "interview"]}),
    # --- P45 step 5: the distress route, to a NAMED human ---------------------------------
    dict(decision_id="adm-2027-0003", surface="admissions", decision="refer-to-committee",
         annex_limb="III-3-a-admission", decider=READER, rubric_version="ug-2027-rev3",
         subject_ref="appl-1a55c9", decided_at="2026-10-18T09:48:11Z",
         distress_flag=True, distress_routed_to={"id": "dean-of-students-3", "kind": "human"},
         agent={"slug": "iblai/higher-education-agents", "ref": "1a2d898bbd04",
                "recommendation": None, "role": "advisory"},
         shown={"statement_excerpt": ["content suggesting the applicant is in distress"],
                "handling": ["routed to a named human before any admissions act"]}),
    # --- P46 retention: the score RANKS, the adviser decides ------------------------------
    dict(decision_id="ret-2027-0044", surface="retention", decision="invite-to-support",
         annex_limb="III-3-b-learning-outcomes", decider=ADVISER,
         rubric_version="invitation-rule-2026q4", subject_ref="stu-77b30e",
         decided_at="2026-10-18T10:02:00Z",
         agent={"slug": "cedanl/student-signal", "ref": "4463e8d17cfb",
                "recommendation": "invite-to-support", "role": "advisory"},
         shown={"rank": ["decile 2 of 10 on the invitation rule"],
                "threshold": ["precision 0.41 / recall 0.63 at this invitation threshold"],
                "not_captured": ["term-time employment", "caring responsibilities"]}),
    dict(decision_id="ret-2027-0045", surface="retention", decision="no-contact",
         annex_limb="III-3-b-learning-outcomes", decider=ADVISER,
         rubric_version="invitation-rule-2026q4", subject_ref="stu-2c91af",
         decided_at="2026-10-18T10:07:35Z",
         agent={"slug": "cedanl/student-signal", "ref": "4463e8d17cfb",
                "recommendation": "invite-to-support", "role": "advisory"},
         shown={"rank": ["decile 3 of 10"],
                "adviser_note": ["already in a support plan via another route"]}),
    # --- P47 grading: the model drafts, the marker marks ----------------------------------
    dict(decision_id="grd-2027-0912", surface="grading", decision="amend-draft",
         annex_limb="III-3-b-learning-outcomes", decider=MARKER,
         rubric_version="essay-band-descriptors-v7", subject_ref="sub-5e04d1",
         decided_at="2026-10-18T10:41:19Z",
         agent={"slug": "draft-grader", "ref": "local", "recommendation": "accept-draft",
                "role": "advisory"},
         shown={"per_criterion": ["argument 3/5 — span cited", "evidence 4/5 — span cited"],
                "aggregate_withheld": ["no mark is produced by the model"],
                "not_captured": ["the band descriptor's 'originality' limb"]}),
    # --- P48 vocational: a REGULATED credential, the limb an auditor probes first ---------
    dict(decision_id="cle-2026-0310", surface="vocational", decision="not-yet-competent",
         annex_limb="III-3-a-admission", decider=ASSESSOR,
         rubric_version="cle-cycle-2026-rev1", subject_ref="prac-8830fe",
         decided_at="2026-10-18T11:05:52Z",
         agent={"slug": "iblai/legal-agents", "ref": "pinned", "recommendation": "certify",
                "role": "advisory"},
         shown={"hours": ["18 of 24 CLE hours evidenced"],
                "gap": ["ethics limb unevidenced"],
                "not_captured": ["carry-over from the prior cycle"]}),
    # --- P48 step 2: the recorded EXCLUSION, which is what an auditor probes first --------
    dict(decision_id="cle-2026-0311", surface="vocational", decision="refer-to-assessor",
         annex_limb="NONE-DECLARED", decider=ASSESSOR, rubric_version="cle-cycle-2026-rev1",
         subject_ref="prac-45c1d7", decided_at="2026-10-18T11:12:06Z",
         agent={"slug": "iblai/legal-agents", "ref": "pinned", "recommendation": None,
                "role": "advisory"},
         shown={"reason": ["administrative routing only — no competence act taken"],
                "limb_note": ["recorded as declaring NO limb, deliberately"]}),
]

# 🔴 The two records the store REFUSES.  A reference implementation that only demonstrates
# the happy path has not demonstrated the control.
REFUSALS = [
    ("the agent recorded as the decider",
     dict(decision_id="adm-2027-9001", surface="admissions", decision="deny",
          annex_limb="III-3-a-admission",
          decider={"id": "application-reader-agent", "kind": "agent"},
          rubric_version="ug-2027-rev3", subject_ref="appl-000bad",
          decided_at="2026-10-18T11:30:00Z",
          agent={"slug": "iblai/higher-education-agents", "ref": "1a2d898bbd04",
                 "recommendation": "deny", "role": "advisory"},
          shown={"academic": ["below threshold"]})),
    ("distress routed to a QUEUE instead of a named human",
     dict(decision_id="adm-2027-9002", surface="admissions", decision="refer-to-committee",
          annex_limb="III-3-a-admission", decider=READER, rubric_version="ug-2027-rev3",
          subject_ref="appl-001bad", decided_at="2026-10-18T11:33:00Z", distress_flag=True,
          distress_routed_to={"id": "safeguarding-queue", "kind": "queue"},
          agent={"slug": "iblai/higher-education-agents", "ref": "1a2d898bbd04",
                 "recommendation": None, "role": "advisory"},
          shown={"statement_excerpt": ["distress content"]})),
]


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    args = ap.parse_args(argv)

    store = Store(args.out)
    if store.head() != "GENESIS":
        print(f"🔴 {args.out} already holds records — the store is append-only by design.")
        return 1

    for row in ROWS:
        store.append(**row)
    print(f"🟢 {len(store)} records appended across 4 surfaces")

    print("\n🔴 The refusals — nothing is written:")
    for why, row in REFUSALS:
        try:
            store.append(**row)
            print(f"   🔴 NOT REFUSED: {why}")
            return 1
        except Refused as exc:
            print(f"   🟢 refused ({why}): {exc.findings[0].split(chr(9))[0]}")
    print(f"   🟢 store still holds {len(store)} records")

    findings = store.verify()
    print(f"\nchain walk: {len(findings)} finding(s)")
    if findings:
        for f in findings:
            print("   " + f)
        return 1

    con, comparable, rate = store.concurrence_rate()
    print(f"🔵 concurrence {con}/{comparable} = {rate:.2f} — the rubber-stamp measurement, "
          "available only because concurrence is recorded rather than refused")
    print(f"🔵 Annex III limb census (P48 step 2): {store.limb_census()}")
    print("\n" + anchor_statement(store))
    return 0


if __name__ == "__main__":
    sys.exit(main())
