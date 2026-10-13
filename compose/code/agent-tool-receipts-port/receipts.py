#!/usr/bin/env python3
"""Pass 183, ACTION LV. A minimal runnable port of civil-ai's auditable
assessment record: `assessment_policy_versions` + `agent_tool_receipts`,
with the status state machine, version-checked concurrency and the
`ON DELETE RESTRICT` policy FK that makes the record non-erasable.

Ported by reading, not by running. Source:
  zhangl1001/civil-ai @ 37ba5e2 (MIT)
    web/src/capabilities/database/migrations/001_foundation.sql
    web/src/capabilities/database/migrations/032_agent_tool_receipts.sql
    web/src/modules/agent/adapters/SqliteAgentToolReceiptRepository.ts
    web/src/modules/agent/adapters/IndexedDbAgentToolReceiptRepository.ts

Stdlib only (sqlite3). No network, no registry install.

Run:  python3 test_receipts.py
"""
from __future__ import annotations

import hashlib
import sqlite3

# ---------------------------------------------------------------------------
# Schema. Column names and CHECK vocabularies are the source's, verbatim where
# the source has them; the parent tables are reduced to the columns the two
# audit tables actually need.
# ---------------------------------------------------------------------------

SCHEMA = """
CREATE TABLE metadata_packages (
  id         TEXT PRIMARY KEY NOT NULL,
  label      TEXT NOT NULL,
  created_at INTEGER NOT NULL CHECK(created_at >= 0)
);

CREATE TABLE assessment_policy_versions (
  id                  TEXT PRIMARY KEY NOT NULL,
  metadata_package_id TEXT NOT NULL REFERENCES metadata_packages(id) ON DELETE RESTRICT,
  subject             TEXT NOT NULL,
  policy_type         TEXT NOT NULL,
  version             TEXT NOT NULL,
  config_json         TEXT NOT NULL,
  content_hash        TEXT NOT NULL CHECK(length(content_hash) >= 16),
  status              TEXT NOT NULL CHECK(status IN ('draft', 'published', 'retired')),
  created_at          INTEGER NOT NULL CHECK(created_at >= 0),
  UNIQUE(subject, policy_type, version)
);

CREATE TABLE exam_cycles (
  id         TEXT PRIMARY KEY NOT NULL,
  exam_name  TEXT,
  created_at INTEGER NOT NULL CHECK(created_at >= 0)
);

-- The anchor. A policy version that a cycle is BOUND to cannot be deleted:
-- the grading decision keeps its rule reachable for as long as the binding
-- exists. This is the FK that turns a schema into an audit record.
CREATE TABLE exam_cycle_policy_bindings (
  exam_cycle_id                TEXT NOT NULL REFERENCES exam_cycles(id) ON DELETE CASCADE,
  subject                      TEXT NOT NULL,
  policy_type                  TEXT NOT NULL,
  assessment_policy_version_id TEXT NOT NULL REFERENCES assessment_policy_versions(id) ON DELETE RESTRICT,
  bound_at                     INTEGER NOT NULL CHECK(bound_at >= 0),
  PRIMARY KEY(exam_cycle_id, subject, policy_type)
);

CREATE TABLE tutor_agent_runs (
  id         TEXT PRIMARY KEY NOT NULL,
  status     TEXT NOT NULL CHECK(status IN ('queued', 'running', 'waiting_user', 'succeeded', 'failed')),
  version    INTEGER NOT NULL DEFAULT 1 CHECK(version >= 1),
  created_at INTEGER NOT NULL CHECK(created_at >= 0)
);

CREATE TABLE agent_tool_receipts (
  agent_run_id             TEXT NOT NULL REFERENCES tutor_agent_runs(id) ON DELETE CASCADE,
  tool_call_id             TEXT NOT NULL,
  tool_name                TEXT NOT NULL,
  arguments_hash           TEXT NOT NULL,
  business_idempotency_key TEXT NOT NULL,
  status                   TEXT NOT NULL CHECK(status IN ('prepared', 'running', 'succeeded', 'failed', 'unknown')),
  result_json              TEXT,
  result_ref               TEXT,
  failure_code             TEXT,
  retryable                INTEGER NOT NULL DEFAULT 1 CHECK(retryable IN (0, 1)),
  attempt_count            INTEGER NOT NULL DEFAULT 0 CHECK(attempt_count >= 0),
  lease_epoch              INTEGER NOT NULL DEFAULT 0 CHECK(lease_epoch >= 0),
  created_at               INTEGER NOT NULL,
  updated_at               INTEGER NOT NULL,
  completed_at             INTEGER,
  version                  INTEGER NOT NULL DEFAULT 0 CHECK(version >= 0),
  PRIMARY KEY(agent_run_id, tool_call_id)
);

CREATE INDEX agent_tool_receipts_status_idx
  ON agent_tool_receipts(status, updated_at);

CREATE INDEX agent_tool_receipts_business_key_idx
  ON agent_tool_receipts(business_idempotency_key);
"""

