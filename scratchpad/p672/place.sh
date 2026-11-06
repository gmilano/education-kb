#!/bin/bash
# 667-G1: placement on search/users, which is THREE-VALUED and actually
# discriminates: 422 = login unsearchable, 0 = exists but no match, >=1 = placed.
# 667-G2: the location field is FREE TEXT, so probe BOTH spellings -- a 0 on one
# spelling is not absence (portabilis answers Brasil not Brazil; psiagoleal the
# reverse). p668: throttle, the endpoint caps at 30/min and an exhausted quota is
# indistinguishable from an absent owner unless you read the body.
set -u
probe() {
  local owner="$1" loc="$2"
  local body code
  body=$(gh api -X GET search/users -f q="user:$owner location:$loc" 2>&1)
  if echo "$body" | grep -q '"total_count"'; then
    echo "$body" | python3 -I -c 'import sys,json;print(json.load(sys.stdin)["total_count"])'
  else
    echo "ERR"
  fi
  sleep 2.5
}
printf 'owner\tbase_searchable\tprobe\tresult\n'
for owner in "$@"; do
  base=$(gh api -X GET search/users -f q="user:$owner" --jq '.total_count' 2>/dev/null || echo ERR)
  printf '%s\tbase=%s\t-\t-\n' "$owner" "$base"
  sleep 2.5
  for loc in "United States" "USA" "China" "Beijing" "Portugal" "Lisbon" "Bangladesh" "Indonesia" "India"; do
    r=$(probe "$owner" "$loc")
    [ "$r" != "0" ] && printf '%s\t%s\t%s\t%s\n' "$owner" "$base" "$loc" "$r"
  done
done
