#!/usr/bin/env bash
# p1040 limb A -- re-run the licence census over the WHOLE corpus with
# classify_ecl WIRED IN, not beside it.
#
# Usage: bash census.sh <addresses-file> [parallelism]   # TSV on stdout
#
# TWO changes from p1029/probe.sh, both measured before being relied on:
#
# 1. THE REF. p1029 spent one `git ls-remote --symref` per address purely to
#    learn the default branch name for the raw path. raw.githubusercontent.com
#    serves the literal ref `HEAD`, so that round-trip is unnecessary:
#    sakaiproject/sakai answers 200 at HEAD and 404 at `main` (its default is
#    master), which is the case that would have broken a guessed branch name.
#    Dropping it removes 1-2 git round-trips per address and is what makes a
#    1 395-address census affordable at all. Calibrated in test_p1040.sh
#    against p1029's own 99-row result, licence for licence.
#
# 2. ls-remote BECOMES THE TIE-BREAKER, NOT THE FIRST STEP. Without it there is
#    no way to tell "repository is gone" from "repository has no LICENSE and no
#    README" -- both are a pair of 404s. So it runs ONLY for the addresses where
#    licence AND control both came back non-200, which is the handful of rows
#    where the distinction is load-bearing (P1005 applied to the ABSENT verdict
#    rather than to the grant).

set -u
cd "$(dirname "$0")"
. ./classify.sh

export GIT_TERMINAL_PROMPT=0
ADDR_FILE="${1:-lost-addresses.corpus-census-1381.2026-10-10.txt}"
PAR="${2:-8}"

# Identical list and order to p1029, so a divergence can only come from the ref
# change and never from looking in a different place.
LICENCE_NAMES="LICENSE LICENSE.md LICENSE.txt LICENCE LICENCE.md COPYING COPYING.txt LICENSE.rst MIT-LICENSE LICENSE-MIT LICENSE-APACHE"

OUT=$(mktemp -d)
trap 'rm -rf "$OUT"' EXIT
export OUT LICENCE_NAMES

probe_one() {
  local slug="$1"
  local tmp; tmp=$(mktemp -d)
  local lic="ABSENT" licfile="-" bytes="-" sum="-" bucket="-" diverge="-"
  local code ctl status

  for name in $LICENCE_NAMES; do
    code=$(curl -sS --max-time 45 -o "$tmp/payload" -w '%{http_code}' \
             "https://raw.githubusercontent.com/${slug}/HEAD/${name}" 2>/dev/null || echo 000)
    if [ "$code" = "200" ]; then
      licfile="$name"
      bytes=$(wc -c < "$tmp/payload" | tr -d ' ')
      sum=$(sha256sum "$tmp/payload" | cut -c1-16)
      lic=$(classify_grant "$tmp/payload")
      bucket=$(bucket_of "$lic")
      diverge=$(divergence_flag "$tmp/payload")
      break
    fi
  done

  ctl=$(curl -sS --max-time 45 -o "$tmp/ctl" -w '%{http_code}' \
          "https://raw.githubusercontent.com/${slug}/HEAD/README.md" 2>/dev/null || echo 000)
  [ "$ctl" = "200" ] && ctl="200/$(wc -c < "$tmp/ctl" | tr -d ' ')B"

  status="LIVE"
  if [ "$lic" = "ABSENT" ]; then
    case "$ctl" in
      200/*) status="LIVE-NOGRANT" ;;
      # Gap 388: the one open payload channel throttles, and a throttle
      # publishes as a negative. 429 is NOT an absence of grant -- the row is
      # unmeasured and says so, so a retry can target exactly these rows.
      429)   status="THROTTLED" ;;
      *)
        # The tie-breaker, and the ONLY place this limb spends a git round-trip.
        if timeout 60 git ls-remote --symref "https://github.com/${slug}" HEAD >/dev/null 2>&1; then
          status="LIVE-NOCONTROL"
        else
          status="ABSENT"
        fi ;;
    esac
  fi

  printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' \
    "$slug" "$status" "$lic" "$bucket" "$licfile" "$bytes" "$sum" "$diverge" "$ctl" \
    > "$OUT/$(printf '%s' "$slug" | tr '/' '_').row"
  rm -rf "$tmp"
}
# The export list is DERIVED from classify.sh, never hand-maintained.
#
# Twice in one pass a function was added to classify.sh and not to this line,
# and the second time the hand-written guard below missed it too -- because the
# guard had its own copy of the same list. `declares_known_grant` was added,
# exported nowhere, and 1 381 rows' worth of "command not found" went to stderr
# while the census emitted rows regardless.
#
# A guard keyed on a hand-maintained list fails in exactly the case it exists
# for: someone adds a function and updates neither place. So the list comes
# from the file itself -- every top-level `name()` definition in classify.sh --
# and adding a function to classify.sh now exports it with no second edit.
CLASSIFY_FNS=$(grep -oE '^[a-z_][a-z0-9_]*\(\)' classify.sh | tr -d '()')
[ -n "$CLASSIFY_FNS" ] || { printf 'REFUSING TO RUN: no functions found in classify.sh\n' >&2; exit 2; }
for fn in $CLASSIFY_FNS; do export -f "$fn"; done
export -f probe_one

# GUARD, added after this limb published 1 077 empty families.
#
# probe_one runs inside an `xargs bash -c` subshell, so every function it calls
# must be named in `export -f`. Two functions added to classify.sh this pass
# were not. The subshell's "command not found" went to stderr while the census
# wrote a row for each address anyway: classify_restricted failed, its output
# was empty, the empty string fell through classify_grant's final case, and
# 1 077 rows published a BLANK licence that tallied as UNREAD.
#
# That is the Gap 398 failure mode in its purest form -- a silence counted as
# data -- produced by this instrument's own plumbing rather than by any licence
# text. The export list is now checked against a child shell's own view of what
# is exported, and the census REFUSES to emit rows if any function is missing.
#
# The check is the child shell's, deliberately: asking `declare -F` in THIS
# shell would answer yes for a function that is defined here and not exported,
# which is exactly the state that caused the failure. It now iterates the
# DERIVED list, so it cannot go stale against classify.sh either.
for fn in probe_one $CLASSIFY_FNS; do
  if ! bash -c "declare -F $fn >/dev/null 2>&1"; then
    printf 'REFUSING TO RUN: %s is defined but not exported to the worker subshell\n' "$fn" >&2
    exit 2
  fi
done

printf 'slug\tstatus\tlicence\tbucket\tfile\tbytes\tsha256\tdivergence\tcontrol\n'

grep -v '^[[:space:]]*\(#\|$\)' "$ADDR_FILE" \
  | xargs -r -P "$PAR" -I{} bash -c 'probe_one "$@"' _ {}

# Sorted, so the file is byte-reproducible regardless of which worker finished
# first (p399's census-order gate applies to a parallel census too).
cat "$OUT"/*.row 2>/dev/null | LC_ALL=C sort -t"$(printf '\t')" -k1,1
