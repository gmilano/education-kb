#!/usr/bin/env bash
# p442 — read EVERY grant the tree carries, not the first one a filename ladder finds.
#
# Gap 441-A: `lib/probe_payload.sh::probe_repo` RETURNS ON THE FIRST LADDER HIT, so every
# shelf cell on this base names exactly one payload per repository.  `p441`'s tree
# enumerator (`p441-tree-licence-enumeration/enumerate_licence.py`) already answers the
# question the ladder cannot — it is simply not what any pass sources.  This script does not
# re-implement either one: it SOURCES the shared measurement half and READS the paths the
# enumerator returned, so the only new thing here is the JOIN.
#
# In: a TSV of `repo <TAB> path` on stdin.  Out: repo, branch, path, bytes, sha256₁₂, family,
# holder — measured from the file where it landed (`P834`), never from a capture.
set -uo pipefail
LIB="$(cd "$(dirname "$0")/../lib" && pwd)"
. "$LIB/payload_measure.sh"

printf 'repo\tbranch\thead\tpath\tbytes\tsha12\tfamily\tholder\n'
while IFS=$'\t' read -r repo path; do
  [ -z "${repo:-}" ] && continue
  br=$(timeout 25 git ls-remote --symref "https://github.com/$repo" HEAD 2>/dev/null \
        | sed -n 's|^ref: refs/heads/\(.*\)\tHEAD$|\1|p' | head -1)
  head=$(timeout 25 git ls-remote "https://github.com/$repo" HEAD 2>/dev/null | awk '{print substr($1,1,12)}' | head -1)
  [ -z "$br" ] && { printf '%s\t-\t-\t%s\t0\tUNRESOLVED\tUNRESOLVED\t-\n' "$repo" "$path"; continue; }
  tmp=$(mktemp)
  curl -sS --max-time 25 "https://raw.githubusercontent.com/$repo/$br/$path" > "$tmp" 2>/dev/null
  if [ -s "$tmp" ] && ! head -1 "$tmp" | grep -q '^404: Not Found$'; then
    printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' "$repo" "$br" "$head" "$path" \
      "$(size_of_file "$tmp")" "$(sha256sum "$tmp" | cut -c1-12)" \
      "$(family_of_file "$tmp")" "$(holder_of_file "$tmp")"
  else
    printf '%s\t%s\t%s\t%s\t0\t-\tNO-PAYLOAD\t-\n' "$repo" "$br" "$head" "$path"
  fi
  rm -f "$tmp"
done
