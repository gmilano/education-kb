/**
 * p139-oauthstore-adapter — `ACTION CL`: the P13 step-2 adapter, executed.
 *
 *   node adapter.mjs <path-to-canvas-lms-mcp-package>
 *
 * p138 answered `ACTION CE` by READING `canvas-lms-mcp`'s `OAuthStore` interface and
 * concluding it was a sufficient seam for the `P13` brokered-identity pattern. p138 said
 * so itself in its own omissions list: *"`ACTION CE` was answered by reading an
 * interface, not by calling it."* `ACTION CL` calls it.
 *
 * The registered question:
 *
 *   > Execute the `P13` step-2 adapter against `canvas-lms-mcp`'s `OAuthStore` for real,
 *   > with a fixture grant. Refuted if the brokered flow still demands the Canvas
 *   > redirect when a grant is pre-seeded.
 *
 * So the test is not "does the store accept a grant" — a Map accepts anything. It is:
 * **with a grant already in the store, can a client obtain MCP access tokens without any
 * call to Canvas at all?** That is what an institution holding Canvas refresh tokens from
 * an LTI launch, a prior consent or a service account actually needs, and it decides
 * whether the adapter is days of work or weeks.
 *
 * ## Why this drives `createHttpHandler` and not `AuthorizationServer`
 *
 * The first version of this adapter imported `AuthorizationServer`, `ClientResolver` and
 * `CanvasOAuthClient` from `dist/auth/oauth/*.js`, because the package ships a `.d.ts`
 * for each of them declaring them exported. 🔴 **Those modules do not exist in the
 * payload.** The build is bundled: the classes live inside `dist/http.js`, which exports
 * exactly five symbols — `MemoryOAuthStore`, `FileOAuthStore`, `createHttpHandler`,
 * `loadOAuthProfileConfig`, `openOAuthStore`. The per-module typings describe the
 * SOURCE tree, not the shipped surface.
 *
 * That is a finding about the seam rather than a problem with the test, and driving the
 * public handler is the truer measurement anyway: `oauthStore` and `fetch` are both
 * documented embedder inputs on `HttpHandlerConfig`, so this adapter is written the way
 * an integrator would have to write it.
 *
 * The Canvas-facing `fetch` RECORDS AND THROWS. If the flow touches Canvas, the run fails
 * loudly rather than quietly succeeding over the network.
 */

import { createHash, randomUUID } from 'node:crypto'
import { Readable } from 'node:stream'
import { pathToFileURL } from 'node:url'
import path from 'node:path'

const pkgRoot = process.argv[2]
if (!pkgRoot) {
  console.error('usage: node adapter.mjs <path-to-canvas-lms-mcp-package>')
  process.exit(2)
}

const httpMod = pathToFileURL(path.join(pkgRoot, 'dist/http.js')).href
const { MemoryOAuthStore, createHttpHandler } = await import(httpMod)

const sha256 = (s) => createHash('sha256').update(s).digest('hex')

// --- the recording fetch: any Canvas contact is a refutation ----------------------
const canvasCalls = []
const refusingFetch = async (input, init) => {
  canvasCalls.push({ url: String(input?.url ?? input), method: init?.method ?? 'GET' })
  throw new Error('CANVAS CONTACTED — the pre-seeded grant did not avoid the redirect')
}

// --- config: loopback issuer, so the issuer check does not demand https -------------
const ISSUER = 'http://127.0.0.1:8080'
const RESOURCE = `${ISSUER}/mcp`
const CLIENT_ID = 'p139-fixture-client'
const CLIENT_SECRET = 'p139-fixture-secret'

const oauth = {
  issuer: ISSUER,
  issuerPath: '',
  resource: RESOURCE,
  canvas: {
    baseUrl: 'https://canvas.example.edu',
    clientId: 'canvas-dev-key',
    clientSecret: 'canvas-dev-secret',
  },
  clients: [
    {
      client_id: CLIENT_ID,
      client_name: 'p139 fixture',
      redirect_uris: ['http://127.0.0.1:9999/callback'],
      client_secret: CLIENT_SECRET,
    },
  ],
  dynamicRegistration: false,
  cimdAllowedHosts: [],
}

// --- step 2 of P13: the store an institution brings, pre-seeded ----------------------
const store = new MemoryOAuthStore()
const now = Date.now()
const GRANT_ID = randomUUID()
const RAW_REFRESH = 'p139-fixture-refresh-token'
const YEAR = 365 * 24 * 3600 * 1000

