//! p151 / ACTION FF — p149's data-layer bypass, as an integration test.
//!
//! An integration test is its OWN CRATE, so it sees exactly what a downstream consumer
//! sees. On HEAD it compiles and the gated write succeeds with no approval, no protocol
//! version and no sealed request state. After the patch (`store` made private) this file
//! must FAIL TO COMPILE — that compile failure is the test holding the fix.
use mcp_student_records::server::StudentServer;
use mcp_student_records::store::StudentStore;
use std::sync::Arc;

#[test]
fn gated_write_is_reachable_without_approval() {
    let store = Arc::new(StudentStore::new());
    let server = StudentServer { store };
    let h = server
        .store
        .place_hold("STU-1001", "FINANCIAL", "p151 bypass probe", "nobody@nowhere")
        .expect("place_hold must not require approval on HEAD");
    assert!(h.active, "the bypassed hold is active");
    let log = server.store.access_log_for("STU-1001");
    assert!(
        log.iter().any(|e| e.action == "place_hold"),
        "the bypassed write is still FERPA-logged"
    );
}
