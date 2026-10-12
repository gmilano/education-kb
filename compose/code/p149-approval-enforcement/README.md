---
industry: education
region: Global
updated: 2026-10-12
---

# `p149-approval-enforcement` — `ACTION FD`: the gate is real, fail-closed, and bypassable

> 🟡 **`ACTION FD`** — write the **enforcement** half of `P35`: a test that
> `mcp-student-records` actually refuses an approval-gated write without approval, rather than
> merely declaring `requires_approval = true`. Run the repository's own suite (`cargo test`)
> if the toolchain is reachable.
> 🔴 *Refuted if the Rust toolchain is unavailable in this environment.*

## 🟢 Falsifier silent — the toolchain is here

🟢 **`cargo 1.97.0`, `rustc 1.97.0`.** 🟢 **`cargo fetch` resolved every dependency**, including
the git dependency `adk-mcp-sdk` pinned at rev `4dac4301`, and 🟢 **the repository's own suite
runs and passes: 24 tests** (`integration_test` 10, `manifest_test` 5, `v11_test` 9).
🟢 **This file adds 7, for 31 passing.**

    cp p149_approval_enforcement.rs <clone>/tests/ && cargo test --offline

## 🟢 The gate exists, and it is better than `P35` claimed

🔵 **p148 could only say the manifest *declares* approval.** Reading the SDK settles what the
declaration does. `mcp_2026_server!` generates `ServerHandler::call_tool`, and its **first**
action — before the router, before any task dispatch — is:

    if let Some(response) = $crate::approval_gate(&request, &context, &policy)? {
        return Ok(response);
    }

🟢 **`approval_gate` is fail-closed on three independent conditions**:

| # | condition | what happens if it fails |
|---|---|---|
| 1 | the tool is in `approval_tools` | not gated → passes straight through |
| 2 | protocol version **is** `2026-07-28` | 🔴 **`invalid_request`** — *"this protected tool requires MCP 2026-07-28 MRTR approval"* |
| 3 | a **sealed** `request_state` that matches **this caller and this tool** | 🔴 **`invalid_request`** — *"approval state does not match this caller or tool"* |
| 4 | `input_responses["approval"]["action"] == "accept"` | 🔴 **`invalid_request`** — *"protected operation was not approved"* |

🟢 **First call returns an `input_required` response** carrying freshly sealed state, so
approval cannot be forged by replaying another caller's token. 🟢 **This is a genuinely
strong gate** and `P35` understated it.

## 🆕 🟢 A THIRD surface agrees — and nobody tests that either

🔴 **p148 found two surfaces at 46 and pinned them.** There is a third:

| surface | what it declares | count |
|---|---|---|
| `mcp-server.toml` `[[tools]]` | per-tool `requires_approval` | **46 tools, 23 true** |
| `src/server.rs` `#[tool_router]` | `#[tool(…)]` sites | **46** |
| 🆕 `src/server.rs` `mcp_2026_server!` | `approval_tools: [...]` | 🆕 **23** |

🟢 **The manifest's 23 `requires_approval = true` names are SET-IDENTICAL to the macro's 23
`approval_tools`** — symmetric difference empty both ways, no duplicates on either side.
🟢 **So the row is three-way consistent**, which is the best-governed thing on this shelf.

🔴 **And the repository asserts none of it.** `manifest_test.rs` checks `requires_approval`
for **11 named tools** (4 + 7) out of 23, 🔴 **never the set**, 🔴 **never against the macro**,
and 🔴 **never behaviour**. 🔵 **So `P35`'s CI gate should pin three surfaces, not two** — and
the 23-name approval set is a second contract, independent of the 46-name tool set.

## 🔴 The finding: the gate is bypassable in-process

🔴 **The gate lives at the protocol boundary and nowhere else.** The write methods are
reachable without it:

    pub struct StudentServer { pub store: Arc<StudentStore> }   // both pub
    pub fn place_hold(&self, student_id: &str, kind: &str, …)   // on StudentStore, pub

🟢 **The tool methods on `StudentServer` are private** (`fn place_hold`, not `pub fn`), so an
external crate cannot call *them* — 🔵 **which is good design and worth crediting.** 🔴 **But
`StudentServer` has no constructor and needs none**: the struct and its `store` field are both
`pub`, so any crate can build one and reach straight past `call_tool`.

🟢 **Six distinct gated writes succeed with no approval, no protocol version and no sealed
state**, proved by test: `add_accommodation`, `place_hold`, `add_guardian`,
`send_communication`, `raise_flag`, `set_student_status`. 🔵 **`place_hold` returns a hold with
`active == true`** — live, not staged.

🟢 **The one mitigation, stated precisely**: the bypassed write **is still FERPA-logged**.
`StudentStore::place_hold` calls `log_access` on its own, so the entry appears in
`access_log_for(student_id)` with the bypassing actor's name. 🔵 **The audit trail survives
the bypass; the approval does not.**

## 🔵 What this means for `P35`, said plainly

| claim | status after `ACTION FD` |
|---|---|
| the manifest and router agree on 46 names | 🟢 **proved by p148** |
| the manifest and the macro agree on 23 gated names | 🟢 **proved here** |
| a gated tool CALL is refused without approval | 🟢 **proved by reading the SDK; fail-closed on 3 conditions** |
| a gated WRITE is refused without approval | 🔴 **FALSE — bypassable via the public store** |

🔵 **`P35` is sound as an MCP-surface gate and must not be sold as a data-layer control.** A
client embedding this crate, rather than running it as a server, gets the audit log and not
the approval. 🟢 **The fix is one visibility change plus a store-level guard**, and the tests
here assert the *current* behaviour so they fail loudly when it lands. 🟢 **`ACTION FF` is
registered for it.**

🔴 **The limit of this measurement, stated**: a full protocol round-trip — a real
`RequestContext` at version `2026-07-28` with sealed state — is **not** exercised here.
Constructing one needs a live client session, so conditions 2–4 are established by **reading
the SDK source at the pinned rev**, not by running them. 🟢 **Condition 1 and the bypass are
executed.**

## Files

| file | what it is |
|---|---|
| `p149_approval_enforcement.rs` | **7 tests**; copy into the subject's `tests/`, `cargo test --offline` |
