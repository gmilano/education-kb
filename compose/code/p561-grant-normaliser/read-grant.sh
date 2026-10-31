#!/usr/bin/env bash
# p561 — inline grant reader. Resolve default branch, then status-gate 6 candidate paths.
# Published convention: raw (what wc -c returns), per 560-A.
NAMES="LICENSE LICENSE.txt LICENSE.md COPYING COPYING.txt license.txt LICENSE.TXT LICENCE"
read_one () {
  local slug="$1" want="$2"
  local br
  br=$(timeout 60 git ls-remote --symref "https://github.com/$slug" HEAD 2>/dev/null | awk '/^ref:/{sub("refs/heads/","",$2); print $2; exit}')
  local head
  head=$(timeout 60 git ls-remote "https://github.com/$slug" HEAD 2>/dev/null | awk 'NR==1{print substr($1,1,12)}')
  if [ -z "$br" ]; then printf '%-44s %-10s %s\n' "$slug" "NO-BRANCH" "-"; return; fi
  local tried=0
  for n in ${want:-$NAMES}; do
    tried=$((tried+1))
    local tmp code
    tmp=$(mktemp)
    code=$(curl -sS -o "$tmp" -w '%{http_code}' "https://raw.githubusercontent.com/$slug/$br/$n" 2>/dev/null)
    if [ "$code" = "200" ]; then
      printf '%-44s %-10s %-14s %-9s %-14s %s\n' "$slug" "$br" "$n" "$(wc -c < "$tmp" | tr -d ' ')" "$(sha256sum "$tmp" | cut -c1-12)" "HEAD=$head"
      rm -f "$tmp"; return
    fi
    rm -f "$tmp"
  done
  printf '%-44s %-10s %-14s %-9s %-14s %s\n' "$slug" "$br" "NO-GRANT/$tried" "-" "-" "HEAD=$head"
}
printf '%-44s %-10s %-14s %-9s %-14s %s\n' SLUG BRANCH PATH RAW_B SHA256_12 HEAD
for s in "$@"; do read_one "$s"; done
