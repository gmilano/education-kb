#!/bin/bash
# byte-read licence payloads via raw.githubusercontent
REPOS="operepo/ope UnlockedLabs/UnlockEdv2 BloomBooks/BloomDesktop UstadMobile/UstadMobile open-learning-exchange/planet digitalgreenorg/FarmStack"
NAMES="LICENSE LICENSE.md LICENSE.txt LICENCE COPYING LICENSE-MIT license"
for r in $REPOS; do
  for br in main master develop; do
    ok=0
    for n in $NAMES; do
      u="https://raw.githubusercontent.com/$r/$br/$n"
      code=$(curl -sS -o /tmp/p.bin -w "%{http_code}" "$u" 2>/dev/null)
      if [ "$code" = "200" ]; then
        sz=$(stat -c %s /tmp/p.bin)
        sha=$(sha256sum /tmp/p.bin | cut -c1-12)
        title=$(head -3 /tmp/p.bin | tr -s ' \t\n' ' ' | cut -c1-90)
        printf "%-34s %-8s %-14s %6s B  %s  | %s\n" "$r" "$br" "$n" "$sz" "$sha" "$title"
        ok=1
      fi
    done
    [ $ok = 1 ] && break
  done
done
