#!/usr/bin/env bash
# test_p110.sh — offline suite for busfactor.sh.
#
# NO MOCKS. Every fixture is a REAL git repository built here and served to
# the real script over file://, so the code under test is byte-identical to
# the code that reads github.com; only the transport differs (P110_BASE).
# Runs with no network.
set -uo pipefail
cd "$(dirname "$0")"
HERE=$(pwd)
PASS=0; FAIL=0
ok()   { PASS=$((PASS+1)); printf '  ok   %s\n' "$1"; }
bad()  { FAIL=$((FAIL+1)); printf '  FAIL %s\n       want=[%s] got=[%s]\n' "$1" "$2" "$3"; }
eq()   { if [ "$2" = "$3" ]; then ok "$1"; else bad "$1" "$2" "$3"; fi; }

ROOT=$(mktemp -d); trap 'rm -rf "$ROOT"' EXIT
export P110_WORK="$ROOT/work"

# commit <repo> <author-name> <author-email> <committer-name> <committer-email> <msg>
commit() {
  local r=$1 an=$2 ae=$3 cn=$4 ce=$5 m=$6
  echo "$m $RANDOM" >> "$r/f.txt"
  git -C "$r" add -A
  GIT_AUTHOR_NAME="$an" GIT_AUTHOR_EMAIL="$ae" \
  GIT_COMMITTER_NAME="$cn" GIT_COMMITTER_EMAIL="$ce" \
    git -C "$r" commit -q -m "$m"
}
# newrepo <name> [seed-author-name] [seed-author-email]
# The seed author is parameterised because the ROOT commit can never be a
# merge commit, so a fixture that needs a window with no HUMAN commits must be
# able to make its root a bot too (F8).
newrepo() {
  local r="$ROOT/$1"; mkdir -p "$r"; git init -q -b main "$r"
  local sn="${2:-seed}" se="${3:-seed@x}"
  git -C "$r" config user.name t; git -C "$r" config user.email t@t
  echo "$1" > "$r/f.txt"; git -C "$r" add -A
  GIT_AUTHOR_NAME="$sn" GIT_AUTHOR_EMAIL="$se" \
  GIT_COMMITTER_NAME="$sn" GIT_COMMITTER_EMAIL="$se" \
    git -C "$r" commit -q -m seed
  echo "$r"
}
# field <tsv> <slug> <1-based col>
field() { awk -F'\t' -v s="$2" -v c="$3" '$1==s{print $c}' "$1"; }

run() { # run <listfile> [extra env already exported]
  P110_BASE="file://$ROOT" ./busfactor.sh "$1"
}

echo "== fixtures =="

# ---- F1 pr-merge: 3 contributors by PR, maintainer merges (P110-A) --------
R=$(newrepo pr-merge)
for who in a b c; do
  git -C "$R" checkout -q -b "feat-$who" main
  commit "$R" "Dev $who" "$who@ex.org" "Dev $who" "$who@ex.org" "work $who"
  commit "$R" "Dev $who" "$who@ex.org" "Dev $who" "$who@ex.org" "work2 $who"
  git -C "$R" checkout -q main
  GIT_AUTHOR_NAME=Maint GIT_AUTHOR_EMAIL=maint@ex.org \
  GIT_COMMITTER_NAME=Maint GIT_COMMITTER_EMAIL=maint@ex.org \
    git -C "$R" merge -q --no-ff -m "Merge PR $who" "feat-$who"
done
# main now: 1 seed + 6 contributor commits + 3 merge commits by Maint

# ---- F2 squash: author varies, committer always the maintainer (P110-B) ---
R=$(newrepo squash)
for who in a b c d e; do
  commit "$R" "Dev $who" "$who@ex.org" "Maint" "maint@ex.org" "squashed $who"
  commit "$R" "Dev $who" "$who@ex.org" "Maint" "maint@ex.org" "squashed2 $who"
done

# ---- F3 botty: a bot out-commits the humans (P110-C) ----------------------
R=$(newrepo botty)
for i in 1 2 3 4 5 6 7 8; do
  commit "$R" "dependabot[bot]" "49699333+dependabot[bot]@users.noreply.github.com" \
               "GitHub" "noreply@github.com" "bump dep $i"
done
commit "$R" "Real Human" "human@ex.org" "Real Human" "human@ex.org" "actual fix"
commit "$R" "Real Human" "human@ex.org" "Real Human" "human@ex.org" "actual fix 2"