await store.putClient({
  clientId: CLIENT_ID,
  clientName: 'p139 fixture',
  redirectUris: oauth.clients[0].redirect_uris,
  tokenEndpointAuthMethod: 'client_secret_post',
  clientSecretHash: sha256(CLIENT_SECRET),
  grantTypes: ['authorization_code', 'refresh_token'],
  source: 'preregistered',
  createdAt: now,
})

// The whole point: a Canvas connection the broker already holds. `expiresAt` is a year
// out, so no Canvas refresh is due — if the flow calls Canvas anyway, that is the finding.
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

// --- the embedder surface, exactly as HttpHandlerConfig documents it -----------------
const handler = createHttpHandler({
  authProfile: 'oauth_brokered',
  oauth,
  oauthStore: store,
  fetch: refusingFetch,
  baseUrl: oauth.canvas.baseUrl,
})

// --- minimal node http doubles -------------------------------------------------------
function mockRequest(method, url, body, headers = {}) {
  const req = Readable.from(body ? [body] : [])
  req.method = method
  req.url = url
  req.headers = {
    host: '127.0.0.1:8080',
    ...(body
      ? {
        'content-type': 'application/x-www-form-urlencoded',
        'content-length': String(Buffer.byteLength(body)),
      }
      : {}),
    ...headers,
  }
  return req
}

function mockResponse() {
  const chunks = []
  return {
    statusCode: 0,
    headers: {},
    headersSent: false,
    setHeader(k, v) { this.headers[k.toLowerCase()] = v },
    getHeader(k) { return this.headers[k.toLowerCase()] },
    removeHeader(k) { delete this.headers[k.toLowerCase()] },
    writeHead(status, maybeHeaders) {
      this.statusCode = status
      if (maybeHeaders && typeof maybeHeaders === 'object') Object.assign(this.headers, maybeHeaders)
      return this
    },
    write(chunk) { if (chunk) chunks.push(String(chunk)); return true },
    end(chunk) { if (chunk) chunks.push(String(chunk)); this.headersSent = true; return this },
    on() { return this },
    once() { return this },
    emit() { return false },
    get body() { return chunks.join('') },
  }
}

async function call(method, url, body, headers) {
  const res = mockResponse()
  await handler(mockRequest(method, url, body, headers), res)
  let json
  try { json = JSON.parse(res.body) } catch { json = null }
  return { status: res.statusCode, headers: res.headers, body: res.body, json }
}

// --- probe 1: the metadata the spec requires, with no grant involved ------------------
const meta = await call('GET', '/.well-known/oauth-authorization-server')

// --- probe 2: the registered question — refresh_token against the seeded grant --------
const form = new URLSearchParams({
  grant_type: 'refresh_token',
  refresh_token: RAW_REFRESH,
  client_id: CLIENT_ID,
  client_secret: CLIENT_SECRET,
  resource: RESOURCE,
})
const token = await call('POST', '/token', form.toString())

const issued = token.status === 200 && typeof token.json?.access_token === 'string'
const refuted = !issued || canvasCalls.length > 0

const result = {
  action: 'CL',
  package: 'canvas-lms-mcp@2.2.0',
  embedder_surface: 'createHttpHandler({ authProfile: "oauth_brokered", oauthStore, fetch })',
  metadata_probe: {
    status: meta.status,
    issuer: meta.json?.issuer ?? null,
    grant_types: meta.json?.grant_types_supported ?? null,
    code_challenge_methods: meta.json?.code_challenge_methods_supported ?? null,
  },
  token_probe: {
    status: token.status,
    access_token_issued: issued,
    token_type: token.json?.token_type ?? null,
    expires_in: token.json?.expires_in ?? null,
    scope: token.json?.scope ?? null,
    refresh_token_rotated:
      typeof token.json?.refresh_token === 'string' && token.json.refresh_token !== RAW_REFRESH,
    error: token.json?.error ?? null,
    error_description: token.json?.error_description ?? null,
  },
  canvas_calls: canvasCalls.length,
  canvas_call_detail: canvasCalls,
  verdict: refuted ? 'REFUTED' : 'NOT REFUTED',
}

// --- probe 3: is the issued access token a real record bound to the seeded grant? -----
if (issued) {
  const rec = await store.getToken(sha256(token.json.access_token))
  result.access_token_record = {
    found_in_store: Boolean(rec),
    kind: rec?.kind ?? null,
    grant_matches_seed: rec?.grantId === GRANT_ID,
    resource: rec?.resource ?? null,
    scopes: rec?.scopes ?? null,
  }
  // Rotation check: the old refresh token must be gone (single-use), per OAuth 2.1.
  result.old_refresh_consumed = !(await store.getToken(sha256(RAW_REFRESH)))
}

console.log(JSON.stringify(result, null, 2))
process.exit(refuted ? 1 : 0)
