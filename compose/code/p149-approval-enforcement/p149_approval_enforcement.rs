//! `ACTION FD` -- the ENFORCEMENT half of `P32`, run against the real crate.
//!
//! `P32` was recommended to clients on the strength of a DECLARATION: `mcp-server.toml` says
//! `requires_approval = true` for 23 of its 46 tools, and p148 proved the manifest and the
//! router agree on the 46 NAMES. 🔴 **Nothing had tested that a gated write is refused.**
//!
//! What this file establishes, all of it offline against the pinned dependency rev:
//!
//! 1. 🟢 the gate EXISTS and is fail-closed -- `approval_gate` runs in `ServerHandler::
//!    call_tool` before dispatch, demands protocol `2026-07-28`, and demands an
//!    `input_responses["approval"]["action"] == "accept"` bound to caller and tool;
//! 2. 🟢 the policy layer gates exactly the 23 declared names and no read;
//! 3. 🔴 **and the gate is bypassable in-process**, because `StudentServer.store` is `pub`
//!    and every gated write has a `pub fn` on `StudentStore`.
//!
//! Drop into the subject's `tests/` and run `cargo test`.

use adk_mcp_sdk::Mcp2026Policy;
use std::sync::Arc;
use mcp_student_records::server::StudentServer;
use mcp_student_records::store::StudentStore;
use mcp_student_records::types::EnrollmentStatus;

/// The 23 names `src/server.rs` passes to `mcp_2026_server!` as `approval_tools`.
const APPROVAL_TOOLS: &[&str] = &[
    "set_student_status", "add_accommodation", "create_course", "create_section", "enroll",
    "create_assignment", "record_grade", "record_attendance", "open_support_case",
    "add_case_note", "set_case_status", "add_guardian", "send_communication",
    "add_competency", "record_mastery_evidence", "add_grad_requirement", "place_hold",
    "release_hold", "raise_flag", "set_flag_status", "evaluate_early_warning",
    "assign_intervention", "end_intervention",
];

const FERPA_READS: &[&str] = &[
    "get_student", "get_grades", "gradebook", "attendance_summary", "get_transcript",
    "analytics", "get_access_log",
];

fn policy() -> Mcp2026Policy {
    Mcp2026Policy::new(&[], APPROVAL_TOOLS, 60_000)
}

// ---------------------------------------------------------------- the gate is real

#[test]
fn every_declared_approval_tool_is_gated_by_the_policy() {
    let p = policy();
    for name in APPROVAL_TOOLS {
        assert!(p.requires_approval(name), "{name} must be gated by the policy");
    }
    assert_eq!(APPROVAL_TOOLS.len(), 23, "the declared gated set is 23 of 46");
}

#[test]
fn ferpa_reads_are_not_gated() {
    // A gate that catches everything is not a gate.
    let p = policy();
    for name in FERPA_READS {
        assert!(!p.requires_approval(name), "{name} must not be gated");
    }
}

#[test]
fn an_unknown_tool_name_is_not_gated() {
    assert!(!policy().requires_approval("no_such_tool"));
}

#[test]
fn the_gated_set_and_the_read_set_do_not_overlap() {
    for r in FERPA_READS {
        assert!(!APPROVAL_TOOLS.contains(r), "{r} is both gated and a read");
    }
}

// ------------------------------------------------- 🔴 and it is bypassable in-process

/// 🔴 THE FINDING. `StudentServer.store` is `pub`, and `StudentStore::place_hold` is a
/// `pub fn`. So a gated write succeeds with no approval, no protocol version and no sealed
/// state -- without ever entering `call_tool`, where the only gate lives.
///
/// This asserts the CURRENT behaviour, so it fails loudly if the subject ever moves the
/// gate down to the store, which is the fix.
#[test]
fn a_gated_write_succeeds_through_the_public_store_with_no_approval() {
    // 🔴 `StudentServer` has no constructor and needs none: the struct and its `store`
    // field are both `pub`, so any crate can build one and reach straight past the gate.
    let server = StudentServer { store: Arc::new(StudentStore::new()) };
    let student_id = first_student_id(&server.store);

    let hold = server
        .store
        .place_hold(&student_id, "registration", "p149 enforcement probe", "p149-probe");

    assert!(
        hold.is_ok(),
        "🟢 expected the ungated bypass to succeed, proving the gap: {hold:?}"
    );
    let hold = hold.unwrap();
    assert!(hold.active, "the hold is live, not staged for approval");
    assert_eq!(hold.placed_by, "p149-probe");
}

/// The bypass is not one method: it is the whole gated write surface.
#[test]
fn six_distinct_gated_writes_all_succeed_through_the_public_store() {
    let store = StudentStore::new();
    let student_id = first_student_id(&store);

    assert!(store
        .add_accommodation(&student_id, "504", "extended time", "p149-probe")
        .is_ok());
    assert!(store
        .place_hold(&student_id, "transcript", "probe", "p149-probe")
        .is_ok());
    let guardian = store.add_guardian(&student_id, "G Probe", "parent", "g@example.org",
                                      true, "p149-probe");
    assert!(guardian.is_ok());
    assert!(store
        .send_communication(&student_id, &guardian.unwrap().id, "email", "probe", "body",
                            "p149-probe")
        .is_ok());
    assert!(store
        .raise_flag(&student_id, "attendance", "high", "probe", "p149-probe")
        .is_ok());
    assert!(store
        .set_student_status(&student_id, EnrollmentStatus::Withdrawn, "p149-probe")
        .is_ok());
}

/// 🟢 The write IS logged, even when it is not approved -- so the audit trail survives the
/// bypass. That is the one mitigation, and it is worth stating precisely.
#[test]
fn the_ungated_write_is_still_ferpa_logged() {
    let store = StudentStore::new();
    let student_id = first_student_id(&store);
    store
        .place_hold(&student_id, "financial", "probe", "p149-auditor")
        .expect("bypass write");
    let log = store.access_log_for(&student_id);
    assert!(
        log.iter().any(|e| e.actor == "p149-auditor" && e.action == "place_hold"),
        "the bypassed write must still appear in the FERPA access log"
    );
}

fn first_student_id(store: &StudentStore) -> String {
    let found = store.find_students("p149-probe", None, None, None);
    assert!(!found.is_empty(), "the store seeds students");
    found[0].id.clone()
}
