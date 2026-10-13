#!/usr/bin/env python3
"""Pass 183, ACTION LV. The assertions the action names, plus the two the port
itself turned up: the FK pragma trap and the CASCADE asymmetry.

Run:  python3 test_receipts.py
"""
from __future__ import annotations

import os
import sqlite3
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import receipts as R

checks: list[tuple[bool, str, str]] = []


def check(ok, label, detail=""):
    checks.append((bool(ok), label, detail))


def raises(exc, fn, *a, **kw):
    try:
        fn(*a, **kw)
    except exc as e:
        return True, str(e)
    except Exception as e:  # wrong exception type is a failure, not a pass
        return False, "raised %s instead: %s" % (type(e).__name__, e)
    return False, "did not raise"


def fixture(run_status="running"):
    conn = R.connect()
    conn.execute(
        "INSERT INTO metadata_packages(id,label,created_at) VALUES('mp1','cefr-b2',1)"
    )
    conn.execute("INSERT INTO exam_cycles(id,exam_name,created_at) VALUES('ec1','mock',1)")
    R.publish_policy_version(
        conn,
        policy_id="pol1",
        metadata_package_id="mp1",
        subject="maths",
        policy_type="grading",
        version="1.0.0",
        config_json='{"rubric":"analytic","pass_mark":60}',
        now=1,
    )
    conn.execute(
        "INSERT INTO tutor_agent_runs(id,status,version,created_at) VALUES('run1',?,1,1)",
        (run_status,),
    )
    conn.commit()
    return conn


