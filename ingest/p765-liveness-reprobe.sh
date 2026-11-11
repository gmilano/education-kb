#!/bin/bash
: > "$2"
while read -r a; do
  [ -z "$a" ] && continue
  r=$(gh api -X GET search/repositories -f q="repo:$a" -f per_page=1 2>&1)
  if echo "$r" | grep -q '"total_count":1'; then cls=LIVE_RETRY
  elif echo "$r" | grep -q 'Validation Failed'; then cls=422_ABSENT
  elif echo "$r" | grep -q '"total_count":0'; then cls=200_UNINDEXED
  else cls=UNKNOWN; fi
  printf "%s\t%s\n" "$a" "$cls" >> "$2"
  sleep 0.7
done < "$1"
echo DONE >&2
