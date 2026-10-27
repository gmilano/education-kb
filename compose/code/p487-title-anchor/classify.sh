#!/bin/bash
# p487 defect fix. A whole-body GNU grep is UNSOUND IN BOTH DIRECTIONS:
#   - GPLv3's closing paragraph recommends the LGPL  (p450's finding)
#   - GPL-2.0's PREAMBLE names the Library/Lesser GPL (p487's finding)
# p450 "fixed" the first by testing "gnu lesser" FIRST. That ordering is what
# mis-grades GPL-2.0. The sound anchor is the TITLE BLOCK -- p455's anchor,
# the one region of a payload a preamble cannot reach.
classify() {
  f="$1"
  title=$(grep -v '^[[:space:]]*$' "$f" | head -3 | tr 'A-Z' 'a-z' | tr -s ' \n' ' ')
  body=$(tr 'A-Z' 'a-z' < "$f")
  case "$title" in
    *"affero general public"*) echo "AGPL$(ver "$title")"; return;;
    *"lesser general public"*) echo "LGPL$(ver "$title")"; return;;
    *"library general public"*) echo "LGPL$(ver "$title")"; return;;
    *"general public license"*) echo "GPL$(ver "$title")"; return;;
    *"apache license"*)        echo "Apache$(ver "$title")"; return;;
    *"mit license"*)           echo "MIT"; return;;
    *"mozilla public"*)        echo "MPL$(ver "$title")"; return;;
    *"creative commons"*)      echo "CC"; return;;
  esac
  case "$body" in
    *"permission is hereby granted, free of charge"*) echo "MIT";;
    *"redistributions of source code"*) echo "BSD";;
    *) echo "UNCLASSIFIED";;
  esac
}
ver() { case "$1" in *"version 3"*) echo "-3.0";; *"version 2.1"*) echo "-2.1";; *"version 2"*) echo "-2.0";; *) echo "";; esac; }
printf 'file\tOLD_whole_body_rule\tNEW_title_anchor\tverdict\n'
for f in "$@"; do
  low=$(tr 'A-Z' 'a-z' < "$f")
  if   printf '%s' "$low" | grep -q 'gnu affero'; then old=AGPL
  elif printf '%s' "$low" | grep -q 'gnu lesser';  then old=LGPL
  elif printf '%s' "$low" | grep -q 'gnu general public'; then old=GPL
  else old=other; fi
  new=$(classify "$f")
  [ "$old" = "${new%%-*}" ] && v="agree" || v="🔴 DISAGREE"
  printf '%s\t%s\t%s\t%s\n' "$(basename $f)" "$old" "$new" "$v"
done
