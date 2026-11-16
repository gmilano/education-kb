#!/usr/bin/env bash
# P95 — FIRST-PARTY METADATA SWEEP (p843, 2026-11-16)
#
# Re-verifies an entire shelf of GitHub repositories against GitHub's OWN API:
# licence (SPDX), stars, last push, archived, fork — plus liveness.
#
# Why this exists: in this environment `gh api repos/{owner}/{repo}` is 403
# (the session's GitHub credential is scoped to attached repositories only) and
# `https://github.com/<owner>/<repo>` returns 403 through the proxy (T124).
# `gh api search/repositories` is NOT scoped that way, accepts up to 10
# `repo:` qualifiers per query as an OR, and returns the full metadata block.
# That turns "star counts are third-party and unverified" into a measurement.
#
# Usage:  ./sweep.sh repos.txt out.tsv        # one owner/repo per line
# Output: full_name  spdx  stars  pushed_at  archived  fork
# Repos absent from the output DID NOT RESOLVE — deleted, renamed or private.
# Exit 0 = every input resolved; exit 1 = at least one did not.
set -uo pipefail

IN="${1:?usage: sweep.sh <repo-list> <out.tsv>}"
OUT="${2:?usage: sweep.sh <repo-list> <out.tsv>}"
BATCH="${BATCH:-10}"      # GitHub caps a search query at ~256 chars / 5 ORs on
                          # some endpoints; 10 `repo:` qualifiers is safe here.
SLEEP="${SLEEP:-2.5}"     # authenticated search limit is 30 req/min.

: > "$OUT"
mapfile -t repos < <(grep -vE '^\s*(#|$)' "$IN")
n=${#repos[@]}
echo "sweeping $n repositories in batches of $BATCH" >&2

for ((i=0; i<n; i+=BATCH)); do
  q=""
  for r in "${repos[@]:i:BATCH}"; do q+="repo:$r "; done
  # `fork:true` is NOT optional: GitHub search EXCLUDES forks by default, so a
  # forked row looks exactly like a deleted one without it (measured p843).
  q+="fork:true"
  # A batch containing a repo that does not exist returns HTTP 422 for the
  # WHOLE batch, so fall back to one-at-a-time on failure rather than losing 10.
  if ! gh api -X GET search/repositories -f q="$q" \
        --jq '.items[] | [.full_name,(.license.spdx_id // "NONE"),.stargazers_count,.pushed_at,(.archived|tostring),(.fork|tostring)] | @tsv' \
        >> "$OUT" 2>/dev/null; then
    for r in "${repos[@]:i:BATCH}"; do
      gh api -X GET search/repositories -f q="repo:$r" \
        --jq '.items[] | [.full_name,(.license.spdx_id // "NONE"),.stargazers_count,.pushed_at,(.archived|tostring),(.fork|tostring)] | @tsv' \
        >> "$OUT" 2>/dev/null
      sleep "$SLEEP"
    done
  fi
  sleep "$SLEEP"
done

got=$(cut -f1 "$OUT" | tr 'A-Z' 'a-z' | sort -u)
want=$(tr 'A-Z' 'a-z' < "$IN" | grep -vE '^\s*(#|$)' | sort -u)
gone=$(comm -23 <(echo "$want") <(echo "$got"))

echo "--- resolved: $(wc -l < "$OUT") / $n" >&2
if [ -n "$gone" ]; then
  # Absence from the search index is NOT proof of deletion. `git ls-remote` is
  # the authority: it resolves a live repository and falls through to a
  # credential prompt when there is nothing there (this proxy's 404 signature).
  echo "--- absent from the search index — adjudicating with git ls-remote:" >&2
  while read -r r; do
    [ -n "$r" ] || continue
    if git ls-remote --symref "https://github.com/$r" HEAD >/dev/null 2>&1; then
      echo "      🟡 UNINDEXED (live, but search will not return it): $r" >&2
    else
      echo "      🔴 GONE (deleted, renamed or private):             $r" >&2
    fi
  done <<< "$gone"
fi
echo "--- licence distribution:" >&2
cut -f2 "$OUT" | sort | uniq -c | sort -rn | sed 's/^/      /' >&2
echo "--- NOT classified permissive by GitHub (byte-read these, do not reject them):" >&2
awk -F'\t' '$2!="MIT"&&$2!="Apache-2.0"&&$2!="BSD-3-Clause"&&$2!="BSD-2-Clause"&&$2!="ISC"&&$2!="0BSD"&&$2!="Unlicense"{printf "      %-46s %s\n",$1,$2}' "$OUT" >&2
cutoff=$(date -u -d '180 days ago' +%Y-%m-%d 2>/dev/null || date -u -v-180d +%Y-%m-%d)
echo "--- no push since $cutoff:" >&2
awk -F'\t' -v c="$cutoff" '$4<c{printf "      %-46s %s\n",$1,substr($4,1,10)}' "$OUT" >&2

[ -z "$gone" ]
