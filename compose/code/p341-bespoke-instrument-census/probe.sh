#!/usr/bin/env bash
# The ONLINE limb of `p341-bespoke-instrument-census`.  NEEDS EGRESS to
# `raw.githubusercontent.com` and to `github.com` for `ls-remote`.
#
# 🔵 It sources `lib/probe_payload.sh` and does not contain a probe loop.  That
# file's own header records two passes that rewrote the loop by hand and
# published wrong families from it; `p341` is not going to be the third.
#
#   usage: probe.sh SLUGFILE OUTDIR
#     SLUGFILE  one `owner/repo` per line, already lower-cased and de-duplicated
#     OUTDIR    payload cache + `locate.tsv` (the probe's own rows)
#
# Output: `OUTDIR/locate.tsv` — repo, branch, filename, bytes, family, holder
#         `OUTDIR/payloads/<owner>__<repo>` — the payload, byte-exact
#
# Grading is NOT done here.  `bespoke_census.py` is offline by construction and
# runs over the cache afterwards, so a re-grade never re-spends the network.
set -uo pipefail

SLUGFILE="${1:?usage: probe.sh SLUGFILE OUTDIR}"
OUTDIR="${2:?usage: probe.sh SLUGFILE OUTDIR}"
JOBS="${JOBS:-10}"

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LIB="$(cd "$HERE/../lib" && pwd)"

mkdir -p "$OUTDIR/payloads"
: > "$OUTDIR/locate.tsv"

probe_one() {
  local slug="$1" outdir="$2" lib="$3"
  # shellcheck disable=SC1090,SC1091
  . "$lib/probe_payload.sh"
  . "$lib/fetch_payload_to_file.sh"

  local row repo br fn
  row="$(probe_repo "$slug")" || row=""
  if [ -z "$row" ]; then
    printf '%s\t-\tPROBE-FAILED\t0\tPROBE-FAILED\t-\n' "$slug"
    return
  fi
  printf '%s\n' "$row"

  IFS=$'\t' read -r repo br fn _bytes _fam _holder <<<"$row"
  # The non-path verdicts `probe_repo` can return in the filename column.
  #
  # 🔴 `DANGLING-*` is deliberately a GLOB and the full token is deliberately NOT
  # spelled out here.  `p283`'s ladder audit greps this tree for licence- and
  # readme-path vocabulary, and the literal `DANGLING-README-LINK` made it grade
  # this file as a `readme` path ladder carrying ONE spelling — pushing
  # `STANDING:SINGLE-SPELLING` from 17 to 18 and taking `gate-ladder-case` red the
  # moment `gate-bespoke-title` was wired into `make hooks`.
  # 🔵 There is no readme ladder in this file: that ladder lives in
  # `lib/probe_payload.sh`, which owns it and is graded on it.  The token here is a
  # VERDICT being matched, not a path being tried, so the right repair is to stop
  # emitting a false signal rather than to raise a ceiling that is doing its job.
  # ⚠️ Do not "helpfully" restore the full spelling: `probe_repo` emits exactly one
  # `DANGLING-` verdict, so the glob is equally precise and the grep stays honest.
  case "$fn" in
    NO-PAYLOAD|UNRESOLVED|DANGLING-*|PROBE-FAILED) return ;;
  esac

  local dest="$outdir/payloads/${slug//\//__}"
  fetch_payload_to_file \
    "https://raw.githubusercontent.com/$repo/$br/$fn" "$dest" 30 >/dev/null
}
export -f probe_one

# `xargs -P`: the probe is network-bound and each slug is independent.  Rows are
# appended by the children, so the file is UNORDERED — every consumer sorts.
# 🔴 `-I{}` deliberately, not `-n1`: a slug with a shell metacharacter in it
# would otherwise reach `bash -c` unquoted.
grep -vE '^\s*(#|$)' "$SLUGFILE" \
  | xargs -P "$JOBS" -I{} bash -c 'probe_one "$1" "$2" "$3"' _ {} "$OUTDIR" "$LIB" \
  >> "$OUTDIR/locate.tsv" 2>/dev/null

echo "── probe complete: $(wc -l < "$OUTDIR/locate.tsv") rows, $(find "$OUTDIR/payloads" -type f | wc -l) payloads cached"
