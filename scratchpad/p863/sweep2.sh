#!/bin/bash
out=sweep2.tsv; : > "$out"
run() {
  local q="$1"
  tot=$(gh api -X GET search/repositories -f q="$q" -f per_page=1 2>/dev/null | python3 -c 'import sys,json;print(json.load(sys.stdin).get("total_count","ERR"))' 2>/dev/null); sleep 2
  echo "### $q  total=$tot" | tee -a "$out"
  gh api -X GET search/repositories -f q="$q stars:>5" -f per_page=8 2>/dev/null | python3 -c '
import sys,json
d=json.load(sys.stdin)
print("  stars>5 total:",d.get("total_count"))
for i in d.get("items",[]):
    lic=(i.get("license") or {}).get("spdx_id","NONE")
    print("  "+"\t".join([i["full_name"],str(i["stargazers_count"]),lic,(i.get("pushed_at") or "-")[:10],(i.get("description") or "")[:110].replace("\t"," ")]))
' | tee -a "$out"
  sleep 2
}
run '"banco de preguntas"'
run 'reactivos examen'
run '"opción múltiple"'
run '"planeación didáctica"'
run '"guía de estudio" examen'
