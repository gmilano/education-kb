#!/usr/bin/env bash
# p139-oauthstore-adapter, step 2 — start the REAL server on the seeded store and ask the
# registered question over real HTTP: with a grant already present, does `POST /token`
# issue MCP tokens without any contact with Canvas?
#
#   ./probe_token.sh <pkg-dir> <harness-dir>
#
# A sentinel listener stands in for Canvas. `CANVAS_BASE_URL` points at it, so any Canvas
# contact is recorded as a connection rather than inferred from a timeout. If the token
# endpoint answers 200 with zero sentinel hits, the pre-seeded grant really did avoid the
# redirect; if it answers an error, or the sentinel is hit, `ACTION CL` is refuted.
set -u

PKG=${1:?pkg dir}
RUN=${2:?harness dir}

PORT=8097
SENTINEL_PORT=8099
SEED_PORT=8098
STORE="$RUN/p139-store.json"
KEY="p139-store-key-not-a-secret"
SENTINEL_LOG="$RUN/canvas-sentinel.log"

rm -f "$STORE" "$SENTINEL_LOG"

# --- the Canvas stand-in: records any connection, answers nothing useful --------------
node -e '
const http = require("http");
const fs = require("fs");
const log = process.argv[1];
http.createServer((req, res) => {
  fs.appendFileSync(log, `${new Date().toISOString()} ${req.method} ${req.url}\n`);
  res.writeHead(500, { "content-type": "application/json" });
  res.end(JSON.stringify({ error: "sentinel" }));
}).listen(Number(process.argv[2]), "127.0.0.1");
' "$SENTINEL_LOG" "$SENTINEL_PORT" &
SENTINEL_PID=$!
sleep 1

export CANVAS_AUTH_PROFILE=oauth_brokered
export CANVAS_BASE_URL="http://127.0.0.1:$SENTINEL_PORT"
export CANVAS_OAUTH_CLIENT_ID=canvas-dev-key
export CANVAS_OAUTH_CLIENT_SECRET=canvas-dev-secret

# --- step 1: seed, with NO store path in env so main() cannot touch the file ----------
export CANVAS_MCP_ISSUER="http://127.0.0.1:$PORT"
SEED_JSON=$(node "$RUN/seed_store.mjs" "$PKG" "$STORE" "$KEY" serve --port "$SEED_PORT" 2>"$RUN/seed.err" | grep -o '{"step":"seed".*')
echo "SEED: ${SEED_JSON:-FAILED}"
if [ -z "${SEED_JSON:-}" ]; then echo "--- seed stderr:"; head -5 "$RUN/seed.err"; kill $SENTINEL_PID 2>/dev/null; exit 1; fi

REFRESH=$(printf '%s' "$SEED_JSON" | python3 -I -c 'import json,sys; print(json.load(sys.stdin)["refresh_token"])')
RESOURCE=$(printf '%s' "$SEED_JSON" | python3 -I -c 'import json,sys; print(json.load(sys.stdin)["resource"])')

# --- step 2: start the real server ON the seeded store --------------------------------
export CANVAS_MCP_OAUTH_STORE="$STORE"
export CANVAS_MCP_OAUTH_STORE_KEY="$KEY"
node "$PKG/dist/http.js" serve --port "$PORT" > "$RUN/server.log" 2>&1 &
SERVER_PID=$!

for _ in $(seq 1 30); do
  curl -sS -o /dev/null --max-time 2 "http://127.0.0.1:$PORT/health" 2>/dev/null && break
  sleep 0.5
done
echo "SERVER LOG:"; sed 's/^/  /' "$RUN/server.log" | head -8

# --- the registered question, over real HTTP ------------------------------------------
echo "METADATA:"
curl -sS --max-time 10 "http://127.0.0.1:$PORT/.well-known/oauth-authorization-server" \
  | head -c 600; echo

# The path comes from the server's own metadata document, not from a guess: the first
# run of this probe posted to /token and got 404, because the issuer mounts OAuth under
# /oauth. `authorization_endpoint` and `token_endpoint` are both advertised there.
echo "TOKEN RESPONSE (POST /oauth/token):"
curl -sS --max-time 15 -w '\nHTTP_STATUS=%{http_code}\n' \
  -X POST "http://127.0.0.1:$PORT/oauth/token" \
  -H 'content-type: application/x-www-form-urlencoded' \
  --data-urlencode "grant_type=refresh_token" \
  --data-urlencode "refresh_token=$REFRESH" \
  --data-urlencode "client_id=p139-fixture-client" \
  --data-urlencode "client_secret=p139-fixture-secret" \
  --data-urlencode "resource=$RESOURCE"

echo "CANVAS SENTINEL HITS: $( [ -f "$SENTINEL_LOG" ] && wc -l < "$SENTINEL_LOG" || echo 0 )"
[ -s "$SENTINEL_LOG" ] && { echo "--- sentinel log:"; sed 's/^/  /' "$SENTINEL_LOG"; }

kill $SERVER_PID $SENTINEL_PID 2>/dev/null
wait 2>/dev/null
exit 0
