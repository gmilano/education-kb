#!/usr/bin/env bash
# p525 promotion-gap sweep.  For every github address that agents/top.md NAMES but
# does NOT carry on its canonical Permissive/Copyleft shelf tables, resolve the
# default branch over the git protocol and grade the grant from served bytes with
# the title-anchored classifier.
#
# NARROWNESS DECLARED: this probes SEVEN grant filenames, not the 53 that
# ingest/probe-grant.sh probes.  So UNRESOLVED-on-7 here is NOT a nil -- it means
# "re-probe with the 53-name instrument before writing any absence claim".
set -uo pipefail
cd "$(dirname "$0")"
one() {
  # NOTE: bash cannot export an ARRAY to an `xargs bash -c` child, so the name list
  # MUST live inside this function.  p525's first run put it at file scope, every
  # child saw an empty list, and the sweep reported UNRESOLVED-on-7 for 137 of 138
  # addresses -- caught by the tally, not by a row.
  local NAMES=(LICENSE LICENSE.md LICENSE.txt LICENCE COPYING LICENSE-CODE NOTICE)
  slug="$1"
  symref=$(git ls-remote --symref "https://github.com/${slug}" HEAD 2>/dev/null)
  if [ -z "$symref" ]; then printf '%s\tDEAD-OR-PRIVATE\t-\t-\t-\t-\t-\t-\n' "$slug"; return; fi
  br=$(printf '%s' "$symref" | sed -n 's#^ref: refs/heads/\([^\t]*\).*#\1#p' | head -1)
  # The symref line ALSO ends in "HEAD" ("ref: refs/heads/master\tHEAD"), so a
  # /HEAD$/ match returns "ref:" as the SHA and every raw read 404s.  p525's first
  # two runs did exactly that and reported UNRESOLVED-on-7 for 137 of 138 addresses.
  # Require a 40-hex first field.
  sha=$(printf '%s' "$symref" | awk '$1 ~ /^[0-9a-f]{40}$/ {print $1; exit}')
  for n in "${NAMES[@]}"; do
    tmp=$(mktemp)
    code=$(curl -s -m 25 -w '%{http_code}' -o "$tmp" "https://raw.githubusercontent.com/${slug}/${sha}/${n}")
    if [ "$code" = "200" ]; then
      bytes=$(wc -c < "$tmp" | tr -d ' ')
      dig=$(sha256sum "$tmp" | cut -c1-16)
      out=$(python3 -I title_grant.py "$tmp")
      printf '%s\tLIVE\t%s\t%s\t%s\t%s\t%s\t%s\n' "$slug" "$br" "${sha:0:12}" "$n" "$bytes" "$dig" "$(printf '%s' "$out" | cut -f2,3 | tr '\t' '|')"
      rm -f "$tmp"; return
    fi
    rm -f "$tmp"
  done
  printf '%s\tLIVE\t%s\t%s\tUNRESOLVED-on-7\t-\t-\t-\n' "$slug" "$br" "${sha:0:12}"
}
export -f one
printf 'slug\tlive\tdefault_branch\thead_sha\tgrant_file\tbytes\tsha256_16\tfamily|confidence\n'
xargs -a candidates.txt -I{} -P 8 bash -c 'one "$@"' _ {}
