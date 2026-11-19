#!/usr/bin/env bash
# p917 leg runner: records total_count + items for each query shape.
set -uo pipefail
OUTL="$1"; OUTH="$2"; shift 2
printf 'leg_id\tquery\ttotal_count\thttp\n' > "$OUTL"
printf 'leg_id\tslug\tstars\tspdx\tpushed_at\tdescription\n' > "$OUTH"
i=0
while IFS=$'\t' read -r lid q; do
  [ -z "${lid:-}" ] && continue
  i=$((i+1))
  resp=$(gh api -X GET search/repositories -f q="$q" -f per_page=25 -f sort=stars 2>/dev/null)
  if [ -z "$resp" ]; then
    printf '%s\t%s\tERR\tERR\n' "$lid" "$q" >> "$OUTL"; sleep 3; continue
  fi
  tc=$(printf '%s' "$resp" | python3 -I -c 'import sys,json; print(json.load(sys.stdin).get("total_count","ERR"))' 2>/dev/null)
  printf '%s\t%s\t%s\t200\n' "$lid" "$q" "$tc" >> "$OUTL"
  printf '%s' "$resp" | python3 -I -c '
import sys,json
lid=sys.argv[1]
try: d=json.load(sys.stdin)
except Exception: sys.exit(0)
for it in d.get("items",[]):
    lic=(it.get("license") or {}).get("spdx_id") or "NONE"
    desc=(it.get("description") or "").replace("\t"," ").replace("\n"," ")[:160]
    print("\t".join([lid,it.get("full_name",""),str(it.get("stargazers_count",0)),lic,(it.get("pushed_at") or "")[:10],desc]))
' "$lid" >> "$OUTH"
  sleep 3
done
