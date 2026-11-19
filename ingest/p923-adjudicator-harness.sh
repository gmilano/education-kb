#!/usr/bin/env bash
# p923 offline fixture harness: runs ONLY the adjudicator, over local payload files.
# Extracts the function by its own delimiters so it cannot drift out of date (p923).
set -uo pipefail
SRC="${SRC:-/home/user/education-kb/ingest/p913-grant-authority.sh}"
eval "$(awk '/^adjudicate\(\) \{/{p=1} p{print} p&&/^\}/{exit}' "$SRC")"
for f in "$@"; do
  b=$(wc -c < "$f" | tr -d ' ')
  printf '%s\t%s\t%s\n' "$(basename "$f")" "$b" "$(adjudicate "$f" "$b" | tr '\t' '|')"
done
