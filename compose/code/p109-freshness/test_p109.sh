#!/usr/bin/env bash
# test_p109.sh — OFFLINE tests for freshness.sh.
# No network: every remote is a real local git repository served over file://,
# so the actual fetch/log code path is exercised, not a mock of it.
set -uo pipefail
cd "$(dirname "$0")"
PASS=0; FAIL=0
ok(){ PASS=$((PASS+1)); printf '  ok   %s\n' "$1"; }
no(){ FAIL=$((FAIL+1)); printf '  FAIL %s — got [%s] want [%s]\n' "$1" "$2" "$3"; }
eq(){ [ "$2" = "$3" ] && ok "$1" || no "$1" "$2" "$3"; }

T=$(mktemp -d); trap 'rm -rf "$T"' EXIT
export GIT_CONFIG_GLOBAL=/dev/null GIT_CONFIG_SYSTEM=/dev/null
export GIT_AUTHOR_NAME=t GIT_AUTHOR_EMAIL=t@t GIT_COMMITTER_NAME=t GIT_COMMITTER_EMAIL=t@t

# mkrepo <name> <committer-date> [author-date]
mkrepo(){
  local n=$1
  local cd_=$2
  local ad_=${3:-$2}
  local r="$T/$n"
  git init -q "$r"; : > "$r/f"; git -C "$r" add f
  GIT_COMMITTER_DATE="$cd_" GIT_AUTHOR_DATE="$ad_" \
    git -C "$r" commit -q -m c
  echo "$r"
}

# run <today> <slug-lines...>  -> writes $T/out.tsv
run(){
  local today=$1; shift
  printf '%s\n' "$@" > "$T/list.txt"
  P109_WORK="$T/work" ./freshness.sh "$T/list.txt" "$today" > "$T/out.tsv" 2>"$T/err.txt"
  echo $?
}
col(){ awk -F'\t' -v s="$2" '$1==s{print $'"$3"'}' "$T/out.tsv"; }

echo "== dates and ages =="
R=$(mkrepo fresh  "2026-10-01T12:00:00+0000")
rc=$(run 2026-10-10 "file://$R")
eq "exit 0"                      "$rc" "0"
eq "age_days = 9"                "$(col x "file://$R" 6)" "9"
eq "band fresh"                  "$(col x "file://$R" 7)" "fresh"
eq "rc column 0"                 "$(col x "file://$R" 2)" "0"
eq "sha is 40 chars"             "$(col x "file://$R" 3 | wc -c | tr -d ' ')" "41"
eq "header present"              "$(head -1 "$T/out.tsv" | cut -f1,6,7)" "$(printf 'slug\tage_days\tband')"
eq "7 columns on data row"       "$(sed -n 2p "$T/out.tsv" | awk -F'\t' '{print NF}')" "7"

echo "== band boundaries are exact =="
for pair in "30 fresh" "31 active" "90 active" "91 slowing" "365 slowing" "366 dormant" "730 dormant" "731 abandoned"; do
  set -- $pair; days=$1; want=$2
  d=$(date -u -d "2026-10-10 -$days days" +%Y-%m-%dT12:00:00+0000)
  B=$(mkrepo "b$days" "$d")
  run 2026-10-10T12:00:00 "file://$B" >/dev/null
  eq "age $days -> $want" "$(col x "file://$B" 7)" "$want"
done

echo "== P109-C: committer date is reported, not author date =="
# A rebased/cherry-picked commit: authored 2019, committed yesterday.
# Reading author date would report a live repo as abandoned.
RB=$(mkrepo rebased "2026-10-09T12:00:00+0000" "2019-01-01T12:00:00+0000")
run 2026-10-10 "file://$RB" >/dev/null
eq "age from committer date"     "$(col x "file://$RB" 6)" "1"
eq "band active-or-fresh"        "$(col x "file://$RB" 7)" "fresh"
eq "author date still RECORDED"  "$(col x "file://$RB" 5 | cut -c1-4)" "2019"
ad=$(col x "file://$RB" 5 | cut -c1-4); cdy=$(col x "file://$RB" 4 | cut -c1-4)
eq "trap fires: author/committer differ by 7y" "$(( cdy - ad ))" "7"

echo "== P1040: an unread row is UNREAD, never stale =="
run 2026-10-10 "file://$T/does-not-exist-at-all" >/dev/null
eq "band UNREAD"                 "$(col x "file://$T/does-not-exist-at-all" 7)" "UNREAD"
eq "rc nonzero"                  "$([ "$(col x "file://$T/does-not-exist-at-all" 2)" != 0 ] && echo y)" "y"
eq "age is - not a number"       "$(col x "file://$T/does-not-exist-at-all" 6)" "-"
eq "NOT banded abandoned"        "$(grep -c abandoned "$T/out.tsv")" "0"

echo "== a future-dated commit is a clock fault, not freshness =="
FUT=$(mkrepo future "2027-01-01T12:00:00+0000")
run 2026-10-10 "file://$FUT" >/dev/null
eq "age clamped to 0"            "$(col x "file://$FUT" 6)" "0"
eq "band fresh"                  "$(col x "file://$FUT" 7)" "fresh"
eq "no negative age emitted"     "$(awk -F'\t' '$6 ~ /^-[0-9]/' "$T/out.tsv" | wc -l | tr -d ' ')" "0"

echo "== list hygiene =="
A=$(mkrepo h1 "2026-10-05T12:00:00+0000")
printf '%s\n\n# a comment line\n%s\n' "file://$A" "file://$A" > "$T/list2.txt"
P109_WORK="$T/work" ./freshness.sh "$T/list2.txt" 2026-10-10 > "$T/out.tsv" 2>/dev/null
eq "blank + comment skipped"     "$(tail -n +2 "$T/out.tsv" | wc -l | tr -d ' ')" "2"
eq "no row for the comment"      "$(grep -c '^#' "$T/out.tsv")" "0"

echo "== the real address list is well formed =="
eq "296 addresses"               "$(grep -c . addresses.txt)" "296"
eq "every line is owner/repo"    "$(grep -vcE '^[A-Za-z0-9._-]+/[A-Za-z0-9._-]+$' addresses.txt)" "0"
eq "no case-duplicates (P108-F)" "$(tr 'A-Z' 'a-z' < addresses.txt | sort | uniq -d | wc -l | tr -d ' ')" "0"
eq "no trailing whitespace"      "$(grep -c '[[:space:]]$' addresses.txt)" "0"

echo
printf '%s passed / %s failed\n' "$PASS" "$FAIL"
[ "$FAIL" -eq 0 ]
