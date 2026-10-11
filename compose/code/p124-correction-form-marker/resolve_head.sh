#!/usr/bin/env bash
# Resolve an address's EXISTENCE and DEFAULT BRANCH in one call.
# Carried from p123 (which carried it from p122) UNCHANGED in behaviour.
# p124 depends on it for ACTION AE: the gold set must contain rows whose
# default branch is neither `main` nor `master`, and only this script knows.
# usage: resolve_head.sh ADDRESS_LIST > out.tsv
# output: address <TAB> EXISTS|ABSENT <TAB> default-branch|-
set -uo pipefail
resolve() {
  local addr="$1" out br
  out="$(GIT_TERMINAL_PROMPT=0 timeout 25 git ls-remote --symref \
        "https://github.com/${addr}" HEAD 2>&1)"
  if printf '%s' "$out" | grep -q '^ref:'; then
    br="$(printf '%s' "$out" | grep -m1 '^ref:' | sed 's#ref: refs/heads/##; s#[[:space:]]*HEAD##')"
    printf '%s\tEXISTS\t%s\n' "$addr" "$br"
  else
    printf '%s\tABSENT\t-\n' "$addr"
  fi
}
export -f resolve
grep -vE '^\s*(#|$)' "$1" | xargs -P 10 -I{} bash -c 'resolve "$@"' _ {}
