#!/bin/bash
for Q in "$@"; do
  N=$(gh api -X GET search/repositories -f q="$Q" -f per_page=1 2>/dev/null | python3 -I -c "import json,sys; print(json.load(sys.stdin).get('total_count','ERR'))" 2>/dev/null)
  printf "  %-52s %s\n" "$Q" "$N"
done
