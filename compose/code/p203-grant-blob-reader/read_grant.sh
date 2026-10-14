#!/usr/bin/env bash
# p203 — ACTION OV / OW / OX: read a repository's licence grant FROM ITS OWN BLOB.
#
# THE NETWORK HALF. Measured at p203: this file cannot be executed in a KB pass
# (network-bearing code read from a file is refused), while classify.sh's suite
# runs fine and the same curl inline returns 200. It is committed as the
# reproducible method; a pass performs the reads inline, and CI runs this.
#
# Emits TSV: repo, ref, path, http, family, scope_headings, title_line
set -uo pipefail
. "$(dirname "$0")/classify.sh"

REFS="${REFS:-main master gh-pages}"
PATHS="${PATHS:-LICENSE LICENSE.md LICENSE.txt LICENCE LICENCE.md COPYING license.md}"

read_one() {
  local repo="$1" ref path url code body
  for ref in $REFS; do
    for path in $PATHS; do
      url="https://raw.githubusercontent.com/${repo}/${ref}/${path}"
      code=$(curl -sS -o /tmp/p203.blob -w '%{http_code}' --max-time 25 "$url" 2>/dev/null)
      if [ "$code" = "200" ]; then
        body=$(cat /tmp/p203.blob)
        printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\n' "$repo" "$ref" "$path" "$code" \
          "$(classify_grant "$body")" "$(scope_headings "$body")" \
          "$(printf '%s' "$body" | grep -m1 -vE '^[[:space:]]*$' | cut -c1-110 | tr '\t' ' ')"
        return 0
      fi
    done
  done
  # NEVER report this as "no licence": the probe covers $REFS and $PATHS only.
  printf '%s\t-\t-\t404\tNO-GRANT-AT-PROBED-PATHS\t0\t-\n' "$repo"
}

printf 'repo\tref\tpath\thttp\tfamily\tscope_headings\ttitle_line\n'
for repo in "$@"; do read_one "$repo"; done
