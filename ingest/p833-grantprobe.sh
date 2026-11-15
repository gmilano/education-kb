#!/usr/bin/env bash
# p833 grant probe: resolves heads FIRST (ACTION p832-B), then probes licence filenames.
# Prints the probed ref set inside every verdict so an absence is falsifiable.
set -u
slug="$1"
dir="${GRANTPROBE_OUT:-$(mktemp -d)}"; mkdir -p "$dir"
heads=$(git ls-remote --heads "https://github.com/$slug" 2>/dev/null | awk '{sub("refs/heads/","",$2); print $2}')
if [ -z "$heads" ]; then echo "$slug :: EMPTY-REF-SET (dead or unreachable address) :: refs=[]"; exit 0; fi
# prefer common defaults, then all heads, capped
ordered=$(printf '%s\n' $heads | awk '{print ($0=="main"?0:($0=="master"?1:($0=="dev"?2:3)))"\t"$0}' | sort -s -k1,1n | cut -f2 | head -6)
names="LICENSE LICENSE.md LICENSE.txt LICENCE LICENCE.md license license.md license.txt COPYING COPYING.txt"
for br in $ordered; do
  for fn in $names; do
    out="$dir/$(echo "$slug" | tr '/' '%')-$br-$fn"
    code=$(curl -sS --max-time 20 -o "$out" -w '%{http_code}' "https://raw.githubusercontent.com/$slug/$br/$fn" 2>/dev/null)
    if [ "$code" = "200" ]; then
      printf '%s :: GRANT at %s/%s :: bytes=%s sha256=%s :: head="%s" :: refs=[%s]\n' \
        "$slug" "$br" "$fn" "$(wc -c <"$out")" "$(sha256sum "$out" | cut -c1-12)" \
        "$(head -2 "$out" | tr '\n' ' ' | sed 's/  */ /g' | cut -c1-70)" "$(printf '%s ' $ordered)"
      exit 0
    fi
    rm -f "$out"
  done
done
printf '%s :: NO-GRANT-AT-ROOT :: probed %s filenames x %s refs :: refs=[%s]\n' \
  "$slug" "$(printf '%s\n' $names | wc -l)" "$(printf '%s\n' $ordered | wc -l)" "$(printf '%s ' $ordered)"
