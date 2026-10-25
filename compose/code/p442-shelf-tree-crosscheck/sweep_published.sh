#!/usr/bin/env bash
# p442 — RE-MEASURE every payload cell this base publishes, and separate the three ways a
# cell can fail to reproduce.
#
# 🔵 Why a third verdict exists.  `P834` says the bytes run of a payload is destroyed by
# `$(…)`, and `lib/payload_measure.sh::size_of_file` is the fix.  A cell measured through a
# capture is therefore not merely WRONG — it is wrong by a signature: its byte count is
# short by the trailing-newline run and its digest is the digest OF THE STRIPPED BYTES.  So
# this sweep computes BOTH digests and reports which one the shelf published:
#
#   REPRODUCES        bytes and digest match the file  -> the cell was measured correctly
#   CAPTURE-MEASURED  bytes and digest match `printf '%s' "$(cat f)"` -> `P834`, in the cell
#   MISMATCH          neither -> the payload CHANGED, or the cell was never measured
#   NO-PAYLOAD        the path the cell names is not in the repository at that ref
#   UNRESOLVED        the repository does not resolve over `git`
#
# A capture signature is a MEASURED claim about how the number was produced, not a guess:
# the stripped digest is reproduced here, beside the file's own.
set -uo pipefail
LIB="$(cd "$(dirname "$0")/../lib" && pwd)"
. "$LIB/payload_measure.sh"

printf 'slug\tref\tpub_path\tpath\tpub_bytes\tpub_sha12\tfile_bytes\tfile_sha12\tcapture_sha12\tverdict\n'
tail -n +2 "$1" | while IFS=$'\t' read -r file line slug path pub_bytes pub_sha head; do
  [ -z "${slug:-}" ] && continue
  br=$(timeout 25 git ls-remote --symref "https://github.com/$slug" HEAD 2>/dev/null \
        | sed -n 's|^ref: refs/heads/\(.*\)\tHEAD$|\1|p' | head -1)
  if [ -z "$br" ]; then
    printf '%s\t-\t%s\t%s\t%s\t%s\t0\t-\t-\tUNRESOLVED\n' "$slug" "$path" "$path" "$pub_bytes" "$pub_sha"; continue
  fi
  # Declared normalisation: a published path whose FIRST segment is the branch name is a
  # branch-qualified spelling of a root file (`master/LICENSE`), not a subdirectory.  Only
  # that exact case is stripped; `docs/License.txt` is left alone.
  p="$path"; case "$path" in "$br"/*) p="${path#"$br"/}";; esac
  # The row's own HEAD is the ref it claims to have measured.  Measuring at today's HEAD
  # instead would conflate an upstream edit with a mismeasurement.
  ref="$br"; [ "$head" != "-" ] && ref="$head"
  tmp=$(mktemp)
  curl -sS --max-time 25 "https://raw.githubusercontent.com/$slug/$ref/$p" > "$tmp" 2>/dev/null
  if [ ! -s "$tmp" ] || head -1 "$tmp" | grep -q '^404: Not Found$'; then
    printf '%s\t%s\t%s\t%s\t%s\t%s\t0\t-\t-\tNO-PAYLOAD\n' "$slug" "$ref" "$path" "$p" "$pub_bytes" "$pub_sha"
    rm -f "$tmp"; continue
  fi
  fb=$(size_of_file "$tmp")
  fs=$(sha12_of_file "$tmp")
  cs=$(sha12_of_capture_BROKEN "$tmp")   # the library's own P834 control, not a hand-rolled capture
  if [ "$fs" = "$pub_sha" ]; then v=REPRODUCES
  elif [ "$cs" = "$pub_sha" ]; then v=CAPTURE-MEASURED
  else v=MISMATCH; fi
  printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' "$slug" "$ref" "$path" "$p" "$pub_bytes" "$pub_sha" "$fb" "$fs" "$cs" "$v"
  rm -f "$tmp"
done
