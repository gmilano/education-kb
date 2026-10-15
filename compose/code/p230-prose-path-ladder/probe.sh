#!/usr/bin/env bash
# p230 — ACTION TA. Probe the grant paths THESE SHELVES RECORD against the slugs
# p229 left unresolved. The probe list is harvest.py's output, not a vocabulary.
#
#   usage: probe.sh <slugs-file> <paths-file> <out.tsv>
#
# Columns: slug  state  path  http  bytes  sha256_12  ref  head_sha
set -uo pipefail
SLUGS="$1"; PATHS="$2"; OUT="$3"
: > "$OUT"

probe_one() {
  local slug="$1"
  local ref head line
  line=$(git ls-remote --symref "https://github.com/${slug}" HEAD 2>/dev/null)
  if [[ -z "$line" ]]; then
    printf '%s\tABSENT\t-\t-\t-\t-\t-\t-\n' "$slug"; return
  fi
  ref=$(sed -n 's#^ref: refs/heads/\([^\t]*\)\tHEAD$#\1#p' <<<"$line" | head -1)
  head=$(awk '/\tHEAD$/{print $1; exit}' <<<"$line")
  [[ -z "$ref" ]] && ref=HEAD
  local found=0
  while IFS=$'\t' read -r path _rest; do
    [[ -z "$path" ]] && continue
    local url="https://raw.githubusercontent.com/${slug}/${ref}/${path}"
    local tmp; tmp=$(mktemp)
    local code; code=$(curl -sS -L --max-time 25 -o "$tmp" -w '%{http_code}' "$url" 2>/dev/null)
    if [[ "$code" == "200" ]]; then
      local bytes sha
      bytes=$(wc -c < "$tmp" | tr -d ' ')
      sha=$(sha256sum "$tmp" | cut -c1-12)
      if [[ "$bytes" -gt 40 ]]; then
        printf '%s\tHIT\t%s\t200\t%s\t%s\t%s\t%s\n' "$slug" "$path" "$bytes" "$sha" "$ref" "$head"
        found=1
      fi
    fi
    rm -f "$tmp"
  done < "$PATHS"
  [[ "$found" -eq 0 ]] && printf '%s\tNO-HIT\t-\t-\t-\t-\t%s\t%s\n' "$slug" "$ref" "$head"
}
export -f probe_one
export PATHS

grep -v '^#' "$SLUGS" | grep -v '^$' | xargs -P 6 -I{} bash -c 'probe_one "$@"' _ {} >> "$OUT"
sort -o "$OUT" "$OUT"
wc -l < "$OUT"
