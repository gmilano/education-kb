#!/usr/bin/env bash
# P460-A — resolve the default ref, then walk grant paths CASE-INSENSITIVELY.
# Separates: GRANTED | POINTER_OR_STUB | REPO_LIVE_NO_GRANT | ADDRESS_DEAD.
set -uo pipefail
repo="$1"   # e.g. openedx/XBlock

ref=$(git ls-remote --symref "https://github.com/$repo" HEAD 2>/dev/null \
      | awk '/^ref:/{sub("refs/heads/","",$2); print $2; exit}')
if [ -z "$ref" ]; then echo "$repo ADDRESS_DEAD (no ref)"; exit 0; fi

stems="LICENSE LICENCE COPYING NOTICE LICENSE-MIT MIT-LICENSE LICENSE-APACHE"
# NOTE: the empty extension is a literal "" entry, NOT produced by `eval echo` —
# an unquoted empty word is dropped by word-splitting and the bare stem is then
# never probed. That defect is what made this ladder miss plain `LICENSE`.
exts=("" ".md" ".txt" ".TXT" ".rst" ".MD" ".html")

for s in $stems; do
  for e in "${exts[@]}"; do
    lower=$(printf '%s' "$s" | tr 'A-Z' 'a-z')
    upper=$(printf '%s%s' "$s" "$e" | tr 'a-z' 'A-Z')
    for cand in "$s$e" "$lower$e" "$upper"; do
      url="https://raw.githubusercontent.com/$repo/$ref/$cand"
      code=$(curl -s -o /tmp/p460.payload -w '%{http_code}' --max-time 12 "$url")
      # GATE ON STATUS, never on body: a 404 here is a 14-byte "404: Not Found"
      # that a byte-reader will otherwise shelve as a licence (Gap 453-E(d)).
      if [ "$code" = "200" ]; then
        sz=$(stat -c%s /tmp/p460.payload)
        if [ "$sz" -lt 200 ]; then
          echo "$repo POINTER_OR_STUB $cand ${sz}B"; continue
        fi
        echo "$repo GRANTED $cand ${sz}B $(sha256sum /tmp/p460.payload | cut -c1-12)"
        echo "  title: $(head -2 /tmp/p460.payload | tr -d '\n' | tr -s ' ' | cut -c1-58)"
        exit 0
      fi
    done
  done
done
# Live-but-ungranted is NOT dead: probe a known-present file before concluding.
live=$(curl -s -o /dev/null -w '%{http_code}' --max-time 12 \
       "https://raw.githubusercontent.com/$repo/$ref/README.md")
[ "$live" = "200" ] && echo "$repo REPO_LIVE_NO_GRANT (ref=$ref)" \
                    || echo "$repo UNRESOLVED (ref=$ref)"
