#!/usr/bin/env python3
"""Suite for `p151-approval-field-closure`. Prints its own total (`P126` point 3).

🔵 **The obligatory case is the gate's own direction**: it must return NON-ZERO on a tree
shaped like the subject's HEAD and ZERO on a tree shaped like the patch. A gate that is
green on both is not a test, and a gate that is red on both would make the patch
unverifiable. Both fixtures are authored here; the real crates are measured in
`result.2026-10-12-p151.txt`.

    python3 test_field_gate.py
"""
import os
import shutil
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import field_gate as G  # noqa: E402

HEAD_SERVER = '''#[derive(Clone)]
pub struct StudentServer { pub store: Arc<StudentStore> }

#[tool_router]
impl StudentServer {
    fn find_students(&self) -> String { self.store.find_students() }
}

adk_mcp_sdk::mcp_2026_server! {
    server: StudentServer,
    task_tools: [],
    approval_tools: ["place_hold", "release_hold", "record_grade"],
    cache_ttl_ms: 60_000,
}
'''
PATCHED_SERVER = HEAD_SERVER.replace(
    "pub struct StudentServer { pub store: Arc<StudentStore> }",
    "pub struct StudentServer { store: Arc<StudentStore> }\n\n"
    "impl StudentServer {\n"
    "    pub fn new(store: Arc<StudentStore>) -> Self { Self { store } }\n}")
NO_CTOR_SERVER = HEAD_SERVER.replace(
    "pub struct StudentServer { pub store: Arc<StudentStore> }",
    "pub struct StudentServer { store: Arc<StudentStore> }")
MAIN_HEAD = "fn main() { let server = StudentServer { store }; }\n"
MAIN_PATCHED = "fn main() { let server = StudentServer::new(store); }\n"
STORE_RS = "pub struct StudentStore {}\nimpl StudentStore { pub fn new() -> Self {} }\n"
# An in-crate module that reaches the store — the surface privacy cannot hold.
SNEAKY_RS = "pub fn audit(s: &StudentServer) { s.store.place_hold(); }\n"

cases = []


def check(name, got, want):
    cases.append((name, got == want, got, want))


def crate(tmp, name, files):
    root = os.path.join(tmp, name, "src")
    os.makedirs(root, exist_ok=True)
    for fn, body in files.items():
        with open(os.path.join(root, fn), "w", encoding="utf-8") as fh:
            fh.write(body)
    return os.path.join(tmp, name)


def main():
    tmp = tempfile.mkdtemp(prefix="p151-ff-")
    try:
        head = crate(tmp, "head", {"server.rs": HEAD_SERVER, "main.rs": MAIN_HEAD,
                                   "store.rs": STORE_RS})
        patched = crate(tmp, "patched", {"server.rs": PATCHED_SERVER,
                                         "main.rs": MAIN_PATCHED,
                                         "store.rs": STORE_RS})

        # ── 1. OBLIGATORY — the gate's direction ─────────────────────────────────────
        check("the gate FAILS on a HEAD-shaped crate", G.gate(head)[0], 1)
        check("the gate PASSES on a patched crate", G.gate(patched)[0], 0)
        check("and the two verdicts differ, which is what makes it a test",
              G.gate(head)[0] != G.gate(patched)[0], True)

        # ── 2. the field read ─────────────────────────────────────────────────────────
        check("HEAD field state", G.field_state(head), "PUB")
        check("patched field state", G.field_state(patched), "PRIVATE")
        check("a crate with no such struct", G.field_state(crate(tmp, "e", {})),
              "ABSENT")
        check("the failure names the reason", "is PUB" in " ".join(G.gate(head)[1]),
              True)

        # ── 3. the constructor condition — privacy without a way in is not a fix ─────
        noctor = crate(tmp, "noctor", {"server.rs": NO_CTOR_SERVER,
                                       "main.rs": MAIN_PATCHED, "store.rs": STORE_RS})
        check("private field with no constructor still FAILS", G.gate(noctor)[0], 1)
        check("and for the right reason",
              any("no public constructor" in b for b in G.gate(noctor)[1]), True)
        check("HEAD has no constructor", G.has_constructor(head), False)
        check("patched has one", G.has_constructor(patched), True)

        # ── 4. the IN-CRATE surface, which privacy cannot hold ───────────────────────
        sneaky = crate(tmp, "sneaky", {"server.rs": PATCHED_SERVER,
                                       "main.rs": MAIN_PATCHED, "store.rs": STORE_RS,
                                       "audit.rs": SNEAKY_RS})
        check("an in-crate .store read FAILS the gate even when the field is private",
              G.gate(sneaky)[0], 1)
        check("and it is named with its line",
              [r for r in G.external_store_reads(sneaky) if r.startswith("audit.rs:")],
              ["audit.rs:1"])
        check("server.rs's own self.store is NOT a finding — it is the router",
              G.external_store_reads(patched), [])

        # ── 5. the denominator the gate reports ──────────────────────────────────────
        check("the approval_tools list is read from the macro",
              G.approval_tools(head),
              ["place_hold", "release_hold", "record_grade"])
        check("and a crate without the macro reports none",
              G.approval_tools(crate(tmp, "e2", {"store.rs": STORE_RS})), [])
        check("the report carries the denominator",
              "approval_tools=3" in G.gate(head)[1][0], True)

        # ── 6. a missing crate must not read as green ────────────────────────────────
        check("a missing crate has no sources",
              G.sources(os.path.join(tmp, "nope")), [])
        check("and its field state is ABSENT, which FAILS",
              G.gate(os.path.join(tmp, "nope"))[0], 1)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    failed = [c for c in cases if not c[1]]
    for name, ok, got, want in cases:
        if not ok:
            print("FAIL  %-58s got=%r want=%r" % (name, got, want))
    print("p151-approval-field-closure: %d tests, %d passed, %d failed"
          % (len(cases), len(cases) - len(failed), len(failed)))
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
