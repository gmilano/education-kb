---
industry: education
region: Global
updated: 2026-10-12
---

# `p139-oauthstore-adapter` — `ACTION CL`: the pre-seeded grant works, and the documented way to reach it does not

**Executes p138's pre-registered `ACTION CL`**, written as:

> Execute the `P13` step-2 adapter against `canvas-lms-mcp`'s `OAuthStore` for real, with a
> fixture grant. 🔴 *Refuted if the brokered flow still demands the Canvas redirect when a
> grant is pre-seeded — which would put the adapter back above two weeks.*

p138 put this action on itself, in its own omissions list: *"`ACTION CE` was answered by
reading an interface, not by calling it."* This pass called it.

## Verdict: **DISCHARGED, NOT REFUTED — and a blocker found one layer above the one tested**

| measurement | value |
|---|---|
| `POST /oauth/token`, `grant_type=refresh_token`, against a pre-seeded grant | 🟢 **HTTP 200** |
| MCP access token issued | 🟢 **`mcpat_…`, `Bearer`, `expires_in: 3600`** |
| scopes carried through from the seeded grant | 🟢 **`canvas:read canvas:write`** |
| refresh token rotated (single-use, OAuth 2.1 §6.1) | 🟢 **yes — `mcprt_…`, not the seeded value** |
| 🟢 **Canvas contacts during the whole flow** | 🟢 **0 — measured by a sentinel, not inferred** |
| grant store on disk | 🟢 **encrypted: `scrypt` KDF, AES-GCM `iv`+`tag`, no plaintext** |
| 🔴 the documented embedder entry point | 🔴 **unusable — see `P139-C1`** |

🔵 **The brokered flow does not demand the Canvas redirect when a grant is pre-seeded.** An
institution that already holds Canvas refresh tokens — from an LTI launch, an earlier consent,
or a service account — can mint MCP tokens for its own clients without sending a single user
through Canvas's authorize screen, and without the server touching Canvas at all. That is
`P13` step 2, and it runs today.

## `P139-C1` — 🔴 importing the documented entry point kills the host process

p138 cited `oauthStore?: OAuthStore` as the embedder extension point, and `HttpHandlerConfig`
documents it as exactly that: *"Embedders may supply their own implementation."* The package's
own `exports` map points `canvas-lms-mcp/http` at `dist/http.js`. 🔴 **That file calls `main()`
at module top level, unguarded:**

```js
// dist/http.js, last statements of the module — ESM build
main().catch((error) => {
  console.error("Fatal error:", error);
  process.exit(1);
});
export { FileOAuthStore, MemoryOAuthStore, createHttpHandler, loadOAuthProfileConfig, openOAuthStore };
```

`main()` calls `parseArgs(process.argv.slice(2))`. So `import { createHttpHandler } from
'canvas-lms-mcp/http'` makes the **importer's** command line the server's configuration. The
observed stack, from this pass's first run:

```
at fatal      (dist/chunk-7XQVFCG3.js:23:11)
at parseArgs  (dist/chunk-7XQVFCG3.js:163:5)
at main       (dist/http.js:2182:18)
at            (dist/http.js:2226:1)     ← module top level
```

…and the process exited **1** with `Canvas API token required. Use --token or set
CANVAS_API_TOKEN.` 🔴 **There is no `import.meta.main` or `require.main === module` guard**, and
`dist/http.cjs` does the same thing at its line 2226. 🔵 **By the time an embedder's code could
pass `oauthStore`, `main()` has already read `argv`, built its own handler, and either bound a
port or exited.** The extension point is real in the type system and unreachable through the
documented import.

🟡 **Three further seam facts, each of which cost a run:**

| expectation | reality |
|---|---|
| per-module JS at `dist/auth/oauth/store.js` (a `.d.ts` sits there) | 🔴 does not exist — the build is bundled; the `.d.ts` tree describes the **source**, not the payload |
| `AuthorizationServer`, `ClientResolver`, `CanvasOAuthClient` importable (all have exported `.d.ts`) | 🔴 not exported — `dist/http.js` exports exactly **5** symbols |
| token endpoint at `/token` | 🔴 `404` — it is **`/oauth/token`**, as the issuer's own metadata says |

🔵 **The last one is the cheapest lesson: read the metadata document, do not guess the path.**
`/.well-known/oauth-authorization-server` advertises `authorization_endpoint`,
`token_endpoint`, `registration_endpoint` and `revocation_endpoint`, and this probe takes the
path from there.

## How the action was discharged anyway — the operator route

Since the store cannot be injected by import, it is injected **by configuration**, which is how
an operator would do it. Two steps, both in this directory:

1. **`seed_store.mjs`** opens an encrypted `FileOAuthStore` at a path of its own and writes the
   three records `P13` step 2 needs: a preregistered client, a `Grant` holding a
   `CanvasConnection` (expiry a year out, so no Canvas refresh is due), and a `refresh`
   `TokenRecord` whose `hash` is `sha256(raw token)`. Then `flush()`.
   🔵 **`CANVAS_MCP_OAUTH_STORE` is deliberately absent from this step's environment**, so the
   `main()` that runs on import opens an in-memory store and cannot rewrite the seed underneath
   the script.
