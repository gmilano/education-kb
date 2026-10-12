---
industry: education
region: Global
updated: 2026-10-12
---

# `p143-lockfile-audit` — `ACTION DO`: the shelf's one self-verifying row verifies

🟢 **Falsifier silent. 10 of 10 hashes recompute, and 10 of 10 agree with the source** on
every signature field that can be derived without executing the repository.

## What was registered

> 🟢 **`ACTION DO`** — audit `malkreide/global-education-mcp`'s `tools.lock.json` against
> its source: recompute all ten signature hashes from `server.py` and diff.
> 🔴 **Refuted if any hash disagrees with the committed lockfile** — which would make the
> one row this KB holds up as the practice to copy an unverified one, and 🔵 **matters
> more than its ten tools do**.

## Two questions, deliberately separated

🔴 **"The hashes verify" is two different claims and only one of them is answerable from
the lockfile.** Conflating them is how a lockfile audit becomes circular.

### (a) Internal consistency — `lockaudit.py`

Does each entry's stored `hash` actually digest the `signature` block stored beside it?
Answered from the lockfile alone, with the algorithm the repository documents:

```
signature = {"name", "description", "inputSchema", "annotations"}
canonical = json.dumps(signature, sort_keys=True, ensure_ascii=False)
hash      = sha256(canonical.encode("utf-8")).hexdigest()
```

🔵 **Reimplemented, not invoked.** The repository ships its own generator
(`scripts/tool_signatures.py`); running it would ask the lockfile's author whether the
lockfile is right. An independent reimplementation is the only version of this audit worth
doing.

| | |
|---|---|
| tools in lockfile | **10** |
| 🟢 hash AGREE | **10** |
| 🔴 hash DISAGREE | **0** |
| entries whose signature key-set is not the documented four | 🟢 **0** |
| entries without `readOnlyHint: true` | 🟢 **0** |

### (b) Source agreement — `srcagree.py`

🔴 **Internal consistency is NOT the claim `P21` rests on.** A lockfile can be perfectly
self-consistent and describe a server that no longer exists. So the three signature fields
that are *literal in source* are re-derived from `server.py` with `ast` and diffed:

| field | derivable from source? | result |
|---|---|---|
| `name` | 🟢 yes — the decorated function's name | 🟢 **10 of 10 agree** |
| `annotations` | 🟢 yes — the literal dict in `@mcp.tool(annotations={…})` | 🟢 **10 of 10 agree** |
| `description` | 🟢 yes — the docstring, `inspect.cleandoc`-normalised exactly as the generator documents | 🟢 **10 of 10 agree** |
| `inputSchema` | 🔴 **NO** — pydantic generates it from the `params` model at import | 🔴 **NOT VERIFIED** |

🔴 **One of the four hashed fields cannot be checked without executing the repository, and
this probe does not execute it.** So the honest statement is: *three of four signature
fields are confirmed against source for all ten tools, and the fourth is unverified here.*
🔵 **A reader is entitled to know which field is which**, and "the lockfile verifies" would
have concealed it.

🔵 **Parsed with `ast`, not regex** — every decorator in this repository spans **10 lines**,
and a regex over a nested multi-line decorator is precisely the defect `ACTION DM` was
registered against. The same blindness would have produced "0 tools found" here.

## The finding that fed `ACTION DM`

🟢 **10 of 10 decorators are multi-line.** That is the measurement confirming the
`ACTION DM` premise from the other direction: this is the best-instrumented row on the
shelf, and `p141-agent-surface-gate` returned `NO_REGISTRATION_SITE_FOUND` on it.

## What a studio takes from this

🟢 **`P21` stands, and now stands on a checked claim rather than a declared one.**
`tools.lock.json` is the cheapest tool-surface control on these shelves: one CI step
(`scripts/tool_signatures.py ci`) replaces `p139-tool-count-drift`,
`description-drift-audit` and `p141-agent-surface-gate` for the repository that has it.

🔴 **With one limit to carry into the runbook:** the lockfile pins the schema, but a
*consumer* cannot verify the schema half without running the server. 🔵 **Pin the lockfile
in CI where you can execute; where you cannot, you have verified three fields of four.**

## Run it

```
python3 -I lockaudit.py <tools.lock.json>              # result.2026-10-12-p143.txt
python3 -I srcagree.py <server.py> <tools.lock.json>   # srcagree.2026-10-12-p143.txt
```

Subject: `malkreide/global-education-mcp`, HEAD `26f7cd2`, **2026-10-04**, MIT
(`LICENSE` present, declared in `pyproject.toml`).
