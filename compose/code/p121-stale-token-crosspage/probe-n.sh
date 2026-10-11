#!/usr/bin/env bash
# P121 ACTION N. Full 22-path grant probe (p120's path list verbatim) plus the
# README BADGE axis: a shields.io licence badge whose link target 404s.
set -u
PATHS="LICENSE LICENSE.md LICENSE.txt LICENCE LICENCE.md license license.md license.txt
LICENSE-CODIGO.md LICENSE-DADOS.md LICENSE-CODE.md LICENSE-DATA.md COPYING COPYING.txt
COPYRIGHT NOTICE LICENSE.rst LICENSE-MIT LICENSE-APACHE DESCRIPTION docs/License.txt .github/LICENSE"
while IFS=$'\t' read -r slug branch; do
  [ -z "${slug:-}" ] && continue
  found=""; n=0
  for p in $PATHS; do
    n=$((n+1))
    code=$(curl -sS -o /tmp/p121n.body -w '%{http_code}' --max-time 20 \
      "https://raw.githubusercontent.com/$slug/$branch/$p" 2>/dev/null || echo 000)
    if [ "$code" = "200" ]; then
      t=$(head -c 2500 /tmp/p121n.body | grep -m1 -oiE 'GNU AFFERO GENERAL PUBLIC LICENSE|GNU GENERAL PUBLIC LICENSE|GNU LESSER GENERAL PUBLIC|Apache License|MIT License|BSD [0-9]-Clause|Mozilla Public License|CC0 1\.0|Creative Commons' || echo '')
      if [ -n "$t" ]; then found="$p:$t"; break; fi
    fi
  done
  # README badge axis
  badge="-"; btarget="-"; bcode="-"
  rc=$(curl -sS -o /tmp/p121n.readme -w '%{http_code}' --max-time 20 \
     "https://raw.githubusercontent.com/$slug/$branch/README.md" 2>/dev/null || echo 000)
  if [ "$rc" = "200" ]; then
    badge=$(grep -m1 -oiE '!\[[^]]*[Ll]icen[sc]e[^]]*\]\([^)]*\)' /tmp/p121n.readme || echo '-')
    btarget=$(grep -m1 -oiE '\[!\[[^]]*[Ll]icen[sc]e[^]]*\]\([^)]*\)\]\(([^)]*)\)' /tmp/p121n.readme \
              | sed -E 's/.*\]\(([^)]*)\)$/\1/' || echo '-')
    [ -z "$badge" ] && badge="-"; [ -z "$btarget" ] && btarget="-"
    if [ "$btarget" != "-" ]; then
      case "$btarget" in http*) u="$btarget";; *) u="https://raw.githubusercontent.com/$slug/$branch/${btarget#./}";; esac
      bcode=$(curl -sS -o /dev/null -w '%{http_code}' --max-time 20 "$u" 2>/dev/null || echo 000)
    fi
  fi
  if [ -n "$found" ]; then
    printf '%s\t%s\tGRANTED\t%s\tbadge=%s\tbadge_target=%s\tbadge_http=%s\n' "$slug" "$branch" "$found" "${badge:0:40}" "$btarget" "$bcode"
  else
    printf '%s\t%s\tNO-GRANT-FOUND\t%d paths probed\tbadge=%s\tbadge_target=%s\tbadge_http=%s\n' "$slug" "$branch" "$n" "${badge:0:40}" "$btarget" "$bcode"
  fi
done
