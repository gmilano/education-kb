//! p151 / ACTION FF — the positive control for the patch: the legitimate construction
//! path still exists and still works, so the fix is not a regression.
use mcp_student_records::server::StudentServer;
use mcp_student_records::store::StudentStore;
use std::sync::Arc;

#[test]
fn constructor_is_the_only_way_in() {
    let store = Arc::new(StudentStore::new());
    let _server = StudentServer::new(store);
}