def main():
    print("-- the schema applies, and both audit tables are really there --")
    conn = fixture()
    tables = {
        r["name"]
        for r in conn.execute("SELECT name FROM sqlite_master WHERE type='table'")
    }
    check(
        "agent_tool_receipts" in tables and "assessment_policy_versions" in tables,
        "both tables named in ACTION LV exist after one executescript",
        "ported from civil-ai @ 37ba5e2, stdlib sqlite3 only",
    )
    check(
        conn.execute("PRAGMA foreign_keys").fetchone()[0] == 1,
        "connect() turns foreign_keys ON",
        "SQLite defaults it OFF -- see the trap check below",
    )

    print("\n-- prepare is idempotent, as INSERT OR IGNORE promises --")
    first = R.prepare_receipt(
        conn,
        agent_run_id="run1",
        tool_call_id="tc1",
        tool_name="grade_submission",
        arguments_hash="a" * 32,
        business_idempotency_key="sub-42:grade",
        now=10,
    )
    second = R.prepare_receipt(
        conn,
        agent_run_id="run1",
        tool_call_id="tc1",
        tool_name="grade_submission",
        arguments_hash="a" * 32,
        business_idempotency_key="sub-42:grade",
        now=11,
    )
    rows = conn.execute("SELECT COUNT(*) c FROM agent_tool_receipts").fetchone()["c"]
    check(first and not second and rows == 1,
          "a retried prepare is a no-op, not a duplicate and not an error",
          "first=%s second=%s rows=%d" % (first, second, rows))

    print("\n-- the state machine: the legal path, with versions counted --")
    r1 = R.transition_receipt(
        conn, agent_run_id="run1", tool_call_id="tc1",
        to_status="running", expected_version=0, now=12,
    )
    check(r1["status"] == "running" and r1["version"] == 1 and r1["attempt_count"] == 1,
          "prepared -> running bumps version 0->1 and counts the attempt",
          "version=%d attempt_count=%d" % (r1["version"], r1["attempt_count"]))
    check(r1["completed_at"] is None,
          "a non-terminal transition leaves completed_at NULL")
    r2 = R.transition_receipt(
        conn, agent_run_id="run1", tool_call_id="tc1",
        to_status="succeeded", expected_version=1, now=13,
        result_json='{"score":72}',
    )
    check(r2["status"] == "succeeded" and r2["version"] == 2 and r2["completed_at"] == 13,
          "running -> succeeded bumps 1->2 and stamps completed_at",
          "the source requires new version == expected + 1; this writes exactly that")

    print("\n-- and the refusals, which are the point --")
    ok, msg = raises(
        R.IllegalTransition, R.transition_receipt,
        conn, agent_run_id="run1", tool_call_id="tc1",
        to_status="running", expected_version=2, now=14,
    )
    check(ok, "a terminal receipt cannot be re-opened", msg)
    conn2 = fixture()
    R.prepare_receipt(
        conn2, agent_run_id="run1", tool_call_id="tcv", tool_name="t",
        arguments_hash="v" * 32, business_idempotency_key="k", now=10,
    )
    ok, msg = raises(
        R.StaleWrite, R.transition_receipt,
        conn2, agent_run_id="run1", tool_call_id="tcv",
        to_status="running", expected_version=7, now=11,
    )
    check(ok,
          "a stale expected_version is refused (optimistic concurrency)",
          "checked on a LEGAL transition, so the version guard is what refuses "
          "and not the transition table: " + msg)

    R.prepare_receipt(
        conn2, agent_run_id="run1", tool_call_id="tc2", tool_name="t",
        arguments_hash="b" * 32, business_idempotency_key="k", now=10,
    )
    ok, msg = raises(
        R.IllegalTransition, R.transition_receipt,
        conn2, agent_run_id="run1", tool_call_id="tc2",
        to_status="succeeded", expected_version=0, now=11,
    )
    check(ok,
          "prepared -> succeeded is refused: a tool cannot succeed without running",
          "NOTE this is the port tightening the source. civil-ai's CHECK admits "
          "any of the 5 values; the transition table is this module's: " + msg)

    print("\n-- two writers, one winner --")
    conn3 = fixture()
    R.prepare_receipt(
        conn3, agent_run_id="run1", tool_call_id="tc3", tool_name="t",
        arguments_hash="c" * 32, business_idempotency_key="k", now=10,
    )
    # Both workers read the receipt at version 0. Worker A lands first.
    R.transition_receipt(
        conn3, agent_run_id="run1", tool_call_id="tc3",
        to_status="running", expected_version=0, now=11,
    )
    # Worker B still holds version 0 and reports the outcome it observed. The
    # transition is legal from the CURRENT state, so the transition table
    # cannot refuse it -- only the version guard can.
    ok, msg = raises(
        R.StaleWrite, R.transition_receipt,
        conn3, agent_run_id="run1", tool_call_id="tc3",
        to_status="succeeded", expected_version=0, now=12, result_json="{}",
    )
    check(ok,
          "the loser of a real race is refused rather than overwriting the winner",
          "running -> succeeded is a LEGAL transition, so this refusal comes "
          "from the stale version alone: " + msg)

    print("\n-- a receipt cannot be advanced under a run that is not running --")
    conn4 = fixture(run_status="succeeded")
    R.prepare_receipt(
        conn4, agent_run_id="run1", tool_call_id="tc4", tool_name="t",
        arguments_hash="d" * 32, business_idempotency_key="k", now=10,
    )
    ok, msg = raises(
        R.RunNotRunning, R.transition_receipt,
        conn4, agent_run_id="run1", tool_call_id="tc4",
        to_status="running", expected_version=0, now=11,
    )
    check(ok, "the parent-run guard holds (the source's `AND run.status='running'`)", msg)

    print("\n-- ON DELETE RESTRICT: the rule a grade was given under cannot vanish --")
    conn5 = fixture()
    R.bind_policy(
        conn5, exam_cycle_id="ec1", subject="maths",
        policy_type="grading", policy_id="pol1", now=20,
    )
    ok, msg = raises(
        sqlite3.IntegrityError, conn5.execute,
        "DELETE FROM assessment_policy_versions WHERE id='pol1'",
    )
    check(ok, "deleting a BOUND policy version is refused by the database", msg)

    R.publish_policy_version(
        conn5, policy_id="pol2", metadata_package_id="mp1", subject="physics",
        policy_type="grading", version="1.0.0", config_json="{}", now=21,
    )
    conn5.execute("DELETE FROM assessment_policy_versions WHERE id='pol2'")
    left = conn5.execute(
        "SELECT COUNT(*) c FROM assessment_policy_versions"
    ).fetchone()["c"]
    check(left == 1,
          "an UNBOUND policy version still deletes -- RESTRICT is targeted, not a freeze",
          "%d row(s) left" % left)

    print("\n-- the trap: the same schema with the pragma off enforces nothing --")
    loose = sqlite3.connect(":memory:")
    loose.row_factory = sqlite3.Row
    loose.executescript(R.SCHEMA)  # deliberately NOT turning foreign_keys on
    loose.execute("INSERT INTO metadata_packages(id,label,created_at) VALUES('mp1','x',1)")
    loose.execute("INSERT INTO exam_cycles(id,exam_name,created_at) VALUES('ec1','m',1)")
    R.publish_policy_version(
        loose, policy_id="pol1", metadata_package_id="mp1", subject="maths",
        policy_type="grading", version="1.0.0", config_json="{}", now=1,
    )
    R.bind_policy(
        loose, exam_cycle_id="ec1", subject="maths",
        policy_type="grading", policy_id="pol1", now=2,
    )
    loose.execute("DELETE FROM assessment_policy_versions WHERE id='pol1'")
    orphan = loose.execute(
        """SELECT COUNT(*) c FROM exam_cycle_policy_bindings b
             LEFT JOIN assessment_policy_versions p
               ON p.id = b.assessment_policy_version_id
            WHERE p.id IS NULL"""
    ).fetchone()["c"]
    check(orphan == 1,
          "with foreign_keys OFF the bound policy deletes and leaves an ORPHAN binding",
          "SQLite's default is OFF, so a correct schema audits nothing until a "
          "connection opts in -- check this in the deployment, not the migration")

    print("\n-- the asymmetry the port exposes: receipts are NOT non-erasable --")
    conn6 = fixture()
    R.prepare_receipt(
        conn6, agent_run_id="run1", tool_call_id="tc5", tool_name="t",
        arguments_hash="e" * 32, business_idempotency_key="k", now=10,
    )
    conn6.execute("DELETE FROM tutor_agent_runs WHERE id='run1'")
    gone = conn6.execute("SELECT COUNT(*) c FROM agent_tool_receipts").fetchone()["c"]
    check(gone == 0,
          "deleting the parent run CASCADES the receipts away",
          "the policy side is RESTRICT, the receipt side is CASCADE: the rule "
          "survives, the evidence that an agent applied it does not")

    print("\n-- the CHECK constraints are load-bearing --")
    ok, msg = raises(
        sqlite3.IntegrityError, conn.execute,
        """INSERT INTO assessment_policy_versions(id,metadata_package_id,subject,
             policy_type,version,config_json,content_hash,status,created_at)
           VALUES('short','mp1','s','t','1','{}','abc','published',1)""",
    )
    check(ok, "a content_hash under 16 chars is refused", msg)
    ok, msg = raises(
        sqlite3.IntegrityError, conn.execute,
        """INSERT INTO assessment_policy_versions(id,metadata_package_id,subject,
             policy_type,version,config_json,content_hash,status,created_at)
           VALUES('bad','mp1','s','t','1','{}','%s','live',1)""" % ("f" * 32),
    )
    check(ok, "a status outside draft/published/retired is refused", msg)

    print("\n-- the trail a studio shows an auditor --")
    trail = R.audit_trail(conn, "run1")
    check(len(trail) == 1 and trail[0]["tool_name"] == "grade_submission"
          and trail[0]["status"] == "succeeded",
          "audit_trail() returns the invoked tool, its terminal status and its "
          "business key",
          "%d row(s): %s" % (len(trail), ", ".join(
              "%s=%s" % (r["tool_name"], r["status"]) for r in trail)))

    failed = sum(1 for ok_, _, _ in checks if not ok_)
    print("\n" + "=" * 72)
    for ok_, label, detail in checks:
        print("%s %s" % ("PASS" if ok_ else "FAIL", label))
        if detail and not ok_:
            print("      %s" % detail)
        elif detail:
            print("      %s" % detail)
    print("=" * 72)
    print("%d checks, %d failed" % (len(checks), failed))
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
