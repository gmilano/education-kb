---
industry: education
region: Global
updated: 2026-10-12
---

# p147-scope-parity — `ACTION EG` refuted, and the action's own premise is the defect

`P145-J` found `ahmedEid1/lumen` pinning **tools → scopes** and never the reverse:

    for tool_name in all_tool_names():
        assert tool_name in md["scopes_supported"]      # tests/test_mcp_auth.py:338

`ACTION EG` asked for the missing half, *refuted if the two sets are not equal — which
would mean lumen's OAuth vocabulary and its tool registry have already drifted, and
`P145-J` has found a pin that does not hold.*

    python3 scope_parity.py <lumen-checkout>
    python3 test_scope_parity.py        # 9 tests, authored fixtures, offline

## 🔴 REFUTED on the letter, and the consequence clause is wrong

| property | value |
|---|---|
| `all_tool_names()` | **9** |
| `scopes_supported` | **10** |
| raw set equality | 🔴 **False** |
| equality modulo the wildcard | 🟢 **True** |
| scopes with no tool | 🟢 **none** |
| tools with no scope | 🟢 **none** |

🔴 **The extra element is `WILDCARD_SCOPE = "*"`** (`app/models/mcp_client.py:88`) — a
designed element, not drift. `set(scopes_supported) - {"*"} == set(all_tool_names())`
holds, 9 == 9, with **zero orphans in either direction**.

🔵 **So a bidirectional equality assertion would FAIL on a correct repository**, which makes
the test `ACTION EG` specified the wrong test. 🟢 **The assertion that catches both
directions names the wildcard instead of counting past it**, and this probe is that
assertion, extracted so it can be run rather than argued about. 🟢 **`P145-J`'s pin holds.**

## 🔴 The deployment finding, independent of the set algebra

`has_scope()` short-circuits on the wildcard (`app/mcp/principal.py:87`), and `"*"` is the
**shipped default** on two of the three paths that mint a client:

| path | default scopes |
|---|---|
| `app/api/v1/admin_mcp_clients.py:66` | 🔴 `Field(default_factory=lambda: [WILDCARD_SCOPE])` |
| `app/cli.py:478` | 🔴 `scope_list = [WILDCARD_SCOPE]` |
| `issue_token` with an explicit list | 🟢 intersected against the grant (`auth.py:102`) |

🔴 **So the per-tool OAuth vocabulary is, by default, not enforced.**

🟢 **The posture gate is a real second gate and still applies.** The wildcard bypasses
`has_scope` only; `spec.auth == "admin"` still requires `principal.is_admin`
(`app/mcp/server.py:123`). 🔵 **That is the difference between "misconfigured" and "open",
and it is why this is a warning and not a vulnerability.**

| tool | posture | reachable with `"*"` and no elevated role |
|---|---|---|
| `list_courses`, `get_course` | `public` | 🟢 yes, and read-only |
| `search_lesson_content`, `ask_tutor`, `list_my_due_reviews`, `list_my_progress` | `user` | 🟢 yes, read-only |
| 🔴 **`grade_review_card`** | `user` | 🔴 **yes — and it changes a student's record** |
| 🔴 **`create_course_draft`** | `user` | 🔴 **yes** |
| `ingest_url_to_draft` | `admin` | 🟢 **no** — the one posture-gated tool |

🔴 **8 of 9 tools are reachable with a wildcard token held by any authenticated principal**,
two of them writes. 🔵 **For a school deployment the actionable line is: mint MCP clients
with an explicit scope list, never the default.**
