#!/bin/bash
OUT=sweep2.tsv; : > $OUT; : > sweep2.log
mapfile -t QS < queries2.txt
for q in "${QS[@]}"; do
  [ -z "$q" ] && continue
  enc=$(python3 -c "import urllib.parse,sys;print(urllib.parse.quote(sys.argv[1]))" "$q" < /dev/null)
  code=$(curl -s -w '%{http_code}' -o resp2.json "https://api.github.com/search/repositories?q=${enc}&sort=stars&order=desc&per_page=30" < /dev/null)
  tc=$(python3 -c "import json;d=json.load(open('resp2.json'));print(d.get('total_count','ERR'))" < /dev/null 2>/dev/null)
  printf '%s\t%s\t%s\n' "$code" "$q" "$tc" >> sweep2.log
  if [ "$code" = "200" ]; then
    python3 parse.py "$q" resp2.json >> $OUT
  fi
  sleep 7
done
