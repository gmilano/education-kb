#!/usr/bin/env bash
# p275 — the ONLINE half.  Kept OUT of `make hooks` so the standing check stays runnable
# where there is no egress (the Makefile's own rule).
#
# Replaces a path LADDER with a path ENUMERATION.  Two stages:
#   1. git ls-remote  -> does the slug resolve at all?  (p274's positive control: the
#      gegok12 refusal was 15 probes against a string that was never a repository.)
#   2. blobless shallow clone + git ls-tree -r --name-only HEAD  -> every path that exists.
#
# A ladder can only refute the paths it tried.  This cannot miss a path, because it never
# guesses one.  Emits the TSV that evidence/tree-enumeration.*.tsv is built from.
#
#   ./enumerate.sh < slugs.txt > ../../../evidence/tree-enumeration.$(date +%F)-pNNN.tsv
set -uo pipefail
WORK="${WORK:-$(mktemp -d)}"
printf "slug\tls_remote\thead_sha\tfiles_in_tree\tlicence_like_paths_in_tree\n"
while read -r slug; do
  [ -z "${slug// }" ] && continue
  case "$slug" in \#*) continue;; esac
  out=$(GIT_TERMINAL_PROMPT=0 timeout 45 git ls-remote "https://github.com/$slug" HEAD 2>&1)
  sha=$(echo "$out" | awk '/HEAD/{print substr($1,1,12); exit}')
  if [ -z "$sha" ]; then
    # Indistinguishable from a nonexistent repo -- which is the WHOLE point of the control.
    printf "%s\tFAIL\t-\t-\tSLUG_DOES_NOT_RESOLVE\n" "$slug"
    continue
  fi
  d="$WORK/$(echo "$slug" | tr '/' '_')"
  rm -rf "$d"
  if GIT_TERMINAL_PROMPT=0 timeout 240 git clone --depth 1 --filter=blob:none \
       --no-checkout --quiet "https://github.com/$slug" "$d" >/dev/null 2>&1; then
    all=$(git -C "$d" ls-tree -r --name-only HEAD 2>/dev/null)
    n=$(printf '%s' "$all" | grep -c .)
    lic=$(printf '%s' "$all" \
          | grep -i -E '(^|/)(licen[cs]e|copying|notice|unlicense|eupl|copyright)' \
          | paste -sd',' -)
    printf "%s\tOK\t%s\t%s\t%s\n" "$slug" "$sha" "$n" "${lic:-NONE_IN_TREE}"
  else
    printf "%s\tOK\t%s\tCLONE_FAIL\t-\n" "$slug" "$sha"
  fi
  sleep 1   # the session git proxy caps concurrent smart-HTTP ops; serialise deliberately
done
