#!/usr/bin/env bash
# Measure each address's licence from the LIVE tree via raw.githubusercontent.com.
#
# api.github.com and github.com HTML are both 403 through this session's proxy
# (measured p122), so raw.githubusercontent.com is the only readable channel.
# Probes (branch x path) in order and stops at the first file that returns 200.
#
# usage: scan_licences.sh ADDRESS_LIST_FILE > out.tsv
# output: address <TAB> branch <TAB> path <TAB> bytes <TAB> token
set -uo pipefail
HERE="$(cd "$(dirname "$0")" && pwd)"
BRANCHES="${BRANCHES:-main master}"
PATHS="${PATHS:-LICENSE LICENSE.md LICENSE.txt LICENCE LICENCE.md COPYING COPYING.txt LICENSE.rst LICENSE-MIT license.txt}"

probe_one() {
  local addr="$1" b p url code body token bytes
  for b in $BRANCHES; do
    for p in $PATHS; do
      url="https://raw.githubusercontent.com/${addr}/${b}/${p}"
      body="$(curl -sL --max-time 25 -w '\nHTTPCODE:%{http_code}' "$url" 2>/dev/null)"
      code="${body##*HTTPCODE:}"
      body="${body%$'\n'HTTPCODE:*}"
      if [ "$code" = "200" ]; then
        bytes=$(printf '%s' "$body" | wc -c | tr -d ' ')
        token=$(printf '%s' "$body" | python3 -I "${HERE}/classify_licence.py")
        printf '%s\t%s\t%s\t%s\t%s\n' "$addr" "$b" "$p" "$bytes" "$token"
        return 0
      fi
    done
  done
  printf '%s\t-\t-\t0\tNO-FILE\n' "$addr"
}

export -f probe_one
export BRANCHES PATHS HERE
grep -vE '^\s*(#|$)' "$1" | xargs -P 16 -I{} bash -c 'probe_one "$@"' _ {}
