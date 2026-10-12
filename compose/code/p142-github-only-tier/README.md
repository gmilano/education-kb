---
industry: education
region: Global
updated: 2026-10-12
---

# `p142-github-only-tier` — `ACTION DI`: the falsifier did not fire, and the conclusion p141 attached to it is backwards

## The action, as p141 wrote it

> Test `T30` on a third tier: run the `P18`(a)/(b) enumeration over the ten largest
> **GitHub-only** connector rows and report the dynamic-registration share. 🔴 *Refuted if the
> share matches the npm tier's 12% rather than the agent tier's 50% — which would mean the split
> is npm-vs-everything rather than connector-vs-agent, and `T30`'s worked example must be re-cut
> along the right axis.*

The instrument is p141's `surface_gate.py`, **executed unchanged**. Only the population is new.

## Verdict: 🔴 **DISCHARGED. The share is 50% — and `T30` must be re-cut anyway**

| tier | MCP servers | 🔴 dynamic registration | share | gated |
|---|---|---|---|---|
| npm connectors *(p140)* | 8 | 1 | **12%** | 0 |
| agent servers *(p141)* | 4 | 2 | 🔴 **50%** | 0 |
| 🆕 **GitHub-only connectors *(this pass)*** | **6** | 🔴 **3** | 🔴 **50%** | 🔴 **0** |

🔴 **p141 mapped its two outcomes to the wrong conclusions.** Its falsifier says a 12% result
*"would mean the split is npm-vs-everything"*. The opposite is true: these rows are
**connectors** that are **not npm-published**, so a connector-like 12% would have shown the axis
is *connector-vs-agent*, and an agent-like 50% shows the axis is **npm-vs-everything**.

The measurement is 50%. 🔵 **So the falsifier as worded does not fire, while the thing it was
written to detect is exactly what happened.** `T30`'s worked example is re-cut along the
npm-publication axis, and the *mechanism* is left open rather than invented: 🔴 why publishing
to a registry should correlate with literal registration is not established, and asserting a
cause here would be the same mistake one layer up. Registered as `ACTION DL`.

🟢 **`GATED` is now 0 of 18 servers across three tiers.** `T28` belongs to `tutor-mcp`'s
maturity and to nothing else on these shelves — the third tier to say so.

## 🔴 4 of the 10 "connector" rows are not MCP servers at all

| row | verdict |
|---|---|
| `BetterSEQTA/BetterSEQTA-Plus` | 🔴 `NOT_AN_MCP_SERVER` — **0** `mcp` tokens in the tree |
| `BetterSEQTA/DesQTA` | 🔴 `NOT_AN_MCP_SERVER` — **0** tokens |
| `Agso-o/sigaa-calendar` | 🔴 `NOT_AN_MCP_SERVER` — Go, 0 tokens |
| `juliancasaburi/siu-guarani-promedio-extension` | 🔴 `NOT_AN_MCP_SERVER` — a browser extension |

🔵 **With p141's `zijinz456/OpenTutor`, that is 5 rows across two passes shelved beside
connectors they do not resemble.** They remain real software; they have no tool surface to bound,
and a reader taking "connector" from the shelf heading is misled. 🔵 Not one of the four is named
`*-mcp` by accident — two are, and the name is the whole of the evidence that put them there.

## 🆕 🟢 A THIRD registration shape, and the row that uses it ships the best practice on this shelf

`oliverhruby/edupage-mcp` returned `NO_REGISTRATION_SITE_FOUND` — **a server with no visible
registration**. Hand-read, the cause is a shape neither p140 nor p141 has a name for:

```python
def _tool(fn):
    hints = TOOL_ANNOTATIONS.get(fn.__name__)
    if server is not None:
        annotations = ToolAnnotations(**hints) if (hints and ToolAnnotations) else None
        return server.tool(annotations=annotations)(fn)
    return fn
```

🔴 **`REFLECTION`: the tool's name is the Python function's `__name__` and is never written as a
string anywhere.** p141's `REG_PY` requires `@something.tool(...)`; a bare `@_tool` wrapping
`server.tool` matches nothing. 🔵 **`LITERAL` and `DYNAMIC` were never the two options** — this
is a third, and it is invisible to every instrument this KB has built. Registered as
`ACTION DM`. Hand-reading puts the row at **31 tools**, fixed at import, so it is
`BOUNDED_STATIC`; 🟢 **the 50% share is unchanged either way**, which is why the figure is
published.

🟢 **And the row is the exemplar this shelf has been missing.** All **31 of 31** tools carry a
declared MCP `ToolAnnotations` class:

| class | tools | meaning |
|---|---|---|
| 🟢 `_READ` | **19** | read-only |
| `_WRITE_SAFE` | 4 | mutating, non-destructive |
| `_LOCAL_WRITE` | 3 | writes to local disk |
| 🔴 `_WRITE_DESTRUCTIVE` | 3 | `destructiveHint: true`, idempotent |
| 🔴 `_WRITE_NON_IDEMPOTENT` | 2 | `send_message`, `custom_request` |

🟢 **12 of 31 (39%) are writes, declared by the row itself rather than counted by this KB** —
the first row on any of these three tiers to publish its own write surface machine-readably.
MIT, `LICENSE` present, bearer-token auth gated on `MCP_API_KEY`, and a docstring that warns
which tools mutate. Promoted on `agents/top.md` this pass.

## Two substitutions the action did not specify, both forced and both declared

🔴 **"Largest" is commit count, not stars.** `api.github.com` answers `403` through this
environment's proxy, so no star count is measurable on a readable channel this pass; taking one
from this KB's own pages would not be a measurement.

🔴 **"GitHub-only" was checked, not assumed.** `alejooroncoy/campus-cli` **is** npm-published —
`campus-cli` 2.2.3 declares `alejooroncoy/campus-cli` as its repository — and is excluded.
🔵 **And `bb-mcp` on npm is a different project**: *"MCP server for Bitbucket Server"*,
maintainer `g7v`, no repository field. A name match on a registry is not a publication of the
row that shares the name, and excluding `nitsuah/bb-mcp` on that basis would have dropped the
only `DYNAMIC` row from the sample of six.

## Reproduce

```sh
./sweep.sh "owner/repo=/path/to/clone" ...   # p141's surface_gate.py, unchanged
```

Committed: [`result.2026-10-12-p142.tsv`](result.2026-10-12-p142.tsv),
[`detail.2026-10-12-p142.txt`](detail.2026-10-12-p142.txt).
