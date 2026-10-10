#!/usr/bin/env bash
# validate.sh — believe the new channel only after it reproduces a known one.
#
# p107 recorded a full 40-char HEAD sha for every shelf address from
# `git ls-remote` (a REF read). p109 reads HEAD by FETCHING THE OBJECT and then
# asking git for its committer date — a different operation over the same lane.
# The two should agree. There are exactly three licit reasons to differ, and
# every one of them is checked against evidence rather than assumed:
#
#   1. a push landed between the two runs      -> p109 age MUST be 0
#   2. P109-E: p107's head_sha40 fell back to refs/heads/main then
#      refs/heads/master, so for a repo whose DEFAULT branch is neither it
#      recorded a legacy branch tip. Confirmed per-row against defbranch.tsv,
#      which reads the default branch from the remote HEAD symref.
#   3. p107 had no baseline at all ("-") -> nothing to compare
#
# Anything else is UNEXPLAINED and means this census is not trustworthy.
set -uo pipefail
cd "$(dirname "$0")"
p107=../p107-git-lane-census/result.2026-10-10.tsv
p109=${1:-result.2026-10-10.tsv}
defb=${2:-defbranch.2026-10-10.tsv}
for f in "$p107" "$p109" "$defb"; do
  [ -r "$f" ] || { echo "missing $f" >&2; exit 2; }
done

awk -F'\t' '
  # 1st file: p107 baseline shas
  FNR==NR { if (FNR>1 && $6 ~ /^[0-9a-f]{40}$/) old[$1]=$6; next }
  # 2nd file: default branches
  FILENAME==ARGV[2] { if (FNR>1 && $2==0) db[$1]=$3; next }
  # 3rd file: this pass
  FNR==1 { next }
  {
    slug=$1; rc=$2; sha=$3; age=$6
    if (rc!=0)          { unread++; next }
    if (!(slug in old)) { nobase++; next }
    if (sha==old[slug]) { agree++;  next }
    if (age==0)         { pushed++; next }
    d = (slug in db) ? db[slug] : "?"
    if (d!="main" && d!="master" && d!="?") {
      p109e++; printf "  P109-E  %-52s default=%-18s age=%s\n", slug, d, age > "/dev/stderr"
      next
    }
    bad++
    printf "  UNEXPLAINED  %-46s p107=%s p109=%s age=%s\n", slug, substr(old[slug],1,12), substr(sha,1,12), age > "/dev/stderr"
  }
  END {
    printf "compared against p107 head_sha40\n"
    printf "  agree (identical sha)            %3d\n", agree
    printf "  differ, age=0 (push since p107)  %3d  explained\n", pushed
    printf "  differ, P109-E default-branch    %3d  explained\n", p109e
    printf "  no p107 baseline (\"-\")           %3d  explained\n", nobase
    printf "  UNEXPLAINED                      %3d  <- must be 0\n", bad
    printf "  unread this pass                 %3d\n", unread
    printf "  ----\n  total                            %3d\n", agree+pushed+p109e+nobase+bad+unread
    exit (bad>0)
  }
' "$p107" "$defb" "$p109"
