#!/bin/bash
CAN=/home/user/education-kb/evidence/canonical
norm(){ # operative body: cut appendix, drop copyright line, normalise
  sed -e '/APPENDIX: How to apply/,$d' -e '/How to Apply These Terms/,$d' "$1" \
  | grep -vi '^[[:space:]]*\(copyright\|Copyright (c)\)' \
  | tr 'A-Z' 'a-z' | tr -cs 'a-z0-9' '\n' | grep -v '^$'
}
printf "repo\tpinned_sha\tpath\thttp\tbytes\tspdx\tverdict\tword_delta\n"
while IFS=$'\t' read -r repo ref; do
  sha=$(timeout 90 git ls-remote "https://github.com/$repo" "$ref" 2>/dev/null | awk '{print $1}' | head -1)
  [ -z "$sha" ] && { printf "%s\t-\t-\tNO_REF\t-\t-\t-\t-\n" "$repo"; continue; }
  got=0
  for p in LICENSE LICENSE.md LICENSE.txt; do
    code=$(curl -s -o /tmp/L -w "%{http_code}" "https://raw.githubusercontent.com/$repo/$sha/$p")
    [ "$code" = "200" ] && { got=1; break; }
  done
  [ $got -eq 0 ] && { printf "%s\t%s\t-\tNO_GRANT\t-\t-\t-\t-\n" "$repo" "${sha:0:12}"; continue; }
  b=$(wc -c </tmp/L)
  if   grep -qi "Apache License" /tmp/L && grep -qi "Version 2.0" /tmp/L; then s=Apache-2.0; c=$CAN/Apache-2.0.txt
  elif grep -qi "Permission is hereby granted, free of charge" /tmp/L; then s=MIT; c=$CAN/MIT.txt
  elif grep -qi "Elastic License" /tmp/L; then s=Elastic-2.0; c=""
  else s=SPLIT-or-OTHER; c=""; fi
  if [ -n "$c" ] && [ -f "$c" ]; then
    norm /tmp/L > /tmp/a; norm "$c" > /tmp/b
    if diff -q /tmp/a /tmp/b >/dev/null; then v="IDENTICAL"; d=0
    else v="DEVIANT"; d=$(( $(wc -l </tmp/a) - $(wc -l </tmp/b) )); fi
  else v="NOT-GRADEABLE(abstain)"; d="-"; fi
  printf "%s\t%s\t%s\t200\t%s\t%s\t%s\t%s\n" "$repo" "${sha:0:12}" "$p" "$b" "$s" "$v" "$d"
done
