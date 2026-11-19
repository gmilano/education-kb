#!/usr/bin/env bash
set -uo pipefail
OUT="$1"; IN="$2"
printf 'repo\tstars\tspdx\tpushed_at\tarchived\n' > "$OUT"
mapfile -t S < "$IN"
for ((i=0;i<${#S[@]};i+=10)); do
  q=""; for s in "${S[@]:i:10}"; do q="$q repo:$s"; done
  gh api -X GET search/repositories -f q="$q" -f per_page=30 2>/dev/null | python3 -I -c '
import sys,json
try: d=json.load(sys.stdin)
except Exception: sys.exit()
for it in d.get("items",[]):
    lic=(it.get("license") or {}).get("spdx_id") or "NONE"
    print("\t".join([it.get("full_name",""),str(it.get("stargazers_count",0)),lic,(it.get("pushed_at") or "")[:10],str(it.get("archived",False))]))
' >> "$OUT"
  sleep 3
done