# ---- F4 privacy: real humans on users.noreply addresses (P110-F) ---------
R=$(newrepo privacy)
for who in 111+alice 222+bob 333+carol; do
  n=${who#*+}
  commit "$R" "$n" "${who}@users.noreply.github.com" "$n" "${who}@users.noreply.github.com" "p $n"
  commit "$R" "$n" "${who}@users.noreply.github.com" "$n" "${who}@users.noreply.github.com" "p2 $n"
done

# ---- F5 solo: genuinely one person ---------------------------------------
R=$(newrepo solo)
for i in 1 2 3 4 5; do
  commit "$R" "Only One" "one@ex.org" "Only One" "one@ex.org" "c$i"
done

# ---- F6 multimail: ONE human, three addresses, one name (P110-E) ---------
R=$(newrepo multimail)
for e in sam@home.net sam@work.com sam@uni.edu; do
  commit "$R" "Sam Smith" "$e" "Sam Smith" "$e" "from $e"
  commit "$R" "Sam Smith" "$e" "Sam Smith" "$e" "from2 $e"
done

# ---- F7 mergeonly: window contains only merge commits --------------------
R=$(newrepo mergeonly)
git -C "$R" checkout -q -b side main
commit "$R" "S" "s@ex.org" "S" "s@ex.org" "side work"
git -C "$R" checkout -q main
GIT_AUTHOR_NAME=M GIT_AUTHOR_EMAIL=m@ex.org GIT_COMMITTER_NAME=M GIT_COMMITTER_EMAIL=m@ex.org \
  git -C "$R" merge -q --no-ff -m "Merge side" side

# ---- F8 botonly: every commit in the window is a bot ---------------------
R=$(newrepo botonly "renovate[bot]" "bot@renovateapp.com")
for i in 1 2 3; do
  commit "$R" "renovate[bot]" "bot@renovateapp.com" "renovate[bot]" "bot@renovateapp.com" "r$i"
done

# ---- F9 caseemail: same address, different case (P110-E) -----------------
R=$(newrepo caseemail)
commit "$R" "Kay" "Kay@Ex.ORG" "Kay" "Kay@Ex.ORG" "upper"
commit "$R" "Kay" "kay@ex.org" "Kay" "kay@ex.org" "lower"
commit "$R" "Kay" "KAY@EX.ORG" "Kay" "KAY@EX.ORG" "allcaps"

printf 'pr-merge\nsquash\nbotty\nprivacy\nsolo\nmultimail\nmergeonly\nbotonly\ncaseemail\n' > "$ROOT/list.txt"
printf 'does-not-exist-%s\n' "$RANDOM" > "$ROOT/missing.txt"

echo "== A. no-merges mode (the reported mode) =="
OUT="$ROOT/out.tsv"; run "$ROOT/list.txt" > "$OUT"
eq "header is the 10-column contract" \
   "slug rc commits_read bots_stripped authors_email authors_name top_author_share bus_factor committer_bus_factor band" \
   "$(head -1 "$OUT" | tr '\t' ' ')"
eq "every fixture produced exactly one row" 9 "$(($(wc -l < "$OUT")-1))"

# F1 (P110-A): merges excluded -> the 3 devs dominate, Maint contributes none
eq "F1 pr-merge commits_read excludes the 3 merges" 7 "$(field "$OUT" pr-merge 3)"
eq "F1 pr-merge authors are the 3 devs + seed"      4 "$(field "$OUT" pr-merge 5)"
eq "F1 pr-merge bus_factor counts real writers"     2 "$(field "$OUT" pr-merge 8)"
eq "F1 pr-merge band"                           pair "$(field "$OUT" pr-merge 10)"

# F2 (P110-B): author bench is 5, committer bench is 1
eq "F2 squash author bus_factor sees 5 writers"     3 "$(field "$OUT" squash 8)"
eq "F2 squash committer bus_factor collapses to 1"  1 "$(field "$OUT" squash 9)"
eq "F2 squash authors_email"                        6 "$(field "$OUT" squash 5)"
eq "F2 squash band from AUTHOR axis"            small "$(field "$OUT" squash 10)"

# F3 (P110-C): bot stripped, human exposed as solo
eq "F3 botty stripped all 8 bot commits"            8 "$(field "$OUT" botty 4)"
eq "F3 botty counts only human commits"             3 "$(field "$OUT" botty 3)"
eq "F3 botty exposes the solo human"                1 "$(field "$OUT" botty 8)"
eq "F3 botty band"                               solo "$(field "$OUT" botty 10)"

# F4 (P110-F): privacy addresses are humans, NOT bots
eq "F4 privacy stripped nothing"                    0 "$(field "$OUT" privacy 4)"
eq "F4 privacy kept all 3 humans + seed"            4 "$(field "$OUT" privacy 5)"
eq "F4 privacy read all 7 commits"                  7 "$(field "$OUT" privacy 3)"
eq "F4 privacy band is not solo"                 pair "$(field "$OUT" privacy 10)"

# F5 solo
eq "F5 solo bus_factor"                             1 "$(field "$OUT" solo 8)"
eq "F5 solo band"                                solo "$(field "$OUT" solo 10)"
eq "F5 solo top share is the majority"              1 "$([ "$(field "$OUT" solo 7)" -ge 50 ] && echo 1)"

# F6 (P110-E): 3 emails, 2 names -> email count OVERSTATES the bench
eq "F6 multimail authors_email overstates"          4 "$(field "$OUT" multimail 5)"
eq "F6 multimail authors_name is the truth"         2 "$(field "$OUT" multimail 6)"
eq "F6 multimail names < emails is detectable"      1 \
   "$([ "$(field "$OUT" multimail 6)" -lt "$(field "$OUT" multimail 5)" ] && echo 1)"

# F7 (P110-A, the core case): a history whose only main-line commit is a merge.
# The ROOT commit of a git repo can never be a merge, so the EMPTY band is
# unreachable for any repo that fetches at all -- it stays in the code as a
# guard, and this fixture asserts the behaviour that DOES occur: the merge
# commit is dropped, the work it merged is kept, and the merger -- who wrote
# no code -- is not counted as an author.
eq "F7 mergeonly rc is 0 (it WAS read)"             0 "$(field "$OUT" mergeonly 2)"
eq "F7 mergeonly keeps seed + merged work, drops the merge" 2 "$(field "$OUT" mergeonly 3)"
eq "F7 mergeonly does NOT count the merger as an author" 2 "$(field "$OUT" mergeonly 5)"

# F8: bot-only window
eq "F8 botonly band"                          BOTONLY "$(field "$OUT" botonly 10)"
eq "F8 botonly strips the root bot commit too"       4 "$(field "$OUT" botonly 4)"
eq "F8 botonly bus_factor is blank not 1"          "" "$(field "$OUT" botonly 8)"

# F9 (P110-E): case folding
eq "F9 caseemail folds 3 spellings to 1 author"     2 "$(field "$OUT" caseemail 5)"
eq "F9 caseemail band"                           solo "$(field "$OUT" caseemail 10)"

echo "== B. P1040: an unreadable row is UNREAD, never zero =="
OUT2="$ROOT/out2.tsv"; run "$ROOT/missing.txt" > "$OUT2"
S=$(awk -F'\t' 'NR==2{print $1}' "$OUT2")
eq "missing repo rc=1"                              1 "$(field "$OUT2" "$S" 2)"
eq "missing repo band=UNREAD"                  UNREAD "$(field "$OUT2" "$S" 10)"
eq "missing repo commits_read is BLANK not 0"      "" "$(field "$OUT2" "$S" 3)"
eq "missing repo bus_factor is BLANK not 1"        "" "$(field "$OUT2" "$S" 8)"

echo "== C. P110-A, measured: merge mode must bias toward concentration =="
OUT3="$ROOT/out3.tsv"; P110_MERGES=1 run "$ROOT/list.txt" > "$OUT3"
eq "merge mode counts the 3 merge commits" 10 "$(field "$OUT3" pr-merge 3)"
eq "merge mode invents Maint as an author"  5 "$(field "$OUT3" pr-merge 5)"
# THE POINT, stated correctly. An earlier draft of this suite asserted that
# merge mode always reads MORE concentrated. That is FALSE, and this shelf
# disproves it in both directions: on moodle/moodle (real, pass 110) merge
# mode took bus_factor 9 -> 5, understating the bench by four; on this
# fixture it takes 2 -> 3, OVERstating it by one. Both are wrong, because a
# merge commit is not authorship -- it inflates the merger's share (which
# concentrates) AND adds the merger as a distinct author (which disperses),
# and which effect wins depends on the shape of the history. So the testable
# claim is not a direction, it is that the figure is CORRUPTED and that the
# corruption is visible.
B_no=$(field "$OUT" pr-merge 8); B_yes=$(field "$OUT3" pr-merge 8)
eq "merge mode changes the answer at all" 1 "$([ "$B_yes" != "$B_no" ] && echo 1)"
eq "merge mode credits a merger who wrote no code" 1 \
   "$([ "$(field "$OUT3" pr-merge 5)" -gt "$(field "$OUT" pr-merge 5)" ] && echo 1)"
eq "no-merge mode is the one that excludes the merger" 4 "$(field "$OUT" pr-merge 5)"
eq "merge mode invents the merger on F7 too" 3 "$(field "$OUT3" mergeonly 5)"

echo "== D. determinism and depth =="
OUT4="$ROOT/out4.tsv"; run "$ROOT/list.txt" > "$OUT4"
eq "two runs agree byte for byte" "" "$(diff "$OUT" "$OUT4")"
OUT5="$ROOT/out5.tsv"; P110_DEPTH=2 run "$ROOT/list.txt" > "$OUT5"
eq "depth=2 reads no more than depth=200 on solo" 1 \
   "$([ "$(field "$OUT5" solo 3)" -le "$(field "$OUT" solo 3)" ] && echo 1)"
eq "depth is honoured (solo window shrinks)" 1 \
   "$([ "$(field "$OUT5" solo 3)" -lt 5 ] && echo 1)"

echo "== E. comment/blank handling in the address list =="
printf '# a comment\n\nsolo\n' > "$ROOT/list2.txt"
OUT6="$ROOT/out6.tsv"; run "$ROOT/list2.txt" > "$OUT6"
eq "comments and blanks are skipped" 1 "$(($(wc -l < "$OUT6")-1))"

echo
printf '%s passed / %s failed\n' "$PASS" "$FAIL"
[ "$FAIL" -eq 0 ]
