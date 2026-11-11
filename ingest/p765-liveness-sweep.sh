#!/bin/bash
# batched liveness sweep: 10 repo: qualifiers per search call; missing from result = dead/renamed
SD="$1"; IN="$2"; OUT="$3"
: > "$OUT"
total=$(wc -l < "$IN")
i=0
while read -r batch; do
  q=""
  for a in $batch; do q="$q repo:$a"; done
  res=$(gh api -X GET search/repositories -f q="${q# }" -f per_page=30 2>/dev/null \
        | python3 -I -c 'import sys,json
try: d=json.load(sys.stdin)
except Exception: sys.exit(1)
for it in d.get("items",[]): print(it["full_name"])' )
  rc=$?
  for a in $batch; do
    if [ $rc -ne 0 ]; then
      echo -e "$a\tBATCHERR" >> "$OUT"
    elif echo "$res" | grep -qix -- "$a"; then
      echo -e "$a\tLIVE" >> "$OUT"
    else
      echo -e "$a\tMISSING" >> "$OUT"
    fi
  done
  i=$((i+10))
  [ $((i % 500)) -eq 0 ] && echo "progress $i / $total" >&2
  sleep 0.8
done < <(xargs -n 10 < "$IN" | sed 's/^/ /')
echo "DONE $(wc -l < "$OUT")" >&2
