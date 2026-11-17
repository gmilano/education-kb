#!/bin/bash
out=cands.tsv
: > "$out"
get() {
  local q="$1"
  gh api -X GET search/repositories -f q="$q stars:>5" -f per_page=10 2>/dev/null | python3 -c '
import sys,json
d=json.load(sys.stdin)
for i in d.get("items",[]):
    lic=(i.get("license") or {}).get("spdx_id","NONE")
    print("\t".join([i["full_name"],str(i["stargazers_count"]),str(i["forks_count"]),lic,(i.get("language") or "-"),(i.get("pushed_at") or "-")[:10],(i.get("description") or "")[:160].replace("\t"," ")]))
'
  sleep 2
}
for q in 'EXANI' 'Ceneval' 'ICFES' '"Saber Pro"' '"examen de admisión"' '"examen de ingreso"'; do
  echo "### $q" >> "$out"
  get "$q" >> "$out"
done
cat "$out"
