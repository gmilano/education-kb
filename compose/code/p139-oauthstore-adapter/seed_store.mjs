/**
 * p139-oauthstore-adapter, step 1 — write the grant an institution already holds into an
 * encrypted `FileOAuthStore`, so that a server started later opens it and finds the grant.
 *
 *   node seed_store.mjs <pkg> <store-path> <store-key> serve --port <unused-port>
 *
 * `--port` is not this script's argument. It is consumed by the package: importing
 * `dist/http.js` runs `main()` at module top level (see README, `P139-C1`), which parses
 * `process.argv` and binds a port. The flag is here so that side effect lands somewhere
 * harmless, and the process is killed explicitly once the seed has reached disk.
 *
 * Deliberately NO `CANVAS_MCP_OAUTH_STORE` in this step's environment: that would make
 * `main()` open the same file and its purge loop could rewrite the seed underneath us.
 * `main()` gets an in-memory store; the seed is written through a store this script owns.
 */

import { createHash, randomUUID } from 'node:crypto'
import { pathToFileURL } from 'node:url'
import path from 'node:path'

const [pkgRoot, storePath, storeKey] = process.argv.slice(2)
if (!pkgRoot || !storePath || !storeKey) {
  console.error('usage: node seed_store.mjs <pkg> <store-path> <store-key> serve --port <n>')
  process.exit(2)
}

const { FileOAuthStore } = await import(
  pathToFileURL(path.join(pkgRoot, 'dist/http.js')).href
)

const sha256 = (s) => createHash('sha256').update(s).digest('hex')

const ISSUER = process.env.CANVAS_MCP_ISSUER
const RESOURCE = `${ISSUER}/mcp`
const CLIENT_ID = 'p139-fixture-client'
const CLIENT_SECRET = 'p139-fixture-secret'
const RAW_REFRESH = 'p139-fixture-refresh-token'
const GRANT_ID = randomUUID()
const now = Date.now()
const YEAR = 365 * 24 * 3600 * 1000

const store = await FileOAuthStore.open(storePath, storeKey)

await store.putClient({
  clientId: CLIENT_ID,
  clientName: 'p139 fixture',
  redirectUris: ['http://127.0.0.1:9999/callback'],
  tokenEndpointAuthMethod: 'client_secret_post',
  clientSecretHash: sha256(CLIENT_SECRET),
  grantTypes: ['authorization_code', 'refresh_token'],
  source: 'preregistered',
  createdAt: now,
})

// Step 2 of P13: the Canvas credential an LTI launch or prior consent already produced.
// `expiresAt` a year out, so no Canvas refresh is due — if the flow calls Canvas anyway,
// the sentinel in step 2 records it and the action is refuted.
await store.putGrant({
  id: GRANT_ID,
  clientId: CLIENT_ID,
  scopes: ['canvas:read', 'canvas:write'],
  resource: RESOURCE,
  canvasUserId: '4242',
  canvas: {
    accessToken: 'canvas-access-from-lti-launch',
    refreshToken: 'canvas-refresh-from-lti-launch',
    expiresAt: now + YEAR,
  },
  createdAt: now,
})

await store.putToken({
  hash: sha256(RAW_REFRESH),
  kind: 'refresh',
  grantId: GRANT_ID,
  clientId: CLIENT_ID,
  scopes: ['canvas:read', 'canvas:write'],
  resource: RESOURCE,
  createdAt: now,
  expiresAt: now + YEAR,
})

await store.flush()

console.log(JSON.stringify({
  step: 'seed',
  store_path: storePath,
  grant_id: GRANT_ID,
  client_id: CLIENT_ID,
  refresh_token: RAW_REFRESH,
  resource: RESOURCE,
}))

// `main()` is listening on the throwaway port; nothing else to do here.
process.exit(0)
