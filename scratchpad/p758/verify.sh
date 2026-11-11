#!/bin/bash
# p758 verifier. Instruments: existence/stars/licence-index via search channel (T418/T521);
# payload bytes via raw.githubusercontent.com at HEAD (Gap 261); path set per Gap 265 + Gap 748-D;
# classifier scans PAST a leading copyright block (ACTION p757-F).
PATHS="LICENSE LICENSE.md LICENSE.txt LICENCE LICENCE.md license license.txt licence COPYING COPYING.txt copying.txt COPYING.LESSER LICENSE-APACHE LICENSE-MIT licenses/LICENSE legal/LICENSE LICENSE.rst"
for slug in "$@"; do
  o=${slug%%/*}; n=${slug##*/}
  meta=$(gh api -X GET search/repositories -f q="repo:$slug fork:true" 2>/dev/null | python3 -I -c "
import json,sys
try: d=json.load(sys.stdin)
except Exception: print('SEARCHERR||||'); raise SystemExit
if not d.get('total_count'): print('ABSENT||||'); raise SystemExit
i=d['items'][0]
print('%s|%s|%s|%s|%s|%s'%(i['full_name'],i['stargazers_count'],(i.get('license') or {}).get('spdx_id'),i['default_branch'],i['pushed_at'][:10],'ARCHIVED' if i['archived'] else 'live'))
")
  full=$(cut -d'|' -f1 <<<"$meta")
  if [ "$full" = "ABSENT" ] || [ "$full" = "SEARCHERR" ]; then
     rawcode=$(curl -s -o /dev/null -m 25 -w "%{http_code}" "https://raw.githubusercontent.com/$slug/HEAD/README.md")
     printf "%s\tSEARCH=%s\tRAW_README=%s\n" "$slug" "$full" "$rawcode"; continue
  fi
  got=""
  for p in $PATHS; do
    body=$(curl -s -m 25 "https://raw.githubusercontent.com/$o/$n/HEAD/$p")
    code=$(curl -s -o /dev/null -m 25 -w "%{http_code}" "https://raw.githubusercontent.com/$o/$n/HEAD/$p")
    [ "$code" != "200" ] && continue
    len=$(printf '%s' "$body" | wc -c); sha=$(printf '%s' "$body" | sha256sum | cut -c1-12)
    # classifier: skip leading copyright/blank lines, then read the first substantive line
    title=$(printf '%s' "$body" | grep -viE '^\s*$|^\s*copyright|^\s*\(c\)|^\s*all rights reserved' | head -3 | tr '\n' ' ' | cut -c1-90)
    got="$p|$len|$sha|$title"; break
  done
  printf "%s\tSTARS=%s\tINDEX=%s\tBRANCH=%s\tPUSHED=%s\t%s\tPAYLOAD=%s\n" \
    "$full" "$(cut -d'|' -f2 <<<"$meta")" "$(cut -d'|' -f3 <<<"$meta")" "$(cut -d'|' -f4 <<<"$meta")" \
    "$(cut -d'|' -f5 <<<"$meta")" "$(cut -d'|' -f6 <<<"$meta")" "${got:-NO_GRANT_AT_18_PATHS}"
done