# The state machine the source's CHECK constraint names but does not enforce as
# transitions. `unknown` is the honest terminal: the tool was invoked and the
# outcome was never observed. It is NOT a synonym for failure, and a studio that
# collapses it into one loses the only state that says "we do not know whether
# the learner's record changed".
TERMINAL = frozenset({"succeeded", "failed", "unknown"})
LEGAL_TRANSITIONS: dict[str, frozenset[str]] = {
    "prepared": frozenset({"running", "failed", "unknown"}),
    "running": frozenset({"succeeded", "failed", "unknown"}),
    "succeeded": frozenset(),
    "failed": frozenset(),
    "unknown": frozenset(),
}


class ReceiptError(RuntimeError):
    """Base for every refusal this module raises. Refusing is the feature."""


class IllegalTransition(ReceiptError):
    pass


class StaleWrite(ReceiptError):
    pass


class RunNotRunning(ReceiptError):
    pass


def connect(path: str = ":memory:") -> sqlite3.Connection:
    """Open a connection with the schema applied.

    PRAGMA foreign_keys is OFF by default in SQLite, and with it off the
    ON DELETE RESTRICT above is decorative. Every caller gets it ON here, and
    `test_receipts.py` asserts what happens when it is not.
    """
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    conn.executescript(SCHEMA)
    return conn


def content_hash(config_json: str) -> str:
    """>= 16 chars, per the source's CHECK. sha256 hex is 64."""
    return hashlib.sha256(config_json.encode("utf-8")).hexdigest()


def publish_policy_version(
    conn: sqlite3.Connection,
    *,
    policy_id: str,
    metadata_package_id: str,
    subject: str,
    policy_type: str,
    version: str,
    config_json: str,
    now: int,
    status: str = "published",
) -> str:
    conn.execute(
        """INSERT INTO assessment_policy_versions(
             id, metadata_package_id, subject, policy_type, version,
             config_json, content_hash, status, created_at)
           VALUES(?,?,?,?,?,?,?,?,?)""",
        (
            policy_id,
            metadata_package_id,
            subject,
            policy_type,
            version,
            config_json,
            content_hash(config_json),
            status,
            now,
        ),
    )
    return policy_id


def bind_policy(
    conn: sqlite3.Connection,
    *,
    exam_cycle_id: str,
    subject: str,
    policy_type: str,
    policy_id: str,
    now: int,
) -> None:
    conn.execute(
        """INSERT INTO exam_cycle_policy_bindings(
             exam_cycle_id, subject, policy_type,
             assessment_policy_version_id, bound_at)
           VALUES(?,?,?,?,?)""",
        (exam_cycle_id, subject, policy_type, policy_id, now),
    )


def prepare_receipt(
    conn: sqlite3.Connection,
    *,
    agent_run_id: str,
    tool_call_id: str,
    tool_name: str,
    arguments_hash: str,
    business_idempotency_key: str,
    now: int,
) -> bool:
    """Idempotent prepare. Returns True if this call created the row.

    The source uses INSERT OR IGNORE for exactly this: a retried prepare of the
    same (run, tool_call) is a no-op rather than a duplicate or an error.
    """
    cur = conn.execute(
        """INSERT OR IGNORE INTO agent_tool_receipts(
             agent_run_id, tool_call_id, tool_name, arguments_hash,
             business_idempotency_key, status, retryable, attempt_count,
             lease_epoch, created_at, updated_at, version)
           VALUES(?,?,?,?,?,'prepared',1,0,0,?,?,0)""",
        (
            agent_run_id,
            tool_call_id,
            tool_name,
            arguments_hash,
            business_idempotency_key,
            now,
            now,
        ),
    )
    return cur.rowcount == 1