2. **`probe_token.sh`** starts the real server — `node dist/http.js serve --port 8097` — with
   `CANVAS_MCP_OAUTH_STORE` now pointing at the seeded file, confirms `Grant store: encrypted
   file` in its log, reads the metadata document, and posts the refresh grant over real HTTP.

**The Canvas sentinel is the point of the harness.** `CANVAS_BASE_URL` points at a local
listener that logs every request it receives and answers `500`. So "no Canvas call" is a
**measurement of zero connections**, not an inference from the absence of a timeout. Had the
flow reached for Canvas, the log would name the path it asked for.

```
SEED: {"step":"seed","grant_id":"4f0fa2d4-…","refresh_token":"p139-fixture-refresh-token", …}
SERVER LOG: Grant store: encrypted file
TOKEN RESPONSE (POST /oauth/token):
{"access_token":"mcpat_8O0m8fTnomzwmy8iB5IfnFHuN_x_Dl3aG_VhdPZ-B-c","token_type":"Bearer",
 "expires_in":3600,"scope":"canvas:read canvas:write","refresh_token":"mcprt_…"}
HTTP_STATUS=200
CANVAS SENTINEL HITS: 0
```

## What this changes for `P13`

🟢 **Step 2 is hours, not weeks — but it is a different shape of work than p138 implied.**

| p138's reading | what execution shows |
|---|---|
| supply an `OAuthStore` implementation to the handler, in process | 🔴 not available by import; `main()` owns the handler |
| the adapter is an in-process embed | 🟢 the adapter is a **store-seeding job plus a managed process**: write records into the encrypted file (or a custom store behind a fork), run `serve` |
| the risk was that Canvas's redirect would still be demanded | 🟢 it is not; the risk is **process topology**, which is cheaper |

🔵 **So the two-week estimate stands corrected downward on the protocol and upward on the
plumbing.** The grant model, scope carry-through, refresh rotation and encrypted persistence
are all present and working. What a client pays for is a seeding path into the store and a
supervised process — and, if an in-process embed is required, a fork that guards `main()`.

🟡 **The "no fork" half of `P138-D` is therefore narrowed, not refuted.** No fork is needed to
*use* the brokered profile. A fork — or a one-line patch adding a `main` guard — is needed to
*embed* it.

## Files

| file | role |
|---|---|
| `adapter.mjs` | the in-process attempt, kept because its failure is `P139-C1`. Drives `createHttpHandler` with an injected store and a refusing `fetch` |
| `seed_store.mjs` | step 1: write a client, grant and refresh token into an encrypted `FileOAuthStore` |
| `probe_token.sh` | step 2: Canvas sentinel, real server on the seeded store, metadata read, `POST /oauth/token` |
| `result.2026-10-12-p139.txt` | the run transcript published above, captured from a clean re-run |

### Reproduce

```sh
npm install @modelcontextprotocol/sdk@1.32.0 zod@4.4.3 @iarna/toml@2.2.5 prompts@2.4.2
# unpack canvas-lms-mcp@2.2.0 so its deps resolve (node_modules must be a parent dir)
bash probe_token.sh /path/to/package /path/to/harness
```

## 🔴 What this probe does NOT establish

- 🔴 **No MCP tool was called with the issued token.** The token is verified to exist in the
  store, bound to the seeded grant, with the seeded scopes — but `tools/call` against
  `/mcp` was not exercised, so "the agent can now read Canvas as that user" is still
  **unproven**. The Canvas side of that call would need a real Canvas, which this channel
  does not have.
- 🔴 **The Canvas credential in the grant is a fixture string.** Nothing checked that a *real*
  Canvas token in that field is accepted by Canvas — only that the MCP layer never asks.
- 🔴 **One version, one profile.** `canvas-lms-mcp@2.2.0`, `oauth_brokered`, loopback issuer
  over `http`. An `https` issuer exercises `isLoopbackIssuer` differently and was not tested.
- 🔴 **The `authorization_code` path was not run.** Only `refresh_token`. A client that has no
  refresh token still needs the redirect, and that is the normal first-contact case.
- 🔴 **`FileOAuthStore`'s key handling was not audited.** The file is `scrypt` + AES-GCM with
  no plaintext, which is what the format claims; the KDF parameters were not read.
- 🟡 **`P139-C1` is a defect in a 2026-10-10 release and may be fixed upstream at any time.**
  It is recorded against **`canvas-lms-mcp@2.2.0`** specifically. The repository is
  [`bruchris/canvas-lms-mcp`](https://github.com/bruchris/canvas-lms-mcp) (MIT), which p137
  measured at **9★** and p138 read at **978 lines** of OAuth code.
