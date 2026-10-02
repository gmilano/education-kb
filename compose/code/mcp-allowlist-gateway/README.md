# `mcp-allowlist-gateway` — the generic P85 piece (gap 103, closed in pass 48)

**What this is:** the allowlist gateway **P85** documents in `compose/patterns.md` and
which **pass 47 found was not in this repository**. P85 claimed *«175 líneas, escrito y
probado»*; the code was in the pattern's prose, under the documented variable name
`MCP_ALLOWLIST`, and nowhere in `compose/code/`. This directory is that piece, written,
run and measured.

```
python3 test_gateway.py        # 34/34, stdlib only, no network, no Docker
```

## Why it could not be extracted from the two existing gates

Pass 47's action said to extract the generic gateway from
`../sebserver-mcp-gate/gate.py` and `../unitime-mcp-gate/gate.py`. **That turns out to be
the wrong factoring, and the reason is architectural rather than cosmetic:**

| | the two concrete gates | this gateway |
|---|---|---|
| Role | **they ARE the upstream** | **it PROXIES an upstream** |
| Tool manifest | synthesized from a surface measured out of a checkout (`operations.tsv`, `connectors.tsv`) | unknown until the upstream answers `tools/list` |
| Trust in upstream | total — it is their own code | none — third-party, unmeasurable, may change under them |
| What P85's wiring describes | — | ✅ `gateway.py -- npx -y frappe-mcp-server` |

A gateway that proxies cannot be a copy of a gateway that serves. **What the two shapes
genuinely share is the DECISION**, so that is what was extracted, into `policy.py`, and
both shapes are expressed on top of it.

## The files

| File | raw | non-blank | non-blank-non-comment | What it is |
|---|---|---|---|---|
| `policy.py` | 105 | 83 | **76** | The decision core, transport-free. Default deny, exact names, floor-wins |
| `gateway.py` | 128 | 113 | **108** | The stdio proxy P85 wires. `MCP_ALLOWLIST`, `MCP_HARD_DENY`, `MCP_AUDIT_LOG` |
| `fake_upstream.py` | 71 | 59 | 58 | A stand-in for `frappe-mcp-server`'s 7 tools that **counts its own executions** |
| `test_gateway.py` | 215 | 191 | 185 | The 34 checks |

🔴 **The shippable piece is `policy.py` + `gateway.py` = 233 raw / 196 non-blank / 184
non-blank-non-comment. P85's «175 líneas» is still not any of those numbers**, so the
claim is replaced rather than rescued. Every figure above names its instrument, which is
what **gap 101** asked for.

## The three rules

1. **Default deny.** Unset or empty `MCP_ALLOWLIST` ⇒ zero tools exposed, every call
   refused. There is no value of the variable meaning "expose everything".
2. **Exact names.** No globs, no prefixes: `preview_submit_assignment` in the allowlist
   does not admit `submit_assignment`, and a literal `delete_*` matches nothing.
3. **The floor wins.** A name in `MCP_HARD_DENY` is refused *though an operator put it in
   the allowlist*. This is **pass 45's floor**, and P85's inline code did not have it. The
   case that forces it: UniTime's `GET /api/script` delegates to `doPost`, so no
   read/write policy can protect it.

Enforcement is at **two** points and **only the second is a control**: trimming
`tools/list` hides a tool, but refusing `tools/call` **before the call reaches the
upstream** is what makes this a compliance control. The suite measures that distinction
**at the upstream** — `fake_upstream.py` appends every execution to
`MCP_UPSTREAM_COUNTER`, so *«no llegó al upstream»* is a measurement, not an inference.

## What the 34 checks cover

- **(A) P85's published verification table, converted from prose into assertions** —
  7 upstream tools → 3 exposed; the allowed call runs; `delete_document` and
  `call_method` both refused `-32601`; **neither reached the upstream**; total upstream
  executions **1**; `initialize` passes through untouched. Plus default deny: empty
  allowlist ⇒ 0 exposed, 3/3 blocked, 0 reached the upstream.
- **(B) The floor** — a floored tool is neither advertised nor served *even when
  allowlisted*, does not reach the upstream, and **never appears in `data.allowed`**.
- **(C) 🟢 EQUIVALENCE with the two concrete gates — the control that makes the
  extraction honest.** `policy.Policy` re-derives both partitions and must agree
  tool-for-tool: **UniTime 26 tools → 13 exposed, identical, 0 disagreements**, floor
  `{unitime.script.get}` reproduced; **seb-server 341 operations → 162 exposed,
  identical, 0 disagreements**, whole write surface withheld. Both floors are non-empty,
  so the agreement is not vacuous. This is pass 31's rule applied to an extraction: a
  method that declares equivalence must be run against a case already known.
- **(D)** Anti-glob, `parse_allowlist` edge cases, and that no `_`-prefixed decision
  metadata ever reaches `tools/list`.

## Corrections this piece forced on the KB

1. 🔴 **P85's «175 líneas» is unsupported by any instrument** — see the table above.
2. 🔴 **Pass 47 wrote that the two gates measure «145 y 145 no-blancas».** The value 145
   is right and **the metric name is wrong**: by `grep -cve '^[[:space:]]*$'` they are
   **162** and **146**; **145/145 is non-blank-NON-COMMENT**. The defect gap 101 named —
   a figure published without its instrument — recurred *inside pass 47's own correction
   of it*.
3. 🔴 **Pass 47 cites this suite's sibling as «`unitime-mcp-gate/` (46)».** 46 is that
   suite's **check** count; its **manifest is 26 tools**. A bare parenthesized number is
   not a measurement.

## Limits, declared

- **Surface control, not authorization.** It does not replace the LMS's permissions or
  the token's role: an allowed tool can still do whatever the token permits.
- **stdio transport only.** For an HTTP upstream the same filter belongs in a reverse
  proxy; **that code is not written here** and must not be presented as if it were.
- **The audit log is ordered per direction, not globally serialized.** `c2u` and `u2c`
  are separate threads, so a `tool_call_blocked` can be written before the
  `tools_list_filtered` of an earlier request id. Each line is individually accurate and
  carries `ts` + `request_id`; **an auditor must sort, not assume file order.**
- **The floor must be stated by name** (`MCP_HARD_DENY`). When proxying a third-party
  upstream there is no measured metadata to derive it from — that derivation is available
  only to the manifest-driven gates, which is exactly why `hard_deny()` takes both a
  predicate and a name list.
