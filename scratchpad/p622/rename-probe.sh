#!/usr/bin/env bash
# p622: the rename / stale-address instrument 621-R asked for (622-E).
# Two addresses whose ls-remote HEAD shas are IDENTICAL are ONE repository under two names.
# ls-remote PRESENT + channel B 422/0  =>  NOT CITABLE AS CANONICAL.
export GIT_TERMINAL_PROMPT=0
for slug in "$@"; do
  r=$(timeout 35 git ls-remote --symref "https://github.com/$slug" HEAD 2>&1)
  if echo "$r" | grep -q "could not read Username"; then echo -e "$slug\tDEAD\t-\t-"; continue; fi
  br=$(echo "$r" | sed -n 's|^ref: refs/heads/\([^\t]*\).*|\1|p' | head -1)
  sha=$(echo "$r" | awk '/HEAD$/ && $1 ~ /^[0-9a-f]{40}$/{print substr($1,1,12); exit}')
  tc=$(timeout 45 gh api -X GET search/repositories -f q="repo:$slug" --jq '.total_count' 2>/dev/null)
  [ -z "$tc" ] && tc=422
  if [ "$tc" = "1" ]; then cls=CANONICAL; else cls=NOT-CITABLE-AS-CANONICAL; fi
  echo -e "$slug\t$cls\t$br\t$sha\tB=$tc"
done