def get_receipt(
    conn: sqlite3.Connection, agent_run_id: str, tool_call_id: str
) -> sqlite3.Row | None:
    return conn.execute(
        "SELECT * FROM agent_tool_receipts WHERE agent_run_id=? AND tool_call_id=?",
        (agent_run_id, tool_call_id),
    ).fetchone()


def transition_receipt(
    conn: sqlite3.Connection,
    *,
    agent_run_id: str,
    tool_call_id: str,
    to_status: str,
    expected_version: int,
    now: int,
    result_json: str | None = None,
    result_ref: str | None = None,
    failure_code: str | None = None,
    retryable: bool | None = None,
    lease_epoch: int | None = None,
) -> sqlite3.Row:
    """Advance one receipt, refusing every write the source refuses.

    Three independent guards, each of which the source has:
      1. the transition must be legal for the current status;
      2. `expected_version` must match the stored version (optimistic
         concurrency) -- the source additionally requires the new version to be
         exactly expected + 1, which is what this function writes;
      3. the parent run must still be 'running'. A receipt cannot be advanced
         under a run that has finished or lost its lease.
    """
    if to_status not in LEGAL_TRANSITIONS:
        raise IllegalTransition(f"unknown status {to_status!r}")

    row = get_receipt(conn, agent_run_id, tool_call_id)
    if row is None:
        raise ReceiptError(f"no receipt for {agent_run_id}/{tool_call_id}")

    current = row["status"]
    if to_status not in LEGAL_TRANSITIONS[current]:
        raise IllegalTransition(
            f"{current} -> {to_status} is not a legal transition"
            + (" (terminal)" if current in TERMINAL else "")
        )
    if row["version"] != expected_version:
        raise StaleWrite(
            f"expected version {expected_version}, stored is {row['version']}"
        )

    run = conn.execute(
        "SELECT status FROM tutor_agent_runs WHERE id=?", (agent_run_id,)
    ).fetchone()
    if run is None or run["status"] != "running":
        raise RunNotRunning(
            f"run {agent_run_id} is {run['status'] if run else 'absent'}, not running"
        )

    next_version = expected_version + 1
    completed_at = now if to_status in TERMINAL else None
    lease_predicate = ""
    params: list[object] = [
        to_status,
        result_json,
        result_ref,
        failure_code,
        1 if (retryable if retryable is not None else bool(row["retryable"])) else 0,
        row["attempt_count"] + (1 if to_status == "running" else 0),
        lease_epoch if lease_epoch is not None else row["lease_epoch"],
        now,
        completed_at,
        next_version,
        agent_run_id,
        tool_call_id,
        expected_version,
    ]
    if lease_epoch is not None:
        lease_predicate = " AND lease_epoch <= ?"
        params.append(lease_epoch)

    cur = conn.execute(
        f"""UPDATE agent_tool_receipts SET
              status=?, result_json=?, result_ref=?, failure_code=?, retryable=?,
              attempt_count=?, lease_epoch=?, updated_at=?, completed_at=?, version=?
            WHERE agent_run_id=? AND tool_call_id=? AND version=?{lease_predicate}""",
        params,
    )
    if cur.rowcount != 1:
        # Lost the race between the SELECT above and this UPDATE.
        raise StaleWrite("concurrent writer won; version no longer matches")

    out = get_receipt(conn, agent_run_id, tool_call_id)
    assert out is not None
    return out


def audit_trail(conn: sqlite3.Connection, agent_run_id: str) -> list[sqlite3.Row]:
    """Every tool the agent invoked under one run, with the rule still bound."""
    return list(
        conn.execute(
            """SELECT r.tool_call_id, r.tool_name, r.status, r.business_idempotency_key,
                      r.attempt_count, r.version, r.completed_at
                 FROM agent_tool_receipts r
                WHERE r.agent_run_id = ?
                ORDER BY r.created_at, r.tool_call_id""",
            (agent_run_id,),
        )
    )
