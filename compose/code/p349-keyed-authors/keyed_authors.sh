#!/bin/bash
# `p349-keyed-authors` — discharges `ACTION ZZ-ac`: AN AUTHOR COUNT WITHOUT A KEY CANNOT BE
# RE-DERIVED, so this instrument never emits one.  p348 measured the cost first-hand:
# `terracotta-education/terracotta` is published on these shelves as "2 815 commits, 18
# authors"; the commit count re-derives exactly and the author count re-derives under NO
# obvious key -- %an 14 / %ae 18 / %an|%ae 20.  A successor reaching for `%an` (which
# p346's PII refusal makes the likely reach) reads every published author figure as
# inflated, which looks like repositories losing contributors.
#
# So every row this instrument writes carries THREE author columns, each keyed, and the
# shelf cell that quotes one of them has to name which.  The same blobless clone pays for
# the placement channel (commit timezones), so region and authors are ONE read.
#
#   keyed_authors.sh <slugs-file> -> TSV on stdout
#   cols: slug  head  commits  an  ae  an_ae  tz_top  tz_top_n  tz_all  first  last
#
# Channels and their declared LIMITS:
#   * `commits`  -- every commit reachable from HEAD.  Exact and re-derivable.
#   * `an/ae/an_ae` -- distinct author NAMES / ADDRESSES / pairs.  Aggregate counts only:
#     no name and no address is ever written out (p346's refusal).
#   * `tz_*`     -- author-time UTC offsets.  A PLACEMENT channel, not a nationality:
#     p346's and p348's rule stands, a name is not a channel and neither is an offset
#     alone.  `tz_all` prints the whole histogram so a mixed stream is VISIBLE rather
#     than collapsed into a single verdict.
set -uo pipefail
IN="${1:?usage: keyed_authors.sh <slugs-file>}"
TMP="$(mktemp -d)"; trap 'rm -rf "$TMP"' EXIT
printf 'slug\thead\tcommits\tan\tae\tan_ae\ttz_top\ttz_top_n\ttz_all\tfirst\tlast\n'
while read -r slug; do
  [ -z "$slug" ] && continue
  case "$slug" in \#*) continue;; esac
  head_sha="$(timeout 60 git ls-remote "https://github.com/$slug" HEAD 2>/dev/null | awk 'NR==1{print substr($1,1,12)}')"
  [ -z "$head_sha" ] && { printf '%s\tNO-PIN\t-\t-\t-\t-\t-\t-\t-\t-\t-\n' "$slug"; continue; }
  d="$TMP/$(echo "$slug" | tr '/' '_')"
  if ! timeout 420 git clone --quiet --filter=blob:none --no-checkout "https://github.com/$slug" "$d" >/dev/null 2>&1; then
    printf '%s\t%s\tNO-CLONE\t-\t-\t-\t-\t-\t-\t-\t-\n' "$slug" "$head_sha"; continue
  fi
  commits=$(git -C "$d" rev-list --count HEAD)
  an=$(git -C "$d" log --format='%an' | sort -u | wc -l)
  ae=$(git -C "$d" log --format='%ae' | sort -u | wc -l)
  anae=$(git -C "$d" log --format='%an|%ae' | sort -u | wc -l)
  tz_all=$(git -C "$d" log --format='%ad' --date=format:'%z' | sort | uniq -c | sort -rn \
            | awk '{printf "%s×%s ", $1, $2}')
  # 🔴 Build 1 of this script read the top offset with `cut -d'×'`, and `cut` refuses a
  # MULTIBYTE delimiter: "the delimiter must be a single character", twice per row, on
  # stderr, while the row itself printed fine with `-` in both columns.  A defect that
  # writes a PLAUSIBLE value is worse than one that crashes, and `×` was this base's own
  # choice of separator.  Bash parameter expansion is byte-blind, so it is the control.
  tz_first=${tz_all%% *}
  tz_top=${tz_first#*×}
  tz_top_n=${tz_first%%×*}
  first=$(git -C "$d" log --reverse --format='%ad' --date=short | head -1)
  last=$(git -C "$d" log -1 --format='%ad' --date=short)
  printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' \
    "$slug" "$head_sha" "$commits" "$an" "$ae" "$anae" "${tz_top:--}" "${tz_top_n:--}" "${tz_all% }" "$first" "$last"
  rm -rf "$d"
done < "$IN"
