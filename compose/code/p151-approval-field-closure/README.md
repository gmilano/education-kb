# `p151-approval-field-closure` — `ACTION FF`: `P35`'s data-layer gap, closed

🟢 **DISCHARGED, falsifier SILENT.** 🔵 **The highest-consequence item on this shelf, open
for three passes, and two lines of the subject's own code close it.**

Subject: [`zavora-ai/mcp-student-records`](https://github.com/zavora-ai/mcp-student-records)
**v1.2.0**, Apache-2.0, depth-1 clone at this pass's HEAD. `cargo 1.97.0` / `rustc 1.97.0`.

## The exact change

```diff
-pub struct StudentServer { pub store: Arc<StudentStore> }
+pub struct StudentServer { store: Arc<StudentStore> }
+
+impl StudentServer {
+    pub fn new(store: Arc<StudentStore>) -> Self { Self { store } }
+}
```
```diff
-    let server = StudentServer { store };
+    let server = StudentServer::new(store);
```

🟢 **One call site in the whole repository** (`src/main.rs:14`). The repo's own 24 tests
never construct a `StudentServer`, so nothing else moves. Full diff:
[`field-privacy.patch`](field-privacy.patch).

## The failing test that holds it

🔵 **A Rust integration test is its own crate**, so it sees exactly what a downstream
consumer sees — and p149 demonstrated its bypass from `tests/`. The bypass it demonstrated
*is* the bypass a consumer has, and `pub`/private is exactly the boundary that closes it.

| tree | [`p151_bypass.rs`](p151_bypass.rs) | the repository's own suite |
|---|---|---|
| **HEAD** | 🔴 **compiles and PASSES** — `place_hold` returns `active == true` with no approval, no protocol version, no sealed request state. 🟢 And the bypassed write *is* still FERPA-logged, asserted | 🟢 **24 pass** |
| **patched** | 🟢 **FAILS TO COMPILE** — `E0616` ×2 on the two field reads, `E0451` on the struct literal | 🟢 **24 pass**, plus [`p151_legit.rs`](p151_legit.rs), the constructor control |

Transcript: [`result.2026-10-12-p151.txt`](result.2026-10-12-p151.txt). 🔵 **An honest note
on observation order**: within one file rustc reported only the two `E0616`s; `E0451`
appears as its own test target's error. Both surfaces are closed; the *reporting* is
ordered, not the closure.

🟢 **And a gate that is itself the failing test**, for CI, with no new dependency:
[`field_gate.py`](field_gate.py) returns **1** on HEAD and **0** on the patched tree.

```
$ python3 field_gate.py .../head
approval_tools=23  field=PUB  constructor=no  in-crate .store reads=0
  FAIL 1. StudentServer.store is PUB — every consumer can bypass the gate     # exit 1

$ python3 field_gate.py .../patched
approval_tools=23  field=PRIVATE  constructor=yes  in-crate .store reads=0
  OK   the data layer is reachable only through the tool router               # exit 0
```

## 🔴 What this does NOT close, said rather than implied — 🆕 `T83`

🔴 **An IN-CRATE bypass remains.** `pub`/private is a *module* boundary: a future module
inside `mcp-student-records` can still reach `self.store` and call a `pub fn` write on
`StudentStore`. Closing that needs the action's second option — a sealed approval token
minted only by the gate and threaded into all **23** write signatures — a 23-site change
to a repository this KB does not own.

🟢 **So the recommendation splits, and `P35` now says so:** ship the two-line privacy
change, and hold the in-crate surface with this gate in CI. Condition 3 of the gate is
exactly that check, and `test_field_gate.py` exercises it on a fixture crate whose field
is private and which reaches the store from another module anyway.

- instrument: [`field_gate.py`](field_gate.py) · **19 tests**, all offline, authored crates
- the enforcement half this builds on: [`../p149-approval-enforcement`](../p149-approval-enforcement/README.md)

```
python3 test_field_gate.py
python3 field_gate.py /path/to/mcp-student-records
```
