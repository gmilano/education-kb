#!/bin/sh
# P793 — GATE 0 of the pre-flight: resolve the ref BEFORE any other gate reads a byte.
#
# `raw.githubusercontent.com` serves the DEFAULT branch for the literal ref `master`, even when the
# repository has no `master`. Measured 3 of 3 with a control: `main` 404, an invented branch 404,
# `master` 200, `HEAD` 200 — on repositories whose real defaults are `refs/heads/0.7`,
# `refs/heads/public` and `refs/heads/2.12`. So "payload-read at master" is not provenance, and
# every gate that takes a `[ref]` argument inherits the error if it is handed one.
#
# Exit codes, so it composes in a pre-flight:
#   0  resolved, and the default is `main` or `master`     -> the usual assumption holds
#   3  resolved, and the default is NEITHER               -> pass THIS ref to the other gates
#   5  unresolved (ls-remote did not answer)              -> no gate below may claim an absence
#   2  usage
set -u

[ "$#" -ge 1 ] || { echo "usage: sh ref.sh <owner/repo> [...]" >&2; exit 2; }

rc=0
for slug in "$@"; do
  case "$slug" in
    */*) : ;;
    *) printf '%s\tBAD-SLUG\t-\t-\n' "$slug"; rc=2; continue ;;
  esac
  ref=$(timeout 40 git ls-remote --symref "https://github.com/$slug" HEAD 2>/dev/null \
        | awk '/^ref:/{sub(/^refs\/heads\//, "", $2); print $2; exit}')
  sha=$(timeout 40 git ls-remote "https://github.com/$slug" HEAD 2>/dev/null \
        | awk 'NR==1{print substr($1,1,7); exit}')
  if [ -z "$ref" ]; then
    printf '%s\tUNRESOLVED\t-\t-\n' "$slug"
    [ "$rc" -lt 5 ] && rc=5
    continue
  fi
  case "$ref" in
    main|master) printf '%s\tDEFAULT-IS-NAMED\t%s\t%s\n' "$slug" "$ref" "${sha:--}" ;;
    *)           printf '%s\tDEFAULT-IS-NEITHER\t%s\t%s\n' "$slug" "$ref" "${sha:--}"
                 [ "$rc" -lt 3 ] && rc=3 ;;
  esac
done
exit "$rc"
