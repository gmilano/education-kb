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
  local addr="$1" b p url code body token bytes __p
  for b in $BRANCHES; do
    for p in $PATHS; do
      url="https://raw.githubusercontent.com/${addr}/${b}/${p}"
      # `ACTION XY` (p253): `bytes` was taken from the capture, which is `P834` — and here
      # the capture was doubly lossy, since the appended `HTTPCODE:` sentinel was stripped
      # back off with `${body%...}` after the substitution had already eaten the trailing
      # newline run.  The status now comes from `-w` into its own file and the size from
      # the payload file; the capture stays for the classifier, which is newline-insensitive.
      __p=$(mktemp)
      code=$(curl -sL --max-time 25 -o "$__p" -w '%{http_code}' "$url" 2>/dev/null)
      body="$(cat "$__p")"
      if [ "$code" = "200" ]; then
        bytes=$(wc -c < "$__p" | tr -d ' ')
        token=$(printf '%s' "$body" | python3 -I "${HERE}/classify_licence.py")
        rm -f "$__p"
        printf '%s\t%s\t%s\t%s\t%s\n' "$addr" "$b" "$p" "$bytes" "$token"
        return 0
      fi
      rm -f "$__p"
    done
  done
  printf '%s\t-\t-\t0\tNO-FILE\n' "$addr"
}

export -f probe_one
export BRANCHES PATHS HERE
grep -vE '^\s*(#|$)' "$1" | xargs -P 16 -I{} bash -c 'probe_one "$@"' _ {}
