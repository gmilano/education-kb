#!/bin/bash
# p436 — re-verify a restoration tranche FIRST-HAND before any row is written back.
#
# 🔴 THIS FILE WAS WRITTEN WRONG ONCE, AND THE LIBRARY IT IGNORED PREDICTED IT.
# `lib/probe_payload.sh` opens with "SHARED PAYLOAD PROBE — source this, do not rewrite
# it", and records two prior passes that rewrote the probe loop from scratch and
# re-imported defects this base had already measured and fixed.  p436's first build of
# this file hand-rolled a `curl` ladder over `main`/`master` with an uppercase-only
# filename list -- the THIRD recorded instance of that error.  It was caught by
# `gate-ladder-case`, whose ratchet went red on `STANDING:SINGLE-SPELLING` 18 -> 19,
# because the hand-rolled ladder was used to decide a file was ABSENT.
#
# 🟢 What the library buys that the hand-rolled loop did not:
#   * the default branch resolved with `ls-remote --symref` rather than assumed (measured
#     on real education platforms: `v31.0.00`, `2.12`, `mobile`);
#   * the README's own licence LINK tried before an absence verdict, so a mixed-case
#     subdirectory payload (`docs/License.txt`) is found;
#   * `LICENCE` (British spelling), measured at 1 payout in 44;
#   * `DANGLING-README-LINK` kept distinct from `NO-PAYLOAD` -- a maintainer who believes
#     they granted is an upstream ASK, not a refusal;
#   * the family classifier that does NOT read GPL-3.0 §6's "noncommercially" as a
#     NonCommercial grant.
#
# The recency channel stays here because it is p435's, not the payload library's:
# a treeless bare clone gives HEAD's committer date AND timezone offset in ~0.5 s,
# which is the channel `gate-offset-region` places regions with.
#
#   usage: restore_sweep.sh SLUG_FILE WORKDIR
#
# 🔴 `set -u` is deliberately NOT used: `lib/probe_payload.sh` references optional
# variables, and under `-u` every `probe_repo` call returned an EMPTY row -- a silent
# all-blank payload column, which is the worst possible failure mode for an instrument
# whose output becomes shelf evidence.  Arguments are validated explicitly instead.
set +u
SLUGS="${1:-}"
WORK="${2:-}"
if [ -z "$SLUGS" ] || [ -z "$WORK" ]; then
  echo "usage: restore_sweep.sh SLUG_FILE WORKDIR" >&2
  echo "  SLUG_FILE  one owner/repo per line" >&2
  echo "  WORKDIR    scratch directory for the treeless clones" >&2
  exit 2
fi
if [ ! -s "$SLUGS" ]; then
  echo "restore_sweep.sh: empty or missing slug file: $SLUGS" >&2
  exit 2
fi

_HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
# shellcheck source=/dev/null
. "$_HERE/../lib/probe_payload.sh" || {
  echo "restore_sweep.sh: cannot source lib/probe_payload.sh -- refusing to hand-roll a probe" >&2
  exit 2
}

mkdir -p "$WORK" || exit 2
printf 'slug\tbranch\tpath\tbytes\tfamily\tholder\thead_sha\thead_date\thead_offset\n'
while IFS= read -r slug; do
  [ -n "$slug" ] || continue
  case "$slug" in \#*) continue ;; esac
  row=$(probe_repo "$slug")
  hs=""; hd=""; ho=""
  if git clone --quiet --depth 1 --bare --filter=tree:0 \
       "https://github.com/$slug" "$WORK/h.git" >/dev/null 2>&1; then
    hs=$(git -C "$WORK/h.git" rev-parse HEAD 2>/dev/null | cut -c1-12)
    hd=$(git -C "$WORK/h.git" log -1 --format=%cd --date=short 2>/dev/null)
    ho=$(git -C "$WORK/h.git" log -1 --format=%ci 2>/dev/null | awk '{print $3}')
  fi
  rm -rf "$WORK/h.git"
  printf '%s\t%s\t%s\t%s\n' "$row" "${hs:--}" "${hd:--}" "${ho:--}"
done < "$SLUGS"
