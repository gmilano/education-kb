#!/bin/bash
# p779 instrument: produce a FALSIFIABLE licence row for one repository.
# Emits, on both channels: claim-channel spdx_id/stars/pushed (search/repositories),
# ref-channel default branch and HEAD (git ls-remote --symref), and body-channel
# filename/bytes/sha256-12/title-line (raw at the resolved branch, never `HEAD`,
# so the row names the tree it was read from). gate-refs exists because rows
# without branch-and-HEAD cannot be re-read; this writes them with it.
row() {
  slug="$1"; owner="${slug%%/*}"; name="${slug##*/}"
  cj=$(timeout 60 gh api -X GET search/repositories -f q="repo:$slug" -f per_page=1 2>/dev/null \
    | python3 -I -c "
import sys,json
try: d=json.load(sys.stdin); i=d['items'][0]
except Exception: print('-\t-\t-'); raise SystemExit
print(((i.get('license') or {}).get('spdx_id') or 'NONE'), i.get('stargazers_count',0), (i.get('pushed_at') or '')[:10], sep='\t')")
  sym=$(timeout 60 git ls-remote --symref "https://github.com/$slug" HEAD 2>/dev/null)
  br=$(printf '%s' "$sym" | awk '/^ref:/{sub("refs/heads/","",$2); print $2; exit}')
  hd=$(printf '%s' "$sym" | awk '/HEAD$/ && $1 ~ /^[0-9a-f]{40}$/{print substr($1,1,12); exit}')
  [ -z "$br" ] && br="-"
  lf="-"; lb="0"; lh="-"; lt="-"
  for f in LICENSE LICENCE LICENSE.txt LICENSE.md LICENCE.txt COPYING LICENSE-CODE LICENSE-APACHE; do
    tmp=$(mktemp)
    code=$(timeout 30 curl -sS -o "$tmp" -w "%{http_code}" "https://raw.githubusercontent.com/$slug/$br/$f" 2>/dev/null)
    if [ "$code" = "200" ]; then
      lf="$f"; lb=$(stat -c%s "$tmp"); lh=$(sha256sum "$tmp" | cut -c1-12)
      lt=$(sed -n '1,3p' "$tmp" | tr -s ' \t\n' ' ' | sed 's/^ *//' | cut -c1-60)
      rm -f "$tmp"; break
    fi
    rm -f "$tmp"
  done
  printf "%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n" "$slug" "$cj" "$br" "$hd" "$lf" "$lb" "$lh" "$lt"
}
export -f row
for s in "$@"; do row "$s"; done
