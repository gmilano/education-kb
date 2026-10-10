#!/usr/bin/env bash
# freshness.sh — commit-RECENCY census over this KB's shelf addresses.
#
# WHY THIS AXIS. `Gap 376` has asked for a maintenance signal since pass 92.
# p107 answered with tag COUNT and p108 showed that inverts at the top of the
# shelf (4 468 tags, never a release). p108 answered with release IDENTITY —
# *can* you pin it. Neither answers *is it alive*. A repo can be flawless
# semver and five years dead. This reads the one figure that says so.
#
# CHANNEL. Anonymous git lane only. Measured live at pass 109:
#   git ls-remote / git fetch          rc=0
#   raw.githubusercontent.com          200
#   api.github.com                     403   (P107-A, session scoping)
#   github.com HTML + .atom feeds      403   <- NEW this pass, see P109-B
# So the commit date cannot come from an API or a feed. It comes from the
# object itself: a depth-1, blob-filtered fetch of HEAD, then `git log`.
#
# DATE DISCIPLINE (P109-C). Reads COMMITTER date (%cI), not author date (%aI).
# Author date survives rebase/cherry-pick and can be arbitrarily old on a
# commit pushed today; committer date is when this history was actually
# written. On a rebased repo the two disagree by years, and author date would
# report a live project as dormant.
#
# Output TSV: slug rc head_sha40 head_cdate head_adate age_days band
#   rc!=0 -> UNREAD. An unread row is NEVER "stale" and never zero (P1040).
set -uo pipefail
cd "$(dirname "$0")"

list="${1:-addresses.txt}"
# Reference date is an ARGUMENT, not `date` — so a test can pin it and the
# result file is reproducible.
today="${2:-$(date -u +%Y-%m-%d)}"
workroot="${P109_WORK:-${TMPDIR:-/tmp}/p109work}"

# AGE IS IN UTC CALENDAR DAYS (P109-D). An earlier draft differenced raw
# timestamps, which made the answer depend on the time of day in `today` and on
# the commit's own timezone: a commit 9 calendar days back read as 8 when
# `today` was taken as midnight. "Nine days old" is a statement about dates, so
# both sides are floored to a UTC date before differencing.
today_utc=$(date -u -d "$today" +%Y-%m-%d) || exit 2
today_epoch=$(date -u -d "${today_utc}T00:00:00Z" +%s) || exit 2

band() { # age_days -> band
  local d=$1
  if   [ "$d" -le 30  ]; then echo fresh
  elif [ "$d" -le 90  ]; then echo active
  elif [ "$d" -le 365 ]; then echo slowing
  elif [ "$d" -le 730 ]; then echo dormant
  else                        echo abandoned
  fi
}

printf 'slug\trc\thead_sha40\thead_cdate\thead_adate\tage_days\tband\n'
while IFS= read -r slug; do
  [ -n "$slug" ] || continue
  case "$slug" in \#*) continue ;; esac
  d="$workroot/$(printf '%s' "$slug" | tr '/' '_')"
  rm -rf "$d"; mkdir -p "$d"
  git init -q --bare "$d" 2>/dev/null
  # A bare `owner/repo` is resolved against github.com; anything carrying a
  # scheme is used verbatim. That second form is what lets test_p109.sh serve
  # real git repositories over file:// and exercise this exact code path with no
  # network at all.
  case "$slug" in
    *://*) url="$slug" ;;
    *)     url="https://github.com/$slug" ;;
  esac
  # No slug is ever interpolated into a string that is evaluated by a shell.
  git -C "$d" remote add origin "$url" 2>/dev/null
  GIT_TERMINAL_PROMPT=0 timeout 90 git -C "$d" -c protocol.version=2 \
      fetch -q --depth 1 --filter=blob:none origin HEAD >/dev/null 2>&1
  rc=$?
  if [ $rc -ne 0 ]; then
    # Partial clone is a server capability. If it is refused, retry WITHOUT the
    # filter before calling the row unread — otherwise a capability gap would be
    # misreported as an unreachable repo.
    GIT_TERMINAL_PROMPT=0 timeout 90 git -C "$d" -c protocol.version=2 \
        fetch -q --depth 1 origin HEAD >/dev/null 2>&1
    rc=$?
  fi
  if [ $rc -eq 0 ]; then
    sha=$(git -C "$d" rev-parse FETCH_HEAD 2>/dev/null)
    cd_iso=$(git -C "$d" log -1 --format=%cI FETCH_HEAD 2>/dev/null)
    ad_iso=$(git -C "$d" log -1 --format=%aI FETCH_HEAD 2>/dev/null)
    if [ -n "$cd_iso" ] && [ ${#sha} -eq 40 ]; then
      ce=$(date -u -d "$(date -u -d "$cd_iso" +%Y-%m-%d)T00:00:00Z" +%s)
      age=$(( (today_epoch - ce) / 86400 ))
      # A commit dated in the future is a clock fault, not freshness. Clamp to 0
      # and keep the row readable rather than emitting a negative age.
      [ "$age" -lt 0 ] && age=0
      printf '%s\t0\t%s\t%s\t%s\t%s\t%s\n' \
        "$slug" "$sha" "$cd_iso" "$ad_iso" "$age" "$(band "$age")"
    else
      printf '%s\t90\t-\t-\t-\t-\tUNREAD\n' "$slug"
    fi
  else
    printf '%s\t%s\t-\t-\t-\t-\tUNREAD\n' "$slug" "$rc"
  fi
  rm -rf "$d"
done < "$list"
rm -rf "$workroot" 2>/dev/null
