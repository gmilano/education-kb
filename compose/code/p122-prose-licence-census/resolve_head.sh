#!/usr/bin/env bash
# Resolve an address's EXISTENCE and DEFAULT BRANCH in one call (p122).
#
# Every licence probe in this KB before p122 GUESSED the branch (main, then
# master). That is why p120 needed 462 probes to read 52 files: 410 were
# 404s, and a 404 from raw.githubusercontent cannot tell you whether the
# BRANCH was wrong, the PATH was wrong, or the REPOSITORY does not exist.
#
# `git ls-remote --symref` answers all three: a public repository returns its
# symbolic HEAD, and a missing or private one fails asking for credentials.
# This matters beyond efficiency — p122 found 3 addresses that had been
# inferred from a product name in vendor prose and do not exist at all.
# Without this channel they would have been published as "no licence file".
#
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
grep -vE '^\s*(#|$)' "$1" | xargs -P 12 -I{} bash -c 'resolve "$@"' _ {}
