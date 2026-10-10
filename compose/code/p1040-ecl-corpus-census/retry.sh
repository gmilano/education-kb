#!/usr/bin/env bash
# p1040 limb B retry -- re-probe ONLY the rows limb B lost to the channel.
# Gap 388: a throttle or a dropped tunnel publishes as a negative unless the
# negative is re-probed. The retry is scoped to the lost rows so an agreeing
# re-measurement of the rest is not mistaken for new evidence (P1038).
set -u
cd "$(dirname "$0")"
TMP=$(mktemp -d); trap 'rm -rf "$TMP"' EXIT
fixed=0; still=0

# types
awk -F'\t' 'NR>1 && $2 !~ /^[0-9]+$/ {print $1}' result.types-packagist.2026-10-10.tsv > "$TMP/t"
while read -r t; do
  [ -n "${t:-}" ] || continue
  for attempt in 1 2 3; do
    code=$(curl -sS --max-time 40 -o "$TMP/l" -w '%{http_code}' \
            "https://packagist.org/packages/list.json?type=$t" 2>/dev/null) || code=000
    [ "$code" = "200" ] && break
    sleep 3
  done
  if [ "$code" = "200" ]; then
    n=$(python3 -I -c "import json;print(len(json.load(open('$TMP/l')).get('packageNames',[])))")
    python3 -I -c "
import json
for p in json.load(open('$TMP/l')).get('packageNames',[]): print('$t\t'+p)
" >> "$TMP/newpkgs"
    sed -i "s#^${t}\t.*#${t}\t${n}#" result.types-packagist.2026-10-10.tsv
    fixed=$((fixed+1)); printf 'RECOVERED type %s -> %s\n' "$t" "$n"
  else
    still=$((still+1)); printf 'STILL LOST type %s -> %s\n' "$t" "$code"
  fi
done < "$TMP/t"

# packages that failed, plus any newly discovered by a recovered type
awk -F'\t' 'NR>1 && ($3 ~ /^HTTP-/ || $3=="PARSE-ERR") {print $1"\t"$2}' \
  result.packages-packagist.2026-10-10.tsv > "$TMP/p"
[ -f "$TMP/newpkgs" ] && cat "$TMP/newpkgs" >> "$TMP/p"
sort -u "$TMP/p" -o "$TMP/p"

while IFS=$'\t' read -r t p; do
  [ -n "${p:-}" ] || continue
  for attempt in 1 2 3; do
    code=$(curl -sS --max-time 40 -o "$TMP/m" -w '%{http_code}' \
            "https://repo.packagist.org/p2/${p}.json" 2>/dev/null) || code=000
    [ "$code" = "200" ] && break
    sleep 3
  done
  if [ "$code" = "200" ]; then
    row=$(python3 -I -c "
import json
d=json.load(open('$TMP/m'))
vs=d.get('packages',{}).get('$p') or []
if not vs: print('$t\t$p\tNO-VERSIONS\t-\t-')
else:
    v=vs[0]; lic=v.get('license') or []
    print('\t'.join(['$t','$p','+'.join(lic) if lic else 'NO-LICENCE-FIELD',
                     v.get('type') or '-', (v.get('source') or {}).get('url') or '-']))
")
    grep -qP "^\Q${t}\E\t\Q${p}\E\t" result.packages-packagist.2026-10-10.tsv \
      && python3 -I -c "
import re,io
path='result.packages-packagist.2026-10-10.tsv'
lines=open(path).read().split('\n')
out=[]
for L in lines:
    f=L.split('\t')
    if len(f)>2 and f[0]=='$t' and f[1]=='$p': out.append('''$row''')
    else: out.append(L)
open(path,'w').write('\n'.join(out))
" \
      || printf '%s\n' "$row" >> result.packages-packagist.2026-10-10.tsv
    fixed=$((fixed+1))
  else
    still=$((still+1)); printf 'STILL LOST pkg %s -> %s\n' "$p" "$code"
  fi
done < "$TMP/p"

printf 'retry: recovered=%d still_lost=%d\n' "$fixed" "$still" >&2
